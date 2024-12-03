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


# FLUX.1-dev-Controlnet-Union

<img src="./images/image_union.png" width = "1000" />


## Release

- [2024/08/26] 🔥 Release [FLUX.1-dev-ControlNet-Union-Pro](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro). Please install from [the source](https://github.com/huggingface/diffusers) before the next release. We have supported CN-Union and Multi-ControlNets via [this PR](https://github.com/huggingface/diffusers/pull/9175).

- [2024/08/20] Release the beta version.

- [2024/08/14] Release the alpha version.



## Checkpoint

The training of union controlnet requires a significant amount of computational power. 
The current release is the first beta version checkpoint that maybe not been fully trained. 
The fully trainedbeta version is in the training process. 
We have conducted ablation studies that have demonstrated the validity of the code. 
The open-source release of the first beta version is solely to facilitate the rapid growth of the open-source community and the Flux ecosystem; 
it is common to encounter bad cases (please accept my apologies). 
It is worth noting that we have found that even a fully trained Union model may not perform as well as specialized models, such as pose control. 
However, as training progresses, the performance of the Union model will continue to approach that of specialized models.


## Control Mode

| Control Mode | Description | Current Model Validity |
|:------------:|:-----------:|:-----------:|
|0|canny|🟢high|
|1|tile|🟢high|
|2|depth|🟢high|
|3|blur|🟢high|
|4|pose|🟢high|
|5|gray|🔴low|
|6|lq|🟢high|


# Inference
```python
import torch
from diffusers.utils import load_image
from diffusers import FluxControlNetPipeline, FluxControlNetModel

base_model = 'black-forest-labs/FLUX.1-dev'
controlnet_model = 'InstantX/FLUX.1-dev-Controlnet-Union'

controlnet = FluxControlNetModel.from_pretrained(controlnet_model, torch_dtype=torch.bfloat16)
pipe = FluxControlNetPipeline.from_pretrained(base_model, controlnet=controlnet, torch_dtype=torch.bfloat16)
pipe.to("cuda")

control_image_canny = load_image("https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Union-alpha/resolve/main/images/canny.jpg")
controlnet_conditioning_scale = 0.5
control_mode = 0

width, height = control_image.size

prompt = 'A bohemian-style female travel blogger with sun-kissed skin and messy beach waves.'

image = pipe(
    prompt, 
    control_image=control_image,
    control_mode=control_mode,
    width=width,
    height=height,
    controlnet_conditioning_scale=controlnet_conditioning_scale,
    num_inference_steps=24, 
    guidance_scale=3.5,
).images[0]
image.save("image.jpg")
```

# Multi-Controls Inference
```python
import torch
from diffusers.utils import load_image
from diffusers import FluxControlNetPipeline, FluxControlNetModel, FluxMultiControlNetModel

base_model = 'black-forest-labs/FLUX.1-dev'
controlnet_model_union = 'InstantX/FLUX.1-dev-Controlnet-Union'

controlnet_union = FluxControlNetModel.from_pretrained(controlnet_model_union, torch_dtype=torch.bfloat16)
controlnet = FluxMultiControlNetModel([controlnet_union]) # we always recommend loading via FluxMultiControlNetModel

pipe = FluxControlNetPipeline.from_pretrained(base_model, controlnet=controlnet, torch_dtype=torch.bfloat16)
pipe.to("cuda")

prompt = 'A bohemian-style female travel blogger with sun-kissed skin and messy beach waves.'
control_image_depth = load_image("https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Union/resolve/main/images/depth.jpg")
control_mode_depth = 2

control_image_canny = load_image("https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Union/resolve/main/images/canny.jpg")
control_mode_canny = 0

width, height = control_image.size

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

# Resources
- [InstantX/FLUX.1-dev-Controlnet-Canny](https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Canny)
- [InstantX/FLUX.1-dev-Controlnet-Union](https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Union)
- [Shakker-Labs/FLUX.1-dev-ControlNet-Depth](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Depth)
- [Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro](https://huggingface.co/Shakker-Labs/FLUX.1-dev-ControlNet-Union-Pro)

# Acknowledgements
Thanks [zzzzzero](https://github.com/zzzzzero) for help us pointing out some bugs in the training.
