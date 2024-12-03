---
license: apache-2.0
library_name: pytorch
tags:
- llava
license_name: yi-license
license_link: LICENSE
pipeline_tag: image-text-to-text
---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/01-ai/Yi/main/assets/img/Yi_logo_icon_dark.svg" width="200px">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/01-ai/Yi/main/assets/img/Yi_logo_icon_light.svg" width="200px"> 
  <img alt="specify theme context for images" src="https://raw.githubusercontent.com/01-ai/Yi/main/assets/img/Yi_logo_icon_light.svg" width="200px">
</picture>

</div>

<div align="center">
  <h1 align="center">Yi Vision Language Model</h1>
</div>


<div align="center">
  <h3 align="center">Better Bilingual Multimodal Model</h3>
</div>

<p align="center">
🤗 <a href="https://huggingface.co/01-ai" target="_blank">Hugging Face</a> • 🤖 <a href="https://www.modelscope.cn/organization/01ai/" target="_blank">ModelScope</a> • 🟣 <a href="https://wisemodel.cn/organization/01.AI" target="_blank">wisemodel</a>
</p> 

<p align="center">
    👩‍🚀 Ask questions or discuss ideas on <a href="https://github.com/01-ai/Yi/discussions" target="_blank"> GitHub </a>!
</p> 

<p align="center">
    👋 Join us 💬 <a href="https://github.com/01-ai/Yi/issues/43#issuecomment-1827285245" target="_blank"> WeChat (Chinese) </a>!
</p> 

<p align="center">
    📚 Grow at <a href="https://github.com/01-ai/Yi/blob/main/docs/learning_hub.md"> Yi Learning Hub </a>!
</p> 

<hr>

<!-- DO NOT REMOVE ME -->

<details open>
<summary></b>📕 Table of Contents</b></summary>

- [What is Yi-VL?](#what-is-yi-vl)
  - [Overview](#overview)
  - [Models](#models)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Training](#training)
  - [Limitations](#limitations)
- [Why Yi-VL?](#why-yi-vl)
  - [Tech report](#tech-report)
  - [Benchmarks](#benchmarks)
  - [Showcases](#showcases)
- [How to use Yi-VL?](#how-to-use-yi-vl)
  - [Quick start](#quick-start)
  - [Hardware requirements](#hardware-requirements)
- [Misc.](#misc)
  - [Acknowledgements and attributions](#acknowledgements-and-attributions)
    - [List of used open-source projects](#list-of-used-open-source-projects)
  - [License](#license)

</details>

<hr>

# What is Yi-VL?

## Overview

- **Yi Vision Language (Yi-VL)** model is the open-source, multimodal version of the Yi **Large Language Model (LLM)** series, enabling content comprehension, recognition, and multi-round conversations about images.
  
- Yi-VL demonstrates exceptional performance, **ranking first** among all existing open-source models in the latest benchmarks including [MMMU](https://mmmu-benchmark.github.io/#leaderboard) in English and [CMMMU](https://mmmu-benchmark.github.io/#leaderboard) in Chinese (based on data available up to January 2024).
  
- Yi-VL-34B is the **first** open-source 34B vision language model worldwide.

## Models

Yi-VL has released the following versions.

Model |       Download
|---|---
Yi-VL-34B |• [🤗 Hugging Face](https://huggingface.co/01-ai/Yi-VL-34B)  • [🤖 ModelScope](https://www.modelscope.cn/models/01ai/Yi-VL-34B/summary) • [🟣 wisemodel](https://wisemodel.cn/models/01.AI/Yi-VL-34B)
Yi-VL-6B | • [🤗 Hugging Face](https://huggingface.co/01-ai/Yi-VL-6B)  • [🤖 ModelScope](https://www.modelscope.cn/models/01ai/Yi-VL-6B/summary) • [🟣 wisemodel](https://wisemodel.cn/models/01.AI/Yi-VL-6B)

## Features

Yi-VL offers the following features:

- Multi-round text-image conversations: Yi-VL can take both text and images as inputs and produce text outputs. Currently, it supports multi-round visual question answering with one image.
  
- Bilingual text support: Yi-VL supports conversations in both English and Chinese, including text recognition in images.  
  
- Strong image comprehension: Yi-VL is adept at analyzing visuals, making it an efficient tool for tasks like extracting, organizing, and summarizing information from images.
  
- Fine-grained image resolution: Yi-VL supports image understanding at a higher resolution of 448&times;448.

## Architecture

Yi-VL adopts the [LLaVA](https://github.com/haotian-liu/LLaVA) architecture, which is composed of three primary components:

- Vision Transformer (ViT): it's initialized with [CLIP ViT-H/14 model](https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K) and used for image encoding.

- Projection Module: it's designed to align image features with text feature space, consisting of a two-layer Multilayer Perceptron (MLP) with layer normalizations.
  
- Large Language Model (LLM): it's initialized with [Yi-34B-Chat](https://huggingface.co/01-ai/Yi-34B-Chat) or [Yi-6B-Chat](https://huggingface.co/01-ai/Yi-6B-Chat), demonstrating exceptional proficiency in understanding and generating both English and Chinese. 

![image/png](https://cdn-uploads.huggingface.co/production/uploads/656d9adce8bf55919aca7c3f/EGVHSWG4kAcX01xDaoeXS.png)

## Training 

### Training process

Yi-VL is trained to align visual information well to the semantic space of Yi LLM, which undergoes a comprehensive three-stage training process:

- Stage 1: The parameters of ViT and the projection module are trained using an image resolution of 224&times;224. The LLM weights are frozen. The training leverages an image caption dataset comprising 100 million image-text pairs from [LAION-400M](https://laion.ai/blog/laion-400-open-dataset/). The primary objective is to enhance the ViT's knowledge acquisition within our specified architecture and to achieve better alignment between the ViT and the LLM. 
     
- Stage 2: The image resolution of ViT is scaled up to 448&times;448, and the parameters of ViT and the projection module are trained. It aims to further boost the model's capability for discerning intricate visual details. The dataset used in this stage includes about 25 million image-text pairs, such as [LAION-400M](https://laion.ai/blog/laion-400-open-dataset/), [CLLaVA](https://huggingface.co/datasets/LinkSoul/Chinese-LLaVA-Vision-Instructions), [LLaVAR](https://llavar.github.io/), [Flickr](https://www.kaggle.com/datasets/hsankesara/flickr-image-dataset), [VQAv2](https://paperswithcode.com/dataset/visual-question-answering-v2-0), [RefCOCO](https://github.com/lichengunc/refer/tree/master), [Visual7w](http://ai.stanford.edu/~yukez/visual7w/) and so on.
     
- Stage 3: The parameters of the entire model (that is, ViT, projection module, and LLM) are trained. The primary goal is to enhance the model's proficiency in multimodal chat interactions, thereby endowing it with the ability to seamlessly integrate and interpret visual and linguistic inputs. To this end, the training dataset encompasses a diverse range of sources, totalling approximately 1 million image-text pairs, including [GQA](https://cs.stanford.edu/people/dorarad/gqa/download.html), [VizWiz VQA](https://vizwiz.org/tasks-and-datasets/vqa/), [TextCaps](https://opendatalab.com/OpenDataLab/TextCaps), [OCR-VQA](https://ocr-vqa.github.io/), [Visual Genome](https://homes.cs.washington.edu/~ranjay/visualgenome/api.html), [LAION GPT4V](https://huggingface.co/datasets/laion/gpt4v-dataset) and so on. To ensure data balancing, we impose a cap on the maximum data contribution from any single source, restricting it to no more than 50,000 pairs. 

Below are the parameters configured for each stage.

Stage | Global batch size | Learning rate | Gradient clip | Epochs
|---|---|---|---|---
Stage 1, 2 |4096|1e-4|0.5|1
Stage 3|256|2e-5|1.0|2

### Training resource consumption

- The training consumes 128 NVIDIA A800 (80G) GPUs. 

- The total training time amounted to approximately 10 days for Yi-VL-34B and 3 days for Yi-VL-6B. 

## Limitations

This is the initial release of the Yi-VL, which comes with some known limitations. It is recommended to carefully evaluate potential risks before adopting any models. 

- Feature limitation
  
    - Visual question answering is supported. Other features like text-to-3D and image-to-video are not yet supported.
    
    - A single image rather than several images can be accepted as an input. 
 
- Hallucination problem
  
    - There is a certain possibility of generating content that does not exist in the image.
    
    - In scenes containing multiple objects, some objects might be incorrectly identified or described with insufficient detail.
  
- Resolution issue
  
    - Yi-VL is trained on images with a resolution of 448&times;448. During inference, inputs of any resolution are resized to 448&times;448. Low-resolution images may result in information loss, and more fine-grained images (above 448) do not bring in extra knowledge.
    
- Other limitations of the Yi LLM.

# Why Yi-VL?

## Tech report

For detailed capabilities of the Yi series model, see [Yi: Open Foundation Models by 01.AI](https://arxiv.org/abs/2403.04652).

### Citation
```
@misc{ai2024yi,
    title={Yi: Open Foundation Models by 01.AI},
    author={01. AI and : and Alex Young and Bei Chen and Chao Li and Chengen Huang and Ge Zhang and Guanwei Zhang and Heng Li and Jiangcheng Zhu and Jianqun Chen and Jing Chang and Kaidong Yu and Peng Liu and Qiang Liu and Shawn Yue and Senbin Yang and Shiming Yang and Tao Yu and Wen Xie and Wenhao Huang and Xiaohui Hu and Xiaoyi Ren and Xinyao Niu and Pengcheng Nie and Yuchi Xu and Yudong Liu and Yue Wang and Yuxuan Cai and Zhenyu Gu and Zhiyuan Liu and Zonghong Dai},
    year={2024},
    eprint={2403.04652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```


## Benchmarks

Yi-VL outperforms all existing open-source models in [MMMU](https://mmmu-benchmark.github.io) and [CMMMU](https://cmmmu-benchmark.github.io), two advanced benchmarks that include massive multi-discipline multimodal questions (based on data available up to January 2024).

- MMMU

![image/png](https://cdn-uploads.huggingface.co/production/uploads/656d9adce8bf55919aca7c3f/kCmXuwLbLvequ93kjh3mg.png)

- CMMMU
  
![image/png](https://cdn-uploads.huggingface.co/production/uploads/656d9adce8bf55919aca7c3f/6YuSakMCg3D2AozixdoZ0.png)

## Showcases

Below are some representative examples of detailed description and visual question answering, showcasing the capabilities of Yi-VL.

- English
  

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64cc65d786d8dc0caa6ab3cd/F_2bIVwMtVamygbVqtb8E.png)

- Chinese
  
![image/png](https://cdn-uploads.huggingface.co/production/uploads/656d9adce8bf55919aca7c3f/l_tLzugFtHk1dkVsFJE7B.png)

# How to use Yi-VL?

## Quick start

Please refer to [Yi GitHub Repo](https://github.com/01-ai/Yi/tree/main/VL) for details.

## Hardware requirements

For model inference, the recommended GPU examples are:

- Yi-VL-6B: RTX 3090, RTX 4090, A10, A30

- Yi-VL-34B: 4 &times; RTX 4090, A800 (80 GB)

# Misc.

## Acknowledgements and attributions

This project makes use of open-source software/components. We acknowledge and are grateful to these developers for their contributions to the open-source community.

### List of used open-source projects

1. LLaVA
  - Authors: Haotian Liu, Chunyuan Li, Qingyang Wu, Yuheng Li, and Yong Jae Lee
  - Source: https://github.com/haotian-liu/LLaVA
  - License: Apache-2.0 license
  - Description: The codebase is based on LLaVA code.

2. OpenClip
  - Authors: Gabriel Ilharco, Mitchell Wortsman, Ross Wightman, Cade Gordon, Nicholas Carlini, Rohan Taori, Achal Dave, Vaishaal Shankar, Hongseok Namkoong, John Miller, Hannaneh Hajishirzi, Ali Farhadi, and Ludwig Schmidt
  - Source: https://huggingface.co/laion/CLIP-ViT-H-14-laion2B-s32B-b79K
  - License: MIT
  - Description: The ViT is initialized using the weights of OpenClip.

**Notes**

- This attribution does not claim to cover all open-source components used. Please check individual components and their respective licenses for full details.
  
- The use of the open-source components is subject to the terms and conditions of the respective licenses.

We appreciate the open-source community for their invaluable contributions to the technology world.

## License

Please refer to the [acknowledgments and attributions](#acknowledgments_and_attributions) as well as individual components, for the license of source code. 

The Yi series models are fully open for academic research and free for commercial use, permissions of which are automatically granted upon application. 

All usage must adhere to the [Apache 2.0 license](https://github.com/01-ai/Yi/blob/main/LICENSE). 

For free commercial use, you only need to send an email to get official commercial permission.