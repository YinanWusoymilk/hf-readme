---
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/model-cards
{}
---

# ToonCrafter (512x320) Generative Cartoon Interpolation Model Card
![row01](ToonCrafter.webp)
<!-- Provide a quick summary of what the model is/does. -->

ToonCrafter (512x320) is a video diffusion model that <br> takes in two still images as conditioning images and text prompt describing dynamics,<br> and generates interpolation videos from them.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

ToonCrafter, a generative cartoon interpolation approach, aims to generate <br>
short video clips (~2 seconds) from two conditioning images (starting frame and ending frame) and text prompt.

This model was trained to generate 16 video frames at a resolution of 512x320 <br>
given a context frame of the same resolution.


- **Developed by:** CUHK & Tencent AI Lab
- **Funded by:** CUHK & Tencent AI Lab
- **Model type:** Video Diffusion Model
- **Finetuned from model:** DynamiCrafter-interpolation (512x320)

### Model Sources

<!-- Provide the basic links for the model. -->
For research purpose, we recommend our Github repository (https://github.com/ToonCrafter/ToonCrafter), <br>
which includes detailed implementations.
- **Repository:** https://github.com/ToonCrafter/ToonCrafter
- **Paper:** https://arxiv.org/abs/2405.17933
- **Project page:** https://doubiiu.github.io/projects/ToonCrafter/
- **Demo1:** https://huggingface.co/spaces/Doubiiu/tooncrafter
- **Demo2:** https://replicate.com/fofr/tooncrafter
## Uses

Feel free to use it under the Apache-2.0 license. Note that we don't have any official commercial product for ToonCrafter currently.
<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

<!-- ### Direct Use

We develop this repository for RESEARCH purposes, so it can only be used for personal/research/non-commercial purposes. -->



## Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
- The generated videos are relatively short (2 seconds, FPS=8).
- The model cannot render legible text.
- The autoencoding part of the model is lossy, resulting in slight flickering artifacts.



## How to Get Started with the Model

Check out https://github.com/ToonCrafter/ToonCrafter
