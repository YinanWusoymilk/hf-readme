---
license: other
license_name: faipl-1.0-sd
license_link: https://freedevproject.org/faipl-1.0-sd/
language:
- en
tags:
  - text-to-image
  - stable-diffusion
  - safetensors
  - stable-diffusion-xl
base_model: cagliostrolab/animagine-xl-3.1
widget:
- text: 1girl, green hair, sweater, looking at viewer, upper body, beanie, outdoors, night, turtleneck, masterpiece, best quality, very aesthetic, absurdres
  parameter:
    negative_prompt: nsfw, low quality, worst quality, very displeasing, 3d, watermark, signature, ugly, poorly drawn
  example_title: 1girl
- text: 1boy, male focus, green hair, sweater, looking at viewer, upper body, beanie, outdoors, night, turtleneck, masterpiece, best quality, very aesthetic, absurdres
  parameter: 
    negative_prompt: nsfw, low quality, worst quality, very displeasing, 3d, watermark, signature, ugly, poorly drawn
  example_title: 1boy
---

<style>

body {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f4f4f9;
  overflow: auto;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 20px;
}

.title-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 1em;
  border-radius: 10px;
}

.title {
  font-size: 3em;
  font-family: 'Montserrat', sans-serif;
  text-align: center;
  font-weight: bold;
}

.title span {
  background: -webkit-linear-gradient(45deg, #0077b6, #00b4d8, #90e0ef);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.gallery {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 10px;
}

.gallery img {
  width: 100%;
  height: auto;
  margin-top: 0px;
  margin-bottom: 0px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s;
}

.gallery img:hover {
  transform: scale(1.05);
}

.note {
  font-size: 1em;
  opacity: 50%;
  text-align: center;
  margin-top: 20px;
  color: #555;
}
  
</style>

<div class="container">
  <div class="title-container">
    <div class="title"><span>Kivotos XL 2.0</span></div>
  </div>
  <div class="gallery">
    <img src="https://huggingface.co/yodayo-ai/kivotos-xl-2.0/resolve/main/samples/sample-001.png" alt="Image 1">
    <img src="https://huggingface.co/yodayo-ai/kivotos-xl-2.0/resolve/main/samples/sample-002.png" alt="Image 2">
    <img src="https://huggingface.co/yodayo-ai/kivotos-xl-2.0/resolve/main/samples/sample-003.png" alt="Image 3">
    <img src="https://huggingface.co/yodayo-ai/kivotos-xl-2.0/resolve/main/samples/sample-004.png" alt="Image 4">
    <img src="https://huggingface.co/yodayo-ai/kivotos-xl-2.0/resolve/main/samples/sample-005.png" alt="Image 5">
    <img src="https://huggingface.co/yodayo-ai/kivotos-xl-2.0/resolve/main/samples/sample-006.png" alt="Image 6">
    <img src="https://huggingface.co/yodayo-ai/kivotos-xl-2.0/resolve/main/samples/sample-007.png" alt="Image 7">
    <img src="https://huggingface.co/yodayo-ai/kivotos-xl-2.0/resolve/main/samples/sample-008.png" alt="Image 8">
    <img src="https://huggingface.co/yodayo-ai/kivotos-xl-2.0/resolve/main/samples/sample-009.png" alt="Image 9">
    <img src="https://huggingface.co/yodayo-ai/kivotos-xl-2.0/resolve/main/samples/sample-010.png" alt="Image 10">
  </div>
  <div class="note">
    Drag and drop each image to <a href="https://huggingface.co/spaces/Linaqruf/pnginfo" target="_blank">this link</a> or use ComfyUI to get the metadata.
  </div>
</div>

## Overview

**Kivotos XL 2.0** is the latest version of the [Yodayo Kivotos XL](https://yodayo.com/models/ee3c3839-e723-45f5-9151-18b592bc93b9) series, following the previous iteration, [Kivotos XL 1.0](https://yodayo.com/models/ee3c3839-e723-45f5-9151-18b592bc93b9/?modelversion=bf0091c7-4337-4edb-8c34-160d647d249a). This open-source model is built upon Animagine XL V3, a specialized SDXL model designed for generating high-quality anime-style artwork. Kivotos XL V2.0 has undergone additional fine-tuning and optimization to focus specifically on generating images that accurately represent the visual style and aesthetics of the Blue Archive franchise. 

## Model Details
- **Developed by**: [Linaqruf](https://github.com/Linaqruf)
- **Model type**: Diffusion-based text-to-image generative model
- **Model Description**: Kivotos XL V2.0, the latest in the Yodayo Kivotos XL series, is an open-source model built on Animagine XL V3. Fine-tuned for high-quality Blue Archive anime-style art generation.
- **License**: [Fair AI Public License 1.0-SD](https://freedevproject.org/faipl-1.0-sd/)
- **Finetuned from model**: [Animagine XL 3.1](https://huggingface.co/cagliostrolab/animagine-xl-3.1)

## Supported Platform
1. Use this model in our platform: [![Open In Spaces](https://img.shields.io/badge/Generate%20in%20Yodayo-141414?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAGtUExURf/JZf/KZf/LZf64aftuevx+dv7DZv/HZvyKc/toe/2wa//KZP/MZPt4d/oIjvQUj7uVmPXKa/6va/ohifsFjcpfmtvGe//JZPtme/QOkGOEz87Hg//JY/2mbfoYi/4Hi5lNuoq/rfUOkF2E08THifoZiplOun6/tF6E0sXHiPUOj16F0sXHif6mbfoYivoIjVyG08TJiP/MYv/NZPYNj4Bpw9Cdiv+fbf2eb/2fb/60av2mbPoLjfIRkfcUjfoUi/oUjPkuh+mBgfgai/sJjf4Ii/8Ii/8Hi+8RkoJpw+galf+5aN5pjJ9Ot5lPuplRupxQuYtawIddwvERke/Ib6XAnY+/qpDAqpDCqo+8q42Zs5lcuNInoPcNjvsKjP8GioxXwHzAtf/KY/++Zv+OcP5Lfv4aiP4Ji+4TkrA+rzKZ6JPBp/61avpEgvoQjP0IjN8empdQu0iL3jaz4X2/tevHcvyYcPoOjP4HjPYOj8kto3hmyTid5EW615TCpt/Gef3JZf+8aO5fhKlGslt71jOq5V2+yLPElPDHb/PHbZW9p4TBsM7FhPrIaP///xdsY3gAAAABYktHRI6CBbNvAAAAB3RJTUUH6AIMCis5IjcvIAAAAE96VFh0UmF3IHByb2ZpbGUgdHlwZSBpcHRjAAB4nOPKLChJ5lIAAyMLLmMLEyMTS5MUAxMgRIA0w2QDI7NUIMvY1MjEzMQcxAfLgEigSi4AKJUO4yoibR8AAAEJSURBVDjLY2AYSoCRiQnOZmJixJRnZmFlg7LZOTi5uNEV8PDy8QsIQvQLCYuIiomjKWCS4JOUkpYBM2Xl5BUUZTAVKCmrQBWoyqupY1EgqaGJX4GWtg5EgS5OE3Twm6BESAHCCj2sCvQlDQyNeIDAGJcJJqZm5hYWFpZW1jgU2Nja2QOBg6OTMxYFPLwurm7yIODu4enljqmA0dvH1w8E/AMCg4LdMBUwcIeEhoWFR0RGRcfExsUnJGIoYBCXkUlKTklNS3d1zcjMysZUALQmJzdPPz+uoLCouKRUHIsCnrLyisqq6prauvoGbPIMjI1NzS2tbe0dMlilQQ7t7Oru6cUpDXUpwxAEACsWOLO6J6SrAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDI0LTAyLTEyVDEwOjQzOjU3KzAwOjAwbykEPgAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyNC0wMi0xMlQxMDo0Mzo1NyswMDowMB50vIIAAAAASUVORK5CYII=)](https://yodayo.com/models/ee3c3839-e723-45f5-9151-18b592bc93b9/?modelversion=f3989e22-5afc-40a1-b435-38eae7760f37)
2. Use it in [`ComfyUI`](https://github.com/comfyanonymous/ComfyUI) or [`Stable Diffusion Webui`](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
3. Use it with 🧨 `diffusers`

## 🧨 Diffusers Installation

First install the required libraries:

```bash
pip install diffusers transformers accelerate safetensors --upgrade
```

Then run image generation with the following example code:

```python
import torch
from diffusers import StableDiffusionXLPipeline

pipe = StableDiffusionXLPipeline.from_pretrained(
    "yodayo-ai/kivotos-xl-2.0", 
    torch_dtype=torch.float16, 
    use_safetensors=True,
    custom_pipeline="lpw_stable_diffusion_xl",
    add_watermarker=False,
    variant="fp16"
)
pipe.to('cuda')

prompt = "1girl, kazusa \(blue archive\), blue archive, solo, upper body, v, smile, looking at viewer, outdoors, night, masterpiece, best quality, very aesthetic, absurdres"
negative_prompt = "nsfw, (low quality, worst quality:1.2), very displeasing, 3d, watermark, signature, ugly, poorly drawn"

image = pipe(
    prompt, 
    negative_prompt=negative_prompt,
    width=832,
    height=1216, 
    guidance_scale=7,
    num_inference_steps=28
).images[0]

image.save("./cat.png")
```

## Usage Guidelines

### Tag Ordering

For optimal results, it's recommended to follow the structured prompt template because we train the model like this:

```
1girl/1boy, character name, from which series, by which artists, everything else in any order.
```

### Special Tags

Kivotos XL 2.0 inherits special tags from Animagine XL 3.1 to enhance image generation by steering results toward quality, rating, creation date, and aesthetic. This inheritance ensures that Kivotos XL 2.0 can produce high-quality, relevant, and aesthetically pleasing images. While the model can generate images without these tags, using them helps achieve better results.

- **Quality tags**: masterpiece, best quality, great quality, good quality, normal quality, low quality, worst quality  
- **Rating tags**: safe, sensitive, nsfw, explicit  
- **Year tags**: newest, recent, mid, early, oldest  
- **Aesthetic tags**: very aesthetic, aesthetic, displeasing, very displeasing

### Recommended Settings

To guide the model towards generating high-aesthetic images, use the following recommended settings:

- **Negative prompts**: 
```
nsfw, (low quality, worst quality:1.2), very displeasing, 3d, watermark, signature, ugly, poorly drawn
```
- **Positive prompts**:
```
masterpiece, best quality, very aesthetic, absurdres
```
- **Classifier-Free Guidance (CFG) Scale**: should be around 5 to 7; 10 is fried, >12 is deep-fried.
- **Sampling steps**: should be around 25 to 30; 28 is the sweet spot.
- **Sampler**: Euler Ancestral (Euler a) is highly recommended.
- **Supported resolutions**:
```
1024 x 1024, 1152 x 896, 896 x 1152, 1216 x 832, 832 x 1216, 1344 x 768, 768 x 1344, 1536 x 640, 640 x 1536
```

## Training 

These are the key hyperparameters used during training:

| Feature                       | Pretraining               | Finetuning                      |
|-------------------------------|----------------------------|---------------------------------|
| **Hardware**                  | 2x H100 80GB PCIe          | 1x A100 80GB PCIe               |
| **Batch Size**                | 32                         | 48                              |
| **Gradient Accumulation Steps** | 2                        | 1                               |
| **Noise Offset**              | None                       | 0.0357                          |
| **Epochs**                    | 10                         | 10                              |
| **UNet Learning Rate**        | 5e-6                       | 3.75e-6                         |
| **Text Encoder Learning Rate** | 2.5e-6                   | None                            |
| **Optimizer**                 | Adafactor                  | Adafactor                       |
| **Optimizer Args**            | Scale Parameter: False, Relative Step: False, Warmup Init: False (0.9, 0.99) | Scale Parameter: False, Relative Step: False, Warmup Init: False |
| **Scheduler**                 | Constant with Warmups      | Constant with Warmups           |
| **Warmup Steps**              | 0.05%                       | 0.05%                            |

## License

Kivotos XL 2.0 falls under [Fair AI Public License 1.0-SD](https://freedevproject.org/faipl-1.0-sd/) license, which is compatible with Stable Diffusion models’ license. Key points:

1. **Modification Sharing:** If you modify Kivotos XL 2.0, you must share both your changes and the original license.
2. **Source Code Accessibility:** If your modified version is network-accessible, provide a way (like a download link) for others to get the source code. This applies to derived models too.
3. **Distribution Terms:** Any distribution must be under this license or another with similar rules.
