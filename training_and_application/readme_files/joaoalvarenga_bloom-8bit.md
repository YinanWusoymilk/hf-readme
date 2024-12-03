---
inference: false
license: bigscience-bloom-rail-1.0
language:
- ak
- ar
- as
- bm
- bn
- ca
- en
- es
- eu
- fon
- fr
- gu
- hi
- id
- ig
- ki
- kn
- lg
- ln
- ml
- mr
- ne
- nso
- ny
- or
- pa
- pt
- rn
- rw
- sn
- st
- sw
- ta
- te
- tn
- ts
- tum
- tw
- ur
- vi
- wo
- xh
- yo
- zh
- zu
pipeline_tag: text-generation
---
### Quantized bigscience/bloom with 8-bit weights

Heavily inspired by [Hivemind's GPT-J-6B with 8-bit weights](https://huggingface.co/hivemind/gpt-j-6B-8bit), this is a version of [bigscience/bloom](https://huggingface.co/bigscience/bloom) a ~176 billion parameters language model that you run and fine-tune with less memory.

Here, we also apply [LoRA (Low Rank Adaptation)](https://arxiv.org/abs/2106.09685) to reduce model size. The original version takes \~353GB memory, this version takes **\~180GB**.

Our main goal is to generate a model compressed enough to be deployed in a traditional Kubernetes cluster.

### How to fine-tune

In this [notebook](https://nbviewer.org/urls/huggingface.co/joaoalvarenga/bloom-8bit/raw/main/fine-tuning-example.ipynb) you can find an adaptation from [Hivemind's GPT-J 8-bit fine-tuning notebook](https://colab.research.google.com/drive/1ft6wQU0BhqG5PRlwgaZJv2VukKKjU4Es) to fine-tune Bloom 8-bit with a 3x NVIDIA A100 instance.

### How to use

This model can be used by adapting Bloom original implementation. This is an adaptation from [Hivemind's GPT-J 8-bit](https://nbviewer.org/urls/huggingface.co/hivemind/gpt-j-6B-8bit/raw/main/convert-gpt-j.ipynb):

```python
import transformers
import torch
import torch.nn as nn
import torch.nn.functional as F

from bitsandbytes.functional import quantize_blockwise, dequantize_blockwise
from typing import Tuple
from torch.cuda.amp import custom_fwd, custom_bwd

class FrozenBNBLinear(nn.Module):
    def __init__(self, weight, absmax, code, bias=None):
        assert isinstance(bias, nn.Parameter) or bias is None
        super().__init__()
        self.out_features, self.in_features = weight.shape
        self.register_buffer("weight", weight.requires_grad_(False))
        self.register_buffer("absmax", absmax.requires_grad_(False))
        self.register_buffer("code", code.requires_grad_(False))
        self.adapter = None
        self.bias = bias
 
    def forward(self, input):
        output = DequantizeAndLinear.apply(input, self.weight, self.absmax, self.code, self.bias)
        if self.adapter:
            output += self.adapter(input)
        return output
 
    @classmethod
    def from_linear(cls, linear: nn.Linear) -> "FrozenBNBLinear":
        weights_int8, state = quantize_blockise_lowmemory(linear.weight)
        return cls(weights_int8, *state, linear.bias)
 
    def __repr__(self):
        return f"{self.__class__.__name__}({self.in_features}, {self.out_features})"
 
 
class DequantizeAndLinear(torch.autograd.Function): 
    @staticmethod
    @custom_fwd
    def forward(ctx, input: torch.Tensor, weights_quantized: torch.ByteTensor,
                absmax: torch.FloatTensor, code: torch.FloatTensor, bias: torch.FloatTensor):
        weights_deq = dequantize_blockwise(weights_quantized, absmax=absmax, code=code)
        ctx.save_for_backward(input, weights_quantized, absmax, code)
        ctx._has_bias = bias is not None
        return F.linear(input, weights_deq, bias)
 
    @staticmethod
    @custom_bwd
    def backward(ctx, grad_output: torch.Tensor):
        assert not ctx.needs_input_grad[1] and not ctx.needs_input_grad[2] and not ctx.needs_input_grad[3]
        input, weights_quantized, absmax, code = ctx.saved_tensors
        # grad_output: [*batch, out_features]
        weights_deq = dequantize_blockwise(weights_quantized, absmax=absmax, code=code)
        grad_input = grad_output @ weights_deq
        grad_bias = grad_output.flatten(0, -2).sum(dim=0) if ctx._has_bias else None
        return grad_input, None, None, None, grad_bias
 
 
class FrozenBNBEmbedding(nn.Module):
    def __init__(self, weight, absmax, code):
        super().__init__()
        self.num_embeddings, self.embedding_dim = weight.shape
        self.register_buffer("weight", weight.requires_grad_(False))
        self.register_buffer("absmax", absmax.requires_grad_(False))
        self.register_buffer("code", code.requires_grad_(False))
        self.adapter = None
 
    def forward(self, input, **kwargs):
        with torch.no_grad():
            # note: both quantuized weights and input indices are *not* differentiable
            weight_deq = dequantize_blockwise(self.weight, absmax=self.absmax, code=self.code)
            output = F.embedding(input, weight_deq, **kwargs)
        if self.adapter:
            output += self.adapter(input)
        return output 
 
    @classmethod
    def from_embedding(cls, embedding: nn.Embedding) -> "FrozenBNBEmbedding":
        weights_int8, state = quantize_blockise_lowmemory(embedding.weight)
        return cls(weights_int8, *state)
 
    def __repr__(self):
        return f"{self.__class__.__name__}({self.num_embeddings}, {self.embedding_dim})"
 
 
def quantize_blockise_lowmemory(matrix: torch.Tensor, chunk_size: int = 2 ** 20):
    assert chunk_size % 4096 == 0
    code = None
    chunks = []
    absmaxes = []
    flat_tensor = matrix.view(-1)
    for i in range((matrix.numel() - 1) // chunk_size + 1):
        input_chunk = flat_tensor[i * chunk_size: (i + 1) * chunk_size].clone()
        quantized_chunk, (absmax_chunk, code) = quantize_blockwise(input_chunk, code=code)
        chunks.append(quantized_chunk)
        absmaxes.append(absmax_chunk)
 
    matrix_i8 = torch.cat(chunks).reshape_as(matrix)
    absmax = torch.cat(absmaxes)
    return matrix_i8, (absmax, code)
 
 
def convert_to_int8(model):
    """Convert linear and embedding modules to 8-bit with optional adapters"""
    for module in list(model.modules()):
        for name, child in module.named_children():
            if isinstance(child, nn.Linear):
                print(name, child)
                setattr( 
                    module,
                    name,
                    FrozenBNBLinear(
                        weight=torch.zeros(child.out_features, child.in_features, dtype=torch.uint8),
                        absmax=torch.zeros((child.weight.numel() - 1) // 4096 + 1),
                        code=torch.zeros(256),
                        bias=child.bias,
                    ),
                )
            elif isinstance(child, nn.Embedding):
                setattr(
                    module,
                    name,
                    FrozenBNBEmbedding(
                        weight=torch.zeros(child.num_embeddings, child.embedding_dim, dtype=torch.uint8),
                        absmax=torch.zeros((child.weight.numel() - 1) // 4096 + 1),
                        code=torch.zeros(256),
                    )
                )

class BloomBlock(transformers.models.bloom.modeling_bloom.BloomBlock):
    def __init__(self, config, layer_number=None):
        super().__init__(config, layer_number)

        convert_to_int8(self.self_attention)
        convert_to_int8(self.mlp)


class BloomModel(transformers.models.bloom.modeling_bloom.BloomModel):
    def __init__(self, config):
        super().__init__(config)
        convert_to_int8(self)
        

class BloomForCausalLM(transformers.models.bloom.modeling_bloom.BloomForCausalLM):
    def __init__(self, config):
        super().__init__(config)
        convert_to_int8(self)
        
transformers.models.bloom.modeling_bloom.BloomBlock = BloomBlock

model = BloomForCausalLM.from_pretrained('joaoalvarenga/bloom-8bit', low_cpu_mem_usage=True)
tokenizer = BloomTokenizerFast.from_pretrained('joaoalvarenga/bloom-8bit')

prompt = tokenizer("Given a table named salaries and columns id, created_at, salary, age. Creates a SQL to answer What is the average salary for 22 years old:", return_tensors='pt')
out = model.generate(**prompt, min_length=10, do_sample=True)
tokenizer.decode(out[0])
```






