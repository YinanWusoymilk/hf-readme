---
license: mit
---

# 🍰 Tiny AutoEncoder for Stable Diffusion (XL)

[TAESDXL](https://github.com/madebyollin/taesd) is very tiny autoencoder which uses the same "latent API" as [SDXL-VAE](https://huggingface.co/stabilityai/sdxl-vae).
TAESDXL is useful for [real-time previewing](https://twitter.com/madebyollin/status/1679356448655163394) of the SDXL generation process.

Comparison on my laptop:

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/630447d40547362a22a969a2/9iMkNdI1B9AC6vEpQTfTl.jpeg)

This repo contains `.safetensors` versions of the TAESDXL weights.

For SD1.x / SD2.x, use [TAESD](https://huggingface.co/madebyollin/taesd/) instead (the SD and SDXL VAEs are [incompatible](https://huggingface.co/madebyollin/sdxl-vae-fp16-fix/discussions/6#64b8a9c13707b7d603c6ac16)).

## Using in 🧨 diffusers

```python
import torch
from diffusers import DiffusionPipeline, AutoencoderTiny

pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16
)
pipe.vae = AutoencoderTiny.from_pretrained("madebyollin/taesdxl", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "slice of delicious New York-style berry cheesecake"
image = pipe(prompt, num_inference_steps=25).images[0]
image.save("cheesecake_sdxl.png")
```