---
tags:
- text-to-image
- flux
- lora
- diffusers
- template:sd-lora
widget:
- text: >-
    a coca cola can "sacred elixir" arcana in the style of TOK a trtcrd, tarot
    style
  output:
    url: >-
      images/7e180627edd846e899b6cd307339140d_5b2a09f0842c476b83b6bd2cb9143a52.png
- text: >-
    a person giving a ted talk on a TED stage with the TED logo, "the speaker"
    in the style of TOK a trtcrd, tarot style
  output:
    url: >-
      images/e04f78fe65274f8d8db2598693ab9300_4a6c854c99534da9a878b0ce7940e146.png
- text: >-
    a trtcrd of a person on a computer, on the computer you see a meme being
    made with an ancient looking trollface, "the shitposter" arcana, in the
    style of TOK a trtcrd, tarot style
  output:
    url: >-
      images/e5f2761e5d474e6ba492d20dca0fa26f_e78f1524074b42b6ac49643ffad50ac6.png
- text: a work cubicle in the style of TOK a trtcrd, tarot style
  output:
    url: >-
      images/05732ed81b2a44b5a27a3281b298fe2a_a35e6d1091924b65bb751e2156ede234.png
- text: a dog eating pasta, in the style of TOK a trtcrd, tarot style
  output:
    url: >-
      images/a1a8466576514faa9119fab78d7aa4a2_fba6e09c329a49a2b5fcf57ec29a8d56.png
- text: >-
    a man cutting meat from a kebab vertical rotisserie, it reads "Döner" in the
    style of TOK a trtcrd, tarot style
  output:
    url: >-
      images/1c3e07c46cb341caa96fe668a4bb1777_025eb7c596fe4c2da20958b4f07418ef.png
base_model: black-forest-labs/FLUX.1-dev
instance_prompt: in the style of TOK a trtcrd tarot style
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
inference:
  parameters:
    width: 768
    height: 1024
datasets:
- multimodalart/1920-raider-waite-tarot-public-domain
---
# FLUX Tarot v1

<Gallery />

## Model description 

A tarot card LoRA trained with the public domain card set of Raider Waite 1920. [Dataset](https:&#x2F;&#x2F;huggingface.co&#x2F;datasets&#x2F;multimodalart&#x2F;1920-raider-waite-tarot-public-domain)

Trained with [fal-ai trainer](https://fal.ai/models/fal-ai/flux-lora-general-training?a=1) based on the open source trainer [ostris AI Toolkit](https://github.com/ostris/ai-toolkit).

## Trigger words

You should use `in the style of TOK a trtcrd tarot style` to trigger the image generation.

## Download model

Weights for this model are available in Safetensors format.

[Download](/multimodalart/flux-tarot-v1/tree/main) them in the Files & versions tab.

## Use it with the [🧨 diffusers library](https://github.com/huggingface/diffusers)

```py
from diffusers import AutoPipelineForText2Image
import torch

pipeline = AutoPipelineForText2Image.from_pretrained('black-forest-labs/FLUX.1-dev', torch_dtype=torch.bfloat16).to('cuda')
pipeline.load_lora_weights('multimodalart/flux-tarot-v1', weight_name='flux_tarot_v1_lora.safetensors')
image = pipeline('in the style of TOK a trtcrd tarot style').images[0]
```