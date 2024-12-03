---
library_name: transformers
language:
- ru
- en
---

# Релиз вихря 0.3-0.4 

Долили сильно больше данных в sft, теперь стабильнее работает json и multiturn, слегка подточили параметры претрена модели

Added a lot more data to sft, now json and multiturn work more stable on long context and hard prompts

 - [Google Colab](https://colab.research.google.com/drive/15O9LwZhVUa1LWhZa2UKr_B-KOKenJBvv#scrollTo=5EeNFU2-9ERi)
 - [GGUF](https://huggingface.co/Vikhrmodels/Vikhr-7B-instruct_0.4-GGUF)

```python


from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
model = AutoModelForCausalLM.from_pretrained("Vikhrmodels/Vikhr-7B-instruct_0.4",
                                             device_map="auto",
                                             attn_implementation="flash_attention_2",
                                             torch_dtype=torch.bfloat16)

tokenizer = AutoTokenizer.from_pretrained("Vikhrmodels/Vikhr-7B-instruct_0.4")
from transformers import  AutoTokenizer, pipeline
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
prompts = [
    "В чем разница между фруктом и овощем?",
    "Годы жизни колмагорова?"]

def test_inference(prompt):
    prompt = pipe.tokenizer.apply_chat_template([{"role": "user", "content": prompt}], tokenize=False, add_generation_prompt=True)
    print(prompt)
    outputs = pipe(prompt, max_new_tokens=512, do_sample=True, num_beams=1, temperature=0.25, top_k=50, top_p=0.98, eos_token_id=79097)
    return outputs[0]['generated_text'][len(prompt):].strip()


for prompt in prompts:
    print(f"    prompt:\n{prompt}")
    print(f"    response:\n{test_inference(prompt)}")
    print("-"*50)

```


```
@article{nikolich2024vikhr,
  title={Vikhr: The Family of Open-Source Instruction-Tuned Large Language Models for Russian},
  author={Aleksandr Nikolich and Konstantin Korolev and Artem Shelmanov},
  journal={arXiv preprint arXiv:2405.13929},
  year={2024},
  url={https://arxiv.org/pdf/2405.13929}
}
```