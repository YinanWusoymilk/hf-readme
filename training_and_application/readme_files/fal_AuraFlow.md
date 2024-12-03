---
license: apache-2.0
tags:
- text-to-image
---
# AuraFlow

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6380ebb8471a4550ff255c62/jMkLXPFVNGdUb7P4nNTqX.png)


AuraFlow v0.1 is the fully open-sourced largest flow-based text-to-image generation model.

This model achieves state-of-the-art results on GenEval. Read our [blog post](https://blog.fal.ai/auraflow/) for more technical details.

The model is currently in beta. We are working on improving it and the community's feedback is important.
Join [fal's Discord](https://discord.gg/fal-ai) to give us feedback and stay in touch with the model development.

Credits: A huge thank you to [@cloneofsimo](https://twitter.com/cloneofsimo) and [@isidentical](https://twitter.com/isidentical) for bringing this project to life. It's incredible what two cracked engineers can achieve in
such a short period of time. We also extend our gratitude to the incredible researchers whose prior work laid the foundation for our efforts.

## Usage

```bash
$ pip install transformers accelerate protobuf sentencepiece
$ pip install git+https://github.com/huggingface/diffusers.git
```

```python
from diffusers import AuraFlowPipeline
import torch

pipeline = AuraFlowPipeline.from_pretrained(
    "fal/AuraFlow",
    torch_dtype=torch.float16
).to("cuda")

image = pipeline(
    prompt="close-up portrait of a majestic iguana with vibrant blue-green scales, piercing amber eyes, and orange spiky crest. Intricate textures and details visible on scaly skin. Wrapped in dark hood, giving regal appearance. Dramatic lighting against black background. Hyper-realistic, high-resolution image showcasing the reptile's expressive features and coloration.",
    height=1024,
    width=1024,
    num_inference_steps=50, 
    generator=torch.Generator().manual_seed(666),
    guidance_scale=3.5,
).images[0]
```