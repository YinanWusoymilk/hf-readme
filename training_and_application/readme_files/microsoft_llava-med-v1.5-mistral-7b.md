---
license: apache-2.0
tags:
- image-text-to-text
- medical
- vision
---


# LLaVA-Med v1.5, using [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) as LLM for a better commercial license

Large Language and Vision Assistant for bioMedicine (i.e., “LLaVA-Med”) is a large language and vision model trained using a curriculum learning method for adapting LLaVA to the biomedical domain. It is an open-source release intended for research use only to facilitate reproducibility of the corresponding paper which claims improved performance for open-ended biomedical questions answering tasks, including common visual question answering (VQA) benchmark datasets such as PathVQA and VQA-RAD.

LLaVA-Med was proposed in [LLaVA-Med: Training a Large Language-and-Vision Assistant for Biomedicine in One Day](https://arxiv.org/abs/2306.00890) by Chunyuan Li, Cliff Wong, Sheng Zhang, Naoto Usuyama, Haotian Liu, Jianwei Yang, Tristan Naumann, Hoifung Poon, Jianfeng Gao.


**Model date:**
LLaVA-Med-v1.5-Mistral-7B was trained in April 2024.

**Paper or resources for more information:**
https://aka.ms/llava-med

**Where to send questions or comments about the model:**
https://github.com/microsoft/LLaVA-Med/issues


## License
[mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) license.

## Intended use

The data, code, and model checkpoints are intended to be used solely for (I) future research on visual-language processing and (II) reproducibility of the experimental results reported in the reference paper. The data, code, and model checkpoints are not intended to be used in clinical care or for any clinical decision making purposes.

### Primary Intended Use

The primary intended use is to support AI researchers reproducing and building on top of this work. LLaVA-Med and its associated models should be helpful for exploring various biomedical vision-language processing (VLP ) and vision question answering (VQA) research questions.

### Out-of-Scope Use

Any deployed use case of the model --- commercial or otherwise --- is out of scope. Although we evaluated the models using a broad set of publicly-available research benchmarks, the models and evaluations are intended for research use only and not intended for deployed use cases. Please refer to [the associated paper](https://aka.ms/llava-med) for more details.


## Data

This model builds upon [PMC-15M dataset](https://aka.ms/biomedclip-paper), which is a large-scale parallel image-text dataset for biomedical vision-language processing. It contains 15 million figure-caption pairs extracted from biomedical research articles in PubMed Central. It covers a diverse range of biomedical image types, such as microscopy, radiography, histology, and more.



## How to use

See the [Serving](https://github.com/microsoft/LLaVA-Med?tab=readme-ov-file#serving) and [Evaluation](https://github.com/microsoft/LLaVA-Med?tab=readme-ov-file#evaluation) sections in the [LLaVA-Med repo](https://aka.ms/llava-med).

## Limitations

This model was developed using English corpora, and thus may be considered English-only. This model is evaluated on a narrow set of biomedical benchmark tasks, described in [LLaVA-Med paper](https://aka.ms/llava-med). As such, it is not suitable for use in any clinical setting. Under some conditions, the model may make inaccurate predictions and display limitations, which may require additional mitigation strategies. In particular, this model is likely to carry many of the limitations of the model from which it is derived, [LLaVA](https://llava-vl.github.io/).

Further, this model was developed in part using the [PMC-15M](https://aka.ms/biomedclip-paper) dataset. The figure-caption pairs that make up this dataset may contain biases reflecting the current practice of academic publication. For example, the corresponding papers may be enriched for positive findings, contain examples of extreme cases, and otherwise reflect distributions that are not representative of other sources of biomedical data.


### BibTeX entry and citation info

```bibtex
@article{li2023llavamed,
  title={Llava-med: Training a large language-and-vision assistant for biomedicine in one day},
  author={Li, Chunyuan and Wong, Cliff and Zhang, Sheng and Usuyama, Naoto and Liu, Haotian and Yang, Jianwei and Naumann, Tristan and Poon, Hoifung and Gao, Jianfeng},
  journal={arXiv preprint arXiv:2306.00890},
  year={2023}
}
```