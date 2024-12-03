---
tags:
- text-to-image
- flux
- lora
- diffusers
- replicate
pipeline_tag: text-to-image
thumbnail: "https://cdn-uploads.huggingface.co/production/uploads/633792e60578e2c92edffc1e/dNdc3ktAsZVsS6eVsqnJx.webp"
widget:
- text: In the style of TOK, a photo editorial avant-garde dramatic action pose of a woman short blue hair wearing 70s round wacky sunglasses pulling glasses down looking forward, in Tokyo with large marble structures and bonsai trees at sunset with a vibrant illustrated jacket surrounded by illustrations of flowers, smoke, flames, ice cream, sparkles, rock and roll 
  output:
    url: images/example1.webp
- text: In the style of TOK, a photo editorial avant-garde dramatic action pose of a person wearing 90s round wacky sunglasses pulling glasses down looking forward, in Tokyo with large marble structures and bonsai trees at sunset with a vibrant illustrated jacket surrounded by illustrations of flowers, smoke, flames, ice cream, sparkles, rock and roll 
  output:
    url: images/example2.webp
- text: In the style of TOK, a photo editorial avant-garde dramatic action pose of a person wearing 90s round wacky sunglasses pulling glasses down looking forward, in Seattle at sunset with a vibrant illustrated jacket surrounded by illustrations of flowers, smoke, flames, ice cream, sparkles, rock and roll
  output:
    url: images/example3.webp
- text: In the style of TOK, a photo editorial dramatic action pose of a person piercing eyes, tattoos on face, with creative bucket hat, standing in Tokyo with large marble structures and white purple trees in a Basketball court, with a vibrant illustrated street wear puffy vintage jacket, black shirt, volcano in the background, surrounded by illustrations of smoke, flames, and flowers, fog, exclamation marks, lines shooting outwards, minion characters, butterflies 
  output:
    url: images/example5.webp
- text: In the style of TOK, a photo editorial dramatic action pose of a person with mirrored lenses with creative bucket hat, standing in Tokyo with large marble structures and white purple trees in a Basketball court, with a vibrant illustrated street wear puffy architectural leather jacket surrounded by illustrations of smoke, flames, birds, and flowers, fog, exclamation mark, lines shooting outwards, ascii characters
  output:
    url: images/example7.webp
base_model: black-forest-labs/FLUX.1-dev
instance_prompt: in the style of TOK
license: other
license_name: flux-dev-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
---
# Create unique half illustrated, half photo images

<Gallery />

## Model description 

Flux Dev 1 model that creates images with both photographic and illustrative elements. Pretty cool right? You can also run the model on Replicate. Let me know your thoughts and have a wonderful day!

https://replicate.com/davisbrown/flux-half-illustration


## Trigger words

It would help if you used `in the style of TOK` for better style preservation. It is best to place the trigger words first and describe illustrative elements in your scene like clothing or expressive elements.

# Flux Multi Angle

Trained on Replicate using:
https://replicate.com/ostris/flux-dev-lora-trainer/train

## Download model

[Download the *.safetensors LoRA](https://huggingface.co/davisbro/half_illustration/tree/main) in the Files & versions tab.

## Use it with the [🧨 diffusers library](https://github.com/huggingface/diffusers)

```py
from diffusers import AutoPipelineForText2Image
import torch
pipeline = AutoPipelineForText2Image.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16).to('cuda')
pipeline.load_lora_weights('davisbro/half_illustration', weight_name='flux_train_replicate.safetensors')
image = pipeline('A 50mm bokeh photo of a fashion show in paris, midday sun, surrounded by the colorful friendly rock and roll text "Paris" and other french themed doodles').images[0]
```

For more details, including weighting, merging and fusing LoRAs, check the [documentation on loading LoRAs in diffusers](https://huggingface.co/docs/diffusers/main/en/using-diffusers/loading_adapters)

## License

Please adhere to the licensing terms as described [here](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md).