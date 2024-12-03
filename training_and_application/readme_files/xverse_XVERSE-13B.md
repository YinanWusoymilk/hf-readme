---
license: apache-2.0

inference: false

---

# XVERSE-13B

## 更新信息
**[2023/11/06]** 发布新版本的 **XVERSE-13B-2** 底座模型和 **XVERSE-13B-Chat-2** 对话模型，相较于原始版本，新版本的模型训练更加充分（从 1.4T 增加到 3.2T），各方面的能力均得到大幅提升，同时新增工具调用能力。  
**[2023/09/26]** 发布 7B 尺寸的 [XVERSE-7B](https://github.com/xverse-ai/XVERSE-7B) 底座模型和 [XVERSE-7B-Chat](https://github.com/xverse-ai/XVERSE-7B) 对话模型，支持在单张消费级显卡部署运行，并保持高性能、全开源、免费可商用。  
**[2023/08/22]** 发布经过指令精调的 XVERSE-13B-Chat 对话模型。   
**[2023/08/07]** 发布 13B 尺寸的 XVERSE-13B 底座模型。

## Update Information
**[2023/11/06]** The new versions of the **XVERSE-13B-2** base model and the **XVERSE-13B-Chat-2** model have been released. Compared to the original versions, the new models have undergone more extensive training (increasing from 1.4T to 3.2T), resulting in significant improvements in all capabilities, along with the addition of Function Call abilities.   
**[2023/09/26]** Released the [XVERSE-7B](https://github.com/xverse-ai/XVERSE-7B) base model and [XVERSE-7B-Chat](https://github.com/xverse-ai/XVERSE-7B) instruct-finetuned model with 7B size, which support deployment and operation on a single consumer-grade graphics card while maintaining high performance, full open source, and free for commercial use.   
**[2023/08/22]** Released the aligned instruct-finetuned model XVERSE-13B-Chat.
**[2023/08/07]* Released the XVERSE-13B base model.

## 模型介绍

**XVERSE-13B** 是由深圳元象科技自主研发的支持多语言的大语言模型（Large Language Model），主要特点如下：

- **模型结构**：XVERSE-13B 使用主流 Decoder-only 的标准 Transformer 网络结构，支持 8K 的上下文长度（Context Length），为同尺寸模型中最长，能满足更长的多轮对话、知识问答与摘要等需求，模型应用场景更广泛。
- **训练数据**：构建了 3.2 万亿 token 的高质量、多样化的数据对模型进行充分训练，包含中、英、俄、西等 40 多种语言，通过精细化设置不同类型数据的采样比例，使得中英两种语言表现优异，也能兼顾其他语言效果。
- **分词**：基于 BPE（Byte-Pair Encoding）算法，使用上百 GB 语料训练了一个词表大小为 100,534 的分词器，能够同时支持多语言，而无需额外扩展词表。
- **训练框架**：自主研发多项关键技术，包括高效算子、显存优化、并行调度策略、数据-计算-通信重叠、平台和框架协同等，让训练效率更高，模型稳定性强，在千卡集群上的峰值算力利用率可达到 58.5%，位居业界前列。

## Model Introduction

**XVERSE-13B** is a multilingual large language model, independently developed by Shenzhen Yuanxiang Technology. Its key features are as follows:

- **Model Structure**: XVERSE-13B uses the mainstream Decoder-only Transformer network structure, supports 8k context length, the longest one among models of the same size, which can meet the need of longer multi-round dialogues, knowledge question-answering, and summarization. This makes the model more versatile in application scenarios.
- **Training Data**: The model has been thoroughly trained on a diversified and high-quality dataset consisting of 3.2 trillion of tokens, including more than 40 languages such as Chinese, English, Russian, and Spanish. The sampling ratio of different types of data is finely set, which makes the performance of Chinese and English excellent, and also takes into account the effect of other languages.
- **Tokenization**: Based on the BPE (Byte-Pair Encoding) algorithm, a tokenizer with a vocabulary size of 100,534 has been trained using hundreds of gigabytes of language data. This tokenizer is capable of supporting multilingual without the need for additional vocabulary expansion.
- **Training Framework**: Several key technologies have also been independently developed, including efficient operators, memory optimization, parallel scheduling strategies, overlap of data-computation-communication, and synergy between platforms and frameworks. These advancements enhance training efficiency and model stability. With these technologies, the peak computational power utilization rate on a thousand-card cluster can reach 58.5%, ranking at the forefront of the industry.

## 评测结果

为了综合评估模型的性能，我们在一系列标准数据集上进行了全面测试，包括C-Eval、CMMLU、Gaokao-Bench、MMLU、GAOKAO-English、AGIEval、RACE-M、CommonSenseQA、PIQA、GSM8K和HumanEval。这些评估覆盖了模型在多个领域的能力，具体包括中文问答、英文问答、语言理解、常识问答、逻辑推理、数学问题解答以及编程能力。评估结果如下：

|  能力维度  |           数据集           |        | XVERSE-13B-2 | XVERSE-13B | Baichuan2-13B | Llama1-13B | Llama2-13B |
| :--------: | :------------------------: | :----: | :----------: | :--------: | :-----------: | :--------: | :--------: |
|  中文问答  |           C-Eval           | 5-shot |     63.5     |    54.7    |     58.1      |    28.8    |    35.6    |
|            |           CMMLU            | 5-shot |     66.2     |    59.1    |     62.0      |    31.5    |    38.4    |
|            |  Gaokao-Bench<sup>1</sup>  | 5-shot |     67.5     |    53.9    |     54.3      |    26.4    |    35.4    |
|  英文问答  |            MMLU            | 5-shot |     61.2     |    55.1    |     59.2      |    46.9    |    54.8    |
|            | GAOKAO-English<sup>1</sup> | 5-shot |     73.7     |    66.5    |     67.7      |    38.1    |    60.6    |
| 中英文问答 |    AGIEval<sup>1</sup>     | 5-shot |     54.5     |    41.4    |     48.2      |    27.3    |    33.4    |
|  语言理解  |           RACE-M           | 0-shot |     84.6     |    74.2    |     68.9      |    61.6    |    63.0    |
|  常识问答  |       CommonSenseQA        | 7-shot |     74.0     |    69.5    |     65.6      |    62.0    |    67.3    |
|    推理    |            PIQA            | 0-shot |     80.8     |    79.0    |     78.5      |    80.1    |    80.5    |
|    数学    |           GSM8K            | 4-shot |     54.9     |    18.4    |     52.7      |    17.8    |    28.7    |
|    代码    |         HumanEval          | 0-shot |     39.6     |    15.9    |     17.1      |    15.8    |    18.3    |

> <sup>1：只针对其中的单项选择题进行测试，即排除了填空题、开放性问题和多项选择题</sup>   

对于上述所有比较模型，我们优先汇报其官方公布的结果。在缺少官方结果的情况下，我们采用了 [OpenCompass 榜单](https://opencompass.org.cn/leaderboard-llm)的报告结果。其他结果则来自于我们自行执行的评估流程所获得的数据。   
对于 MMLU ，我们采用作者提供的[评测工具](https://github.com/hendrycks/test)，C-Eval、AGIEval、GAOKAO-Bench、GAOKAO-English 与 MMLU 的评测方式相同，其余评测数据集使用 [OpenCompass 评估框架](https://github.com/open-compass/OpenCompass/)进行评估。

## Model Evaluation

To comprehensively assess the performance of the model, we conducted extensive testing across a range of standard datasets, including C-Eval, CMMLU, Gaokao-Bench, MMLU, GAOKAO-English, AGIEval, RACE-M, CommonSenseQA, PIQA, GSM8K and HumanEval. These evaluations spanned multiple capabilities of the model, specifically including Chinese question answering, English question answering, language comprehension, common sense questioning, logical reasoning, mathematical problem-solving, and coding ability. The results of the evaluations are as follows:

|  Capability Dimension  |          Dataset           |        | XVERSE-13B-2 | XVERSE-13B | Baichuan2-13B | Llama1-13B | Llama2-13B |
| :--------------------: | :------------------------: | :----: | :----------: | :--------: | :-----------: | :--------: | :--------: |
|       Chinese QA       |           C-Eval           | 5-shot |     63.5     |    54.7    |     58.1      |    28.8    |    35.6    |
|                        |           CMMLU            | 5-shot |     66.2     |    59.1    |     62.0      |    31.5    |    38.4    |
|                        |  Gaokao-Bench<sup>1</sup>  | 5-shot |     67.5     |    53.9    |     54.3      |    26.4    |    35.4    |
|       English QA       |            MMLU            | 5-shot |     61.2     |    55.1    |     59.2      |    46.9    |    54.8    |
|                        | GAOKAO-English<sup>1</sup> | 5-shot |     73.7     |    66.5    |     67.7      |    38.1    |    60.6    |
|  Chinese & English QA  |    AGIEval<sup>1</sup>     | 5-shot |     54.5     |    41.4    |     48.2      |    27.3    |    33.4    |
| Language Understanding |           RACE-M           | 0-shot |     84.6     |    74.2    |     68.9      |    61.6    |    63.0    |
|    Common Sense QA     |       CommonSenseQA        | 7-shot |     74.0     |    69.5    |     65.6      |    62.0    |    67.3    |
|       Reasoning        |            PIQA            | 0-shot |     80.8     |    79.0    |     78.5      |    80.1    |    80.5    |
|          Math          |           GSM8K            | 4-shot |     54.9     |    18.4    |     52.7      |    17.8    |    28.7    |
|         Coding         |         HumanEval          | 0-shot |     39.6     |    15.9    |     17.1      |    15.8    |    18.3    |

> <sup>1: Tests are conducted only on single-answer multiple-choice questions, thus excluding fill-in-the-blanks, open-ended questions, and multiple-answer multiple-choice questions.</sup>   

For all the comparison models mentioned above, we prioritize the disclosure of their officially published results. In the absence of official data, we refer to the reported outcomes from [OpenCompass Leaderboard](https://opencompass.org.cn/leaderboard-llm). Results not covered by the aforementioned sources are derived from our own evaluation pipline.   
For MMLU, we adopt the [evaluation tools](https://github.com/hendrycks/test) provided by the authors, C-Eval, AGIEval, GAOKAO-Bench, GAOKAO-English are the same as MMLU. For the remaining evaluation datasets, the [OpenCompass](https://github.com/open-compass/OpenCompass/) is employed for evaluation.

### Loading with Transformers

可通过以下代码加载 XVERSE-13B 模型进行推理：

The XVERSE-13B model can be loaded for inference using the following code:

```python
>>> import torch
>>> from transformers import AutoTokenizer, AutoModelForCausalLM
>>> tokenizer = AutoTokenizer.from_pretrained("xverse/XVERSE-13B")
>>> model = AutoModelForCausalLM.from_pretrained("xverse/XVERSE-13B", trust_remote_code=True, torch_dtype=torch.bfloat16, device_map='auto')
>>> model = model.eval()
>>> inputs = tokenizer('北京的景点：故宫、天坛、万里长城等。\n深圳的景点：', return_tensors='pt').input_ids
>>> inputs = inputs.cuda()
>>> generated_ids = model.generate(inputs, max_new_tokens=64, eos_token_id=tokenizer.eos_token_id, repetition_penalty=1.1)
>>> print(tokenizer.batch_decode(generated_ids, skip_special_tokens=True))
```

更多细节，包括对话demo、模型微调及量化等，请参考我们的[Github](https://github.com/xverse-ai/XVERSE-13B)。

For more details, including chat demo, model fine-tuning and quantization, please refer to our [Github](https://github.com/xverse-ai/XVERSE-13B).

## 局限性与免责申明

XVERSE-13B 与其他所有 LLM 一样，在某些情况下可能会产生不准确、有偏见或其他令人反感的内容。因此，请谨慎使用模型生成的内容，请勿将生成的有害内容进行传播，在部署任何 XVERSE-13B 的应用之前，开发人员应根据其具体应用对模型进行安全测试和调优。

我们强烈警告不要将 XVERSE-13B 模型用于制造或传播有害信息，或进行任何可能损害公众、国家、社会安全或违反法规的活动。如果使用 XVERSE-13B 模型产生任何问题，无论是数据安全问题、公共舆论风险，还是模型被误解、滥用、传播或不合规使用所引发的任何风险和问题，我们将不承担任何责任。

## Limitations and Disclaimer

Like all other Large Language Models (LLMs), XVERSE-13B may produce inaccurate, biased, or otherwise offensive content under certain circumstances. Therefore, please use the content generated by the model with caution and refrain from disseminating harmful content. Before deploying any application of XVERSE-13B, developers should conduct safety tests and optimization of the model according to its specific application.

We strongly warn against the use of the XVERSE-13B model for producing or spreading harmful information, or conducting any activities that might harm the public, national, or social security, or violate regulations. We assume no responsibility for any problems arising from the use of the XVERSE-13B model, whether it be data security issues, public opinion risks, or any risks and issues caused by misunderstanding, misuse, dissemination, or non-compliance with the model.

## 模型开源协议

使用本仓库的源码需要遵循 [Apache-2.0](https://github.com/xverse-ai/XVERSE-13B/blob/main/LICENSE) 开源协议，使用 XVERSE-13B 的模型权重则需要遵循[模型许可协议](https://github.com/xverse-ai/XVERSE-13B/blob/main/MODEL_LICENSE.pdf)。

XVERSE-13B 模型权重对学术研究**完全开放**，并且支持**免费商用**。如需申请商业许可证，请填写【[申请表](https://chat.xverse.cn/home/business.html)】，如有其他问题或合作，请联系 <opensource@xverse.cn>。

## Open Source License

The use of the source code in this repository must follow the [Apache-2.0](https://github.com/xverse-ai/XVERSE-13B/blob/main/LICENSE) open-source license, while the use of the model weights of XVERSE-13B needs to adhere to the [Model License Agreement](https://github.com/xverse-ai/XVERSE-13B/blob/main/MODEL_LICENSE.pdf).

The XVERSE-13B model weights are **fully open** to academic research and support **free commercial use**. To apply for a commercial license, please fill in the [application form](https://chat.xverse.cn/home/business.html). For other questions or collaborations, please contact <opensource@xverse.cn>.
