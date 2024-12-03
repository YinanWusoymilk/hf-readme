---
datasets:
- lmms-lab/LLaVA-OneVision-Data
- lmms-lab/LLaVA-Video-178K
language:
- en
library_name: transformers
license: apache-2.0
metrics:
- accuracy
tags:
- multimodal
pipeline_tag: video-text-to-text
model-index:
- name: LLaVA-Video-7B-Qwen2
  results:
  - task:
      type: multimodal
    dataset:
      name: ActNet-QA
      type: actnet-qa
    metrics:
    - type: accuracy
      value: 56.5
      name: accuracy
      verified: true
  - task:
      type: multimodal
    dataset:
      name: EgoSchema
      type: egoschema
    metrics:
    - type: accuracy
      value: 57.3
      name: accuracy
      verified: true
  - task:
      type: multimodal
    dataset:
      name: MLVU
      type: mlvu
    metrics:
    - type: accuracy
      value: 70.8
      name: accuracy
      verified: true
  - task:
      type: multimodal
    dataset:
      name: MVBench
      type: mvbench
    metrics:
    - type: accuracy
      value: 58.6
      name: accuracy
      verified: true
  - task:
      type: multimodal
    dataset:
      name: NextQA
      type: nextqa
    metrics:
    - type: accuracy
      value: 83.2
      name: accuracy
      verified: true
  - task:
      type: multimodal
    dataset:
      name: PercepTest
      type: percepTest
    metrics:
    - type: accuracy
      value: 67.9
      name: accuracy
      verified: true
  - task:
      type: multimodal
    dataset:
      name: VideoChatGPT
      type: videochatgpt
    metrics:
    - type: score
      value: 3.52
      name: score
      verified: true
  - task:
      type: multimodal
    dataset:
      name: VideoDC
      type: videodc
    metrics:
    - type: score
      value: 3.66
      name: score
      verified: true
  - task:
      type: multimodal
    dataset:
      name: LongVideoBench
      type: longvideobench
    metrics:
    - type: accuracy
      value: 58.2
      name: accuracy
      verified: true
  - task:
      type: multimodal
    dataset:
      name: VideoMME
      type: videomme
    metrics:
    - type: accuracy
      value: 63.3
      name: accuracy
      verified: true
base_model:
- lmms-lab/llava-onevision-qwen2-7b-si
---

# LLaVA-Video-7B-Qwen2

##  Table of Contents

1. [Model Summary](##model-summary)
2. [Use](##use)
3. [Limitations](##limitations)
4. [Training](##training)
5. [License](##license)
6. [Citation](##citation)

## Model Summary

The LLaVA-Video models are 7/72B parameter models trained on [LLaVA-Video-178K](https://huggingface.co/datasets/lmms-lab/LLaVA-Video-178K) and [LLaVA-OneVision Dataset](https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data), based on Qwen2 language model with a context window of 32K tokens.

This model support at most 64 frames.

- **Project Page:** [Project Page](https://llava-vl.github.io/blog/2024-09-30-llava-video/).
- **Paper**: For more details, please check our [paper](https://arxiv.org/abs/2410.02713) 
- **Repository:** [LLaVA-VL/LLaVA-NeXT](https://github.com/LLaVA-VL/LLaVA-NeXT?tab=readme-ov-file)
- **Point of Contact:** [Yuanhan Zhang](https://zhangyuanhan-ai.github.io/)
- **Languages:** English, Chinese


## Use

### Intended use

The model was trained on [LLaVA-Video-178K](https://huggingface.co/datasets/lmms-lab/LLaVA-Video-178K) and [LLaVA-OneVision Dataset](https://huggingface.co/datasets/lmms-lab/LLaVA-OneVision-Data), having the ability to interact with images, multi-image and videos, but specific to videos.



**Feel free to share your generations in the Community tab!**

### Generation

We provide the simple generation process for using our model. For more details, you could refer to [Github](https://github.com/LLaVA-VL/LLaVA-NeXT).

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
from decord import VideoReader, cpu
import numpy as np
warnings.filterwarnings("ignore")
def load_video(video_path, max_frames_num,fps=1,force_sample=False):
    if max_frames_num == 0:
        return np.zeros((1, 336, 336, 3))
    vr = VideoReader(video_path, ctx=cpu(0),num_threads=1)
    total_frame_num = len(vr)
    video_time = total_frame_num / vr.get_avg_fps()
    fps = round(vr.get_avg_fps()/fps)
    frame_idx = [i for i in range(0, len(vr), fps)]
    frame_time = [i/fps for i in frame_idx]
    if len(frame_idx) > max_frames_num or force_sample:
        sample_fps = max_frames_num
        uniform_sampled_frames = np.linspace(0, total_frame_num - 1, sample_fps, dtype=int)
        frame_idx = uniform_sampled_frames.tolist()
        frame_time = [i/vr.get_avg_fps() for i in frame_idx]
    frame_time = ",".join([f"{i:.2f}s" for i in frame_time])
    spare_frames = vr.get_batch(frame_idx).asnumpy()
    # import pdb;pdb.set_trace()
    return spare_frames,frame_time,video_time
pretrained = "lmms-lab/LLaVA-Video-7B-Qwen2"
model_name = "llava_qwen"
device = "cuda"
device_map = "auto"
tokenizer, model, image_processor, max_length = load_pretrained_model(pretrained, None, model_name, torch_dtype="bfloat16", device_map=device_map)  # Add any other thing you want to pass in llava_model_args
model.eval()
video_path = "XXXX"
max_frames_num = 64
video,frame_time,video_time = load_video(video_path, max_frames_num, 1, force_sample=True)
video = image_processor.preprocess(video, return_tensors="pt")["pixel_values"].cuda().half()
video = [video]
conv_template = "qwen_1_5"  # Make sure you use correct chat template for different models
time_instruciton = f"The video lasts for {video_time:.2f} seconds, and {len(video[0])} frames are uniformly sampled from it. These frames are located at {frame_time}.Please answer the following questions related to this video."
question = DEFAULT_IMAGE_TOKEN + f"{time_instruciton}\nPlease describe this video in detail."
conv = copy.deepcopy(conv_templates[conv_template])
conv.append_message(conv.roles[0], question)
conv.append_message(conv.roles[1], None)
prompt_question = conv.get_prompt()
input_ids = tokenizer_image_token(prompt_question, tokenizer, IMAGE_TOKEN_INDEX, return_tensors="pt").unsqueeze(0).to(device)
cont = model.generate(
    input_ids,
    images=video,
    modalities= ["video"],
    do_sample=False,
    temperature=0,
    max_new_tokens=4096,
)
text_outputs = tokenizer.batch_decode(cont, skip_special_tokens=True)[0].strip()
print(text_outputs)
```


# Training

## Model

- **Architecture:** SO400M + Qwen2
- **Initialized Model:** lmms-lab/llava-onevision-qwen2-7b-si
- **Data:** A mixture of 1.6M single-image/multi-image/video data, 1 epoch, full model
- **Precision:** bfloat16

## Hardware & Software

- **GPUs:** 256 * Nvidia Tesla A100 (for whole model series training)
- **Orchestration:** [Huggingface Trainer](https://huggingface.co/docs/transformers/main_classes/trainer)
- **Neural networks:** [PyTorch](https://github.com/pytorch/pytorch)

# Citation

```bibtex

@misc{zhang2024videoinstructiontuningsynthetic,
    title={Video Instruction Tuning With Synthetic Data}, 
    author={Yuanhan Zhang and Jinming Wu and Wei Li and Bo Li and Zejun Ma and Ziwei Liu and Chunyuan Li},
    year={2024},
    eprint={2410.02713},
    archivePrefix={arXiv},
    primaryClass={cs.CV},
    url={https://arxiv.org/abs/2410.02713}, 
}
```