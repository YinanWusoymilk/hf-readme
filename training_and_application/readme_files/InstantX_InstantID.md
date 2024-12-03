---
license: apache-2.0
language:
- en
library_name: diffusers
pipeline_tag: text-to-image
---

# InstantID Model Card

<div align="center">

[**Project Page**](https://instantid.github.io/) **|** [**Paper**](https://arxiv.org/abs/2401.07519) **|** [**Code**](https://github.com/InstantID/InstantID) **|** [🤗 **Gradio demo**](https://huggingface.co/spaces/InstantX/InstantID)


</div>

## Introduction

InstantID is a new state-of-the-art tuning-free method to achieve ID-Preserving generation with only single image, supporting various downstream tasks.

<div  align="center">
<img src='examples/applications.png'>
</div>


## Usage

You can directly download the model in this repository.
You also can download the model in python script:

```python
from huggingface_hub import hf_hub_download
hf_hub_download(repo_id="InstantX/InstantID", filename="ControlNetModel/config.json", local_dir="./checkpoints")
hf_hub_download(repo_id="InstantX/InstantID", filename="ControlNetModel/diffusion_pytorch_model.safetensors", local_dir="./checkpoints")
hf_hub_download(repo_id="InstantX/InstantID", filename="ip-adapter.bin", local_dir="./checkpoints")
```

For face encoder, you need to manutally download via this [URL](https://github.com/deepinsight/insightface/issues/1896#issuecomment-1023867304) to `models/antelopev2`.

```python
# !pip install opencv-python transformers accelerate insightface
import diffusers
from diffusers.utils import load_image
from diffusers.models import ControlNetModel

import cv2
import torch
import numpy as np
from PIL import Image

from insightface.app import FaceAnalysis
from pipeline_stable_diffusion_xl_instantid import StableDiffusionXLInstantIDPipeline, draw_kps

# prepare 'antelopev2' under ./models
app = FaceAnalysis(name='antelopev2', root='./', providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

# prepare models under ./checkpoints
face_adapter = f'./checkpoints/ip-adapter.bin'
controlnet_path = f'./checkpoints/ControlNetModel'

# load IdentityNet
controlnet = ControlNetModel.from_pretrained(controlnet_path, torch_dtype=torch.float16)

pipe = StableDiffusionXLInstantIDPipeline.from_pretrained(
...     "stabilityai/stable-diffusion-xl-base-1.0", controlnet=controlnet, torch_dtype=torch.float16
... )
pipe.cuda()

# load adapter
pipe.load_ip_adapter_instantid(face_adapter)
```

Then, you can customized your own face images

```python
# load an image
image = load_image("your-example.jpg")

# prepare face emb
face_info = app.get(cv2.cvtColor(np.array(face_image), cv2.COLOR_RGB2BGR))
face_info = sorted(face_info, key=lambda x:(x['bbox'][2]-x['bbox'][0])*x['bbox'][3]-x['bbox'][1])[-1] # only use the maximum face
face_emb = face_info['embedding']
face_kps = draw_kps(face_image, face_info['kps'])

pipe.set_ip_adapter_scale(0.8)

prompt = "analog film photo of a man. faded film, desaturated, 35mm photo, grainy, vignette, vintage, Kodachrome, Lomography, stained, highly detailed, found footage, masterpiece, best quality"
negative_prompt = "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured (lowres, low quality, worst quality:1.2), (text:1.2), watermark, painting, drawing, illustration, glitch,deformed, mutated, cross-eyed, ugly, disfigured"

# generate image
image = pipe(
...     prompt, image_embeds=face_emb, image=face_kps, controlnet_conditioning_scale=0.8
... ).images[0]
```

For more details, please follow the instructions in our [GitHub repository](https://github.com/InstantID/InstantID). 

## Usage Tips
1. If you're not satisfied with the similarity, try to increase the weight of "IdentityNet Strength" and "Adapter Strength".
2. If you feel that the saturation is too high, first decrease the Adapter strength. If it is still too high, then decrease the IdentityNet strength.
3. If you find that text control is not as expected, decrease Adapter strength.
4. If you find that realistic style is not good enough, go for our Github repo and use a more realistic base model.

## Demos

<div  align="center">
<img src='examples/0.png'>
</div>

<div  align="center">
<img src='examples/1.png'>
</div>

## Disclaimer

This project is released under Apache License and aims to positively impact the field of AI-driven image generation. Users are granted the freedom to create images using this tool, but they are obligated to comply with local laws and utilize it responsibly. The developers will not assume any responsibility for potential misuse by users.

## Citation
```bibtex
@article{wang2024instantid,
  title={InstantID: Zero-shot Identity-Preserving Generation in Seconds},
  author={Wang, Qixun and Bai, Xu and Wang, Haofan and Qin, Zekui and Chen, Anthony},
  journal={arXiv preprint arXiv:2401.07519},
  year={2024}
}
```