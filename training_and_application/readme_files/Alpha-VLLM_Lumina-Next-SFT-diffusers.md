---
license: apache-2.0
tags:
- text-to-image
- safetensors
- diffusers
datasets:
- JourneyDB/JourneyDB
library_name: diffusers
pipeline_tag: text-to-image
---

# Lumina-Next-SFT

The `Lumina-Next-SFT` is a Next-DiT model containing 2B parameters and utilizes [Gemma-2B](https://huggingface.co/google/gemma-2b) as the text encoder, enhanced through high-quality supervised fine-tuning (SFT).

Our generative model has `Next-DiT` as the backbone, the text encoder is the `Gemma` 2B model, and the VAE uses a version of `sdxl` fine-tuned by stabilityai.

- Generation Model: Next-DiT
- Text Encoder: [Gemma-2B](https://huggingface.co/google/gemma-2b)
- VAE: [stabilityai/sdxl-vae](https://huggingface.co/stabilityai/sdxl-vae)

[![Lumina-Next](https://img.shields.io/badge/Paper-Lumina--Next-2b9348.svg?logo=arXiv)](https://github.com/Alpha-VLLM/Lumina-T2X/blob/main/assets/lumina-next.pdf)
[Lumina-T2X paper](https://arxiv.org/abs/2405.05945)

![hero](https://github.com/Alpha-VLLM/Lumina-T2X/assets/54879512/9f52eabb-07dc-4881-8257-6d8a5f2a0a5a)

## 📰 News

- **[2024-07-08] 🎉🎉🎉 Lumina-Next is now supported in the [diffusers](https://github.com/huggingface/diffusers)! Thanks to [@yiyixuxu](https://github.com/yiyixuxu) and [@sayakpaul](https://github.com/sayakpaul)!**

- [2024-06-08] 🎉🎉🎉 We have released the `Lumina-Next-SFT` model.

- [2024-05-28] We updated the `Lumina-Next-T2I` model to support 2K Resolution image generation.

- [2024-05-16] We have converted the `.pth` weights to `.safetensors` weights. Please pull the latest code to use `demo.py` for inference.

- [2024-05-12] We release the next version of `Lumina-T2I`, called `Lumina-Next-T2I` for faster and lower memory usage image generation model.

## 🎮 Model Zoo

More checkpoints of our model will be released soon~

| Resolution | Next-DiT Parameter| Text Encoder | Prediction | Download URL  |
| ---------- | ----------------------- | ------------ | -----------|-------------- |
| 1024  | 2B  | [Gemma-2B](https://huggingface.co/google/gemma-2b)  | Rectified Flow | [hugging face](https://huggingface.co/Alpha-VLLM/Lumina-Next-SFT-diffusers) |

## Installation

### 1. Create a conda environment and install PyTorch

Note: You may want to adjust the CUDA version [according to your driver version](https://docs.nvidia.com/deploy/cuda-compatibility/#default-to-minor-version).

```bash
conda create -n Lumina_T2X -y
conda activate Lumina_T2X
conda install python=3.11 pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 pytorch-cuda=12.1 -c pytorch -c nvidia -y
```

### 2. Install dependencies

```bash
pip install diffusers huggingface_hub
```

### 3. Install ``flash-attn``

```bash
pip install flash-attn --no-build-isolation
```

## Inference


1. Prepare the pre-trained model

⭐⭐ (Recommended) you can use huggingface_cli to download our model:

```bash
huggingface-cli download --resume-download Alpha-VLLM/Lumina-Next-SFT-diffusers --local-dir /path/to/ckpt
```

2. Run with demo code:

```python
from diffusers import LuminaText2ImgPipeline
import torch

pipeline = LuminaText2ImgPipeline.from_pretrained("/path/to/ckpt/Lumina-Next-SFT-diffusers", torch_dtype=torch.bfloat16).to("cuda")

# or you can download the model using code directly
# pipeline = LuminaText2ImgPipeline.from_pretrained("Alpha-VLLM/Lumina-Next-SFT-diffusers", torch_dtype=torch.bfloat16).to("cuda")

image = pipeline(prompt="Upper body of a young woman in a Victorian-era outfit with brass goggles and leather straps. "
                        "Background shows an industrial revolution cityscape with smoky skies and tall, metal structures").images[0]
```
