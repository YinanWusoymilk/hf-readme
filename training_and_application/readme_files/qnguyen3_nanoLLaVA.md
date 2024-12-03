---
language:
- en
tags:
- llava
- multimodal
- qwen
license: apache-2.0
---
# nanoLLaVA - Sub 1B Vision-Language Model

<p align="center">
  <img src="https://i.postimg.cc/d15k3YNG/nanollava.webp" alt="Logo" width="350">
</p>

## Description
nanoLLaVA is a "small but mighty" 1B vision-language model designed to run efficiently on edge devices.
- **Base LLM**: [Quyen-SE-v0.1](https://huggingface.co/vilm/Quyen-SE-v0.1) (Qwen1.5-0.5B)
- **Vision Encoder**: [google/siglip-so400m-patch14-384](https://huggingface.co/google/siglip-so400m-patch14-384)

| Model   | **VQA v2** | **TextVQA** | **ScienceQA** | **POPE** | **MMMU (Test)** | **MMMU (Eval)** | **GQA**  | **MM-VET** |
|---------|--------|---------|-----------|------|-------------|-------------|------|--------|
| Score   | 70.84  | 46.71   | 58.97     | 84.1 | 28.6        | 30.4        | 54.79| 23.9   |

## Training Data
Training Data will be released later as I am still writing a paper on this. Expect the final final to be much more powerful than the current one.

## Finetuning Code
Coming Soon!!!

## Usage
You can use with `transformers` with the following script:

```bash
pip install -U transformers accelerate flash_attn
```

```python
import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import warnings

# disable some warnings
transformers.logging.set_verbosity_error()
transformers.logging.disable_progress_bar()
warnings.filterwarnings('ignore')

# set device
torch.set_default_device('cuda')  # or 'cpu'

# create model
model = AutoModelForCausalLM.from_pretrained(
    'qnguyen3/nanoLLaVA',
    torch_dtype=torch.float16,
    device_map='auto',
    trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(
    'qnguyen3/nanoLLaVA',
    trust_remote_code=True)

# text prompt
prompt = 'Describe this image in detail'

messages = [
    {"role": "user", "content": f'<image>\n{prompt}'}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

print(text)

text_chunks = [tokenizer(chunk).input_ids for chunk in text.split('<image>')]
input_ids = torch.tensor(text_chunks[0] + [-200] + text_chunks[1], dtype=torch.long).unsqueeze(0)

# image, sample images can be found in images folder
image = Image.open('/path/to/image.png')
image_tensor = model.process_images([image], model.config).to(dtype=model.dtype)

# generate
output_ids = model.generate(
    input_ids,
    images=image_tensor,
    max_new_tokens=2048,
    use_cache=True)[0]

print(tokenizer.decode(output_ids[input_ids.shape[1]:], skip_special_tokens=True).strip())
```

## Prompt Format
The model follow the ChatML standard, however, without `\n` at the end of `<|im_end|>`:
```
<|im_start|>system
Answer the question<|im_end|><|im_start|>user
<image>
What is the picture about?<|im_end|><|im_start|>assistant
```

---
| Image                                | Example                                                                                     |
|--------------------------------------|---------------------------------------------------------------------------------------------|
| ![small](example_1.png)              | **What is the text saying?** <br> "Small but mighty". <br>**How does the text correlate to the context of the image?** <br> The text seems to be a playful or humorous representation of a small but mighty figure, possibly a mouse or a mouse toy, holding a weightlifting bar. |
---

Model is trained using a modified version from [Bunny](https://github.com/BAAI-DCAI/Bunny/tree/main/bunny)