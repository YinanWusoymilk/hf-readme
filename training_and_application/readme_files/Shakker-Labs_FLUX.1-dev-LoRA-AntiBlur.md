---
tags:
- text-to-image
- stable-diffusion
- lora
- diffusers
- image-generation
- flux
- safetensors
widget:
- text: >-
    a young college student, walking on the street, campus background,
    photography
  output:
    url: images/2f82e6b1e5969d70a9044c19975bcdcca06b0f251d14f9c2c6095fa6.jpg
- text: a young woman, New York City
  output:
    url: images/340c1ae6709f56f3d8176848653dcade93d2b5b8ade662da167ef818.jpg
- text: >-
    happy stunning girl with long dark hair, wearing blue clothes, playing
    guitar, a beautiful field of flowers, colorful flowers everywhere, hills in
    the background
  output:
    url: images/ec9a40eed46e8d17d3db1560a6543c6e6be9ebe1e41ecd5d137c01e0.jpg
base_model: black-forest-labs/FLUX.1-dev
instance_prompt: null
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
---
# FLUX.1-dev-LoRA-AntiBlur

This is a functional LoRA trained on FLUX.1-dev for deep DoF (Anti-Blur🔥) by [Vadim_Fedenko](https://www.shakker.ai/userpage/1f90018d803d4045b8dec4d627915098/publish) on [Shakker AI](https://www.shakker.ai/modelinfo/5c3fa3f1d5034e63be325196eae0b4f6?from=search). 
It may not be fancy, but it works.

<div class="container">
  <img src="./poster.jpg" width="1024"/>
</div>

<!-- ## Showcases
<Gallery /> -->

## Comparison

The following example shows a simple comparison with FLUX.1-dev under the same parameter setting.

<div class="container">
  <img src="./compare1.png" width="1024"/>
</div>

It is worth noting that this LoRA has very little damage to image quality while enhancing the depth of field, and can be used together with other components, such as ControlNet. We regard it as a basic functional LoRA.

<div class="container">
  <img src="./compare2.png" width="1024"/>
</div>

## Trigger words
The trigger word is not required. The recommended scale is `1.0` to `1.5` in diffusers.

## Inference

```python
import torch
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)
pipe.load_lora_weights("Shakker-Labs/FLUX.1-dev-LoRA-AntiBlur", weight_name="FLUX-dev-lora-AntiBlur.safetensors")
pipe.fuse_lora(lora_scale=1.5)
pipe.to("cuda")

prompt = "a young college student, walking on the street, campus background, photography"

image = pipe(prompt, 
             num_inference_steps=24, 
             guidance_scale=3.5,
             width=768, height=1024,
            ).images[0]
image.save(f"example.png")
```

## Online Inference

You can also run this model at [Shakker AI](https://www.shakker.ai/modelinfo/5c3fa3f1d5034e63be325196eae0b4f6?from=search), where we provide an online interface to generate images.


## Acknowledgements
This model is trained by our copyrighted users [Vadim_Fedenko](https://www.shakker.ai/userpage/1f90018d803d4045b8dec4d627915098/publish). We release this model under permissions. The model follows [flux-1-dev-non-commercial-license](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md).
