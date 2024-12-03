---
license: apache-2.0
tags:
- art
- pytorch
- super-resolution
pipeline_tag: image-to-image
---
# AuraSR-v2 
![aurasr example](https://storage.googleapis.com/falserverless/gallery/aurasr-animated.webp)

GAN-based Super-Resolution for upscaling generated images, a variation of the [GigaGAN](https://mingukkang.github.io/GigaGAN/) paper for image-conditioned upscaling. Torch implementation is based on the unofficial [lucidrains/gigagan-pytorch](https://github.com/lucidrains/gigagan-pytorch) repository.

## Usage

```bash
$ pip install aura-sr
```

```python
from aura_sr import AuraSR

aura_sr = AuraSR.from_pretrained("fal/AuraSR-v2")
```

```python
import requests
from io import BytesIO
from PIL import Image

def load_image_from_url(url):
    response = requests.get(url)
    image_data = BytesIO(response.content)
    return Image.open(image_data)

image = load_image_from_url("https://mingukkang.github.io/GigaGAN/static/images/iguana_output.jpg").resize((256, 256))
upscaled_image = aura_sr.upscale_4x_overlapped(image)
```