---
license: apache-2.0
datasets:
- yuvalkirstain/pickapic_v1
language:
- en
pipeline_tag: text-to-image
---
# Step-aware Preference Optimization: Aligning Preference with Denoising Performance at Each Step

<a href="https://arxiv.org/abs/2406.04314"><img src="https://img.shields.io/badge/Paper-arXiv-red?style=for-the-badge" height=22.5></a>
<a href="https://github.com/RockeyCoss/SPO"><img src="https://img.shields.io/badge/Gihub-Code-succees?style=for-the-badge&logo=GitHub" height=22.5></a>
<a href="https://rockeycoss.github.io/spo.github.io/"><img src="https://img.shields.io/badge/Project-Page-blue?style=for-the-badge" height=22.5></a>

<table>
  <tr>
    <td><img src="assets/imgs/0.png" alt="teaser example 0" width="200"/></td>
    <td><img src="assets/imgs/1.png" alt="teaser example 1" width="200"/></td>
    <td><img src="assets/imgs/2.png" alt="teaser example 2" width="200"/></td>
    <td><img src="assets/imgs/3.png" alt="teaser example 3" width="200"/></td>
  </tr>
</table>

## Abstract
<p>
Recently, Direct Preference Optimization (DPO) has extended its success from aligning large language models (LLMs) to aligning text-to-image diffusion models with human preferences.
Unlike most existing DPO methods that assume all diffusion steps share a consistent preference order with the final generated images, we argue that this assumption neglects step-specific denoising performance and that preference labels should be tailored to each step's contribution.
</p>
<p> 
To address this limitation, we propose Step-aware Preference Optimization (SPO), a novel post-training approach that independently evaluates and adjusts the denoising performance at each step, using a <em>step-aware preference model</em> and a <em>step-wise resampler</em> to ensure accurate step-aware supervision.
Specifically, at each denoising step, we sample a pool of images, find a suitable win-lose pair, and, most importantly, randomly select a single image from the pool to initialize the next denoising step. This step-wise resampler process ensures the next win-lose image pair comes from the same image, making the win-lose comparison independent of the previous step. To assess the preferences at each step, we train a separate step-aware preference model that can be applied to both noisy and clean images.
</p> 
<p>
Our experiments with Stable Diffusion v1.5 and SDXL demonstrate that SPO significantly outperforms the latest Diffusion-DPO in aligning generated images with complex, detailed prompts and enhancing aesthetics, while also achieving more than 20&times; times faster in training efficiency. Code and model: <a ref="https://rockeycoss.github.io/spo.github.io/">https://rockeycoss.github.io/spo.github.io/</a>
</p>

## Model Description

This model is fine-tuned from [stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0). It has been trained on 4,000 prompts for 10 epochs.

This is a merged checkpoint that combines the LoRA checkpoint with the base model [stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0). If you want to access the LoRA checkpoint, please visit [SPO-SDXL_4k-p_10ep_LoRA](https://huggingface.co/SPO-Diffusion-Models/SPO-SDXL_4k-p_10ep_LoRA). We also provide a LoRA checkpoint compatible with [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), which can be accessed [here](https://civitai.com/models/510261?modelVersionId=567119).


## A quick example
```python
from diffusers import StableDiffusionXLPipeline, UNet2DConditionModel
import torch

# load pipeline
inference_dtype = torch.float16
pipe = StableDiffusionXLPipeline.from_pretrained(
    "SPO-Diffusion-Models/SPO-SDXL_4k-p_10ep", 
    torch_dtype=inference_dtype,
)
vae = AutoencoderKL.from_pretrained(
    'madebyollin/sdxl-vae-fp16-fix',
    torch_dtype=inference_dtype,
)
pipe.vae = vae
pipe.to('cuda')

generator=torch.Generator(device='cuda').manual_seed(42)
image = pipe(
    prompt='a child and a penguin sitting in front of the moon',
    guidance_scale=5.0,
    generator=generator,
    output_type='pil',
).images[0]
image.save('moon.png')
```

## Citation
If you find our work or codebase useful, please consider giving us a star and citing our work.
```
@article{liang2024step,
  title={Step-aware Preference Optimization: Aligning Preference with Denoising Performance at Each Step},
  author={Liang, Zhanhao and Yuan, Yuhui and Gu, Shuyang and Chen, Bohan and Hang, Tiankai and Li, Ji and Zheng, Liang},
  journal={arXiv preprint arXiv:2406.04314},
  year={2024}
}
```