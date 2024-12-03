---
license: other
license_name: tongyi-qianwen
base_model: Qwen/Qwen2-72B
tags:
- generated_from_trainer
- axolotl
datasets:
- cognitivecomputations/Dolphin-2.9
- teknium/OpenHermes-2.5
- m-a-p/CodeFeedback-Filtered-Instruction
- cognitivecomputations/dolphin-coder
- cognitivecomputations/samantha-data
- microsoft/orca-math-word-problems-200k
- Locutusque/function-calling-chatml
- internlm/Agent-FLAN
---

# DolphinVision 72b 🐬

Curated and trained by Quan Nguyen (qnguyen3/stablequan), Eric Hartford, and Cognitive Computations

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/h3K4XGj2RH)
Discord: https://discord.gg/h3K4XGj2RH

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/DBGu4dJ95RHHN3yOEuXuP.png" width="600" />

Our appreciation for the sponsors of DolphinVision:
- [Crusoe Cloud](https://crusoe.ai/) - provided excellent on-demand 8xH100 node used for training
- [TensorWave](https://tensorwave.com/) - provided 8x mi300x node used for evaluations and inference

DolphinVision is a multimodal model.  It is uncensored, and capable to reason and comment regarding images that other popular models would object to.


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

model_name = 'cognitivecomputations/dolphin-vision-72b'

# create model
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map='auto',
    trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
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

## Examples

![image/png](https://cdn-uploads.huggingface.co/production/uploads/630430583926de1f7ec62c6b/TFl5SJ4o3v-hKIqA82_qA.png)
```
<|im_start|>user
: do OCR on all the text
<|im_start|>assistant
: The text in the image reads as follows:

- STOP USING DOCKER
- Applications were not meant to be trapped in virtual jars like digital fireflies
- Years of software development, yet no one questioned why we were putting programs in imaginary boats
- Let's containerize our monolith. I'll just quickly spin up 17 microservices. Statements dreamt up by the utterly deranged
- Observe the whale-sized deception they fooled us with all this time
- These are real images used to explain Docker
- "Yay Matey, I'd like to run my website in a virtual sea"
- They have played us for absolute fools

This text is a satirical commentary on the use of Docker in software development, using humor and exaggeration to question the practice.
```

## Benchmarks

| Model   | **VQA v2** | **MMBench** | **MMMU (Eval)** | **MathVista**  | **RealWorldQA** |
|---------|--------|---------|------------|------|--------|
| Dolphin-Vision-72B   | 83.6  | 81.2 | 45.7| 47.25| 66.4   |
| GPT-4V               | 84.4  | 78.1 | 52.4| -| 67.9   |