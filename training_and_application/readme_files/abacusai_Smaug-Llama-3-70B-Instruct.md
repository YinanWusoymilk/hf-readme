---
library_name: transformers
license: llama3
datasets:
- aqua_rat
- microsoft/orca-math-word-problems-200k
- m-a-p/CodeFeedback-Filtered-Instruction
---

# Smaug-Llama-3-70B-Instruct

### Built with Meta Llama 3


![image/png](https://cdn-uploads.huggingface.co/production/uploads/64c14f6b02e1f8f67c73bd05/ZxYuHKmU_AtuEJbGtuEBC.png)

This model was built using a new Smaug recipe  for improving performance on real world multi-turn conversations applied to 
[meta-llama/Meta-Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct).

The model outperforms Llama-3-70B-Instruct substantially, and is on par with GPT-4-Turbo, on MT-Bench (see below).

EDIT: Smaug-Llama-3-70B-Instruct is the top open source model on Arena-Hard currently! It is also nearly on par with Claude Opus - see below.

We are conducting additional benchmark evaluations and will add those when available.

### Model Description

- **Developed by:** [Abacus.AI](https://abacus.ai)
- **License:** https://llama.meta.com/llama3/license/
- **Finetuned from model:** [meta-llama/Meta-Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct).

## How to use

The prompt format is unchanged from Llama 3 70B Instruct.

### Use with transformers

See the snippet below for usage with Transformers:

```python
import transformers
import torch

model_id = "abacusai/Smaug-Llama-3-70B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user", "content": "Who are you?"},
]

prompt = pipeline.tokenizer.apply_chat_template(
		messages, 
		tokenize=False, 
		add_generation_prompt=True
)

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = pipeline(
    prompt,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.9,
)
print(outputs[0]["generated_text"][len(prompt):])
```


## Evaluation

### Arena-Hard

Score vs selected others (sourced from: (https://lmsys.org/blog/2024-04-19-arena-hard/#full-leaderboard-with-gpt-4-turbo-as-judge)). GPT-4o and Gemini-1.5-pro-latest were missing from the original blob post, and we produced those numbers from a local run using the same methodology. 

| Model | Score | 95% Confidence Interval | Average Tokens |
| :---- | ---------: | ----------: | ------: |
| GPT-4-Turbo-2024-04-09 | 82.6  | (-1.8, 1.6)  | 662 |
| GPT-4o | 78.3  | (-2.4, 2.1)  | 685 |
| Gemini-1.5-pro-latest | 72.1  | (-2.3, 2.2)  | 630 |
| Claude-3-Opus-20240229 | 60.4  | (-3.3, 2.4)  | 541 |
| **Smaug-Llama-3-70B-Instruct** | 56.7  | (-2.2, 2.6)  | 661 |
| GPT-4-0314 | 50.0  | (-0.0, 0.0)  | 423 |
| Claude-3-Sonnet-20240229 | 46.8  | (-2.1, 2.2)  | 552 |
| Llama-3-70B-Instruct | 41.1  | (-2.5, 2.4)  | 583 |
| GPT-4-0613 | 37.9  | (-2.2, 2.0)  | 354 |
| Mistral-Large-2402 | 37.7 | (-1.9, 2.6)  | 400 |
| Mixtral-8x22B-Instruct-v0.1 | 36.4  | (-2.7, 2.9)  | 430 |
| Qwen1.5-72B-Chat | 36.1 | (-2.5, 2.2)  | 474 |
| Command-R-Plus | 33.1 | (-2.1, 2.2)  | 541 |
| Mistral-Medium | 31.9  | (-2.3, 2.4)  | 485 |
| GPT-3.5-Turbo-0613 | 24.8 | (-1.6, 2.0)  | 401 |

### MT-Bench

```
########## First turn ##########
                   score
model             turn
Smaug-Llama-3-70B-Instruct         1     9.40000                                                                                                                            
GPT-4-Turbo                        1     9.37500
Meta-Llama-3-70B-Instruct          1     9.21250 
########## Second turn ##########
                   score
model             turn
Smaug-Llama-3-70B-Instruct         2     9.0125
GPT-4-Turbo                        2     9.0000
Meta-Llama-3-70B-Instruct          2     8.8000
########## Average ##########
                 score
model
Smaug-Llama-3-70B-Instruct          9.206250
GPT-4-Turbo                         9.187500
Meta-Llama-3-70B-Instruct           9.006250
```

| Model | First turn | Second Turn | Average |
| :---- | ---------: | ----------: | ------: |
| **Smaug-Llama-3-70B-Instruct**  | 9.40 | 9.01 | 9.21 |
| GPT-4-Turbo | 9.38 |  9.00 | 9.19 |
| Meta-Llama-3-70B-Instruct | 9.21 |  8.80 | 9.01 |

### OpenLLM Leaderboard Manual Evaluation

| Model | ARC  | Hellaswag | MMLU | TruthfulQA | Winogrande | GSM8K* | Average |
| :---- | ---: | ------:   | ---: | ---:       | ---:       | ---:   | ---:   |
| Smaug-Llama-3-70B-Instruct | 70.6 | 86.1 | 79.2 | 62.5 | 83.5 | 90.5 | 78.7 |
| Llama-3-70B-Instruct | 71.4 | 85.7 | 80.0 | 61.8 | 82.9 | 91.1 | 78.8 |

**GSM8K** The GSM8K numbers quoted here are computed using a recent release
of the [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness/).
The commit used by the leaderboard has a significant issue that impacts models that
tend to use `:` in their responses due to a bug in the stop word configuration for
GSM8K. The issue is covered in more detail in this
[GSM8K evaluation discussion](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard/discussions/770).
The score for both Llama-3 and this model are significantly different when evaluated
with the updated harness as the issue with stop words has been addressed.


This version of Smaug uses new techniques and new data compared to [Smaug-72B](https://huggingface.co/abacusai/Smaug-72B-v0.1), and more information will be released later on. For now, see the previous Smaug paper: https://arxiv.org/abs/2402.13228.