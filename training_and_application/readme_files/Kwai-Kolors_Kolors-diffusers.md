---
license: apache-2.0
language:
- zh
- en
tags:
- Kolors
---
# Kolors: Effective Training of Diffusion Model for Photorealistic Text-to-Image Synthesis
<div align="center" style="display: flex; justify-content: center; flex-wrap: wrap;">
  <a href="https://github.com/Kwai-Kolors/Kolors"><img src="https://img.shields.io/static/v1?label=Kolors Code&message=Github&color=blue&logo=github-pages"></a> &ensp;
  <a href="https://kwai-kolors.github.io/"><img src="https://img.shields.io/static/v1?label=Team%20Page&message=Page&color=green"></a> &ensp;
  <a href="https://github.com/Kwai-Kolors/Kolors/blob/master/imgs/Kolors_paper.pdf"><img src="https://img.shields.io/static/v1?label=Tech Report&message=Arxiv:Kolors&color=red&logo=arxiv"></a> &ensp;
  <a href="https://kolors.kuaishou.com/"><img src="https://img.shields.io/static/v1?label=Official Website&message=Page&color=green"></a>
</div>
<figure>
  <img src="imgs/head_final3.png">
</figure>

## 📖 Introduction
Kolors is a large-scale text-to-image generation model based on latent diffusion, developed by the Kuaishou Kolors team. Trained on billions of text-image pairs, Kolors exhibits significant advantages over both open-source and proprietary models in visual quality, complex semantic accuracy, and text rendering for both Chinese and English characters. Furthermore, Kolors supports both Chinese and English inputs, demonstrating strong performance in understanding and generating Chinese-specific content. For more details, please refer to this <a href="https://github.com/Kwai-Kolors/Kolors/blob/master/imgs/Kolors_paper.pdf">technical report</a></b>.

## 🚀 Quick Start
### Using with Diffusers
Make sure you upgrade to the latest version of diffusers==0.30.0.dev0: 
```
git clone https://github.com/huggingface/diffusers
cd diffusers
python3 setup.py install
```
**Notes:**
- The pipeline uses the `EulerDiscreteScheduler` by default. We recommend using this scheduler with `guidance scale=5.0` and `num_inference_steps=50`.
- The pipeline also supports the `EDMDPMSolverMultistepScheduler`. `guidance scale=5.0` and `num_inference_steps=25` is a good default for this scheduler.
- In addition to Text-to-Image, `KolorsImg2ImgPipeline` also supports Image-to-Image.

And then you can run:
```python
import torch

from diffusers import KolorsPipeline

pipe = KolorsPipeline.from_pretrained(
    "Kwai-Kolors/Kolors-diffusers", 
    torch_dtype=torch.float16, 
    variant="fp16"
).to("cuda")

prompt = '一张瓢虫的照片，微距，变焦，高质量，电影，拿着一个牌子，写着"可图"'

image = pipe(
    prompt=prompt,
    negative_prompt="",
    guidance_scale=5.0,
    num_inference_steps=50,
    generator=torch.Generator(pipe.device).manual_seed(66),
).images[0]
image.show()
```

## 📜 License&Citation
### License
Kolors are fully open-sourced for academic research. For commercial use, please fill out this [questionnaire](https://github.com/Kwai-Kolors/Kolors/blob/master/imgs/可图KOLORS模型商业授权申请书.docx) and sent it to kwai-kolors@kuaishou.com for registration.

We open-source Kolors to promote the development of large text-to-image models in collaboration with the open-source community. The code of this project is open-sourced under the Apache-2.0 license. We sincerely urge all developers and users to strictly adhere to the [open-source license](MODEL_LICENSE), avoiding the use of the open-source model, code, and its derivatives for any purposes that may harm the country and society or for any services not evaluated and registered for safety. Note that despite our best efforts to ensure the compliance, accuracy, and safety of the data during training, due to the diversity and combinability of generated content and the probabilistic randomness affecting the model, we cannot guarantee the accuracy and safety of the output content, and the model is susceptible to misleading. This project does not assume any legal responsibility for any data security issues, public opinion risks, or risks and liabilities arising from the model being misled, abused, misused, or improperly utilized due to the use of the open-source model and code.


### Citation
If you find our work helpful, please cite it!

```
@article{kolors,
  title={Kolors: Effective Training of Diffusion Model for Photorealistic Text-to-Image Synthesis},
  author={Kolors Team},
  journal={arXiv preprint},
  year={2024}
}
```

### Acknowledgments
- Thanks to [Diffusers](https://github.com/huggingface/diffusers) for providing the codebase.
- Thanks to [ChatGLM3](https://github.com/THUDM/ChatGLM3) for providing the powerful Chinese language model.

### Contact Us

If you want to leave a message for our R&D team and product team, feel free to join our [WeChat group](https://github.com/Kwai-Kolors/Kolors/blob/main/imgs/wechat.png). You can also contact us via email (kwai-kolors@kuaishou.com).