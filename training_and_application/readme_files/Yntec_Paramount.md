---
language:
- en
license: creativeml-openrail-m
tags:
- General
- Photorealistic
- Sexy
- Girls
- CornmeisterNL 
- SG161222
- wavymulder
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: false
---

# Paramount

A mix of Paragon 1.0 and AnalogMadness to bring their versatility and style in a single model. Now with Analog Diffusion added for good measure!

Samples and prompts (click for larger versions, scroll down for more):

![1990 movie screenshot. young husband with beautiful wife. festive scene at a copper brewery with a wooden keg of beer in the center. sitting cute girl. Display mugs of dark beer. faces. accompanied Shirley by halloween ingredients AI prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/xFKRbxXsxZobfgwR0EUK7.png)

1990 movie screenshot. young husband with beautiful wife. festive scene at a copper brewery with a wooden keg of beer in the center. sitting cute girl. Display mugs of dark beer. faces. accompanied Shirley by halloween ingredients

![absurdres, adorable cute harley quinn, at night, dark alley, moon, :) face. red ponytail, blonde ponytail, in matte black hardsuit, military, roughed up, bat, city fog, AI prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/bx2-Kpg1ZJx6V66ar9Wot.png)

absurdres, adorable cute harley quinn, at night, dark alley, moon, :) face. red ponytail, blonde ponytail, in matte black hardsuit, military, roughed up, bat, city fog,

![kodachrome camera transparency. dramatic lighting faces. PARTY HARD BACKGROUND, closeup, young guy with pretty cute little daughter in Zone 51, film grain, looking Extraterrestrial, Alien Space Ship Delivering Christmas Presents, Alien Space Ship Decorated With Garlands and Christmas Balls, Snowstorm AI prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/tr9cihs1gOtqH0WiQv2Rt.png)

kodachrome camera transparency. dramatic lighting faces. PARTY HARD BACKGROUND, closeup, young guy with pretty cute little daughter in Zone 51, film grain, looking Extraterrestrial, Alien Space Ship Delivering Christmas Presents, Alien Space Ship Decorated With Garlands and Christmas Balls, Snowstorm 

![blonde pretty Princess Peach wearing crown in the mushroom kingdom AI prompt](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/UwnWpYifpJP8Dxmd32ci9.png)

blonde pretty Princess Peach wearing crown in the mushroom kingdom

![Top Text to image prompts](https://cdn-uploads.huggingface.co/production/uploads/63239b8370edc53f51cd5d42/6o7TkZe8kGi94fLBERg6d.png)

Top left: Pretty Cute Girl, holding jackpot coins, beautiful detailed slot machine, Detailed Eyes, gorgeous detailed hair, pants, Magazine ad, iconic, 1943, from the movie, sharp focus. visible brushstrokes ​by ROSSDRAWS and Clay Mann

Top right: Focused gaze, boxer stance, black gloves with teal accents, pretty cute girl with intense eyes, close-up, shallow depth of field, high contrast, cool color temperature, direct lighting, sharp focus on eyes, blurred foreground sparring glove, dynamic tension, determination, sweat-glistening skin, peek-through composition, anticipation atmosphere, gym setting suggested, personal struggle narrative, resilience symbolism

Bottom left: riding motorcycle. closeup photo of a baby pelican, forest, haze, halation, bloom, dramatic atmosphere, centred, rule of thirds, 200mm 1.4f macro shot

Bottom right: 60s TV screenshot of pretty cute little daughter as Marie Antoinette playing on toy harp in bedroom. braids, detailed eyes. smile

Original pages:

https://civitai.com/models/8030?modelVersionId=9519 (Analog Madness 1.1)

https://huggingface.co/SG161222/Paragon_V1.0

https://huggingface.co/wavymulder/Analog-Diffusion/

# Paramount Alpha & Beta

I produced these merges to make one involving Analog Diffusion, to have distinct outputs. Originally the diffusers version was based on Paramount Alpha, after testing it was clear it should be based on this one instead. Then I renamed it as the Beta version when I added Analog Diffusion in.

You can compare their outputs for similar prompts here: https://huggingface.co/Yntec/Paramount/discussions/3

# Recipes

SuperMerger Weight sum MBW 0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1

Model A: AnalogMadness 1.1

Model B: Paragon 1.0

Output: ParamountBeta

SuperMerger Weight sum MBW 1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,1,1,1

Model A: AnalogMadness 1.1

Model B: Paragon 1.0

Output: ParamountAlpha

- SuperMerger Add Difference Train Difference Alpha 1

Model A: Analog Diffusion

Model B: ParamountAlpha

Model C: Stable Diffusion 1.5

Output: ParamountDiffusion

- SuperMerger Weight sum Train Difference 0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1

Model A: ParamountBeta

Model B: ParamountDiffusion

Model C: Stable Diffusion 1.5

Output: AnalogParamount

- SuperMerger Weight sum 0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1

Model A: AnalogParamount

Model B: ParamountDiffusion

Output: Paramount