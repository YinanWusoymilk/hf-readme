---
license: other
license_name: fluently-license
license_link: https://huggingface.co/spaces/fluently/License
datasets:
- ehristoforu/midjourney-images
- ehristoforu/dalle-3-images
- ehristoforu/fav_images
library_name: diffusers
pipeline_tag: text-to-image
base_model: stabilityai/stable-diffusion-xl-base-1.0
tags:
- safetensors
- stable-diffusion
- sdxl
- fluetnly-xl
- fluently
- trained
inference:
  parameters:
    num_inference_steps: 25
    guidance_scale: 5
    negative_prompt: "(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation"
  
---
# **Fluently XL** V4 - the best XL-model (4th place in the [imgsys.org](https://imgsys.org/rankings) arena)

![preview](images/preview.png)


Introducing Fluently XL, you are probably ready to argue with the name of the model: “The best XL-model”, but now I will prove to you why it is true.

## About this model

The model was obtained through training on *expensive graphics accelerators*, a lot of work was done, now we will show why this XL model is better than others.

### Features

  - Correct anatomy

  - Art and realism in one

  - Controling contrast

  - Great nature

  - Great faces without AfterDetailer

### More info

Our model is better than others because we do not mix but **train**, but at first it may seem that the model is not very good, but if you are a real professional you will like it.

## Using

Optimal parameters in Automatic1111/ComfyUI:

  - Sampling steps: 20-35

  - Sampler method: Euler a/Euler

  - CFG Scale: 4-6.5

## End

Let's remove models that copy each other from the top and put one that is actually developing, thank you)