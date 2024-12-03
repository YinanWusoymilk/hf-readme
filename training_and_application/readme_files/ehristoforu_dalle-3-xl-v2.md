---
tags:
- text-to-image
- safetensors
- stable-diffusion
- lora
- diffusers
- dalle-3
- dalle
- deepvision
- template:sd-lora
widget:
- text: >-
    The image is a 3D render of a green dinosaur named Yoshi from the Mario
    series. Yoshi is standing on a brick street in a town and is holding a sign
    that says "Feed me please!" in capital white letters. Yoshi has a white
    belly, orange shoes, and a brown shell with orange spots. He is looking at
    the camera with a hopeful expression on his face. The background of the
    image is slightly blurred and shows a building with large windows behind
    Yoshi. The image is well-lit, and the colors are vibrant,
    <lora:dalle-3-xl-lora-v2:0.8>
  output:
    url: images/v2-1.png
- text: >-
    The image is a 3D rendering of a cartoon fox wearing aviator goggles and a
    scarf sitting on a mossy tree stump in a forest. The fox has bright orange
    fur, white paws and underbelly, and dark brown eyes. The goggles are brown
    and have a light blue tint. The scarf is dark brown and has a light brown
    buckle. The tree stump is dark brown and has a light green moss growing on
    it. The forest is green and lush, with tall trees and a variety of shrubs
    and plants. The sun is shining brightly through the trees, creating a
    dappled pattern of light and shadow on the ground. The fox is sitting in a
    relaxed pose, with its head tilted slightly to the left and its eyes looking
    up at the viewer. The image is rendered in a realistic style, with soft
    lighting and detailed textures. <lora:dalle-3-xl-lora-v2:0.8>
  output:
    url: images/v2-2.png
- text: >-
    The image is of Shadow the Hedgehog, a character from the Sonic the Hedgehog
    series. He is standing on a rock in front of a ruined city. He is wearing
    his signature black and red outfit and has his arms crossed. He has a smug
    expression on his face. The city is in ruins, with buildings destroyed and
    debris everywhere. The sky is dark and cloudy. The image is rendered in a
    realistic style. Shadow is a black hedgehog with red stripes on his head and
    arms. He has yellow eyes and a white muzzle. He is wearing black boots with
    red soles and white gloves. He is standing on a large rock in the middle of
    a ruined city. The city is in ruins, with buildings destroyed and debris
    everywhere. The sky is dark and cloudy. Shadow is looking at the camera with
    a smug expression on his face., <lora:dalle-3-xl-lora-v2:0.8>
  output:
    url: images/v2-3.png
- text: >-
    The image is an illustration of the character Goku from the anime series
    Dragon Ball Z. He is standing in a powered-up state with his hair spiked up
    and surrounded by blue lightning. He is wearing his orange and blue gi with
    a white belt and boots. His expression is serious and determined. The
    background is a dark blue void with bright white lightning bolts. The image
    is in a 3D rendered anime style, <lora:dalle-3-xl-lora-v2:0.8>
  output:
    url: images/v2-4.png
base_model: fluently/Fluently-XL-v2
instance_prompt: <lora:dalle-3-xl-lora-v2:0.8>
license: creativeml-openrail-m
library_name: diffusers
datasets:
- ehristoforu/dalle-3-images
pipeline_tag: text-to-image
---
# DALL•E 3 XL LoRA v2

<Gallery />

## Model description 

This is a test model very similar to Dall•E 3.

## Official demo

You can use official demo on Spaces: [try](https://huggingface.co/spaces/ehristoforu/dalle-3-xl-lora-v2).

## Trigger words

You should use `<lora:dalle-3-xl-lora-v2:0.8>` to trigger the image generation.


## Download model

Weights for this model are available in Safetensors format.

[Download](/ehristoforu/dalle-3-xl-v2/tree/main) them in the Files & versions tab.