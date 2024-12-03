---
language:
- en
pipeline_tag: image-text-to-text
inference: false
arxiv: 2312.00784
tags:
- vision
- image-text-to-text
---
# VipLLaVA Model Card

![image/png](https://github.com/mu-cai/ViP-LLaVA/blob/main/images/vip-llava_arch.png?raw=true)

Below is the model card of VipLlava model 7b, which is copied from the original Llava model card that you can find [here](https://huggingface.co/liuhaotian/llava-v1.5-13b).

Check out also the Google Colab demo to run Llava on a free-tier Google Colab instance (the model works similarly as Llava): [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1-0G7Kuj2iQgKux4NJneP2JefFMamxG6Q?usp=sharing)

Or check out our Spaces demo! [![Open in Spaces](https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-md-dark.svg)](https://huggingface.co/spaces/llava-hf/llava-4bit)


## Model details

**Model type:**
LLaVA is an open-source chatbot trained by fine-tuning LLaMA/Vicuna on GPT-generated multimodal instruction-following data.
It is an auto-regressive language model, based on the transformer architecture.

Vip-LlaVa enhances the training protocol of Llava by marking images and interact with the model using natural cues like a
“red bounding box” or “pointed arrow” during training.

**Model date:**
ViP-LLaVa was released in December 2023.

**Paper or resources for more information:**
https://vip-llava.github.io/

## How to use the model

First, make sure to have `transformers >= 4.35.3`. 
The model supports multi-image and multi-prompt generation. Meaning that you can pass multiple images in your prompt. Make sure also to follow the correct prompt template and add the token `<image>` to the location where you want to query images:

According to the official code base, it is recommeneded to use this template:

```bash
A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.###Human: <image>\n<prompt>###Assistant:
```

Where `<prompt>` denotes the prompt asked by the user

### Using `pipeline`:


```python
from transformers import pipeline
from PIL import Image    
import requests

model_id = "llava-hf/vip-llava-7b-hf"
pipe = pipeline("image-to-text", model=model_id)
url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/ai2d-demo.jpg"
image = Image.open(requests.get(url, stream=True).raw)

# Define a chat histiry and use `apply_chat_template` to get correctly formatted prompt
# Each value in "content" has to be a list of dicts with types ("text", "image") 
conversation = [
    {

      "role": "user",
      "content": [
          {"type": "text", "text": "What does the label 15 represent? (1) lava (2) core (3) tunnel (4) ash cloud"},
          {"type": "image"},
        ],
    },
]
prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)

outputs = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 200})
print(outputs)
```

### Using pure `transformers`:

Below is an example script to run generation in `float16` precision on a GPU device:

```python
import requests
from PIL import Image

import torch
from transformers import AutoProcessor, VipLlavaForConditionalGeneration

model_id = "llava-hf/vip-llava-7b-hf"
model = VipLlavaForConditionalGeneration.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    low_cpu_mem_usage=True, 
).to(0)

processor = AutoProcessor.from_pretrained(model_id)


# Define a chat histiry and use `apply_chat_template` to get correctly formatted prompt
# Each value in "content" has to be a list of dicts with types ("text", "image") 
conversation = [
    {

      "role": "user",
      "content": [
          {"type": "text", "text": "What are these?"},
          {"type": "image"},
        ],
    },
]
prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)

image_file = "http://images.cocodataset.org/val2017/000000039769.jpg"
raw_image = Image.open(requests.get(image_file, stream=True).raw)
inputs = processor(images=raw_image, text=prompt, return_tensors='pt').to(0, torch.float16)

output = model.generate(**inputs, max_new_tokens=200, do_sample=False)
print(processor.decode(output[0][2:], skip_special_tokens=True))
```

### Model optimization

#### 4-bit quantization through `bitsandbytes` library

First make sure to install `bitsandbytes`, `pip install bitsandbytes` and make sure to have access to a CUDA compatible GPU device. Simply change the snippet above with: 

```diff
model = VipLlavaForConditionalGeneration.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    low_cpu_mem_usage=True,
+   load_in_4bit=True
)
```

#### Use Flash-Attention 2 to further speed-up generation

First make sure to install `flash-attn`. Refer to the [original repository of Flash Attention](https://github.com/Dao-AILab/flash-attention) regarding that package installation. Simply change the snippet above with: 

```diff
model = VipLlavaForConditionalGeneration.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    low_cpu_mem_usage=True,
+   use_flash_attention_2=True
).to(0)
```

## License
Llama 2 is licensed under the LLAMA 2 Community License, 
Copyright (c) Meta Platforms, Inc. All Rights Reserved.

## Citation
To cite this work please use
```bibtex
@misc{cai2023making,
      title={Making Large Multimodal Models Understand Arbitrary Visual Prompts}, 
      author={Mu Cai and Haotian Liu and Siva Karthik Mustikovela and Gregory P. Meyer and Yuning Chai and Dennis Park and Yong Jae Lee},
      year={2023},
      eprint={2312.00784},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```