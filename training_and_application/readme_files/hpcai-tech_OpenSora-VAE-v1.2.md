---
license: apache-2.0
---


<p align="center">
    <img src="https://cdn-uploads.huggingface.co/production/uploads/63993d721fad4d6eb265d999/UXleJWJExX2WlBizxzYxn.png" width="250"/>
</p>


# Open-Sora VAE-v1.2 Weights

This repository stores the weights of the VAE released by the Open-Sora team. You can visit our project at:

- [GitHub](https://github.com/hpcaitech/Open-Sora)
- [Gallery](https://hpcaitech.github.io/Open-Sora/)
- [Gradio Demo](https://huggingface.co/spaces/hpcai-tech/open-sora)

The weights are released together with Open-Sora v1.2.

We recommend you to use this weights in the [Open-Sora codebase]((https://github.com/hpcaitech/Open-Sora)). If you want to use VAE in your own project, you may use the following sample code.

1. Install `opensora`

```bash
pip install git+https://github.com/hpcaitech/Open-Sora.git
```

2. Use `STDiT3` in your own code

```python
from opensora.models.vae.vae import VideoAutoencoderPipeline
vae = VideoAutoencoderPipeline.from_pretrained("hpcai-tech/OpenSora-VAE-v1.2")
```