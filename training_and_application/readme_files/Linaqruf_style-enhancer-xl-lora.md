---
library_name: diffusers
license: openrail++
language:
- en
tags:
  - text-to-image
  - stable-diffusion
  - lora
  - safetensors
  - stable-diffusion-xl
base_model: Linaqruf/animagine-xl-2.0
widget:
- text: face focus, cute, masterpiece, best quality, 1girl, green hair, sweater, looking at viewer, upper body, beanie, outdoors, night, turtleneck
  parameter:
    negative_prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry
  example_title: 1girl
- text: face focus, bishounen, masterpiece, best quality, 1boy, green hair, sweater, looking at viewer, upper body, beanie, outdoors, night, turtleneck
  parameter:
    negative_prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry
  example_title: 1boy
---

<style>
  .title-container {
    display: flex;
    flex-direction: column; /* Allow vertical stacking of title and subtitle */
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f5f5f5;
  }

  .title {
    font-size: 2em;
    text-align: center;
    color: #333;
    font-family: 'Verdana', sans-serif;
    text-transform: uppercase;
    padding: 1em;
    box-shadow: 0px 0px 0px rgba(0,0,0,0.1);
  }
  
  .title span {
    background: -webkit-linear-gradient(45deg, #ff9a9e, #fad0c4, #f6d365);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  
  .custom-table {
    table-layout: fixed;
    width: 100%;
    border-collapse: collapse;
    margin-top: 2em;
  }

  .custom-table td {
    width: 50%;
    vertical-align: top;
    padding: 10px;
    box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0.15);
  }

  .custom-image-container {
    position: relative;
    width: 100%;
    margin-bottom: 0em;
    overflow: hidden;
    border-radius: 10px;
    transition: transform .7s;
    /* Smooth transition for the container */
  }

  .custom-image-container:hover {
    transform: scale(1.05);
    /* Scale the container on hover */
  }

  .custom-image {
    width: 100%;
    height: auto;
    object-fit: cover;
    border-radius: 10px;
    transition: transform .7s;
    margin-bottom: 0em;
  }

  .nsfw-filter {
    filter: blur(8px); /* Apply a blur effect */
    transition: filter 0.3s ease; /* Smooth transition for the blur effect */
  }

  .custom-image-container:hover .nsfw-filter {
    filter: none; /* Remove the blur effect on hover */
  }
</style>

<h1 class="title">
  <span>Style Enhancer XL LoRA</span>
</h1>
<table class="custom-table">
  <tr>
    <td>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/kMqCcN3CpMPHO1qyEgnGk.png" alt="sample1">
      </div>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/pfLIDf7ZX6WJHgTlfqiQk.png" alt="sample4">
      </div>
    </td>
    <td>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/s5ZCIaETb_eKijgbLbXwU.png" alt="sample2">
      </div>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/qjC5jKExA_JE5BuQJ6-Ue.png" alt="sample3">
    </td>
    <td>
      <div class="custom-image-container">
        <img class="custom-image nsfw-filter" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/1vvUY1qbgot5np4CPmORh.png" alt="sample1">
      </div>
      <div class="custom-image-container">
        <img class="custom-image" src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/7OQJdRKKpZponZiZ8cOre.png" alt="sample4">
      </div>
    </td>
  </tr>
</table>

<hr>

## Overview

**Style Enhancer XL LoRA** is an advanced, high-resolution LoRA (Low-Rank Adaptation) adapter designed to enhance the capabilities of Animagine XL 2.0. This innovative model excels in fine-tuning and refining anime-style images, producing unparalleled quality and detail. It seamlessly integrates with the Stable Diffusion XL framework, and uniquely supports Danbooru tags for precise and creative image generation.

Example tags include _**face focus, cute, masterpiece, best quality, 1girl, green hair, sweater, looking at viewer, upper body, beanie, outdoors, night, turtleneck**_.

<hr>

## Model Details

- **Developed by:** [Linaqruf](https://github.com/Linaqruf)
- **Model type:** LoRA adapter for Stable Diffusion XL
- **Model Description:** A compact yet powerful adapter designed to augment and enhance the output of large models like Animagine XL 2.0. This adapter not only improves the style and quality of anime-themed images but also allows users to recreate the distinct 'old-school' art style of SD 1.5. It's the perfect tool for generating high-fidelity, anime-inspired visual content.
- **License:** [CreativeML Open RAIL++-M License](https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/LICENSE-MODEL)
- **Finetuned from model:** [Animagine XL 2.0](https://huggingface.co/Linaqruf/animagine-xl-2.0)

<hr>

## 🧨 Diffusers Installation

Ensure the installation of the latest `diffusers` library, along with other essential packages:

```bash
pip install diffusers --upgrade
pip install transformers accelerate safetensors
```

The following Python script demonstrates how to utilize the Style Enhancer XL LoRA with Animagine XL 2.0. The default scheduler is EulerAncestralDiscreteScheduler, but it can be explicitly defined for clarity.

```py
import torch
from diffusers import (
    StableDiffusionXLPipeline, 
    EulerAncestralDiscreteScheduler,
    AutoencoderKL
)

# Initialize LoRA model and weights
lora_model_id = "Linaqruf/style-enhancer-xl-lora"
lora_filename = "style-enhancer-xl.safetensors"

# Load VAE component
vae = AutoencoderKL.from_pretrained(
    "madebyollin/sdxl-vae-fp16-fix", 
    torch_dtype=torch.float16
)

# Configure the pipeline
pipe = StableDiffusionXLPipeline.from_pretrained(
    "Linaqruf/animagine-xl-2.0", 
    vae=vae,
    torch_dtype=torch.float16, 
    use_safetensors=True, 
    variant="fp16"
)
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
pipe.to('cuda')

# Load and fuse LoRA weights
pipe.load_lora_weights(lora_model_id, weight_name=lora_filename)
pipe.fuse_lora(lora_scale=0.6)

# Define prompts and generate image
prompt = "face focus, cute, masterpiece, best quality, 1girl, green hair, sweater, looking at viewer, upper body, beanie, outdoors, night, turtleneck"
negative_prompt = "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"

image = pipe(
    prompt, 
    negative_prompt=negative_prompt, 
    width=1024,
    height=1024,
    guidance_scale=12,
    num_inference_steps=50
).images[0]

# Unfuse LoRA before saving the image
pipe.unfuse_lora()
image.save("anime_girl.png")

```
