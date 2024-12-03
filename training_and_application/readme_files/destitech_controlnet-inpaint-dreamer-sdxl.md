---
license: openrail
tags:
- art
- controlnet
- stable-diffusion
- stable-diffusion-xl
- image-to-image
---
# Controlnet - Inpainting dreamer

This ControlNet has been conditioned on **Inpainting** and **Outpainting**.

**It is an early alpha version made by experimenting in order to learn more about controlnet.**

**You want to support this kind of work and the development of this model ? Feel free to [buy me a coffee](https://www.buymeacoffee.com/destitech) !**

It is designed to work with [Stable Diffusion XL](https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/stable_diffusion_xl). It should work with any model based on it.

**The image to inpaint or outpaint is to be used as input of the controlnet in a txt2img pipeline with denoising set to 1.0. The part to in/outpaint should be colors in solid white.**

Depending on the prompts, the rest of the image might be kept as is or modified more or less.

## Model Details
- **Developed by:** [Destitech](https://destitech.com)
- **Model type:** Controlnet
- **License:** [The CreativeML OpenRAIL M license](https://huggingface.co/spaces/CompVis/stable-diffusion-license) is an [Open RAIL M license](https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses), adapted from the work that [BigScience](https://bigscience.huggingface.co/) and [the RAIL Initiative](https://www.licenses.ai/) are jointly carrying in the area of responsible AI licensing. See also [the article about the BLOOM Open RAIL license](https://bigscience.huggingface.co/blog/the-bigscience-rail-license) on which our license is based.

## Released Checkpoints

[Model link](./models/diffusion_pytorch_model.safetensors)
[Model link - fp16 version - Built by OzzyGT](./models/diffusion_pytorch_model.safetensors)

## Usage with Diffusers

OzzyGT made a really good guide on how to use this model for outpainting, give it a try [Here](https://github.com/huggingface/diffusers/discussions/7482) !

A big thank you to him for pointing me out how to name the files for diffusers compatibility and for the fp16 version, you should be able to use it this way with both normal and fp16 version:

```python
from diffusers import ControlNetModel
import torch

controlnet = ControlNetModel.from_pretrained(
    "destitech/controlnet-inpaint-dreamer-sdxl", torch_dtype=torch.float16, variant="fp16"
)
```

## Usage with ComfyUI

[Workflow link](./workflows/workflow.json)

<a href="./workflows/workflow-preview.png"><img  style="margin:0;padding:0;" src="./workflows/workflow-preview.png"/></a>
<br/>
<a href="./workflows/masked.png"><img width="256" style="margin:0;padding:0;" src="./workflows/masked.png"/></a>
<a href="./workflows/output_cyberpunk_manor.png"><img width="256" style="margin:0;padding:0;" src="./workflows/output_cyberpunk_manor.png"/></a>
<a href="./workflows/output_casual_woman.png"><img width="256" style="margin:0;padding:0;" src="./workflows/output_casual_woman.png"/></a>

## More examples

<a href="./tests/test1.jpeg"><img width="768" style="margin:0;padding:0;" src="./tests/test1-thumb.jpeg"/></a>
<br/>
<a href="./tests/test2.jpeg"><img width="768" style="margin:0;padding:0;" src="./tests/test2-thumb.jpeg"/></a>

