---
license: llama3.1
library_name: transformers
pipeline_tag: text-generation
base_model: meta-llama/Meta-Llama-3.1-8B-Instruct
language:
- en
- zh
tags:
- llama-factory
- orpo
---

> [!CAUTION]
> For optimal performance, we refrain from fine-tuning the model's identity. Thus, inquiries such as "Who are you" or "Who developed you" may yield random responses that are not necessarily accurate. 

> [!IMPORTANT]
> If you enjoy our model, please **give it a star on our Hugging Face repo** and kindly [**cite our model**](https://huggingface.co/shenzhi-wang/Llama3.1-8B-Chinese-Chat#citation). Your support means a lot to us. Thank you!


# Updates

- 🚀🚀🚀 [July 24, 2024] We now introduce [shenzhi-wang/Llama3.1-8B-Chinese-Chat](https://huggingface.co/shenzhi-wang/Llama3.1-8B-Chinese-Chat)! The training dataset contains >100K preference pairs, and it exhibits significant enhancements, especially in **roleplay**, **function calling**, and **math** capabilities!
- 🔥 We provide the official **q4_k_m, q8_0, and f16 GGUF** versions of Llama3.1-8B-Chinese-Chat-**v2.1** at https://huggingface.co/shenzhi-wang/Llama3.1-8B-Chinese-Chat/tree/main/gguf!


# Model Summary

llama3.1-8B-Chinese-Chat is an instruction-tuned language model for Chinese & English users with various abilities such as roleplaying & tool-using built upon the Meta-Llama-3.1-8B-Instruct model.

Developers: [Shenzhi Wang](https://shenzhi-wang.netlify.app)\*, [Yaowei Zheng](https://github.com/hiyouga)\*, Guoyin Wang (in.ai), Shiji Song, Gao Huang. (\*: Equal Contribution)

- License: [Llama-3.1 License](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B/blob/main/LICENSE)
- Base Model: Meta-Llama-3.1-8B-Instruct
- Model Size: 8.03B
- Context length: 128K (reported by [Meta-Llama-3.1-8B-Instruct model](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct), untested for our Chinese model)

# 1. Introduction

This is the first model specifically fine-tuned for Chinese & English users based on the [Meta-Llama-3.1-8B-Instruct model](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct). The fine-tuning algorithm used is ORPO [1].


[1] Hong, Jiwoo, Noah Lee, and James Thorne. "Reference-free Monolithic Preference Optimization with Odds Ratio." arXiv preprint arXiv:2403.07691 (2024).

Training framework: [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory).

Training details:

- epochs: 3
- learning rate: 3e-6
- learning rate scheduler type: cosine
- Warmup ratio: 0.1
- cutoff len (i.e. context length): 8192
- orpo beta (i.e. $\lambda$ in the ORPO paper): 0.05
- global batch size: 128
- fine-tuning type: full parameters
- optimizer: paged_adamw_32bit



# 2. Usage

## 2.1 Usage of Our BF16 Model

1. Please upgrade the `transformers` package to ensure it supports Llama3.1 models. The current version we are using is `4.43.0`.

2. Use the following Python script to download our BF16 model

```python
from huggingface_hub import snapshot_download
snapshot_download(repo_id="shenzhi-wang/Llama3.1-8B-Chinese-Chat", ignore_patterns=["*.gguf"])  # Download our BF16 model without downloading GGUF models.
```

3. Inference with the BF16 model

```python
import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "/Your/Local/Path/to/Llama3.1-8B-Chinese-Chat"
dtype = torch.bfloat16

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="cuda",
    torch_dtype=dtype,
)

chat = [
    {"role": "user", "content": "写一首关于机器学习的诗。"},
]
input_ids = tokenizer.apply_chat_template(
    chat, tokenize=True, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

outputs = model.generate(
    input_ids,
    max_new_tokens=8192,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
response = outputs[0][input_ids.shape[-1] :]
print(tokenizer.decode(response, skip_special_tokens=True))
```

## 2.2 Usage of Our GGUF Models

1. Download our GGUF models from the [gguf_models folder](https://huggingface.co/shenzhi-wang/Llama3.1-8B-Chinese-Chat/tree/main/gguf);
2. Use the GGUF models with [LM Studio](https://lmstudio.ai/);
3. You can also follow the instructions from https://github.com/ggerganov/llama.cpp/tree/master#usage to use gguf models.


# Citation

If our Llama3.1-8B-Chinese-Chat is helpful, please kindly cite as:

```
@misc {shenzhi_wang_2024,
	author       = { Wang, Shenzhi and Zheng, Yaowei and Wang, Guoyin and Song, Shiji and Huang, Gao },
	title        = { Llama3.1-8B-Chinese-Chat },
	year         = 2024,
	url          = { https://huggingface.co/shenzhi-wang/Llama3.1-8B-Chinese-Chat },
	doi          = { 10.57967/hf/2779 },
	publisher    = { Hugging Face }
}
```

