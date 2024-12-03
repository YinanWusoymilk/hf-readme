---
language:
- zh
- en
base_model: openbmb/MiniCPM-2B-sft-bf16
model-index:
- name: MiniCPM-Embedding
  results:
  - task:
      type: Retrieval
    dataset:
      type: mteb/arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
    metrics:
    - type: ndcg_at_10
      value: 64.65
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
    metrics:
    - type: ndcg_at_10
      value: 46.53
  - task:
      type: Retrieval
    dataset:
      type: mteb/climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
    metrics:
    - type: ndcg_at_10
      value: 35.55
  - task:
      type: Retrieval
    dataset:
      type: mteb/dbpedia
      name: MTEB DBPedia
      config: default
      split: test
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
    metrics:
    - type: ndcg_at_10
      value: 47.82
  - task:
      type: Retrieval
    dataset:
      type: mteb/fever
      name: MTEB FEVER
      config: default
      split: test
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
    metrics:
    - type: ndcg_at_10
      value: 90.76
  - task:
      type: Retrieval
    dataset:
      type: mteb/fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
    metrics:
    - type: ndcg_at_10
      value: 56.64
  - task:
      type: Retrieval
    dataset:
      type: mteb/hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
    metrics:
    - type: ndcg_at_10
      value: 78.11
  - task:
      type: Retrieval
    dataset:
      type: mteb/msmarco
      name: MTEB MSMARCO
      config: default
      split: dev
      revision: c5a29a104738b98a9e76336939199e264163d4a0
    metrics:
    - type: ndcg_at_10
      value: 43.93
  - task:
      type: Retrieval
    dataset:
      type: mteb/nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
    metrics:
    - type: ndcg_at_10
      value: 39.77
  - task:
      type: Retrieval
    dataset:
      type: mteb/nq
      name: MTEB NQ
      config: default
      split: test
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
    metrics:
    - type: ndcg_at_10
      value: 69.29
  - task:
      type: Retrieval
    dataset:
      type: mteb/quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 89.97
  - task:
      type: Retrieval
    dataset:
      type: mteb/scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 22.38
  - task:
      type: Retrieval
    dataset:
      type: mteb/scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
    metrics:
    - type: ndcg_at_10
      value: 86.6
  - task:
      type: Retrieval
    dataset:
      type: mteb/trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: ndcg_at_10
      value: 81.32
  - task:
      type: Retrieval
    dataset:
      type: mteb/touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
    metrics:
    - type: ndcg_at_10
      value: 25.08
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CmedqaRetrieval
      name: MTEB CmedqaRetrieval
      config: default
      split: dev
      revision: cd540c506dae1cf9e9a59c3e06f42030d54e7301
    metrics:
    - type: ndcg_at_10
      value: 46.05
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/CovidRetrieval
      name: MTEB CovidRetrieval
      config: default
      split: dev
      revision: 1271c7809071a13532e05f25fb53511ffce77117
    metrics:
    - type: ndcg_at_10
      value: 92.01
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/DuRetrieval
      name: MTEB DuRetrieval
      config: default
      split: dev
      revision: a1a333e290fe30b10f3f56498e3a0d911a693ced
    metrics:
    - type: ndcg_at_10
      value: 90.98
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/EcomRetrieval
      name: MTEB EcomRetrieval
      config: default
      split: dev
      revision: 687de13dc7294d6fd9be10c6945f9e8fec8166b9
    metrics:
    - type: ndcg_at_10
      value: 70.21
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MMarcoRetrieval
      name: MTEB MMarcoRetrieval
      config: default
      split: dev
      revision: 539bbde593d947e2a124ba72651aafc09eb33fc2
    metrics:
    - type: ndcg_at_10
      value: 85.55
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/MedicalRetrieval
      name: MTEB MedicalRetrieval
      config: default
      split: dev
      revision: 2039188fb5800a9803ba5048df7b76e6fb151fc6
    metrics:
    - type: ndcg_at_10
      value: 63.91
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/T2Retrieval
      name: MTEB T2Retrieval
      config: default
      split: dev
      revision: 8731a845f1bf500a4f111cf1070785c793d10e64
    metrics:
    - type: ndcg_at_10
      value: 87.33
  - task:
      type: Retrieval
    dataset:
      type: C-MTEB/VideoRetrieval
      name: MTEB VideoRetrieval
      config: default
      split: dev
      revision: 58c2597a5943a2ba48f4668c3b90d796283c5639
    metrics:
    - type: ndcg_at_10
      value: 78.05
pipeline_tag: feature-extraction
tags:
- mteb
- sentence-transformers
library_name: transformers
---
## MiniCPM-Embedding

**MiniCPM-Embedding** 是面壁智能与清华大学自然语言处理实验室（THUNLP）、东北大学信息检索小组（NEUIR）共同开发的中英双语言文本嵌入模型，有如下特点：
- 出色的中文、英文检索能力。
- 出色的中英跨语言检索能力。

MiniCPM-Embedding 基于 [MiniCPM-2B-sft-bf16](https://huggingface.co/openbmb/MiniCPM-2B-sft-bf16) 训练，结构上采取双向注意力和 Weighted Mean Pooling [1]。采取多阶段训练方式，共使用包括开源数据、机造数据、闭源数据在内的约 600 万条训练数据。

欢迎关注 RAG 套件系列：

- 检索模型：[MiniCPM-Embedding](https://huggingface.co/openbmb/MiniCPM-Embedding)
- 重排模型：[MiniCPM-Reranker](https://huggingface.co/openbmb/MiniCPM-Reranker)
- 面向 RAG 场景的 LoRA 插件：[MiniCPM3-RAG-LoRA](https://huggingface.co/openbmb/MiniCPM3-RAG-LoRA)

**MiniCPM-Embedding** is a bilingual & cross-lingual text embedding model developed by ModelBest Inc. , THUNLP and NEUIR , featuring:

- Exceptional Chinese and English retrieval capabilities.
- Outstanding cross-lingual retrieval capabilities between Chinese and English.

MiniCPM-Embedding is trained based on [MiniCPM-2B-sft-bf16](https://huggingface.co/openbmb/MiniCPM-2B-sft-bf16) and incorporates bidirectional attention and Weighted Mean Pooling [1] in its architecture. The model underwent multi-stage training using approximately 6 million training examples, including open-source, synthetic, and proprietary data.

We also invite you to explore the RAG toolkit series:

- Retrieval Model: [MiniCPM-Embedding](https://huggingface.co/openbmb/MiniCPM-Embedding)
- Re-ranking Model: [MiniCPM-Reranker](https://huggingface.co/openbmb/MiniCPM-Reranker)
- LoRA Plugin for RAG scenarios: [MiniCPM3-RAG-LoRA](https://huggingface.co/openbmb/MiniCPM3-RAG-LoRA)

[1] Muennighoff, N. (2022). Sgpt: Gpt sentence embeddings for semantic search. arXiv preprint arXiv:2202.08904.

## 模型信息 Model Information

- 模型大小：2.4B
- 嵌入维度：2304
- 最大输入token数：512

- Model Size: 2.4B
- Embedding Dimension: 2304
- Max Input Tokens: 512

## 使用方法 Usage

### 输入格式 Input Format

本模型支持 query 侧指令，格式如下：

MiniCPM-Embedding supports query-side instructions in the following format:

```
Instruction: {{ instruction }} Query: {{ query }}
```

例如：

For example:

```
Instruction: 为这个医学问题检索相关回答。Query: 咽喉癌的成因是什么？
```

```
Instruction: Given a claim about climate change, retrieve documents that support or refute the claim. Query: However the warming trend is slower than most climate models have forecast.
```

也可以不提供指令，即采取如下格式：

MiniCPM-Embedding also works in instruction-free mode in the following format:

```
Query: {{ query }}
```

我们在 BEIR 与 C-MTEB/Retrieval 上测试时使用的指令见 `instructions.json`，其他测试不使用指令。文档侧直接输入文档原文。

When running evaluation on BEIR and C-MTEB/Retrieval, we use instructions in `instructions.json`. For other evaluations, we do not use instructions. On the document side, we directly use the bare document as the input.

### 环境要求 Requirements

```
transformers==4.37.2
flash-attn>2.3.5
```

### 示例脚本 Demo

#### Huggingface Transformers
```python

from transformers import AutoModel, AutoTokenizer
import torch
import torch.nn.functional as F

model_name = "openbmb/MiniCPM-Embedding"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name, trust_remote_code=True, attn_implementation="flash_attention_2", torch_dtype=torch.float16).to("cuda")
model.eval()

# 由于在 `model.forward` 中缩放了最终隐层表示，此处的 mean pooling 实际上起到了 weighted mean pooling 的作用
# As we scale hidden states in `model.forward`, mean pooling here actually works as weighted mean pooling
def mean_pooling(hidden, attention_mask):
    s = torch.sum(hidden * attention_mask.unsqueeze(-1).float(), dim=1)
    d = attention_mask.sum(dim=1, keepdim=True).float()
    reps = s / d
    return reps

@torch.no_grad()
def encode(input_texts):
    batch_dict = tokenizer(input_texts, max_length=512, padding=True, truncation=True, return_tensors='pt', return_attention_mask=True).to("cuda")
    
    outputs = model(**batch_dict)
    attention_mask = batch_dict["attention_mask"]
    hidden = outputs.last_hidden_state

    reps = mean_pooling(hidden, attention_mask)   
    embeddings = F.normalize(reps, p=2, dim=1).detach().cpu().numpy()
    return embeddings

queries = ["中国的首都是哪里？"]
passages = ["beijing", "shanghai"]


INSTRUCTION = "Query: "
queries = [INSTRUCTION + query for query in queries]

embeddings_query = encode(queries)
embeddings_doc = encode(passages)

scores = (embeddings_query @ embeddings_doc.T)
print(scores.tolist())  # [[0.3535913825035095, 0.18596848845481873]]
```

#### Sentence Transformers

```python
import torch
from sentence_transformers import SentenceTransformer

model_name = "openbmb/MiniCPM-Embedding"
model = SentenceTransformer(model_name, trust_remote_code=True, model_kwargs={"attn_implementation": "flash_attention_2", "torch_dtype": torch.float16})

queries = ["中国的首都是哪里？"]
passages = ["beijing", "shanghai"]

INSTRUCTION = "Query: "

embeddings_query = model.encode(queries, prompt=INSTRUCTION)
embeddings_doc = model.encode(passages)

scores = (embeddings_query @ embeddings_doc.T)
print(scores.tolist())  # [[0.35365450382232666, 0.18592746555805206]]
```

## 实验结果 Evaluation Results

### 中文与英文检索结果 CN/EN Retrieval Results

| 模型 Model                    | C-MTEB/Retrieval (NDCG@10) | BEIR (NDCG@10) |
|------------------------------|-------------------|---------------|
| bge-large-zh-v1.5            | 70.46             | -             |
| gte-large-zh                 | 72.49             | -             |
| Zhihui_LLM_Embedding         | 76.74             |               |
| bge-large-en-v1.5            | -                 | 54.29         |
| gte-en-large-v1.5            | -                 | 57.91         |
| NV-Retriever-v1              | -                 | 60.9          |
| bge-en-icl                   | -                 | 62.16         |
| NV-Embed-v2                  | -                 | 62.65         |
| me5-large                    | 63.66             | 51.43         |
| bge-m3(Dense)                | 65.43             | 48.82         |
| gte-multilingual-base(Dense) | 71.95             | 51.08         |
| gte-Qwen2-1.5B-instruct      | 71.86             | 58.29         |
| gte-Qwen2-7B-instruct        | 76.03             | 60.25         |
| bge-multilingual-gemma2      | 73.73             | 59.24         |
| MiniCPM-Embedding                    | **76.76**         | 58.56         |
| MiniCPM-Embedding+MiniCPM-Reranker         | 77.08             | 61.61         |

### 中英跨语言检索结果 CN-EN Cross-lingual Retrieval Results

| 模型  Model                | MKQA En-Zh_CN (Recall@20) | NeuCLIR22 (NDCG@10) | NeuCLIR23 (NDCG@10) |
|------------------------------|--------------------|--------------------|--------------------|
| me5-large                    | 44.3               | 9.01               | 25.33              |
| bge-m3(Dense)                | 66.4               | 30.49              | 41.09              |
| gte-multilingual-base(Dense) | 68.2               | 39.46              | 45.86              |
| gte-Qwen2-1.5B-instruct      | 68.52              | 49.11              | 45.05              |
| gte-Qwen2-7B-instruct        | 68.27              | 49.14              | 49.6               |
| MiniCPM-Embedding                    | **72.95**          | **52.65**          | **49.95**          |
| MiniCPM-Embedding+MiniCPM-Reranker         | 74.33              | 53.21              | 54.12              |

## 许可证 License

- 本仓库中代码依照 [Apache-2.0 协议](https://github.com/OpenBMB/MiniCPM/blob/main/LICENSE)开源。
- MiniCPM-Embedding 模型权重的使用则需要遵循 [MiniCPM 模型协议](https://github.com/OpenBMB/MiniCPM/blob/main/MiniCPM%20Model%20License.md)。
- MiniCPM-Embedding 模型权重对学术研究完全开放。如需将模型用于商业用途，请填写[此问卷](https://modelbest.feishu.cn/share/base/form/shrcnpV5ZT9EJ6xYjh3Kx0J6v8g)。

* The code in this repo is released under the [Apache-2.0](https://github.com/OpenBMB/MiniCPM/blob/main/LICENSE) License. 
* The usage of MiniCPM-Embedding model weights must strictly follow [MiniCPM Model License.md](https://github.com/OpenBMB/MiniCPM/blob/main/MiniCPM%20Model%20License.md).
* The models and weights of MiniCPM-Embedding are completely free for academic research. After filling out a ["questionnaire"](https://modelbest.feishu.cn/share/base/form/shrcnpV5ZT9EJ6xYjh3Kx0J6v8g) for registration, MiniCPM-Embedding weights are also available for free commercial use.