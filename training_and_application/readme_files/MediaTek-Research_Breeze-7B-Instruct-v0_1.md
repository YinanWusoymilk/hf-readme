---
pipeline_tag: text-generation
license: apache-2.0
language:
- zh
- en
---

# Model Card for MediaTek Research Breeze-7B-Instruct-v0_1

MediaTek Research Breeze-7B (hereinafter referred to as Breeze-7B) is a language model family that builds on top of [Mistral-7B](https://huggingface.co/mistralai/Mistral-7B-v0.1), specifically intended for Traditional Chinese use.

[Breeze-7B-Base](https://huggingface.co/MediaTek-Research/Breeze-7B-Base-v0_1) is the base model for the Breeze-7B series. 
It is suitable for use if you have substantial fine-tuning data to tune it for your specific use case.

[Breeze-7B-Instruct](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-v0_1) derives from the base model Breeze-7B-Base, making the resulting model amenable to be used as-is for commonly seen tasks.

[Breeze-7B-Instruct-64k](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-64k-v0_1) is a slightly modified version of 
Breeze-7B-Instruct to enable a 64k-token context length. Roughly speaking, that is equivalent to 88k Traditional Chinese characters.

*Update (Feb. 21st, 2024): Breeze-7B-Instruct-64k-v0_1 has been temporarily removed from Hugging Face due to its actual performance in long context tests not meeting expectations.*

*Update (Mar. 7th, 2024): The current release version of Breeze-7B is v1.0. See [Breeze-7B-Instruct-v1_0](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-v1_0).*

The current release version of Breeze-7B is v0.1.

Practicality-wise:
- Breeze-7B-Base expands the original vocabulary with additional 30,000 Traditional Chinese tokens. With the expanded vocabulary, everything else being equal, Breeze-7B operates at twice the inference speed for Traditional Chinese to Mistral-7B and Llama 7B. [See [Inference Performance](#inference-performance).]
- Breeze-7B-Instruct can be used as is for common tasks such as Q&A, RAG, multi-round chat, and summarization.
- In particular, Breeze-7B-Instruct-64k can perform tasks at a document level, not a chapter level.


Performance-wise:
- Breeze-7B-Instruct demonstrates impressive performance in benchmarks for Traditional Chinese and English, when compared to similar sized open-source contemporaries such as Taiwan-LLM-7B/13B-chat, QWen-7B-Chat, and Yi-6B-Chat. [See [Chat Model Performance](#chat-model-performance).]


*A project by the members (in alphabetical order): Chan-Jan Hsu 許湛然, Chang-Le Liu 劉昶樂, Feng-Ting Liao 廖峰挺, Po-Chun Hsu 許博竣, Yi-Chang Chen 陳宜昌, and the supervisor Da-Shan Shiu 許大山.*

## Features

- Breeze-7B-Base-v0_1
  - Expanding the vocabulary dictionary size from 32k to 62k to better support Traditional Chinese
  - 8k-token context length
- Breeze-7B-Instruct-v0_1
  - Expanding the vocabulary dictionary size from 32k to 62k to better support Traditional Chinese 
  - 8k-token context length
  - Multi-turn dialogue (without special handling for harmfulness)
- Breeze-7B-Instruct-64k-v0_1
  - Expanding the vocabulary dictionary size from 32k to 62k to better support Traditional Chinese
  - 64k-token context length
  - Multi-turn dialogue (without special handling for harmfulness)

## Model Details

- Breeze-7B-Base-v0_1
  - Finetuned from: [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)
  - Model type: Causal decoder-only transformer language model
  - Language: English and Traditional Chinese (zh-tw)
- Breeze-7B-Instruct-v0_1
  - Finetuned from: [MediaTek-Research/Breeze-7B-Base-v0_1](https://huggingface.co/MediaTek-Research/Breeze-7B-Base-v0_1)
  - Model type: Causal decoder-only transformer language model
  - Language: English and Traditional Chinese (zh-tw)
- Breeze-7B-Instruct-64k-v0_1
  - Finetuned from: [MediaTek-Research/Breeze-7B-Instruct-v0_1](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-v0_1)
  - Model type: Causal decoder-only transformer language model
  - Language: English and Traditional Chinese (zh-tw)

## Base Model Performance

**TMMLU+**, **DRCD**, and **Table** source from [MediaTek-Research/TCEval-v2](https://huggingface.co/datasets/MediaTek-Research/TCEval-v2).
[MediaTek-Research/TCEval-v2](https://huggingface.co/datasets/MediaTek-Research/TCEval-v2) derives from [TCEval-v1](https://github.com/mtkresearch/MR-Models/tree/main/TC-Eval)
 and [ikala/tmmluplus](https://huggingface.co/datasets/ikala/tmmluplus). **MMLU** sources from [hails/mmlu_no_train](https://huggingface.co/datasets/hails/mmlu_no_train).
 We use the code revised from [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) to evaluate **TMMLU+**, **DRCD**, **Table**, and **MMLU**. All choice problems adapt the selection by the log-likelihood.


| Models                                       |        |↑ TMMLU+ (ACC) | DRCD (EM)   | Table (ACC) | MMLU (ACC) |
|----------------------------------------------|--------|--------------|-------------|-------------|------------|
|                                              |        |TC, Knowledge |TC, Reasoning|TC, Reasoning|EN, Knowledge|
|                                              |        | 5 shot       | 3 shot      | 5 shot      | 5 shot     |
| [Yi-34B](https://huggingface.co/01-ai/Yi-34B)| 34B    | 63.10        | 84.57       | 49.31  | 77.42      |
| [Qwen-14B](https://huggingface.co/01-ai/Qwen/Qwen-14B)| 14B    | 51.30        | 16.95 *     | 50.69  | 68.83      |
| [Yi-6B](https://huggingface.co/01-ai/Yi-6B) | 6B     | 49.63        | 76.61       | 34.72  | 65.35      |
| [Qwen-7B](https://huggingface.co/01-ai/Qwen/Qwen-7B)| 7B     | 42.84        | 0.0 *       | 39.58  | 61.00      |
| [**Breeze-7B-Base-v0_1**](https://huggingface.co/MediaTek-Research/Breeze-7B-Base-v0_1)       | 7B     | 40.35        | 81.13        | 28.47  | 61.63      |
| [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1)| 7B     | 36.93        | 79.27        | 27.78 | 64.89      |


\* Few-shot learning cannot effectively guide the model to generate the proper answer.


## Chat Model Performance

**TMMLU+**, **DRCD**, **Table**, and **MT-Bench-tw** source from [MediaTek-Research/TCEval-v2](https://huggingface.co/datasets/MediaTek-Research/TCEval-v2).
[MediaTek-Research/TCEval-v2](https://huggingface.co/datasets/MediaTek-Research/TCEval-v2) derives from [TCEval-v1](https://github.com/mtkresearch/MR-Models/tree/main/TC-Eval)
 and [ikala/tmmluplus](https://huggingface.co/datasets/ikala/tmmluplus). **MMLU** sources from [hails/mmlu_no_train](https://huggingface.co/datasets/hails/mmlu_no_train).
 **MT-Bench** source from [lmsys/mt_bench_human_judgments](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments).
 We use the code revised from [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) to evaluate **TMMLU+**, **DRCD**, **Table**, and **MMLU**. All choice problems adapt the selection by the log-likelihood.
 We use the code revised from [fastchat llm_judge](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) (GPT4 as judge) to evaluate **MT-Bench-tw** and **MT-Bench**.


| Models                                                                                                  |        |↑ MT-Bench-tw (Score)| TMMLU+ (ACC) | TMMLU+ (ACC) | DRCD (EM)   | Table (ACC) | MT-Bench (Score) | MMLU (ACC)  | MMLU (ACC)  | 
|---------------------------------------------------------------------------------------------------------|--------|--------------------|--------------|--------------|-------------|-------------|------------------|-------------|-------------|
|                                                                                                         |        |TC, Chat            |TC, Knowledge |TC, Knowledge |TC, Reasoning|TC, Reasoning|EN, Chat          |EN, Knowledge|EN, Knowledge|
|                                                                                                         |        |0 shot              | 0 shot       | 5 shot       | 3 shot      | 0 shot      |0 shot            |  0 shot     | 5 shot      | 
| [gpt-3.5-turbo](https://openai.com)                                                                     |        |7.1                 | 43.56        |              |             | 45.14       |7.9               |  67.09      |             |    
| [Yi-34B-Chat](https://huggingface.co/01-ai/Yi-34B-Chat)                                                 | 34B    |6.9                 | 54.87        |              |             | 36.81       |7.6               |   71.04     |             |    
| [Qwen-14B-Chat](https://huggingface.co/Qwen/Qwen-14B-Chat)                                              | 14B    |6.4                 | 48.41        |              |             | 41.67       |7.2               |    64.91    |             |    
| [**Breeze-7B-Instruct-v0_1**](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-v0_1)         | 7B     |5.7                 | 41.61        |              |             | 45.83       |7.1               |    63.26    |             |    
| [**Breeze-7B-Instruct-64k-v0_1**](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-64k-v0_1) | 7B     |5.5                 | 40.99        |              |             | 36.11       |7.1               |    63.68    |             |    
| [Qwen-7B-Chat](https://huggingface.co/Qwen/Qwen-7B-Chat)                                                | 7B     |5.4                 | 40.02        |              |             | 33.33       |6.2               |    55.94    |             |    
| [Yi-6B-Chat](https://huggingface.co/01-ai/Yi-6B-Chat)                                                   | 6B     |5.0                 | 44.79        |              |             | 25.69       |6.0               |    59.45    |             |    
| [Taiwan-LLM-13B-v2.0-chat](https://huggingface.co/yentinglin/Taiwan-LLM-13B-v2.0-chat)                  | 13B    |5.0                 | 29.47        |              |             | 23.61       |-*                |    50.50    |             |     
| [Taiwan-LLM-7B-v2.1-chat](https://huggingface.co/yentinglin/Taiwan-LLM-7B-v2.1-chat)                    | 7B     |4.2                 | 28.08        |              |             | 31.25       | -*               |    42.72    |             |    

\* Taiwan-LLM models responds to multi-turn questions (English) in Traditional Chinese.


| Details on MT-Bench-tw (0 shot):<br/>Models         | STEM    |Extraction|Reasoning| Math   | Coding  | Roleplay| Writing |Humanities|↑ AVG   |
|-----------------------------------------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| gpt-3.5-turbo                                       |  7.8    |  6.1    |   5.1   |   6.4   |  6.2    |   8.7   |   7.4   |   9.3   |   7.1   |
| Yi-34B-Chat                                         |  9.0    |  4.8    |   5.7   |   4.0   |  4.7    |   8.5   |   8.7   |   9.8   |   6.9   |
| Qwen-14B-Chat                                       |  7.6    |  5.7    |   4.5   |   4.2   |  5.3    |   7.5   |   7.3   |   9.1   |   6.4   |
| **Breeze-7B-Instruct-v0_1**                         |  6.5    |  5.6    |   3.9   |   3.6   |  4.3    |   6.9   |   5.7   |   9.3   |   5.7   |
| **Breeze-7B-Instruct-64k-v0_1**                     |  6.1    |  5.3    |   3.7   |   2.9   |  4.2    |   7.0   |   6.7   |   8.3   |   5.5   |
| Qwen-7B-Chat                                        |  6.6    |  4.5    |   4.8   |   2.9   |  3.6    |   6.2   |   6.8   |   8.2   |   5.4   |
| Yi-6B-Chat                                          |  7.3    |  2.7    |   3.1   |   3.3   |  2.3    |   7.2   |   5.2   |   8.8   |   5.0   |
| Taiwan-LLM-13B-v2.0-chat                            |  6.1    |  3.4    |   4.1   |   2.3   |  3.1    |   7.4   |   6.6   |   6.8   |   5.0   |
| Taiwan-LLM-7B-v2.1-chat                             |  5.2    |  2.6    |   2.3   |   1.2   |  3.4    |   6.6   |   5.7   |   6.8   |   4.2   |


| Details on TMMLU+ (0 shot):<br/>Model               | STEM         | Social Science | Humanities | Other      | ↑ AVG   |
|-----------------------------------------------------|--------------|----------------|------------|------------|---------|
| Yi-34B-Chat                                         | 47.65        | 64.25          | 52.73      | 54.91      | 54.87   |
| Qwen-14B-Chat                                       | 43.83        | 55.00          | 48.55      | 46.22      | 48.41   |
| Yi-6B-Chat                                          | 37.80        | 51.74          | 45.36      | 44.25      | 44.79   |
| gpt-3.5-turbo                                       | 41.58        | 48.52          | 40.96      | 43.18      | 43.56   |
| **Breeze-7B-Instruct-v0_1**                         | 37.41        | 46.81          | 42.06      | 40.16      | 41.61   |
| **Breeze-7B-Instruct-64k-v0_1**                     | 37.88        | 46.35          | 40.31      | 39.40      | 40.99   |
| Qwen-7B-Chat                                        | 35.44        | 46.22          | 38.35      | 40.06      | 40.02   |
| Taiwan-LLM-13B-v2.0-chat                            | 27.74        | 33.69          | 27.03      | 29.43      | 29.47   |
| Taiwan-LLM-7B-v2.1-chat                             | 25.58        | 31.76          | 27.36      | 27.61      | 28.08   |



## Inference Performance
In this test, we use the first 700 characters of the [web article](https://health.udn.com/health/story/5976/7699252?from=udn_ch1005_main_index) as the input and ask the model to write the same article again.
All inferences run on 2 RTX A6000 GPUs (using `vllm`, with a tensor-parallel size of 2).

| Models                                                             | ↓ Inference Time (sec)|Estimated Max Input Length (Char)|
|--------------------------------------------------------------------|-------------------|--------------------------|
| Yi-6B-Chat                                                         |   10.62  |   5.2k                |
| **Breeze-7B-Instruct-v0_1**                                        |  10.74  |    11.1k                 |
| **Breeze-7B-Instruct-64k-v0_1**                                    | 10.74       |  88.8k            |
| Qwen-7B-Chat                                                       |   10.86         |    9.8k                  |
| Qwen-14B-Chat                                                      |   18.89  |    9.8k                  |
| Mistral-7B-v0.1-Instruct                                           |  20.48   |    5.1k                 |
| Taiwan-LLM-7B-v2.1-chat                                            |   26.26          |    2.2k                  |
| Taiwan-LLM-13B-v2.0-chat                                           |   36.80          |    2.2k                  |
| Yi-34B-Chat                                                        |  43.71   |    4.5k                  |

## Long-context Performance

TBD

## Use in Transformers

First install direct dependencies:
```
pip install transformers torch accelerate
```
If you want faster inference using flash-attention2, you need to install these dependencies:
```bash
pip install packaging ninja
pip install flash-attn
```
Then load the model in transformers:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "MediaTek-Research/Breeze-7B-Instruct-v0_1",
    device_map="auto",
    torch_dtype=torch.bfloat16,
    attn_implementation="flash_attention_2" # optional
)
```

The structure of the query is 
```txt
<s>SYS_PROMPT   [INST] QUERY1 [/INST] RESPONSE1 [INST] QUERY2 [/INST] 
```
where `SYS_PROMPT`, `QUERY1`, `RESPONSE1`, and `QUERY2` can be provided by the user.

The suggested default `SYS_PROMPT` is 
```txt
You are a helpful AI assistant built by MediaTek Research. The user you are helping speaks Traditional Chinese and comes from Taiwan.
```

We also integrate `chat_template` into [tokenizer_config.json](tokenizer_config.json), so you can `apply_chat_template` to get the prompt.

```python
>>> from transformers import AutoTokenizer
>>> tokenizer = AutoTokenizer.from_pretrained("MediaTek-Research/Breeze-7B-Instruct-v0_1")
>>> chat = [
...   {"role": "user", "content": "你好，請問你可以完成什麼任務？"},
...   {"role": "assistant", "content": "你好，我可以幫助您解決各種問題、提供資訊和協助您完成許多不同的任務。例如：回答技術問題、提供建議、翻譯文字、尋找資料或協助您安排行程等。請告訴我如何能幫助您。"},
...   {"role": "user", "content": "太棒了！"},
... ]
>>> tokenizer.apply_chat_template(chat, tokenize=False)
"<s>You are a helpful AI assistant built by MediaTek Research. The user you are helping speaks Traditional Chinese and comes from Taiwan.   [INST] 你好，請問你可以完成什麼任務？ [/INST] 你好，我可以幫助您解決各種問題、提供資訊和協助您完成許多不同的任務。例如：回答技術問題、提供建議、翻譯文字、尋找資料或協助您安排行程等。請告訴我如何能幫助您。 [INST] 太棒了！ [/INST] "
# Tokenized results
# ['▁', '你好', '，', '請問', '你', '可以', '完成', '什麼', '任務', '？']
# ['▁', '你好', '，', '我', '可以', '幫助', '您', '解決', '各種', '問題', '、', '提供', '資訊', '和', '協助', '您', '完成', '許多', '不同', '的', '任務', '。', '例如', '：', '回答', '技術', '問題', '、', '提供', '建議', '、', '翻譯', '文字', '、', '尋找', '資料', '或', '協助', '您', '安排', '行程', '等', '。', '請', '告訴', '我', '如何', '能', '幫助', '您', '。']
# ['▁', '太', '棒', '了', '！']
```

## Citation

```
@article{MediaTek-Research2024breeze7b,
      title={Breeze-7B Technical Report}, 
      author={Chan-Jan Hsu and Chang-Le Liu and Feng-Ting Liao and Po-Chun Hsu and Yi-Chang Chen and Da-Shan Shiu},
      year={2024},
      eprint={2403.02712},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```