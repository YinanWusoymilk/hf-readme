---
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
tags:
- Text-to-Image
- ControlNet
- Diffusers
- Stable Diffusion
base_model: black-forest-labs/FLUX.1-dev
---

# FLUX.1-dev Controlnet

We have completed the training of the first version. 
The training was conducted with a total pixel count of `1024*1024` at multi-scale. 
We trained for 30k steps using a batch size of 8*8.



<img src="./images/image_demo.jpg" width = "800" />
<img src="./images/image_demo_weight.png" width = "800" />


# Diffusers version

Please ensure that you have installed the latest version of [Diffusers](https://github.com/huggingface/diffusers).





# Demo
```python
import torch
from diffusers.utils import load_image
from diffusers.pipelines.flux.pipeline_flux_controlnet import FluxControlNetPipeline
from diffusers.models.controlnet_flux import FluxControlNetModel

base_model = 'black-forest-labs/FLUX.1-dev'
controlnet_model = 'InstantX/FLUX.1-dev-Controlnet-Canny'
controlnet = FluxControlNetModel.from_pretrained(controlnet_model, torch_dtype=torch.bfloat16)
pipe = FluxControlNetPipeline.from_pretrained(base_model, controlnet=controlnet, torch_dtype=torch.bfloat16)
pipe.to("cuda")

control_image = load_image("https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Canny/resolve/main/canny.jpg")
prompt = "A girl in city, 25 years old, cool, futuristic"
image = pipe(
    prompt, 
    control_image=control_image,
    controlnet_conditioning_scale=0.6,
    num_inference_steps=28, 
    guidance_scale=3.5,
).images[0]
image.save("image.jpg")
```







