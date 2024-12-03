---
license: apache-2.0
base_model: google/vit-large-patch16-224-in21k
tags:
- image-classification
- vision
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: fashion-images-gender-age-vit-large-patch16-224-in21k-v3
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: touchtech/fashion-images-gender-age
      type: imagefolder
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9959630911188004
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fashion-images-gender-age-vit-large-patch16-224-in21k-v3

This model is a fine-tuned version of [google/vit-large-patch16-224-in21k](https://huggingface.co/google/vit-large-patch16-224-in21k) on the touchtech/fashion-images-gender-age dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0223
- Accuracy: 0.9960

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 1337
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.1868        | 1.0   | 2457  | 0.0547          | 0.9853   |
| 0.1209        | 2.0   | 4914  | 0.0401          | 0.9888   |
| 0.1027        | 3.0   | 7371  | 0.0262          | 0.9937   |
| 0.0654        | 4.0   | 9828  | 0.0223          | 0.9960   |
| 0.0542        | 5.0   | 12285 | 0.0273          | 0.9948   |


### Framework versions

- Transformers 4.33.0.dev0
- Pytorch 2.0.1+cu118
- Datasets 2.14.5
- Tokenizers 0.13.3
