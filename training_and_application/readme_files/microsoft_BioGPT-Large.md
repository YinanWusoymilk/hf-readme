---
license: mit
datasets:
- pubmed
language:
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- medical
widget:
- text: COVID-19 is
inference:
  parameters:
    max_new_tokens: 50
---

## BioGPT

Pre-trained language models have attracted increasing attention in the biomedical domain, inspired by their great success in the general natural language domain. Among the two main branches of pre-trained language models in the general language domain, i.e. BERT (and its variants) and GPT (and its variants), the first one has been extensively studied in the biomedical domain, such as BioBERT and PubMedBERT. While they have achieved great success on a variety of discriminative downstream biomedical tasks, the lack of generation ability constrains their application scope. In this paper, we propose BioGPT, a domain-specific generative Transformer language model pre-trained on large-scale biomedical literature. We evaluate BioGPT on six biomedical natural language processing tasks and demonstrate that our model outperforms previous models on most tasks. Especially, we get 44.98%, 38.42% and 40.76% F1 score on BC5CDR, KD-DTI and DDI end-to-end relation extraction tasks, respectively, and 78.2% accuracy on PubMedQA, creating a new record. Our case study on text generation further demonstrates the advantage of BioGPT on biomedical literature to generate fluent descriptions for biomedical terms.


## Citation

If you find BioGPT useful in your research, please cite the following paper:

```latex
@article{10.1093/bib/bbac409,
    author = {Luo, Renqian and Sun, Liai and Xia, Yingce and Qin, Tao and Zhang, Sheng and Poon, Hoifung and Liu, Tie-Yan},
    title = "{BioGPT: generative pre-trained transformer for biomedical text generation and mining}",
    journal = {Briefings in Bioinformatics},
    volume = {23},
    number = {6},
    year = {2022},
    month = {09},
    abstract = "{Pre-trained language models have attracted increasing attention in the biomedical domain, inspired by their great success in the general natural language domain. Among the two main branches of pre-trained language models in the general language domain, i.e. BERT (and its variants) and GPT (and its variants), the first one has been extensively studied in the biomedical domain, such as BioBERT and PubMedBERT. While they have achieved great success on a variety of discriminative downstream biomedical tasks, the lack of generation ability constrains their application scope. In this paper, we propose BioGPT, a domain-specific generative Transformer language model pre-trained on large-scale biomedical literature. We evaluate BioGPT on six biomedical natural language processing tasks and demonstrate that our model outperforms previous models on most tasks. Especially, we get 44.98\%, 38.42\% and 40.76\% F1 score on BC5CDR, KD-DTI and DDI end-to-end relation extraction tasks, respectively, and 78.2\% accuracy on PubMedQA, creating a new record. Our case study on text generation further demonstrates the advantage of BioGPT on biomedical literature to generate fluent descriptions for biomedical terms.}",
    issn = {1477-4054},
    doi = {10.1093/bib/bbac409},
    url = {https://doi.org/10.1093/bib/bbac409},
    note = {bbac409},
    eprint = {https://academic.oup.com/bib/article-pdf/23/6/bbac409/47144271/bbac409.pdf},
}
```