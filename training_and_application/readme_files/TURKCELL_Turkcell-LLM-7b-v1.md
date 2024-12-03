---
license: apache-2.0
language:
- tr
---

<img src="https://huggingface.co/TURKCELL/Turkcell-LLM-7b-v1/resolve/main/icon.jpeg"
alt="Turkcell LLM" width="300"/>

# Turkcell-LLM-7b-v1

This model is an extended version of a Mistral-based Large Language Model (LLM) for Turkish. It was trained on a cleaned Turkish raw dataset containing 5 billion tokens. The training process involved using the DORA method initially. Following this, we utilized Turkish instruction sets created from various open-source and internal resources for fine-tuning with the LORA method.

## Model Details

- **Base Model**: Mistral 7B based LLM
- **Tokenizer Extension**: Specifically extended for Turkish
- **Training Dataset**: Cleaned Turkish raw data with 5 billion tokens, custom Turkish instruction sets
- **Training Method**: Initially with DORA, followed by fine-tuning with LORA

### DORA Configuration

- `lora_alpha`: 128
- `lora_dropout`: 0.05
- `r`: 64
- `target_modules`: "all-linear"


### LORA Fine-Tuning Configuration

- `lora_alpha`: 128
- `lora_dropout`: 0.05
- `r`: 256
- `target_modules`: "all-linear"

## Usage Examples

```python

from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("TURKCELL/Turkcell-LLM-7b-v1")
tokenizer = AutoTokenizer.from_pretrained("TURKCELL/Turkcell-LLM-7b-v1")

messages = [
    {"role": "user", "content": "Türkiye'nin başkenti neresidir?"},
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

eos_token = tokenizer("<|im_end|>",add_special_tokens=False)["input_ids"][0]

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, 
                               max_new_tokens=1024, 
                               do_sample=True, 
                               eos_token_id=eos_token)
                               
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])

