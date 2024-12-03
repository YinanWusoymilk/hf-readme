---
license: mit
datasets:
- laion/laion2B-en
- laion/laion-coco
- laion/laion2B-multi
- kakaobrain/coyo-700m
- conceptual_captions
- wanng/wukong100m
pipeline_tag: image-feature-extraction
base_model: OpenGVLab/InternViT-6B-448px-V1-2
base_model_relation: finetune
---

# InternViT-6B-448px-V1-5

[\[📂 GitHub\]](https://github.com/OpenGVLab/InternVL)  [\[🆕 Blog\]](https://internvl.github.io/blog/)  [\[📜 InternVL 1.0 Paper\]](https://arxiv.org/abs/2312.14238)  [\[📜 InternVL 1.5 Report\]](https://arxiv.org/abs/2404.16821)

[\[🗨️ Chat Demo\]](https://internvl.opengvlab.com/)  [\[🤗 HF Demo\]](https://huggingface.co/spaces/OpenGVLab/InternVL)  [\[🚀 Quick Start\]](#quick-start)  [\[📖 中文解读\]](https://zhuanlan.zhihu.com/p/706547971)  [\[📖 Documents\]](https://internvl.readthedocs.io/en/latest/)

We develop InternViT-6B-448px-V1-5 based on the pre-training of the strong foundation of [InternViT-6B-448px-V1-2](https://huggingface.co/OpenGVLab/InternViT-6B-448px-V1-2). In this update, the resolution of training images is expanded from 448&times;448 to dynamic 448&times;448, where the basic tile size is 448&times;448 and the number of tiles ranges from 1 to 12.
Additionally, we enhance the data scale, quality, and diversity of the pre-training dataset, resulting in the powerful robustness, OCR capability, and high-resolution processing capability of our
1.5 version model. 

## Model Details
- **Model Type:** vision foundation model, feature backbone
- **Model Stats:**
  - Params (M): 5540 (the last 3 blocks are discarded)
  - Image size: 448 x 448, training with 1 - 12 tiles
- **Pretrain Dataset:** LAION-en, LAION-zh, COYO, GRIT, COCO, TextCaps, Objects365, OpenImages, All-Seeing, Wukong-OCR, LaionCOCO-OCR, and other OCR-related datasets. 
To enhance the OCR capability of the model, we have incorporated additional OCR data alongside the general caption datasets. Specifically, we utilized PaddleOCR to perform Chinese OCR on images from Wukong and English OCR on images from LAION-COCO. 
- **Note:** InternViT-6B originally had 48 blocks, and we found that using the output after the fourth-to-last block worked best for MLLM. For ease of use and to save GPU memory, we simply discarded the last 3 blocks. Now, the model has only 45 blocks and the number of parameters has been reduced from 5.9B to 5.5B. Therefore, if you want to build a MLLM based on this model, **please make use of the features from the last layer.**

## Model Usage (Image Embeddings)

```python
import torch
from PIL import Image
from transformers import AutoModel, CLIPImageProcessor

model = AutoModel.from_pretrained(
    'OpenGVLab/InternViT-6B-448px-V1-5',
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    trust_remote_code=True).cuda().eval()

image = Image.open('./examples/image1.jpg').convert('RGB')

image_processor = CLIPImageProcessor.from_pretrained('OpenGVLab/InternViT-6B-448px-V1-5')

pixel_values = image_processor(images=image, return_tensors='pt').pixel_values
pixel_values = pixel_values.to(torch.bfloat16).cuda()

outputs = model(pixel_values)
```

## Citation

If you find this project useful in your research, please consider citing:

```BibTeX
@article{chen2023internvl,
  title={InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks},
  author={Chen, Zhe and Wu, Jiannan and Wang, Wenhai and Su, Weijie and Chen, Guo and Xing, Sen and Zhong, Muyan and Zhang, Qinglong and Zhu, Xizhou and Lu, Lewei and Li, Bin and Luo, Ping and Lu, Tong and Qiao, Yu and Dai, Jifeng},
  journal={arXiv preprint arXiv:2312.14238},
  year={2023}
}
@article{chen2024far,
  title={How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},
  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and Ye, Shenglong and Gao, Zhangwei and Cui, Erfei and Tong, Wenwen and Hu, Kongzhi and Luo, Jiapeng and Ma, Zheng and others},
  journal={arXiv preprint arXiv:2404.16821},
  year={2024}
}
```
