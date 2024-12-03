---
title: Alpaca LoRa 7B
language: en
license: other
tags:
- alpaca
- lora
- llama
- peft
---

# Alpaca LoRa 7B

This repository contains a LLaMA-7B fine-tuned model on the [Standford Alpaca](https://github.com/tatsu-lab/stanford_alpaca) cleaned version dataset.

⚠️ **I used [LLaMA-7B-hf](https://huggingface.co/decapoda-research/llama-7b-hf) as a base model, so this model is for Research purpose only (See the [license](https://huggingface.co/decapoda-research/llama-7b-hf/blob/main/LICENSE))**

# Usage

## Creating prompt

The model was trained on the following kind of prompt:

```python
def generate_prompt(instruction: str, input_ctxt: str = None) -> str:
    if input_ctxt:
        return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{input_ctxt}

### Response:"""
    else:
        return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:"""
```

## Using the model

```python
import torch
from transformers import GenerationConfig, LlamaTokenizer, LlamaForCausalLM

tokenizer = LlamaTokenizer.from_pretrained("chainyo/alpaca-lora-7b")
model = LlamaForCausalLM.from_pretrained(
    "chainyo/alpaca-lora-7b",
    load_in_8bit=True,
    torch_dtype=torch.float16,
    device_map="auto",
)
generation_config = GenerationConfig(
    temperature=0.2,
    top_p=0.75,
    top_k=40,
    num_beams=4,
    max_new_tokens=128,
)

model.eval()
if torch.__version__ >= "2":
    model = torch.compile(model)

instruction = "What is the meaning of life?"
input_ctxt = None  # For some tasks, you can provide an input context to help the model generate a better response.

prompt = generate_prompt(instruction, input_ctxt)
input_ids = tokenizer(prompt, return_tensors="pt").input_ids
input_ids = input_ids.to(model.device)

with torch.no_grad():
    outputs = model.generate(
        input_ids=input_ids,
        generation_config=generation_config,
        return_dict_in_generate=True,
        output_scores=True,
    )

response = tokenizer.decode(outputs.sequences[0], skip_special_tokens=True)
print(response)

>>> The meaning of life is to live a life of meaning.
```