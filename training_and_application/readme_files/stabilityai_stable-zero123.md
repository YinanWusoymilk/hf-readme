---
datasets:
- allenai/objaverse
tags:
- 3d
extra_gated_fields:
  Name: text
  Email: text
  Country: text
  Organization or Affiliation: text
  I ALLOW Stability AI to email me about new model releases: checkbox
license: other
license_name: sai-nc-community
license_link_stable_zero123: https://huggingface.co/stabilityai/sdxl-turbo/blob/main/LICENSE_stable_zero123.md  
license_link_stable_zero123_c: https://huggingface.co/stabilityai/sdxl-turbo/blob/main/LICENSE_stable_zero123_c.md  
pipeline_tag: text-to-3d
---
# Stable Zero123

Please note: For commercial use, please refer to https://stability.ai/license

## Model Description

Stable Zero123 is a model for view-conditioned image generation based on [Zero123](https://github.com/cvlab-columbia/zero123). 

With improved data rendering and model conditioning strategies, our model demonstrates improved performance when compared to the original Zero123 and its subsequent iteration, Zero123-XL.

<img src='img.png' width='700'>

## Usage

By using Score Distillation Sampling (SDS) along with the Stable Zero123 model, we can produce high-quality 3D models from any input image. The process can also extend to text-to-3D generation by first generating a single image using SDXL and then using SDS on Stable Zero123 to generate the 3D object.

To enable open research in 3D object generation, we've improved the open-source code of threestudio by supporting Zero123 and Stable Zero123.
To use Stable Zero123 for object 3D mesh generation in [threestudio](https://github.com/threestudio-project/threestudio#stable-zero123), you can follow these steps:

1. Install threestudio using their [instructions](https://github.com/threestudio-project/threestudio#installation)
2. Download the Stable Zero123 checkpoint `stable_zero123.ckpt` into the `load/zero123/` directory
2. Take an image of your choice, or generate it from text using your favourite AI image generator such as Stable Assistant (https://stability.ai/stable-assistant) E.g. "A simple 3D render of a friendly dog"
3. Remove its background using Stable Assistant (https://stability.ai/stable-assistant)
4. Save to `load/images/`, preferably with `_rgba.png` as the suffix
5. Run Zero-1-to-3 with the Stable Zero123 ckpt:
```sh
python launch.py --config configs/stable-zero123.yaml --train --gpu 0 data.image_path=./load/images/hamburger_rgba.png
```

## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: latent diffusion model.
* **Finetuned from model**: [lambdalabs/sd-image-variations-diffusers](https://huggingface.co/lambdalabs/sd-image-variations-diffusers)
* **License**: We released 2 versions of Stable Zero123.
    * **Stable Zero123** included some CC-BY-NC 3D objects, so it cannot be used commercially, but can be used for research purposes. It is released under the [Stability AI Non-Commercial Research Community License](https://huggingface.co/stabilityai/zero123-sai/raw/main/LICENSE_stable_zero123.md).
    * **Stable Zero123C** (“C” for “Commercially-available”) was only trained on CC-BY and CC0 3D objects. It is released under [StabilityAI Community License](https://huggingface.co/stabilityai/zero123-sai/raw/main/LICENSE_stable_zero123_c.md). You can read more about the license [here](https://stability.ai/license). 
According to our internal tests, both models perform similarly in terms of prediction visual quality.

### Training Dataset

We use renders from the [Objaverse](https://objaverse.allenai.org/objaverse-1.0) dataset, utilizing our enhanced rendering method

### Training Infrastructure

* **Hardware**: `Stable Zero123` was trained on the Stability AI cluster on a single node with 8 A100 80GBs GPUs.
* **Code Base**: We use our modified version of [the original zero123 repository](https://github.com/cvlab-columbia/zero123).


### Misuse, Malicious Use, and Out-of-Scope Use

The model should not be used to intentionally create or disseminate images that create hostile or alienating environments for people. This includes generating images that people would foreseeably find disturbing, distressing, or offensive; or content that propagates historical or current stereotypes.