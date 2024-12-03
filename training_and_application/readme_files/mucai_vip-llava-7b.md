---
inference: false
---


<br>
<br>

# ViP-LLaVA Model Card

## Model details

**Model type:**
ViP-LLaVA is an open-source chatbot trained by fine-tuning LLaMA/Vicuna on both image level instruction data and region-level instruction data annotated with visual prompts.
It is an auto-regressive language model, based on the transformer architecture.

**Model date:**
ViP-LLaVA-7B was trained in November 2023. [Paper](https://arxiv.org/abs/2312.00784)

**Paper or resources for more information:**
https://vip-llava.github.io/

## License
Llama 2 is licensed under the LLAMA 2 Community License, 
Copyright (c) Meta Platforms, Inc. All Rights Reserved.

**Where to send questions or comments about the model:**
https://github.com/mu-cai/ViP-LLaVA/issues

## Intended use
**Primary intended uses:**
The primary use of ViP-LLaVA is research on large multimodal models and chatbots.

**Primary intended users:**
The primary intended users of the model are researchers and hobbyists in computer vision, natural language processing, machine learning, and artificial intelligence.

## Training dataset
- 558K filtered image-text pairs from LAION/CC/SBU, captioned by BLIP.
- 665K image level instruction data from LLaVA-1.5.
- 520K image-text pairs marked with visual prompts. 
- 13K region-level instruction data generated from GPT-4V.

## Evaluation dataset
ViP-LLaVA achieves state-of-the-art performance in 4 academic region-level benchmarks and our newly proposed RegionBench.

