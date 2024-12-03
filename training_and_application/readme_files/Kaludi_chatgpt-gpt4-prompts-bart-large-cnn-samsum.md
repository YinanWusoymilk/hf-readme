---
license: mit
tags:
- generated_from_keras_callback
model-index:
- name: chatgpt-gpt4-prompts-bart-large-cnn-samsum
  results: []
datasets:
- fka/awesome-chatgpt-prompts
---

<!-- This model card has been generated automatically according to the information Keras had access to. You should
probably proofread and complete it, then remove this comment. -->

# chatgpt-gpt4-prompts-bart-large-cnn-samsum

This model generates ChatGPT/BingChat & GPT-3 prompts and is a fine-tuned version of [philschmid/bart-large-cnn-samsum](https://huggingface.co/philschmid/bart-large-cnn-samsum) on an [this](https://huggingface.co/datasets/fka/awesome-chatgpt-prompts) dataset.
It achieves the following results on the evaluation set:
- Train Loss: 1.2214
- Validation Loss: 2.7584
- Epoch: 4

### Streamlit

This model supports a [Streamlit](https://streamlit.io/) Web UI to run the chatgpt-gpt4-prompts-bart-large-cnn-samsum model:
[![Open In HF Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/Kaludi/ChatGPT-BingChat-GPT3-Prompt-Generator_App)

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 3.1982     | 2.6801          | 0     |
| 2.3601     | 2.5493          | 1     |
| 1.9225     | 2.5377          | 2     |
| 1.5465     | 2.6794          | 3     |
| 1.2214     | 2.7584          | 4     |


### Framework versions

- Transformers 4.27.3
- TensorFlow 2.11.0
- Datasets 2.10.1
- Tokenizers 0.13.2