---
language:
- ces
- slk
- cs
- sk
- en
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-en-ces_slk
  results:
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng ces devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 34.1
  - task:
      name: Translation eng-slk
      type: translation
      args: eng-slk
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng slk devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 35.9
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: multi30k_test_2016_flickr
      type: multi30k-2016_flickr
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 33.4
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: multi30k_test_2018_flickr
      type: multi30k-2018_flickr
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 33.4
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: news-test2008
      type: news-test2008
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 22.8
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 47.5
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: newstest2009
      type: wmt-2009-news
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 24.3
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: newstest2010
      type: wmt-2010-news
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 24.4
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: newstest2011
      type: wmt-2011-news
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 25.5
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: newstest2012
      type: wmt-2012-news
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 22.6
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: newstest2013
      type: wmt-2013-news
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 27.4
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: newstest2014
      type: wmt-2014-news
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 31.4
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: newstest2015
      type: wmt-2015-news
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 27.0
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: newstest2016
      type: wmt-2016-news
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 29.9
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: newstest2017
      type: wmt-2017-news
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 24.9
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: newstest2018
      type: wmt-2018-news
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 24.6
  - task:
      name: Translation eng-ces
      type: translation
      args: eng-ces
    dataset:
      name: newstest2019
      type: wmt-2019-news
      args: eng-ces
    metrics:
    - name: BLEU
      type: bleu
      value: 26.4
---
# opus-mt-tc-big-en-ces_slk

Neural machine translation model for translating from English (en) to Czech and Slovak (ces+slk).

This model is part of the [OPUS-MT project](https://github.com/Helsinki-NLP/Opus-MT), an effort to make neural machine translation models widely available and accessible for many languages in the world. All models are originally trained using the amazing framework of [Marian NMT](https://marian-nmt.github.io/), an efficient NMT implementation written in pure C++. The models have been converted to pyTorch using the transformers library by huggingface. Training data is taken from [OPUS](https://opus.nlpl.eu/) and training pipelines use the procedures of [OPUS-MT-train](https://github.com/Helsinki-NLP/Opus-MT-train).

* Publications: [OPUS-MT – Building open translation services for the World](https://aclanthology.org/2020.eamt-1.61/) and [The Tatoeba Translation Challenge – Realistic Data Sets for Low Resource and Multilingual MT](https://aclanthology.org/2020.wmt-1.139/) (Please, cite if you use this model.)

```
@inproceedings{tiedemann-thottingal-2020-opus,
    title = "{OPUS}-{MT} {--} Building open translation services for the World",
    author = {Tiedemann, J{\"o}rg  and Thottingal, Santhosh},
    booktitle = "Proceedings of the 22nd Annual Conference of the European Association for Machine Translation",
    month = nov,
    year = "2020",
    address = "Lisboa, Portugal",
    publisher = "European Association for Machine Translation",
    url = "https://aclanthology.org/2020.eamt-1.61",
    pages = "479--480",
}

@inproceedings{tiedemann-2020-tatoeba,
    title = "The Tatoeba Translation Challenge {--} Realistic Data Sets for Low Resource and Multilingual {MT}",
    author = {Tiedemann, J{\"o}rg},
    booktitle = "Proceedings of the Fifth Conference on Machine Translation",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.wmt-1.139",
    pages = "1174--1182",
}
```

## Model info

* Release: 2022-03-13
* source language(s): eng
* target language(s): ces
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-03-13.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ces+slk/opusTCv20210807+bt_transformer-big_2022-03-13.zip)
* more information released models: [OPUS-MT eng-ces+slk README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-ces+slk/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    ">>ces<< We were enemies.",
    ">>ces<< Do you think Tom knows what's going on?"
]

model_name = "pytorch-models/opus-mt-tc-big-en-ces_slk"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Byli jsme nepřátelé.
#     Myslíš, že Tom ví, co se děje?
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-ces_slk")
print(pipe(">>ces<< We were enemies."))

# expected output: Byli jsme nepřátelé.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-03-13.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ces+slk/opusTCv20210807+bt_transformer-big_2022-03-13.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-03-13.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-ces+slk/opusTCv20210807+bt_transformer-big_2022-03-13.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| eng-ces | tatoeba-test-v2021-08-07 | 0.66128 | 47.5 | 13824 | 91332 |
| eng-ces | flores101-devtest | 0.60411 | 34.1 | 1012 | 22101 |
| eng-slk | flores101-devtest | 0.62415 | 35.9 | 1012 | 22543 |
| eng-ces | multi30k_test_2016_flickr | 0.58547 | 33.4 | 1000 | 10503 |
| eng-ces | multi30k_test_2018_flickr | 0.59236 | 33.4 | 1071 | 11631 |
| eng-ces | newssyscomb2009 | 0.52702 | 25.3 | 502 | 10032 |
| eng-ces | news-test2008 | 0.50286 | 22.8 | 2051 | 42484 |
| eng-ces | newstest2009 | 0.52152 | 24.3 | 2525 | 55533 |
| eng-ces | newstest2010 | 0.52527 | 24.4 | 2489 | 52955 |
| eng-ces | newstest2011 | 0.52721 | 25.5 | 3003 | 65653 |
| eng-ces | newstest2012 | 0.50007 | 22.6 | 3003 | 65456 |
| eng-ces | newstest2013 | 0.53643 | 27.4 | 3000 | 57250 |
| eng-ces | newstest2014 | 0.58944 | 31.4 | 3003 | 59902 |
| eng-ces | newstest2015 | 0.55094 | 27.0 | 2656 | 45858 |
| eng-ces | newstest2016 | 0.56864 | 29.9 | 2999 | 56998 |
| eng-ces | newstest2017 | 0.52504 | 24.9 | 3005 | 54361 |
| eng-ces | newstest2018 | 0.52490 | 24.6 | 2983 | 54652 |
| eng-ces | newstest2019 | 0.53994 | 26.4 | 1997 | 43113 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 16:46:48 EEST 2022
* port machine: LM0-400-22516.local
