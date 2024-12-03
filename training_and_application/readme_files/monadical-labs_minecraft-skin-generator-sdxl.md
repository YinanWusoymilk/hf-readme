---
license: openrail
language:
- en
library_name: diffusers
tags:
- minecraft
- skins
- gaming
- stable diffusion
- stable diffusion xl
pipeline_tag: text-to-image
---

# Minecraft Skin Generator XL

Monadical is pleased to announce the official release of the Minecraft Skin Generator XL model. We had previously released the [Minecraft Skin Generator](https://huggingface.co/monadical-labs/minecraft-skin-generator) model based upon Stable Diffusion 2. This new model offers significant improvements over the last generation of models.

### Key Features

1. **Upgrade to Stable Diffusion XL** - Our model is now based upon the Stable Diffusion XL model, which greatly improves the quality of generated skins when compared to previous models.
1. **Transparent Layer Support** - The new model now supports the transparency layer in the hair and helmet section of the skin.

### Examples

* 'Kelly Kapoor from the TV show "The Office"'
![Kelly Kapoor](images/kelly.png)

* 'Saul Goodman from the TV show "Better Call Saul"'
![Saul Goodman](images/saul.png)

* 'Gustavo Fring from the TV show "Breaking Bad"'
![Gustavo Fring](images/fring.png)

* 'Daryl Dixon from the TV show "The Walking Dead"'
![Daryl Dixon](images/daryl.png)

* 'Zach Galifianakis as Alan in the movie "The Hangover"'
![Alan from The Hangover](images/hangover.png)

### Try It Out Yourself

There are several options for trying out this new model:

1. Download the model and run it locally on your machine. Note that we recommend a GPU for this - while it is possible to run on a CPU, we do not currently support this method.  **Note**: Output from the StableDiffusionXL pipeline should be constrained to 768x768 pixels, or the model will automatically generate a 1024x1024 output image, and fill in the extra space with unusuable garbage.
1. Try our hosted version of the model on the [Minecraft Skin Generator website](https://www.skingenerator.io).

### Get Involved

Have any feedback or suggestions? Join us on our [Minecraft Skin Generator Discord channel](https://discord.com/invite/yMzFzVUPDf) or send us an [email](mailto:info@skingenerator.io).

Happy crafting!

[The Monadical Minecraft Skin Generator Team](https://monadical.com/)