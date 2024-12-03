---
datasets:
- tatsu-lab/alpaca
language:
- en
---
### Model card for Alpaca-30B

This is a Llama model instruction-finetuned with LoRa for 3 epochs on the Tatsu Labs Alpaca dataset. It was trained in 8bit mode.

To run this model, you can run the following or use the following repo for [generation](https://github.com/aspctu/alpaca-lora). 

```
# Code adapted from https://github.com/tloen/alpaca-lora
import torch
from peft import PeftModel
import transformers

from transformers import LlamaTokenizer, LlamaForCausalLM, GenerationConfig

tokenizer = LlamaTokenizer.from_pretrained("decapoda-research/llama-30b-hf")

model = LlamaForCausalLM.from_pretrained(
    "decapoda-research/llama-30b-hf",
    load_in_8bit=True,
    torch_dtype=torch.float16,
    device_map="auto",
)

model = PeftModel.from_pretrained(
    model, 
    "baseten/alpaca-30b",
    torch_dtype=torch.float16
)

def generate_prompt(instruction, input=None):
    if input:
        return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{input}

### Response:"""
    else:
        return f"""Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:"""


model.eval()


def evaluate(
        instruction,
        input=None,
        temperature=0.1,
        top_p=0.75,
        top_k=40,
        num_beams=4,
        **kwargs,
):
    prompt = generate_prompt(instruction, input)
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].to(device)
    generation_config = GenerationConfig(
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        num_beams=num_beams,
        **kwargs,
    )
    with torch.no_grad():
        generation_output = model.generate(
            input_ids=input_ids,
            generation_config=generation_config,
            return_dict_in_generate=True,
            output_scores=True,
            max_new_tokens=2048,
        )
    s = generation_output.sequences[0]
    output = tokenizer.decode(s)
    return output.split("### Response:")[1].strip()
```