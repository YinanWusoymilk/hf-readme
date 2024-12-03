---
language: de

widget:
- text: "Heute ist sehr schönes Wetter in"

license: mit
---

# German GPT-2 model

In this repository we release (yet another) GPT-2 model, that was trained on various texts for German.

The model is meant to be an entry point for fine-tuning on other texts, and it is definitely not as good or "dangerous" as the English GPT-3 model. We do not plan extensive PR or staged releases for this model 😉

**Note**: The model was initially released under an anonymous alias (`anonymous-german-nlp/german-gpt2`) so we now "de-anonymize" it.

More details about GPT-2 can be found in the great [Hugging Face](https://huggingface.co/transformers/model_doc/gpt2.html) documentation.

# Changelog

16.08.2021: Public release of re-trained version of our German GPT-2 model with better results.

15.11.2020: Initial release. Please use the tag `v1.0` for [this older version](https://huggingface.co/dbmdz/german-gpt2/tree/v1.0).

# Training corpora

We use pretty much the same corpora as used for training the DBMDZ BERT model, that can be found in [this repository](https://github.com/dbmdz/berts).

Thanks to the awesome Hugging Face team, it is possible to create byte-level BPE with their awesome [Tokenizers](https://github.com/huggingface/tokenizers) library.

With the previously mentioned awesome Tokenizers library we created a 50K byte-level BPE vocab based on the training corpora.

After creating the vocab, we could train the GPT-2 for German on a v3-8 TPU over the complete training corpus for 20 epochs. All hyperparameters
can be found in the official JAX/FLAX documentation [here](https://github.com/huggingface/transformers/blob/master/examples/flax/language-modeling/README.md)
from Transformers.

# Using the model

The model itself can be used in this way:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("dbmdz/german-gpt2")

model = AutoModelWithLMHead.from_pretrained("dbmdz/german-gpt2")
```

However, text generation is a bit more interesting, so here's an example that shows how to use the great Transformers *Pipelines* for generating text:

```python
from transformers import pipeline

pipe = pipeline('text-generation', model="dbmdz/german-gpt2",
                 tokenizer="dbmdz/german-gpt2")

text = pipe("Der Sinn des Lebens ist es", max_length=100)[0]["generated_text"]

print(text)
```

This could output this beautiful text:

```
Der Sinn des Lebens ist es, im Geist zu verweilen, aber nicht in der Welt zu sein, sondern ganz im Geist zu leben.
Die Menschen beginnen, sich nicht nach der Natur und nach der Welt zu richten, sondern nach der Seele,'
```

# License

All models are licensed under [MIT](LICENSE).

# Huggingface model hub

All models are available on the [Huggingface model hub](https://huggingface.co/dbmdz).

# Contact (Bugs, Feedback, Contribution and more)

For questions about our BERT models just open an issue
[here](https://github.com/stefan-it/german-gpt/issues/new) 🤗

# Acknowledgments

Research supported with Cloud TPUs from Google's TensorFlow Research Cloud (TFRC).
Thanks for providing access to the TFRC ❤️

Thanks to the generous support from the [Hugging Face](https://huggingface.co/) team,
it is possible to download both cased and uncased models from their S3 storage 🤗

