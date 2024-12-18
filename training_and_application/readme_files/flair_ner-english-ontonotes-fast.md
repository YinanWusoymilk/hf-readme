---
tags:
- flair
- token-classification
- sequence-tagger-model
language: en
datasets:
- ontonotes
widget:
- text: "On September 1st George Washington won 1 dollar."
---

## English NER in Flair (Ontonotes fast model)

This is the fast version of the 18-class NER model for English that ships with [Flair](https://github.com/flairNLP/flair/).

F1-Score: **89.3** (Ontonotes)

Predicts 18 tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| CARDINAL    | cardinal value | 
| DATE         | date value | 
| EVENT         | event name | 
| FAC         | building name | 
| GPE         | geo-political entity | 
| LANGUAGE         | language name | 
| LAW         | law name | 
| LOC         | location name | 
| MONEY         | money name | 
| NORP         | affiliation | 
| ORDINAL         | ordinal value | 
| ORG         | organization name | 
| PERCENT         | percent value | 
| PERSON         | person name | 
| PRODUCT         | product name | 
| QUANTITY         | quantity value | 
| TIME         | time value | 
| WORK_OF_ART         | name of work of art | 

Based on [Flair embeddings](https://www.aclweb.org/anthology/C18-1139/) and LSTM-CRF.

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger

# load tagger
tagger = SequenceTagger.load("flair/ner-english-ontonotes-fast")

# make example sentence
sentence = Sentence("On September 1st George Washington won 1 dollar.")

# predict NER tags
tagger.predict(sentence)

# print sentence
print(sentence)

# print predicted NER spans
print('The following NER tags are found:')
# iterate over entities and print
for entity in sentence.get_spans('ner'):
    print(entity)

```

This yields the following output:
```
Span [2,3]: "September 1st"   [− Labels: DATE (0.9655)]
Span [4,5]: "George Washington"   [− Labels: PERSON (0.8243)]
Span [7,8]: "1 dollar"   [− Labels: MONEY (0.8022)]
```

So, the entities "*September 1st*" (labeled as a **date**), "*George Washington*" (labeled as a **person**) and "*1 dollar*" (labeled as a **money**) are found in the sentence "*On September 1st George Washington won 1 dollar*". 


---

### Training: Script to train this model

The following Flair script was used to train this model: 

```python
from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import WordEmbeddings, StackedEmbeddings, FlairEmbeddings

# 1. load the corpus (Ontonotes does not ship with Flair, you need to download and reformat into a column format yourself)
corpus: Corpus = ColumnCorpus(
                "resources/tasks/onto-ner",
                column_format={0: "text", 1: "pos", 2: "upos", 3: "ner"},
                tag_to_bioes="ner",
            )

# 2. what tag do we want to predict?
tag_type = 'ner'

# 3. make the tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# 4. initialize each embedding we use
embedding_types = [

    # GloVe embeddings
    WordEmbeddings('en-crawl'),

    # contextual string embeddings, forward
    FlairEmbeddings('news-forward-fast'),

    # contextual string embeddings, backward
    FlairEmbeddings('news-backward-fast'),
]

# embedding stack consists of Flair and GloVe embeddings
embeddings = StackedEmbeddings(embeddings=embedding_types)

# 5. initialize sequence tagger
from flair.models import SequenceTagger

tagger = SequenceTagger(hidden_size=256,
                        embeddings=embeddings,
                        tag_dictionary=tag_dictionary,
                        tag_type=tag_type)

# 6. initialize trainer
from flair.trainers import ModelTrainer

trainer = ModelTrainer(tagger, corpus)

# 7. run training
trainer.train('resources/taggers/ner-english-ontonotes-fast',
              train_with_dev=True,
              max_epochs=150)
```



---

### Cite

Please cite the following paper when using this model.

```
@inproceedings{akbik2018coling,
  title={Contextual String Embeddings for Sequence Labeling},
  author={Akbik, Alan and Blythe, Duncan and Vollgraf, Roland},
  booktitle = {{COLING} 2018, 27th International Conference on Computational Linguistics},
  pages     = {1638--1649},
  year      = {2018}
}
```

---

### Issues?

The Flair issue tracker is available [here](https://github.com/flairNLP/flair/issues/).
