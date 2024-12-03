---
license: openrail++
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- controlnet
---

# Aesthetic ControlNet
This model can produce highly aesthetic results from an input image and a text prompt.

ControlNet is a method that can be used to condition diffusion models on arbitrary input features, such as image edges, segmentation maps, or human poses. 

Aesthetic ControlNet is a version of this technique that uses image features extracted using a [Canny edge detector](https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html) and guides a text-to-image diffusion model trained on a large aesthetic dataset.

The base diffusion model is a fine-tuned version of Stable Diffusion 2.1 trained at a resolution of 640x640, and the control network comes from [thibaud/controlnet-sd21](https://huggingface.co/thibaud/controlnet-sd21) by [@thibaudz](https://twitter.com/thibaudz).

For more information about ControlNet, please have a look at this [thread](https://twitter.com/krea_ai/status/1626672218477559809) or at the original [work](https://arxiv.org/pdf/2302.05543.pdf) by Lvmin Zhang and Maneesh Agrawala.

![Example](./examples.jpg)


### Diffusers
Install the following dependencies and then run the code below:

```bash
pip install opencv-python git+https://github.com/huggingface/diffusers.git
```


```py
import cv2
import numpy as np
from diffusers import StableDiffusionControlNetPipeline, EulerAncestralDiscreteScheduler
from diffusers.utils import load_image

image = load_image("https://huggingface.co/krea/aesthetic-controlnet/resolve/main/krea.jpg")

image = np.array(image)

low_threshold = 100
high_threshold = 200

image = cv2.Canny(image, low_threshold, high_threshold)
image = image[:, :, None]
image = np.concatenate([image, image, image], axis=2)
canny_image = Image.fromarray(image)

pipe = StableDiffusionControlNetPipeline.from_pretrained("krea/aesthetic-controlnet").to("cuda")
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

output = pipe(
    "fantasy flowers",
    canny_image,
    num_inference_steps=20,
    guidance_scale=4,
    width=768,
    height=768,
)

result = output.images[0]
result.save("result.png")
```

## Examples
![More examples](./more_examples.jpg)


## Misuse and Malicious Use
The model should not be used to intentionally create or disseminate images that create hostile or alienating environments for people. This includes generating images that people would foreseeably find disturbing, distressing, or offensive; or content that propagates historical or current stereotypes.

## Authors
Erwann Millon and Victor Perez