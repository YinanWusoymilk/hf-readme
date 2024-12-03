---
inference: false
pipeline_tag: image-text-to-text
---
<br>
<br>

# ShareGPT4V-7B Model Card

## Model details

**Model type:**
ShareGPT4V-7B is an open-source chatbot trained by fine-tuning CLP vision tower and LLaMA/Vicuna on GPT4-Vision-assisted [ShareGPT4V](https://huggingface.co/datasets/Lin-Chen/ShareGPT4V) data and LLaVA instruction-tuning data.

**Model date:**
ShareGPT4V-7B was trained in Nov 2023.

**Paper or resources for more information:**
[[Project](https://ShareGPT4V.github.io/)] [[Paper](https://huggingface.co/papers/2311.12793)] [[Code](https://github.com/ShareGPT4Omni/ShareGPT4V)]

## Usage
You can directly utilize this model as we provide in our [[repository](https://github.com/ShareGPT4Omni/ShareGPT4V)]. Moreover, you can modify the architecture name from "Share4VLlamaForCausalLM" to "LLaVALlamaForCausalLM" and the model_type keyword from "share4v" to "llava" in our config file and seamlessly load our model in the [[LLaVA repository](https://github.com/haotian-liu/LLaVA)].

## License
Llama 2 is licensed under the LLAMA 2 Community License, 
Copyright (c) Meta Platforms, Inc. All Rights Reserved.

## Intended use
**Primary intended uses:**
The primary use of ShareGPT4V-7B is research on large multimodal models and chatbots.

**Primary intended users:**
The primary intended users of the model are researchers and hobbyists in computer vision, natural language processing, machine learning, and artificial intelligence.

## Training dataset
- 1.2M high-quality image-text pairs, i.e., ShareGPT4V-PT data
- 100K GPT4-Vision-generated image-text pairs
- LLaVA instruction-tuning data

## Evaluation dataset
A collection of 11 benchmarks