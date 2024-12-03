---
license: mit
language:
- en
base_model:
- black-forest-labs/FLUX.1-dev
---

# Flux-dev-de-distill

This is an experiment to de-distill guidance from flux.1-dev. We removed the original distilled guidance and make true classifier-free guidance reworks.

## Model Details

Following Algorithm 1 in [On Distillation of Guided Diffusion Models](https://arxiv.org/abs/2210.03142), we attempted to reverse the distillation process by re-matching guidance scale w. we introduce a student model
x(zt) to match the output of the teacher at any time-step t ∈ [0, 1] and any guidance scale w ∈ [1, 4]. We initialize the student model with parameters from the teacher model except for the parameters related to w-embedding.

Since this model uses true CFG instead of distilled CFG, it is not compatible with diffusers pipeline. Please use [inference script](./inference.py) or manually add guidance in the iteration loop.

Train: 150K Unsplash images, 1024px square, 6k steps with global batch size 32, frozen teacher model, approx 12 hours due to limited compute.

Examples: Distilled CFG / True CFG

![](./example2.webp)
![](./example1.webp)