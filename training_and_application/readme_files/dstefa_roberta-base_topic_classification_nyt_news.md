---
license: mit
base_model: roberta-base
tags:
  - topic
  - classification
  - news
  - roberta
metrics:
- accuracy
- f1
- precision
- recall
datasets:
  - dstefa/New_York_Times_Topics
widget:
  - text: >-
      Olympic champion Kostas Kederis today left hospital ahead of his date with IOC inquisitors claiming his innocence and vowing.
    example_title: Sports
  - text: >-
      Although many individuals are doing fever checks to screen for Covid-19, many Covid-19 patients never have a fever.
    example_title: Health and Wellness
  - text: >-
      Twelve myths about Russia's War in Ukraine exposed
    example_title: Crime
model-index:
- name: roberta-base_topic_classification_nyt_news
  results:
    - task:
          name: Text Classification
          type: text-classification
      dataset:
          name: New_York_Times_Topics
          type: News
      metrics:
          - type: F1
            name: F1
            value: 0.91
          - type: accuracy
            name: accuracy
            value: 0.91
          - type: precision
            name: precision
            value: 0.91
          - type: recall
            name: recall
            value: 0.91
pipeline_tag: text-classification
---

# roberta-base_topic_classification_nyt_news

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the NYT News dataset, which contains 256,000 news titles from articles published from 2000 to the present (https://www.kaggle.com/datasets/aryansingh0909/nyt-articles-21m-2000-present).
It achieves the following results on the test set of 51200 cases:
- Accuracy: 0.91
- F1: 0.91
- Precision: 0.91
- Recall: 0.91

## Training data
Training data was classified as follow:

class |Description
-|-
0 |Sports
1 |Arts, Culture, and Entertainment
2 |Business and Finance
3 |Health and Wellness
4 |Lifestyle and Fashion
5 |Science and Technology
6 |Politics
7 |Crime

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:------:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.3192        | 1.0   | 20480  | 0.4078          | 0.8865   | 0.8859 | 0.8892    | 0.8865 |
| 0.2863        | 2.0   | 40960  | 0.4271          | 0.8972   | 0.8970 | 0.8982    | 0.8972 |
| 0.1979        | 3.0   | 61440  | 0.3797          | 0.9094   | 0.9092 | 0.9098    | 0.9094 |
| 0.1239        | 4.0   | 81920  | 0.3981          | 0.9117   | 0.9113 | 0.9114    | 0.9117 |
| 0.1472        | 5.0   | 102400 | 0.4033          | 0.9137   | 0.9135 | 0.9134    | 0.9137 |

### Model performance

-|precision|recall|f1|support
-|-|-|-|-
Sports|0.97|0.98|0.97|6400
Arts, Culture, and Entertainment|0.94|0.95|0.94|6400
Business and Finance|0.85|0.84|0.84|6400
Health and Wellness|0.90|0.93|0.91|6400
Lifestyle and Fashion|0.95|0.95|0.95|6400
Science and Technology|0.89|0.83|0.86|6400
Politics|0.93|0.88|0.90|6400
Crime|0.85|0.93|0.89|6400
 | | | |
accuracy|||0.91|51200
macro avg|0.91|0.91|0.91|51200
weighted avg|0.91|0.91|0.91|51200

### How to use roberta-base_topic_classification_nyt_news with HuggingFace

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dstefa/roberta-base_topic_classification_nyt_news")
model = AutoModelForSequenceClassification.from_pretrained("dstefa/roberta-base_topic_classification_nyt_news")
pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)

text = "Kederis proclaims innocence Olympic champion Kostas Kederis today left hospital ahead of his date with IOC inquisitors claiming his innocence and vowing."
pipe(text)

[{'label': 'Sports', 'score': 0.9989326596260071}]

```

### Framework versions

- Transformers 4.32.1
- Pytorch 2.1.0+cu121
- Datasets 2.12.0
- Tokenizers 0.13.2
