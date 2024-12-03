---
license: mit
library_name: diffusers
pipeline_tag: text-to-image
---

# Mann-E Dreams

<p align="center">
  <img src="./collage.png" width=512 height=512 />
</p>

## Description

This is the newest SDXL based model from [Mann-E](https://mann-e.com) platform, which is a generative AI startup based in Iran. This model used thousands of midjourney generated images in order to make it possible to make high-quality images. Also, we've used a lot of tricks in order to make it possible to make the model as fast as SDXL Turbo or any other model which claims to be fast. 

The model has been mostly developed by Founder and CEO of Mann-E, [Muhammadreza Haghiri](https://haghiri75.com/en) and a team of four. We spent months on collecting the data, labeling them and training this model. The model is _mostly uncensored_ and tested with Automatic1111. 

## Model Settings

- CLIP Skip: 1 or 2 are both fine. 1 gives better results.
- Steps: 6-10. Usually 8 is perfect.
- CFG Scale: 2-4.
- Scale: 768x768 and 832x832 are just fine. Higher isn't tested. For 16:9 just try 1080x608
- Sampler : DPM++ SDE Karras

## Use it with diffusers

```py
from diffusers import DiffusionPipeline, DPMSolverSinglestepScheduler
import torch

pipe = DiffusionPipeline.from_pretrained(
    "mann-e/Mann-E_Dreams", torch_dtype=torch.float16
).to("cuda")

#This is equivalent to DPM++ SDE Karras, as noted in https://huggingface.co/docs/diffusers/main/en/api/schedulers/overview
pipe.scheduler = DPMSolverSinglestepScheduler.from_config(pipe.scheduler.config, use_karras_sigmas=True)

image = pipe(
  prompt="a cat in a bustling middle eastern city",
  num_inference_steps=8,
  guidance_scale=3,
  width=768,
  height=768,
  clip_skip=1
).images[0]
image.save("a_cat.png")
```

## Additional Notes

- SDXL 1.0 LoRas are working just fine with the model.
- ControlNet, IPAdapter, InstantID are just fine. 

## Donations

- __Tron/USDT (TRC20)__ : `TPXpiWACUZXtUszDbpLeDYR75NQTwngD8o`
- __ETH (ERC20)__: `0x44e262f121b88bcb21caac3d353edd78c3717e08`