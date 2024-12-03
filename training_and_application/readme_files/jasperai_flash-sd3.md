---
license: cc-by-nc-4.0
library_name: diffusers
base_model: stabilityai/stable-diffusion-3-medium
tags:
- lora
- text-to-image
inference: False
---
# ⚡ Flash Diffusion: FlashSD3 ⚡


Flash Diffusion is a diffusion distillation method proposed in [Flash Diffusion: Accelerating Any Conditional
Diffusion Model for Few Steps Image Generation](http://arxiv.org/abs/2406.02347) *by Clément Chadebec, Onur Tasar, Eyal Benaroche, and Benjamin Aubin* from Jasper Research.
This model is a **90.4M** LoRA distilled version of [SD3](https://huggingface.co/stabilityai/stable-diffusion-3-medium) model that is able to generate 1024x1024 images in **4 steps**.
See our [live demo](https://huggingface.co/spaces/jasperai/flash-sd3) and official [Github repo](https://github.com/gojasper/flash-diffusion).


<p align="center">
   <img style="width:700px;" src="assets/flash_sd3.png">
</p>

# How to use?

The model can be used using the `StableDiffusion3Pipeline` from `diffusers` library directly. It can allow reducing the number of required sampling steps to **4 steps**.

⚠️ First, you need to install a specific version of `diffusers` by running ⚠️

```bash
pip install git+https://github.com/initml/diffusers.git@clement/feature/flash_sd3
```

 Then, you can run the following to generate an image

```python
import torch
from diffusers import StableDiffusion3Pipeline, SD3Transformer2DModel, FlashFlowMatchEulerDiscreteScheduler
from peft import PeftModel

# Load LoRA
transformer = SD3Transformer2DModel.from_pretrained(
    "stabilityai/stable-diffusion-3-medium-diffusers",
    subfolder="transformer",
    torch_dtype=torch.float16,
)
transformer = PeftModel.from_pretrained(transformer, "jasperai/flash-sd3")


# Pipeline
pipe = StableDiffusion3Pipeline.from_pretrained(
    "stabilityai/stable-diffusion-3-medium-diffusers",
    transformer=transformer,
    torch_dtype=torch.float16,
    text_encoder_3=None,
    tokenizer_3=None
)

# Scheduler
pipe.scheduler = FlashFlowMatchEulerDiscreteScheduler.from_pretrained(
  "stabilityai/stable-diffusion-3-medium-diffusers",
  subfolder="scheduler",
)

pipe.to("cuda")

prompt = "A raccoon trapped inside a glass jar full of colorful candies, the background is steamy with vivid colors."

image = pipe(prompt, num_inference_steps=4, guidance_scale=0).images[0]
```
<p align="center">
   <img style="width:400px;" src="assets/raccoon.png">
</p>


## Training details
The model was trained for ~50 hours on 2 H100 GPUs.

💡 Training Hint : Model could perform much better on text if distilled on dataset of images containing text, feel free to try it yourself.


## Citation
If you find this work useful or use it in your research, please consider citing us

```bibtex
@misc{chadebec2024flash,
      title={Flash Diffusion: Accelerating Any Conditional Diffusion Model for Few Steps Image Generation}, 
      author={Clement Chadebec and Onur Tasar and Eyal Benaroche and Benjamin Aubin},
      year={2024},
      eprint={2406.02347},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## License
This model is released under the the Creative Commons BY-NC license.