---
license: creativeml-openrail-m
library_name: diffusers
pipeline_tag: text-to-image
base_model: stabilityai/stable-diffusion-xl-base-1.0
tags:
- safetensors
- stable-diffusion
- sdxl
- flash
- sdxl-flash
- lightning
- turbo
- lcm
- hyper
- fast
- fast-sdxl
- sd-community
inference:
  parameters:
    num_inference_steps: 7
    guidance_scale: 3
    negative_prompt: >-
      (deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong
      anatomy, extra limb, missing limb, floating limbs, (mutated hands and
      fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting,
      blurry, amputation
---

# **SDXL Flash** *in collaboration with [Project Fluently](https://hf.co/fluently)*

![preview](images/preview.png)

Introducing the new fast model SDXL Flash, we learned that all fast XL models work fast, but the quality decreases, and we also made a fast model, but it is not as fast as LCM, Turbo, Lightning and Hyper, but the quality is higher. Below you will see the study with steps and cfg.

### Steps and CFG (Guidance)

![steps_and_cfg_grid_test](images/steps_cfg_grid.png)

### Optimal settings
- **Steps**: 6-9
- **CFG Scale**: 2.5-3.5
- **Sampler**: DPM++ SDE

### Diffusers usage

```bash
pip install torch diffusers
```

```py
import torch
from diffusers import StableDiffusionXLPipeline, DPMSolverSinglestepScheduler

# Load model.
pipe = StableDiffusionXLPipeline.from_pretrained("sd-community/sdxl-flash", torch_dtype=torch.float16).to("cuda")

# Ensure sampler uses "trailing" timesteps.
pipe.scheduler = DPMSolverSinglestepScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")

# Image generation.
pipe("a happy dog, sunny day, realism", num_inference_steps=7, guidance_scale=3).images[0].save("output.png")
```
