---
license: openrail
language:
- en
- ru
library_name: diffusers
pipeline_tag: text-to-image
tags:
- midjourney
- midjourney V6
- v6
- MJ
- mj
- kviai
- kvikontent
- text-to-image
- lora
base_model: runwayml/stable-diffusion-v1-5
widget:
- text: ed sheeran made of thnderstorm clouds, lights, thunder, rain, particles
  output:
    url: images/ed.png
- text: silhouette of a dog in the thunderstorm clouds, thumder, photo, bad weather,
  output:
    url: images/dog.png
- text: >-
    A professional photo of a beautiful night waterfall in the jungle with a
    touch of blue and a few fireflies flying around
  output:
    url: images/water.png
---

# Midjourney V6

Midjourney is most realistic and powerful ai image generator in the world. Here is is Stable Diffusion LoRA model trained on 100k+ midjourney V6 images.

## Examples

<Gallery />

## Usage

You can use this model using huggingface Interface API:
```Python
import requests

API_URL = "https://api-inference.huggingface.co/models/Kvikontent/midjourney-v6"
headers = {"Authorization": "Bearer HUGGINGFACE_API_TOKEN"}

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