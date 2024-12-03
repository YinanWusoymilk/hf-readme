---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: lm-ner-linkedin-skills-recognition
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# lm-ner-linkedin-skills-recognition

This model is a fine-tuned version of [algiraldohe/distilbert-base-uncased-linkedin-domain-adaptation](https://huggingface.co/algiraldohe/distilbert-base-uncased-linkedin-domain-adaptation) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0307
- Precision: 0.9119
- Recall: 0.9312
- F1: 0.9214
- Accuracy: 0.9912

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1301        | 1.0   | 729  | 0.0468          | 0.8786    | 0.8715 | 0.8750 | 0.9863   |
| 0.0432        | 2.0   | 1458 | 0.0345          | 0.8994    | 0.9219 | 0.9105 | 0.9900   |
| 0.0332        | 3.0   | 2187 | 0.0307          | 0.9119    | 0.9312 | 0.9214 | 0.9912   |


### Framework versions

- Transformers 4.30.2
- Pytorch 2.0.1+cu118
- Datasets 2.13.1
- Tokenizers 0.13.3
