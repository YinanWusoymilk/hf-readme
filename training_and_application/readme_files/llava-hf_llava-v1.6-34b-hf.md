---
tags:
- vision
- image-text-to-text
language:
- en
pipeline_tag: image-text-to-text
---

# LLaVa-Next, leveraging [NousResearch/Nous-Hermes-2-Yi-34B](https://huggingface.co/NousResearch/Nous-Hermes-2-Yi-34B) as LLM

The LLaVA-NeXT model was proposed in [LLaVA-NeXT: Improved reasoning, OCR, and world knowledge](https://llava-vl.github.io/blog/2024-01-30-llava-next/) by Haotian Liu, Chunyuan Li, Yuheng Li, Bo Li, Yuanhan Zhang, Sheng Shen, Yong Jae Lee. LLaVa-NeXT (also called LLaVa-1.6) improves upon [LLaVa](https://huggingface.co/llava-hf/llava-1.5-7b-hf) by increasing the input image resolution and training on an improved visual instruction tuning dataset to improve OCR and common sense reasoning.

Disclaimer: The team releasing LLaVa-NeXT did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

LLaVa combines a pre-trained large language model with a pre-trained vision encoder for multimodal chatbot use cases. LLaVA 1.6 improves on LLaVA 1.5 BY:
- Using [Mistral-7B](https://mistral.ai/news/announcing-mistral-7b/) and [Nous-Hermes-2-Yi-34B](https://huggingface.co/NousResearch/Nous-Hermes-2-Yi-34B)  (for this checkpoint) which has better commercial licenses,
  and bilingual support
- More diverse and high quality data mixture
- Dynamic high resolution
  
![image/png](https://cdn-uploads.huggingface.co/production/uploads/62441d1d9fdefb55a0b7d12c/FPshq08TKYD0e-qwPLDVO.png)

## Intended uses & limitations

You can use the raw model for tasks like image captioning, visual question answering, multimodal chatbot use cases. See the [model hub](https://huggingface.co/models?search=llava-hf) to look for
other versions on a task that interests you.

### How to use

Here's the prompt template for this model:
```
"<|im_start|>system\n<your_system_prompt_here><|im_end|><|im_start|>user\n<image>\n<your_text_prompt_here><|im_end|><|im_start|>assistant\n"
```

You can load and use the model like following:
```python
from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
import torch
from PIL import Image
import requests

processor = LlavaNextProcessor.from_pretrained("llava-hf/llava-v1.6-34b-hf")

model = LlavaNextForConditionalGeneration.from_pretrained("llava-hf/llava-v1.6-34b-hf", torch_dtype=torch.float16, low_cpu_mem_usage=True) 
model.to("cuda:0")

# prepare image and text prompt, using the appropriate prompt template
url = "https://github.com/haotian-liu/LLaVA/blob/1a91fc274d7c35a9b50b3cb29c4247ae5837ce39/images/llava_v1_5_radar.jpg?raw=true"
image = Image.open(requests.get(url, stream=True).raw)

# Define a chat histiry and use `apply_chat_template` to get correctly formatted prompt
# Each value in "content" has to be a list of dicts with types ("text", "image") 
conversation = [
    {

      "role": "user",
      "content": [
          {"type": "text", "text": "What is shown in this image?"},
          {"type": "image"},
        ],
    },
]
prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)

inputs = processor(images=image, text=prompt, return_tensors="pt").to("cuda:0")

# autoregressively complete prompt
output = model.generate(**inputs, max_new_tokens=100)

print(processor.decode(output[0], skip_special_tokens=True))
```

### Model optimization

#### 4-bit quantization through `bitsandbytes` library

First make sure to install `bitsandbytes`, `pip install bitsandbytes` and make sure to have access to a CUDA compatible GPU device. Simply change the snippet above with: 

```diff
model = LlavaNextForConditionalGeneration.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    low_cpu_mem_usage=True,
+   load_in_4bit=True
)
```

#### Use Flash-Attention 2 to further speed-up generation

First make sure to install `flash-attn`. Refer to the [original repository of Flash Attention](https://github.com/Dao-AILab/flash-attention) regarding that package installation. Simply change the snippet above with: 

```diff
model = LlavaNextForConditionalGeneration.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    low_cpu_mem_usage=True,
+   use_flash_attention_2=True
).to(0)
```

### BibTeX entry and citation info

```bibtex
@misc{liu2023improved,
      title={Improved Baselines with Visual Instruction Tuning}, 
      author={Haotian Liu and Chunyuan Li and Yuheng Li and Yong Jae Lee},
      year={2023},
      eprint={2310.03744},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```