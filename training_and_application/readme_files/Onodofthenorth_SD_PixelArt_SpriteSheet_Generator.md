---
license: apache-2.0
language:
- en
pipeline_tag: text-to-image
tags:
- spritesheet
- text-to-image 
---
This Stable diffusion checkpoint allows you to generate pixel art sprite sheets from four different angles.
These first images are my results after merging this model with another model trained on my wife. merging another model with this one is the easiest way to get a consistent character with each view. still requires a bit of playing around with settings in img2img to get them how you want. for left and right, I suggest picking your best result and mirroring. after you are satisfied take your photo into photoshop or Krita, remove the background, and scale to the desired size. after this you can scale back up to display your results; this also clears up some of the color murkiness in the initial outputs.
![final sheet.png](https://s3.amazonaws.com/moonup/production/uploads/1667278292305-63028bc42db53f7d9f38dadb.png)

### 🧨 Diffusers

This model can be used just like any other Stable Diffusion model. For more information,
please have a look at the [Stable Diffusion](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion).

You can also export the model to [ONNX](https://huggingface.co/docs/diffusers/optimization/onnx), [MPS](https://huggingface.co/docs/diffusers/optimization/mps) and/or [FLAX/JAX]().

```python
#!pip install diffusers transformers scipy torch
from diffusers import StableDiffusionPipeline
import torch
model_id = "Onodofthenorth/SD_PixelArt_SpriteSheet_Generator"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
prompt = "PixelartLSS"
image = pipe(prompt).images[0]
image.save("./pixel.png")
```
___
___
For the front view use "PixelartFSS"
![Layer-0.png](https://s3.amazonaws.com/moonup/production/uploads/1667278301151-63028bc42db53f7d9f38dadb.png)
___
___
For the right view use "PixelartRSS"
![tmpjn2e6lle-001.png](https://s3.amazonaws.com/moonup/production/uploads/1667278489924-63028bc42db53f7d9f38dadb.png)
___
___
For the back view use "PixelartBSS"
![tmpxowqvkbj-001.png](https://s3.amazonaws.com/moonup/production/uploads/1667278497366-63028bc42db53f7d9f38dadb.png)
___
___
For the left view use "PixelartLSS"
![Left-001.png](https://s3.amazonaws.com/moonup/production/uploads/1667278508076-63028bc42db53f7d9f38dadb.png)
___
___
These are random results from the unmerged model 
![pixel art full.png](https://s3.amazonaws.com/moonup/production/uploads/1667278579019-63028bc42db53f7d9f38dadb.png)
___
___
here's a result from a merge with my Hermione model
![00711-1613350423-PixelartFSS, hermione.png](https://s3.amazonaws.com/moonup/production/uploads/1667278700840-63028bc42db53f7d9f38dadb.png)
___
___
here's a result from a merge with my cat girl model
![00675-557755173-(catgirl) PixelartLSS.png](https://s3.amazonaws.com/moonup/production/uploads/1667278670012-63028bc42db53f7d9f38dadb.png)