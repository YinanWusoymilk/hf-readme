---
language:
- it
- en
library_name: transformers
license: apache-2.0
---

# Qwen2 1.5B: Almost the Same Performance as ITALIA (iGenius) but 6 Times Smaller 🚀

### Model Overview

**Model Name:** Qwen2 1.5B Fine-tuned for Italian Language  
**Version:** 1.5b  
**Model Type:** Language Model  
**Parameter Count:** 1.5 billion  
**Language:** Italian  
**Comparable Model:** [ITALIA by iGenius](https://huggingface.co/iGeniusAI) (9 billion parameters)

### Model Description

Qwen2 1.5B is a compact language model specifically fine-tuned for the Italian language. Despite its relatively small size of 1.5 billion parameters, Qwen2 1.5B demonstrates strong performance, nearly matching the capabilities of larger models, such as the **9 billion parameter ITALIA model by iGenius**. The fine-tuning process focused on optimizing the model for various language tasks in Italian, making it highly efficient and effective for Italian language applications.

### Performance Evaluation

The performance of Qwen2 1.5B was evaluated on several benchmarks and compared against the ITALIA model. The results are as follows:

### Performance Evaluation

| Model      | Parameters | Average |  MMLU |  ARC  | HELLASWAG |
|:----------:|:----------:|:-------:|:-----:|:-----:|:---------:|
| ITALIA     |     9B     |  43.5   | 35.22 | **38.49** | **56.79** |
| Qwen2-1.5B-Ita |    1.5B    | **43.98** | **51.45** | 32.34 |  48.15   |


## How to Use

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "DeepMount00/Qwen2-1.5B-Ita"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

prompt = [{'role': 'user', 'content': """Marco ha comprato 5 scatole di cioccolatini. Ogni scatola contiene 12 cioccolatini. Ha deciso di dare 3 cioccolatini a ciascuno dei suoi 7 amici. Quanti cioccolatini gli rimarranno dopo averli distribuiti ai suoi amici?"""}]
inputs = tokenizer.apply_chat_template(
    prompt,
    add_generation_prompt=True,
    return_tensors='pt'
)
tokens = model.generate(
    inputs.to(model.device),
    max_new_tokens=1024,
    temperature=0.001,
    do_sample=True
)

print(tokenizer.decode(tokens[0], skip_special_tokens=False))
```


### Conclusion

Qwen2 1.5B demonstrates that a smaller, more efficient model can achieve performance levels comparable to much larger models. It excels in the MMLU benchmark, showing its strength in multitask language understanding. While it scores slightly lower in the ARC and HELLASWAG benchmarks, its overall performance makes it a viable option for Italian language tasks, offering a balance between efficiency and capability.