---
license: other
license_name: deepseek
license_link: https://github.com/deepseek-ai/DeepSeek-V2/blob/main/LICENSE-MODEL
---

<!-- markdownlint-disable first-line-h1 -->
<!-- markdownlint-disable html -->
<!-- markdownlint-disable no-duplicate-header -->

<div align="center">
  <img src="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/figures/logo.svg?raw=true" width="60%" alt="DeepSeek-V2" />
</div>
<hr>
<div align="center" style="line-height: 1;">
  <a href="https://www.deepseek.com/" target="_blank" style="margin: 2px;">
    <img alt="Homepage" src="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/figures/badge.svg?raw=true" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://chat.deepseek.com/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/🤖%20Chat-DeepSeek%20V2-536af5?color=536af5&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://huggingface.co/deepseek-ai" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-DeepSeek%20AI-ffc107?color=ffc107&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://discord.gg/Tc7c45Zzu5" target="_blank" style="margin: 2px;">
    <img alt="Discord" src="https://img.shields.io/badge/Discord-DeepSeek%20AI-7289da?logo=discord&logoColor=white&color=7289da" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/figures/qr.jpeg?raw=true" target="_blank" style="margin: 2px;">
    <img alt="Wechat" src="https://img.shields.io/badge/WeChat-DeepSeek%20AI-brightgreen?logo=wechat&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://twitter.com/deepseek_ai" target="_blank" style="margin: 2px;">
    <img alt="Twitter Follow" src="https://img.shields.io/badge/Twitter-deepseek_ai-white?logo=x&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div align="center" style="line-height: 1;">
  <a href="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/LICENSE-CODE" style="margin: 2px;">
    <img alt="Code License" src="https://img.shields.io/badge/Code_License-MIT-f5de53?&color=f5de53" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/deepseek-ai/DeepSeek-V2/blob/main/LICENSE-MODEL" style="margin: 2px;">
    <img alt="Model License" src="https://img.shields.io/badge/Model_License-Model_Agreement-f5de53?&color=f5de53" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<p align="center">
  <a href="#2-model-downloads">Model Download</a> |
  <a href="#3-evaluation-results">Evaluation Results</a> |
  <a href="#4-model-architecture">Model Architecture</a> |
  <a href="#6-api-platform">API Platform</a> |
  <a href="#8-license">License</a> |
  <a href="#9-citation">Citation</a>
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2405.04434"><b>Paper Link</b>👁️</a>
</p>

# DeepSeek-V2-Chat-0628

## 1. Introduction

DeepSeek-V2-Chat-0628 is an improved version of DeepSeek-V2-Chat. For model details, please visit [DeepSeek-V2 page](https://huggingface.co/deepseek-ai/DeepSeek-V2-Chat) for more information. 

DeepSeek-V2-Chat-0628 has achieved remarkable performance on the LMSYS Chatbot Arena Leaderboard:

Overall Ranking: #11, outperforming all other open-source models.

<p align="center">
  <img width="90%" src="figures/arena1.jpeg" />
</p>

Coding Arena Ranking: #3, showcasing exceptional capabilities in coding tasks.

<p align="center">
  <img width="90%" src="figures/arena2.png" />
</p>

Hard Prompts Arena Ranking: #3, demonstrating strong performance on challenging prompts.

<p align="center">
  <img width="90%" src="figures/arena3.png" />
</p>

## 2. Improvement

Compared to the previous version DeepSeek-V2-Chat, the new version has made the following improvements:

| **Benchmark** | **DeepSeek-V2-Chat** | **DeepSeek-V2-Chat-0628** | **Improvement** |
|:-----------:|:------------:|:---------------:|:-------------------------:|
| **HumanEval** | 81.1 | 84.8 | +3.7 |
| **MATH** | 53.9 | 71.0 | +17.1 |
| **BBH** | 79.7 | 83.4 | +3.7 |
| **IFEval** | 63.8 | 77.6 | +13.8 |
| **Arena-Hard** | 41.6 | 68.3 | +26.7 |
| **JSON Output (Internal)** | 78 | 85 | +7 |

Furthermore, the instruction following capability in the "system" area has been optimized, significantly enhancing the user experience for immersive translation, RAG, and other tasks.

## 3. How to run locally

**To utilize DeepSeek-V2-Chat-0628 in BF16 format for inference, 80GB*8 GPUs are required.**
### Inference with Huggingface's Transformers
You can directly employ [Huggingface's Transformers](https://github.com/huggingface/transformers) for model inference.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig

model_name = "deepseek-ai/DeepSeek-V2-Chat-0628"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
# `max_memory` should be set based on your devices
max_memory = {i: "75GB" for i in range(8)}
# `device_map` cannot be set to `auto`
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, device_map="sequential", torch_dtype=torch.bfloat16, max_memory=max_memory, attn_implementation="eager")
model.generation_config = GenerationConfig.from_pretrained(model_name)
model.generation_config.pad_token_id = model.generation_config.eos_token_id

messages = [
    {"role": "user", "content": "Write a piece of quicksort code in C++"}
]
input_tensor = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
outputs = model.generate(input_tensor.to(model.device), max_new_tokens=100)

result = tokenizer.decode(outputs[0][input_tensor.shape[1]:], skip_special_tokens=True)
print(result)
```

The complete chat template can be found within `tokenizer_config.json` located in the huggingface model repository.

**Note: The chat template has been updated compared to the previous DeepSeek-V2-Chat version.**

An example of chat template is as belows:

```bash
<｜begin▁of▁sentence｜><｜User｜>{user_message_1}<｜Assistant｜>{assistant_message_1}<｜end▁of▁sentence｜><｜User｜>{user_message_2}<｜Assistant｜>
```

You can also add an optional system message:

```bash
<｜begin▁of▁sentence｜>{system_message}

<｜User｜>{user_message_1}<｜Assistant｜>{assistant_message_1}<｜end▁of▁sentence｜><｜User｜>{user_message_2}<｜Assistant｜>
```

### Inference with vLLM (recommended)
To utilize [vLLM](https://github.com/vllm-project/vllm) for model inference, please merge this Pull Request into your vLLM codebase: https://github.com/vllm-project/vllm/pull/4650.

```python
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

max_model_len, tp_size = 8192, 8
model_name = "deepseek-ai/DeepSeek-V2-Chat-0628"
tokenizer = AutoTokenizer.from_pretrained(model_name)
llm = LLM(model=model_name, tensor_parallel_size=tp_size, max_model_len=max_model_len, trust_remote_code=True, enforce_eager=True)
sampling_params = SamplingParams(temperature=0.3, max_tokens=256, stop_token_ids=[tokenizer.eos_token_id])

messages_list = [
    [{"role": "user", "content": "Who are you?"}],
    [{"role": "user", "content": "Translate the following content into Chinese directly: DeepSeek-V2 adopts innovative architectures to guarantee economical training and efficient inference."}],
    [{"role": "user", "content": "Write a piece of quicksort code in C++."}],
]

prompt_token_ids = [tokenizer.apply_chat_template(messages, add_generation_prompt=True) for messages in messages_list]

outputs = llm.generate(prompt_token_ids=prompt_token_ids, sampling_params=sampling_params)

generated_text = [output.outputs[0].text for output in outputs]
print(generated_text)
```

## 4. License
This code repository is licensed under [the MIT License](LICENSE-CODE). The use of DeepSeek-V2 Base/Chat models is subject to [the Model License](LICENSE-MODEL). DeepSeek-V2 series (including Base and Chat) supports commercial use.

## 5. Citation
```
@misc{deepseekv2,
      title={DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model}, 
      author={DeepSeek-AI},
      year={2024},
      eprint={2405.04434},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

## 6. Contact
If you have any questions, please raise an issue or contact us at [service@deepseek.com](service@deepseek.com).
