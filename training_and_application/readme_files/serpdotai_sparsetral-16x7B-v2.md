---
license: apache-2.0
datasets:
- teknium/OpenHermes-2.5
language:
- en
---
## Training
- 8x A6000s
- [Forked version of unsloth](https://github.com/serp-ai/unsloth) for efficient training
- Sequence Length: 4096
- Effective batch size: 128
- Learning Rate: 2e-5 with linear decay
- Epochs: 1
- [Base model](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) trained with QLoRA (rank 64, alpha 16) and MoE adapters/routers trained in bf16
- Num Experts: 16
- Top K: 4
- Adapter Dim: 512

## Prompt Format 
```
<|im_start|>system\n{message}<|im_end|>\n<|im_start|>user\n{message}<|im_end|>\n<|im_start|>assistant\n
```

## Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("serpdotai/sparsetral-16x7B-v2", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("serpdotai/sparsetral-16x7B-v2", device_map="auto", trust_remote_code=True).eval()

system_str = "<|im_start|>system\n{message}<|im_end|>\n"
user_str = "<|im_start|>user\n{message}<|im_end|>\n"
assistant_str = "<|im_start|>assistant\n{message}<|im_end|>\n"

def construct_prompt(messages):
    prompt = ""
    for message in messages:
        if message["from"] in ["human", "user"]:
            prompt += user_str.format(
                message=message["value"]
            )
        elif message["from"] in ["gpt", "assistant"]:
            prompt += assistant_str.format(
                message=message["value"]
            )
        elif message["from"] in ["system", "instruction"]:
            prompt += system_str.format(
                message=message["value"]
            )
        else:
            raise ValueError(
                f"Unknown message type: {message['from']}"
            )
    return prompt + "<|im_start|>assistant\n"

system = "You are a helpful assistant who will help the user to the best of their ability. If you don't know something, say \"I don't know\""
user = "Are you sentient?"

messages = [
    {"from": "system", "value": system},
    {"from": "user", "value": user},
]

prompt = construct_prompt(messages)
inputs = tokenizer(prompt, return_tensors="pt")
inputs = inputs.to(model.device)
pred = model.generate(**inputs, max_length=4096, do_sample=True, top_k=50, top_p=0.99, temperature=0.9, num_return_sequences=1)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))
```

## Other Information
Paper reference: [Parameter-Efficient Sparsity Crafting from Dense to Mixture-of-Experts for Instruction Tuning on General Tasks](https://arxiv.org/abs/2401.02731)

[Original Paper repo](https://github.com/wuhy68/Parameter-Efficient-MoE)

[Forked repo with mistral support (sparsetral)](https://github.com/serp-ai/Parameter-Efficient-MoE)

If you are interested in faster inferencing, check out our [fork of vLLM](https://github.com/serp-ai/vllm) that adds sparsetral support