---
license: cc-by-nc-sa-4.0
language: "en"
tags:
- splade
- query-expansion
- document-expansion
- bag-of-words
- passage-retrieval
- knowledge-distillation
- document encoder
datasets:
- ms_marco
---
## Efficient SPLADE 
Efficient SPLADE model for passage retrieval. This architecture uses two distinct models for query and document inference. This is the **query** one, please also download the **doc** one (https://huggingface.co/naver/efficient-splade-VI-BT-large-doc). For additional details, please visit:
* paper: https://dl.acm.org/doi/10.1145/3477495.3531833
* code: https://github.com/naver/splade
| | MRR@10 (MS MARCO dev) | R@1000 (MS MARCO dev) | Latency (PISA) ms | Latency (Inference) ms
| --- | --- | --- | --- | --- |
| `naver/efficient-splade-V-large` | 38.8 | 98.0 | 29.0 | 45.3
| `naver/efficient-splade-VI-BT-large` | 38.0 | 97.8 | 31.1 | 0.7
## Citation
If you use our checkpoint, please cite our work:
```
@inproceedings{10.1145/3477495.3531833,
author = {Lassance, Carlos and Clinchant, St\'{e}phane},
title = {An Efficiency Study for SPLADE Models},
year = {2022},
isbn = {9781450387323},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3477495.3531833},
doi = {10.1145/3477495.3531833},
abstract = {Latency and efficiency issues are often overlooked when evaluating IR models based on Pretrained Language Models (PLMs) in reason of multiple hardware and software testing scenarios. Nevertheless, efficiency is an important part of such systems and should not be overlooked. In this paper, we focus on improving the efficiency of the SPLADE model since it has achieved state-of-the-art zero-shot performance and competitive results on TREC collections. SPLADE efficiency can be controlled via a regularization factor, but solely controlling this regularization has been shown to not be efficient enough. In order to reduce the latency gap between SPLADE and traditional retrieval systems, we propose several techniques including L1 regularization for queries, a separation of document/query encoders, a FLOPS-regularized middle-training, and the use of faster query encoders. Our benchmark demonstrates that we can drastically improve the efficiency of these models while increasing the performance metrics on in-domain data. To our knowledge, we propose the first neural models that, under the same computing constraints, achieve similar latency (less than 4ms difference) as traditional BM25, while having similar performance (less than 10% MRR@10 reduction) as the state-of-the-art single-stage neural rankers on in-domain data.},
booktitle = {Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval},
pages = {2220–2226},
numpages = {7},
keywords = {splade, latency, information retrieval, sparse representations},
location = {Madrid, Spain},
series = {SIGIR '22}
}
```

