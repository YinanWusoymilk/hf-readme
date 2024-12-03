---
language:
- en
license: openrail++
tags:
- stable-diffusion
- stable-diffusion-diffusers
- stable-diffusion-xl
- stable-diffusion-xl-turbo
- text-to-image
- art
- artistic
- diffusers
- anime
- dreamshaper
- turbo
- lcm
duplicated_from: lykon/dreamshaper-xl-v2-turbo
---

# Dreamshaper XL v2 Turbo

`lykon/dreamshaper-xl-v2-turbo` is a Stable Diffusion model that has been fine-tuned on [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0).

Please consider supporting me: 
- on [Patreon](https://www.patreon.com/Lykon275)
- or [buy me a coffee](https://snipfeed.co/lykon)

## Diffusers

For more general information on how to run text-to-image models with 🧨 Diffusers, see [the docs](https://huggingface.co/docs/diffusers/using-diffusers/conditional_image_generation).

1. Installation

```
pip install diffusers transformers accelerate
```

2. Run
```py
from diffusers import AutoPipelineForText2Image, DPMSolverMultistepScheduler
import torch

pipe = AutoPipelineForText2Image.from_pretrained('lykon/dreamshaper-xl-v2-turbo', torch_dtype=torch.float16, variant="fp16")
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

prompt = "portrait photo of muscular bearded guy in a worn mech suit, light bokeh, intricate, steel metal, elegant, sharp focus, soft lighting, vibrant colors"

generator = torch.manual_seed(0)
image = pipe(prompt, num_inference_steps=6, guidance_scale=2).images[0]  
image.save("./image.png")
```