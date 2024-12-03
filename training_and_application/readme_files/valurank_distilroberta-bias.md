---
license: other
language: en
datasets:
- valurank/wikirev-bias
---
# DistilROBERTA fine-tuned for bias detection

This model is based on [distilroberta-base](https://huggingface.co/distilroberta-base) pretrained weights, with a classification head fine-tuned to classify text into 2 categories (neutral, biased).

## Training data
The dataset used to fine-tune the model is [wikirev-bias](https://huggingface.co/datasets/valurank/wikirev-bias), extracted from English wikipedia revisions, see https://github.com/rpryzant/neutralizing-bias for details on the WNC wiki edits corpus.

## Inputs
Similar to its base model, this model accepts inputs with a maximum length of 512 tokens.

