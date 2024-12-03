---
thumbnail: "https://huggingface.co/Hosioka/Baka-Diffusion/resolve/main/Images/Header.png"
language:
- en
- my
tags:
- text-to-image
- stable-Diffusion
- stable-diffusion-diffusers
- diffusers
- safetensors
inference: true
pipeline_tag: text-to-image
library_name: diffusers
license: cc-by-nc-4.0
---


<p align='center'>
    <img src="https://huggingface.co/Hosioka/Baka-Diffusion/resolve/main/Images/Header.png" align='center'>
</p>
<h1 align='center'><b>·</b> Baka-Diffusion <b>·</b></h1>

<h3 align='center'>
    <a href='https://www.figma.com/file/1JYEljsTwm6qRwR665yI7w/Merging-lab%E3%80%8CHosioka-Fork%E3%80%8D?type=design&node-id=1-69&t=MPKBSTP9UWxp91vw-0'><b>·</b>  MBW Resources <b>·</b></a>
</h3>

---
<h1 align='center'><b>·</b> မင်္ဂလာပါ/Hello <b>·</b></h1>
<p align='center'><b>Baka-Diffusion</b> is a latent diffusion model based on series of finetuned / U-Net Block merges made to push the limits of SD1.x based models. Our models uses the Danbooru Tagging system </p>

---
# 

## **⚠️ Disclaimer**
**You are responsible for the content you generate, whether it is NSFW or SFW. The AI models do not contain explicit visual content that can be accessed easily.**

---

### **⚒️ Model synopsis**
Due to the nature of **U-Net Block merging**, some models function differently in CFG Scales. It is generally preferred to use the models in this repository with CFG 3-9. above this range are usable, but you may encounter artifacting, visible leftover noise, or color burn.

----

### ***Baka-Diffusion\[General\]***
Baka-Diffusion\[General\] was created with the idea of being a blank canvas; Without heavy focus on stylization, I wanted to make something compatible with most LoRA/LyCORIS models, but with coherency that would outperform [\[S3D\]](https://huggingface.co/Hosioka/dasda#baka-diffusions3d). To achieve that I've used some inference tricks as well as becoming an ***Inference rat*** in the process. Issues such as burned gens when having a long prompt are gone. **CFG** is also much more stable in this release. 

<p align='center'>
    <img src='https://huggingface.co/Hosioka/Baka-Diffusion/resolve/main/Images/Model%20Showcase%20General.png'>
    <img src='https://huggingface.co/Hosioka/Baka-Diffusion/resolve/main/Images/model%20showcase6%20General.png'>
</p>

----
### ***Baka-Diffusion\[S3D\]***
Baka-Diffusion\[S3D\] aims to bring a subtle 3D textured look and mimic natural lighting, diverging from the typical anime-style lighting seen in regular Baka-Diffusion models. It's specifically designed for higher resolutions, preferring 600x896 over the traditional 512x768. This model works well with low rank networks like LoRA / LyCORIS models, ensuring compatibility and versatility.

<p align='center'>
    <img src='https://huggingface.co/Hosioka/Baka-Diffusion/resolve/main/Images/model%20showcase6%20S3D.png'>

  negative settings: ***(worst quality, low quality:1.2), lowres, bad anatomy,***
</p>

----

### 🔧 Inference tricks
To become an inference rat such as myself, You will need these !


- #### Textual Inversion
"*Why is Hosioka recommending people to use a textual inversion alongside the model? is he stupid?*" <br></br>
Using a very light weight negative textual inversion such as [SimpleNegativeV1](https://civitai.com/models/87243?modelVersionId=92840) by Aikimi does wonders to your model's overall coherency without sacrificing the style. Thank you very much [Aikimi!](https://note.com/aikimi/n/nf5f4c979a002). 

- #### [FreeU for everyone!](https://arxiv.org/abs/2309.11497)
Here is my preset for FreeU, steering the model toward aesthetically pleasing generations, Also gives the model [ZeroTerminalSNR](https://arxiv.org/abs/2305.08891) effect when it comes being able to generate much lighter and darker images.
<p align='center'>
    <img src='https://files.catbox.moe/a9hpct.png'>
   Transition smoothness is optional.
</p>

----

### 📝 **Notes and Findings**
<details>
<summary><kbd>Toggle to read</kbd></summary>
Training a standalone aesthetic model within this architecture seems nearly impossible without compromising anatomy quality. Even with a carefully curated dataset, the model doesn't converge into a high-quality aesthetic model. Instead, it appears to converge into an output that represents the average of all the training images, even when efforts are made to maintain a uniform dataset. I wonder if this issue is inherent to the nature of illustrations themselves. Unlike training a model focused on realism, which only requires high-quality data, training a weeb model with an aesthetic focus turns out to be a pain in the rear.
<p align='center'>
    <img src='https://huggingface.co/Hosioka/Baka-Diffusion/resolve/main/Images/Funny%20compromise.png'>
</p>
The solution I've resorted to is nothing more than a half-assed approach, I've tried Block Merging from a model that exhibits good anatomy into the trained aesthetic model. If you're familiar with Block Weighted Merging, you'd know that this kind of issue is quite challenging to fix, even with knowledge of what each U-Net layer does. It's a time-consuming process and, unfortunately, can give the author mild autism. Even this approach has its drawbacks. Recklessly merging, as is often done by many model authors, leads to a poorer overall coherency. I've experimented with various models, and most of them are incapable of drawing simple expressions.

Now on the topic of trainers. Everyone use either Kohya or EveryDream2 for finetuning. Based on my experiences with both, Kohya falls short in full fine-tuning, whereas EveryDream2 excels in this aspect. Each trainer has features I wish to see combined into one. For example, EveryDream2 allows the freezing of layers in the text encoder to retain parent data while training the rest. On the other hand, Kohya has Neuron Dropout, a feature that can compel layer(X) to learn what layer(Y) excels at. On the surface, both trainers have their strengths and weaknesses. Each excels in certain features but also falls short in other aspects.

For example, if OUT5 is proficient in learning faces but IN00 isn't, Network Dropout enables you to instruct OUT5 to take a temporary break while IN00 focuses on mastering the skill of drawing a face. This approach compels the targeted layer(X) to improve in areas where it is weak, while temporarily halting other layers to prevent them from learning at the same pace and overfitting. Idiot proofy infographic below.
<p align='center'>
    <img src='https://huggingface.co/Hosioka/Baka-Diffusion/resolve/main/Images/Network%20Dropout.png?download=true'>
</p>
If what you're looking for is full fine-tuning go with EveryDream2 and If what you're looking for are low rank adapters Kohya has your back. but in all honesty I just want Kohya features in EveryDream2. Kudos to Freon and Kohya for developing these trainers !

Lastly, I've decided to step back from creating any more models. I want to take a break and wait a few more years until open-source diffusion matures. I'll still be around, occasionally making gens and low-rank adapters. Thank you for using Baka-Diffusion!
</details>

----
### 🔗 **Credits!**
- Erasing : https://github.com/rohitgandikota/erasing
- Runtime Block Merge : https://github.com/ashen-sensored/sd-webui-runtime-block-merge
- Super Merger : https://github.com/hako-mikan/sd-webui-supermerger
- KL-F8 Anime2 VAE : https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/vae/kl-f8-anime2.ckpt
- SimpleNegative : https://civitai.com/models/87243?modelVersionId=92840
- (You)
----
## 📝 **License**
This project under the [CC BY-NC 4.0 License](https://creativecommons.org/licenses/by-nc/4.0/deed.en).
<br></br>

----
<br></br>
<p align='center'>
    <i>2021 me just wanted to generate some drill haired waifus.... How did it come to this... Anyhow, I hope everyone enjoyed my work. <i>
</p>