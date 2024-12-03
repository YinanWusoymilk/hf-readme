---
license: apache-2.0
language:
- en
base_model:
- openai/clip-vit-large-patch14-336
- allenai/OLMoE-1B-7B-0924
datasets:
- allenai/OLMoE-mix-0924
pipeline_tag: image-text-to-text
tags:
- multimodal
- moe
- olmo
- olmoe
- molmo
- molmoe
library_name: transformers
---

<img src="molmo_logo.png" alt="Logo for the Molmo Project" style="width: auto; height: 50px;">

# MolmoE 1B


Molmo is a family of open vision-language models developed by the Allen Institute for AI. 
Molmo models are trained on PixMo, a dataset of 1 million, highly-curated image-text pairs. 
It has state-of-the-art performance among multimodal models with a similar size while being fully open-source. 
You can find all models in the Molmo family [here](https://huggingface.co/collections/allenai/molmo-66f379e6fe3b8ef090a8ca19).
**Learn more** about the Molmo family [in our announcement blog post](https://molmo.allenai.org/blog) or the [paper](https://huggingface.co/papers/2409.17146).

MolmoE-1B is a multimodal Mixture-of-Experts LLM with 1.5B active and 7.2B total parameters based on [OLMoE-1B-7B-0924](https://huggingface.co/allenai/OLMoE-1B-7B-0924). 
It nearly matches the performance of GPT-4V on both academic benchmarks and human evaluation, and achieves state-of-the-art performance among similarly-sized open multimodal models.

This checkpoint is a **preview** of the Molmo release. All artifacts used in creating Molmo (PixMo dataset, training code, evaluations, intermediate checkpoints) will be made available at a later date, furthering our commitment to open-source AI development and reproducibility.

**[Sign up here](https://docs.google.com/forms/d/e/1FAIpQLSdML1MhNNBDsCHpgWG65Oydg2SjZzVasyqlP08nBrWjZp_c7A/viewform)** to be the first to know when artifacts are released.

Quick links:
- 💬 [Demo](https://molmo.allenai.org/)
- 📂 [All Models](https://huggingface.co/collections/allenai/molmo-66f379e6fe3b8ef090a8ca19)
- 📃 [Paper](https://molmo.allenai.org/paper.pdf)
- 🎥 [Blog with Videos](https://molmo.allenai.org/blog)

## Quick Start

To run MolmoE, first install dependencies:

```bash
pip install einops torchvision
```

Then, follow these steps:

```python
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig
from PIL import Image
import requests

# load the processor
processor = AutoProcessor.from_pretrained(
    'allenai/MolmoE-1B-0924',
    trust_remote_code=True,
    torch_dtype='auto',
    device_map='auto'
)

# load the model
model = AutoModelForCausalLM.from_pretrained(
    'allenai/MolmoE-1B-0924',
    trust_remote_code=True,
    torch_dtype='auto',
    device_map='auto'
)

# process the image and text
inputs = processor.process(
    images=[Image.open(requests.get("https://picsum.photos/id/237/536/354", stream=True).raw)],
    text="Describe this image."
)

# move inputs to the correct device and make a batch of size 1
inputs = {k: v.to(model.device).unsqueeze(0) for k, v in inputs.items()}

# generate output; maximum 200 new tokens; stop generation when <|endoftext|> is generated
output = model.generate_from_batch(
    inputs,
    GenerationConfig(max_new_tokens=200, stop_strings="<|endoftext|>"),
    tokenizer=processor.tokenizer
)

# only get generated tokens; decode them to text
generated_tokens = output[0,inputs['input_ids'].size(1):]
generated_text = processor.tokenizer.decode(generated_tokens, skip_special_tokens=True)

# print the generated text
print(generated_text)

# >>> This photograph captures a small black puppy, likely a Labrador or a similar breed,
#     sitting attentively on a weathered wooden deck. The deck, composed of three...
```

## Evaluations

| Model                       | Average Score on 11 Academic Benchmarks | Human Preference Elo Rating |
|-----------------------------|-----------------------------------------|-----------------------------|
| Molmo 72B                   | 81.2                                    | 1077                        |
| Molmo 7B-D                  | 77.3                                    | 1056                        |
| Molmo 7B-O                  | 74.6                                    | 1051                        |
| **MolmoE 1B (this model)**  | **68.6**                                | **1032**                    |
| GPT-4o                      | 78.5                                    | 1079                        |
| GPT-4V                      | 71.1                                    | 1041                        |
| Gemini 1.5 Pro              | 78.3                                    | 1074                        |
| Gemini 1.5 Flash            | 75.1                                    | 1054                        |
| Claude 3.5 Sonnet           | 76.7                                    | 1069                        |
| Claude 3 Opus               | 66.4                                    |  971                        |
| Claude 3 Haiku              | 65.3                                    |  999                        |
| Qwen VL2 72B                | 79.4                                    | 1037                        |
| Qwen VL2 7B                 | 73.7                                    | 1025                        |
| Intern VL2 LLAMA 76B        | 77.1                                    | 1018                        |
| Intern VL2 8B               | 69.4                                    |  953                        |
| Pixtral 12B                 | 69.5                                    | 1016                        |
| Phi3.5-Vision 4B            | 59.7                                    |  982                        |
| PaliGemma 3B                | 50.0                                    |  937                        |
| LLAVA OneVision 72B         | 76.6                                    | 1051                        |
| LLAVA OneVision 7B          | 72.0                                    | 1024                        |
| Cambrian-1 34B              | 66.8                                    |  953                        |
| Cambrian-1 8B               | 63.4                                    |  952                        |
| xGen - MM - Interleave 4B   | 59.5                                    |  979                        |
| LLAVA-1.5 13B               | 43.9                                    |  960                        |
| LLAVA-1.5 7B                | 40.7                                    |  951                        |

*Benchmarks: AI2D test, ChartQA test, VQA v2.0 test, DocQA test, InfographicVQA test, TextVQA val, RealWorldQA, MMMU val, MathVista testmini, CountBenchQA, Flickr Count (we collected this new dataset that is significantly harder than CountBenchQA).*


## FAQs

### I'm getting an error a broadcast error when processing images!

Your image might not be in RGB format. You can convert it using the following code snippet:

```python
from PIL import Image

image = Image.open(...)

if image.mode != "RGB":
    image = image.convert("RGB")
```

### Molmo doesn't work great with transparent images!

We received reports that Molmo models might struggle with transparent images. 
For the time being, we recommend adding a white or dark background to your images before passing them to the model. The code snippet below shows how to do this using the Python Imaging Library (PIL):

```python

# Load the image
url = "..."
image = Image.open(requests.get(url, stream=True).raw)

# Convert the image to grayscale to calculate brightness
gray_image = image.convert('L')  # Convert to grayscale

# Calculate the average brightness
stat = ImageStat.Stat(gray_image)
average_brightness = stat.mean[0]  # Get the average value

# Define background color based on brightness (threshold can be adjusted)
bg_color = (0, 0, 0) if average_brightness > 127 else (255, 255, 255)

# Create a new image with the same size as the original, filled with the background color
new_image = Image.new('RGB', image.size, bg_color)

# Paste the original image on top of the background (use image as a mask if needed)
new_image.paste(image, (0, 0), image if image.mode == 'RGBA' else None)

# Now you can pass the new_image to Molmo
processor = AutoProcessor.from_pretrained(
    'allenai/Molmo-7B-D-0924',
    trust_remote_code=True,
    torch_dtype='auto',
    device_map='auto'
)
```

## License and Use

This model is licensed under Apache 2.0. It is intended for research and educational use.
For more information, please see our [Responsible Use Guidelines](https://allenai.org/responsible-use).