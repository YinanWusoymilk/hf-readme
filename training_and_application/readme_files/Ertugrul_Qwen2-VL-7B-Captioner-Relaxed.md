---
library_name: transformers
license: apache-2.0
language:
- en
base_model:
- Qwen/Qwen2-VL-7B-Instruct
pipeline_tag: image-to-text
---

# Qwen2-VL-7B-Captioner-Relaxed

## Introduction

Qwen2-VL-7B-Captioner-Relaxed is an instruction-tuned version of [Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct), an advanced multimodal large language model. This fine-tuned version is based on a hand-curated dataset for text-to-image models, providing significantly more detailed descriptions of given images.

### Key Features:

* **Enhanced Detail:** Generates more comprehensive and nuanced image descriptions.
* **Relaxed Constraints:** Offers less restrictive image descriptions compared to the base model.
* **Natural Language Output:** Describes different subjects in the image while specifying their locations using natural language.
* **Optimized for Image Generation:** Produces captions in formats compatible with state-of-the-art text-to-image generation models.

**Note:** This fine-tuned model is optimized for creating text-to-image datasets. As a result, performance on other tasks (e.g., ~10% decrease on mmmu_val) may be lower compared to the original model.

## Requirements

If you encounter errors such as `KeyError: 'qwen2_vl'` or `ImportError: cannot import name 'Qwen2VLForConditionalGeneration' from 'transformers'`, try installing the latest version of the transformers library from source:

`pip install git+https://github.com/huggingface/transformers`

## Quickstart
```python
from PIL import Image
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from transformers import BitsAndBytesConfig
import torch

model_id = "Ertugrul/Qwen2-VL-7B-Captioner-Relaxed"

model = Qwen2VLForConditionalGeneration.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto"
)
processor = AutoProcessor.from_pretrained(model_id)

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



image = Image.open(r"PATH_TO_YOUR_IMAGE")

# you can resize the image here if it's not fitting to vram, or set model max sizes.
# image = image.resize((1024, 1024)) # like this

text_prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)

inputs = processor(
    text=[text_prompt], images=[image], padding=True, return_tensors="pt"
)
inputs = inputs.to("cuda")

with torch.no_grad():
    with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
        output_ids  = model.generate(**inputs, max_new_tokens=384, do_sample=True, temperature=0.7, use_cache=True, top_k=50)


generated_ids = [
    output_ids[len(input_ids) :]
    for input_ids, output_ids in zip(inputs.input_ids, output_ids)
]
output_text = processor.batch_decode(
    generated_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True
)[0]
print(output_text)
```

### Gradio UI

If you prefer no coding option, there's simple gui that allows you to caption selected images. You can find more about it here:

[qwen2vl-captioner-gui](https://github.com/ertugrul-dmr/qwen2vl-captioner-gui)

## Acknowledgements

- Google AI/ML Developer Programs team supported this work by providing Google Cloud Credit

For more detailed options, refer to the [Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct) documentation.
