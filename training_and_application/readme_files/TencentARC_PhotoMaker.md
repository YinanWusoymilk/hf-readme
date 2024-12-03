---
license: apache-2.0
language:
- en
library_name: diffusers
pipeline_tag: text-to-image
---

# PhotoMaker Model Card

<div align="center">

[**Project Page**](https://photo-maker.github.io/) **|** [**Paper (ArXiv)**](https://arxiv.org/abs/2312.04461) **|** [**Code**](https://github.com/TencentARC/PhotoMaker)

[🤗 **Gradio demo (Realistic)**](https://huggingface.co/spaces/TencentARC/PhotoMaker) **|** [🤗 **Gradio demo (Stylization)**](https://huggingface.co/spaces/TencentARC/PhotoMaker-Style)

</div>

## Introduction

<!-- Provide a quick summary of what the model is/does. -->
Users can input one or a few face photos, along with a text prompt, to receive a customized photo or painting within seconds (no training required!). Additionally, this model can be adapted to any base model based on SDXL or used in conjunction with other LoRA modules.

### Realistic results

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/6285a9133ab6642179158944/BYBZNyfmN4jBKBxxt4uxz.jpeg)

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/6285a9133ab6642179158944/9KYqoDxfbNVLzVKZzSzwo.jpeg)

### Stylization results

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/6285a9133ab6642179158944/du884lcjpqqjnJIxpATM2.jpeg)


![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/6285a9133ab6642179158944/-AC7Hr5YL4yW1zXGe_Izl.jpeg)

More results can be found in our [project page](https://photo-maker.github.io/)

## Model Details

It mainly contains two parts corresponding to two keys in loaded state dict:

1. `id_encoder` includes finetuned OpenCLIP-ViT-H-14 and a few fuse layers.

2. `lora_weights` applies to all attention layers in the UNet, and the rank is set to 64.


## Usage

You can directly download the model in this repository.
You also can download the model in python script:

```python
from huggingface_hub import hf_hub_download
photomaker_ckpt = hf_hub_download(repo_id="TencentARC/PhotoMaker", filename="photomaker-v1.bin", repo_type="model")
```

Then, please follow the instructions in our [GitHub repository](https://github.com/TencentARC/PhotoMaker). 


## Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

- The model's customization performance degrades on Asian male faces.
- The model still struggles with accurately rendering human hands.

## Bias

While the capabilities of image generation models are impressive, they can also reinforce or exacerbate social biases.

## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```bibtex
@inproceedings{li2023photomaker,
  title={PhotoMaker: Customizing Realistic Human Photos via Stacked ID Embedding},
  author={Li, Zhen and Cao, Mingdeng and Wang, Xintao and Qi, Zhongang and Cheng, Ming-Ming and Shan, Ying},
  booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2024}
}
```