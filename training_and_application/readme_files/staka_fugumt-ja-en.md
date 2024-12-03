---
license: cc-by-sa-4.0

language: 
- en
- ja

tags:
- translation

widget:
- text: "猫はかわいいです。"

---

# FuguMT

This is a translation model using Marian-NMT.
For more details, please see [my repository](https://github.com/s-taka/fugumt).

* source language: ja
* target language: en 

### How to use

This model uses transformers and sentencepiece.
```python
!pip install transformers sentencepiece
```

You can use this model directly with a pipeline:

```python
from transformers import pipeline
fugu_translator = pipeline('translation', model='staka/fugumt-ja-en')
fugu_translator('猫はかわいいです。')
```

### Eval results

The results of the evaluation using [tatoeba](https://tatoeba.org/ja)(randomly selected 500 sentences) are as follows:

|source |target |BLEU(*1)| 
|-------|-------|--------|
|ja     |en     |39.1    |

(*1) sacrebleu