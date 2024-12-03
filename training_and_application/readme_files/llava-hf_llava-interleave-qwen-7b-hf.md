---
language:
- en
license: other
license_name: tongyi-qianwen-research
license_link: LICENSE
pipeline_tag: image-text-to-text
tags:
- vision
- image-text-to-text
---

# LLaVA Interleave Model Card

## Model Details


**Model type:**
LLaVA Interleave is an open-source chatbot trained by fine-tuning LLM on multimodal instruction-following data. It is an auto-regressive language model, based on the transformer architecture. 
Base LLM: [Qwen/Qwen1.5-7B-Chat](https://huggingface.co/Qwen/Qwen1.5-0.5B-Chat)

**Paper or resources for more information:**
https://llava-vl.github.io/

**Primary intended uses:** 
The primary use of LLaVA-Next Interleave is research on large multimodal models and chatbots. This is only for research exploration, and prohibited for commercial usage.

**Primary intended users:** 
The primary intended users of the model are researchers and hobbyists in computer vision, natural language processing, machine learning, and artificial intelligence.


## How to use the model

First, make sure to have `transformers >= 4.35.3`. 
The model supports multi-image and multi-prompt generation. Meaning that you can pass multiple images in your prompt. Make sure also to follow the correct prompt template (`USER: xxx\nASSISTANT:`) and add the token `<image>` to the location where you want to query images:

### Using `pipeline`:

Below we used [`"llava-hf/llava-interleave-qwen-0.5b-hf"`](https://huggingface.co/llava-hf/llava-interleave-qwen-0.5b-hf) checkpoint.


```python
from transformers import pipeline, AutoProcessor
from PIL import Image    
import requests

model_id = "llava-hf/llava-interleave-qwen-7b-hf"
pipe = pipeline("image-to-text", model=model_id)
processor = AutoProcessor.from_pretrained(model_id)

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/ai2d-demo.jpg"
image = Image.open(requests.get(url, stream=True).raw)

# Define a chat history and use `apply_chat_template` to get correctly formatted prompt
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
from transformers import AutoProcessor, LlavaForConditionalGeneration

model_id = "llava-hf/llava-interleave-qwen-7b-hf"
model = LlavaForConditionalGeneration.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    low_cpu_mem_usage=True, 
).to(0)

processor = AutoProcessor.from_pretrained(model_id)

# Define a chat history and use `apply_chat_template` to get correctly formatted prompt
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


When prompting with videos/3D/multi-view input, prompt like following: 

```python
# if you downsampled n frames from the input

image_tokens = "<image>" * n
prompt = f"<|im_start|>user {image_tokens}\nWhat are these?|im_end|><|im_start|>assistant"

# With chat template if you sampled 5 frames you have to have 5 images in one conversation turn
conversation = [
    {

      "role": "user",
      "content": [
          {"type": "text", "text": "What are these?"},
          {"type": "image"},
          {"type": "image"},
          {"type": "image"},
          {"type": "image"},
          {"type": "image"},
        ],
    },
]
prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
```

When prompting with interleaved images and videos, prompt like following: 

```python
# two interleaved images
prompt = "<|im_start|>user <image><image>\nWhat is the difference between these two images?|im_end|><|im_start|>assistant"

# two interleaved videos, if you downsampled n frames in total from both videos
image_tokens = "<image>" * n
prompt = f"<|im_start|>user {image_tokens}\nWhat are these?|im_end|><|im_start|>assistant"

# chat template in interleaved format work same as in sampling videos. Just pass in as many images you want for a prompt
conversation = [
    {

      "role": "user",
      "content": [
          {"type": "text", "text": "What is the difference between these two images?"},
          {"type": "image"},
          {"type": "image"},
        ],
    },
]
```

### Model optimization

#### 4-bit quantization through `bitsandbytes` library

First make sure to install `bitsandbytes`, `pip install bitsandbytes` and make sure to have access to a CUDA compatible GPU device. Simply change the snippet above with: 

```diff
model = LlavaForConditionalGeneration.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    low_cpu_mem_usage=True,
+   load_in_4bit=True
)
```

#### Use Flash-Attention 2 to further speed-up generation

First make sure to install `flash-attn`. Refer to the [original repository of Flash Attention](https://github.com/Dao-AILab/flash-attention) regarding that package installation. Simply change the snippet above with: 

```diff
model = LlavaForConditionalGeneration.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    low_cpu_mem_usage=True,
+   use_flash_attention_2=True
).to(0)
```

### License Notices
  
This project utilizes certain datasets and checkpoints that are subject to their respective original licenses. Users must comply with all terms and conditions of these original licenses, including but not limited to the OpenAI Terms of Use for the dataset and the specific licenses for base language models for checkpoints trained using the dataset [Tongyi Qianwen LICENSE AGREEMENT](https://github.com/QwenLM/Qwen/blob/main/Tongyi%20Qianwen%20LICENSE%20AGREEMENT) and [META LLAMA 3 COMMUNITY LICENSE AGREEMENT](https://llama.meta.com/llama3/license/)). This project does not impose any additional constraints beyond those stipulated in the original licenses. Furthermore, users are reminded to ensure that their use of the dataset and checkpoints is in compliance with all applicable laws and regulations.

### Bibtext citation

```bibtext
@misc{li2024llavanextinterleavetacklingmultiimagevideo,
      title={LLaVA-NeXT-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models}, 
      author={Feng Li and Renrui Zhang and Hao Zhang and Yuanhan Zhang and Bo Li and Wei Li and Zejun Ma and Chunyuan Li},
      year={2024},
      eprint={2407.07895},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2407.07895}, 
}
```