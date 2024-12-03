---
language:
- en
tags:
- stable-diffusion-xl
- text-to-image
license: unknown
inference: true

---

### NOTE: The work here is a Work in Progress! Nothing in this repository is final.

# waifu-diffusion-xl - Diffusion for Rich Weebs

waifu-diffusion-xl is a latent text-to-image diffusion model that has been conditioned on high-quality anime images through fine-tuning StabilityAI's SDXL 0.9 model provided as a research preview.

![image](https://user-images.githubusercontent.com/26317155/254350263-59eca9df-503d-4ee7-b12e-b060d8eebd60.png)

<sub>masterpiece, best quality, 1girl, green hair, sweater, looking at viewer, upper body, beanie, outdoors, watercolor, night, turtleneck</sub>

## Model Description(s)

- [wdxl-aesthetic-0.9](https://huggingface.co/hakurei/waifu-diffusion-xl/blob/main/wdxl-aesthetic-0.9.safetensors) is a checkpoint that has been finetuned against our in-house aesthetic dataset which was created with the help of 15k aesthetic labels collected by volunteers. This model also used Stability.AI's [SDXL 0.9 checkpoint](https://huggingface.co/stabilityai/stable-diffusion-xl-base-0.9) as the base model for finetuning.

## License

This model has been released under the [SDXL 0.9 RESEARCH LICENSE AGREEMENT](https://huggingface.co/hakurei/waifu-diffusion-xl/blob/main/LICENSE.md) due to the repository containing the SDXL 0.9 weights before an official release. We have been given permission to release this model.

## Downstream Uses

This model can be used for entertainment purposes and as a generative art assistant.

## Team Members and Acknowledgements

This project would not have been possible without the incredible work by Stability AI and Novel AI.

- [Haru](https://github.com/harubaru)
- [Salt](https://github.com/sALTaccount/)
- [closertodeath](https://huggingface.co/closertodeath)
- [Kudo](https://negotiator.itch.io/)

In order to reach us, you can join our [Discord server](https://discord.gg/touhouai).

[![Discord Server](https://discordapp.com/api/guilds/930499730843250783/widget.png?style=banner2)](https://discord.gg/touhouai)