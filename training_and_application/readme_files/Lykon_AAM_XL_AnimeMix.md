---
language:
- en
license: other
tags:
- stable-diffusion
- stable-diffusion-diffusers
- stable-diffusion-xl
- text-to-image
- art
- artistic
- diffusers
- anime
---

# AAM XL AnimeMix

`Lykon/AAM_XL_AnimeMix` is a Stable Diffusion model that has been fine-tuned on [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0).

Please consider supporting me: 
- on [Patreon](https://www.patreon.com/Lykon275)
- or [buy me a coffee](https://snipfeed.co/lykon)

**License**: [Fair AI Public License 1.0-SD](https://freedevproject.org/faipl-1.0-sd/)

## Diffusers

For more general information on how to run text-to-image models with 🧨 Diffusers, see [the docs](https://huggingface.co/docs/diffusers/using-diffusers/conditional_image_generation).

1. Installation

```
pip install diffusers transformers accelerate
```

2. Run
```py
from diffusers import AutoPipelineForText2Image, DEISMultistepScheduler
import torch

pipe = AutoPipelineForText2Image.from_pretrained('Lykon/AAM_XL_AnimeMix', torch_dtype=torch.float16, variant="fp16")
pipe.scheduler = DEISMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

prompt = "anime girl, night, blue light behind her, ((Galaxy, Lens flare)), short hair, flower field, night sky, cinematic shot. Wallpaper. (Blue color schema), detailed background, a city in the distance"

generator = torch.manual_seed(0)
image = pipe(prompt, num_inference_steps=25).images[0]  
image.save("./image.png")
```

![](./image.png)
