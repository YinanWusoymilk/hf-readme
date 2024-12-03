---
license: apache-2.0
tags:
- audio-classification
- generated_from_trainer
datasets:
- xtreme_s
metrics:
- accuracy
base_model: openai/whisper-medium
model-index:
- name: whisper-medium-fleurs-lang-id
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium FLEURS Language Identification

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the [FLEURS subset](https://huggingface.co/datasets/google/xtreme_s#language-identification---fleurs-langid) of the [google/xtreme_s](https://huggingface.co/google/xtreme_s) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8413
- Accuracy: 0.8805

To reproduce this run, execute the command in [`run.sh`](https://huggingface.co/sanchit-gandhi/whisper-medium-fleurs-lang-id/blob/main/run.sh).

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 0
- distributed_type: multi-GPU
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.0152        | 1.0   | 8494  | 0.9087          | 0.8431   |
| 0.0003        | 2.0   | 16988 | 1.0059          | 0.8460   |
| 0.0           | 3.0   | 25482 | 0.8413          | 0.8805   |


### Framework versions

- Transformers 4.27.0.dev0
- Pytorch 1.13.1
- Datasets 2.9.0
- Tokenizers 0.13.2
