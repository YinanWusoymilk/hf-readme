---
base_model: mistralai/Mistral-7B-Instruct-v0.3
inference: false
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
quantized_by: Suparious
tags:
- 4-bit
- AWQ
- text-generation
- autotrain_compatible
- endpoints_compatible
---
# mistralai/Mistral-7B-Instruct-v0.3 AWQ

- Model creator: [mistralai](https://huggingface.co/mistralai)
- Original model: [Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)

## Model Summary

The Mistral-7B-Instruct-v0.3 Large Language Model (LLM) is an instruct fine-tuned version of the Mistral-7B-v0.3.

Mistral-7B-v0.3 has the following changes compared to [Mistral-7B-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2/edit/main/README.md)
- Extended vocabulary to 32768
- Supports v3 Tokenizer
- Supports function calling

## How to use

### Install the necessary packages

```bash
pip install --upgrade autoawq autoawq-kernels
```

### Example Python code

```python
from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer, TextStreamer

model_path = "solidrust/Mistral-7B-Instruct-v0.3-AWQ"
system_message = "You are Mistral-7B-Instruct-v0.3, incarnated as a powerful AI. You were created by mistralai."

# Load model
model = AutoAWQForCausalLM.from_quantized(model_path,
                                          fuse_layers=True)
tokenizer = AutoTokenizer.from_pretrained(model_path,
                                          trust_remote_code=True)
streamer = TextStreamer(tokenizer,
                        skip_prompt=True,
                        skip_special_tokens=True)

# Convert prompt to tokens
prompt_template = """\
<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant"""

prompt = "You're standing on the surface of the Earth. "\
        "You walk one mile south, one mile west and one mile north. "\
        "You end up exactly where you started. Where are you?"

tokens = tokenizer(prompt_template.format(system_message=system_message,prompt=prompt),
                  return_tensors='pt').input_ids.cuda()

# Generate output
generation_output = model.generate(tokens,
                                  streamer=streamer,
                                  max_new_tokens=512)
```

### About AWQ

AWQ is an efficient, accurate and blazing-fast low-bit weight quantization method, currently supporting 4-bit quantization. Compared to GPTQ, it offers faster Transformers-based inference with equivalent or better quality compared to the most commonly used GPTQ settings.

AWQ models are currently supported on Linux and Windows, with NVidia GPUs only. macOS users: please use GGUF models instead.

It is supported by:

- [Text Generation Webui](https://github.com/oobabooga/text-generation-webui) - using Loader: AutoAWQ
- [vLLM](https://github.com/vllm-project/vllm) - version 0.2.2 or later for support for all model types.
- [Hugging Face Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference)
- [Transformers](https://huggingface.co/docs/transformers) version 4.35.0 and later, from any code or client that supports Transformers
- [AutoAWQ](https://github.com/casper-hansen/AutoAWQ) - for use from Python code
