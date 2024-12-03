---
datasets:
- lmms-lab/LLaVA-OneVision-Data
language:
- en
- zh
library_name: transformers
license: apache-2.0
metrics:
- accuracy
tags:
- multimodal
---

# LLaVA-OneVision

![banner](https://i.postimg.cc/pL17YtG4/WX20240508-220230-2x.png)

Play with the model on the [LLaVA OneVision Chat](https://llava-onevision.lmms-lab.com/).

## Table of Contents

1. [Model Summary](##model-summary)
2. [Use](##use)
3. [Limitations](##limitations)
4. [Training](##training)
5. [License](##license)
6. [Citation](##citation)

## Model Summary

`llava-onevision-7b-ov-chat` is our latest model specifically designed for chat scenarios. It is built upon `llava-onevision-7b-ov` and has undergone iterative DPO training with human preference, making it well-suited for chat applications.

Research by [Tianyi Xiong](https://tyxiong23.github.io/) indicates that our iterative DPO training method enhances the model's chat capabilities while preserving its instruction-following abilities.

For further details, please refer to our upcoming blog or paper.

- **Repository:** [LLaVA-VL/LLaVA-NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT?tab=readme-ov-file)
- **Project Website:** [llava-onevision.lmms-lab.com](llava-onevision.lmms-lab.com)
- **Paper:** [LLaVA-OneVision](arxiv.org/abs/2408.03326)
- **Point of Contact:** [Tianyi Xiong](https://tyxiong23.github.io/), [Bo Li](mailto:drluodian@gmail.com)
- **Languages:** English, Chinese

## Benchmark Performance

To be released

## Use

### Intended use

The model was trained on [LLaVA-OneVision Dataset](https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data) and have the ability to interact with images, multi-image and videos.

**Feel free to share your generations in the Community tab!**

### Generation

```python
# pip install git+https://github.com/LLaVA-VL/LLaVA-NeXT.git
from llava.model.builder import load_pretrained_model
from llava.mm_utils import get_model_name_from_path, process_images, tokenizer_image_token
from llava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN, IGNORE_INDEX
from llava.conversation import conv_templates, SeparatorStyle

from PIL import Image
import requests
import copy
import torch

import sys
import warnings

warnings.filterwarnings("ignore")
pretrained = "lmms-lab/llava-onevision-qwen2-0.5b-si"
model_name = "llava_qwen"
device = "cuda"
device_map = "auto"
tokenizer, model, image_processor, max_length = load_pretrained_model(pretrained, None, model_name, device_map=device_map)  # Add any other thing you want to pass in llava_model_args

model.eval()

url = "https://github.com/haotian-liu/LLaVA/blob/1a91fc274d7c35a9b50b3cb29c4247ae5837ce39/images/llava_v1_5_radar.jpg?raw=true"
image = Image.open(requests.get(url, stream=True).raw)
image_tensor = process_images([image], image_processor, model.config)
image_tensor = [_image.to(dtype=torch.float16, device=device) for _image in image_tensor]

conv_template = "qwen_1_5"  # Make sure you use correct chat template for different models
question = DEFAULT_IMAGE_TOKEN + "\nWhat is shown in this image?"
conv = copy.deepcopy(conv_templates[conv_template])
conv.append_message(conv.roles[0], question)
conv.append_message(conv.roles[1], None)
prompt_question = conv.get_prompt()

input_ids = tokenizer_image_token(prompt_question, tokenizer, IMAGE_TOKEN_INDEX, return_tensors="pt").unsqueeze(0).to(device)
image_sizes = [image.size]


cont = model.generate(
    input_ids,
    images=image_tensor,
    image_sizes=image_sizes,
    do_sample=False,
    temperature=0,
    max_new_tokens=4096,
)
text_outputs = tokenizer.batch_decode(cont, skip_special_tokens=True)
print(text_outputs)
```

# Training

## Model

- **Architecture:** SO400M + Qwen2
- **Pretraining Stage:** LCS-558K, 1 epoch, projector
- **Mid Stage:** A mixture of 4.7M high-quality synthetic data, 1 epoch, full model
- **Final-Image Stage:** A mixture of 3.6M single-image data, 1 epoch, full model
- **OneVision Stage:** A mixture of 1.6M single-image/multi-image/video data, 1 epoch, full model
- **Critic / Preference Learning Stage:** 9.4k question-image input from [LLaVA-RLHF](https://llava-rlhf.github.io/) with self-generated responses, reward signal from [llava-critic-7b](https://huggingface.co/lmms-lab/llava-critic-7b), iterative DPO for 3 rounds, full model
- **Precision:** bfloat16

## Hardware & Software

- **GPUs:** 256 \* Nvidia Tesla A100 (for whole model series training)
- **Orchestration:** [Huggingface Trainer](https://huggingface.co/docs/transformers/main_classes/trainer)
- **Neural networks:** [PyTorch](https://github.com/pytorch/pytorch)

# Citation

```
@article{li2024llavaonevision,
  	title={LLaVA-OneVision: Easy Visual Task Transfer},
  	author={Li, Bo and Zhang, Yuanhan and Guo, Dong and Zhang, Renrui and Li, Feng and Zhang, Hao and Zhang, Kaichen and Li, Yanwei and Liu, Ziwei and Li, Chunyuan},
  	journal={arXiv preprint arXiv:2408.03326},
  	year={2024}
}

@article{xiong2024llavacritic,
  title={LLaVA-Critic: Learning to Evaluate Multimodal Models},
  author={Xiong, Tianyi and Wang, Xiyao and Guo, Dong and Ye, Qinghao and Fan, Haoqi and Gu, Quanquan and Huang, Heng and Li, Chunyuan},
  year={2024},
  eprint={2410.02712},
  archivePrefix={arXiv},
  primaryClass={cs.CV},
  url={https://arxiv.org/abs/2410.02712},
}
```
