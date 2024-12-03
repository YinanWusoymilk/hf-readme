---
license: mit
library_name: diffusers
---

# Ostris VAE - KL-f8-d16

A 16 channel VAE with 8x downsample. Trained from scratch on a balance of photos, artistic, text, cartoons, vector images. 

It is lighter weight that most VAEs with only 57,266,643 parameters (vs SD3 VAE: 83,819,683) which means it is faster and uses less VRAM yet scores quite similarly
on real images. Plus it is MIT licensed so you can do whatever you want with it.

| VAE|PSNR (higher better)| LPIPS (lower better) | # params |
|----|----|----|----|
| sd-vae-ft-mse|26.939|0.0581|83,653,863|
| SDXL|27.370|0.0540|83,653,863|
| SD3|31.681|0.0187|83,819,683|
| **Ostris KL-f8-d16** |**31.166**|**0.0198**|**57,266,643**|

### Compare
Check out the comparison at [imgsli](https://imgsli.com/Mjc2MjA3).

### Use with SD1.5 (Diffusers)
```py
import torch
from diffusers import AutoencoderKL, StableDiffusionPipeline
from huggingface_hub import hf_hub_download
from safetensors.torch import load_file

model_id = "runwayml/stable-diffusion-v1-5"
decoder_id = "ostris/vae-kl-f8-d16"
adapter_id = "ostris/16ch-VAE-Adapters"
adapter_ckpt = "16ch-VAE-Adapter-SD15-alpha.safetensors"
dtype = torch.float16

vae = AutoencoderKL.from_pretrained(decoder_id, torch_dtype=dtype)
pipe = StableDiffusionPipeline.from_pretrained(model_id, vae=vae, torch_dtype=torch.float16)

ckpt_file = hf_hub_download(adapter_id, adapter_ckpt)
ckpt = load_file(ckpt_file)

lora_state_dict = {k: v for k, v in ckpt.items() if "lora" in k}
unet_state_dict = {k.replace("unet_", ""): v for k, v in ckpt.items() if "unet_" in k}

pipe.unet.conv_in = torch.nn.Conv2d(16, 320, 3, 1, 1)
pipe.unet.conv_out = torch.nn.Conv2d(320, 16, 3, 1, 1)
pipe.unet.load_state_dict(unet_state_dict, strict=False)
pipe.unet.conv_in.to(dtype)
pipe.unet.conv_out.to(dtype)
pipe.unet.config.in_channels = 16
pipe.unet.config.out_channels = 16

pipe.load_lora_weights(lora_state_dict)
pipe.fuse_lora()

pipe = pipe.to("cuda")
prompt = "a photo of an astronaut riding a horse on mars"
negative_prompt = (
    "ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame,"
    "extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature,"
    "cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face"
)
image = pipe(prompt, negative_prompt=negative_prompt).images[0]

image.save("astronaut_rides_horse.png")
```

### What do I do with this?

If you don't know, you probably don't need this. This is made as an open source lighter version of a 16ch vae. 
You would need to train it into a network before it is useful. I plan to do this myself for SD 1.5, SDXL, and possibly pixart. 
[Follow me on Twitter](https://x.com/ostrisai) to keep up with my work on that. 

### Note: Not SD3 compatable
This VAE is not SD3 compatable as it is trained from scratch and has an entirely different latent space.