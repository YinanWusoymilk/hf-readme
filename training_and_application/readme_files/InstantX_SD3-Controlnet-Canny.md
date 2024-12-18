# SD3 Controlnet




| control image | weight=0.0 | weight=0.3 | weight=0.5 | weight=0.7 | weight=0.9 |
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img src="./canny.jpg" width = "400" /> | <img src="./demo_0.jpg" width = "400" /> | <img src="./demo_3.jpg" width = "400" /> | <img src="./demo_5.jpg" width = "400" /> | <img src="./demo_7.jpg" width = "400" /> | <img src="./demo_9.jpg" width = "400" /> |



**Please ensure that the version of diffusers >= 0.30.0.dev0.**






# Demo
```python
import torch
from diffusers import StableDiffusion3ControlNetPipeline
from diffusers.models import SD3ControlNetModel, SD3MultiControlNetModel
from diffusers.utils import load_image

# load pipeline
controlnet = SD3ControlNetModel.from_pretrained("InstantX/SD3-Controlnet-Canny")
pipe = StableDiffusion3ControlNetPipeline.from_pretrained(
    "stabilityai/stable-diffusion-3-medium-diffusers",
    controlnet=controlnet
)
pipe.to("cuda", torch.float16)

# config
control_image = load_image("https://huggingface.co/InstantX/SD3-Controlnet-Canny/resolve/main/canny.jpg")
prompt = 'Anime style illustration of a girl wearing a suit. A moon in sky. In the background we see a big rain approaching. text "InstantX" on image'
n_prompt = 'NSFW, nude, naked, porn, ugly'
image = pipe(
    prompt, 
    negative_prompt=n_prompt, 
    control_image=control_image, 
    controlnet_conditioning_scale=0.5,
).images[0]
image.save('image.jpg')
```


## Limitation
Due to the fact that only 1024*1024 pixel resolution was used during the training phase, 
the inference performs best at this size, with other sizes yielding suboptimal results. 
We will initiate multi-resolution training in the future, and at that time, we will open-source the new weights.

