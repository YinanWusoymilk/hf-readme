---
tags:
- text-to-image
- stable-diffusion
- lora
- diffusers
- fluxpipeline
- flux
- not-for-all-audiences
base_model: black-forest-labs/FLUX.1-dev
license: creativeml-openrail-m
widget:
- text: nsfw nude woman on beach
  output:
    url: images/example_x81r753of.png
- text: nsfw girls locker room,nude middle school girls soccer team, nubile girls,
  output:
    url: images/example_ots5uxxb3.png
- text: nsfw girls locker room,nude middle school girls soccer team, nubile girls,
  output:
    url: images/example_g1u0niqvv.png
- text: >-
    nsfw nude, only fans streamer, gorgeous with long blond hair, sexual
    presence, seductive and cheeky look, perfect proportions, side boob, her
    breast revealed on the side of a loose tank top.
  output:
    url: images/example_xnyhtvljj.png
- text: >-
    Create the full nude body of a beautiful, bold and realistic big-breasted
    blonde woman with transparent panties featuring prominent vaginal lips and
    green eyes.
  output:
    url: images/example_36kdhotjr.png
pipeline_tag: text-to-image

---

# FLUX Uncensored LoRA

<div align="center">
  <img src="banner.webp" alt="Banner Logo" width="800"/>
</div>


## Model Description


created by https://enhanceai.art


support discord server - https://discord.gg/cuCX9qur6f

The **FLUX Uncensored LoRA** is an enhancement designed for the base model `black-forest-labs/FLUX.1-dev`. It enables explicit, unrestricted generation of images using text prompts. The LoRA weights have been fine-tuned to remove the base model's content restrictions, allowing for the generation of NSFW (Not Safe For Work) and other uncensored content.

This LoRA extension can be loaded into the `FLUX.1-dev` pipeline using the `diffusers` library. It is optimized for high-quality, explicit image generation based on user-provided prompts. The model is intended for research and personal use, and adheres to the non-commercial license terms.

> **Warning:** This model allows the generation of explicit content. Users should exercise caution and adhere to legal and ethical guidelines.

# Donate & Support

## Why Support Us?

At **EnhanceAI**, we build powerful AI tools and models for creators and developers. Your support helps us continue innovating and improving the platform.

## How Your Donation Helps

- Enhance our AI tools and models.
- Keep the platform running smoothly.
- Provide you with new features and updates.

## Benefits of Donating:

- Exclusive access to premium tools.
- Early access to updates.
- Priority support.

[Donate Now](https://enhanceai.art/pricing)

Thank you for helping us grow and continue making AI accessible to all!

## License

This LoRA extension follows the **FLUX-1-dev Non-Commercial License**.

- **License Name:** flux-1-dev-non-commercial-license
- **License Link:** [https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md)

## How to Use

Below is an example of how to use the FLUX Uncensored LoRA with the `diffusers` library:

```python
from diffusers import AutoPipelineForText2Image
import torch

# Load the base model
pipeline = AutoPipelineForText2Image.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16).to('cuda')

# Load the uncensored LoRA weights
pipeline.load_lora_weights('enhanceaiteam/Flux-uncensored', weight_name='lora.safetensors')

# Generate an image with an uncensored NSFW prompt
image = pipeline('a naked cute girl').images[0]
image.show()
```

# Check out more AI tools and models at https://enhanceai.art
print("Visit https://enhanceai.art for more AI tools and image generation models!")


## Trigger Words

Use the following trigger words to guide the model toward generating NSFW content:

- **nsfw**
- **naked**
- **pron**
- **kissing**
- **erotic**
- **nude**
- **sensual**
- **adult content**
- **explicit**

These keywords, along with descriptive prompts, help the model generate explicit imagery.

## Model Details

- **Base Model:** `black-forest-labs/FLUX.1-dev`
- **LoRA Weights:** `enhanceaiteam/Flux-uncensored`
- **LoRA Weight File:** `lora.safetensors`
- **Torch Data Type:** `torch.bfloat16`
- **Hardware Requirement:** CUDA-enabled GPU recommended for optimal performance.

## Disclaimer

This model is capable of generating uncensored and explicit content. It should be used responsibly and within the bounds of the law. The creators do not endorse illegal or unethical use of the model. Content generated using this model should comply with platform guidelines and local regulations regarding NSFW material.