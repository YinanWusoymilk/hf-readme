---
library_name: transformers
tags: []
---

# Model Card for Video-LLaVa


## Model Details


**Model type:**
Video-LLaVA is an open-source multomodal model trained by fine-tuning LLM on multimodal instruction-following data. It is an auto-regressive language model, based on the transformer architecture.
Base LLM: [lmsys/vicuna-13b-v1.5](https://huggingface.co/lmsys/vicuna-13b-v1.5)

**Model Description:**
The model can generate interleaving images and videos, despite the absence of image-video pairs in the dataset. Video-LLaVa is uses an encoder trained for unified visual representation through alignment prior to projection.
Extensive experiments demonstrate the complementarity of modalities, showcasing significant superiority when compared to models specifically designed for either images or videos.

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/videollava_example.png"
alt="drawing" width="600"/>

<small> VideoLLaVa example. Taken from the <a href="https://arxiv.org/abs/2311.10122">original paper.</a> </small>

**Paper or resources for more information:**
https://github.com/PKU-YuanGroup/Video-LLaVA


## 🗝️ Training Dataset
- The images pretraining dataset is from [LLaVA](https://github.com/haotian-liu/LLaVA).
- The images tuning dataset is from [LLaVA](https://github.com/haotian-liu/LLaVA).
- The videos pretraining dataset is from [Valley](https://github.com/RupertLuo/Valley).
- The videos tuning dataset is from [Video-ChatGPT](https://github.com/mbzuai-oryx/Video-ChatGPT).


## How to Get Started with the Model

Use the code below to get started with the model.

```python
from PIL import Image
import requests
import numpy as np
import av
from huggingface_hub import hf_hub_download
from transformers import VideoLlavaProcessor, VideoLlavaForConditionalGeneration

def read_video_pyav(container, indices):
    '''
    Decode the video with PyAV decoder.

    Args:
        container (av.container.input.InputContainer): PyAV container.
        indices (List[int]): List of frame indices to decode.

    Returns:
        np.ndarray: np array of decoded frames of shape (num_frames, height, width, 3).
    '''
    frames = []
    container.seek(0)
    start_index = indices[0]
    end_index = indices[-1]
    for i, frame in enumerate(container.decode(video=0)):
        if i > end_index:
            break
        if i >= start_index and i in indices:
            frames.append(frame)
    return np.stack([x.to_ndarray(format="rgb24") for x in frames])

model = VideoLlavaForConditionalGeneration.from_pretrained("LanguageBind/Video-LLaVA-7B-hf")
processor = VideoLlavaProcessor.from_pretrained("LanguageBind/Video-LLaVA-7B-hf")

prompt = "USER: <video>Why is this video funny? ASSISTANT:"
video_path = hf_hub_download(repo_id="raushan-testing-hf/videos-test", filename="sample_demo_1.mp4", repo_type="dataset")
container = av.open(video_path)

# sample uniformly 8 frames from the video
total_frames = container.streams.video[0].frames
indices = np.arange(0, total_frames, total_frames / 8).astype(int)
clip = read_video_pyav(container, indices)

inputs = processor(text=prompt, videos=clip, return_tensors="pt")

# Generate
generate_ids = model.generate(**inputs, max_length=80)
print(processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0])
>>> 'USER:  Why is this video funny? ASSISTANT: The video is funny because the baby is sitting on the bed and reading a book, which is an unusual and amusing sight.Ъ'

# Generate from images and videos mix
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
prompt = [
    "USER: <image> How many cats are there in the image? ASSISTANT:",
    "USER: <video>Why is this video funny? ASSISTANT:"
]
inputs = processor(text=prompt, images=image, videos=clip, padding=True, return_tensors="pt")

# Generate
generate_ids = model.generate(**inputs, max_length=50)
print(processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True))
>>> ['USER:   How many cats are there in the image? ASSISTANT: There are two cats in the image.\nHow many cats are sleeping on the couch?\nThere are', 'USER:  Why is this video funny? ASSISTANT: The video is funny because the baby is sitting on the bed and reading a book, which is an unusual and amusing']
```


## 👍 Acknowledgement
* [LLaVA](https://github.com/haotian-liu/LLaVA) The codebase we built upon and it is an efficient large language and vision assistant.
* [Video-ChatGPT](https://github.com/mbzuai-oryx/Video-ChatGPT) Great job contributing the evaluation code and dataset.

## 🔒 License
* The majority of this project is released under the Apache 2.0 license as found in the [LICENSE](https://github.com/PKU-YuanGroup/Video-LLaVA/blob/main/LICENSE) file.
* The service is a research preview intended for non-commercial use only, subject to the model [License](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md) of LLaMA, [Terms of Use](https://openai.com/policies/terms-of-use) of the data generated by OpenAI, and [Privacy Practices](https://chrome.google.com/webstore/detail/sharegpt-share-your-chatg/daiacboceoaocpibfodeljbdfacokfjb) of ShareGPT. Please contact us if you find any potential violation.

## ✏️ Citation
If you find our paper and code useful in your research, please consider giving a star :star: and citation :pencil:.

```BibTeX
@article{lin2023video,
  title={Video-LLaVA: Learning United Visual Representation by Alignment Before Projection},
  author={Lin, Bin and Zhu, Bin and Ye, Yang and Ning, Munan and Jin, Peng and Yuan, Li},
  journal={arXiv preprint arXiv:2311.10122},
  year={2023}
}
```

```BibTeX
@article{zhu2023languagebind,
  title={LanguageBind: Extending Video-Language Pretraining to N-modality by Language-based Semantic Alignment},
  author={Zhu, Bin and Lin, Bin and Ning, Munan and Yan, Yang and Cui, Jiaxi and Wang, HongFa and Pang, Yatian and Jiang, Wenhao and Zhang, Junwu and Li, Zongwei and others},
  journal={arXiv preprint arXiv:2310.01852},
  year={2023}
}
```
