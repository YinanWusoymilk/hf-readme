---
license: apache-2.0
language:
- en
pipeline_tag: text-generation
tags:
  - nvidia
  - Megatron-LM
  - Mamba
  - Mamba-2
  - SSM
  - 8B
library_name: Megatron-LM
---

# An Empirical Study of Mamba-based Language Models

[Documentation](https://github.com/NVIDIA/Megatron-LM/tree/ssm/examples/mamba) &ensp; [Paper](https://arxiv.org/abs/2406.07887) &ensp; [Models](https://huggingface.co/collections/nvidia/ssms-666a362c5c3bb7e4a6bcfb9c)

## Overview
We release the 8B-parameter [Mamba-2](https://arxiv.org/abs/2405.21060) and Mamba-2-Hybrid model (made of Mamba-2, attention, and MLP layers) trained for the paper [An Empirical Study of Mamba-based Language Models.](https://arxiv.org/abs/2406.07887). These models were trained for 3.5T tokens with a sequence length of 4K. These models can be compared to the released 8B-parameter Transformer trained on the same data with the same hyperparameters. We also release the 32K and 128K long-context extensions of Mamba-2-Hybrid. 

### Model Version(s)

`mamba2-hybrid-8b-3t-4k`: 8B-parameter base Mamba-2-Hybrid model trained on 3.5T tokens with 4K sequence length.

### Toolkit
[Megatron-LM Framework](https://github.com/NVIDIA/Megatron-LM/tree/ssm/examples/mamba)

# Citations

See more details in our paper:

[An Empirical Study of Mamba-based Language Models.](https://arxiv.org/abs/2406.07887) 

_Roger Waleffe, Wonmin Byeon, Duncan Riach, Brandon Norick, Vijay Korthikanti, Tri Dao, Albert Gu, Ali Hatamizadeh, Sudhakar Singh, Deepak Narayanan, Garvit Kulshreshtha, Vartika Singh, Jared Casper, Jan Kautz, Mohammad Shoeybi, Bryan Catanzaro._ (2024)

Please cite the paper as follows if you use the models from this repo:

```bibtex
@article{waleffe2024anempirical,
    title   = {An Empirical Study of Mamba-based Language Models},
    author  = {Roger Waleffe and Wonmin Byeon and Duncan Riach and Brandon Norick and Vijay Korthikanti and Tri Dao and Albert Gu and Ali Hatamizadeh and Sudhakar Singh and Deepak Narayanan and Garvit Kulshreshtha and Vartika Singh and Jared Casper and Jan Kautz and Mohammad Shoeybi and Bryan Catanzaro},
    year    = {2024},
    journal = {arXiv preprint arXiv: 2406.07887}
}
```
