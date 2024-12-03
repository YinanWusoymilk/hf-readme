---
datasets:
- yuvalkirstain/pickapic_v2
language:
- en
library_name: diffusers
pipeline_tag: text-to-image
license: openrail++
---
# Diffusion Model Alignment Using Direct Preference Optimization

![row01](01.gif)

Direct Preference Optimization (DPO) for text-to-image diffusion models is a method to align diffusion models to text human preferences by directly optimizing on human comparison data. Please check our paper at [Diffusion Model Alignment Using Direct Preference Optimization](https://arxiv.org/abs/2311.12908).

This model is fine-tuned from [stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) on offline human preference data [pickapic_v2](https://huggingface.co/datasets/yuvalkirstain/pickapic_v2).

## Code
The code is available [here](https://github.com/huggingface/diffusers/tree/main/examples/research_projects/diffusion_dpo).

## SD1.5
We also have a model finedtuned from [stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) available at [dpo-sd1.5-text2image-v1](https://huggingface.co/mhdang/dpo-sd1.5-text2image-v1).

## A quick example
```python
from diffusers import StableDiffusionXLPipeline, UNet2DConditionModel
import torch

# load pipeline
model_id = "stabilityai/stable-diffusion-xl-base-1.0"
pipe = StableDiffusionXLPipeline.from_pretrained(model_id, torch_dtype=torch.float16, variant="fp16", use_safetensors=True).to("cuda")

# load finetuned model
unet_id = "mhdang/dpo-sdxl-text2image-v1"
unet = UNet2DConditionModel.from_pretrained(unet_id, subfolder="unet", torch_dtype=torch.float16)
pipe.unet = unet
pipe = pipe.to("cuda")

prompt = "Two cats playing chess on a tree branch"
image = pipe(prompt, guidance_scale=5).images[0].resize((512,512))
    
image.save("cats_playing_chess.png")
```

More details coming soon.