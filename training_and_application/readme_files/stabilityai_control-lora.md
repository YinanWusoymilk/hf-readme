---
tags:
- text-to-image
- stable-diffusion
license: other
language:
- en
---

# Control-LoRA Model Card


## Introduction
By adding low-rank parameter efficient fine tuning to ControlNet, we introduce ***Control-LoRAs***. This approach offers a more efficient and compact method to bring model control to a wider variety of consumer GPUs.

For each model below, you'll find:

- *Rank 256* files (reducing the original `4.7GB` ControlNet models down to `~738MB` Control-LoRA models) and experimental
- *Rank 128* files (reducing to model down to `~377MB`)

Each Control-LoRA has been trained on a diverse range of image concepts and aspect ratios.

### MiDaS and ClipDrop Depth
![canny](samples/depth-sample.jpeg)

This Control-LoRA utilizes a grayscale depth map for guided generation.

Depth estimation is an image processing technique that determines the distance of objects in a scene, providing a depth map that highlights variations in proximity.

The model was trained on the depth results of `MiDaS dpt_beit_large_512`.

It was further finetuned on the `Portrait Depth Estimation` model available in the [ClipDrop API by Stability AI](https://clipdrop.co/apis/docs/portrait-depth-estimation).

### Canny Edge
![canny](samples/canny-sample.jpeg)
Canny Edge Detection is an image processing technique that identifies abrupt changes in intensity to highlight edges in an image.

This Control-LoRA uses the edges from an image to generate the final image.

### Photograph and Sketch Colorizer
![photograph colorizer](samples/colorizer-sample.jpeg)
These two Control-LoRAs can be used to colorize images.

*Recolor* is designed to colorize black and white photographs.

*Sketch* is designed to color in drawings input as a white-on-black image (either hand-drawn, or created with a `pidi` edge model).

### Revision
![photograph colorizer](samples/revision-sample.jpeg)
Revision is a novel approach of using images to prompt SDXL.

It uses pooled CLIP embeddings to produce images conceptually similar to the input. It can be used either in addition, or to replace text prompts.

Revision also includes a blending function for combining multiple image or text concepts, as either positive or negative prompts.


## Inference

Control-LoRAs have been implemented into [ComfyUI](https://github.com/comfyanonymous/ComfyUI) and [StableSwarmUI](https://github.com/Stability-AI/StableSwarmUI)

Basic ComfyUI workflows (using the base model only) are available in this HF repo. Custom nodes from Stability are [available here](https://github.com/Stability-AI/stability-ComfyUI-nodes).

**Recolor example on ComfyUI:** ![comfyui recolor](samples/comfyui-recolor-example.jpeg)

**Canny edge on StableSwarmUI:** ![swarmui recolor](samples/swarmui-canny-example.jpeg)