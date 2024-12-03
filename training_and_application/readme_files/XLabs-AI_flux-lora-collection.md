---
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.
language:
- en
pipeline_tag: text-to-image
tags:
- LoRA
- Stable Diffusion
- image-generation
- Flux
---
![FLUX LoRA Collections](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/light/flux-lora-collection-rev1.png?raw=true)
This repository provides a checkpoint with trained LoRAs for
[FLUX.1-dev model](https://huggingface.co/black-forest-labs/FLUX.1-dev) by Black Forest Labs
[<img src="https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/light/join-our-discord-rev1.png?raw=true">](https://discord.gg/FHY2guThfy)

![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/furry4.png?raw=true)
# ComfyUI

[See our github](https://github.com/XLabs-AI/x-flux-comfyui) for comfy ui workflows.
![Example Picture 1](https://github.com/XLabs-AI/x-flux-comfyui/blob/main/assets/image1.png?raw=true)
# Training details
[XLabs AI](https://github.com/XLabs-AI) team is happy to publish fune-tuning Flux scripts, including:

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

Thank https://civitai.com/user/dobrosketchkun and https://civitai.com/user/sadxzero for datasets for loras

# Inference
## furry_lora
```bash
python3 main.py \
 --prompt "Female furry Pixie with text 'hello world'" \
 --lora_repo_id XLabs-AI/flux-furry-lora --lora_name furry_lora.safetensors --device cuda --offload --use_lora \
 --model_type flux-dev-fp8 --width 1024 --height 1024 \
 --timestep_to_start_cfg 1 --num_steps 25 --true_gs 3.5 --guidance 4

```
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/furry4.png?raw=true)
```bash
python3 main.py \
 --prompt "Male furry Lycanthrope with fur-covered body in ancient ruins, howling at the full moon, surrounded by eerie mist, werewolf transformation, elder scrolls, eslweyr, glitch aesthetic, anime-inspired, digital illustration, artstation, furry" \
 --lora_repo_id XLabs-AI/flux-furry-lora --lora_name furry_lora.safetensors --device cuda --offload --use_lora \
 --model_type flux-dev-fp8 --width 1024 --height 1024 \
 --timestep_to_start_cfg 1 --num_steps 25 --true_gs 3.5

```

![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/furry2.png?raw=true)
## mjv6_lora
```bash
python3 main.py \
--prompt "A handsome man in a suit, 25 years old, cool, futuristic" \
--lora_repo_id XLabs-AI/flux-lora-collection --lora_name mjv6_lora.safetensors \
--device cuda:4 --offload --use_lora --model_type flux-dev-fp8 --width 1024 --height 1024
```

![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/result_13.png?raw=true)

```bash
python3 main.py \
--prompt "A girl in a suit covered with bold tattoos and holding a vest pistol, beautiful woman, 25 years old, cool, future fantasy, turquoise & light orange ping curl hair" \
--lora_repo_id XLabs-AI/flux-lora-collection --lora_name mjv6_lora.safetensors \
--device cuda --offload --use_lora --model_type flux-dev-fp8 --width 1024 --height 1024
```

![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/result_12.png?raw=true)
## anime_lora
```bash
python3 main.py \
--prompt "A cute corgi lives in a house made out of sushi, anime" \
--lora_repo_id XLabs-AI/flux-lora-collection --lora_name anime_lora.safetensors \
--device cuda --offload --use_lora --model_type flux-dev-fp8 --width 1024 --height 1024
```
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/result_14.png?raw=true)
```bash
python3 main.py \
--prompt "a girl with orange hair, standing in a room with a window, looking out at a cityscape, anime" \
--lora_repo_id XLabs-AI/flux-lora-collection --lora_name anime_lora.safetensors \
--device cuda --offload --use_lora --model_type flux-dev-fp8 --width 1024 --height 1024
```
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/result_15.png?raw=true)

## disney_lora
```bash
python3 main.py \
--prompt "An aerial view of beach with people on it, disney style" \
--lora_repo_id XLabs-AI/flux-lora-collection --lora_name disney_lora.safetensors \
--device cuda --offload --use_lora --model_type flux-dev-fp8 --width 1024 --height 1024
```
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/result_19.png?raw=true)

```bash
python3 main.py \
--prompt "A blue jay standing on a large basket of rainbow macarons, disney style" \
--lora_repo_id XLabs-AI/flux-lora-collection --lora_name disney_lora.safetensors \
--device cuda --offload --use_lora --model_type flux-dev-fp8 --width 1024 --height 1024
```
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/result_18.png?raw=true)

## scenery_lora
```bash
python3 main.py \
--prompt "A fantasy cityscape with multiple buildings and skyscrapers all of which are covered in snow and ice, scenery style" \
--lora_repo_id XLabs-AI/flux-lora-collection --lora_name scenery_lora.safetensors \
--device cuda --offload --use_lora --model_type flux-dev-fp8 --width 1024 --height 1024
```
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/result_21.png?raw=true)

```bash
python3 main.py \
--prompt "A large ornate building with multiple levels and arches surrounded by trees and greenery. In front of it there are several statues and sculptures on pedestals with fire burning brightly in front of them, scenery style" \
--lora_repo_id XLabs-AI/flux-lora-collection --lora_name scenery_lora.safetensors \
--device cuda --offload --use_lora --model_type flux-dev-fp8 --width 1024 --height 1024
```
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/result_22.png?raw=true)
## art_lora
```bash
python3 main.py \
--prompt "white rabbit in blue dress and hat holding bow and arrow, art" \
--lora_repo_id XLabs-AI/flux-lora-collection --lora_name art_lora.safetensors \
--device cuda --offload --use_lora --model_type flux-dev-fp8 --width 1024 --height 1024
```
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/result_23.png?raw=true)

```bash
python3 main.py \
--prompt "castle in the middle of forest at night, art" \
--lora_repo_id XLabs-AI/flux-lora-collection --lora_name art_lora.safetensors \
--device cuda --offload --use_lora --model_type flux-dev-fp8 --width 1024 --height 1024
```
![Example Picture 1](https://github.com/XLabs-AI/x-flux/blob/main/assets/readme/examples/result_24.png?raw=true)
# License

lora.safetensors falls under the [FLUX.1 [dev]](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md) Non-Commercial License<br/>