---
tags:
- flux
- text-to-image
- lora
- diffusers
- fal
base_model: black-forest-labs/FLUX.1-dev
instance_prompt: a vintage ad of
license: other
license_name: flux-1-dev-non-commercial-license
license_link: https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md
widget:
  - text: >-
      A vintage ad of a roomba robot while a person on the couch vntgads, it reads "I clean, you chill", "roomba" brand on the bottom right
    output:
      url: >-
        samples/j_XNU6Oe0mgttyvf9uPb3_dc244dd3d6c246b4aff8351444868d66.png
  - text: >-
      a vintage ad with a woman wearing a VR headset with an apple logo and laughing, vtgads; it reads "Vision Pro" on the top and "escape the real world" in the bottom
    output:
      url: >-
        samples/89XhAeDdYRGAYvBMLkBhc_803a8764d5a04cdd9c9d008d3d14272b.png
  - text: >-
      a vintage ad illustrating a cute Hugging Face emoji giving a talk to other emojis, it reads "Hugging Face" on top and "join the community" on the bottom
    output:
      url: >-
        samples/BV0fi30jybwMKs--hAAQl_968329383e3748bdbbf54c90e55ddd83.png
  - text: >-
      a vintage ad of Twitter, the twitter bird with a speech baloon that reads "I will never be X"
    output:
      url: >-
        samples/-FMpgla6rQ1hBwBpbr-Ao_da7b23c29de14a9cad94901879ae2e2b.png
  - text: a vintage ad illustrating istambul skyline and a tabby cat on the foreground; it reads "come to istambul, we have cats!"
    output:
      url: >-
        samples/fvpUmQ1Lx2aogKF35XrpR_286be86aa96f4bc4ab6f37eb0a04b914.png
  - text: a vintage ad of neuralink, a person with a brain computer implant, vtgads; it reads "neuralink" on the top and "if you can't defeat the AI, join it!"
    output:
      url: >-
        samples/jAq9FSh7s0OxEzU5qYaIa_f57fd771a4c045c08afa9a11b0506ff4.png
datasets:
  - multimodalart/vintage-ads
---
# vintage ads flux

<Gallery />


## Model description

Model trained on public domain Vintage Ads


## Trigger words

You should use `a vintage ad of` to trigger the image generation.


## Download model

Weights for this model are available in Safetensors format.

[Download](/multimodalart/vintage-ads-flux/tree/main) them in the Files & versions tab.

## Training at fal.ai

Training was done using [fal.ai/models/fal-ai/flux-lora-general-training](https://fal.ai/models/fal-ai/flux-lora-general-training).
