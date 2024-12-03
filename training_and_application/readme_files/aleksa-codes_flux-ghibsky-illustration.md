---
tags:
- text-to-image
- diffusers
- lora
- template:sd-lora
- image-generation
- flux
- replicate
pipeline_tag: text-to-image
thumbnail: >-
  https://tjzk.replicate.delivery/models_models_cover_image/e5bc70de-c6ae-497f-bf2c-7e81b1183f05/out-0.jpg
widget:
- text: >-
    GHIBSKY style, a cat on a windowsill gazing out at a starry night sky and
    distant city lights
  output:
    url: images/example1.jpg
- text: >-
    GHIBSKY style, a fisherman casting a line into a peaceful village lake
    surrounded by quaint cottages
  output:
    url: images/example2.jpg
- text: >-
    GHIBSKY style, cozy mountain cabin covered in snow, with smoke curling from
    the chimney and a warm, inviting light spilling through the windows
  output:
    url: images/example3.jpg
- text: GHIBSKY style, Mykonos
  output:
    url: images/example4.jpg
- text: >-
    GHIBSKY style, an orange Lamborghini driving down a hill road at night with
    a beautiful ocean view in the background, side view, no text
  output:
    url: images/example5.jpg
- text: >-
    GHIBSKY style, a small Yorkie on a windowsill during a snowy winter night,
    with a warm, cozy glow from inside and soft snowflakes drifting outside
  output:
    url: images/example6.jpg
- text: >-
    GHIBSKY style, serene Japanese garden with a koi pond and a traditional tea
    house, nestled under a canopy of cherry blossoms in full bloom
  output:
    url: images/example7.jpg
- text: GHIBSKY style, the most beautiful place in the universe
  output:
    url: images/example8.jpg
base_model: black-forest-labs/FLUX.1-dev
instance_prompt: GHIBSKY style
license: other
license_name: flux-dev-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
---

# Flux Ghibsky Illustration: Create Serene and Enchanting Landscapes

<Gallery />

## Model Description

The Flux Ghibsky Illustration model generates landscapes that blend serene, surreal skies with intricate, Ghibli-inspired details. This fusion of styles creates enchanting scenes that capture the essence of both Ghibli's whimsical charm and Makoto Shinkai's atmospheric beauty. Perfect for creating dreamy visuals. You can also run the model on Replicate. Feedback is welcome!

[Replicate Model Page](https://replicate.com/aleksa-codes/flux-ghibsky-illustration)

## Trigger Words

Use `GHIBSKY style` to invoke the model’s unique aesthetic. It’s best to start your prompt with the trigger word, followed by descriptions of your scene, such as nature, skies, houses, roads, villages, etc.

If you are getting too realistic images try adding `painting` to your prompt, for example: `GHIBSKY style painting`

## Training Details

- **Trained Using**: [ostris/flux-dev-lora-trainer](https://replicate.com/ostris/flux-dev-lora-trainer/train)
- **Number of Images**: 35
- **Trigger Word**: GHIBSKY
- **Auto-captioning**: Enabled
- **Auto-captioning Prefix**: “”
- **Auto-captioning Suffix**: “, GHIBSKY style”
- **Training Steps**: 1000
- **Learning Rate**: 0.0004
- **Batch Size**: 1
- **LoRA Rank**: 16

## Download Model

[Download the *.safetensors LoRA](https://huggingface.co/aleksa-codes/flux-ghibsky-illustration/tree/main) in the Files & versions tab.

## Use it with the [🧨 diffusers library](https://github.com/huggingface/diffusers)

```py
from diffusers import AutoPipelineForText2Image
import torch
pipeline = AutoPipelineForText2Image.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16).to('cuda')
pipeline.load_lora_weights('aleksa-codes/flux-ghibsky-illustration', weight_name='lora.safetensors')
image = pipeline('GHIBSKY style, a serene lakeside village with colorful houses and towering mountains under a dreamy sky').images[0]
```

For more details, including weighting, merging, and fusing LoRAs, check the [documentation on loading LoRAs in diffusers](https://huggingface.co/docs/diffusers/main/en/using-diffusers/loading_adapters).

## License

Please adhere to the licensing terms as described [here](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md).