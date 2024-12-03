---
license: apache-2.0
language:
- en
pipeline_tag: normals-estimation
tags:
- monocular normals estimation
- single image normals estimation
- normals
- in-the-wild
- zero-shot
- LCM
---
# Marigold Normals (LCM) Model Card

This model belongs to the family of diffusion-based Marigold models for solving various computer vision tasks.
The Marigold Normals model focuses on the surface normals task.
It takes an input image and computes surface normals in each pixel.
The LCM stands for Latent Consistency Models, which is a technique for making the diffusion model fast.
The Marigold Normals model is trained from Stable Diffusion with synthetic data, and the LCM model is further fine-tuned from it.
Thanks to the rich visual knowledge stored in Stable Diffusion, Marigold models possess deep scene understanding and excel at solving computer vision tasks.
Read more about Marigold in our paper titled "Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation".

[![Website](doc/badges/badge-website.svg)](https://marigoldmonodepth.github.io)
[![GitHub](https://img.shields.io/github/stars/prs-eth/Marigold?style=default&label=GitHub%20★&logo=github)](https://github.com/prs-eth/Marigold)
[![Paper](doc/badges/badge-pdf.svg)](https://arxiv.org/abs/2312.02145)
[![Hugging Face Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-yellow)](https://huggingface.co/spaces/toshas/marigold)

Developed by:
[Bingxin Ke](http://www.kebingxin.com/),
[Anton Obukhov](https://www.obukhov.ai/),
[Shengyu Huang](https://shengyuh.github.io/),
[Nando Metzger](https://nandometzger.github.io/),
[Rodrigo Caye Daudt](https://rcdaudt.github.io/),
[Konrad Schindler](https://scholar.google.com/citations?user=FZuNgqIAAAAJ&hl=en)

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

By downloading and using the code and model you agree to the terms in the [LICENSE](LICENSE.txt).

[![License](https://img.shields.io/badge/License-Apache--2.0-929292)](https://www.apache.org/licenses/LICENSE-2.0)
