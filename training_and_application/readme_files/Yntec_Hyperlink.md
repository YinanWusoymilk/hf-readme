---
license: creativeml-openrail-m
library_name: diffusers
pipeline_tag: text-to-image
tags:
- Photorealistic
- Realism
- Girls
- Analog
- alexds9
- text-to-image
- stable-diffusion
- stable-diffusion-diffusers
- diffusers
---

# Hyperlink

Samples and prompts:

![lady with attractive guy. photograph portrait sitting of enjoying in a close up movie in theater , cinematic 4k , epic detailed 4k epic detailed photograph shot on kodak detailed cinematic bokeh hbo dark moody. brown eyes. AI Prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/P6fK2ejCPHaF69CwLp5T5.png)

lady with attractive guy. photograph portrait sitting of enjoying in a close up movie in theater , cinematic 4k , epic detailed 4k epic detailed photograph shot on kodak detailed cinematic bokeh hbo dark moody. brown eyes

![photograph close up portrait of pretty cute Young European girl playing video game with brother wearing sombrero on sofa,happy,excited, cinematic 4k epic detailed 4k epic detailed photograph shot on kodak detailed bokeh cinematic hbo dark moody. AI prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/VE1rAMbDGdH6QBTV6ru2W.png)

photograph close up portrait of pretty cute Young European girl playing video game with brother wearing sombrero on sofa,happy,excited, cinematic 4k epic detailed 4k epic detailed photograph shot on kodak detailed bokeh cinematic hbo dark moody

![on indoor pool side, close up photograph portrait of beautiful girl sitting. lifeguard holding meat tacos, cinematic 4k epic detailed 4k epic detailed photograph shot on kodak detailed cinematic hbo bokeh. dark moody. Sweet smile. AI prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/fbN0wdyl-PM92fRHX-K51.png)

on indoor pool side, close up photograph portrait of beautiful girl sitting. lifeguard holding meat tacos, cinematic 4k epic detailed 4k epic detailed photograph shot on kodak detailed cinematic hbo bokeh. dark moody. Sweet smile

![daughter is sitting in a busy café with her beautiful granny, surrounded faces and eyes woman. little laptop computers Closeup Job search by people chatting and typing on their about the future. Photography (portrait style) with a Canon EOS R camera using a 50mm lens, Set to f/1.8, 1/200 shutter speed. The sunlight streams in through the windows, casting a warm glow on the scene. She's scrolling through job postings on her laptop, feeling both excited and nervous. AI prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/A5zbHNoiO_p7sQzMWz1gq.png)

daughter is sitting in a busy café with her beautiful granny, surrounded faces and eyes woman. little laptop computers Closeup Job search by people chatting and typing on their about the future. Photography (portrait style) with a Canon EOS R camera using a 50mm lens, Set to f/1.8, 1/200 shutter speed. The sunlight streams in through the windows, casting a warm glow on the scene. She's scrolling through job postings on her laptop, feeling both excited and nervous 

The most unique block weights from DreamPhotoGASM, HyperRealismV1.2 and LinkedIn Diffusion to improve the latter's faces and maximize its style!

Original pages:

https://civitai.com/models/158959?modelVersionId=178706 (HyperRealism 1.2)

https://huggingface.co/Yntec/lnkdn

https://huggingface.co/Yntec/DreamPhotoGASM

# HyperDreamPhotoGASM

An intermediate model created for the purposes of this mix. For better backgrounds check: https://huggingface.co/Yntec/HyperPhotoGASM - for better compositions check: https://huggingface.co/Yntec/HyperRemix

# Recipes

- SuperMerger Weight sum Use MBW 1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0

Model A: 

DreamPhotoGASM

Model B:

HyperRealism 1.2

Output Model:

HyperDreamPhotoGASM

- SuperMerger Weight sum Use MBW 0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0

Model A: 

HyperDreamPhotoGASM

Model B:

LinkedIn Diffusion

Output Model:

Hyperlink

# Weight Blocks Analysis

If the models were labeled as such:

DreamPhotoGASM = D

LinkedIn Diffusion = L

HyperRealism 1.2 = H

Its weight blocks would read like this:

H,D,D,D,D,D,D,L,L,L,L,L,L,L,L,L,L,L,L,L,D,D,D,D,D,D