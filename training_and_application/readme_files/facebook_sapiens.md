---
language:
- en
license: cc-by-nc-4.0
tags:
- sapiens
---

# Model Details

<!-- Provide a quick summary of what the model is/does. -->

Sapiens, a family of models for four fundamental human-centric vision tasks - 2D pose estimation, body-part segmentation, depth estimation, and surface normal prediction. 
Our models natively support 1K high-resolution inference and are extremely easy to adapt for individual tasks by simply fine-tuning models pretrained on over 300 million in-the-wild human images. 
The resulting models exhibit remarkable generalization to in-the-wild data, even when labeled data is scarce or entirely synthetic. 
Our simple model design also brings scalability - model performance across tasks improves as we scale the parameters from 0.3 to 2 billion. 
Sapiens consistently surpasses existing baselines across various human-centric benchmarks.


### Model Description
- **Developed by:** Meta
- **Model type:** Vision Transformers
- **License:** Creative Commons Attribution-NonCommercial 4.0


### More Resources
- **Repository:** [https://github.com/facebookresearch/sapiens](https://github.com/facebookresearch/sapiens)
- **Paper:** [https://arxiv.org/abs/2408.12569](https://arxiv.org/abs/2408.12569)
- **Demos:** [Sapiens Gradio Spaces](https://huggingface.co/collections/facebook/sapiens-66d22047daa6402d565cb2fc)
- **Project Page:** [https://about.meta.com/realitylabs/codecavatars/sapiens](https://about.meta.com/realitylabs/codecavatars/sapiens/)
- **Additional Results:** [https://rawalkhirodkar.github.io/sapiens](https://rawalkhirodkar.github.io/sapiens/)
- **HuggingFace Collection:** [https://huggingface.co/collections/facebook/sapiens-66d22047daa6402d565cb2fc](https://huggingface.co/collections/facebook/sapiens-66d22047daa6402d565cb2fc)

## Uses
- pose estimation (keypoints 17, keypoints 133, keypoints 308)
- body-part segmentation (28 classes)
- depth estimation
- surface normal estimation

## Model Zoo
**Note: This repository does not host any checkpoints but contains links to all the model repositories.**

We provide checkpoints in three formats:
- original: weights can be finetuned for your use case along with inference.
- torchscript: (inference only) weights ported to torchscript.
- bfloat16: (inference only) for large scale processing, weights ported to bfloat16 (A100 gpu only + pytorch-2.3).


| Model Name | Original | TorchScript | BFloat16 |
|:-----------|:--------:|:-----------:|:--------:|
| sapiens-pretrain-0.3b | [link](https://huggingface.co/facebook/sapiens-pretrain-0.3b) | [link](https://huggingface.co/facebook/sapiens-pretrain-0.3b-torchscript) | [link](https://huggingface.co/facebook/sapiens-pretrain-0.3b-bfloat16) |
| sapiens-pretrain-0.6b | [link](https://huggingface.co/facebook/sapiens-pretrain-0.6b) | [link](https://huggingface.co/facebook/sapiens-pretrain-0.6b-torchscript) | [link](https://huggingface.co/facebook/sapiens-pretrain-0.6b-bfloat16) |
| sapiens-pretrain-1b | [link](https://huggingface.co/facebook/sapiens-pretrain-1b) | [link](https://huggingface.co/facebook/sapiens-pretrain-1b-torchscript) | [link](https://huggingface.co/facebook/sapiens-pretrain-1b-bfloat16) |
| sapiens-pretrain-2b | [link](https://huggingface.co/facebook/sapiens-pretrain-2b) | [link](https://huggingface.co/facebook/sapiens-pretrain-2b-torchscript) | [link](https://huggingface.co/facebook/sapiens-pretrain-2b-bfloat16) |
<br>
| sapiens-pose-0.3b | [link](https://huggingface.co/facebook/sapiens-pose-0.3b) | [link](https://huggingface.co/facebook/sapiens-pose-0.3b-torchscript) | [link](https://huggingface.co/facebook/sapiens-pose-0.3b-bfloat16) |
| sapiens-pose-0.6b | [link](https://huggingface.co/facebook/sapiens-pose-0.6b) | [link](https://huggingface.co/facebook/sapiens-pose-0.6b-torchscript) | [link](https://huggingface.co/facebook/sapiens-pose-0.6b-bfloat16) |
| sapiens-pose-1b | [link](https://huggingface.co/facebook/sapiens-pose-1b) | [link](https://huggingface.co/facebook/sapiens-pose-1b-torchscript) | [link](https://huggingface.co/facebook/sapiens-pose-1b-bfloat16) |
<br>
| sapiens-seg-0.3b | [link](https://huggingface.co/facebook/sapiens-seg-0.3b) | [link](https://huggingface.co/facebook/sapiens-seg-0.3b-torchscript) | [link](https://huggingface.co/facebook/sapiens-seg-0.3b-bfloat16) |
| sapiens-seg-0.6b | [link](https://huggingface.co/facebook/sapiens-seg-0.6b) | [link](https://huggingface.co/facebook/sapiens-seg-0.6b-torchscript) | [link](https://huggingface.co/facebook/sapiens-seg-0.6b-bfloat16) |
| sapiens-seg-1b | [link](https://huggingface.co/facebook/sapiens-seg-1b) | [link](https://huggingface.co/facebook/sapiens-seg-1b-torchscript) | [link](https://huggingface.co/facebook/sapiens-seg-1b-bfloat16) |
<br>
| sapiens-depth-0.3b | [link](https://huggingface.co/facebook/sapiens-depth-0.3b) | [link](https://huggingface.co/facebook/sapiens-depth-0.3b-torchscript) | [link](https://huggingface.co/facebook/sapiens-depth-0.3b-bfloat16) |
| sapiens-depth-0.6b | [link](https://huggingface.co/facebook/sapiens-depth-0.6b) | [link](https://huggingface.co/facebook/sapiens-depth-0.6b-torchscript) | [link](https://huggingface.co/facebook/sapiens-depth-0.6b-bfloat16) |
| sapiens-depth-1b | [link](https://huggingface.co/facebook/sapiens-depth-1b) | [link](https://huggingface.co/facebook/sapiens-depth-1b-torchscript) | [link](https://huggingface.co/facebook/sapiens-depth-1b-bfloat16) |
| sapiens-depth-2b | [link](https://huggingface.co/facebook/sapiens-depth-2b) | [link](https://huggingface.co/facebook/sapiens-depth-2b-torchscript) | [link](https://huggingface.co/facebook/sapiens-depth-2b-bfloat16) |
<br>
| sapiens-normal-0.3b | [link](https://huggingface.co/facebook/sapiens-normal-0.3b) | [link](https://huggingface.co/facebook/sapiens-normal-0.3b-torchscript) | [link](https://huggingface.co/facebook/sapiens-normal-0.3b-bfloat16) |
| sapiens-normal-0.6b | [link](https://huggingface.co/facebook/sapiens-normal-0.6b) | [link](https://huggingface.co/facebook/sapiens-normal-0.6b-torchscript) | [link](https://huggingface.co/facebook/sapiens-normal-0.6b-bfloat16) |
| sapiens-normal-1b | [link](https://huggingface.co/facebook/sapiens-normal-1b) | [link](https://huggingface.co/facebook/sapiens-normal-1b-torchscript) | [link](https://huggingface.co/facebook/sapiens-normal-1b-bfloat16) |
| sapiens-normal-2b | [link](https://huggingface.co/facebook/sapiens-normal-2b) | [link](https://huggingface.co/facebook/sapiens-normal-2b-torchscript) | [link](https://huggingface.co/facebook/sapiens-normal-2b-bfloat16) |


Helper models for bounding box detection or background removal.
| Model Name | Original | TorchScript | BFloat16 |
|:-----------|:--------:|:-----------:|:--------:|
| sapiens-pose-bbox-detector | [link](https://huggingface.co/facebook/sapiens-pose-bbox-detector) | - | - |
| sapiens-seg-foreground-1b | - | [link](https://huggingface.co/facebook/sapiens-seg-foreground-1b-torchscript) | - |


Other finetuned models (pose-133 and pose-17): [here](https://huggingface.co/noahcao/sapiens-pose-coco/tree/main)
