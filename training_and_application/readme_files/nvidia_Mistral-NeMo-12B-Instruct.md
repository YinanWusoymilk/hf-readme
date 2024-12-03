---
license: apache-2.0
tags:
- nvidia
---

## Mistral-NeMo-12B-Instruct

[![Model architecture](https://img.shields.io/badge/Model%20Arch-Transformer%20Decoder-green)](#model-architecture)[![Model size](https://img.shields.io/badge/Params-12B-green)](#model-architecture)[![Language](https://img.shields.io/badge/Language-Multilingual-green)](#datasets)

### Model Overview:

Mistral-NeMo-12B-Instruct is a Large Language Model (LLM) composed of 12B parameters, trained jointly by NVIDIA and Mistral AI. It significantly outperforms existing models smaller or similar in size.

**Key features**
- Released under the Apache 2 License
- Pre-trained and instructed versions
- Trained with a 128k context window
- Comes with a FP8 quantized version with no accuracy loss
- Trained on a large proportion of multilingual and code data

### Intended use

Mistral-NeMo-12B-Instruct is a chat model intended for use for the English language. 

The instruct model itself can be further customized using the [NeMo Framework](https://docs.nvidia.com/nemo-framework/index.html) suite of customization tools including Parameter-Efficient Fine-Tuning (P-tuning, Adapters, LoRA, and more), and Model Alignment (SFT, SteerLM, RLHF, and more) using [NeMo-Aligner](https://github.com/NVIDIA/NeMo-Aligner).

**Model Developer:** [NVIDIA](https://www.nvidia.com/en-us/) and [MistralAI](https://mistral.ai/)

**Model Dates:** Mistral-NeMo-12B-Instruct was trained between June 2024 and July 2024.

**Data Freshness:** The pretraining data has a cutoff of April 2024.

**Transformers format:** https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407

### Model Architecture:

Mistral-NeMo-12B-Instruct is a transformer model, with the following architecture choices:

- Layers: 40
- Dim: 5,120
- Head dim: 128
- Hidden dim: 14,436
- Activation Function: SwiGLU
- Number of heads: 32
- Number of kv-heads: 8 (GQA)
- Rotary embeddings (theta = 1M)
- Vocabulary size: 2**17 ~= 128k

**Architecture Type:** Transformer Decoder (auto-regressive language model)

### Evaluation Results


- MT Bench (dev): 7.84
- MixEval Hard: 0.534
- IFEval-v5: 0.629
- Wildbench: 42.57

### Limitations

The model was trained on data that contains toxic language, unsafe content, and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive.


### Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

