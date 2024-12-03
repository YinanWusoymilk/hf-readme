---
language: fr
license: mit
tags:
  - "historic french"
---
# 🤗 + 📚 dbmdz BERT model

In this repository the MDZ Digital Library team (dbmdz) at the Bavarian State
Library open sources French Europeana BERT models 🎉

# French Europeana BERT

We extracted all French texts using the `language` metadata attribute from the Europeana corpus.

The resulting corpus has a size of 63GB and consists of 11,052,528,456 tokens.

Based on the metadata information, texts from the 18th - 20th century are mainly included in the
training corpus.

Detailed information about the data and pretraining steps can be found in
[this repository](https://github.com/stefan-it/europeana-bert).

## Model weights

BERT model weights for PyTorch and TensorFlow are available.

* French Europeana BERT: `dbmdz/bert-base-french-europeana-cased` - [model hub page](https://huggingface.co/dbmdz/bert-base-french-europeana-cased/tree/main)

## Results

For results on Historic NER, please refer to [this repository](https://github.com/stefan-it/europeana-bert).

## Usage

With Transformers >= 2.3 our French Europeana BERT model can be loaded like:

```python
from transformers import AutoModel, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-french-europeana-cased")
model = AutoModel.from_pretrained("dbmdz/bert-base-french-europeana-cased")
```

# Huggingface model hub

All models are available on the [Huggingface model hub](https://huggingface.co/dbmdz).

# Contact (Bugs, Feedback, Contribution and more)

For questions about our BERT model just open an issue
[here](https://github.com/dbmdz/berts/issues/new) 🤗

# Acknowledgments

Research supported with Cloud TPUs from Google's TensorFlow Research Cloud (TFRC).
Thanks for providing access to the TFRC ❤️

Thanks to the generous support from the [Hugging Face](https://huggingface.co/) team,
it is possible to download our model from their S3 storage 🤗
