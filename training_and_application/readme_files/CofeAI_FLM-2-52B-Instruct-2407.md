# Introduction

FLM-2 (aka Tele-FLM) is our open-source large language model series. The FLM-2 series demonstrate superior performances at its scale, and sometimes surpass larger models. The currently released versions include (Tele-FLM)[https://huggingface.co/CofeAI/Tele-FLM] and (Tele-FLM-1T)[https://huggingface.co/CofeAI/Tele-FLM-1T]. These models feature a stable, efficient pre-training paradigm and enhanced factual judgment capabilities. This repo contains the instruction-tuned 52B Tele-FLM model, which we have named FLM-2-52B-Instruct.

# Model Details

FLM-2-52B-Instruct utilizes the standard GPT-style decoder-only transformer architecture with a few adjustments:

* Rotary Positional Embedding (RoPE)
* RMSNorm for normalization
* SwiGLU for activation function
* Linear bias disabled
* Embedding and language model head untied
* Input and output multiplier

| Models                    | layer<br>number | attention<br>heads | hidden<br>size | ffn hidden<br>size | vocab<br>size |  params<br>count |
| -------------             | :-------------: | :----------------: | :------------: | :----------------: | :-----------: | :--------------: |
| FLM-2-52B-Instruct-2407   | 64              | 64                 | 8,192          | 21,824             | 80,000        |  52.85 B         |

# Training details

Unlike conventional fine-tuning methods, we employed an innovative and cost-effective fine-tuning approach. Through specialized screening techniques, we meticulously selected 30,735 samples from a large corpus of fine-tuning data. This refined dataset facilitated the fine-tuning process and yielded promising results.

# Quickstart

Here provides simple code for loading the tokenizer, loading the model, and generating contents.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained('CofeAI/FLM-2-52B-Instruct-2407', trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained('CofeAI/FLM-2-52B-Instruct-2407', torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, device_map="auto", trust_remote_code=True)
history = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "你好"},
    {"role": "user", "content": "北京有哪些必去的景点？"}
]
inputs = tokenizer.apply_chat_template(history, return_tensors='pt').to(model.device)
response = model.generate(inputs, max_new_tokens=128, repetition_penalty=1.03)
print(tokenizer.decode(response.cpu()[0], skip_special_tokens=True))
```

# Evaluation

We evaluate the alignment performance of FLM-2-52B-Instruct-2407 in Chinese across various domains utilizing [AlignBench](https://arxiv.org/pdf/2311.18743). AlignBench is a comprehensive and multidimensional evaluation benchmark designed to assess Chinese large language models’ alignment performance. It encompasses 8 categories with a total of 683 question-answer pairs, covering areas such as fundamental language ability (Fund.), Chinese advanced understanding (Chi.), open-ended questions (Open.), writing ability (Writ.), logical reasoning (Logi.), mathematics (Math.), task-oriented role playing (Role.), and professional knowledge (Pro.).

| Models                  | Overall     | Math.     | Logi.     | Fund.     | Chi.      | Open.     | Writ.     | Role.     | Pro.      |
| ----------------------- | :-------:   | :-----:   | :-----:   | :-----:   | :----:    | :-----:   | :-----:   | :-----:   | :----:    |
| gpt-4-1106-preview      |   **7.58**  | **7.39**  | **6.83**  | **7.69**  |<u>7.07</u>| **8.66**  | **8.23**  | **8.08**  | **8.55**  |
| gpt-4-0613              | <u>6.83</u> |<u>6.33</u>|<u>5.15</u>| 7.16      | 6.76      | 7.26      | 7.31      | 7.48      | 7.56      |
| gpt-3.5-turbo-0613      |   5.68      | 4.90      | 4.79      | 6.01      | 5.60      | 6.97      | 7.27      | 6.98      | 6.29      |
| chatglm-turbo           |   6.36      | 4.88      | 5.09      |<u>7.50</u>| 7.03      |<u>8.45</u>| 8.05      | 7.67      | 7.70      |
| FLM-2-52B-Instruct-2407 |   6.23      | 3.79      |<u>5.15</u>| **7.69**  | **7.86**  |<u>8.45</u>|<u>8.17</u>|<u>7.88</u>|<u>7.85</u>|


# Citation

If you find our work helpful, please consider citing it.
```
@article{tele-flm-1t,
  author       = {Xiang Li and Yiqun Yao and Xin Jiang and Xuezhi Fang and Chao Wang and Xinzhang Liu and Zihan Wang and Yu Zhao and Xin Wang and Yuyao Huang and Shuangyong Song and Yongxiang Li and Zheng Zhang and Bo Zhao and Aixin Sun and Yequan Wang and Zhongjiang He and Zhongyuan Wang and Xuelong Li and Tiejun Huang},
  title        = {52B to 1T: Lessons Learned via Tele-FLM Series},
  journal      = {CoRR},
  volume       = {abs/2407.02783},
  year         = {2024},
  url          = {https://doi.org/10.48550/arXiv.2407.02783},
  doi          = {10.48550/ARXIV.2407.02783},
  eprinttype   = {arXiv},
  eprint       = {2407.02783},
}

@article{tele-flm-2024,
  author       = {Xiang Li and Yiqun Yao and Xin Jiang and Xuezhi Fang and Chao Wang and Xinzhang Liu and Zihan Wang and Yu Zhao and Xin Wang and Yuyao Huang and Shuangyong Song and Yongxiang Li and Zheng Zhang and Bo Zhao and Aixin Sun and Yequan Wang and Zhongjiang He and Zhongyuan Wang and Xuelong Li and Tiejun Huang},
  title        = {Tele-FLM Technical Report},
  journal      = {CoRR},
  volume       = {abs/2404.16645},
  year         = {2024},
  url          = {https://doi.org/10.48550/arXiv.2404.16645},
  doi          = {10.48550/ARXIV.2404.16645},
  eprinttype   = {arXiv},
  eprint       = {2404.16645},
}
```
