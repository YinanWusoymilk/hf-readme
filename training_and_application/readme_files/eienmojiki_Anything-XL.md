---
license: other
license_name: faipl-1.0-sd
license_link: https://freedevproject.org/faipl-1.0-sd
pipeline_tag: text-to-image
tags:
- text-to-image
- merge
- StableDiffusionXL
- StableDiffusionXLPipeline
- Anime
language:
- en
library_name: diffusers
---

<style>
  @font-face {
    font-family: 'AegirSeaborn';
    src: url('./assets/AegirSeaborn.ttf');
    /* Thay đổi 'path/to/font' thành đường dẫn đúng tới font đã tải về */
  }
  
  .title-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Adjust this value to position the title vertically */
  }
  
  .title {
    font-size: 2.5em;
    text-align: center;
    color: #333;
    font-family: 'AegirSeaborn';
    /* Thay đổi 'FontName' thành tên font đã tải về */
    /* text-transform: uppercase; */
    letter-spacing: 0.1em;
    padding: 0.5em 0;
    background: transparent;
  }

  .title span {
    background: -webkit-linear-gradient(45deg, #7DF9FF, #0096FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
</style>

<h1 class="title">
  <span>Anything-XL</span>
</h1>

## Intro
- Original author: **Yuno779**
- Main repository: https://civitai.com/models/9409/or-anything-xl
- Last update: Mar 10, 2024

## PLEASE NOTE THAT
1. Abandon your irrelevant high-definition restoration, unless you want to generate images above 2048x2048 or there are serious problems with the generated image content
2. If you feel that the model is biased towards a certain aspect or has any other problems, please check the prompt words first. Some of the cue words themselves didn't work on the model you were using before, but may work here.
3. Please **do not use SDXL according to the usage habits of SD1.5**. Essentially, the models are different. If necessary please use the quality words given below instead of 8k HD etc.
4. It is best not to use it with NegativeXL, and it is not recommended to use heavily weighted negative prompt words such as (ugly:2).
5. If you want a good picture, please describe its content in as much detail as possible instead of **just marking "1girl, nsfw"**. This will not produce any good pictures.

## Usage & Recommendation
### Parameters+：
Prompt words are different from SD1.5, and for best results, it is recommended to follow a structured prompt template:

```bash
<|special|>, 
<|artist|>, 
<|special(optional)|>, 
<|characters name|>, <|copyrights|>, 
<|quality|>, <|meta|>, <|rating|>，……

<|tags|>, 
```
### Special tags：
**years:**
```bash
newest	        2021 to 2024
recent	        2018 to 2020
mid	            2015 to 2017
early	        2011 to 2014
old             2005 to 2010
```
> [!NOTE] These words help guide the results towards modern and retro anime art styles, with a specific timeframe of approximately 2005 to 2023

**NSFW:**
```bash
safe	            General
sensitive	        Sensitive
nsfw	            Questionable
explicit, nsfw	    Explicit
```
> [!NOTE] These words help guide the results towards adult content, but generally do not generate adult content if rating words are not included.
> *Of course, you can also put it in negative prompts.*

**quality** 
```bash
masterpiece	            > 95%
best quality	        > ?
great quality	        > ?
good quality	        > ?
normal quality	        > ?
low quality	            > ?
worst quality	        ≤ 10%
```
> [!NOTE] While this model can function without quality words, in practice, these words can still be used to adjust the output.

**Resolution:**
> [!NOTE] You are free to use the vast majority of reasonable resolutions, whether it is the resolution used by SD1.5 at 512*768 or higher resolutions above 2048, each will have a different effect. However, using images that are too large or too small may cause the picture to break down or the character/background structure to become distorted.

**Tags:** 
> [!NOTE] If you want to generate high-quality pictures, you can use negative prompts, such as:

```bash
nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, artist name
Negative tags can include common negative tags, but it is best not to assign too high of a weight to their content, for example (ugly:2.8).
```
> [!IMPORTANT] Negative tags can include common negative tags, but it is best not to assign too high of a weight to their content, for example (ugly:2.8).
> Because of models merge, some labels in the original model that have not been fully trained may be lost, and some labels may need to have a weight of over 1.5 in order to be effective.

### Resolution:
A resolution greater than 1024×1024 is recommended, and hires fix is recommended if you want higher resolution or quality

Most of the generation parameters of the example graph are:

```bash
euler_a | 20steps | no hires fix | CFG7
```
```bash
2048 x 2048     not recommended
……
1280 x 2048     
1280 x 1536     
960  x 1536     Recommended
1024 x 1024	    1:1   Square
…… 
960  x 640                
768  x 512      SD1.5
……
2048 x 512      ¿  Unable to guarantee the quality
512  x 2048     ¿  Unable to guarantee the quality
```
## License
AnythingXL uses the [**Fair AI Public License 1.0-SD**](https://freedevproject.org/faipl-1.0-sd/), compatible with Stable Diffusion models.