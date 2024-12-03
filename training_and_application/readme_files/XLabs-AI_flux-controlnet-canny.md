---
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
tags:
- Text-to-Image
- ControlNet
- Stable Diffusion
- diffusers
pipeline_tag: text-to-image
base_model: black-forest-labs/FLUX.1-dev
language:
- en
---

![ControlNet Canny for Flux](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/light/controlnet-canny-header-rev1.png?raw=true)

This repository provides a checkpoint with trained ControlNet Canny model for
[FLUX.1-dev model](https://huggingface.co/black-forest-labs/FLUX.1-dev) by Black Forest Labs
# ComfyUI

[See our github](https://github.com/XLabs-AI/x-flux-comfyui) for comfy ui workflows.
![Example Picture 1](https://github.com/XLabs-AI/x-flux-comfyui/blob/main/assets/image1.png?raw=true)
# Training details
[XLabs AI](https://github.com/XLabs-AI) team is happy to publish fune-tuning Flux scripts, including:
- **LoRA** 🔥
- **ControlNet** 🔥

[See our github](https://github.com/XLabs-AI/x-flux) for train script and train configs.

# Training dataset
Dataset has the following format for the training process:
```
├── images/
│    ├── 1.png
│    ├── 1.json
│    ├── 2.png
│    ├── 2.json
│    ├── ...
```
A .json file contains "caption" field with a text prompt.

# Inference

To test our checkpoints, use commands presented below.
```bash
python3 demo_controlnet_inference.py \
    --checkpoint controlnet.safetensors \
    --control_image "input_image.jpg" \
    --prompt "a handsome viking man with white hair, cinematic, MM full HD"
```
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/picture-3-rev1.png?raw=true)
```bash
python3 demo_controlnet_inference.py \
    --checkpoint controlnet.safetensors \
    --control_image "input_image.jpg" \
    --prompt "a dark evil mysterius house with ghosts, cinematic, MM full HD"
```

![Example Picture 2](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/picture-2-rev1.png?raw=true)


# License
controlnet.safetensors falls under the [FLUX.1 [dev]](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md) Non-Commercial License<br/>