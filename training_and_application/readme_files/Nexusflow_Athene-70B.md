---
license: other
language:
- en
library_name: transformers
tags:
- RLHF
- Nexusflow
- Athene
- Chat Model
---
# Llama3-Athene-70B

We introduce Llama3-Athene-70B, an open-weights LLM trained through RLHF based off Llama-3-70B-Instruct. Athene-70B achieves a high score on Arena-Hard-Auto, a proxy benchmark for Chatbot Arena.

- **Developed by:** The Nexusflow Team (Evan Frick\*, Peter Jin\*, Tianle Li\*, Karthik Ganesan, Jian Zhang, Jiantao Jiao and Banghua Zhu).
- **Model type:** Chat Model
- **Finetuned from model:** [Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct).
- **License**: [Nexusflow Research License](https://huggingface.co/Nexusflow/Athene-70B/blob/main/Nexusflow_Research_License.pdf)
- **Blog**: https://nexusflow.ai/blogs/athene

| Model                           | Arena-Hard |
|---------------------------------|------------| 
| Claude-3.5-Sonnet (Proprietary) |      79.3% | 
| GPT-4o (Proprietary)            |      79.2% |  
| **Athene-70B (Open)**           |      77.8% |  
| Gemini-Pro-1.5 (Proprietary)    |      72.0% | 
| Gemma-2-27B (Open)              |      57.0% |  
| Llama-3-70B (Open)              |      46.6% |  

## Usage

Athene-70B uses the same chat template as Llama-3-70B-Instruct. Below is an example simple usage using the Transformers library.

```Python
import transformers
import torch

model_id = "Nexusflow/Athene-70B"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are an Athene Noctura, you can only speak with owl sounds. Whoooo whooo."},
    {"role": "user", "content": "Whooo are you?"},
]

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|end_of_text|>")
]

outputs = pipeline(
    messages,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
print(outputs[0]["generated_text"][-1])
```

## Acknowledgment

We would like to thank the [LMSYS Organization](https://lmsys.org/) for their support of testing the model. We would like to thank Meta AI and the open source community for their efforts in providing the datasets and base models.

## Citation

```
@misc{Athene2024,
    title = {Athene-70B: Redefining the Boundaries of Post-Training for Open Models},
    url = {https://nexusflow.ai/blogs/athene},
    author = {Frick, Evan and Jin, Peter and Li, Tianle and Ganesan, Karthik and Zhang, Jian and Jiao, Jiantao and Zhu, Banghua},    
    month = {July},
    year = {2024}
}
```