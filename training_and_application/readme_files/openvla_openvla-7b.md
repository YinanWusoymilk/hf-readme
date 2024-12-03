---
library_name: transformers
tags:
- robotics
- vla
- image-text-to-text
- multimodal
- pretraining
license: mit
language:
- en
pipeline_tag: image-text-to-text
---

# OpenVLA 7B

OpenVLA 7B (`openvla-7b`) is an open vision-language-action model trained on 970K robot manipulation episodes from the [Open X-Embodiment](https://robotics-transformer-x.github.io/) dataset. 
The model takes language instructions and camera images as input and generates robot actions. It supports controlling multiple robots out-of-the-box, and can be quickly adapted for new robot domains via (parameter-efficient) fine-tuning.

All OpenVLA checkpoints, as well as our [training codebase](https://github.com/openvla/openvla) are released under an MIT License.

For full details, please read [our paper](https://arxiv.org/abs/2406.09246) and see [our project page](https://openvla.github.io/).

## Model Summary

- **Developed by:** The OpenVLA team consisting of researchers from Stanford, UC Berkeley, Google Deepmind, and the Toyota Research Institute.
- **Model type:** Vision-language-action (language, image => robot actions)
- **Language(s) (NLP):** en
- **License:** MIT
- **Finetuned from:** [`prism-dinosiglip-224px`](https://github.com/TRI-ML/prismatic-vlms), a VLM trained from:
  + **Vision Backbone**: DINOv2 ViT-L/14 and SigLIP ViT-So400M/14
  + **Language Model**: Llama-2
- **Pretraining Dataset:** [Open X-Embodiment](https://robotics-transformer-x.github.io/) -- specific component datasets can be found [here](https://github.com/openvla/openvla).
- **Repository:** [https://github.com/openvla/openvla](https://github.com/openvla/openvla)
- **Paper:** [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)
- **Project Page & Videos:** [https://openvla.github.io/](https://openvla.github.io/)

## Uses

OpenVLA models take a language instruction and a camera image of a robot workspace as input, and predict (normalized) robot actions consisting of 7-DoF end-effector deltas
of the form (x, y, z, roll, pitch, yaw, gripper). To execute on an actual robot platform, actions need to be *un-normalized* subject to statistics computed on a per-robot,
per-dataset basis. See [our repository](https://github.com/openvla/openvla) for more information.

OpenVLA models can be used zero-shot to control robots for specific combinations of embodiments and domains seen in the Open-X pretraining mixture (e.g., for 
[BridgeV2 environments with a Widow-X robot](https://rail-berkeley.github.io/bridgedata/)). They can also be efficiently *fine-tuned* for new tasks and robot setups
given minimal demonstration data; [see here](https://github.com/openvla/openvla/blob/main/scripts/finetune.py).

**Out-of-Scope:** OpenVLA models do not zero-shot generalize to new (unseen) robot embodiments, or setups that are not represented in the pretraining mix; in these cases,
we suggest collecting a dataset of demonstrations on the desired setup, and fine-tuning OpenVLA models instead.

## Getting Started

OpenVLA 7B can be used to control multiple robots for domains represented in the pretraining mixture out-of-the-box. For example,
here is an example for loading `openvla-7b` for zero-shot instruction following in the [BridgeV2 environments] with a Widow-X robot:

```python
# Install minimal dependencies (`torch`, `transformers`, `timm`, `tokenizers`, ...)
# > pip install -r https://raw.githubusercontent.com/openvla/openvla/main/requirements-min.txt
from transformers import AutoModelForVision2Seq, AutoProcessor
from PIL import Image

import torch

# Load Processor & VLA
processor = AutoProcessor.from_pretrained("openvla/openvla-7b", trust_remote_code=True)
vla = AutoModelForVision2Seq.from_pretrained(
    "openvla/openvla-7b",
    attn_implementation="flash_attention_2",  # [Optional] Requires `flash_attn`
    torch_dtype=torch.bfloat16, 
    low_cpu_mem_usage=True, 
    trust_remote_code=True
).to("cuda:0")

# Grab image input & format prompt
image: Image.Image = get_from_camera(...)
prompt = "In: What action should the robot take to {<INSTRUCTION>}?\nOut:"

# Predict Action (7-DoF; un-normalize for BridgeV2)
inputs = processor(prompt, image).to("cuda:0", dtype=torch.bfloat16)
action = vla.predict_action(**inputs, unnorm_key="bridge_orig", do_sample=False)

# Execute...
robot.act(action, ...)
```

For more examples, including scripts for fine-tuning OpenVLA models on your own robot demonstration datasets, see [our training repository](https://github.com/openvla/openvla).

## Citation

**BibTeX:**

```bibtex
@article{kim24openvla,
    title={OpenVLA: An Open-Source Vision-Language-Action Model},
    author={{Moo Jin} Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},
    journal = {arXiv preprint arXiv:2406.09246},
    year={2024}
} 
```