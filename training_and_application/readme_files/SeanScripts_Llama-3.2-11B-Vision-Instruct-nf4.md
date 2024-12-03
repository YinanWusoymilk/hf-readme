---
license: llama3.2
base_model:
- meta-llama/Llama-3.2-11B-Vision-Instruct
pipeline_tag: image-text-to-text
library_name: transformers
---

Converted from [meta-llama/Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) using BitsAndBytes with NF4 (4-bit) quantization. Not using double quantization.
Requires `bitsandbytes` to load.

Example usage for image captioning:
```python
from transformers import MllamaForConditionalGeneration, AutoProcessor, BitsAndBytesConfig
from PIL import Image
import time

# Load model
model_id = "SeanScripts/Llama-3.2-11B-Vision-Instruct-nf4"
model = MllamaForConditionalGeneration.from_pretrained(
    model_id,
    use_safetensors=True,
    device_map="cuda:0"
)
# Load tokenizer
processor = AutoProcessor.from_pretrained(model_id)

# Caption a local image (could use a more specific prompt)
IMAGE = Image.open("test.png").convert("RGB")
PROMPT = """<|begin_of_text|><|start_header_id|>user<|end_header_id|>
Caption this image:
<|image|><|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""

inputs = processor(IMAGE, PROMPT, return_tensors="pt").to(model.device)
prompt_tokens = len(inputs['input_ids'][0])
print(f"Prompt tokens: {prompt_tokens}")

t0 = time.time()
generate_ids = model.generate(**inputs, max_new_tokens=256)
t1 = time.time()
total_time = t1 - t0
generated_tokens = len(generate_ids[0]) - prompt_tokens
time_per_token = generated_tokens/total_time
print(f"Generated {generated_tokens} tokens in {total_time:.3f} s ({time_per_token:.3f} tok/s)")

output = processor.decode(generate_ids[0][prompt_tokens:]).replace('<|eot_id|>', '')
print(output)

```

You can get a set of ComfyUI custom nodes for running this model here:
[https://github.com/SeanScripts/ComfyUI-PixtralLlamaVision](https://github.com/SeanScripts/ComfyUI-PixtralLlamaVision)