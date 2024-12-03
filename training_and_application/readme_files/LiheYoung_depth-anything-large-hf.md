---
license: apache-2.0
tags:
- vision
pipeline_tag: depth-estimation
widget:
- inference: false
---

# Depth Anything (large-sized model, Transformers version) 

Depth Anything model. It was introduced in the paper [Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](https://arxiv.org/abs/2401.10891) by Lihe Yang et al. and first released in [this repository](https://github.com/LiheYoung/Depth-Anything).

[Online demo](https://huggingface.co/spaces/LiheYoung/Depth-Anything) is also provided.

Disclaimer: The team releasing Depth Anything did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

Depth Anything leverages the [DPT](https://huggingface.co/docs/transformers/model_doc/dpt) architecture with a [DINOv2](https://huggingface.co/docs/transformers/model_doc/dinov2) backbone.

The model is trained on ~62 million images, obtaining state-of-the-art results for both relative and absolute depth estimation.

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/depth_anything_overview.jpg"
alt="drawing" width="600"/>

<small> Depth Anything overview. Taken from the <a href="https://arxiv.org/abs/2401.10891">original paper</a>.</small>

## Intended uses & limitations

You can use the raw model for tasks like zero-shot depth estimation. See the [model hub](https://huggingface.co/models?search=depth-anything) to look for
other versions on a task that interests you.

### How to use

Here is how to use this model to perform zero-shot depth estimation:

```python
from transformers import pipeline
from PIL import Image
import requests

# load pipe
pipe = pipeline(task="depth-estimation", model="LiheYoung/depth-anything-large-hf")

# load image
url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

# inference
depth = pipe(image)["depth"]
```

Alternatively, one can use the classes themselves:

```python
from transformers import AutoImageProcessor, AutoModelForDepthEstimation
import torch
import numpy as np
from PIL import Image
import requests

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

image_processor = AutoImageProcessor.from_pretrained("LiheYoung/depth-anything-large-hf")
model = AutoModelForDepthEstimation.from_pretrained("LiheYoung/depth-anything-large-hf")

# prepare image for the model
inputs = image_processor(images=image, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)
    predicted_depth = outputs.predicted_depth

# interpolate to original size
prediction = torch.nn.functional.interpolate(
    predicted_depth.unsqueeze(1),
    size=image.size[::-1],
    mode="bicubic",
    align_corners=False,
)
```
For more code examples, we refer to the [documentation](https://huggingface.co/transformers/main/model_doc/depth_anything.html#).


### BibTeX entry and citation info

```bibtex
@misc{yang2024depth,
      title={Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data}, 
      author={Lihe Yang and Bingyi Kang and Zilong Huang and Xiaogang Xu and Jiashi Feng and Hengshuang Zhao},
      year={2024},
      eprint={2401.10891},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```