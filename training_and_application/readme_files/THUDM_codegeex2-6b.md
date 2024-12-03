---
language:
- zh
- en
tags:
- codegeex
- glm
- chatglm
- thudm
---

![](resources/codegeex_logo.png)

<p align="center">
    🏠 <a href="https://codegeex.cn" target="_blank">Homepage</a>｜💻 <a href="https://github.com/THUDM/CodeGeeX2" target="_blank">GitHub</a>｜🛠 Tools <a href="https://marketplace.visualstudio.com/items?itemName=aminer.codegeex" target="_blank">VS Code</a>, <a href="https://plugins.jetbrains.com/plugin/20587-codegeex" target="_blank">Jetbrains</a>｜🤗 <a href="https://huggingface.co/THUDM/codegeex2-6b" target="_blank">HF Repo</a>｜📄 <a href="https://arxiv.org/abs/2303.17568" target="_blank">Paper</a>
</p>

<p align="center">
    👋 Join our <a href="https://discord.gg/8gjHdkmAN6" target="_blank">Discord</a>, <a href="https://join.slack.com/t/codegeexworkspace/shared_invite/zt-1s118ffrp-mpKKhQD0tKBmzNZVCyEZLw" target="_blank">Slack</a>, <a href="https://t.me/+IipIayJ32B1jOTg1" target="_blank">Telegram</a>, <a href="https://github.com/THUDM/CodeGeeX2/blob/main/resources/wechat.md"target="_blank">WeChat</a>
</p>

INT4量化版本｜INT4 quantized version [codegeex2-6b-int4](https://huggingface.co/THUDM/codegeex2-6b-int4)

# CodeGeeX2: 更强大的多语言代码生成模型
# A More Powerful Multilingual Code Generation Model

CodeGeeX2 是多语言代码生成模型 [CodeGeeX](https://github.com/THUDM/CodeGeeX) ([KDD’23](https://arxiv.org/abs/2303.17568)) 的第二代模型。CodeGeeX2 基于 [ChatGLM2](https://github.com/THUDM/ChatGLM2-6B) 架构加入代码预训练实现，得益于 ChatGLM2 的更优性能，CodeGeeX2 在多项指标上取得性能提升（+107% > CodeGeeX；仅60亿参数即超过150亿参数的 StarCoder-15B 近10%），更多特性包括：

* **更强大的代码能力**：基于 ChatGLM2-6B 基座语言模型，CodeGeeX2-6B 进一步经过了 600B 代码数据预训练，相比一代模型，在代码能力上全面提升，[HumanEval-X](https://huggingface.co/datasets/THUDM/humaneval-x) 评测集的六种编程语言均大幅提升 (Python +57%, C++ +71%, Java +54%, JavaScript +83%, Go +56%, Rust +321\%)，在Python上达到 35.9\% 的 Pass@1 一次通过率，超越规模更大的 StarCoder-15B。
* **更优秀的模型特性**：继承 ChatGLM2-6B 模型特性，CodeGeeX2-6B 更好支持中英文输入，支持最大 8192 序列长度，推理速度较一代 CodeGeeX-13B 大幅提升，量化后仅需6GB显存即可运行，支持轻量级本地化部署。
* **更全面的AI编程助手**：CodeGeeX插件（[VS Code](https://marketplace.visualstudio.com/items?itemName=aminer.codegeex), [Jetbrains](https://plugins.jetbrains.com/plugin/20587-codegeex)）后端升级，支持超过100种编程语言，新增上下文补全、跨文件补全等实用功能。结合 Ask CodeGeeX 交互式AI编程助手，支持中英文对话解决各种编程问题，包括且不限于代码解释、代码翻译、代码纠错、文档生成等，帮助程序员更高效开发。
* **更开放的协议**：CodeGeeX2-6B 权重对学术研究完全开放，填写[登记表](https://open.bigmodel.cn/mla/form?mcode=CodeGeeX2-6B)申请商业使用。


CodeGeeX2 is the second-generation model of the multilingual code generation model [CodeGeeX](https://github.com/THUDM/CodeGeeX) ([KDD’23](https://arxiv.org/abs/2303.17568)), which is implemented based on the [ChatGLM2](https://github.com/THUDM/ChatGLM2-6B) architecture trained on more code data. Due to the advantage of ChatGLM2, CodeGeeX2 has been comprehensively improved in coding capability (+107% > CodeGeeX; with only 6B parameters, surpassing larger StarCoder-15B for some tasks). It has the following features:

* **More Powerful Coding Capabilities**: Based on the ChatGLM2-6B model, CodeGeeX2-6B has been further pre-trained on 600B code tokens, which has been comprehensively improved in coding capability compared to the first-generation. On the [HumanEval-X](https://huggingface.co/datasets/THUDM/humaneval-x) benchmark, all six languages have been significantly improved (Python +57%, C++ +71%, Java +54%, JavaScript +83%, Go +56%, Rust +321\%), and in Python it reached 35.9% of Pass@1 one-time pass rate, surpassing the larger StarCoder-15B.
* **More Useful Features**: Inheriting the ChatGLM2-6B model features, CodeGeeX2-6B better supports both Chinese and English prompts, maximum 8192 sequence length, and the inference speed is significantly improved compared to the first-generation. After quantization, it only needs 6GB of GPU memory for inference, thus supports lightweight local deployment.
* **Comprehensive AI Coding Assistant**: The backend of CodeGeeX plugin ([VS Code](https://marketplace.visualstudio.com/items?itemName=aminer.codegeex), [Jetbrains](https://plugins.jetbrains.com/plugin/20587-codegeex)) is upgraded, supporting 100+ programming languages, and adding practical functions such as infilling and cross-file completion. Combined with the "Ask CodeGeeX" interactive AI coding assistant, it can be used to solve various programming problems via Chinese or English dialogue, including but not limited to code summarization, code translation, debugging, and comment generation, which helps increasing the efficiency of developpers.
* **Open Liscense**: CodeGeeX2-6B weights are fully open to academic research, and please apply for commercial use by filling in the [registration form](https://open.bigmodel.cn/mla/form?mcode=CodeGeeX2-6B).


## 软件依赖 ｜ Dependency

```shell
pip install protobuf transformers==4.30.2 cpm_kernels torch>=2.0 gradio mdtex2html sentencepiece accelerate
```

## 快速开始 ｜ Get Started

```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("THUDM/codegeex2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/codegeex2-6b", trust_remote_code=True, device='cuda')
model = model.eval()

# remember adding a language tag for better performance
prompt = "# language: Python\n# write a bubble sort function\n"
inputs = tokenizer.encode(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(inputs, max_length=256, top_k=1)
response = tokenizer.decode(outputs[0])

>>> print(response)
# language: Python
# write a bubble sort function


def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


print(bubble_sort([5, 2, 1, 8, 4]))
```

关于更多的使用说明，请参考 CodeGeeX2 的 [Github Repo](https://github.com/THUDM/CodeGeeX2)。

For more information, please refer to CodeGeeX2's [Github Repo](https://github.com/THUDM/CodeGeeX2).

## 协议 ｜ License

本仓库的代码依照 [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) 协议开源，模型的权重的使用则需要遵循 [Model License](MODEL_LICENSE)。

The code in this repository is open source under the [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) license. The model weights are licensed under the [Model License](MODEL_LICENSE).

## 引用 ｜ Citation

如果觉得我们的工作有帮助，欢迎引用以下论文：

If you find our work helpful, please feel free to cite the following paper:

```
@inproceedings{zheng2023codegeex,
      title={CodeGeeX: A Pre-Trained Model for Code Generation with Multilingual Evaluations on HumanEval-X}, 
      author={Qinkai Zheng and Xiao Xia and Xu Zou and Yuxiao Dong and Shan Wang and Yufei Xue and Zihan Wang and Lei Shen and Andi Wang and Yang Li and Teng Su and Zhilin Yang and Jie Tang},
      booktitle={KDD},
      year={2023}
}
```
