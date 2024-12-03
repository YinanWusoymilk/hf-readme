---
developers: [https://huggingface.co/FlagAlphaAI]
license: apache-2.0
language:
- zh
- en
pipeline_tag: question-answering
library_name: transformers
---
# Atom-7B

Atom-7B完全开源可商用，由Llama中文社区和AtomEcho（原子回声）联合研发，基于Llama2-7B采用大规模的中文数据进行了继续预训练，我们会持续提供更新的模型参数，模型训练过程见[llama.family](https://llama.family)。

模型的部署、训练、微调等方法详见Llama中文社区GitHub仓库：[**Llama-Chinese**](https://github.com/LlamaFamily/Llama-Chinese)。


## 📝 中文数据

| 类型                                                       | 描述                                                         |
| ---------------------------------------------------------- | ------------------------------------------------------------ |
| 网络数据                                                   | 互联网上公开的网络数据，挑选出去重后的高质量中文数据，涉及到百科、书籍、博客、新闻、公告、小说等高质量长文本数据。 |
| [Wikipedia](https://github.com/goldsmith/Wikipedia)        | 中文Wikipedia的数据                                          |
| [悟道](https://github.com/BAAI-WuDao/Model)                | 中文悟道开源的200G数据                                       |
| [Clue](https://github.com/CLUEbenchmark/CLUEDatasetSearch) | Clue开放的中文预训练数据，进行清洗后的高质量中文长文本数据   |
| 竞赛数据集                                                 | 近年来中文自然语言处理多任务竞赛数据集，约150个              |
| [MNBVC](https://github.com/esbatmop/MNBVC)                 | MNBVC 中清洗出来的部分数据集                                 |

**我们也欢迎大家在[llama.family](https://llama.family)中贡献自己的数据，您的数据通过审核后会加入模型训练，也将影响模型未来的能力走向。**


## 📚 中文词表

为了提高中文文本处理的效率，我们针对Llama2模型的词表进行了深度优化。

首先，我们基于数百G的中文文本，**在Llama2词表的基础上扩展词库至65,000个单词**。

经过测试，我们的改进使得**中文编码/解码速度提高了约350％**。

此外，我们还扩大了中文字符集的覆盖范围，包括所有**emoji符号**，这使的生成带有表情符号的文章更加高效。

对于Llama2原生词表中的一些特殊情况，如数字、英文等，我们尽可能地避免对其进行修改或替换。

最终，成功地实现了一种既能提高中文处理效率又能保持Llama2原有性能的方法。


## 📈 训练过程

**模型结构**

基于当前最优秀的开源模型Llama2，使用主流Decoder-only的标准Transformer网络结构，支持4K的上下文长度（Context Length），为同尺寸模型中最长，能满足更长的多轮对话、知识问答与摘要等需求，模型应用场景更广泛。

**FlashAttention-2高效训练**

Atom-7B采用了FlashAttention-2技术进行训练。由于在处理较长的输入序列时，内存消耗的问题可能会导致“内存爆炸”现象。FlashAttention-2是一种高效注意力机制的实现方式之一，相较于传统的注意力技术（Attention），它拥有更快速的速度以及更加优化的内存占用率。

**基于NTK的自适应上下文扩展技术**

- 可在不继续训练模型的情况下支持更长的上下文
- 本项目中模型默认支持4K上下文，利用上述技术可扩展至18K+
- 经过微调可以支持到32K+


## 💻 推理配置
实际应用中，消费级显卡要比专业显卡便宜的多（比如3090相比A10，同样都是24G显存）。

对于消费级显卡，直接FP32肯定放不下，一般最基本的是FP16，而INT8和INT4量化就很有用，例如：

- 对于3080显卡（10G显存），Atom-7B的INT8只需要8G显存可以直接部署。
- 对于3080显卡（10G显存），Atom-7B的INT4只需要5G显存可以直接部署。


---


# Llama中文社区

## 🚀 社区地址：

Github：[**Llama-Chinese**](https://github.com/LlamaFamily/Llama-Chinese)

在线体验链接：[**llama.family**](https://llama.family/)

## 🔥 社区介绍
欢迎来到Llama中文社区！

我们是一个专注于Llama模型在中文方面的优化和上层建设的高级技术社区。

**基于大规模中文数据，从预训练开始对Llama2模型进行中文能力的持续迭代升级**。

我们热忱欢迎对大模型LLM充满热情的开发者和研究者加入我们的行列。

## 🐼 社区资源
  - Llama2在线体验链接[**llama.family**](https://llama.family/)，同时包含Meta原版和中文微调版本！
  - Llama2 Chat模型的[中文问答能力评测](https://github.com/LlamaFamily/Llama-Chinese/tree/main#-%E6%A8%A1%E5%9E%8B%E8%AF%84%E6%B5%8B)！
  - [社区飞书知识库](https://chinesellama.feishu.cn/wiki/space/7257824476874768388?ccm_open_type=lark_wiki_spaceLink)，欢迎大家一起共建！

