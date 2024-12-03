---
license: apache-2.0
base_model: bert-base-multilingual-cased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-cased-Korean-sentiment
  results: []
datasets:
- WhitePeak/shopping_review
language:
- ko
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cased-Korean-sentiment

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2338
- Accuracy: 0.9234
- F1: 0.9238

## Model description

This is a fine-tuned model for a sentiment analysis for the Korean language based on customer reviews in the Korean language

## Intended uses & limitations

```python
from transformers import pipeline

sentiment_model = pipeline(model="WhitePeak/bert-base-cased-Korean-sentiment")
sentiment_mode("매우 좋아")
```

Result:
```
LABEL_0: negative
LABEL_1: positive
```

## Training and evaluation data


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results



### Framework versions

- Transformers 4.33.2
- Pytorch 2.0.1+cu118
- Datasets 2.14.5
- Tokenizers 0.13.3