---
tags:
- text-to-image
- stable-diffusion
- lora
- diffusers
- template:sd-lora
- flux
- flux dev
- realism
widget:
- text: >-
    phone photo five men playing a Medieval diplomacy game around a table on a
    couch in a living room at night in 2014
  output:
    url: images/ComfyUI_00855_.png
- text: >-
    phone photo of two women in roman cosplay outfits holding a sign reading
    'Boreal-FD' on top of a dining room table in front of a crowd in New York at
    night
  output:
    url: images/ComfyUI_00822_.png
- text: >-
    phone photos of three people performing a ritualistic sacrifice in a busy
    hotel lobby with a demon
  output:
    url: images/ComfyUI_00944_.png
- text: >-
    closeup phone photo of a 25 year old women wearing a yoshi cosplay outfit
    while riding a zebra near a crowd while showing a piece of paper
    with'Boreal-FD' written on it at noon in the summer in a alley in new york
    city
  output:
    url: images/ComfyUI_00845_.png
- text: >-
    phone photo of two men eating a full sad potato at a at a restaurant in 2017
    posted to reddit
  output:
    url: images/ComfyUI_01026_.png
base_model: black-forest-labs/FLUX.1-dev
instance_prompt: photo
---
# Boreal-FD

<Gallery />

## Model description 

**Work in Progress**
This is a very early experimental lora for Flux-Dev. It uses the **Bo**ring **Real**ity image datasets to work on shifting Flux towards more realistic images.

![ComfyUI_00855_.png](https:&#x2F;&#x2F;cdn-uploads.huggingface.co&#x2F;production&#x2F;uploads&#x2F;641ba2eeec5b871c0bcfdba3&#x2F;jfGF0xFNij7gC_bcZ3OdW.png)

As with most other AI image generative models, the flux-dev model is biased towards certain photographic aesthetics like shallow depth of fields with centralized posing along with all the artwork influence as well. As a result the models produce very limited types of photos which tends to mask how much knowledge the model actually has.

The goal with these boring reality trained loras is to not only bring out better photorealistic images but to push the model to show how much knowledge and information it can actually place in a single generated image.

**Update 08/21**
I am still exploring new ways to train this model/dataset. For the timebeing, the faded dot issue remains in these LoRAs as these older models have performed a better job of learning the concept than any of the subsequent runs I have done. 
The new Schnell version may be released before updating this Dev model. 
To simplify use of the model, I removed the 400 steps weights to help with resolve issues. If necesary I will add the 400 steps as a seperate model, though you can probably get a slightly similar result reducing the strength of the 1000 steps version.
I will try to seperate models going forward, though it is not the best strategy when you need to manually choose between undertrained/overtrained LoRAs on top of their strength for each image.


**Primary Goals for Boreal-FD**
- Reduce how often shallow depths of field appear in images
- More dynamic poses
- More realistic skin texture
- More interesting backgrounds
- Overall Increase scene complexity



![ComfyUI_00990_.png](https:&#x2F;&#x2F;cdn-uploads.huggingface.co&#x2F;production&#x2F;uploads&#x2F;641ba2eeec5b871c0bcfdba3&#x2F;pX6R5u5ehrLi245qFT1qV.png)

**Additional Notes**
These two flux loras are not expected to create very good images. Many results may be overfitted, distorted, and have this slight faded dotted look for lesser known concepts.

The 1000 step lora is more over-fitted with with distortion and lack of prompt understanding more likely to occur, but it may perform better on things like dynamic posing and skin texture. 

You will want to experiment between the two loras, tweaking the lora strengths between 0.5-2.0 and guidance between 3.0-5.0 along with testing many different seeds. 

As more understanding develops for Flux, better workflows for these current models will come along as well as newer Boreal-FD versions as the training improves.




## Trigger words

You should use `photo` to trigger the image generation.


## Download model

Weights for this model are available in Safetensors format.

[Download](/kudzueye/Boreal/tree/main) them in the Files & versions tab.