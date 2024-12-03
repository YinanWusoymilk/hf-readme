---
tags:
- anime
---
NOTICE: My LoRAs require high amount of tags to look good, I will fix this later on and update all of my LoRAs if everything works out.

# General Information

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [SocialMedia](#socialmedia)
- [Plans for the future](#plans-for-the-future)

# Overview

Welcome to the place where I host my LoRAs. In short, LoRA is just a checkpoint trained on specific artstyle/subject that you load into your WebUI, that can be used with other models.  
Although you can use it with any model, the effects of LoRA will vary between them.
Most of the previews use models that come from [WarriorMama777](https://huggingface.co/WarriorMama777/OrangeMixs) .  
For more information about them, you can visit the original LoRA repository: https://github.com/cloneofsimo/lora  
Every images posted here, or on the other sites have metadata in them that you can use in PNG Info tab in your WebUI to get access to the prompt of the image.  
Everything I do here is for free of charge!  
I don't guarantee that my LoRAs will give you good results, if you think they are bad, don't use them.

# Installation

To use them in your WebUI, please install the extension linked under, following the installation guide:  
https://github.com/kohya-ss/sd-webui-additional-networks#installation

# Usage

All of my LoRAs are to be used with their original danbooru tag. For example:  
```
asuna \(blue archive\)
```
My LoRAs will have sufixes that will tell you how much they were trained. Either by using words like "soft" and "hard",  
where soft stands for lower amount of training and hard for higher amount of training.  

More trained LoRA is harder to modify but provides higher consistency in details and original outfits,  
while lower trained one will be more flexible, but may get details wrong.

All the LoRAs that aren't marked with PRUNED require tagging everything about the character to get the likness of it.
You have to tag every part of the character like: eyes,hair,breasts,accessories,special features,etc...

In theory, this should allow LoRAs to be more flexible, but it requires to prompt those things always, because character tag doesn't have those features baked into it.
From 1/16 I will test releasing pruned versions which will not require those prompting those things.

The usage of them is also explained in this guide:  
https://github.com/kohya-ss/sd-webui-additional-networks#how-to-use

# SocialMedia

Here are some places where you can find my other stuff that I post, or if you feel like buying me a coffee:  
[Twitter](https://twitter.com/Trauter8)  
[Pixiv](https://www.pixiv.net/en/users/88153216)  
[Buymeacoffee](https://www.buymeacoffee.com/Trauter) 

# Plans for the future

- Remake all of my LoRAs into pruned versions which will be more user friendly and easier to use, and use 768x768 res. for training and better Learning Rate
- After finishing all of my LoRA that I want to make, go over the old ones and try to make them better.
- Accept suggestions for almost every character.
- Maybe get motivation to actually tag outfits.
  
# LoRAs

- [Genshin Impact](#genshin-impact)
  - [Eula](#eula)
  - [Barbara](#barbara)
  - [Diluc](#diluc)
  - [Mona](#mona)
  - [Rosaria](#rosaria)
  - [Yae Miko](#yae-miko)
  - [Raiden Shogun](#raiden-shogun)
  - [Kujou Sara](#kujou-sara)
  - [Shenhe](#shenhe)
  - [Yelan](#yelan)
  - [Jean](#jean)
  - [Lisa](#lisa)
  - [Zhongli](#zhongli)
  - [Yoimiya](#yoimiya)
- [Blue Archive](#blue-archive)
  - [Rikuhachima Aru](#rikuhachima-aru)
  - [Ichinose Asuna](#ichinose-asuna)
- [Fate Grand Order](#fate-grand-order)
  - [Minamoto-no-Raikou](#minamoto-no-raikou)
- [Misc. Characters](#misc.-characters)
  - [Aponia](#aponia)
  - [Reisalin Stout](#reisalin-stout)
- [Artstyles](#artstyles)
  - [Pozer](#pozer)


# Genshin Impact
  
  - # Eula
    [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/1.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/1.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, eula \(genshin impact\), 1girl, solo, thighhighs, weapon, gloves, breasts, sword, hairband, necktie, holding, leotard, bangs, greatsword, cape, thighs, boots, blue hair, looking at viewer, arms up, vision (genshin impact), medium breasts, holding sword, long sleeves, holding weapon, purple eyes, medium hair, copyright name, hair ornament, thigh boots, black leotard, black hairband, blue necktie, black thighhighs, yellow eyes, closed mouth
Negative prompt: (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 8, Seed: 2010519914, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 1.8, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305293076)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Eula)
  - # Barbara
    [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/bar.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/bar.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, eula \(genshin impact\), 1girl, solo, thighhighs, weapon, gloves, breasts, sword, hairband, necktie, holding, leotard, bangs, greatsword, cape, thighs, boots, blue hair, looking at viewer, arms up, vision (genshin impact), medium breasts, holding sword, long sleeves, holding weapon, purple eyes, medium hair, copyright name, hair ornament, thigh boots, black leotard, black hairband, blue necktie, black thighhighs, yellow eyes, closed mouth
Negative prompt: (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 8, Seed: 2010519914, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 1.8, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305435137)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Barbara)
  - # Diluc
    [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/dil.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/dil.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, eula \(genshin impact\), 1girl, solo, thighhighs, weapon, gloves, breasts, sword, hairband, necktie, holding, leotard, bangs, greatsword, cape, thighs, boots, blue hair, looking at viewer, arms up, vision (genshin impact), medium breasts, holding sword, long sleeves, holding weapon, purple eyes, medium hair, copyright name, hair ornament, thigh boots, black leotard, black hairband, blue necktie, black thighhighs, yellow eyes, closed mouth
Negative prompt: (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 8, Seed: 2010519914, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 1.8, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305427945)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Diluc)
  - # Mona
    [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/mon.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/mon.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, eula \(genshin impact\), 1girl, solo, thighhighs, weapon, gloves, breasts, sword, hairband, necktie, holding, leotard, bangs, greatsword, cape, thighs, boots, blue hair, looking at viewer, arms up, vision (genshin impact), medium breasts, holding sword, long sleeves, holding weapon, purple eyes, medium hair, copyright name, hair ornament, thigh boots, black leotard, black hairband, blue necktie, black thighhighs, yellow eyes, closed mouth
Negative prompt: (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 8, Seed: 2010519914, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 1.8, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305428050)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Mona)
  - # Rosaria
    [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/ros.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/ros.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, eula \(genshin impact\), 1girl, solo, thighhighs, weapon, gloves, breasts, sword, hairband, necktie, holding, leotard, bangs, greatsword, cape, thighs, boots, blue hair, looking at viewer, arms up, vision (genshin impact), medium breasts, holding sword, long sleeves, holding weapon, purple eyes, medium hair, copyright name, hair ornament, thigh boots, black leotard, black hairband, blue necktie, black thighhighs, yellow eyes, closed mouth
Negative prompt: (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 8, Seed: 2010519914, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 1.8, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305428015)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Rosaria)
  - # Yae Miko
    [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/yae.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/yae.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, eula \(genshin impact\), 1girl, solo, thighhighs, weapon, gloves, breasts, sword, hairband, necktie, holding, leotard, bangs, greatsword, cape, thighs, boots, blue hair, looking at viewer, arms up, vision (genshin impact), medium breasts, holding sword, long sleeves, holding weapon, purple eyes, medium hair, copyright name, hair ornament, thigh boots, black leotard, black hairband, blue necktie, black thighhighs, yellow eyes, closed mouth
Negative prompt: (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 8, Seed: 2010519914, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 1.8, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305448948)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/yae%20miko)
  - # Raiden Shogun
  - [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/ra.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/ra.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, raiden shogun, 1girl, breasts, solo, cleavage, kimono, bangs, sash, mole, obi, tassel, blush, large breasts, purple eyes, japanese clothes, long hair, looking at viewer, hand on own chest, hair ornament, purple hair, bridal gauntlets, closed mouth, purple kimono, blue hair, mole under eye, shoulder armor, long sleeves, wide sleeves, mitsudomoe (shape), tomoe (symbol), cowboy shot
Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, from behind
Steps: 30, Sampler: DPM++ 2M Karras, CFG scale: 4.5, Seed: 2544310848, Size: 704x384, Model hash: 2bba3136, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.05, Hires upscaler: 4x_foolhardy_Remacri
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305313633)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Raiden%20Shogun)
  - # Kujou Sara
  - [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/ku.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/ku.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, kujou sara, 1girl, solo, mask, gloves, bangs, bodysuit, gradient, sidelocks, signature, yellow eyes, bird mask, mask on head, looking at viewer, short hair, black hair, detached sleeves, simple background, japanese clothes, black gloves, black bodysuit, wide sleeves, white background, upper body, gradient background, closed mouth, hair ornament, artist name, elbow gloves
Negative prompt: (worst quality, low quality:1.4)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 8, Seed: 3966121353, Size: 512x768, Model hash: 931f9552, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 1.8, Hires steps: 20, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305311498)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Kujou%20Sara)
  - # Shenhe
  - [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/sh.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/sh.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, shenhe \(genshin impact\), 1girl, solo, breasts, bodysuit, tassel, gloves, bangs, braid, outdoors, bird, jewelry, earrings, sky, breast curtain, long hair, hair over one eye, covered navel, blue eyes, looking at viewer, hair ornament, large breasts, shoulder cutout, clothing cutout, very long hair, hip vent, braided ponytail, partially fingerless gloves, black bodysuit, tassel earrings, black gloves, gold trim, cowboy shot, white hair
Negative prompt: (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 22, Sampler: DPM++ SDE Karras, CFG scale: 6.5, Seed: 573332187, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 2, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305307599)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Shenhe)
  - # Yelan
  - [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/10.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/10.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, yelan \(genshin impact\), 1girl, breasts, solo, bangs, armpits, smile, sky, cleavage, jewelry, gloves, jacket, dice, mole, cloud, grin, dress, blush, earrings, thighs, tassel, sleeveless, day, outdoors, large breasts, looking at viewer, green eyes, arms up, short hair, blue hair, vision (genshin impact), fur trim, white jacket, blue sky, mole on breast, arms behind head, bob cut, multicolored hair, black hair, fur-trimmed jacket, elbow gloves, bare shoulders, blue dress, parted lips, diagonal bangs, clothing cutout, pelvic curtain, asymmetrical gloves
Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name
Steps: 23, Sampler: DPM++ SDE Karras, CFG scale: 6.5, Seed: 575500509, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.58, Clip skip: 2, ENSD: 31337, Hires upscale: 2.4, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305296897)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Yelan)
  - # Jean
  - [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/333.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/333.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, jean \(genshin impact\), 1girl, breasts, solo, cleavage, strapless, smile, ponytail, bangs, jewelry, earrings, bow, capelet, signature, sidelocks, cape, corset, shiny, blonde hair, long hair, upper body, detached sleeves, purple eyes, hair between eyes, hair bow, parted lips, looking to the side, large breasts, detached collar, medium breasts, blue capelet, white background, black bow, blue eyes, bare shoulders, simple background
Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 22, Sampler: DPM++ SDE Karras, CFG scale: 7.5, Seed: 32930253, Size: 512x768, Model hash: ffa7b160, Denoising strength: 0.59, Clip skip: 2, ENSD: 31337, Hires upscale: 1.85, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305307594)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Jean)
  - # Lisa
    [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/lis.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/lis.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, lisa \(genshin impact\), 1girl, solo, hat, breasts, gloves, cleavage, flower, smile, bangs, dress, rose, jewelry, witch, capelet, green eyes, witch hat, brown hair, purple headwear, looking at viewer, white background, large breasts, long hair, simple background, black gloves, purple flower, hair between eyes, upper body, purple rose, parted lips, purple capelet, hat flower, multicolored dress, hair ornament, multicolored clothes, vision (genshin impact)
Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, worst quality, low quality, extra digits, loli, loli face
Steps: 23, Sampler: DPM++ SDE Karras, CFG scale: 6.5, Seed: 350134479, Size: 512x768, Model hash: ffa7b160, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 1.85, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305290865)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Lisa)

  - # Zhongli
[<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/zho.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/zho.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, zhongli \(genshin  impact\), solo, 1boy, bangs, jewelry, tassel, earrings, ponytail, low ponytail, gloves, necktie, jacket, shirt, formal, petals, suit, makeup, eyeliner, eyeshadow, male focus, long hair, brown hair, multicolored hair, long sleeves, tassel earrings, single earring, collared shirt, hair between eyes, black gloves, closed mouth, yellow eyes, gradient hair, orange hair, simple background
Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, worst quality, low quality, extra digits, loli, loli face
Steps: 22, Sampler: DPM++ SDE Karras, CFG scale: 7, Seed: 88418604, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.58, Clip skip: 2, ENSD: 31337, Hires upscale: 2, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305311423)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Zhongli)
    
  - # Yoimiya
    [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/Yoi.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/Yoi.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, eula \(genshin impact\), 1girl, solo, thighhighs, weapon, gloves, breasts, sword, hairband, necktie, holding, leotard, bangs, greatsword, cape, thighs, boots, blue hair, looking at viewer, arms up, vision (genshin impact), medium breasts, holding sword, long sleeves, holding weapon, purple eyes, medium hair, copyright name, hair ornament, thigh boots, black leotard, black hairband, blue necktie, black thighhighs, yellow eyes, closed mouth
Negative prompt: (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 8, Seed: 2010519914, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 1.8, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305448498)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Genshin-Impact/Yoimiya)

# Blue Archive
  - # Rikuhachima Aru
  - [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/22.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/22.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
aru \(blue archive\), masterpiece, best quality, 1girl, solo, horns, skirt, gloves, shirt, halo, window, breasts, blush, sweatdrop, ribbon, coat, bangs, :d, smile, indoors, standing, plant, thighs, sweat, jacket, day, sunlight, long hair, white shirt, white gloves, black skirt, looking at viewer, open mouth, long sleeves, red ribbon, fur trim, neck ribbon, red hair, fur-trimmed coat, collared shirt, orange eyes, medium breasts, brown coat, hands up, side slit, coat on shoulders, v-shaped eyebrows, yellow eyes, potted plant, fur collar, shirt tucked in, demon horns, high-waist skirt, dress shirt
Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 22, Sampler: DPM++ SDE Karras, CFG scale: 6.5, Seed: 1190296645, Size: 512x768, Model hash: ffa7b160, Denoising strength: 0.58, Clip skip: 2, ENSD: 31337, Hires upscale: 1.85, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305293051)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Blue-Archive/Rikuhachima%20Aru)
  - # Ichinose Asuna
  - [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/asu.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/asu.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
photorealistic, (hyperrealistic:1.2), (extremely detailed CG unity 8k wallpaper), (ultra-detailed), (mature female:1.2), masterpiece, best quality, asuna \(blue archive\), 1girl, breasts, solo, gloves, pantyhose, ass, leotard, smile, tail, halo, grin, blush, bangs, sideboob, highleg, standing, mole, strapless, ribbon, thighs, animal ears, playboy bunny, rabbit ears, long hair, white gloves, very long hair, large breasts, high heels, blue leotard, hair over one eye, fake animal ears, blue eyes, looking at viewer, white footwear, rabbit tail, official alternate costume, full body, elbow gloves, simple background, white background, absurdly long hair, bare shoulders, detached collar, thighband pantyhose, leaning forward, highleg leotard, strapless leotard, hair ribbon, brown pantyhose, black pantyhose, mole on breast, light brown hair, brown hair, looking back, fake tail
Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 22, Sampler: DPM++ SDE Karras, CFG scale: 6.5, Seed: 2052579935, Size: 512x768, Model hash: ffa7b160, Clip skip: 2, ENSD: 31337
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305292996)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Blue-Archive/Ichinose%20Asuna)
# Fate Grand Order
  - # Minamoto-no-Raikou
  - [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/3.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/3.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
mature female, masterpiece, best quality, minamoto no raikou \(fate\), 1girl, breasts, solo, bodysuit, gloves, bangs, smile, rope, heart, blush, thighs, armor, kote, long hair, purple hair, fingerless gloves, purple eyes, large breasts, very long hair, looking at viewer, parted bangs, ribbed sleeves, black gloves, arm guards, covered navel, low-tied long hair, purple bodysuit, japanese armor
Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name, (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 22, Sampler: DPM++ SDE Karras, CFG scale: 7.5, Seed: 3383453781, Size: 512x768, Model hash: ffa7b160, Denoising strength: 0.59, Clip skip: 2, ENSD: 31337, Hires upscale: 2, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305290900)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Fate-Grand-Order/Minamoto-no-Raikou)

# Misc. Characters
  
  - # Aponia
    [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/apo.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/apo.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, eula \(genshin impact\), 1girl, solo, thighhighs, weapon, gloves, breasts, sword, hairband, necktie, holding, leotard, bangs, greatsword, cape, thighs, boots, blue hair, looking at viewer, arms up, vision (genshin impact), medium breasts, holding sword, long sleeves, holding weapon, purple eyes, medium hair, copyright name, hair ornament, thigh boots, black leotard, black hairband, blue necktie, black thighhighs, yellow eyes, closed mouth
Negative prompt: (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 8, Seed: 2010519914, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 1.8, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305445819)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Misc.%20Characters/Aponia)

  - # Reisalin Stout
    [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/ryza.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/ryza.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, eula \(genshin impact\), 1girl, solo, thighhighs, weapon, gloves, breasts, sword, hairband, necktie, holding, leotard, bangs, greatsword, cape, thighs, boots, blue hair, looking at viewer, arms up, vision (genshin impact), medium breasts, holding sword, long sleeves, holding weapon, purple eyes, medium hair, copyright name, hair ornament, thigh boots, black leotard, black hairband, blue necktie, black thighhighs, yellow eyes, closed mouth
Negative prompt: (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 8, Seed: 2010519914, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 1.8, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305448553)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Misc.%20Characters/reisalin%20stout)

# Artstyles
  
  - # Pozer
    [<img src="https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/art.png" width="512" height="768">](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/resolve/main/LoRA/Previews/art.png)
<details>
  <summary>Sample Prompt</summary>
  <pre>
masterpiece, best quality, eula \(genshin impact\), 1girl, solo, thighhighs, weapon, gloves, breasts, sword, hairband, necktie, holding, leotard, bangs, greatsword, cape, thighs, boots, blue hair, looking at viewer, arms up, vision (genshin impact), medium breasts, holding sword, long sleeves, holding weapon, purple eyes, medium hair, copyright name, hair ornament, thigh boots, black leotard, black hairband, blue necktie, black thighhighs, yellow eyes, closed mouth
Negative prompt: (worst quality, low quality, extra digits, loli, loli face:1.3)
Steps: 20, Sampler: DPM++ SDE Karras, CFG scale: 8, Seed: 2010519914, Size: 512x768, Model hash: a87fd7da, Denoising strength: 0.57, Clip skip: 2, ENSD: 31337, Hires upscale: 1.8, Hires upscaler: Latent (nearest-exact)
</pre>
</details>

    - [Examples](https://www.flickr.com/photos/197461145@N04/albums/72177720305445399)
    - [Download](https://huggingface.co/YoungMasterFromSect/Trauter_LoRAs/tree/main/LoRA/Artstyles/Pozer)