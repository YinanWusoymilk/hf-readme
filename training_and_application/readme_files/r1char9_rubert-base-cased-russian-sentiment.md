---
license: mit
language:
- ru
metrics:
- f1
- roc_auc
- precision
- recall
pipeline_tag: text-classification
tags:
- sentiment-analysis
- multi-class-classification
- sentiment analysis
- rubert
- sentiment
- bert
- russian
- multiclass
- classification
---

Модель [RuBERT](https://huggingface.co/DeepPavlov/rubert-base-cased) которая был fine-tuned на задачу __sentiment classification__ для коротких __Russian__ текстов.
Задача представляет собой __multi-class classification__ со следующими метками:

```yaml
0: neutral
1: positive
2: negative
```

## Usage

```python
from transformers import pipeline
model = pipeline(model="r1char9/rubert-base-cased-russian-sentiment")
model("Привет, ты мне нравишься!")
# [{'label': 'positive', 'score': 0.8220236897468567}]
```

## Dataset

Модель была натренирована на данных:

- Kaggle Russian News Dataset
- Linis Crowd 2015
- Linis Crowd 2016
- RuReviews
- RuSentiment

```yaml
tokenizer.max_length: 256
batch_size: 32
optimizer: adam
lr: 0.00001
weight_decay: 0
epochs: 2
```