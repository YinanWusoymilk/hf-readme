---
tags:
- text-to-image
- stable-diffusion
- lora
- diffusers
- template:sd-lora
widget:
- text: a bottle of water with the text "clean" on it,  flmft photo style
  output:
    url: images/ComfyUI_00240_.png
- text: a fluffy white kitten,  flmft photo style
  output:
    url: images/ComfyUI_00236_.png
- text: a man,  flmft photo style
  output:
    url: images/ComfyUI_00230_.png
- text: a gray day with mt fuji in the distance, flmft photo style
  output:
    url: images/ComfyUI_00242_ (1).png
- text: a celestial being,  flmft photo style
  output:
    url: images/ComfyUI_00244_.png
- text: a japanese woman with a bit smile,  flmft photo style
  output:
    url: images/ComfyUI_00247_.png
- text: >-
    a messy desk with an pile of old cassette tapes from different indie bands
    with scrawled labels on them, still life, flmft photo style
  output:
    url: images/ComfyUI_00253_ (1).png
base_model: black-forest-labs/FLUX.1-dev
instance_prompt: flmft photo style
license: creativeml-openrail-m
---
# Flux Film Foto

<Gallery />

## Model description 

Here is my first crack at a realism Flux model, and I guess the first realism model I&#39;ve ever shared publicly.

All the training data was opensource&#x2F;open license photographs. I do intend to revisit it and expand and improve on it. It can benefit from emphasizing the style by adding &quot;vintage&quot; or &quot;faded film&quot; to the prompt.

Big appreciation to Glif for sponsoring the model!

![ComfyUI_00269_ (1).png](https:&#x2F;&#x2F;cdn-uploads.huggingface.co&#x2F;production&#x2F;uploads&#x2F;635dd6cd4fabde0df74aeae6&#x2F;EgWqu_KaeVTJHRiOJ6yQe.png)

## Trigger words

You should use `flmft photo style` to trigger the image generation.


## Download model

Weights for this model are available in Safetensors format.

[Download](/alvdansen/flux_film_foto/tree/main) them in the Files & versions tab.
