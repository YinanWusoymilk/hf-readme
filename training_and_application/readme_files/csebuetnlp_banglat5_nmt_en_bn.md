---
language: 
- en
- bn
tags:
- translation
licenses:
- cc-by-nc-sa-4.0
---

# banglat5_nmt_en_bn

This repository contains the **BanglaT5** checkpoint finetuned on the [BanglaNMT]() English-Bengali dataset. 

**Note**: The pretrained model uses a specific normalization pipeline available [here](https://github.com/csebuetnlp/normalizer). For best results, make sure the text units are normalized using this library before tokenization.

## Using this model in `transformers` (tested on 4.11.0.dev0)

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from normalizer import normalize # pip install git+https://github.com/csebuetnlp/normalizer

model = AutoModelForSeq2SeqLM.from_pretrained("csebuetnlp/banglat5_nmt_en_bn")
tokenizer = AutoTokenizer.from_pretrained("csebuetnlp/banglat5_nmt_en_bn", use_fast=False)

input_sentence = ""
input_ids = tokenizer(normalize(input_sentence), return_tensors="pt").input_ids
generated_tokens = model.generate(input_ids)
decoded_tokens = tokenizer.batch_decode(generated_tokens)[0]

print(decoded_tokens)
```

## Benchmarks
 
* On BanglaNMT test set:

|     Model          |   Params   |     MT (SacreBLEU)    |
|--------------------|------------|-----------------------|
|[mT5 (base)](https://huggingface.co/google/mt5-base) | 582M  | 22.5 | 
|[XLM-ProphetNet](https://huggingface.co/microsoft/xprophetnet-large-wiki100-cased) | 616M | 16.4 | 
|[mBART-50](https://huggingface.co/facebook/mbart-large-50) | 611M | 16.7 | 
|[IndicBART](https://huggingface.co/ai4bharat/IndicBART) | 244M | 13.1 | 
|[BanglaT5](https://huggingface.co/csebuetnlp/banglat5) | 247M | 25.2 |  



## Citation

If you use this model, please cite the following paper:
```
@article{bhattacharjee2022banglanlg,
  author    = {Abhik Bhattacharjee and Tahmid Hasan and Wasi Uddin Ahmad and Rifat Shahriyar},
  title     = {BanglaNLG: Benchmarks and Resources for Evaluating Low-Resource Natural Language Generation in Bangla},
  journal   = {CoRR},
  volume    = {abs/2205.11081},
  year      = {2022},
  url       = {https://arxiv.org/abs/2205.11081},
  eprinttype = {arXiv},
  eprint    = {2205.11081}
}
```


If you use the normalization module, please cite the following paper:
```
@inproceedings{hasan-etal-2020-low,
    title = "Not Low-Resource Anymore: Aligner Ensembling, Batch Filtering, and New Datasets for {B}engali-{E}nglish Machine Translation",
    author = "Hasan, Tahmid  and
      Bhattacharjee, Abhik  and
      Samin, Kazi  and
      Hasan, Masum  and
      Basak, Madhusudan  and
      Rahman, M. Sohel  and
      Shahriyar, Rifat",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-main.207",
    doi = "10.18653/v1/2020.emnlp-main.207",
    pages = "2612--2623",
    abstract = "Despite being the seventh most widely spoken language in the world, Bengali has received much less attention in machine translation literature due to being low in resources. Most publicly available parallel corpora for Bengali are not large enough; and have rather poor quality, mostly because of incorrect sentence alignments resulting from erroneous sentence segmentation, and also because of a high volume of noise present in them. In this work, we build a customized sentence segmenter for Bengali and propose two novel methods for parallel corpus creation on low-resource setups: aligner ensembling and batch filtering. With the segmenter and the two methods combined, we compile a high-quality Bengali-English parallel corpus comprising of 2.75 million sentence pairs, more than 2 million of which were not available before. Training on neural models, we achieve an improvement of more than 9 BLEU score over previous approaches to Bengali-English machine translation. We also evaluate on a new test set of 1000 pairs made with extensive quality control. We release the segmenter, parallel corpus, and the evaluation set, thus elevating Bengali from its low-resource status. To the best of our knowledge, this is the first ever large scale study on Bengali-English machine translation. We believe our study will pave the way for future research on Bengali-English machine translation as well as other low-resource languages. Our data and code are available at https://github.com/csebuetnlp/banglanmt.",
}
```


