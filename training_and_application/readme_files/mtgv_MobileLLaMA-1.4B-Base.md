---
license: apache-2.0
datasets:
- togethercomputer/RedPajama-Data-1T
tags:
- llama
---
# Model Summery
MobileLLaMA-1.4B-Base is a Transformer with 1.4B billon paramters. We downscale LLaMA to facilitate the off-the-shelf deployment. To make our work reproducible, all
the models are trained on 1.3T tokens from the [RedPajama v1](https://www.together.ai/blog/redpajama) dataset only. This benefits further research by enabling controlled experiments.

We extensively assess our models on two standard natural language benchmarks, for language understanding and common sense reasoning respectively. Experimental results show that our
MobileLLaMA 1.4B is on par with the most recent opensource models.

# Model Sources
- Repository: https://github.com/Meituan-AutoML/MobileVLM
- Paper: https://arxiv.org/abs/2312.16886

# How to Get Started with the Model
Model weights can be loaded with Hugging Face Transformers. Examples can be found at [Github](https://github.com/Meituan-AutoML/MobileVLM).

# Training Details
please refer to our paper in section 4.1: [MobileVLM: A Fast, Strong and Open Vision Language Assistant for Mobile Devices](https://arxiv.org/pdf/2312.16886.pdf).