---
license: apache-2.0
---

<div align="center">
<h1>
  星辰语义大模型-TeleChat
</h1>
</div>

<p align="center">
🤗 <a href="https://huggingface.co/Tele-AI" target="_blank">Hugging Face</a> • 🏔 <a href="https://gitee.com/mindspore/mindformers/tree/dev/research/telechat" target="_blank">MindSpore</a> • 🐾 <a href="https://gitee.com/Tele-AI/tele-chat" target="_blank">gitee</a>️ • 💬 <a href="https://github.com/Tele-AI/Telechat/blob/master/images/wechat.jpg" target="_blank">WeChat</a>
</p>

<p align="center">
 <a href="https://arxiv.org/abs/2401.03804" target="_blank"> Tech Report </a> 
</p>


# 最新动态
- 2024.3.20 开源12B版本chat模型及量化版本
- 2024.1.11 开源1T中文数据集
- 2024.1.10 开源7B版本chat模型及其量化版本

# 模型介绍
### 星辰语义大模型-TeleChat
- 星辰语义大模型TeleChat是由中电信人工智能科技有限公司研发训练的大语言模型，其中7B模型基座采用1.5万亿 Tokens中英文高质量语料进行训练，12B模型基座采用3万亿 Tokens中英文高质量语料进行训练。
- 我们开源了对话模型**TeleChat-7B-bot**与**TeleChat-12B-bot**，以及其`huggingface`格式的权重文件。此外，我们还开源了7B、12B模型的int8和int4量化版本。
- **TeleChat-12B-bot**在模型结构、训练数据、训练方法等方面进行了改进，在通用问答和知识类、代码类、数学类榜单上相比**TeleChat-7B-bot**均有大幅提升。在模型结构方面，我们使用小规模的模型尝试多种模型结构的组合，选择最优结构。相比**TeleChat-7B-bot**模型，**TeleChat-12B-bot**模型采用了词嵌入层与输出层解耦的结构，将词嵌入层和输出lm head层参数分开，有助于增强训练稳定性和收敛性。在训练数据方面，我们收集了覆盖书籍、百科、新闻、政务、法律、医药、专利、论文、数学、代码等诸多方面的大量中英文数据；通过优化数据清洗策略大幅提升数据的文本干净度、观点无偏性、内容有效性、格式规范性。在训练方法方面，我们使用科学数据配比学习与课程学习的方法，使用小参数模型在多种数据配比的数据上拟合，得到对各个数据集难度的先验估计；训练过程中每隔一段时间自动化评估当前模型在所有数据集上的loss，以及在评测集上的生成效果，动态提升较难学习的数据集权重，保证模型在各个数据集上都有较佳的拟合效果。

### 模型结构

我们采用标准的 `Decoder-only` 结构设计了 **TeleChat** 模型，并在模型维度做了如下的一些改进：

- **位置编码**：我们使用 [Rotary Embedding](https://arxiv.org/pdf/2104.09864.pdf) 的位置编码方法，该方法将相对位置信息依赖集成到 self-attention 中，并且具有较好的位置外推性。Rotary Embedding还可以较好地与Flash-Attention v2 配合使用，将模型的训练速度提升约20%。
- **激活函数**：我们使用 [SwiGLU](https://arxiv.org/pdf/2002.05202.pdf) 激活函数来替代GELU激活函数 , 为了减少计算量，将`ffn_hidden_size`设置为小于原始SwiGLU中的4倍隐藏层大小。
- **层标准化**: 基于 [RMSNorm](https://arxiv.org/abs/1910.07467) 的 Pre-Normalization。
- **词嵌入层与输出层解耦**：我们将**TeleChat-12B-bot**的词嵌入层和输出lm head层参数分开，有助于增强训练稳定性和收敛性。


|     | layer_num | hidden_size | ffn_hidden_size | head_num | tie_word_embeddings |
|-----| --------- | ----------- | --------------- | -------- | ----------------------- |
| 7B  | 30        | 4096        | 12288           | 32       | 是                      |
| 12B  | 38        | 5120        | 12288           | 32       | 否                      |

---

我们开源的TeleChat模型：
- 支持deepspeed微调，开源了基于deepspeed的训练代码，支持Zero并行显存优化，同时集成了FlashAttention2
- 多轮能力支持。开源了多轮数据构建方式，针对多轮模型训练集成了针对多轮的mask loss训练方式，更好的聚焦多轮答案，提升问答效果。
- 外推能力提升。开源了8K训练版本模型，采用NTK-aware外推和attention scaling外推方式，可以外推到96K。
- 具备较好的长文生成能力。在工作总结、工作计划、PPT大纲、申论、招标书、邮件、方案、周报、JD写作等长文写作任务上表现较好。


本次发布版本和下载链接见下表

| 模型版本     | 下载链接                                                                  |
|----------|-----------------------------------------------------------------------|
| 7B-FP16  | [TeleChat-7B-FP16](https://huggingface.co/Tele-AI/Telechat-7B)        |
| 7B-int8  | [TeleChat-7B-int8](https://huggingface.co/Tele-AI/Telechat-7B-int8)   |
| 7B-int4  | [TeleChat-7B-int4](https://huggingface.co/Tele-AI/Telechat-7B-int4)   |
| 12B-FP16 | [TeleChat-12B-FP16](https://huggingface.co/Tele-AI/TeleChat-12B)      |     
| 12B-int8 | [TeleChat-12B-int8](https://huggingface.co/Tele-AI/TeleChat-12B-int8) |  
| 12B-int4 | [TeleChat-12B-int4](https://huggingface.co/Tele-AI/TeleChat-12B-int4) | 

# 数据开源
### 数据介绍
TeleChat-PTD 是由电信星辰大模型**TeleChat**预训练语料中抽取出的的综合性大规模中文数据集。数据主要来源于网页、书籍、官方媒体等。 我们使用规则+模型的方式进行了相关的过滤，并对数据进行了相似性去重，尽可能地提取出高质量地数据。

TeleChat-PTD 数据集大约公开了2.7亿条数据，数据由纯中文文本构成构成，原始大小约1TB,压缩后480G，共189个文件。数据集中已经去除了其它冗余信息。

### 数据下载

huggingface下载地址：[TeleChat-PTD](https://huggingface.co/datasets/Tele-AI/TeleChat-PTD)

天翼云盘下载地址：[数据下载](https://cloud.189.cn/t/ia2QbaVzYf6z)（访问码：pkg8）

# 效果评测
TeleChat模型相比同规模模型在评测效果方面也有较好的表现，我们的评测集涵盖了包括MMLU、C-Eval、GAOKAO、AGIEval、CMMLU、 GSM8K、MATH、HumanEval、CHID等数据集，评测能力包括了自然语言理解、知识、数学计算和推理、代码生成等

## 评测结果如下

| Model               |   MMLU   | C-Eval | CMMLU  |  AGIEval  |  GAOKAO   | GSM8K  |  MATH  | HumanEval |    CSL    |   CHID    | EPRSTMT  |  BBH   | HellaSwag |
|:--------------------|:--------:|:------:|:------:|:---------:|:---------:|:------:|:------:|:---------:|:---------:|:---------:|:--------:|:------:|:---------:|
|                     |  5-shot  | 5-shot | 5-shot | zero-shot | zero-shot | 4-shot | 4-shot | zero-shot | zero-shot | zero-shot |zero-shot | 3-shot | zero-shot |
| LLaMA2-7B-chat      |   46.2   |  31.9  |  31.5  |   28.5    |   16.1    |  26.3  |  3.9   |   12.2    |   58.8    |   44.1    |   57.5   |  35.6  |   74.1    |
| LLaMA2-13B-chat     |   54.6   |  36.2  |  38.7  |   32.3    |   18.6    |  29.6  |  5.0   |   18.9    |   61.2    |   48.0    |   59.4   |  40.2  |   78.2    |
| ChatGLM2-6B-chat    |   45.9   |  52.6  |  49.3  |   39.0    |   46.4    |  28.8  |  6.5   |   11.0    |   61.2    |   57.9    |  71.2    |  32.7  |   57.0    |
| ChatGLM3-6B-chat    |   51.9   |  53.8  |   54   |   38.9    |   49.3    |  56.7  |  18.7  |    61     |   65.6    |   63.4    |    85    |  44.6  |   62.7    |
| Baichuan2-7B-chat   |   52.8   |  55.6  |  54.0  |   35.3    |   39.7    |  32.8  |   6    |   13.4    |    60     |   75.2    |   87.5   |  35.8  |  61.6     | 
| Baichuan2-13B-chat  |    57    |  56.7  |  58.4  |    40     |   51.4    |  55.3  |  8.6   |   17.7    |   63.1    |   78.2    |   87.5   |  49.9  |   66.9    |
| Qwen-7B-chat        |   56.6   |  59.3  |  59.5  |   41.3    |   63.3    |  52.5  |  10.3  |   26.2    |   63.1    |   72.3    |   88.8   |  46.9  |   59.9    |
| Qwen-14B-chat       |   66.4   |  71.7  |  70.0  |   47.3    |   76.5    |  61.0  |  26.8  |   36.6    |   55.6    |   72.3    |   91.2   |  58.0  | 65.2      |
| TeleChat-7B-chat    | **60.5** |  **64.6**  |  **64.3**  |   **46.8**    |    **59**     |  **36.7**  |  **10.3**  |   **20.1**    |   **66.8**    |   **88.0**    |   **87.5**   |  **19.5**  |  **36.7**     |
| TeleChat-12B-chat   |   **73.3**   |  **66.6**  |  **74.2**  |   **51.7**    |   **53.1**    |  **57.2**  |  **16.0**  |   **22.0**    |   **60.6**    |   **83.2**    |   **86.3**   |  **52.2**  |   **71.5**    | 

说明：CMMLU、AGIEval、GAOKAO、CSL、CHID、EPRSTMT均基于[OpenCompass](https://github.com/open-compass/OpenCompass/)平台提供的评测方法进行评估，而对于对比模型，我们同时参考了官方汇报结果和OpenCompass结果。我们使用了自己的评测脚本评测MMLU与CEVAL榜单，具体方法见`evaluation/`文件夹。

# 模型推理

```python
>>> import os
>>> import torch
>>> from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig
>>> os.environ["CUDA_VISIBLE_DEVICES"] = '0'
>>> tokenizer = AutoTokenizer.from_pretrained('../models/7B')
>>> model = AutoModelForCausalLM.from_pretrained('../models/7B', trust_remote_code=True, device_map="auto", torch_dtype=torch.float16)
>>> generate_config = GenerationConfig.from_pretrained('../models/7B')
>>> question="生抽与老抽的区别？"
>>> answer, history = model.chat(tokenizer = tokenizer, question=question, history=[], generation_config=generate_config, stream=False)
>>> print(answer)
生抽和老抽是两种不同的酱油，它们的区别如下：
 
1. 原料不同：生抽是用大豆、小麦等谷物为原料制成的；而老抽则是用豆酱、面酱等发酵后的调味品为原料制成的。
 
2. 制作工艺不同：生抽是通过将大豆浸泡在水中，然后经过蒸煮、发酵等过程制成的；而老抽则是在生抽的基础上加入一定比例的盐、糖、味精等调料，再进行发酵制成的。
 
3. 口感和风味不同：生抽具有咸鲜的味道，口感比较清爽；而老抽则具有特殊的香味和味道，口感相对较重。
 
总的来说，生抽和老抽都是酱油的不同种类，它们在原料、制作工艺和口感等方面都有所不同。
```



# 声明、协议、引用
### 声明
我们在此声明，不要使用TeleChat模型及其衍生模型进行任何危害国家社会安全或违法的活动。同时，我们也要求使用者不要将TeleChat模型用于没有安全审查和备案的互联网服务。我们希望所有使用者遵守上述原则，确保科技发展在合法合规的环境下进行。

我们已经尽我们所能，来确保模型训练过程中使用的数据的合规性。然而，尽管我们已经做出了巨大的努力，但由于模型和数据的复杂性，仍有可能存在一些无法预见的问题。因此，如果由于使用TeleChat开源模型而导致的任何问题，包括但不限于数据安全问题、公共舆论风险，或模型被误导、滥用、传播或不当利用所带来的任何风险和问题，我们将不承担任何责任。

### 协议
社区使用 TeleChat 模型需要遵循《[TeleChat模型社区许可协议](./TeleChat模型社区许可协议.pdf)》。TeleChat模型支持商业用途，如果您计划将 TeleChat 模型或其衍生品用于商业目的，您需要通过以下联系邮箱 tele_ai@chinatelecom.cn，提交《TeleChat模型社区许可协议》要求的申请材料。审核通过后，将特此授予您一个非排他性、全球性、不可转让、不可再许可、可撤销的商用版权许可。

### 引用
如需引用我们的工作，请使用如下 reference:
```
@misc{wang2024telechat,
      title={TeleChat Technical Report}, 
      author={Zihan Wang and Xinzhang Liu and Shixuan Liu and Yitong Yao and Yuyao Huang and Zhongjiang He and Xuelong Li and Yongxiang Li and Zhonghao Che and Zhaoxi Zhang and Yan Wang and Xin Wang and Luwen Pu and Huihan Xu and Ruiyu Fang and Yu Zhao and Jie Zhang and Xiaomeng Huang and Zhilong Lu and Jiaxin Peng and Wenjun Zheng and Shiquan Wang and Bingkai Yang and Xuewei he and Zhuoru Jiang and Qiyi Xie and Yanhan Zhang and Zhongqiu Li and Lingling Shi and Weiwei Fu and Yin Zhang and Zilu Huang and Sishi Xiong and Yuxiang Zhang and Chao Wang and Shuangyong Song},
      year={2024},
      eprint={2401.03804},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```