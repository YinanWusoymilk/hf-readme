---
language: 
  - ar
tags:
  - Arabic BERT
  - MSA
  - Twitter
  - Masked Langauge Model
widget:
  - text: "اللغة [MASK] هي لغة العرب"

---
<img src="https://raw.githubusercontent.com/UBC-NLP/marbert/main/ARBERT_MARBERT.jpg" alt="drawing" width="25%" height="25%" align="right"/>

**ARBERTv2** is the updated version of ARBERT model described in our **ACL 2021 paper** **["ARBERT & MARBERT: Deep Bidirectional Transformers for Arabic"](https://aclanthology.org/2021.acl-long.551.pdf)**. 
**ARBERTv2** is presented in our paper ["ORCA: A Challenging Benchmark for Arabic Language Understanding"](https://arxiv.org/abs/2212.10758)
**ARBERTv2** is trained on MSA data **243 GB** of text and **27.8B tokens**. 



# BibTex

If you use our models (ARBERTv2) for your scientific publication, or if you find the resources in this repository useful, please cite our paper as follows (to be updated):
```bibtex
@inproceedings{abdul-mageed-etal-2021-arbert,
    title = "{ARBERT} {\&} {MARBERT}: Deep Bidirectional Transformers for {A}rabic",
    author = "Abdul-Mageed, Muhammad  and
      Elmadany, AbdelRahim  and
      Nagoudi, El Moatez Billah",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.acl-long.551",
    doi = "10.18653/v1/2021.acl-long.551",
    pages = "7088--7105",
    abstract = "Pre-trained language models (LMs) are currently integral to many natural language processing systems. Although multilingual LMs were also introduced to serve many languages, these have limitations such as being costly at inference time and the size and diversity of non-English data involved in their pre-training. We remedy these issues for a collection of diverse Arabic varieties by introducing two powerful deep bidirectional transformer-based models, ARBERT and MARBERT. To evaluate our models, we also introduce ARLUE, a new benchmark for multi-dialectal Arabic language understanding evaluation. ARLUE is built using 42 datasets targeting six different task clusters, allowing us to offer a series of standardized experiments under rich conditions. When fine-tuned on ARLUE, our models collectively achieve new state-of-the-art results across the majority of tasks (37 out of 48 classification tasks, on the 42 datasets). Our best model acquires the highest ARLUE score (77.40) across all six task clusters, outperforming all other models including XLM-R Large ( 3.4x larger size). Our models are publicly available at https://github.com/UBC-NLP/marbert and ARLUE will be released through the same repository.",
}


@article{elmadany2022orca,
  title={ORCA: A Challenging Benchmark for Arabic Language Understanding},
  author={Elmadany, AbdelRahim and Nagoudi, El Moatez Billah and Abdul-Mageed, Muhammad},
  journal={arXiv preprint arXiv:2212.10758},
  year={2022}
}

```

## Acknowledgments
We gratefully acknowledge support from the Natural Sciences and Engineering Research Council  of Canada, the  Social  Sciences and  Humanities  Research  Council  of  Canada, Canadian  Foundation  for  Innovation,  [ComputeCanada](www.computecanada.ca) and [UBC ARC-Sockeye](https://doi.org/10.14288/SOCKEYE). We  also  thank  the  [Google TensorFlow Research Cloud (TFRC)](https://www.tensorflow.org/tfrc) program for providing us with free TPU access.
