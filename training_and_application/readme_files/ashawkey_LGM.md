---
license: mit
pipeline_tag: text-to-3d
tags:
- image-to-3d
- text-to-3d
---

# LGM

This model contains the pretrained weights for *LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation*.

### [Project Page](https://me.kiui.moe/lgm/) | [Arxiv](https://arxiv.org/abs/2402.05054) | [Weights](https://huggingface.co/ashawkey/LGM)


## Introduction
LGM can generate 3D objects from image or text within 5 seconds at high-resolution based on Gaussian Splatting.

<video controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/63367f9a9895307563659be6/9CVJZ5ZXkhheDPKl3M0pM.mp4"></video>

<video controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/63367f9a9895307563659be6/6DM_hNEDLRJOz95pgVjek.mp4"></video>


## Model Details
The model is trained on a ~80K subset of [Objaverse](https://huggingface.co/datasets/allenai/objaverse).
For more details, please refer to our paper.

## Usage

To download the model:
```python
from huggingface_hub import hf_hub_download
ckpt_path = hf_hub_download(repo_id="ashawkey/LGM", filename="model_fp16_fixrot.safetensors")
```
Please refer to our [repo](https://github.com/3DTopia/LGM) for more details on loading and inference.

## Citation

```
@article{tang2024lgm,
  title={LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation},
  author={Tang, Jiaxiang and Chen, Zhaoxi and Chen, Xiaokang and Wang, Tengfei and Zeng, Gang and Liu, Ziwei},
  journal={arXiv preprint arXiv:2402.05054},
  year={2024}
}
```
