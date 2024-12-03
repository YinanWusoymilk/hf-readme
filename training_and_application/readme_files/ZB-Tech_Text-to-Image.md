---
license: openrail++
library_name: diffusers
tags:
- text-to-image
- diffusers-training
- diffusers
- lora
- template:sd-lora
- stable-diffusion-xl
- stable-diffusion-xl-diffusers
base_model: stabilityai/stable-diffusion-xl-base-1.0
instance_prompt: a photo of TOK dog
widget:
- text: Draw a picture of two female boxers fighting each other.
  output:
    url: images/example_9xsyd09gw.png
datasets:
- ZB-Tech/DreamXL
language:
- en

---

<!-- This model card has been generated automatically according to the information the training script had access to. You
should probably proofread and complete it, then remove this comment. -->


# SDXL LoRA Fine-tuning - ZB-Tech/Text-To-Image

<Gallery />

## Model description

These are ZB-Tech/Text-to-Image LoRA adaption weights for stabilityai/stable-diffusion-xl-base-1.0.

LoRA for the text encoder was enabled: False.

Special VAE used for training: madebyollin/sdxl-vae-fp16-fix.

##### How to use

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/ZB-Tech/Text-to-Image"
headers = {"Authorization": "Bearer HF_API_KEY"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "Astronaut riding a horse",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
```

## Download model

Weights for this model are available in Safetensors format.

[Download](suryasuri/Surya/tree/main) them in the Files & versions tab.