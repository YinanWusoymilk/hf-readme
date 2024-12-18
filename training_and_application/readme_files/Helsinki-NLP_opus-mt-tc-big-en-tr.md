---
language:
- en
- tr
tags:
- translation
- opus-mt-tc
license: cc-by-4.0
model-index:
- name: opus-mt-tc-big-en-tr
  results:
  - task:
      name: Translation eng-tur
      type: translation
      args: eng-tur
    dataset:
      name: flores101-devtest
      type: flores_101
      args: eng tur devtest
    metrics:
    - name: BLEU
      type: bleu
      value: 31.4
  - task:
      name: Translation eng-tur
      type: translation
      args: eng-tur
    dataset:
      name: newsdev2016
      type: newsdev2016
      args: eng-tur
    metrics:
    - name: BLEU
      type: bleu
      value: 21.9
  - task:
      name: Translation eng-tur
      type: translation
      args: eng-tur
    dataset:
      name: tatoeba-test-v2021-08-07
      type: tatoeba_mt
      args: eng-tur
    metrics:
    - name: BLEU
      type: bleu
      value: 42.3
  - task:
      name: Translation eng-tur
      type: translation
      args: eng-tur
    dataset:
      name: newstest2016
      type: wmt-2016-news
      args: eng-tur
    metrics:
    - name: BLEU
      type: bleu
      value: 23.4
  - task:
      name: Translation eng-tur
      type: translation
      args: eng-tur
    dataset:
      name: newstest2017
      type: wmt-2017-news
      args: eng-tur
    metrics:
    - name: BLEU
      type: bleu
      value: 25.4
  - task:
      name: Translation eng-tur
      type: translation
      args: eng-tur
    dataset:
      name: newstest2018
      type: wmt-2018-news
      args: eng-tur
    metrics:
    - name: BLEU
      type: bleu
      value: 22.6
---
# opus-mt-tc-big-en-tr

Neural machine translation model for translating from English (en) to Turkish (tr).

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

* Release: 2022-02-25
* source language(s): eng
* target language(s): tur
* model: transformer-big
* data: opusTCv20210807+bt ([source](https://github.com/Helsinki-NLP/Tatoeba-Challenge))
* tokenization: SentencePiece (spm32k,spm32k)
* original model: [opusTCv20210807+bt_transformer-big_2022-02-25.zip](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tur/opusTCv20210807+bt_transformer-big_2022-02-25.zip)
* more information released models: [OPUS-MT eng-tur README](https://github.com/Helsinki-NLP/Tatoeba-Challenge/tree/master/models/eng-tur/README.md)

## Usage

A short example code:

```python
from transformers import MarianMTModel, MarianTokenizer

src_text = [
    "I know Tom didn't want to eat that.",
    "On Sundays, we would get up early and go fishing."
]

model_name = "pytorch-models/opus-mt-tc-big-en-tr"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))

for t in translated:
    print( tokenizer.decode(t, skip_special_tokens=True) )

# expected output:
#     Tom'un bunu yemek istemediğini biliyorum.
#     Pazar günleri erkenden kalkıp balık tutmaya giderdik.
```

You can also use OPUS-MT models with the transformers pipelines, for example:

```python
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-tr")
print(pipe("I know Tom didn't want to eat that."))

# expected output: Tom'un bunu yemek istemediğini biliyorum.
```

## Benchmarks

* test set translations: [opusTCv20210807+bt_transformer-big_2022-02-25.test.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tur/opusTCv20210807+bt_transformer-big_2022-02-25.test.txt)
* test set scores: [opusTCv20210807+bt_transformer-big_2022-02-25.eval.txt](https://object.pouta.csc.fi/Tatoeba-MT-models/eng-tur/opusTCv20210807+bt_transformer-big_2022-02-25.eval.txt)
* benchmark results: [benchmark_results.txt](benchmark_results.txt)
* benchmark output: [benchmark_translations.zip](benchmark_translations.zip)

| langpair | testset | chr-F | BLEU  | #sent | #words |
|----------|---------|-------|-------|-------|--------|
| eng-tur | tatoeba-test-v2021-08-07 | 0.68726 | 42.3 | 13907 | 84364 |
| eng-tur | flores101-devtest | 0.62829 | 31.4 | 1012 | 20253 |
| eng-tur | newsdev2016 | 0.58947 | 21.9 | 1001 | 15958 |
| eng-tur | newstest2016 | 0.57624 | 23.4 | 3000 | 50782 |
| eng-tur | newstest2017 | 0.58858 | 25.4 | 3007 | 51977 |
| eng-tur | newstest2018 | 0.57848 | 22.6 | 3000 | 53731 |

## Acknowledgements

The work is supported by the [European Language Grid](https://www.european-language-grid.eu/) as [pilot project 2866](https://live.european-language-grid.eu/catalogue/#/resource/projects/2866), by the [FoTran project](https://www.helsinki.fi/en/researchgroups/natural-language-understanding-with-cross-lingual-grounding), funded by the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 771113), and the [MeMAD project](https://memad.eu/), funded by the European Union’s Horizon 2020 Research and Innovation Programme under grant agreement No 780069. We are also grateful for the generous computational resources and IT infrastructure provided by [CSC -- IT Center for Science](https://www.csc.fi/), Finland.

## Model conversion info

* transformers version: 4.16.2
* OPUS-MT git hash: 3405783
* port time: Wed Apr 13 18:11:39 EEST 2022
* port machine: LM0-400-22516.local
