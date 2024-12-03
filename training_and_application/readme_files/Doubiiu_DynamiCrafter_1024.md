---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/model-cards
{}
---

# DynamiCrafter (576x1024) (text-)Image-to-Video/Image Animation Model Card
![row01](DynamiCrafter-1024-21.webp)
![row02](DynamiCrafter-10241.webp)
<!-- Provide a quick summary of what the model is/does. -->

DynamiCrafter (576x1024) (Text-)Image-to-Video is a video diffusion model that <br> takes in a still image as a conditioning image and text prompt describing dynamics,<br> and generates videos from it.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

DynamiCrafter, a (Text-)Image-to-Video/Image Animation approach, aims to generate <br>
short video clips (~2 seconds) from a conditioning image and text prompt.

This model was trained to generate 16 video frames at a resolution of 576x1024 <br>
given a context frame of the same resolution.


- **Developed by:** CUHK & Tencent AI Lab
- **Funded by:** CUHK & Tencent AI Lab
- **Model type:** Generative (text-)image-to-video model
- **Finetuned from model:** DynamiCrafter (320x512)

### Model Sources

<!-- Provide the basic links for the model. -->
For research purpose, we recommend our Github repository (https://github.com/Doubiiu/DynamiCrafter), <br>
which includes the detailed implementations.
- **Repository:** https://github.com/Doubiiu/DynamiCrafter
- **Paper:** https://arxiv.org/abs/2310.12190
- **Demo1:** https://huggingface.co/spaces/Doubiiu/DynamiCrafter
- **Demo2:** https://replicate.com/camenduru/dynami-crafter-576x1024
## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

<!-- ### Direct Use

We develop this repository for RESEARCH purposes, so it can only be used for personal/research/non-commercial purposes. -->



## Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
- The generated videos are relatively short (2 seconds, FPS=8).
- The model cannot render legible text.
- Faces and people in general may not be generated properly.
- The autoencoding part of the model is lossy, resulting in slight flickering artifacts.



## How to Get Started with the Model

Check out https://github.com/Doubiiu/DynamiCrafter

