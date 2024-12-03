---
license: creativeml-openrail-m
language:
- en
tags:
- stable-diffusion
- text-to-image
---
# AnyPastel (Anything v4.5 + Pastel Mix)
Satisfaction.

## Recipe
| Interpolation Method | Primary Model | Secondary Model | Tertiary Model | Output |
| ---- | ---- | ---- | ---- | ---- |
| Weighted sum @ 0.5 | [Anything v4.5](https://huggingface.co/andite/anything-v4.0) | [Pastel Mix](https://huggingface.co/andite/pastel-mix) | \- | AnyPastel |  
| Add difference @ 0.3 | AnyPastel | animefull-final-pruned | animesfw-final-pruned | AnyPastel nsfw |
| Add difference @ 0.25 | AnyPastel nsfw | gape60 | animefull-final-pruned | AnyPastel hard |

## VAE
[**animevae**](https://huggingface.co/andite/anything-v4.0/blob/main/anything-v4.0.vae.pt) is recommended.

## Examples
<img src="https://huggingface.co/m4gnett/any-pastel/resolve/main/images/2023-01-31_16.20.31_259005813.png" width="512px">

```
solo, 1girl, portrait, looking at viewer, masterpiece, best quality, 4k, 8k,
Negative prompt: (worst quality, low quality:1.4), (bad-image-v2-39000:0.75), (bad_prompt_v2:0.85), (censored, bar censor), cropped, mature,
Steps: 28, Sampler: DPM++ 2M Karras, CFG scale: 6, Seed: 259005813, Size: 512x768, Model hash: e8c63e365d, Denoising strength: 0.55, Clip skip: 2, ENSD: 31337, Hires upscale: 1.5, Hires upscaler: Latent (bicubic antialiased)
```