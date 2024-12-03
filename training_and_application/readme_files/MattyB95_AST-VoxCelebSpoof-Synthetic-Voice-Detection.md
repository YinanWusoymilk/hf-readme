---
license: mit
base_model: MIT/ast-finetuned-audioset-10-10-0.4593
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: AST-VoxCelebSpoof-Synthetic-Voice-Detection
  results: []
datasets:
- MattyB95/VoxCelebSpoof
language:
- en
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AST-VoxCelebSpoof-Synthetic-Voice-Detection

This model is a fine-tuned version of [MIT/ast-finetuned-audioset-10-10-0.4593](https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 89136693248.0
- Accuracy: 0.9999
- F1: 0.9999
- Precision: 1.0
- Recall: 0.9998

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss     | Epoch | Step  | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-----------------:|:-----:|:-----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 2218896740319.232 | 1.0   | 29527 | 611463921664.0  | 0.9998   | 0.9998 | 0.9999    | 0.9997 |
| 522149441830.912  | 2.0   | 59054 | 284563668992.0  | 0.9997   | 0.9997 | 0.9999    | 0.9996 |
| 0.0               | 3.0   | 88581 | 89136693248.0   | 0.9999   | 0.9999 | 1.0       | 0.9998 |


### Framework versions

- Transformers 4.36.2
- Pytorch 2.1.2
- Datasets 2.16.1
- Tokenizers 0.15.0