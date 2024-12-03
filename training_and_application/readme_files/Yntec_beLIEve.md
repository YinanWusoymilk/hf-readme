---
license: creativeml-openrail-m
language:
- en
library_name: diffusers
pipeline_tag: text-to-image
tags:
  - Base Model
  - Realism
  - Photorealistic
  - Person
  - Portrait
  - residentchiefnz
  - PromptSharingSamaritan
  - stable-diffusion
  - stable-diffusion-diffusers
  - text-to-image
  - diffusers
inference: true
---

# beLIEve

I Can't Believe It's Not Photography v1 mixed with realisticStockPhoto v3 to improve the details of the former and the facial variety of the latter!

Samples and prompts:

![a cute girl with freckles on her face, cgsociety unreal engine, wet t-shirt, short skirt, style of aenami alena, trending on artstartion, inspired by Fyodor Vasilyev, looks a bit similar to amy adams, emissive light, fluffy skin, blonde, dribbble, dramatic rendering. sweet smile, brown eyes. AI prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/HyU-I5CW50Fr6ES59WGFV.png)

a cute girl with freckles on her face, cgsociety unreal engine, wet t-shirt, short skirt, style of aenami alena, trending on artstartion, inspired by Fyodor Vasilyev, looks a bit similar to amy adams, emissive light, fluffy skin, blonde, dribbble, dramatic rendering. sweet smile, brown eyes

![phone photo of gandalf in the forest with elf girl, uploaded on snapchat. AI prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/H2YhZlikSzlkLBHbniqiV.png)

phone photo of gandalf in the forest with elf girl, uploaded on snapchat

![90s cinematic colored sitcom screenshot. young husband with wife portrait. festive scene at a bronze brewery with a wooden keg of enjoying tomato burrito in the center. sitting cute little daughter. Display mugs of dark beer. accompanied by halloween ingredients. Closeup. beautiful eyes. smile. AI prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/1fBbjhhnGkJ004h-NqHQx.png)

90s cinematic colored sitcom screenshot. young husband with wife portrait. festive scene at a bronze brewery with a wooden keg of enjoying tomato burrito in the center. sitting cute little daughter. Display mugs of dark beer. accompanied by halloween ingredients. Closeup. beautiful eyes. smile

![ultra high resolution, a cute girl, detailed photography, zelda princess, AS Younger, cute pose. AI prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/YBr_VkELxymmPNXyAvIc3.png)

ultra high resolution, a cute girl, detailed photography, zelda princess, AS Younger, cute pose

Original pages:

https://civitai.com/models/139565?modelVersionId=524032 (Realistic Stock Photo 3 SD1.5)

https://civitai.com/models/28059?modelVersionId=33626 (I Can't Believe It's Not Photography v1)

# Recipe

- SuperMerger Weight sum Use MBW 0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1

Model A: 

icbinpICantBelieveIts_v10_pruned

Model B:

realisticStockPhoto_v30SD15

Output Model:

beLIEve