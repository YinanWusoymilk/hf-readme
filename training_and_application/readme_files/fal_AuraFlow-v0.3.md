---
license: apache-2.0
tags:
- text-to-image
---
# AuraFlow v0.3


![image/png](https://cdn-uploads.huggingface.co/production/uploads/6311151c64939fabc00c8436/BcH5xyGCGNnkmPC-OPS9z.png)


AuraFlow v0.3 is the fully open-sourced flow-based text-to-image generation model. The model was trained with more compute compared to the previous version, [AuraFlow-v0.2](https://huggingface.co/fal/AuraFlow-v0.2).

Compared to AuraFlow-v0.2, the model is fine-tuned on more aesthetic datasets and now supports various aspect ratio, (now width and height up to 1536 pixels).

This model achieves state-of-the-art results on GenEval. Read our [blog post](https://blog.fal.ai/auraflow/) for more technical details. You can also check out the comparison with other models on this gallery [page](https://cloneofsimo.github.io/compare_aura_sd3/).

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
    "fal/AuraFlow-v0.3",
    torch_dtype=torch.float16,
    variant="fp16",
).to("cuda")

image = pipeline(
    prompt="rempage of the iguana character riding F1, fast and furious, cinematic movie poster",
    width=1536,
    height=768,
    num_inference_steps=50, 
    generator=torch.Generator().manual_seed(1),
    guidance_scale=3.5,
).images[0]

image.save("output.png")
```