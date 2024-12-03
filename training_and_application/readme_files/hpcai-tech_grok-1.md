---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
---
# Grok-1 (PyTorch Version)

This repository contains the model and weights of the **torch version** of Grok-1 open-weights model. You could find a complete example code of using the torch-version Grok-1 in [ColossalAI GitHub Repository](https://github.com/hpcaitech/ColossalAI/tree/main/examples/language/grok-1). We also applies parallelism techniques from ColossalAI framework (Tensor Parallelism for now) to accelerate the inference.


You could find the original weights released by [xAI](https://x.ai/blog) in [Hugging Face](https://huggingface.co/xai-org/grok-1) and the original model in the Grok open release [GitHub Repository](https://github.com/xai-org/grok-1/tree/main).

## Conversion

We translated the original modeling written in JAX into PyTorch version, and converted the weights by mapping tensor files with parameter keys, de-quantizing the tensors with corresponding packed scales, and save to checkpoint file with torch APIs.

A transformers-compatible version of tokenizer is contributed by [Xenova](https://huggingface.co/Xenova) and [ArthurZ](https://huggingface.co/ArthurZ).

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.set_default_dtype(torch.bfloat16)

tokenizer = AutoTokenizer.from_pretrained("hpcai-tech/grok-1", trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    "hpcai-tech/grok-1",
    trust_remote_code=True,
    device_map="auto",
    torch_dtype=torch.bfloat16,
)
model.eval()

text = "Replace this with your text"
input_ids = tokenizer(text, return_tensors="pt").input_ids
input_ids = input_ids.cuda()
attention_mask = torch.ones_like(input_ids)
generate_kwargs = {}  # Add any additional args if you want
inputs = {
    "input_ids": input_ids,
    "attention_mask": attention_mask,
    **generate_kwargs,
}
outputs = model.generate(**inputs)
print(outputs)
```


Note: A multi-GPU machine is required to test the model with the example code (For now, a 8x80G multi-GPU machine is required).
