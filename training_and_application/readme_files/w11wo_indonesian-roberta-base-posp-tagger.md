---
license: mit
base_model: flax-community/indonesian-roberta-base
tags:
- generated_from_trainer
datasets:
- indonlu
language:
- ind
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: indonesian-roberta-base-posp-tagger
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: indonlu
      type: indonlu
      config: posp
      split: test
      args: posp
    metrics:
    - name: Precision
      type: precision
      value: 0.9625100240577386
    - name: Recall
      type: recall
      value: 0.9625100240577386
    - name: F1
      type: f1
      value: 0.9625100240577386
    - name: Accuracy
      type: accuracy
      value: 0.9625100240577386
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indonesian-roberta-base-posp-tagger

This model is a fine-tuned version of [flax-community/indonesian-roberta-base](https://huggingface.co/flax-community/indonesian-roberta-base) on the indonlu dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1395
- Precision: 0.9625
- Recall: 0.9625
- F1: 0.9625
- Accuracy: 0.9625

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 420  | 0.2254          | 0.9313    | 0.9313 | 0.9313 | 0.9313   |
| 0.4398        | 2.0   | 840  | 0.1617          | 0.9499    | 0.9499 | 0.9499 | 0.9499   |
| 0.1566        | 3.0   | 1260 | 0.1431          | 0.9569    | 0.9569 | 0.9569 | 0.9569   |
| 0.103         | 4.0   | 1680 | 0.1412          | 0.9605    | 0.9605 | 0.9605 | 0.9605   |
| 0.0723        | 5.0   | 2100 | 0.1408          | 0.9635    | 0.9635 | 0.9635 | 0.9635   |
| 0.051         | 6.0   | 2520 | 0.1408          | 0.9642    | 0.9642 | 0.9642 | 0.9642   |
| 0.051         | 7.0   | 2940 | 0.1510          | 0.9635    | 0.9635 | 0.9635 | 0.9635   |
| 0.0368        | 8.0   | 3360 | 0.1653          | 0.9645    | 0.9645 | 0.9645 | 0.9645   |
| 0.0277        | 9.0   | 3780 | 0.1664          | 0.9644    | 0.9644 | 0.9644 | 0.9644   |
| 0.0231        | 10.0  | 4200 | 0.1668          | 0.9646    | 0.9646 | 0.9646 | 0.9646   |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.2.0+cu118
- Datasets 2.16.1
- Tokenizers 0.15.1
