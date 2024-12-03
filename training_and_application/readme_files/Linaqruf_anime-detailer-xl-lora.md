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
    body {
        font-family: 'Verdana', sans-serif;
        background-color: #f5f5f5;
        margin: 0;
        padding: 0;
    }
    
    .title-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f5f5f5;
    }
    
    .title {
        font-size: 3em;
        text-align: center;
        color: #333;
        text-transform: uppercase;
        padding: 0.5em;
        font-weight: bold;
    }
    
    .title span {
        background: -webkit-linear-gradient(45deg, #ff9a9e, #fad0c4, #f6d365);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .gallery-container {
        max-width: 90%;
        margin: 20px auto;
        text-align: center;
        position: relative;
    }
    
    .gallery-radio {
        display: none;
    }
    
    .gallery-image {
        display: none;
        width: 100%;
        margin: 20px auto;
        transition: opacity 0.3s ease;
    }
    
    .gallery-image img {
        width: 100%;
        height: auto;
        border-radius: 10px;
        transition: transform 0.3s ease;
    }
    
    .gallery-image img:hover {
        transform: scale(1.05);
    }
    
    #radio1:checked ~ #image1,
    #radio2:checked ~ #image2,
    #radio3:checked ~ #image3 {
        display: block;
    }
    
    .btn {
        display: inline-block;
        padding: 10px 20px;
        margin: 10px;
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        color: white;
        border: none;
        border-radius: 25px;
        cursor: pointer;
        text-decoration: none;
        transition: all 0.7s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-shadow: 0 1px 1px rgba(0, 0, 0, 0.2);
        font-weight: bold;
    }
    
    .btn:hover, .btn:focus {
        background: linear-gradient(135deg, #5b7de2, #8561c5);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    .btn:active {
        transform: translateY(1px);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
</style>

<h1 class="title">
  <span>Anime Detailer XL LoRA</span>
</h1>

<div class="gallery-container">
    <input type="radio" name="gallery" id="radio1" class="gallery-radio" aria-label="Less Detail">
    <input type="radio" name="gallery" id="radio2" class="gallery-radio" checked aria-label="Normal">
    <input type="radio" name="gallery" id="radio3" class="gallery-radio" aria-label="More Detail">
    <label for="radio1" class="btn">Less Detail</label>
    <label for="radio2" class="btn">Normal</label>
    <label for="radio3" class="btn">More Detail</label>
    <!-- Image Gallery -->
    <div id="image1" class="gallery-image">
        <img src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/RFtKV5Q6-8pWRzUA7AjOw.png" alt="sample1" loading="lazy">
    </div>
    <div id="image2" class="gallery-image">
        <img src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/8_Z2IYeTOYJAMuFyJBRwX.png" alt="sample2" loading="lazy">
    </div>
    <div id="image3" class="gallery-image">
        <img src="https://cdn-uploads.huggingface.co/production/uploads/6365c8dbf31ef76df4042821/0CyCkmFrWjPaBNLAwKMq8.png" alt="sample3" loading="lazy">
    </div>
</div>


## Overview

**Anime Detailer XL LoRA** is a cutting-edge LoRA adapter designed to work alongside Animagine XL 2.0. This unique model specializes in concept modulation, enabling users to adjust the level of detail in generated anime-style images. By manipulating a concept slider, users can create images ranging from highly detailed to more abstract representations.

<hr>

## Model Details

- **Developed by:** [Linaqruf](https://github.com/Linaqruf)
- **Model type:** LoRA adapter for Stable Diffusion XL
- **Model Description:** This adapter is a concept slider, allowing users to control the level of detail in anime-themed images. The closer the slider is set to 2, the more detailed the result; closer to -2, the less detailed. It is a versatile tool for artists and creators seeking various artistic expressions within anime imagery.
- **License:** [CreativeML Open RAIL++-M License](https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/LICENSE-MODEL)
- **Finetuned from model:** [Animagine XL 2.0](https://huggingface.co/Linaqruf/animagine-xl-2.0)

<hr>

## 🧨 Diffusers Installation

Ensure the installation of the latest `diffusers` library, along with other essential packages:

```bash
pip install diffusers --upgrade
pip install transformers accelerate safetensors
```

The following Python script demonstrates how to utilize the LoRA with Animagine XL 2.0. The default scheduler is EulerAncestralDiscreteScheduler, but it can be explicitly defined for clarity.

```py
import torch
from diffusers import (
    StableDiffusionXLPipeline, 
    EulerAncestralDiscreteScheduler,
    AutoencoderKL
)

# Initialize LoRA model and weights
lora_model_id = "Linaqruf/anime-detailer-xl-lora"
lora_filename = "anime-detailer-xl.safetensors"
lora_scale_slider = 2 # -2 for less detailed result

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
pipe.fuse_lora(lora_scale=lora_scale_slider)

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

## Acknowledgements

Our project has been enriched by the following significant works:

- **[Erasing Concepts from Diffusion Models](https://github.com/rohitgandikota/erasing)** by Rohit Gandikota et al.
- **[LECO](https://github.com/p1atdev/LECO)** by p1atdev. 
- **[AI Toolkit](https://github.com/ostris/ai-toolkit)** by Ostris. 


