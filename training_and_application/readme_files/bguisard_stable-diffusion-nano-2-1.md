---
license: creativeml-openrail-m
base_model: stabilityai/stable-diffusion-2-1-base
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
- jax-diffusers-event
inference: true
datasets:
- ChristophSchuhmann/improved_aesthetics_6plus
---

# Stable Diffusion Nano 2.1

Stable Diffusion Nano was built during the [JAX/Diffusers community sprint 🧨](https://github.com/huggingface/community-events/tree/main/jax-controlnet-sprint#jaxdiffusers-community-sprint-).

Based on stable diffusion and fine-tuned on 128x128 images, Stable Diffusion Nano
allows for fast prototyping of diffusion models, enabling quick experimentation
with easily available hardware.

It performs reasonably well on several tasks, but it struggles with small details
such as faces.

prompt: A watercolor painting of an otter

![images_0)](./images_0.png)

prompt: Marvel MCU deadpool, red mask, red shirt, red gloves, black shoulders,
black elbow pads, black legs, gold buckle, black belt, black mask, white eyes,
black boots, fuji low light color 35mm film, downtown Osaka alley at night out
of focus in background, neon lights

![images_1)](./images_1.png)


## Training details
All parameters were initialized from the [stabilityai/stable-diffusion-2-1-base](https://huggingface.co/stabilityai/stable-diffusion-2-1-base)
model. The unet was fine tuned as follows:

U-net fine-tuning:
- 200,000 steps, learning rate = 1e-5, batch size = 992 (248 per TPU).
- 100,000 steps, SNR gamma = 5.0, learning rate = 1e-5, batch size = 992 (248 per TPU).
- Trained on [LAION Improved Aesthetics 6plus](https://huggingface.co/datasets/ChristophSchuhmann/improved_aesthetics_6plus).


## License
This model is open access and available to all, with a CreativeML OpenRAIL-M license
further specifying rights and usage. The CreativeML OpenRAIL License specifies:

- You can't use the model to deliberately produce nor share illegal or harmful outputs or content.
- The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license.
- You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully) Please read the full license here.