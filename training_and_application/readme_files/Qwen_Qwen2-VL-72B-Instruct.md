---
license: other
license_name: tongyi-qianwen
license_link: https://huggingface.co/Qwen/Qwen2-VL-72B-Instruct/blob/main/LICENSE
language:
- en
pipeline_tag: image-text-to-text
tags:
- multimodal
library_name: transformers
---

# Qwen2-VL-72B-Instruct

## Introduction

We're excited to unveil **Qwen2-VL**, the latest iteration of our Qwen-VL model, representing nearly a year of innovation.

### What’s New in Qwen2-VL?

#### Key Enhancements:


* **SoTA understanding of images of various resolution & ratio**: Qwen2-VL achieves state-of-the-art performance on visual understanding benchmarks, including MathVista, DocVQA, RealWorldQA, MTVQA, etc.

* **Understanding videos of 20min+**: Qwen2-VL can understand videos over 20 minutes for high-quality video-based question answering, dialog, content creation, etc.

* **Agent that can operate your mobiles, robots, etc.**: with the abilities of complex reasoning and decision making, Qwen2-VL can be integrated with devices like mobile phones, robots, etc., for automatic operation based on visual environment and text instructions.

* **Multilingual Support**: to serve global users, besides English and Chinese, Qwen2-VL now supports the understanding of texts in different languages inside images, including most European languages, Japanese, Korean, Arabic, Vietnamese, etc.


#### Model Architecture Updates:

* **Naive Dynamic Resolution**: Unlike before, Qwen2-VL can handle arbitrary image resolutions, mapping them into a dynamic number of visual tokens, offering a more human-like visual processing experience.

<p align="center">
    <img src="https://qianwen-res.oss-accelerate-overseas.aliyuncs.com/Qwen2-VL/qwen2_vl.jpg" width="80%"/>
<p>

* **Multimodal Rotary Position Embedding (M-ROPE)**: Decomposes positional embedding into parts to capture 1D textual, 2D visual, and 3D video positional information, enhancing its multimodal processing capabilities.

<p align="center">
    <img src="http://qianwen-res.oss-accelerate-overseas.aliyuncs.com/Qwen2-VL/mrope.png" width="80%"/>
<p>

We have three models with 2, 8 and 72 billion parameters. This repo contains the instruction-tuned 72B Qwen2-VL model. For more information, visit our [Blog](https://qwenlm.github.io/blog/qwen2-vl/) and [GitHub](https://github.com/QwenLM/Qwen2-VL).



## Evaluation

### Image Benchmarks

| Benchmark | Previous SoTA<br><sup>(Open-source LVLM)<sup> | Claude-3.5 Sonnet | GPT-4o | **Qwen2-VL-72B**
| :--- | :---: | :---: | :---: | :---: |
| MMMU<sub>val</sub>  | 58.3 | 68.3 | **69.1** | 64.5 
| DocVQA<sub>test</sub>  | 94.1 | 95.2 | 92.8 | **96.5**
| InfoVQA<sub>test</sub>  | 82.0 | - | - | **84.5** 
| ChartQA<sub>test</sub>  | 88.4 | **90.8** | 85.7 | 88.3 
| TextVQA<sub>val</sub>  | 84.4 | - | - | **85.5** 
| OCRBench | 852 | 788 | 736 | **877** 
| MTVQA | 17.3 | 25.7 | 27.8 | **30.9** 
| VCR<sub>en easy</sub>  | 84.67 | 63.85 | 91.55 | **91.93** 
| VCR<sub>zh easy</sub>  | 22.09 | 1.0| 14.87 | **65.37** 
| RealWorldQA | 72.2 | 60.1 | 75.4 | **77.8** 
| MME<sub>sum</sub>   | 2414.7 | 1920.0 | 2328.7 | **2482.7**
| MMBench-EN<sub>test</sub>  | **86.5** | 79.7 | 83.4 | **86.5** 
| MMBench-CN<sub>test</sub>  | 86.3 | 80.7 | 82.1 | **86.6**
| MMBench-V1.1<sub>test</sub>  | 85.5 | 78.5 | 82.2 | **85.9**
| MMT-Bench<sub>test</sub> | 63.4 | - | 65.5 | **71.7** 
| MMStar | 67.1 | 62.2 | 63.9 | **68.3** 
| MMVet<sub>GPT-4-Turbo</sub>  | 65.7 | 66.0 | 69.1 | **74.0**
| HallBench<sub>avg</sub>  | 55.2 | 49.9 | 55.0 | **58.1** 
| MathVista<sub>testmini</sub>  | 67.5 | 67.7 | 63.8 | **70.5** 
| MathVision  | 16.97 | - | **30.4** | 25.9 

### Video Benchmarks

| Benchmark |  Previous SoTA<br><sup>(Open-source LVLM)<sup> | Gemini 1.5-Pro | GPT-4o | **Qwen2-VL-72B**
| :--- | :---: | :---: | :---: | :---: | 
| MVBench | 69.6 | - | - | **73.6** 
| PerceptionTest<sub>test</sub> |  66.9 | - | - | **68.0** 
| EgoSchema<sub>test</sub>  | 62.0 | 63.2 | 72.2 | **77.9**
| Video-MME<br><sub>(wo/w subs)</sub>  | 66.3/69.6  | **75.0**/**81.3** | 71.9/77.2 | 71.2/77.8 

### Agent Benchmarks
|     |Benchmark | Metric | Previous SoTA | GPT-4o | **Qwen2-VL-72B** |
| :-- | :-- | :--: | :--: | :--: | :--: |
|   General  | FnCall<sup>[1]</sup> | TM | - | 90.2 | **93.1** |
|     |  | EM | - | 50.0 | **53.2** |
|   Game  | Number Line | SR | 89.4<sup>[2]</sup> | 91.5 | **100.0** |
|     | BlackJack | SR | 40.2<sup>[2]</sup> | 34.5 | **42.6** |
|     | EZPoint | SR | 50.0<sup>[2]</sup> | 85.5 | **100.0** |
|     | Point24 | SR | 2.6<sup>[2]</sup> | 3.0 | **4.5** |
| Android | AITZ  | TM | 83.0<sup>[3]</sup> | 70.0 | **89.6** |
|     |  | EM | 47.7<sup>[3]</sup> | 35.3 | **72.1** |
| AI2THOR | ALFRED<sub>valid-unseen</sub> | SR | 67.7<sup>[4]</sup> | - | **67.8** |
|     |  | GC | 75.3<sup>[4]</sup> | - | **75.8** | 
|  VLN   | R2R<sub>valid-unseen</sub>  | SR | **79.0** | 43.7<sup>[5]</sup> | 51.7 | 
|     | REVERIE<sub>valid-unseen</sub> | SR | **61.0** | 31.6<sup>[5]</sup> | 31.0 | 

SR, GC, TM and EM are short for success rate, goal-condition success, type match and exact match. ALFRED is supported by SAM<sup>[6]</sup>.
1. Self-Curated Function Call Benchmark by Qwen Team
2. Fine-Tuning Large Vision-Language Models as Decision-Making Agents via Reinforcement Learning
3. Android in the Zoo: Chain-of-Action-Thought for GUI Agents
4. ThinkBot: Embodied Instruction Following with Thought Chain Reasoning
5. MapGPT: Map-Guided Prompting with Adaptive Path Planning for Vision-and-Language Navigation
6. Segment Anything.

   
### Multilingual Benchmarks

<table style="width:75%; text-align:center;">
    <tr>
        <th>Models</th>
        <td>AR </td>
        <td>DE </td>
        <td>FR </td>
        <td>IT </td>
        <td>JA </td>
        <td>KO </td>
        <td>RU </td>
        <td>TH </td>
        <td>VI </td>
        <td>AVG</td>
    </tr>
    <tr>
        <th align="left">Qwen2-VL-72B</th>
        <td>20.7 </td>
        <td>36.5 </td>
        <td>44.1 </td>
        <td>42.8 </td>
        <td>21.6 </td>
        <td>37.4 </td>
        <td>15.6 </td>
        <td>17.7 </td>
        <td>41.6 </td>
        <td><b>30.9</b></td>
    </tr>
    <tr>
        <th align="left">GPT-4o</th>
        <td>20.2 </td>
        <td>34.2 </td>
        <td>41.2 </td>
        <td>32.7 </td>
        <td>20.0 </td>
        <td>33.9 </td>
        <td>11.5 </td>
        <td>22.5 </td>
        <td>34.2 </td>
        <td>27.8</td>
    </tr>
        <tr>
        <th align="left">Claude3 Opus</th>
        <td>15.1 </td>
        <td>33.4 </td>
        <td>40.6 </td>
        <td>34.4 </td>
        <td>19.4 </td>
        <td>27.2 </td>
        <td>13.0 </td>
        <td>19.5 </td>
        <td>29.1 </td>
        <td>25.7 </td>
    </tr>
    <tr>
        <th align="left">Gemini Ultra</th>
        <td>14.7 </td>
        <td>32.3 </td>
        <td>40.0 </td>
        <td>31.8 </td>
        <td>12.3 </td>
        <td>17.2 </td>
        <td>11.8 </td>
        <td>20.3 </td>
        <td>28.6 </td>
        <td>23.2</td>
    </tr>
</table>




## Requirements
The code of Qwen2-VL has been in the latest Hugging face transformers and we advise you to build from source with command `pip install git+https://github.com/huggingface/transformers`, or you might encounter the following error:
```
KeyError: 'qwen2_vl'
```

## Quickstart
We offer a toolkit to help you handle various types of visual input more conveniently. This includes base64, URLs, and interleaved images and videos. You can install it using the following command:

```bash
pip install qwen-vl-utils
```

Here we show a code snippet to show you how to use the chat model with `transformers` and `qwen_vl_utils`:

```python
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info

# default: Load the model on the available device(s)
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-72B-Instruct", torch_dtype="auto", device_map="auto"
)

# We recommend enabling flash_attention_2 for better acceleration and memory saving, especially in multi-image and video scenarios.
# model = Qwen2VLForConditionalGeneration.from_pretrained(
#     "Qwen/Qwen2-VL-72B-Instruct",
#     torch_dtype=torch.bfloat16,
#     attn_implementation="flash_attention_2",
#     device_map="auto",
# )

# default processer
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-72B-Instruct")

# The default range for the number of visual tokens per image in the model is 4-16384. You can set min_pixels and max_pixels according to your needs, such as a token count range of 256-1280, to balance speed and memory usage.
# min_pixels = 256*28*28
# max_pixels = 1280*28*28
# processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-72B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg",
            },
            {"type": "text", "text": "Describe this image."},
        ],
    }
]

# Preparation for inference
text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to("cuda")

# Inference: Generation of the output
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
```
<details>
<summary>Without qwen_vl_utils</summary>

```python
from PIL import Image
import requests
import torch
from torchvision import io
from typing import Dict
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor

# Load the model in half-precision on the available device(s)
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-72B-Instruct", torch_dtype="auto", device_map="auto"
)
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-72B-Instruct")

# Image
url = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-VL/assets/demo.jpeg"
image = Image.open(requests.get(url, stream=True).raw)

conversation = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
            },
            {"type": "text", "text": "Describe this image."},
        ],
    }
]


# Preprocess the inputs
text_prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
# Excepted output: '<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n<|im_start|>user\n<|vision_start|><|image_pad|><|vision_end|>Describe this image.<|im_end|>\n<|im_start|>assistant\n'

inputs = processor(
    text=[text_prompt], images=[image], padding=True, return_tensors="pt"
)
inputs = inputs.to("cuda")

# Inference: Generation of the output
output_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids = [
    output_ids[len(input_ids) :]
    for input_ids, output_ids in zip(inputs.input_ids, output_ids)
]
output_text = processor.batch_decode(
    generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True
)
print(output_text)
```
</details>
<details>
<summary>Multi image inference</summary>

```python
# Messages containing multiple images and a text query
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/image1.jpg"},
            {"type": "image", "image": "file:///path/to/image2.jpg"},
            {"type": "text", "text": "Identify the similarities between these images."},
        ],
    }
]

# Preparation for inference
text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to("cuda")

# Inference
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
```
</details>

<details>
<summary>Video inference</summary>

```python
# Messages containing a images list as a video and a text query
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video",
                "video": [
                    "file:///path/to/frame1.jpg",
                    "file:///path/to/frame2.jpg",
                    "file:///path/to/frame3.jpg",
                    "file:///path/to/frame4.jpg",
                ],
                "fps": 1.0,
            },
            {"type": "text", "text": "Describe this video."},
        ],
    }
]
# Messages containing a video and a text query
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "video",
                "video": "file:///path/to/video1.mp4",
                "max_pixels": 360 * 420,
                "fps": 1.0,
            },
            {"type": "text", "text": "Describe this video."},
        ],
    }
]

# Preparation for inference
text = processor.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to("cuda")

# Inference
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_text)
```
</details>

<details>
<summary>Batch inference</summary>

```python
# Sample messages for batch inference
messages1 = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/image1.jpg"},
            {"type": "image", "image": "file:///path/to/image2.jpg"},
            {"type": "text", "text": "What are the common elements in these pictures?"},
        ],
    }
]
messages2 = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who are you?"},
]
# Combine messages for batch processing
messages = [messages1, messages1]

# Preparation for batch inference
texts = [
    processor.apply_chat_template(msg, tokenize=False, add_generation_prompt=True)
    for msg in messages
]
image_inputs, video_inputs = process_vision_info(messages)
inputs = processor(
    text=texts,
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)
inputs = inputs.to("cuda")

# Batch Inference
generated_ids = model.generate(**inputs, max_new_tokens=128)
generated_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_texts = processor.batch_decode(
    generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
)
print(output_texts)
```
</details>

### More Usage Tips

For input images, we support local files, base64, and URLs. For videos, we currently only support local files.

```python
# You can directly insert a local file path, a URL, or a base64-encoded image into the position where you want in the text.
## Local file path
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/your/image.jpg"},
            {"type": "text", "text": "Describe this image."},
        ],
    }
]
## Image URL
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "http://path/to/your/image.jpg"},
            {"type": "text", "text": "Describe this image."},
        ],
    }
]
## Base64 encoded image
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "data:image;base64,/9j/..."},
            {"type": "text", "text": "Describe this image."},
        ],
    }
]
```
#### Image Resolution for performance boost

The model supports a wide range of resolution inputs. By default, it uses the native resolution for input, but higher resolutions can enhance performance at the cost of more computation. Users can set the minimum and maximum number of pixels to achieve an optimal configuration for their needs, such as a token count range of 256-1280, to balance speed and memory usage.

```python
min_pixels = 256 * 28 * 28
max_pixels = 1280 * 28 * 28
processor = AutoProcessor.from_pretrained(
    "Qwen/Qwen2-VL-72B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels
)
```

Besides, We provide two methods for fine-grained control over the image size input to the model:

1. Define min_pixels and max_pixels: Images will be resized to maintain their aspect ratio within the range of min_pixels and max_pixels.
   
2. Specify exact dimensions: Directly set `resized_height` and `resized_width`. These values will be rounded to the nearest multiple of 28.

```python
# min_pixels and max_pixels
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "file:///path/to/your/image.jpg",
                "resized_height": 280,
                "resized_width": 420,
            },
            {"type": "text", "text": "Describe this image."},
        ],
    }
]
# resized_height and resized_width
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": "file:///path/to/your/image.jpg",
                "min_pixels": 50176,
                "max_pixels": 50176,
            },
            {"type": "text", "text": "Describe this image."},
        ],
    }
]
```

## Limitations

While Qwen2-VL are applicable to a wide range of visual tasks, it is equally important to understand its limitations. Here are some known restrictions:

1. Lack of Audio Support: The current model does **not comprehend audio information** within videos.
2. Data timeliness: Our image dataset is **updated until June 2023**, and information subsequent to this date may not be covered.
3. Constraints in Individuals and Intellectual Property (IP): The model's capacity to recognize specific individuals or IPs is limited, potentially failing to comprehensively cover all well-known personalities or brands.
4. Limited Capacity for Complex Instruction: When faced with intricate multi-step instructions, the model's understanding and execution capabilities require enhancement.
5. Insufficient Counting Accuracy: Particularly in complex scenes, the accuracy of object counting is not high, necessitating further improvements.
6. Weak Spatial Reasoning Skills: Especially in 3D spaces, the model's inference of object positional relationships is inadequate, making it difficult to precisely judge the relative positions of objects.

These limitations serve as ongoing directions for model optimization and improvement, and we are committed to continually enhancing the model's performance and scope of application.


## Citation

If you find our work helpful, feel free to give us a cite.

```
@article{Qwen2VL,
  title={Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution},
  author={Wang, Peng and Bai, Shuai and Tan, Sinan and Wang, Shijie and Fan, Zhihao and Bai, Jinze and Chen, Keqin and Liu, Xuejing and Wang, Jialin and Ge, Wenbin and Fan, Yang and Dang, Kai and Du, Mengfei and Ren, Xuancheng and Men, Rui and Liu, Dayiheng and Zhou, Chang and Zhou, Jingren and Lin, Junyang},
  journal={arXiv preprint arXiv:2409.12191},
  year={2024}
}

@article{Qwen-VL,
  title={Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond},
  author={Bai, Jinze and Bai, Shuai and Yang, Shusheng and Wang, Shijie and Tan, Sinan and Wang, Peng and Lin, Junyang and Zhou, Chang and Zhou, Jingren},
  journal={arXiv preprint arXiv:2308.12966},
  year={2023}
}
```