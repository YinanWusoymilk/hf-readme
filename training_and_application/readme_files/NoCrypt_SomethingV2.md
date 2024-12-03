---
license: creativeml-openrail-m
thumbnail: >-
  https://huggingface.co/NoCrypt/SomethingV2/resolve/main/imgs/00031-1769428138-masterpiece%2C%20best%20quality%2C%20hatsune%20miku%2C%201girl%2C%20white%20shirt%2C%20blue%20necktie%2C%20bare%20shoulders%2C%20very%20detailed%20background%2C%20hands%20on%20ow.png
tags:
- stable-diffusion
- text-to-image
- safetensors
- diffusers
inference: true
language:
- en
widget:
  - text: >-
      masterpiece, best quality, 1girl, brown hair, green eyes, colorful,
      autumn, cumulonimbus clouds, lighting, blue sky, falling leaves, garden
    example_title: example 1girl
  - text: >-
      masterpiece, best quality, 1boy, medium hair, blonde hair, blue eyes,
      bishounen, colorful, autumn, cumulonimbus clouds, lighting, blue sky,
      falling leaves, garden
    example_title: example 1boy
library_name: diffusers
---

## Introducing SomethingV2.2, An updated version of this model, can be found [here](https://huggingface.co/NoCrypt/SomethingV2_2)

---

[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/NoCrypt/SomethingV2)
<center><img src="https://huggingface.co/NoCrypt/SomethingV2/resolve/main/imgs/banner.webp" width="95%"/></center>
<center><h1><b>SomethingV2</b></h1></center>
<p align="center">Welcome to SomethingV2 - an anime latent diffusion model. This model is intended to produce vibrant but soft anime style images. </p>


## Recommended Settings
- VAE: None (Baked in model)
- Clip Skip: 2
- Sampler: DPM++ 2M Karras
- CFG Scale: 7 - 12
- Negative Prompt: [EasyNegative](https://huggingface.co/datasets/gsdf/EasyNegative)
- For better results, using hires fix is a must. 
- Hires upscaler: Latent (any variant, such as nearest-exact)
- Resolution: At least 512x512 first pass, upscale up to 1500x1500


## Example
<img style="display:inline;margin:0;padding:0;" src="https://huggingface.co/NoCrypt/SomethingV2/resolve/main/imgs/00090-1829045217-masterpiece%20best%20quality%20hatsune%20miku%201girl%20white%20shirt%20blue%20necktie%20bare%20shoulders%20very%20detailed%20background%20hands%20on%20ow2473e4832c888be11494dab007c390c19c5b2f7d.png" width="32%"/>
<img style="display:inline;margin:0;padding:0;" src="https://huggingface.co/NoCrypt/SomethingV2/resolve/main/imgs/00022-1769428138-masterpiece%2C%20best%20quality%2C%20hatsune%20miku%2C%201girl%2C%20white%20shirt%2C%20blue%20necktie%2C%20bare%20shoulders%2C%20very%20detailed%20background%2C%20hands%20on%20ow.png" width="32%"/>
<img style="display:inline;margin:0;padding:0;" src="https://huggingface.co/NoCrypt/SomethingV2/resolve/main/imgs/00098-3514023396-masterpiece%2C%20best%20quality%2C%20hatsune%20miku%2C%201girl%2C%20white%20shirt%2C%20blue%20necktie%2C%20bare%20shoulders%2C%20very%20detailed%20background%2C%20cafe%2C%20angry.png" width="32%"/>

<details><summary><big><b>Prompts</b></big></summary>

```yaml
masterpiece, best quality, hatsune miku, 1girl, white shirt, blue necktie, bare shoulders, very detailed background, hands on own cheeks, open mouth, one eye closed, clenched teeth, smile
Negative prompt: EasyNegative, tattoo, (shoulder tattoo:1.0), (number tattoo:1.3), frills
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1829045217, Size: 456x592, Model: somethingv2_1, Denoising strength: 0.53, Clip skip: 2, ENSD: 31337, Hires upscale: 1.65, Hires steps: 12, Hires upscaler: Latent (nearest-exact), Discard penultimate sigma: True
```

```yaml
masterpiece, best quality, hatsune miku, 1girl, white shirt, blue necktie, bare shoulders, very detailed background, hands on own cheeks, open mouth, eyez closed, clenched teeth, smile, arms behind back,
Negative prompt: EasyNegative, tattoo, (shoulder tattoo:1.0), (number tattoo:1.3), frills
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1769428138, Size: 456x592, Model: somethingv2_1, Denoising strength: 0.53, Clip skip: 2, ENSD: 31337, Hires upscale: 1.65, Hires steps: 12, Hires upscaler: Latent (nearest-exact), Discard penultimate sigma: True
```

```yaml
masterpiece, best quality, hatsune miku, 1girl, white shirt, blue necktie, bare shoulders, very detailed background, cafe, angry, crossed arms, detached sleeves, light particles,
Negative prompt: EasyNegative, tattoo, (shoulder tattoo:1.0), (number tattoo:1.3), frills
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3514023396, Size: 456x592, Model: somethingv2_1, Denoising strength: 0.53, Clip skip: 2, ENSD: 31337, Hires upscale: 1.65, Hires steps: 12, Hires upscaler: Latent (nearest-exact), Discard penultimate sigma: True

```

</details>


## FAQ
### Model differences?
![](https://huggingface.co/NoCrypt/SomethingV2/resolve/main/imgs/xyz_grid-0003-4163886333-masterpiece%2C%20hatsune%20miku%2C%20white%20shirt%2C%20blue%20necktie%2C%20bare%20shoulders%2C%20detached%20sleeves%2C.png)
<details><summary><big><b>Prompts</b></big></summary>

```yaml
masterpiece, hatsune miku, white shirt, blue necktie, bare shoulders, detached sleeves,
Negative prompt: EasyNegative
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 4163886333, Size: 440x592, Model: -, Denoising strength: 0.53, Clip skip: 2, ENSD: 31337, Hires upscale: 1.65, Hires steps: 13, Hires upscaler: Latent (nearest-exact)
```

</details>

### Why all examples is miku?
Because I love miku. But here's other subjects

<img style="display:inline;margin:0;padding:0;" src="https://huggingface.co/NoCrypt/SomethingV2/resolve/main/imgs/00018-4018636341-masterpiece%2C%20best%20quality%2C%201girl%2C%20aqua%20eyes%2C%20baseball%20cap%2C%20blonde%20hair%2C%20closed%20mouth%2C%20earrings%2C%20green%20background%2C%20hat%2C%20hoop%20earr.png" width="49%"/>
<img style="display:inline;margin:0;padding:0;" src="https://huggingface.co/NoCrypt/SomethingV2/resolve/main/imgs/00019-1334620477-masterpiece%2C%20best%20quality%2C%20landscape.png" width="49%"/>
<details><summary><big><b>Prompts</b></big></summary>

```yaml
masterpiece, best quality, 1girl, aqua eyes, baseball cap, blonde hair, closed mouth, earrings, green background, hat, hoop earrings, jewelry, looking at viewer, shirt, short hair, simple background, solo, upper body, yellow shirt
Negative prompt: EasyNegative
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 4018636341, Size: 440x592, Model: somethingv2, Denoising strength: 0.53, Clip skip: 2, ENSD: 31337, Hires upscale: 1.65, Hires steps: 13, Hires upscaler: Latent (nearest-exact)
```

```yaml
masterpiece, best quality, landscape
Negative prompt: EasyNegative
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1334620477, Size: 440x592, Model: somethingv2, Denoising strength: 0.53, Clip skip: 2, ENSD: 31337, Hires upscale: 1.65, Hires steps: 13, Hires upscaler: Latent (nearest-exact)
```

</details>