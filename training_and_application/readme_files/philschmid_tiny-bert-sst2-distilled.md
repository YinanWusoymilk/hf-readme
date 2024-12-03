---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: tiny-bert-sst2-distilled
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: sst2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8325688073394495
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tiny-bert-sst2-distilled

This model is a fine-tuned version of [google/bert_uncased_L-2_H-128_A-2](https://huggingface.co/google/bert_uncased_L-2_H-128_A-2) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7305
- Accuracy: 0.8326

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0007199555649276667
- train_batch_size: 1024
- eval_batch_size: 1024
- seed: 33
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.77          | 1.0   | 66   | 1.6939          | 0.8165   |
| 0.729         | 2.0   | 132  | 1.5090          | 0.8326   |
| 0.5242        | 3.0   | 198  | 1.5369          | 0.8257   |
| 0.4017        | 4.0   | 264  | 1.7025          | 0.8326   |
| 0.327         | 5.0   | 330  | 1.6743          | 0.8245   |
| 0.2749        | 6.0   | 396  | 1.7305          | 0.8337   |
| 0.2521        | 7.0   | 462  | 1.7305          | 0.8326   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.9.1
- Datasets 1.15.1
- Tokenizers 0.10.3
