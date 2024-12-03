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
- text: a young woman
  output:
    url: images/0.png
base_model: black-forest-labs/FLUX.1-dev
instance_prompt: null
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
---
# FLUX.1-dev-LoRA-add-details

This is a LoRA trained on FLUX.1-dev for enhancing realism and details, achieveing natural skin. Made by [Dote](https://www.shakker.ai/userpage/7728c1d6b47649548612edffcb470ccb/publish).

<div class="container">
  <img src="./images/poster.jpeg" width="1024"/>
</div>

## Showcases

<div class="container">
  <img src="./images/20240830-195549.png" width="1024"/>
  <img src="./images/20240830-195552.png" width="1024"/>
  <img src="./images/20240830-195556.png" width="1024"/>
</div>


## Trigger words

There is no essential trigger words. The recommended scale is `1.0`. The scale be can be negative.

## Inference

```python
import torch
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)
pipe.load_lora_weights("Shakker-Labs/FLUX.1-dev-LoRA-blended-realistic-illustration", weight_name="FLUX.1-dev-LoRA-add-details.safetensors")
pipe.fuse_lora(lora_scale=1.0)
pipe.to("cuda")

prompt = "A beautiful woman, flim rendering"

image = pipe(prompt, 
             num_inference_steps=24, 
             guidance_scale=3.5,
             width=768, height=1024,
            ).images[0]
image.save(f"example.png")
```

## Online Inference

You can also download this model at [Shakker AI](https://www.shakker.ai/modelinfo/f040e8f8526945249ff4f150fc727eb3?from=personal_page), where we provide an online interface to generate images.


## Acknowledgements
This model is trained by our copyrighted users [Dote](https://www.shakker.ai/userpage/7728c1d6b47649548612edffcb470ccb/publish). We release this model under permissions.