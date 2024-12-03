---
language:
- en
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- art
- artistic
- diffusers
inference: true
thumbnail: "https://i1.lensdump.com/i/Ty4gfb.png"
license: creativeml-openrail-m
---
             

#  <a href="https://huggingface.co/SweetLuna/Aurora/blob/main/README.md" style="text-decoration: none; background-color: transparent;"><img src="https://i2.lensdump.com/i/Ty4kJ0.png"><h4 style="font-size: 1em; text-align: center;">“Explore the New Horizons.... Don't let indecision limit your potential, The world is full of possibilities.”</h1></a></h1>

<hr>

<h1><b><center>Aurora</center></b></h1>


<a href="https://i1.lensdump.com/i/Ty4gfb.png"><img src="https://i1.lensdump.com/i/Ty4gfb.png" alt="RXYEm2.png" onclick="window.open('https://i1.lensdump.com/i/Ty4gfb.png', '_blank')"></a>



---

### <h1 style="font-size: 1.75em; font-family: Segoe UI"><center>[FULLSCREEN](https://huggingface.co/SweetLuna/Aurora/blob/main/README.md)</center></h1>
<hr>

### <center><h1 style="font-size: 1.75em; font-family: Segoe UI">[CivitAI](https://civitai.com/models/40199/aurora) | [Download](https://huggingface.co/SweetLuna/Aurora/tree/main/Aurora%20ONE) | [Changelog](https://huggingface.co/SweetLuna/Kenshi/blob/main/Changelog.md)</h1></center>
<hr>
<style>▼-preamble {
  font-size: 2em;
}</style>
<details id="#contents">
  
 <summary style="font-size: 2.25em; font-family: Segoe UI"><strong>🔬 Contents</strong></summary>
 <hr>
 
# <h1 style="font-size: 1.5em;"><strong>
- [🌠 Preamble](#▼-preamble)<p>
  - [⚙️ Usage](#▼-usage)<p>
  - [🚨 Negative Embeddings](#▼-musthave)<p>
  - [🎨 Versatility](#▼-versatility)<p>
    - [Pixel Arts 👾](#▼-pixel)
    - [Semi-Realistic 🖼️](#▼-semirealistic)
    - [Low CFG 🔅](#▼-lowcfg)
    - [Flat-Color 🍭](#▼-flatisjustice)<p>
  - [✅ VAE [ IMPORTANT ! ]](#▼-vae)<p>
  - [🏔️ Examples Images ](#▼-sample)
    - [Autumn 🍂](#▼-autumn)
    - [Spring 🌸](#▼-spring)
    - [Winter ❄️](#▼-winter)
    - [Summer 🌻](#▼-summer)<p>
  - [🌏 Demo](#▼-demo)<p>
  - [✨ Merge Recipes](#▼-merge)<p>
  - [💡 Suggestions](#▼-suggestions)
    - [Loras](#loras)
    - [WebUI](#webui)
    - [Embeddings](#embeddings)
  - [💛 Donate](#▼-donation)<p>
  - [📝 Credits](#▼-credits)<p>
  - [License](#license)<p>
  - [Disclaimer](#disclaimer)
  
</strong>
</h1>
</details>
  



<hr>


<details id="▼-preamble">
  
 <summary style="font-size: 2.25em; font-family: Segoe UI"><strong>🌙 What is Aurora?</strong></summary>
   <hr>
    <h1>
      
  **Aurora** is a Stable Diffusion model, similar to its predecessor <a href="https://huggingface.co/SweetLuna/Kenshi">**Kenshi**</a>, with the goal of capturing my own feelings towards the anime styles I desire.
  
  The name Aurora, which means 'dawn' in Latin, represents the idea of a new beginning and a fresh start

</h1>
</details>

<hr>

<details id="▼-usage">

<summary style="font-size: 2.25em; font-family: font-family: Segoe UI"><strong>⚙️ Usage</strong></summary>

   <hr>
   <h1>
     
 ## <h1 style="font-size: 1.5em; text-align: center; font-family: Segoe UI">    These are the settings I always use it is recommended but not essential;

| Settings             | Value                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Steps | 20+ |
| Sampler | DPM++ 2M Karras |
|  CFG scale | 2-7 |
| Size |600x800 |
| Clip skip | 2 |
| ENSD | 31337 |
| Hires Fix | Enabled |
| Upscale by | 1.5-2 |
| Upscaler Fix | https://de-next.owncube.com/index.php/s/x99pKzS7TNaErrC |
| Hires Fix | Enabled |

(install it as an extension on Automatic1111 WebUI) : https://github.com/DominikDoom/a1111-sd-webui-tagcomplete
  </h1>
   </h1>
   <center><a href="https://i2.lensdump.com/i/TxNaxZ.png"><img src="https://i2.lensdump.com/i/TxNaxZ.png" alt="TxNaxZ.png" onclick="window.open('https://i2.lensdump.com/i/TxNaxZ.png', '_blank')"></a></center>
</details>
<hr>

<details id="▼-musthave">
<summary style="font-size: 2.25em; font-family: font-family: Segoe UI"><strong>🚨 Negative Embeddings</strong></summary>

   <hr>
   <h1>
     
 ## <h1 style="font-size: 1.5em; text-align: center; color:black; font-family: Segoe UI">    These are the Embeddings I always use for Aurora, you are free to mix with others Negative Embedding however;</h1>
 **<h1 style="font-size: 1.5em; text-align: center; color:black; font-family: Segoe UI">Installation;**</h1>
 
  <h1 style="font-size: 1em; text-align: center; color:black; font-family: Segoe UI"><a href="https://huggingface.co/SweetLuna/Aurora/tree/main/AuroraEmbeddings">1.Download KHFB and AuroraNegatives here.</a>
  <p>2.Put these files inside this directory </p>
    
  ```c#
    "(LocationThatYouInstallSD):\(Main SD Folder)\stable-diffusion-webui\embeddings"
  ```
    
  <center><img src="https://i.lensdump.com/i/TyzjAP.png"></img></center>
  3.Open Auto1111
  
  4.Put them in Negative Prompt like this
  <center><img src="https://i2.lensdump.com/i/TyzsgD.png"></img></center>

  ```c#
 (KHFB, AuroraNegative),(Worst Quality, Low Quality:1.4), (multiple_girls:1.2),border, nsfw, skimpy, grayscale, umbrella, loli
  ```
</h1>
</details>
<hr>

<details id="▼-versatility">

<summary style="font-size: 2.25em; font-family: font-family: Segoe UI"><strong>🎨 Versatility</strong></summary>

   <hr>
   <h1>
     
   ## Unlike Kenshi, Aurora is known for its versatility and perform better.. 
   <p style="font-size: 2em; font-family: font-family: Segoe UI"><strong>You can archive same results with all these examples.</strong></p>
   <hr>



<details id="▼-pixel">

<summary style="font-size: 1.75em; font-family: monospace"><strong>Pixel Arts 👾</strong></summary>
<center><a href="https://i1.lensdump.com/i/TypbwD.png"><img src="https://i1.lensdump.com/i/TypbwD.png" alt="TypbwD.png" onclick="https://i.lensdump.com/i/TypbwD.png", '_blank')"></a></center>

<h1>
  
 ```#c
(pixelart), (mksks style, detailed background),
nanashi_mumei, feather, solo, brown shirt, brown hair, long hair, comfy,
(outdoors, spring \(season\), autumn), long sleeves,
```

```#c
(KHFB, AuroraNegative),(Worst Quality, Low Quality:1.4), border, nsfw, skimpy, grayscale, multiple_girls,
```
  
# **<a href="https://lensdump.com/a/EJyMk" style="font-size: 48px; font-weight: bold;"><center>More Pixel Arts</center></a>**


# **<center>Aurora ONE</center>**


</h1>
</details>
<hr>

<details id="▼-semirealistic">

<summary style="font-size: 1.75em; font-family: monospace"><strong>SemiRealistic 🖼️</strong></summary>
<center><a href="https://i3.lensdump.com/i/TyOzk2.png"><img src="https://i3.lensdump.com/i/TyOzk2.png" alt="TyOzk2.png" onclick="https://i3.lensdump.com/i/TyOzk2.png", '_blank')"></a></center>

<h1>
  
 ```#c
(realistic:1.2), (mksks style, detailed background),
amelia watson, blonde hair, (short hair:0.6), blue eyes, bob cut, monocle hair ornament, medium breasts, (solo),
(outdoors, spring:1.3)
```

```#c
Negative Prompt : (KHFB, AuroraNegative),(Worst Quality, Low Quality:1.4), border, nsfw, skimpy, multiple_girls, split_screen
```
  
# **<a href="https://lensdump.com/a/EQ2bc" style="font-size: 48px; font-weight: bold;"><center>More Semi-Realistic (Bit NSFW)</center></a>**


# **<center>Aurora ONE</center>**


</h1>
</details>
<hr>

 
<details id="▼-lowcfg">

<summary style="font-size: 1.75em; font-family: monospace"><strong>Low CFG 🔅 (3 CFGs)</strong></summary>
<center><a href="https://i2.lensdump.com/i/TyHVjT.png"><img src="https://i2.lensdump.com/i/TyHVjT.png" alt="TyOzk2.png" onclick="https://i2.lensdump.com/i/TyHVjT.png", '_blank')"></a></center>

<h1>
  
 ```#c
SLE, detailed eyes, 1girl, white hair, (glowing_headphone), white jacket, floating,

detailed background, hologram screen, detailed (moon:1.2),realistic, highly detailed, volumetric lighting, realistic, volumetric lighting,

(colorful_hologram_screen), close up, cyberpunk, futuristic, space, sad

```

```#c
Negative Prompt : (KHFB, AuroraNegative),(Worst Quality, Low Quality:1.4), anime, border, nsfw, skimpy, grayscale, multiple_girls,
```
  
# **<a href="https://lensdump.com/a/EQ0jm" style="font-size: 48px; font-weight: bold;"><center>More Low CFGs</center></a>**


# **<center>Aurora ONE</center>**


</h1>
</details>
<hr>

<details id="▼-flatisjustice">

<summary style="font-size: 1.75em; font-family: monospace"><strong>Flat Color 🍭</strong></summary>
<center><a href="https://i2.lensdump.com/i/TyliSF.png"><img src="https://i2.lensdump.com/i/TyliSF.png" alt="TyliSF.png" onclick="https://i2.lensdump.com/i/TyliSF.png", '_blank')"></a></center>

<h1>
  
 ```#c
sle, (flat_color, pastel_style,anime,black_outlines:1.2),1girl,
Ninomae Ina'nis, solo, virtual youtuber, detailed eyes, coffee shop, portrait,
buttons, white shirt, collared shirt, black pants, volumetric lighting, colorful, cute
```

```#c
Negative Prompt : KHFB, AuroraNegative, (Worst Quality, Low Quality:1.4), skimpy, nsfw, grayscale, realistic, watermark
```
  
# **<a href="https://lensdump.com/a/EQIqi" style="font-size: 48px; font-weight: bold;"><center>More Flat Color</center></a>**


# **<center>Aurora ONE</center>**


</h1>
</details>
<hr>

</details>
<hr>

<details id="▼-vae">

<summary style="font-size: 2.25em; font-family: font-family: Segoe UI"><strong>✅ VAE ⚠️</strong></summary>

   <hr>
   <h1>
     
   ## I recommend <a href="https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/vae/kl-f8-anime2.ckpt" >**kl-f8-anime2.ckpt**</a> VAE from waifu-diffusion-v1-4 <a href="https://huggingface.co/hakurei">which is made by hakurei.</a>
   </h1>
   <a href="https://i.lensdump.com/i/TylmoP.jpeg"><img src="https://i.lensdump.com/i/TylmoP.jpeg" alt="TylmoP.png" onclick="window.open('https://i2.lensdump.com/i/RbBe37.png', '_blank')"></a>
   
# <h1 style="font-size: 2.5em;"><a href="https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/vae/kl-f8-anime2.ckpt" >**VAE is important, please download it.**</h1></a>
</details>
<hr>

<details id="▼-sample">
  
 <summary style="font-size: 2.25em; font-family: Segoe UI"><strong>🏔️ Examples Images</strong></summary><hr>
 
<details id="▼-autumn">

<summary style="font-size: 1.75em; font-family: monospace"><strong>Autumn 🍂</strong></summary>
<img src="https://i3.lensdump.com/i/Ty41Br.png" alt=”1”>

<h1>
  
```c#
(mksks style, detailed background:1.1),
nanashi_mumei, feather, solo, brown shirt, brown hair, long hair, comfy,
(outdoors, spring \(season\), autumn:1.3), long sleeves,
```

```c#
(KHFB, AuroraNegative),(Worst Quality, Low Quality:1.4), anime, border, nsfw, skimpy, grayscale, multiple_girls,
```

# **AURORA ONE**
</details>
<hr>

<details id="▼-spring">

<summary style="font-size: 1.75em; font-family: monospace"><strong>Spring 🌸</strong></summary>

<img src="https://i2.lensdump.com/i/TylcuM.jpeg"  alt=”2”>






```c#
(SLE, mksks style, detailed background:1.1),

(solo:1.3), nakiri ayame, red_kimono, white_hair, horns, cute, comfy, happy, portait, relaxing, volumetric_lighting,

(outdoors, spring)\(season\:1.3), cherry blossoms, cute_house, colorful
```

```c#
Negative Prompt : (KHFB, AuroraNegative),(Worst Quality, Low Quality:1.4), (multiple_girls:1.2),border, nsfw, skimpy, grayscale, umbrella, loli
```
# **AURORA ONE**
</details>
<hr>


<details id="▼-winter">

<summary style="font-size: 1.75em; font-family: monospace"><strong>Winter ❄️</strong></summary>

<img src="https://i1.lensdump.com/i/Tyz8Zc.jpeg"  alt=”5”>





```c#
(SLE, mksks style, detailed background:1.1), (solo:1.3),

ceres fauna, green_hair, antlers, yellow_eyes, mole_under eye, large_breasts,
cute, comfy, happy, portait, relaxing, standing, close_up, volumetric_lighting,

(outdoor, spring)\(winter\:1.3), snow, cute_house, colorful

```

```c#
Negative prompt: (KHFB, AuroraNegative),(Worst Quality, Low Quality:1.4), (multiple_girls:1.2),border, nsfw, skimpy, grayscale, umbrella, loli
```
# **AURORA ONE**
</details>
<hr>

<details id="▼-moon">

<summary style="font-size: 1.75em; font-family: monospace"><strong>Summer 🌻</strong></summary>

<img src="https://i3.lensdump.com/i/TylV71.jpeg"  alt=”6”>





```c#
(mksks style, detailed background:1.1), watson_amelia, (solo:1.2), (eyes_focus), virtual_youtuber,blonde_hair, cap, white_shirt, running,

(outdoors, summer \(season\):1.3), beach, relaxing, beautiful
```
```c#
(KHFB, AuroraNegative),(multiple_girls),(Worst Quality, Low Quality:1.4), border, nsfw, skimpy, grayscale,
```

# **AURORA ONE**

</details>

</details>
<hr>
</h1>

<details id="▼-demo">

<summary style="font-size: 2.25em; font-family: Segoe UI"><strong>🌏 Demo</strong></summary>
<hr>

### <h1 style="font-size: 2em;">You can try Aurora for FREE on <a href="https://discord.gg/pD9MKyBgNp">Discord </a>TXT2IMG <a href="https://discord.com/channels/1020512940526424205/1038609371367747624">channel</a></h1>
<a href="https://discord.gg/pD9MKyBgNp"><img src="https://i1.lensdump.com/i/ThtTw9.png" alt="ThtTw9.png" border="0" /></a>
</details>
<hr>

<details id="▼-merge">
<summary style="font-size: 2.25em; font-family: Segoe UI"><strong>✨ Merge Recipes</strong></summary>
<hr>
<h1><strong>
<a href="https://www.figma.com/file/3nat1kAMIxJm2lFwW56EC4/Aurora?node-id=0%3A1&t=Qb4N2OHue67ROg5W-1" class="no-underline" style="font-size: 1.75em;">Here is my Cookbook that you can check out.
  <img src="https://i1.lensdump.com/i/TylBmZ.png" alt="COOKBOOK"></strong>
  </h1>
</a>

</details>

<hr>

<details id="▼-donation">

<summary style="font-size: 2.25em; font-family: Segoe UI"><strong>💛 Donate</strong></summary>
<hr>
<h1><strong>
I've been working hard to complete my college education. The thing is, paying for college is no joke and I've been feeling the pressure of the mounting bills.

I know times are tough for everyone, but if you're able to help in any way, I would be forever grateful.

Considering supporting me on   <a href="https://www.patreon.com/thesweetluna">Patreon</a>
  </h1>
</a>

</details>
<hr>

<details id="▼-credits">

<summary style="font-size: 2.25em; font-family: Segoe UI"><strong>📝 Credits</strong></summary>
<hr>
<h1><strong>
Your tireless effort and dedication made all the difference – this model won't exist without you.
<p>Biggest thanks to <a href="https://huggingface.co/nubby">Nubby</a> and <a href="https://huggingface.co/closertodeath">CloserToDeath</a> for being there for me and helping me through a tough time. Your kindness and support mean the world to me.</p>
<p>Thank you <a href="https://huggingface.co/Aotsuyu">Aotsuyu</a>  for <a href="https://huggingface.co/Kukicha">Holokuki</a></p>
<p>Thank you <a href="https://huggingface.co/closertodeath">CloserToDeath</a>  for <a href="https://huggingface.co/closertodeath/ctdlora/blob/main/dpep4-768-000004.safetensors">DPEP4</a> and <a href="https://huggingface.co/closertodeath/ctdlora/blob/main/xlimo768.pt">Xlimo768</a></p>
<p>Thank you <a href="https://huggingface.co/nuigurumi">hesw23168</a>  for <a href="https://huggingface.co/hesw23168/Elysium_LORA/blob/main/EL_anime_boost_V1.safetensors">EL_anime_boost_V1</a></p>
<p>Thank you <a href="https://huggingface.co/nuigurumi">nuigurumi</a>  for <a href="https://huggingface.co/nuigurumi/basil_mix">BasilMix</a></p>
<p>Thank you <a href="https://huggingface.co/dolphinz">dolphinz</a>  for <a href="https://huggingface.co/dolphinz/mxlora/blob/main/kogane.safetensors">Kogane</a> and <a href="https://huggingface.co/dolphinz/stlora/blob/main/loras/sttabi_v1.4-04.safetensors">sttabi_v1.4-04</a></p>
<p>Thank you <a href="https://huggingface.co/SatyamSSJ10">SatyamSSJ10</a>  for Jordan3 (Link No Longer Exists)</a></p>
<p>Thank you <a href="https://huggingface.co/Lykon">Lykon</a>  for <a href="https://huggingface.co/Kukicha">mikaPikazoStyleLora_mk</a></p>
<p>Thank you randomaccessmemories#4004</a>  for <a href="https://cdn.discordapp.com/attachments/1067855857037094912/1067855860593852546/MagicLORA.pt">MagicLora</a></p>
<p>Thank you LUNA#1184 for the Showcase</p>  
  </h1>
</a>

</details>

<hr>

<details id="▼-suggestions">

<summary style="font-size: 2.25em; font-family: Segoe UI"><strong>💡 Suggestions</strong></summary>
<hr>

## <h1 style="font-size: 1.75em;">Loras</h1>

<hr>
    <h1 style="font-size: 1.5em;">
     
  <strong>**These Loras not required** but are meant to **enhance the effectiveness of the Lighting** and improve the overall outcome.
   <img src="https://i2.lensdump.com/i/TyzAsK.png" alt="CuteCute"></strong>
   ```c#
    BREAK mksks style, good lighting, sidelighting, backlighting, masterpiece, best quality, detailed background, scenery,
  BREAK 1girl, solo, moriya suwako, grey eyes, hat, purple dress, white sleeves, white scarf, looking at viewer, smile, close_up,
  BREAK (one knee, bus stop, outdoors:1.5), <lora:lighting-locon:0.6>
   ```
  <a href="https://huggingface.co/closertodeath/ctdlora/blob/main/locon/lighting-locon.safetensors">Lighting Locon</a> by <a href="https://huggingface.co/closertodeath">CTD</a>
  </h1>
<hr>
   
## <h1 style="font-size: 1.75em;">WebUI</h1>
<hr>
    <h1 style="font-size: 1.5em;">
   <a href="https://github.com/AUTOMATIC1111/stable-diffusion-webui">AUTOMATIC1111</a> Grab it, a must-have. Have all the features you want and is easy to access.
   <hr>
    </h1>
   
   
  
   ## <h1 style="font-size: 1.75em;">Embeddings</h1>
   <hr>
    <h1 style="font-size: 1.5em;">
      
   I recommend grabbing ***all*** <a href="https://huggingface.co/Nerfgun3">Nerfgun3</a> embeddings ***and*** Sirveggie <a href="https://huggingface.co/SirVeggie/nixeu_embeddings">nixeu_embeddings</a>

   **<a href="https://huggingface.co/SweetLuna/Aurora/tree/main/AuroraEmbeddings">Also don't forget Aurora negatives, grab them all.</a>**
 
</h1>


</details>
 <hr>

 
# License
This embedding is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

```
1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against theprovisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
```

[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

You're free to do whatever you want except selling **my model**. CivitAI doesn't have this option, but I left TL;DR, 
I couldn't care less what you do with the model after it's been merged. 
It's yours, not mine. I don't want my model to be put in shady websites.


<hr>

| Allowed | Permission                                          |
|:-------:|-----------------------------------------------------|
|    🌙    | Use the model without crediting the creator        |
|    🌙    | Sell images they generate                           |
|    ⛔    | Run on services that generate images for money      |
|    🌙    | Share merges using this model                       |
|    ⛔   | Sell this model          |
|    🌙   | Have different permissions when sharing merges      |

# Disclaimer
```c#
The use of this learning model is entirely at the discretion of the user, and they have the freedom to choose whether or not to create NSFW content. 
This is important to note that the model itself does not contain any explicit or inappropriate imagery that can be easily accessed with a single click. 
The purpose of sharing this model is not to showcase obscene material in a public forum, but rather to provide a tool for users to utilize as they see fit. 
The decision of whether to engage with SFW or NSFW content lies with the user and their own personal preferences.
```