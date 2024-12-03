---
license: other
pipeline_tag: text-to-image
tags:
- text-to-image
- turbo
- stable-diffusion
- stable-diffusion-xl
- dpo
widget:
  - text: 'rusty robot cartoon'
    output:
      url: dpo_turbo_robot.jpeg
inference:
  parameters:
    num_inference_steps: 8
---

## Merge of SDXL Turbo & SDXL DPO

<Gallery />

Read their licences before using it.

## `*.safetensors` for AUTOMATIC1111, ComfyUI, InvokeAI
[Download *.safetensors file](https://huggingface.co/thibaud/sdxl_dpo_turbo/resolve/main/sdxl_dpo_turbo.safetensors?download=true)

## Use it with 🧨 diffusers
```python
from diffusers import AutoPipelineForText2Image
import torch
        
pipeline = AutoPipelineForText2Image.from_pretrained('thibaud/sdxl_dpo_turbo', torch_dtype=torch.float16).to('cuda')        
image = pipeline('A mecha robot in a favela', num_inference_steps=2).images[0]
```