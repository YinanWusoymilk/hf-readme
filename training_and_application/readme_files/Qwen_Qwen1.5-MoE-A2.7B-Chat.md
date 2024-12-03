---
license: other
license_name: tongyi-qianwen
license_link: >-
  https://huggingface.co/Qwen/Qwen1.5-MoE-A2.7B-Chat/blob/main/LICENSE
language:
- en
pipeline_tag: text-generation
tags:
- chat
---

# Qwen1.5-MoE-A2.7B-Chat


## Introduction

Qwen1.5-MoE is a transformer-based MoE decoder-only language model pretrained on a large amount of data. 

For more details, please refer to our [blog post](https://qwenlm.github.io/blog/qwen-moe/) and [GitHub repo](https://github.com/QwenLM/Qwen1.5).

## Model Details
Qwen1.5-MoE employs Mixture of Experts (MoE) architecture, where the models are upcycled from dense language models. For instance, `Qwen1.5-MoE-A2.7B` is upcycled from `Qwen-1.8B`. It has 14.3B parameters in total and 2.7B activated parameters during runtime, while achieching comparable performance to `Qwen1.5-7B`, it only requires 25% of the training resources. We also observed that the inference speed is 1.74 times that of `Qwen1.5-7B`.

## Training details
We pretrained the models with a large amount of data, and we post-trained the models with both supervised finetuning and direct preference optimization. 

## Requirements
The code of Qwen1.5-MoE has been in the latest Hugging face transformers and we advise you to build from source with command `pip install git+https://github.com/huggingface/transformers`, or you might encounter the following error:
```
KeyError: 'qwen2_moe'.
```

## Quickstart

Here provides a code snippet with `apply_chat_template` to show you how to load the tokenizer and model and how to generate contents.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen1.5-MoE-A2.7B-Chat",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen1.5-MoE-A2.7B-Chat")

prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

For quantized models, we advise you to use the GPTQ correspondents, namely `Qwen1.5-MoE-A2.7B-Chat-GPTQ-Int4`.


## Tips

* If you encounter code switching or other bad cases, we advise you to use our provided hyper-parameters in `generation_config.json`.
* 