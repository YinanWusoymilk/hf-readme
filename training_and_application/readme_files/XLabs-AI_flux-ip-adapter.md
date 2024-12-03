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
- controlnet
---

![Banner Picture 1](assets/banner-green.png?raw=true)
[<img src="https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/light/join-our-discord-rev1.png?raw=true">](https://discord.gg/FHY2guThfy)
![Greek Picture 1](assets/x_greek.png?raw=true)

This repository provides a IP-Adapter checkpoint for
[FLUX.1-dev model](https://huggingface.co/black-forest-labs/FLUX.1-dev) by Black Forest Labs

[See our github](https://github.com/XLabs-AI/x-flux-comfyui) for comfy ui workflows.
![Flow Example Picture 1](assets/ip_adapter_workflow_example.png?raw=true)

# Models
IP-Adapter is trained on 512x512 resolution for 50k steps and 1024x1024 for 25k steps resolution and works for both 512x512 and 1024x1024 resolution. Model is training, we release new checkpoints regularly, stay updated.
We release **v1 version** - which can be used directly in ComfyUI!   

Please, see our [ComfyUI custom nodes installation guide](https://github.com/XLabs-AI/x-flux-comfyui)

# Examples

See examples of our models results below.  
Also, some generation results with input images are provided in "Files and versions"

# Inference

To try our models, you have 2 options:
1. Use main.py from our [official repo](https://github.com/XLabs-AI/x-flux)
2. Use our custom nodes for ComfyUI and test it with provided workflows (check out folder /workflows)

## Instruction for ComfyUI 
1. Go to ComfyUI/custom_nodes
2. Clone [x-flux-comfyui](https://github.com/XLabs-AI/x-flux-comfyui.git), path should be ComfyUI/custom_nodes/x-flux-comfyui/*, where * is all the files in this repo
3. Go to ComfyUI/custom_nodes/x-flux-comfyui/ and run python setup.py
4. Update x-flux-comfy with `git pull` or reinstall it.
5. Download Clip-L `model.safetensors` from [OpenAI VIT CLIP large](https://huggingface.co/openai/clip-vit-large-patch14), and put it to `ComfyUI/models/clip_vision/*`.
6. Download our IPAdapter from [huggingface](https://huggingface.co/XLabs-AI/flux-ip-adapter/tree/main), and put it to `ComfyUI/models/xlabs/ipadapters/*`.
7. Use `Flux Load IPAdapter` and `Apply Flux IPAdapter` nodes, choose right CLIP model and enjoy your genereations.
8. You can find example workflow in folder workflows in this repo.

If you get bad results, try to set true_gs=2

### Limitations
The IP Adapter is currently in beta.
We do not guarantee that you will get a good result right away, it may take more attempts to get a result. 

![Example Picture 2](assets/ip_adapter_example2.png?raw=true)
![Example Picture 1](assets/ip_adapter_example1.png?raw=true)

## License

Our weights fall under the [FLUX.1 [dev]](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md) Non-Commercial License<br/>