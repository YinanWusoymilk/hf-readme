---
tags:
- text-to-image
- stable-diffusion
- diffusers
- image-generation
- flux
- safetensors
widget:
- text: A young asian girl, filmfotos,film grain, reversal film photography
  output:
    url: images/1.png
- text: >-
    A young Japanese girl, profile, blue hours, Tokyo tower, filmfotos,film
    grain, reversal film photography
  output:
    url: images/2.png
- text: Tokyo street photography, filmfotos,film grain, reversal film photography
  output:
    url: images/3.png
base_model: black-forest-labs/FLUX.1-dev
instance_prompt: filmfotos, film grain, reversal film photography
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
language:
- en
library_name: diffusers
---
# FilmPortrait

<div class="container">
  <img src="./poster.jpeg" width="1024"/>
</div>

FilmPortrait is a LoRA model finetuned on FLUX.1-dev, specifically designed to enhance the film texture. It embodies a subdued, low-saturation color palette reminiscent of classic Japanese cinema, which is particularly evident in its portrayal of characters (with a subtle bias towards Asian features), serene still lifes, and sweeping landscapes. The model delivers an exceptional aesthetic experience, capturing the essence of a bygone era with modern precision.

<div class="container">
  <img src="./cover.jpeg" width="1024"/>
</div>


## Comparison

The following example shows a simple comparison with FLUX.1-dev under the same parameter setting.

<div class="container">
  <img src="./comparison.png" width="1024"/>
</div>


## Trigger words

You should use `filmfotos, film grain, reversal film photography` to trigger the image generation.


## Inference

```python
import torch
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)
pipe.load_lora_weights('Shakker-Labs/FilmPortrait', weight_name='filmfotos.safetensors')
pipe.fuse_lora(lora_scale=0.9)
pipe.to("cuda")

prompt = "a young girl, filmfotos, film grain, reversal film photography"

image = pipe(prompt, 
             num_inference_steps=24, 
             guidance_scale=3.5,
             width=768, height=1024,
            ).images[0]
image.save(f"example.png")
```

## Online Inference

You can also download this model at [Shakker AI](https://www.shakker.ai/modelinfo/ec983ff3497d46ea977dbfcd1d989f67?from=search), where we provide an online interface to generate images.


## Acknowledgements
This model is trained by our copyrighted users [DynamicWang](https://www.shakker.ai/userpage/dfca7abc67c04a9492ea738d864de070/publish). We release this model under permissions. The model follows [flux-1-dev-non-commercial-license](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md).