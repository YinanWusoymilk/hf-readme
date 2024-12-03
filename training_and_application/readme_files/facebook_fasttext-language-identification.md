---
license: cc-by-nc-4.0
library_name: fasttext
tags:
  - text-classification
  - language-identification
---

# fastText (Language Identification)

fastText is an open-source, free, lightweight library that allows users to learn text representations and text classifiers. It works on standard, generic hardware. Models can later be reduced in size to even fit on mobile devices. It was introduced in [this paper](https://arxiv.org/abs/1607.04606). The official website can be found [here](https://fasttext.cc/).

This LID (Language IDentification) model is used to predict the language of the input text, and the hosted version (`lid218e`) was [released as part of the NLLB project](https://github.com/facebookresearch/fairseq/blob/nllb/README.md#lid-model) and can detect 217 languages. You can find older versions (ones that can identify 157 languages) on the [official fastText website](https://fasttext.cc/docs/en/language-identification.html).

## Model description

fastText is a library for efficient learning of word representations and sentence classification. fastText is designed to be simple to use for developers, domain experts, and students. It's dedicated to text classification and learning word representations, and was designed to allow for quick model iteration and refinement without specialized hardware. fastText models can be trained on more than a billion words on any multicore CPU in less than a few minutes.

It includes pre-trained models learned on Wikipedia and in over 157 different languages. fastText can be used as a command line, linked to a C++ application, or used as a library for use cases from experimentation and prototyping to production.

## Intended uses & limitations

You can use pre-trained word vectors for text classification or language identification. See the [tutorials](https://fasttext.cc/docs/en/supervised-tutorial.html) and [resources](https://fasttext.cc/docs/en/english-vectors.html) on its official website to look for tasks that interest you.

### How to use

Here is how to use this model to detect the language of a given text:

```python
>>> import fasttext
>>> from huggingface_hub import hf_hub_download

>>> model_path = hf_hub_download(repo_id="facebook/fasttext-language-identification", filename="model.bin")
>>> model = fasttext.load_model(model_path)
>>> model.predict("Hello, world!")

(('__label__eng_Latn',), array([0.81148803]))

>>> model.predict("Hello, world!", k=5)

(('__label__eng_Latn', '__label__vie_Latn', '__label__nld_Latn', '__label__pol_Latn', '__label__deu_Latn'), 
 array([0.61224753, 0.21323682, 0.09696738, 0.01359863, 0.01319415]))
```

### Limitations and bias

Even if the training data used for this model could be characterized as fairly neutral, this model can have biased predictions. 

Cosine similarity can be used to measure the similarity between two different word vectors. If two two vectors are identical, the cosine similarity will be 1. For two completely unrelated vectors, the value will be 0. If two vectors have an opposite relationship, the value will be -1.

```python
>>> import numpy as np

>>> def cosine_similarity(word1, word2):
>>>     return np.dot(model[word1], model[word2]) / (np.linalg.norm(model[word1]) * np.linalg.norm(model[word2]))

>>> cosine_similarity("man", "boy")

0.061653383

>>> cosine_similarity("man", "ceo")

0.11989131

>>> cosine_similarity("woman", "ceo")

-0.08834904
```

## Training data

Pre-trained word vectors for 157 languages were trained on [Common Crawl](http://commoncrawl.org/) and [Wikipedia](https://www.wikipedia.org/) using fastText. These models were trained using CBOW with position-weights, in dimension 300, with character n-grams of length 5, a window of size 5 and 10 negatives. We also distribute three new word analogy datasets, for French, Hindi and Polish.

## Training procedure

### Tokenization

We used the [Stanford word segmenter](https://nlp.stanford.edu/software/segmenter.html) for Chinese, [Mecab](http://taku910.github.io/mecab/) for Japanese and [UETsegmenter](https://github.com/phongnt570/UETsegmenter) for Vietnamese. For languages using the Latin, Cyrillic, Hebrew or Greek scripts, we used the tokenizer from the [Europarl](https://www.statmt.org/europarl/) preprocessing tools. For the remaining languages, we used the ICU tokenizer.

More information about the training of these models can be found in the article [Learning Word Vectors for 157 Languages](https://arxiv.org/abs/1802.06893).

### License

The language identification model is distributed under the [*Creative Commons Attribution-NonCommercial 4.0 International Public License*](https://creativecommons.org/licenses/by-nc/4.0/).

### Evaluation datasets

The analogy evaluation datasets described in the paper are available here: [French](https://dl.fbaipublicfiles.com/fasttext/word-analogies/questions-words-fr.txt), [Hindi](https://dl.fbaipublicfiles.com/fasttext/word-analogies/questions-words-hi.txt), [Polish](https://dl.fbaipublicfiles.com/fasttext/word-analogies/questions-words-pl.txt).

### BibTeX entry and citation info

Please cite [1] if using this code for learning word representations or [2] if using for text classification.

[1] P. Bojanowski\*, E. Grave\*, A. Joulin, T. Mikolov, [*Enriching Word Vectors with Subword Information*](https://arxiv.org/abs/1607.04606)

```markup
@article{bojanowski2016enriching,
  title={Enriching Word Vectors with Subword Information},
  author={Bojanowski, Piotr and Grave, Edouard and Joulin, Armand and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1607.04606},
  year={2016}
}
```

[2] A. Joulin, E. Grave, P. Bojanowski, T. Mikolov, [*Bag of Tricks for Efficient Text Classification*](https://arxiv.org/abs/1607.01759)

```markup
@article{joulin2016bag,
  title={Bag of Tricks for Efficient Text Classification},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1607.01759},
  year={2016}
}
```

[3] A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, T. Mikolov, [*FastText.zip: Compressing text classification models*](https://arxiv.org/abs/1612.03651)

```markup
@article{joulin2016fasttext,
  title={FastText.zip: Compressing text classification models},
  author={Joulin, Armand and Grave, Edouard and Bojanowski, Piotr and Douze, Matthijs and J{'e}gou, H{'e}rve and Mikolov, Tomas},
  journal={arXiv preprint arXiv:1612.03651},
  year={2016}
}
```

If you use these word vectors, please cite the following paper:

[4] E. Grave\*, P. Bojanowski\*, P. Gupta, A. Joulin, T. Mikolov, [*Learning Word Vectors for 157 Languages*](https://arxiv.org/abs/1802.06893)

```markup
@inproceedings{grave2018learning,
  title={Learning Word Vectors for 157 Languages},
  author={Grave, Edouard and Bojanowski, Piotr and Gupta, Prakhar and Joulin, Armand and Mikolov, Tomas},
  booktitle={Proceedings of the International Conference on Language Resources and Evaluation (LREC 2018)},
  year={2018}
}
```

(\* These authors contributed equally.)

