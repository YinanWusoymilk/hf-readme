---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- semantic-search
- chinese
---

# DMetaSoul/sbert-chinese-general-v2

此模型基于 [bert-base-chinese](https://huggingface.co/bert-base-chinese) 版本 BERT 模型，在百万级语义相似数据集 [SimCLUE](https://github.com/CLUEbenchmark/SimCLUE) 上进行训练，适用于**通用语义匹配**场景，从效果来看该模型在各种任务上**泛化能力更好**。

注：此模型的[轻量化版本](https://huggingface.co/DMetaSoul/sbert-chinese-general-v2-distill)，也已经开源啦！

# Usage

## 1. Sentence-Transformers

通过  [sentence-transformers](https://www.SBERT.net) 框架来使用该模型，首先进行安装：

```
pip install -U sentence-transformers
```

然后使用下面的代码来载入该模型并进行文本表征向量的提取：

```python
from sentence_transformers import SentenceTransformer
sentences = ["我的儿子！他猛然间喊道，我的儿子在哪儿？", "我的儿子呢！他突然喊道，我的儿子在哪里？"]

model = SentenceTransformer('DMetaSoul/sbert-chinese-general-v2')
embeddings = model.encode(sentences)
print(embeddings)
```

## 2. HuggingFace Transformers

如果不想使用   [sentence-transformers](https://www.SBERT.net) 的话，也可以通过 HuggingFace Transformers 来载入该模型并进行文本向量抽取：

```python
from transformers import AutoTokenizer, AutoModel
import torch


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ["我的儿子！他猛然间喊道，我的儿子在哪儿？", "我的儿子呢！他突然喊道，我的儿子在哪里？"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('DMetaSoul/sbert-chinese-general-v2')
model = AutoModel.from_pretrained('DMetaSoul/sbert-chinese-general-v2')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```

## Evaluation

该模型在公开的几个语义匹配数据集上进行了评测，计算了向量相似度跟真实标签之间的相关性系数：

|                              | **csts_dev** | **csts_test** | **afqmc**  | **lcqmc**  | **bqcorpus** | **pawsx**  | **xiaobu** |
| ---------------------------- | ------------ | ------------- | ---------- | ---------- | ------------ | ---------- | ---------- |
| **sbert-chinese-general-v1** | **84.54%**   | **82.17%**    | 23.80%     | 65.94%     | 45.52%       | 11.52%     | 48.51%     |
| **sbert-chinese-general-v2** | 77.20%       | 72.60%        | **36.80%** | **76.92%** | **49.63%**   | **16.24%** | **63.16%** |

这里对比了本模型跟之前我们发布 [sbert-chinese-general-v1](https://huggingface.co/DMetaSoul/sbert-chinese-general-v1) 之间的差异，可以看到本模型在多个任务上的泛化能力更好。

## Citing & Authors

E-mail: xiaowenbin@dmetasoul.com