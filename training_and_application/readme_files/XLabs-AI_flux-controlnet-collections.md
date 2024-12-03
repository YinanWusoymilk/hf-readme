---
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.
language:
- en
pipeline_tag: text-to-image
tags:
- Stable Diffusion
- image-generation
- Flux
- diffusers
---

![Controlnet collections for Flux](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/light/flux-controlnet-collections.png?raw=true)
[<img src="https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/light/join-our-discord-rev1.png?raw=true">](https://discord.gg/FHY2guThfy)

This repository provides a collection of ControlNet checkpoints for
[FLUX.1-dev model](https://huggingface.co/black-forest-labs/FLUX.1-dev) by Black Forest Labs

![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/depth_result1.png?raw=true)

[See our github](https://github.com/XLabs-AI/x-flux-comfyui) for comfy ui workflows.
![Example Picture 1](https://github.com/XLabs-AI/x-flux-comfyui/blob/main/assets/image1.png?raw=true)

[See our github](https://github.com/XLabs-AI/x-flux) for train script, train configs and demo script for inference.

# Models

Our collection supports 3 models:
- Canny
- HED
- Depth (Midas)

Each ControlNet is trained on 1024x1024 resolution and works for 1024x1024 resolution.
We release **v3 versions** - better and realistic versions, which can be used directly in ComfyUI!   

Please, see our [ComfyUI custom nodes installation guide](https://github.com/XLabs-AI/x-flux-comfyui)


# Examples

See examples of our models results below.  
Also, some generation results with input images are provided in "Files and versions"

# Inference

To try our models, you have 2 options:
1. Use main.py from our [official repo](https://github.com/XLabs-AI/x-flux)
2. Use our custom nodes for ComfyUI and test it with provided workflows (check out folder /workflows)
3. Use gradio demo

See examples how to launch our models:

## Canny ControlNet (version 3)

1. Clone our [x-flux-comfyui](https://github.com/XLabs-AI/x-flux-comfyui) custom nodes
2. Launch ComfyUI
3. Try our canny_workflow.json

![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/canny_result1.png?raw=true)
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/canny_result2.png?raw=true)


## Depth ControlNet (version 3)

1. Clone our [x-flux-comfyui](https://github.com/XLabs-AI/x-flux-comfyui) custom nodes
2. Launch ComfyUI
3. Try our depth_workflow.json

![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/depth_result1.png?raw=true)
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/depth_result2.png?raw=true)


## HED ControlNet (version 3)

1. Clone our [x-flux-comfyui](https://github.com/XLabs-AI/x-flux-comfyui) custom nodes
2. Launch ComfyUI
3. Try our hed_workflow.json

![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/hed_result1.png?raw=true)

## License

Our weights fall under the [FLUX.1 [dev]](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md) Non-Commercial License<br/>