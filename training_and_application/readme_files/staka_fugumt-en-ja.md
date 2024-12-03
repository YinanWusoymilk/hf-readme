---
license: cc-by-sa-4.0

language: 
- en
- ja

tags:
- translation

---

# FuguMT

This is a translation model using Marian-NMT.
For more details, please see [my repository](https://github.com/s-taka/fugumt).

* source language: en
* target language: ja 

### How to use

This model uses transformers and sentencepiece.
```python
!pip install transformers sentencepiece
```

You can use this model directly with a pipeline:
```python
from transformers import pipeline
fugu_translator = pipeline('translation', model='staka/fugumt-en-ja')
fugu_translator('This is a cat.')
```

If you want to translate multiple sentences, we recommend using [pySBD](https://github.com/nipunsadvilkar/pySBD).
```python
!pip install transformers sentencepiece pysbd

import pysbd
seg_en = pysbd.Segmenter(language="en", clean=False)

from transformers import pipeline
fugu_translator = pipeline('translation', model='staka/fugumt-en-ja')
txt = 'This is a cat. It is very cute.'
print(fugu_translator(seg_en.segment(txt)))
```


### Eval results

The results of the evaluation using [tatoeba](https://tatoeba.org/ja)(randomly selected 500 sentences) are as follows:

|source |target |BLEU(*1)| 
|-------|-------|--------|
|en     |ja     |32.7    |

(*1) sacrebleu --tokenize ja-mecab