---
base_model:
- black-forest-labs/FLUX.1-dev
library_name: diffusers
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
pipeline_tag: image-to-image
inference: False
tags:
- ControlNet
- super-resolution
- upscaler
---
# ⚡ Flux.1-dev: Upscaler ControlNet ⚡

This is [Flux.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) ControlNet for low resolution images developed by Jasper research team.

<p align="center">
   <img style="width:700px;" src="examples/showcase.jpg">
</p>

# How to use
This model can be used directly with the `diffusers` library

```python
import torch
from diffusers.utils import load_image
from diffusers import FluxControlNetModel
from diffusers.pipelines import FluxControlNetPipeline

# Load pipeline
controlnet = FluxControlNetModel.from_pretrained(
  "jasperai/Flux.1-dev-Controlnet-Upscaler",
  torch_dtype=torch.bfloat16
)
pipe = FluxControlNetPipeline.from_pretrained(
  "black-forest-labs/FLUX.1-dev",
  controlnet=controlnet,
  torch_dtype=torch.bfloat16
)
pipe.to("cuda")

# Load a control image
control_image = load_image(
  "https://huggingface.co/jasperai/Flux.1-dev-Controlnet-Upscaler/resolve/main/examples/input.jpg"
)

w, h = control_image.size

# Upscale x4
control_image = control_image.resize((w * 4, h * 4))

image = pipe(
    prompt="", 
    control_image=control_image,
    controlnet_conditioning_scale=0.6,
    num_inference_steps=28, 
    guidance_scale=3.5,
    height=control_image.size[1],
    width=control_image.size[0]
).images[0]
image
```

<p align="center">
   <img style="width:500px;" src="examples/output.jpg">
</p>


# Training
This model was trained with a synthetic complex data degradation scheme taking as input a *real-life* image and artificially degrading it by combining several degradations such as amongst other image noising (Gaussian, Poisson), image blurring and JPEG compression in a similar spirit as [1]

[1] Wang, Xintao, et al. "Real-esrgan: Training real-world blind super-resolution with pure synthetic data." Proceedings of the IEEE/CVF international conference on computer vision. 2021.

# Licence
This model falls under the [Flux.1-dev model licence](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md).