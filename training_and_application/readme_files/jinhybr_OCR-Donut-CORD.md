---
license: mit
tags:
- donut
- image-to-text
- vision
---

# Donut (base-sized model, fine-tuned on CORD) 

Donut model fine-tuned on CORD. It was introduced in the paper [OCR-free Document Understanding Transformer](https://arxiv.org/abs/2111.15664) by Geewok et al. and first released in [this repository](https://github.com/clovaai/donut).

Disclaimer: The team releasing Donut did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

Donut consists of a vision encoder (Swin Transformer) and a text decoder (BART). Given an image, the encoder first encodes the image into a tensor of embeddings (of shape batch_size, seq_len, hidden_size), after which the decoder autoregressively generates text, conditioned on the encoding of the encoder. 

![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/donut_architecture.jpg)

## Intended uses & limitations

This model is fine-tuned on CORD, a document parsing dataset.

We refer to the [documentation](https://huggingface.co/docs/transformers/main/en/model_doc/donut) which includes code examples.

## CORD Dataset

CORD: A Consolidated Receipt Dataset for Post-OCR Parsing. 
![cord](https://github.com/clovaai/cord/blob/master/figure/sample.png?raw=true)

