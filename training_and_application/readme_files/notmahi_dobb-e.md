---
license: mit
library_name: timm
tags:
- robotics
- vision
pipeline_tag: robotics
---

<img style="max-width: 720px;" src=https://cdn-uploads.huggingface.co/production/uploads/630e567f8df86f1e5bf0d837/CISEAH0AbTJVDJuZWkqFK.jpeg></img>

# Dobb·E

[Project webpage](https://dobb-e.com) · [Documentation (gitbooks)](https://docs.dobb-e.com) · [Paper](https://arxiv.org/abs/2311.16098)

**Authors**: [Mahi Shafiullah*](https://mahis.life), [Anant Rai*](https://raianant.github.io/), [Haritheja Etukuru](https://haritheja.com/), [Yiqian Liu](https://www.linkedin.com/in/eva-liu-ba90a5209/), [Ishan Misra](https://imisra.github.io/), [Soumith Chintala](https://soumith.ch), [Lerrel Pinto](https://lerrelpinto.com)

Open-source repository of the Home Pretrained Representation (HPR) of [Dobb·E](https://dobb-e.com) and the associated paper, [On Bringing Robots Home](https://arxiv.org/abs/2311.16098)

<video autoplay muted style="max-width: 720px;" src="https://cdn-uploads.huggingface.co/production/uploads/630e567f8df86f1e5bf0d837/tmL48wY0F8eL2Mluizrw3.mp4"></video>

## What's on this repo

You can find our [Home Pretrained Models (HPR)](https://dobb-e.com/#models), which is a ResNet34 model trained on our dataset, [Homes of New York (HoNY)](https://dobb-e.com/#dataset), in this repo. You can download the weights if you want, or you can get started by using [Timm](https://huggingface.co/docs/timm/index).

```python
import timm

model = timm.create_model("hf_hub:notmahi/dobb-e", pretrained=True)
```

You can read more about it on our [paper](https://arxiv.org/abs/2311.16098) or our [website](https://dobb-e.com).

Let's bring some robots home!