---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: stevhliu/my_awesome_model
  results: []
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# stevhliu/my_awesome_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Train Loss: 0.0632
- Validation Loss: 0.2355
- Train Accuracy: 0.9295
- Epoch: 2

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'Adam', 'learning_rate': {'class_name': 'PolynomialDecay', 'config': {'initial_learning_rate': 2e-05, 'decay_steps': 7810, 'end_learning_rate': 0.0, 'power': 1.0, 'cycle': False, 'name': None}}, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-08, 'amsgrad': False}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Train Accuracy | Epoch |
|:----------:|:---------------:|:--------------:|:-----:|
| 0.2518     | 0.1859          | 0.9261         | 0     |
| 0.1319     | 0.1822          | 0.9318         | 1     |
| 0.0632     | 0.2355          | 0.9295         | 2     |


### Framework versions

- Transformers 4.22.2
- TensorFlow 2.8.2
- Datasets 2.5.1
- Tokenizers 0.12.1
