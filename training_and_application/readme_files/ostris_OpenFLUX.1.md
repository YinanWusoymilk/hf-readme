---
license: apache-2.0
library_name: diffusers
pipeline_tag: text-to-image
---

<img src="https://huggingface.co/ostris/OpenFLUX.1/resolve/main/assets/banner_0_1_0-2.png" style="max-width: 100%;">

<div style="color: #f0b800;">
  
# <span style="color: #f0b800;"> Beta Version v0.1.0 </span>
  
After numerous iterations and spending way too much of my own money on compute to train this, I think it is finally at the point I am happy to consider it a beta. I am still going to continue to train it, but the distillation has been mostly trained out of it at this point. So phase 1 is complete. Feel free to use it and fine tune it, but be aware that I will likely continue to update it.

</div>

<img src="https://huggingface.co/ostris/OpenFLUX.1/resolve/main/assets/banner_0_1_0-3.png" style="max-width: 100%;">

## What is this?

This is a fine tune of the [FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) model that has had the distillation trained out of it. Flux Schnell is licensed Apache 2.0, but it is a distilled model, meaning you cannot fine-tune it. However, it is an amazing model that can generate amazing images in 1-4 steps. This is an attempt to remove the distillation to create an open source, permissivle licensed model that can be fine tuned. 

<img src="https://huggingface.co/ostris/OpenFLUX.1/resolve/main/assets/banner_0_1_0-1.png" style="max-width: 100%;">


## How to Use

Since the distillation has been fine tuned out of the model, it uses classic CFG. Since it requires CFG, it will require a different pipeline than the original FLUX.1 schnell and dev models. This pipeline can be found in open_flux_pipeline.py in this repo. I will be adding example code in the next few days, but for now, a cfg of 3.5 seems to work well. 

<img src="https://huggingface.co/ostris/OpenFLUX.1/resolve/main/assets/banner_0_1_0-0.png" style="max-width: 100%;">

<img src="https://huggingface.co/ostris/OpenFLUX.1/resolve/main/assets/banner_0_1_0-4.png" style="max-width: 100%;">