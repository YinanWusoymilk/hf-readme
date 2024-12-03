---
base_model: meta-llama/Meta-Llama-3.1-8B-Instruct
library_name: transformers
language:
- en
- it
---

## Model Architecture
- **Base Model:** [Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)
- **Specialization:** Italian Language


## How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

MODEL_NAME = "DeepMount00/Llama-3.1-8b-Ita"

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16).eval()
model.to(device)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def generate_answer(prompt):
    messages = [
        {"role": "user", "content": prompt},
    ]
    model_inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(device)
    generated_ids = model.generate(model_inputs, max_new_tokens=200, do_sample=True,
                                          temperature=0.001)
    decoded = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return decoded[0]

prompt = "Come si apre un file json in python?"
answer = generate_answer(prompt)
print(answer)
```
---
## Developer
[Michele Montebovi]