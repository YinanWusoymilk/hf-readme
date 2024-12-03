---
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md

language:
  - en
library_name: diffusers
pipeline_tag: text-to-image

tags:
- Text-to-Image
- ControlNet
- Diffusers
- Flux.1-dev
- image-generation
- Stable Diffusion
base_model: black-forest-labs/FLUX.1-dev
---

# FLUX.1-dev-ControlNet-Union-Pro

This repository contains a unified ControlNet for FLUX.1-dev model jointly released by researchers from [InstantX Team](https://huggingface.co/InstantX) and [Shakker Labs](https://huggingface.co/Shakker-Labs).

<div class="container">
  <img src="./assets/poster.png" width="1024"/>
</div>


# Model Cards
- This checkpoint is a Pro version of [FLUX.1-dev-Controlnet-Union](https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Union) trained with more steps and datasets.
- This model supports 7 control modes, including canny (0), tile (1), depth (2), blur (3), pose (4), gray (5), low quality (6).
- The recommended controlnet_conditioning_scale is 0.3-0.8.
- This model can be jointly used with other ControlNets.


# Showcases

<div class="container">
  <img src="./assets/teaser1.png" width="1024"/>
  <img src="./assets/teaser2.png" width="1024"/>
  <img src="./assets/teaser3.png" width="1024"/>
</div>


# Inference
Please install `diffusers` from [the source](https://github.com/huggingface/diffusers), as [the PR](https://github.com/huggingface/diffusers/pull/9175) has not been included in currently released version yet.

# Multi-Controls Inference
```python
import torch
from diffusers.utils import load_image

from diffusers import FluxControlNetPipeline, FluxControlNetModel
from diffusers.models import FluxMultiControlNetModel

base_model = 'black-forest-labs/FLUX.1-dev'
controlnet_model_union = 'Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro'

controlnet_union = FluxControlNetModel.from_pretrained(controlnet_model_union, torch_dtype=torch.bfloat16)
controlnet = FluxMultiControlNetModel([controlnet_union]) # we always recommend loading via FluxMultiControlNetModel

pipe = FluxControlNetPipeline.from_pretrained(base_model, controlnet=controlnet, torch_dtype=torch.bfloat16)
pipe.to("cuda")

prompt = 'A bohemian-style female travel blogger with sun-kissed skin and messy beach waves.'
control_image_depth = load_image("https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro/resolve/main/assets/depth.jpg")
control_mode_depth = 2

control_image_canny = load_image("https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro/resolve/main/assets/canny.jpg")
control_mode_canny = 0

width, height = control_image_depth.size

image = pipe(
    prompt, 
    control_image=[control_image_depth, control_image_canny],
    control_mode=[control_mode_depth, control_mode_canny],
    width=width,
    height=height,
    controlnet_conditioning_scale=[0.2, 0.4],
    num_inference_steps=24, 
    guidance_scale=3.5,
    generator=torch.manual_seed(42),
).images[0]
```

We also support loading multiple ControlNets as before, you can load as
```python
from diffusers import FluxControlNetModel
from diffusers.models import FluxMultiControlNetModel

controlnet_model_union = 'Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro'
controlnet_union = FluxControlNetModel.from_pretrained(controlnet_model_union, torch_dtype=torch.bfloat16)

controlnet_model_depth = 'Shakker-Labs/FLUX.1-dev-Controlnet-Depth'
controlnet_depth = FluxControlNetModel.from_pretrained(controlnet_model_depth, torch_dtype=torch.bfloat16)

controlnet = FluxMultiControlNetModel([controlnet_union, controlnet_depth])

# set mode to None for other ControlNets
control_mode=[2, None]
```

# Resources
- [InstantX/FLUX.1-dev-Controlnet-Canny](https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Canny)
- [Shakker-Labs/FLUX.1-dev-ControlNet-Depth](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Depth)
- [Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro)

# Acknowledgements
This project is trained by [InstantX Team](https://huggingface.co/InstantX) and sponsored by [Shakker AI](https://www.shakker.ai/). The original idea is inspired by [xinsir/controlnet-union-sdxl-1.0](https://huggingface.co/xinsir/controlnet-union-sdxl-1.0). All copyright reserved.
