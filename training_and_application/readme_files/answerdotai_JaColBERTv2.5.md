---
inference: false
datasets:
- miracl/miracl
- answerdotai/MMARCO-japanese-32-scored-triplets
- hotchpotch/JQaRA
- matsuxr/JaGovFaqs-22k
- unicamp-dl/mmarco
language:
- ja
pipeline_tag: sentence-similarity
tags:
- ColBERT
base_model:
- cl-tohoku/bert-base-japanese-v3
- bclavie/JaColBERT
license: mit
library_name: RAGatouille
---

Model weights for the final JaColBERTv2.5 checkpoint, using an entirely overhauled training recipe and trained on just 40% of the data of JaColBERTv2.

This model largely outperforms all previous approaches, including JaColBERTV2 multilingual models such as BGE-M3, on all datasets.

This page will be updated with the full details and the model report in the next few days.


```
@misc{clavié2024jacolbertv25optimisingmultivectorretrievers,
      title={JaColBERTv2.5: Optimising Multi-Vector Retrievers to Create State-of-the-Art Japanese Retrievers with Constrained Resources}, 
      author={Benjamin Clavié},
      year={2024},
      eprint={2407.20750},
      archivePrefix={arXiv},
      primaryClass={cs.IR},
      url={https://arxiv.org/abs/2407.20750}, 
}
```