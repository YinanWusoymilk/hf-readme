---
license: openrail
---

# 2d pixel art (beta) embedding for SD 2.0 768px

Hi - I am a big fan of retro/nostalgia things. 
This is the reason why I made this embedding. 
I have trained it on 70 images, the version I will be targeting in upcoming weeks will be based on 128 or 256 well-selected and filtered images, and processed
through pixelate tool to keep the same pixel size on each of the input data. This should improve the embedding dramatically.

**Images:**

<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/lVqWhmx.png">
</div>
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/eMZvUTY.png">
</div>
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/fyGB10h.png">
</div>
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/SJGs2nD.png">
</div>
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/R7t1zrG.png">
</div>
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/rLyeX7J.png">
</div>
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/9eOUMiD.png">
</div>
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/bfknB8t.png">
</div>
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/3bXwXMh.png">
</div>



### Installation:

Just drop the embedding files (.pt extension) to your SD embeddings folder (`your-folder/embeddings`).
Restart the app if running. Use the keyword as a filename ("pixelart" for example). You can rename them as you wish.

Before we start: cool tool to enhance your results even further: [link](https://giventofly.github.io/pixelit/#tryit)

**Version of Stable Diffusion:** `2.0 - 768`
**Supported diffusers:** 
- Euler a (Preffered)
- DDIM 
- other (partially)



### Embeddings

**pixelart:**
The most generic one. Usually gives decent pixels, reads quite well prompts, is not to "old-school".
Used for "pixelating process" in img2img. 

**pixelart-soft:**
The softer version of an embedding. One of the most generic ones.Usually good for characters.

**pixelart-hard:**
More pixelated version of embedding. Vintage/old-school. Depends on the topic - can be colorful or very vintage/dull.

**pixelart-1 & pixelart-2:**
less generic ones. These sometimes give even better results than original (depends on topic, tags and diffuser)

**pixelizer:**
Fun but chaotic one. Good for some experiments but usually gives colorful 8-bit like pixelated platformers/game screens stuff.
I have left that one for experiments or as a factor for combination with other ones.

### Usage

I highly recommend use these embeddings with `Euler a` diffuser. It will give usually best results. In some cases it would be
good to use negative prompts. Sometimes for testing if you caught good composition/colors - you might add or remove them
to impact the image.

**negative prompt**:
Recommend this negative to test stuff when you get bad results:
"3d, 3d render, disfigured, kitsch, ugly, oversaturated, grain, low-res, Deformed, blurry, bad anatomy, 
disfigured, poorly drawn face, mutation, mutated, extra limb, ugly, poorly drawn hands, missing limb, blurry, 
floating limbs, disconnected limbs, malformed hands, blur, out of focus, long neck, long body, ugly, disgusting, 
poorly drawn, childish, mutilated, mangled, old, surreal"

If you have too much pixelated/chaotic output - add (all or some): 
"grid, Tetris, tetris blocks, mosaic, mosaic, pixelated, pixel art"

### Img2img

The embeddings give you a great opportunity to change some of your works into pixel ones.
The best way to do it is to follow this process:

First get your subject. If this is a simple image as:
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/ks4bpSV.png">
</div>

Here it needed just one step!

What I did here was to use: 
**Positive prompt:** "game icon, raven, by pixelart, pixelated" (very important to add pixelated)
**Negative prompt:** none (recommended, but you can of course experiment, especially if subject needs that)
**Sampler:** Euler a (needed for any pixelation)
**steps:** 20, 
**CFG:** 7, 
**Denoising:** 0.58. 
**Resolution:** 768x768.

The result:
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/wErverC.png">
</div>

 Of course, the result can be better - you can re-roll to infinity or choose better settings or different embedding than recommended pixelart (in some cases you can try others)

Pixelating photos/more complex images:
This is more tricky - but doable. As a baseline use the above settings,
you can experiment with higher/lower CFG or denoising. To keep likeness I don't recommend you to go over 0.6 denoising.
Replace the first part of the prompt with a simple description, at the end should be part: "by/in style pixelart, pixelated"
Probably this will take up to 2-3 rounds. When I like the output - I set it as a base for next iteration. Then I reduce denoising by 0.4 each
extra round.
Of course this is rough process - might be different based on images.

Here are some examples:

Input:
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/l2dGhgH.png">
</div>

Resuts:
<div style="display: flex; flex-direction: row; flex-wrap: wrap">
  <img src="https://i.imgur.com/zsrd92w.png">
</div>

I still investigating how to improve on the process.