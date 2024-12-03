---
license: apache-2.0
pipeline_tag: text-generation
---

**InternLM**

<div align="center">

<img src="https://github.com/InternLM/InternLM/assets/22529082/b9788105-8892-4398-8b47-b513a292378e" width="200"/>
  <div>&nbsp;</div>
  <div align="center">
    <b><font size="5">InternLM</font></b>
    <sup>
      <a href="https://internlm.intern-ai.org.cn/">
        <i><font size="4">HOT</font></i>
      </a>
    </sup>
    <div>&nbsp;</div>
  </div>

[![evaluation](https://github.com/InternLM/InternLM/assets/22529082/f80a2a58-5ddf-471a-8da4-32ab65c8fd3b)](https://github.com/internLM/OpenCompass/)

[💻Github Repo](https://github.com/InternLM/InternLM) • [🤔Reporting Issues](https://github.com/InternLM/InternLM/issues/new)

</div>


## Introduction

The Shanghai Artificial Intelligence Laboratory, in collaboration with SenseTime Technology, the Chinese University of Hong Kong, and Fudan University, has officially released the 20 billion parameter pretrained model, InternLM-20B. InternLM-20B was pre-trained on over **2.3T** Tokens containing high-quality English, Chinese, and code data. Additionally, the Chat version has undergone SFT and RLHF training, enabling it to better and more securely meet users' needs.

In terms of model structure, InternLM-20B opted for a deeper architecture, with a depth set at 60 layers. This surpasses the conventional 7B and 13B models that utilize 32 or 40 layers. When parameters are limited, increasing the number of layers can enhance the model's overall capability. Furthermore, compared to InternLM-7B, the pre-training data used for InternLM-20B underwent higher quality cleansing and was supplemented with data rich in knowledge and designed for reinforcing understanding and reasoning capabilities. As a result, it exhibits significant improvements in understanding, reasoning, mathematical, and programming abilities—all of which test the technical proficiency of language models. Overall, InternLM-20B features the following characteristics:
- Outstanding overall performance
- Strong utility invocation capability
- Supports a 16k context length (Through infererence extrapolation)
- Better value alignment.

## Performance Evaluation
On the 5 capability dimensions proposed by OpenCompass, InternLM-20B has achieved excellent results (the bolded scores represent the best performances within the 13B-33B parameter range).

| Capability | Llama-13B | Llama2-13B | Baichuan2-13B | InternLM-20B | Llama-33B | Llama-65B | Llama2-70B |
|----------|-----------|------------|---------------|--------------|-----------|-----------|------------|
| Language     | 42.5      | 47         | 47.5          | **55**           | 44.6      | 47.1      | 51.6       |
| Knowledge     | 58.2      | 58.3       | 48.9          | 60.1         | **64**        | 66        | 67.7       |
| Understanding     | 45.5      | 50.9       | 58.1          | **67.3**         | 50.6      | 54.2      | 60.8       |
| Reasoning     | 42.7      | 43.6       | 44.2          | **54.9**         | 46.4      | 49.8      | 55         |
| Examination     | 37.3      | 45.2       | 51.8          | **62.5**         | 47.4      | 49.7      | 57.3       |
| Overall   | 43.8      | 47.3       | 49.4          | **59.2**         | 48.9      | 51.9      | 57.4       |

The table below compares the performance of mainstream open-source models on some influential and typical datasets.

|      | Benchmarks           | Llama-13B | Llama2-13B | Baichuan2-13B | InternLM-20B | Llama-33B | Llama-65B | Llama2-70B |
|------|------------------|-----------|------------|---------------|--------------|-----------|-----------|------------|
| Examination | MMLU             | 47.73     | 54.99      | 59.55         | **62.05**        | 58.73     | 63.71     | 69.75      |
|      | C-Eval (val)     | 31.83     | 41.4       | **59.01**         | 58.8         | 37.47     | 40.36     | 50.13      |
|      | AGI-Eval         | 22.03     | 30.93      | 37.37         | **44.58**        | 33.53     | 33.92     | 40.02      |
| Knowledge | BoolQ            | 78.75     | 82.42      | 67            | **87.46**        | 84.43     | 86.61     | 87.74      |
|      | TriviaQA         | 52.47     | 59.36      | 46.61         | 57.26        | **66.24**     | 69.79     | 70.71      |
|      | NaturalQuestions | 20.17     | 24.85      | 16.32         | 25.15        | **30.89**     | 33.41     | 34.16      |
| Understanding | CMRC             | 9.26      | 31.59      | 29.85         | **68.78**        | 14.17     | 34.73     | 43.74      |
|      | CSL              | 55        | 58.75      | 63.12         | **65.62**        | 57.5      | 59.38     | 60         |
|      | RACE (middle)    | 53.41     | 63.02      | 68.94         | **86.35**        | 64.55     | 72.35     | 81.55      |
|      | RACE (high)      | 47.63     | 58.86      | 67.18         | **83.28**        | 62.61     | 68.01     | 79.93      |
|      | XSum             | 20.37     | 23.37      | 25.23         | **35.54**        | 20.55     | 19.91     | 25.38      |
| Reasoning | WinoGrande       | 64.64     | 64.01      | 67.32         | **69.38**        | 66.85     | 69.38     | 69.77      |
|      | BBH              | 37.93     | 45.62      | 48.98         | **52.51**        | 49.98     | 58.38     | 64.91      |
|      | GSM8K            | 20.32     | 29.57      | **52.62**         | **52.62**        | 42.3      | 54.44     | 63.31      |
|      | PIQA             | 79.71     | 79.76      | 78.07         | 80.25        | **81.34**     | 82.15     | 82.54      |
| Programming | HumanEval        | 14.02     | 18.9       | 17.07         | **25.61**        | 17.68     | 18.9      | 26.22      |
|      | MBPP             | 20.6      | 26.8       | 30.8          | **35.6**         | 28.4      | 33.6      | 39.6       |

Overall, InternLM-20B comprehensively outperforms open-source models in the 13B parameter range in terms of overall capabilities, and on inference evaluation sets, it approaches or even surpasses the performance of Llama-65B.

## Import from Transformers
To load the InternLM 20B model using Transformers, use the following code:
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("internlm/internlm-20b", trust_remote_code=True)
# Set `torch_dtype=torch.bfloat16` to load model in bfloat16, otherwise it will be loaded as float32 and cause OOM Error.
model = AutoModelForCausalLM.from_pretrained("internlm/internlm-20b", torch_dtype=torch.bfloat16, trust_remote_code=True).cuda()
model = model.eval()
inputs = tokenizer(["Coming to the beautiful nature, we found"], return_tensors="pt")
for k,v in inputs.items():
    inputs[k] = v.cuda()
gen_kwargs = {"max_length": 128, "top_p": 0.8, "temperature": 0.8, "do_sample": True, "repetition_penalty": 1.05}
output = model.generate(**inputs, **gen_kwargs)
output = tokenizer.decode(output[0].tolist(), skip_special_tokens=True)
print(output)
# Coming to the beautiful nature, we found not only various mountains, rivers, trees, and flowers but also many birds and beasts. Birds are the ones we are most familiar with; some are soaring in the sky, some are hopping on the ground, while others perch on trees...
```

**Limitations:** Although we have made efforts to ensure the safety of the model during the training process and to encourage the model to generate text that complies with ethical and legal requirements, the model may still produce unexpected outputs due to its size and probabilistic generation paradigm. For example, the generated responses may contain biases, discrimination, or other harmful content. Please do not propagate such content. We are not responsible for any consequences resulting from the dissemination of harmful information.


## Open Source License

The code is licensed under Apache-2.0, while model weights are fully open for academic research and also allow **free** commercial usage. To apply for a commercial license, please fill in the [application form (English)](https://wj.qq.com/s2/12727483/5dba/)/[申请表（中文）](https://wj.qq.com/s2/12725412/f7c1/). For other questions or collaborations, please contact <internlm@pjlab.org.cn>.


## 简介
上海人工智能实验室与商汤科技联合香港中文大学和复旦大学正式推出书生·浦语200亿参数模型版本 InternLM-20B ，InternLM-20B 在超过 **2.3T** Tokens 包含高质量英文、中文和代码的数据上进行预训练，其中 Chat 版本还经过了 SFT 和 RLHF 训练，使其能够更好、更安全地满足用户的需求。  

InternLM 20B 在模型结构上选择了深结构，层数设定为60层，超过常规7B和13B模型所使用的32层或者40层。在参数受限的情况下，提高层数有利于提高模型的综合能力。此外，相较于InternLM-7B，InternLM-20B使用的预训练数据经过了更高质量的清洗，并补充了高知识密度和用于强化理解与推理能力的训练数据。因此，它在理解能力、推理能力、数学能力、编程能力等考验语言模型技术水平的方面都得到了显著提升。总体而言，InternLM-20B具有以下的特点： 
- 优异的综合性能
- 很强的工具调用功能
- 支持16k语境长度（通过推理时外推）
- 更好的价值对齐

## 性能评测
在OpenCompass提出的5个能力维度上，InternLM-20B都取得很好的效果（粗体为13B-33B这个量级范围内，各项最佳成绩）

| 能力维度 | Llama-13B | Llama2-13B | Baichuan2-13B | InternLM-20B | Llama-33B | Llama-65B | Llama2-70B |
|----------|-----------|------------|---------------|--------------|-----------|-----------|------------|
| 语言     | 42.5      | 47         | 47.5          | **55**           | 44.6      | 47.1      | 51.6       |
| 知识     | 58.2      | 58.3       | 48.9          | 60.1         | **64**        | 66        | 67.7       |
| 理解     | 45.5      | 50.9       | 58.1          | **67.3**         | 50.6      | 54.2      | 60.8       |
| 推理     | 42.7      | 43.6       | 44.2          | **54.9**         | 46.4      | 49.8      | 55         |
| 学科     | 37.3      | 45.2       | 51.8          | **62.5**         | 47.4      | 49.7      | 57.3       |
| 总平均   | 43.8      | 47.3       | 49.4          | **59.2**         | 48.9      | 51.9      | 57.4       |

下表展示了在多个经典数据集上 InternLM 20B 与各个主流开源模型的表现

|      | 评测集           | Llama-13B | Llama2-13B | Baichuan2-13B | InternLM-20B | Llama-33B | Llama-65B | Llama2-70B |
|------|------------------|-----------|------------|---------------|--------------|-----------|-----------|------------|
| 学科 | MMLU             | 47.73     | 54.99      | 59.55         | **62.05**        | 58.73     | 63.71     | 69.75      |
|      | C-Eval (val)     | 31.83     | 41.4       | **59.01**         | 58.8         | 37.47     | 40.36     | 50.13      |
|      | AGI-Eval         | 22.03     | 30.93      | 37.37         | **44.58**        | 33.53     | 33.92     | 40.02      |
| 知识 | BoolQ            | 78.75     | 82.42      | 67            | **87.46**        | 84.43     | 86.61     | 87.74      |
|      | TriviaQA         | 52.47     | 59.36      | 46.61         | 57.26        | **66.24**     | 69.79     | 70.71      |
|      | NaturalQuestions | 20.17     | 24.85      | 16.32         | 25.15        | **30.89**     | 33.41     | 34.16      |
| 理解 | CMRC             | 9.26      | 31.59      | 29.85         | **68.78**        | 14.17     | 34.73     | 43.74      |
|      | CSL              | 55        | 58.75      | 63.12         | **65.62**        | 57.5      | 59.38     | 60         |
|      | RACE (middle)    | 53.41     | 63.02      | 68.94         | **86.35**        | 64.55     | 72.35     | 81.55      |
|      | RACE (high)      | 47.63     | 58.86      | 67.18         | **83.28**        | 62.61     | 68.01     | 79.93      |
|      | XSum             | 20.37     | 23.37      | 25.23         | **35.54**        | 20.55     | 19.91     | 25.38      |
| 推理 | WinoGrande       | 64.64     | 64.01      | 67.32         | **69.38**        | 66.85     | 69.38     | 69.77      |
|      | BBH              | 37.93     | 45.62      | 48.98         | **52.51**        | 49.98     | 58.38     | 64.91      |
|      | GSM8K            | 20.32     | 29.57      | **52.62**         | **52.62**        | 42.3      | 54.44     | 63.31      |
|      | PIQA             | 79.71     | 79.76      | 78.07         | 80.25        | **81.34**     | 82.15     | 82.54      |
| 编程 | HumanEval        | 14.02     | 18.9       | 17.07         | **25.61**        | 17.68     | 18.9      | 26.22      |
|      | MBPP             | 20.6      | 26.8       | 30.8          | **35.6**         | 28.4      | 33.6      | 39.6       |

总体而言，InternLM-20B 在综合能力上全面领先于13B量级的开源模型，同时在推理评测集上能够接近甚至超越Llama-65B的性能。

## 通过 Transformers 加载
通过以下的代码加载 InternLM 20B 模型
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("internlm/internlm-20b", trust_remote_code=True)
# `torch_dtype=torch.bfloat16` 可以令模型以 bfloat16 精度加载，否则 transformers 会将模型加载为 float32，导致显存不足
model = AutoModelForCausalLM.from_pretrained("internlm/internlm-20b", torch_dtype=torch.bfloat16, trust_remote_code=True).cuda()
model = model.eval()
inputs = tokenizer(["来到美丽的大自然，我们发现"], return_tensors="pt")
for k,v in inputs.items():
    inputs[k] = v.cuda()
gen_kwargs = {"max_length": 128, "top_p": 0.8, "temperature": 0.8, "do_sample": True, "repetition_penalty": 1.05}
output = model.generate(**inputs, **gen_kwargs)
output = tokenizer.decode(output[0].tolist(), skip_special_tokens=True)
print(output)
# 来到美丽的大自然，我们发现，这里不仅有大大小小的山川河流和树木花草，而且还有很多飞鸟走兽。我们最熟悉的就是鸟类了，它们有的在天上飞翔，有的在地上跳跃，还有的在树上栖息……
```

**局限性：** 尽管在训练过程中我们非常注重模型的安全性，尽力促使模型输出符合伦理和法律要求的文本，但受限于模型大小以及概率生成范式，模型可能会产生各种不符合预期的输出，例如回复内容包含偏见、歧视等有害内容，请勿传播这些内容。由于传播不良信息导致的任何后果，本项目不承担责任。

## 开源许可证

本仓库的代码依照 Apache-2.0 协议开源。模型权重对学术研究完全开放，也可申请免费的商业使用授权（[申请表](https://wj.qq.com/s2/12725412/f7c1/)）。其他问题与合作请联系 <internlm@pjlab.org.cn>。
