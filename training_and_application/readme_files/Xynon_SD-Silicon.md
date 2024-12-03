---
license: creativeml-openrail-m
tags:
  - stable-diffusion
  - text-to-image
  - safetensors
---

----

# SD-Silicon

SD-Silicon: A series of general-purpose models based off the experimental automerger, autoMBW.

A collaborative creation of Xerxemi#6423 & Xynon#7407.

![](https://raw.githubusercontent.com/Xerxemi/SD-Silicon-README/master/webp/panaroma.webp "")

All models listed have baked WD1.3 VAE. However, for the purposes of this model series, external VAE is also recommended. 

----

# Licence

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage. The CreativeML OpenRAIL License specifies: 
1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully) Please read the full license here ：https://huggingface.co/spaces/CompVis/stable-diffusion-license

# Terms of use

- **Clearly indicate where modifications have been made.**  
If you used it for merging, please state what steps you took to do so.

----

# --base models--

Silicon28: a.k.a. extestg4. The first model of autoMBW to match/surpass quality of manual merge block weight merges.

Silicon29: a.k.a. extesto4. a similar, but much larger list of merges based off the list of Silicon28. First good model to be constructed on a semi-stabilized autoMBW codebase.

# --specialty models--

Silicon28-negzero: a.k.a. extestg4-negzero. A negatively finetuned version of Silicon28 for 10 epochs off a dataset of 3990 images. Better at some, worse at others.

Silicon29-dark: a.k.a. extesto4-dark. Silicon29, but merged with noise offset. Gives darker output than the original base.

# --future models--

More will be posted soon<sup>TM</sup>

----

# Recommended Settings

Sampler: DPM++ 2M

Steps: 42 + 42 | can probably go lower, I just run at this

Upscaler: Latent (bicubic antialiased)

Denoising: ~0.5 to ~0.6

CFG: 13

----

more comparisons here: https://medium.com/@media_97267/the-automated-stable-diffusion-checkpoint-merger-autombw-44f8dfd38871

Note: all comparison photos are pure Silicon29 with the latent bicubic antialiased upscaler.

![](https://raw.githubusercontent.com/Xerxemi/SD-Silicon-README/master/webp/angel3.webp "")
![](https://raw.githubusercontent.com/Xerxemi/SD-Silicon-README/master/webp/sundown2.webp "")
![](https://raw.githubusercontent.com/Xerxemi/SD-Silicon-README/master/webp/mountain2.webp "")
![](https://raw.githubusercontent.com/Xerxemi/SD-Silicon-README/master/webp/landscape2.webp "")

----

# Q: Why is this named Silicon?

A: Silicon's atomic number is 14. This line of models was originally supposed to be the 14th experimental model in Xynon/models, a.k.a. experimental14a/b/c. 

# Q: Where do I find the automerger used to make these models?

A: https://github.com/Xerxemi/sdweb-auto-MBW | preliminary article here: https://medium.com/@media_97267/the-automated-stable-diffusion-checkpoint-merger-autombw-44f8dfd38871

----
