---
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.
language:
- en
pipeline_tag: text-to-image
tags:
- lora
- Stable Diffusion
- image-generation
- Flux
- diffusers
base_model: black-forest-labs/FLUX.1-dev
---
![Lora Photorealism for Flux](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/light/lora-photorealism-header-rev1.png?raw=true)
[<img src="https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/light/join-our-discord-rev1.png?raw=true">](https://discord.gg/FHY2guThfy)

This repository provides a checkpoint with trained LoRA photorealism for
[FLUX.1-dev model](https://huggingface.co/black-forest-labs/FLUX.1-dev) by Black Forest Labs

![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/picture-6-rev1.png?raw=true)
# ComfyUI

[See our github](https://github.com/XLabs-AI/x-flux-comfyui) for comfy ui workflows.
![Example Picture 1](https://github.com/XLabs-AI/x-flux-comfyui/blob/main/assets/image1.png?raw=true)
# Training details
[XLabs AI](https://github.com/XLabs-AI) team is happy to publish fine-tuning Flux scripts, including:

- **LoRA** 🔥
- **ControlNet** 🔥

[See our github](https://github.com/XLabs-AI/x-flux) for train script and train configs.

# Training Dataset
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
```bash
python3 demo_lora_inference.py \
    --checkpoint lora.safetensors \
    --prompt " handsome girl in a suit covered with bold tattoos and holding a pistol. Animatrix illustration style, fantasy style, natural photo cinematic"
```

![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/picture-0-rev1.png?raw=true)


# License

lora.safetensors falls under the [FLUX.1 [dev]](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md) Non-Commercial License<br/>