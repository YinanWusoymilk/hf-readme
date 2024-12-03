---
license: other
language:
- en
base_model:
- meta-llama/Meta-Llama-3.1-8B-Instruct
pipeline_tag: video-text-to-text
inference: false
library_name: transformers
---

[中文阅读](README_zh.md)

# CogVLM2-Llama3-Caption

<div align="center">
    <img src=https://raw.githubusercontent.com/THUDM/CogVLM2/cf9cb3c60a871e0c8e5bde7feaf642e3021153e6/resources/logo.svg> 
</div>


[Code](https://github.com/THUDM/CogVideo/tree/main/tools/caption) | 🤗 [Hugging Face](https://huggingface.co/THUDM/cogvlm2-llama3-caption) | 🤖 [ModelScope](https://modelscope.cn/models/ZhipuAI/cogvlm2-llama3-caption/) 


Typically, most video data does not come with corresponding descriptive text, so it is necessary to convert the video
data into textual descriptions to provide the essential training data for text-to-video models. 
CogVLM2-Caption is a video captioning model used to generate training data for the CogVideoX model.

<div align="center">
    <img width="600px" height="auto" src="./CogVLM2-Caption-example.png">
</div>

## Usage

```python
import io

import argparse
import numpy as np
import torch
from decord import cpu, VideoReader, bridge
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_PATH = "THUDM/cogvlm2-llama3-caption"

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'
TORCH_TYPE = torch.bfloat16 if torch.cuda.is_available() and torch.cuda.get_device_capability()[
    0] >= 8 else torch.float16

parser = argparse.ArgumentParser(description="CogVLM2-Video CLI Demo")
parser.add_argument('--quant', type=int, choices=[4, 8], help='Enable 4-bit or 8-bit precision loading', default=0)
args = parser.parse_args([])


def load_video(video_data, strategy='chat'):
    bridge.set_bridge('torch')
    mp4_stream = video_data
    num_frames = 24
    decord_vr = VideoReader(io.BytesIO(mp4_stream), ctx=cpu(0))

    frame_id_list = None
    total_frames = len(decord_vr)
    if strategy == 'base':
        clip_end_sec = 60
        clip_start_sec = 0
        start_frame = int(clip_start_sec * decord_vr.get_avg_fps())
        end_frame = min(total_frames,
                        int(clip_end_sec * decord_vr.get_avg_fps())) if clip_end_sec is not None else total_frames
        frame_id_list = np.linspace(start_frame, end_frame - 1, num_frames, dtype=int)
    elif strategy == 'chat':
        timestamps = decord_vr.get_frame_timestamp(np.arange(total_frames))
        timestamps = [i[0] for i in timestamps]
        max_second = round(max(timestamps)) + 1
        frame_id_list = []
        for second in range(max_second):
            closest_num = min(timestamps, key=lambda x: abs(x - second))
            index = timestamps.index(closest_num)
            frame_id_list.append(index)
            if len(frame_id_list) >= num_frames:
                break

    video_data = decord_vr.get_batch(frame_id_list)
    video_data = video_data.permute(3, 0, 1, 2)
    return video_data


tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    trust_remote_code=True,
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=TORCH_TYPE,
    trust_remote_code=True
).eval().to(DEVICE)


def predict(prompt, video_data, temperature):
    strategy = 'chat'

    video = load_video(video_data, strategy=strategy)

    history = []
    query = prompt
    inputs = model.build_conversation_input_ids(
        tokenizer=tokenizer,
        query=query,
        images=[video],
        history=history,
        template_version=strategy
    )
    inputs = {
        'input_ids': inputs['input_ids'].unsqueeze(0).to('cuda'),
        'token_type_ids': inputs['token_type_ids'].unsqueeze(0).to('cuda'),
        'attention_mask': inputs['attention_mask'].unsqueeze(0).to('cuda'),
        'images': [[inputs['images'][0].to('cuda').to(TORCH_TYPE)]],
    }
    gen_kwargs = {
        "max_new_tokens": 2048,
        "pad_token_id": 128002,
        "top_k": 1,
        "do_sample": False,
        "top_p": 0.1,
        "temperature": temperature,
    }
    with torch.no_grad():
        outputs = model.generate(**inputs, **gen_kwargs)
        outputs = outputs[:, inputs['input_ids'].shape[1]:]
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response


def test():
    prompt = "Please describe this video in detail."
    temperature = 0.1
    video_data = open('test.mp4', 'rb').read()
    response = predict(prompt, video_data, temperature)
    print(response)


if __name__ == '__main__':
    test()
```

## License

This model is released under the
CogVLM2  [LICENSE](https://modelscope.cn/models/ZhipuAI/cogvlm2-video-llama3-base/file/view/master?fileName=LICENSE&status=0).
For models built with Meta Llama 3, please also adhere to
the [LLAMA3_LICENSE](https://modelscope.cn/models/ZhipuAI/cogvlm2-video-llama3-base/file/view/master?fileName=LLAMA3_LICENSE&status=0).

## Citation

🌟 If you find our work helpful, please leave us a star and cite our paper.

```
@article{yang2024cogvideox,
  title={CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer},
  author={Yang, Zhuoyi and Teng, Jiayan and Zheng, Wendi and Ding, Ming and Huang, Shiyu and Xu, Jiazheng and Yang, Yuanming and Hong, Wenyi and Zhang, Xiaohan and Feng, Guanyu and others},
  journal={arXiv preprint arXiv:2408.06072},
  year={2024}
}