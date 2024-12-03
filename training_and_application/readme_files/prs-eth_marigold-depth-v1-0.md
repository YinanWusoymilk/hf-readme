---
license: apache-2.0
language:
- en
pipeline_tag: depth-estimation
tags:
- monocular depth estimation
- single image depth estimation
- depth
- in-the-wild
- zero-shot
- depth
---
# Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation

This model represents the official checkpoint of the paper titled "Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation".

[![Website](doc/badges/badge-website.svg)](https://marigoldmonodepth.github.io)
[![GitHub](https://img.shields.io/github/stars/prs-eth/Marigold?style=default&label=GitHub%20★&logo=github)](https://github.com/prs-eth/Marigold)
[![Paper](doc/badges/badge-pdf.svg)](https://arxiv.org/abs/2312.02145)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12G8reD13DdpMie5ZQlaFNo2WCGeNUH-u?usp=sharing)
[![Hugging Face Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-yellow)](https://huggingface.co/spaces/toshas/marigold)
[![License](https://img.shields.io/badge/License-Apache--2.0-929292)](https://www.apache.org/licenses/LICENSE-2.0)
<!-- [![HF Space](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-blue)]() -->
<!-- [![Open In Colab](doc/badges/badge-colab.svg)]() -->
<!-- [![Docker](doc/badges/badge-docker.svg)]() -->
<!-- ### [Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation]() -->

[Bingxin Ke](http://www.kebingxin.com/),
[Anton Obukhov](https://www.obukhov.ai/),
[Shengyu Huang](https://shengyuh.github.io/),
[Nando Metzger](https://nandometzger.github.io/),
[Rodrigo Caye Daudt](https://rcdaudt.github.io/),
[Konrad Schindler](https://scholar.google.com/citations?user=FZuNgqIAAAAJ&hl=en )

We present Marigold, a diffusion model and associated fine-tuning protocol for monocular depth estimation. Its core principle is to leverage the rich visual knowledge stored in modern generative image models. Our model, derived from Stable Diffusion and fine-tuned with synthetic data, can zero-shot transfer to unseen data, offering state-of-the-art monocular depth estimation results.

![teaser](doc/teaser_collage_transparant.png)


## 🎓 Citation

```bibtex
@InProceedings{ke2023repurposing,
      title={Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation},
      author={Bingxin Ke and Anton Obukhov and Shengyu Huang and Nando Metzger and Rodrigo Caye Daudt and Konrad Schindler},
      booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
      year={2024}
}
```

## 🎫 License

This work is licensed under the Apache License, Version 2.0 (as defined in the [LICENSE](LICENSE.txt)).

By downloading and using the code and model you agree to the terms in the  [LICENSE](LICENSE.txt).

[![License](https://img.shields.io/badge/License-Apache--2.0-929292)](https://www.apache.org/licenses/LICENSE-2.0)
