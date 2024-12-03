---
tags:
- text-to-image
- stable-diffusion
- lora
- diffusers
- template:sd-lora
widget:
- text: v3ct0r style, simple flat vector art, isolated on white bg, cat
  output:
    url: images/ComfyUI_09405_.jpeg
- text: v3ct0r style, simple flat vector art, isolated on white bg, rocket
  output:
    url: images/ComfyUI_09420_.jpeg
- text: v3ct0r style, simple flat vector art, isolated on white bg, clown
  output:
    url: images/ComfyUI_09424_.jpeg
- text: >-
    v3ct0r style, simple vector art, isolated on white bg, construction worker
    wearing a hard hat and holding a small clipboard, character asset, clip art
    - The text on the clipboard says "FLUX TEST"
  output:
    url: images/ComfyUI_09445_.jpeg
- text: >-
    v3ct0r style, simple vector art, isolated on white bg, salesman giving a
    thumbs up in front of a car, character asset, clip art
  output:
    url: images/ComfyUI_09459_.jpeg
- text: >-
    v3ct0r style, simple vector art, isolated on white bg, ugly witch standing
    next to a bubbling cauldron stirring the pot, character asset, clip art
  output:
    url: images/ComfyUI_09463_.jpeg
- text: >-
    v3ct0r style, simple vector art, isolated on white bg, xmas tree with
    beautifully wrapped gifts beneath it, character asset, clip art
  output:
    url: images/ComfyUI_09465_.jpeg
- text: >-
    v3ct0r style, simple vector art, isolated on white bg, tall cartoon style
    box truck side view, clip art
  output:
    url: images/ComfyUI_09466_.jpeg
- text: >-
    v3ct0r style, simple vector art, isolated on white bg, a boy holding up a
    big gold coin with an orange lightning bolt embossed on the coin, character
    asset, clip art
  output:
    url: images/ComfyUI_09477_.jpeg
- text: >-
    v3ct0r style, simple flat vector art, isolated on white bg, a piglet solving
    a puzzle
  output:
    url: images/example_zyptz08kz.png
- text: >-
    v3ct0r style, simple vector art, isolated on white bg, doctor smiling,
    character asset, clip art
  output:
    url: images/example_rjpji72qt.png
base_model: black-forest-labs/FLUX.1-dev
instance_prompt: v3ct0r, vector
license: creativeml-openrail-m

---
# Simple Vector Flux LoRA

<Gallery />

## Model description 

Simple Vector Flux was trained on a curated dataset of ~50 synthetic images in classic vector style, 17 epochs, 2 repeats, ~1700 steps.

This is a work in progress and it can be a little temperamental, the captioning was done using Joy Caption Batch with the trigger &quot;v3ct0r&quot; and &quot;vector&quot; in the prefix of the captions.

You have to work a little bit to get desired results and sometimes there is bleeding&#x2F;blending of subjects but overall the style is present and the results can be really good. This LoRA takes a couple of tries adjusting your prompt and adding tokens to match the style. 

## Trigger words

You should use `v3ct0r` to trigger the image generation.

You should use `vector` to trigger the image generation.


## Download model

Weights for this model are available in Safetensors format.

[Download](/renderartist/simplevectorflux/tree/main) them in the Files & versions tab.
