---
license: cc0-1.0
tags:
- text-to-image
- stable-diffusion
- lora
- diffusers
base_model: stabilityai/stable-diffusion-xl-base-1.0
instance_prompt: Mickey
widget:
- text: "drawing of Mickey, theater in background"
  output:
    url: "mickey_theater.jpg"
- text: "drawing of Mickey inspiring the communist revolution"
  output:
    url: "communist_mickey.jpg"
- text: "pop-art painting of Mickey walking in Paris"
  output:
    url: "mickey_paris.jpg"
pipeline_tag: text-to-image
datasets:
- Pclanglais/Mickey-1928-dataset
---

**Mickey-1928** is fine-tuned version of Stable-Diffusion-xl trained on 96 stills in the public domain from 1928.

<Gallery />

Mickey-1928 can generate images of Mickey, Minnie and, to a much lesser extent, Pete (with the prompt PeteLegPete).

## Dataset

Since 2024, the first three cartoons of Mickey are in the public domain. The final dataset includes:
- 40 stills from *Gallopin' Gaucho* (in color)
- 22 stills from *Plane Crazy*
- 34 stills from *Steamboat Willie*.

The stills are not currently available in high quality and you should not expect consistently good results from Mickey-1928. The color images from *Gallopin' Gaucho* are in 360x360 pixels. Hopefully with the cartoons now being part of the public domain, higher definition versions should be available.

The generated images aim to adhere to the 1928 design in order to have Mickey, Minnie and Pete in the public domain. This is still a work in progress: while the model is in development, generated images should be checked to ensure they really are in the public domain design.
