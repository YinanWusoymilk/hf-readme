---
tags:
- stable-diffusion
- controlnet
license: openrail++
language:
- en
---
# QR Code Conditioned ControlNet Models for Stable Diffusion 1.5 and 2.1

![1](imgs/1.png)

## Model Description

These ControlNet models have been trained on a large dataset of 150,000 QR code + QR code artwork couples. They provide a solid foundation for generating QR code-based artwork that is aesthetically pleasing, while still maintaining the integral QR code shape.

The Stable Diffusion 2.1 version is marginally more effective, as it was developed to address my specific needs. However, a 1.5 version model was also trained on the same dataset for those who are using the older version.
Separate repos for usage in diffusers can be found here:<br>
1.5: https://huggingface.co/DionTimmer/controlnet_qrcode-control_v1p_sd15<br>
2.1: https://huggingface.co/DionTimmer/controlnet_qrcode-control_v11p_sd21<br>

## How to use with Diffusers


```bash
pip -q install diffusers transformers accelerate torch xformers
```

```python
import torch
from PIL import Image
from diffusers import StableDiffusionControlNetImg2ImgPipeline, ControlNetModel, DDIMScheduler
from diffusers.utils import load_image

controlnet = ControlNetModel.from_pretrained("DionTimmer/controlnet_qrcode-control_v1p_sd15",
                                             torch_dtype=torch.float16)

pipe = StableDiffusionControlNetImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    controlnet=controlnet,
    safety_checker=None,
    torch_dtype=torch.float16
)

pipe.enable_xformers_memory_efficient_attention()
pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()

def resize_for_condition_image(input_image: Image, resolution: int):
    input_image = input_image.convert("RGB")
    W, H = input_image.size
    k = float(resolution) / min(H, W)
    H *= k
    W *= k
    H = int(round(H / 64.0)) * 64
    W = int(round(W / 64.0)) * 64
    img = input_image.resize((W, H), resample=Image.LANCZOS)
    return img


# play with guidance_scale, controlnet_conditioning_scale and strength to make a valid QR Code Image

# qr code image
source_image = load_image("https://s3.amazonaws.com/moonup/production/uploads/6064e095abd8d3692e3e2ed6/A_RqHaAM6YHBodPLwqtjn.png")
# initial image, anything
init_image = load_image("https://s3.amazonaws.com/moonup/production/uploads/noauth/KfMBABpOwIuNolv1pe3qX.jpeg")
condition_image = resize_for_condition_image(source_image, 768)
init_image = resize_for_condition_image(init_image, 768)
generator = torch.manual_seed(123121231)
image = pipe(prompt="a bilboard in NYC with a qrcode",
             negative_prompt="ugly, disfigured, low quality, blurry, nsfw", 
             image=init_image,
             control_image=condition_image,
             width=768,
             height=768,
             guidance_scale=20,
             controlnet_conditioning_scale=1.5,
             generator=generator,
             strength=0.9, 
             num_inference_steps=150,
            )

image.images[0]

```

## Performance and Limitations

These models perform quite well in most cases, but please note that they are not 100% accurate. In some instances, the QR code shape might not come through as expected. You can increase the ControlNet weight to emphasize the QR code shape. However, be cautious as this might negatively impact the style of your output.**To optimize for scanning, please generate your QR codes with correction mode 'H' (30%).**

To balance between style and shape, a gentle fine-tuning of the control weight might be required based on the individual input and the desired output, aswell as the correct prompt. Some prompts do not work until you increase the weight by a lot. The process of finding the right balance between these factors is part art and part science. For the best results, it is recommended to generate your artwork at a resolution of 768. This allows for a higher level of detail in the final product, enhancing the quality and effectiveness of the QR code-based artwork.

## Installation

The simplest way to use this is to place the .safetensors model and its .yaml config file in the folder where your other controlnet models are installed, which varies per application. 
For usage in auto1111 they can be placed in the webui/models/ControlNet folder. They can be loaded using the controlnet webui extension which you can install through the extensions tab in the webui (https://github.com/Mikubill/sd-webui-controlnet). Make sure to enable your controlnet unit and set your input image as the QR code. Set the model to either the SD2.1 or 1.5 version depending on your base stable diffusion model, or it will error. No pre-processor is needed, though you can use the invert pre-processor for a different variation of results. 768 is the preferred resolution for generation since it allows for more detail.
Make sure to look up additional info on how to use controlnet if you get stuck, once you have the webui up and running its really easy to install the controlnet extension aswell.

![2](imgs/2.png) ![3](imgs/3.png) ![4](imgs/4.png)