---
library_name: diffusionkit
language:
- en
license: apache-2.0
tags:
- text-to-image
- image-generation
- flux
- mlx
---
# FLUX.1-schnell on DiffusionKit MLX!
## Check out the [original model](https://huggingface.co/black-forest-labs/FLUX.1-schnell)!
## Check out the [DiffusionKit](https://github.com/argmaxinc/DiffusionKit) github repository!
![FLUX.1 [schnell] Grid](./flux_on_mac.png)
# Usage
- ## Create conda environment
```shell
conda create -n diffusionkit python=3.11 -y
conda activate diffusionkit
pip install diffusionkit
```
- ## Run the cli command
```shell
diffusionkit-cli --prompt "detailed cinematic dof render of a \
detailed MacBook Pro on a wooden desk in a dim room with items \
around, messy dirty room. On the screen are the letters 'FLUX on \
DiffusionKit' glowing softly. High detail hard surface render" \
--height 768 \
--width 1360 \
--seed 1001 \
--step 4 \
--output ~/Desktop/flux_on_mac.png
```