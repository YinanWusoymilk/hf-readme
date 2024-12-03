---
license: llama3.1
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
library_name: transformers
pipeline_tag: text-generation
tags:
- llama-3.1
- meta
- autogptq
---

> [!IMPORTANT]
> This repository is a community-driven quantized version of the original model [`meta-llama/Meta-Llama-3.1-70B-Instruct`](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct) which is the FP16 half-precision official version released by Meta AI.

## Model Information

The Meta Llama 3.1 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction tuned generative models in 8B, 70B and 405B sizes (text in/text out). The Llama 3.1 instruction tuned text only models (8B, 70B, 405B) are optimized for multilingual dialogue use cases and outperform many of the available open source and closed chat models on common industry benchmarks.

This repository contains [`meta-llama/Meta-Llama-3.1-70B-Instruct`](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct) quantized using [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) from FP16 down to INT4 using the GPTQ kernels performing zero-point quantization with a group size of 128.

## Model Usage

> [!NOTE]
> In order to run the inference with Llama 3.1 70B Instruct GPTQ in INT4, around 35 GiB of VRAM are needed only for loading the model checkpoint, without including the KV cache or the CUDA graphs, meaning that there should be a bit over that VRAM available.

In order to use the current quantized model, support is offered for different solutions as `transformers`, `autogptq`, or `text-generation-inference`.

### 🤗 transformers

In order to run the inference with Llama 3.1 70B Instruct GPTQ in INT4, you need to install the following packages:

```bash
pip install -q --upgrade transformers accelerate optimum
pip install -q --no-build-isolation auto-gptq
```

To run the inference on top of Llama 3.1 70B Instruct GPTQ in INT4 precision, the GPTQ model can be instantiated as any other causal language modeling model via `AutoModelForCausalLM` and run the inference normally.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
  model_id,
  torch_dtype=torch.float16,
  low_cpu_mem_usage=True,
  device_map="auto",
)

prompt = [
  {"role": "system", "content": "You are a helpful assistant, that responds as a pirate."},
  {"role": "user", "content": "What's Deep Learning?"},
]
inputs = tokenizer.apply_chat_template(
  prompt,
  tokenize=True,
  add_generation_prompt=True,
  return_tensors="pt",
  return_dict=True,
).to("cuda")

outputs = model.generate(**inputs, do_sample=True, max_new_tokens=256)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True))
```

### AutoGPTQ

In order to run the inference with Llama 3.1 70B Instruct GPTQ in INT4, you need to install the following packages:

```bash
pip install -q --upgrade transformers accelerate optimum
pip install -q --no-build-isolation auto-gptq
```

Alternatively, one may want to run that via `AutoGPTQ` even though it's built on top of 🤗 `transformers`, which is the recommended approach instead as described above.

```python
import torch
from auto_gptq import AutoGPTQForCausalLM
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoGPTQForCausalLM.from_pretrained(
  model_id,
  torch_dtype=torch.float16,
  low_cpu_mem_usage=True,
  device_map="auto",
)

prompt = [
  {"role": "system", "content": "You are a helpful assistant, that responds as a pirate."},
  {"role": "user", "content": "What's Deep Learning?"},
]
inputs = tokenizer.apply_chat_template(
  prompt,
  tokenize=True,
  add_generation_prompt=True,
  return_tensors="pt",
  return_dict=True,
).to("cuda")

outputs = model.generate(**inputs, do_sample=True, max_new_tokens=256)
print(tokenizer.batch_decode(outputs, skip_special_tokens=True))
```

The AutoGPTQ script has been adapted from [`AutoGPTQ/examples/quantization/basic_usage.py`](https://github.com/AutoGPTQ/AutoGPTQ/blob/main/examples/quantization/basic_usage.py).

### 🤗 Text Generation Inference (TGI)

To run the `text-generation-launcher` with Llama 3.1 70B Instruct GPTQ in INT4 with Marlin kernels for optimized inference speed, you will need to have Docker installed (see [installation notes](https://docs.docker.com/engine/install/)) and the `huggingface_hub` Python package as you need to login to the Hugging Face Hub.

```bash
pip install -q --upgrade huggingface_hub
huggingface-cli login
```

Then you just need to run the TGI v2.2.0 (or higher) Docker container as follows:

```bash
docker run --gpus all --shm-size 1g -ti -p 8080:80 \
  -v hf_cache:/data \
  -e MODEL_ID=hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4 \
  -e NUM_SHARD=4 \
  -e QUANTIZE=gptq \
  -e HF_TOKEN=$(cat ~/.cache/huggingface/token) \
  -e MAX_INPUT_LENGTH=4000 \
  -e MAX_TOTAL_TOKENS=4096 \
  ghcr.io/huggingface/text-generation-inference:2.2.0
```

> [!NOTE]
> TGI will expose different endpoints, to see all the endpoints available check [TGI OpenAPI Specification](https://huggingface.github.io/text-generation-inference/#/).

To send request to the deployed TGI endpoint compatible with [OpenAI OpenAPI specification](https://github.com/openai/openai-openapi) i.e. `/v1/chat/completions`:

```bash
curl 0.0.0.0:8080/v1/chat/completions \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "tgi",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "What is Deep Learning?"
      }
    ],
    "max_tokens": 128
  }'
```

Or programatically via the `huggingface_hub` Python client as follows:

```python
import os
from huggingface_hub import InferenceClient

client = InferenceClient(base_url="http://0.0.0.0:8080", api_key=os.getenv("HF_TOKEN", "-"))

chat_completion = client.chat.completions.create(
  model="hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Deep Learning?"},
  ],
  max_tokens=128,
)
```

Alternatively, the OpenAI Python client can also be used (see [installation notes](https://github.com/openai/openai-python?tab=readme-ov-file#installation)) as follows:

```python
import os
from openai import OpenAI

client = OpenAI(base_url="http://0.0.0.0:8080/v1", api_key=os.getenv("OPENAI_API_KEY", "-"))

chat_completion = client.chat.completions.create(
  model="tgi",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Deep Learning?"},
  ],
  max_tokens=128,
)
```

### vLLM

To run vLLM with Llama 3.1 70B Instruct GPTQ in INT4, you will need to have Docker installed (see [installation notes](https://docs.docker.com/engine/install/)) and run the latest vLLM Docker container as follows:

```bash
docker run --runtime nvidia --gpus all --ipc=host -p 8000:8000 \
  -v hf_cache:/root/.cache/huggingface \
  vllm/vllm-openai:latest \
  --model hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4 \
  --quantization gptq_marlin \
  --tensor-parallel-size 4 \
  --max-model-len 4096
```

To send request to the deployed vLLM endpoint compatible with [OpenAI OpenAPI specification](https://github.com/openai/openai-openapi) i.e. `/v1/chat/completions`:

```bash
curl 0.0.0.0:8000/v1/chat/completions \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "What is Deep Learning?"
      }
    ],
    "max_tokens": 128
  }'
```

Or programatically via the `openai` Python client (see [installation notes](https://github.com/openai/openai-python?tab=readme-ov-file#installation)) as follows:

```python
import os
from openai import OpenAI

client = OpenAI(base_url="http://0.0.0.0:8000/v1", api_key=os.getenv("VLLM_API_KEY", "-"))

chat_completion = client.chat.completions.create(
  model="hugging-quants/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Deep Learning?"},
  ],
  max_tokens=128,
)
```

## Quantization Reproduction

> [!NOTE]
> In order to quantize Llama 3.1 70B Instruct using AutoGPTQ, you will need to use an instance with at least enough CPU RAM to fit the whole model i.e. ~140GiB, and an NVIDIA GPU with 40GiB of VRAM to quantize it.

In order to quantize Llama 3.1 70B Instruct with GPTQ in INT4, you need to install the following packages:

```bash
pip install -q --upgrade transformers accelerate optimum
pip install -q --no-build-isolation auto-gptq
```

Then run the following script, adapted from [`AutoGPTQ/examples/quantization/basic_usage.py`](https://github.com/AutoGPTQ/AutoGPTQ/blob/main/examples/quantization/basic_usage.py).

```python
import random

import numpy as np
import torch

from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
from datasets import load_dataset
from transformers import AutoTokenizer

pretrained_model_dir = "meta-llama/Meta-Llama-3.1-70B-Instruct"
quantized_model_dir = "meta-llama/Meta-Llama-3.1-70B-Instruct-GPTQ-INT4"

print("Loading tokenizer, dataset, and tokenizing the dataset...")
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_dir, use_fast=True)
dataset = load_dataset("Salesforce/wikitext", "wikitext-2-raw-v1", split="train")
encodings = tokenizer("\n\n".join(dataset["text"]), return_tensors="pt")

print("Setting random seeds...")
random.seed(0)
np.random.seed(0)
torch.random.manual_seed(0)

print("Setting calibration samples...")
nsamples = 128
seqlen = 2048
calibration_samples = []
for _ in range(nsamples):
    i = random.randint(0, encodings.input_ids.shape[1] - seqlen - 1)
    j = i + seqlen
    input_ids = encodings.input_ids[:, i:j]
    attention_mask = torch.ones_like(input_ids)
    calibration_samples.append({"input_ids": input_ids, "attention_mask": attention_mask})

quantize_config = BaseQuantizeConfig(
    bits=4,  # quantize model to 4-bit
    group_size=128,  # it is recommended to set the value to 128
    desc_act=True,  # set to False can significantly speed up inference but the perplexity may slightly bad
    sym=True,  # using symmetric quantization so that the range is symmetric allowing the value 0 to be precisely represented (can provide speedups)
    damp_percent=0.1,  # see https://github.com/AutoGPTQ/AutoGPTQ/issues/196
)

# load un-quantized model, by default, the model will always be loaded into CPU memory
print("Load unquantized model...")
model = AutoGPTQForCausalLM.from_pretrained(pretrained_model_dir, quantize_config)

# quantize model, the examples should be list of dict whose keys can only be "input_ids" and "attention_mask"
print("Quantize model with calibration samples...")
model.quantize(calibration_samples)

# save quantized model using safetensors
model.save_quantized(quantized_model_dir, use_safetensors=True)
```