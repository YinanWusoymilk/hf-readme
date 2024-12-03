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
- tiny
- russian
- multiclass
- classification
datasets:
- sismetanin/rureviews
- RuSentiment
- LinisCrowd2015
- LinisCrowd2016
- KaggleRussianNews
---

This is [RuBERT-tiny2](https://huggingface.co/cointegrated/rubert-tiny2) model fine-tuned for __sentiment classification__ of short __Russian__ texts.
The task is a __multi-class classification__ with the following labels:

```yaml
0: neutral
1: positive
2: negative
```

Label to Russian label:

```yaml
neutral: нейтральный
positive: позитивный
negative: негативный
```

## Usage

```python
from transformers import pipeline
model = pipeline(model="seara/rubert-tiny2-russian-sentiment")
model("Привет, ты мне нравишься!")
# [{'label': 'positive', 'score': 0.9398769736289978}]
```

## Dataset

This model was trained on the union of the following datasets:

- Kaggle Russian News Dataset
- Linis Crowd 2015
- Linis Crowd 2016
- RuReviews
- RuSentiment

An overview of the training data can be found on [S. Smetanin Github repository](https://github.com/sismetanin/sentiment-analysis-in-russian).

__Download links for all Russian sentiment datasets collected by Smetanin can be found in this [repository](https://github.com/searayeah/russian-sentiment-emotion-datasets).__

## Training

Training were done in this [project](https://github.com/searayeah/bert-russian-sentiment-emotion) with this parameters:

```yaml
tokenizer.max_length: 512
batch_size: 64
optimizer: adam
lr: 0.00001
weight_decay: 0
epochs: 5
```

Train/validation/test splits are 80%/10%/10%.

## Eval results (on test split)


|         |neutral|positive|negative|macro avg|weighted avg|
|---------|-------|--------|--------|---------|------------|
|precision|0.7    |0.84    |0.74    |0.76     |0.75        |
|recall   |0.74   |0.83    |0.69    |0.75     |0.75        |
|f1-score |0.72   |0.83    |0.71    |0.75     |0.75        |
|auc-roc  |0.85   |0.95    |0.91    |0.9      |0.9         |
|support  |5196   |3831    |3599    |12626    |12626       |
