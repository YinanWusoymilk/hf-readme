---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
datasets: embed/EasyNegative
---

# Check the new [Ambientmix](https://huggingface.co/OedoSoldier/ambientmix)!

## Descriptions

Using this model will result in clean, anatomically-correct images that accurately capture the essence of anime-style art, complete with stunning backgrounds.

Two models are provided: an 18 MB LoRA model and a full base model that merges LoRA with Anything V4.5. The full model is recommended for training your character model, and is particularly effective for training anime characters using this model.

## Recommend settings:

 - VAE: Orangemix (the same with NAI)
 - LoRA Strength: 1 (if you're using the LoRA version)
 - Sampler: DPM++ 2M Karras
 - Sampling steps: 20
 - Negative embedding: [EasyNegative](https://civitai.com/models/7808)、[badhandv4](https://civitai.com/models/16993/badhandv4-animeillustdiffusion)

## Samples

Note: all the LoRA name used in those samples are my local name, you need to change them to your saved LoRA filename!

![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/1.png)
```
masterpiece, best quality, 1girl, solo, light smile, mountain, lake, meadow, panorama, jacket, kneehighs, boots
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 738622193, Size: 576x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/2.png)
```
masterpiece, best quality, 1girl, solo, looking_at_viewer, smile, open_mouth, skirt, shirt, hair_ornament, pink_hair, jacket, pink_hair, :d, multicolored_hair, pleated_skirt, wings, choker, hairclip, hood, pink_eyes, hair_bun, chibi, black_shirt, double_bun, black_choker, blush, white_skirt, feathered_wings, angel_wings, white_wings, sky, flying, halo, hand up, skyscraper, angel, from top
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 4110544683, Size: 576x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/3.png)
```
masterpiece, best quality, 1girl, solo, looking away, expressionless, from side, white dress, colorful, floral background, rain, lake, fog, barefoot, sitting on water, from top, 
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 223540873, Size: 576x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/4.png)
```
masterpiece, best quality,1girl, adjusting clothes, adjusting headwear, blush, bow, bowtie, breasts, brown eyes, brown hair, cloak, cloud, cloudy sky, crescent moon, dress, fantasy, flower, glowing, glowing flower, hat, light particles, lily pad, long hair, looking at viewer, moon, moonlight, mountain, mountainous horizon, night, outdoors, parted lips, pointy ears, pond, sky, small breasts, star (sky), starry sky, very long hair, wading, water lily flower, wind, witch, witch hat
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1795361781, Size: 512x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/5.png)
```
best quality, extremely detailed CG unity 8k,close up, illustration, depth of field,cowboy shot,the character is centered,symmetrical composition, (1 girl),red eyes,Wolf tail,Wolf ears,Very long hair ,Messy hair,disheveled hair, ,(beautiful detailed eyes),(Crown:1.1),pleated dress,puffy long sleeves, (moon:1.2), ((The black clouds)),(((flowing transparent black))),(floating black cloud:1.2),building architecture, depth of field,castle,black and white melt

Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 4091383013, Size: 512x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/6.png)
```
masterpiece, best quality, 1man, solo, jacket, hand in pocket, school bag, black hair, black eyes, cyberpunk, street, machinery, motor vehicle, motorcycle, panorama, sunglasses
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 223585745, Size: 576x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/7.png)
```
masterpiece, best quality, 1boy, flat color, limited palette, low contrast, (ligne claire), long straight black hair, looking away, standing. smoke, night sky, city, sunset, sky scrapers, bridge, depth of field, black, red, orange, brown, autumn, haze,
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 646089941, Size: 576x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/8.png)
```
masterpiece, best quality, 1girl, smile, one eye closed, dutch angle, blonde hair, twintails, blue eyes, cowboy shot, maid dress, heart hands
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 278484553, Size: 512x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/9.png)
```
masterpiece, best quality, 1girl, solo, long_hair, looking_at_viewer, smile, dress, ribbon, jewelry, very_long_hair, hair_ribbon, flower, bracelet, two_side_up, hand_on_own_face, head_rest, hand_on_own_cheek
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1453509491, Size: 512x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/10.png)
```
masterpiece, best quality, 1girl, solo, black hair, medium hair, red eyes, blunt bangs, petite, expressionless, red skirt, white legwear, thighhighs, suspender skirt, white shirt, mary janes, night, dark, shadow
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 407943314, Size: 512x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/11.png)
```
masterpiece, best quality, 1girl, solo, long_hair, looking_at_viewer, white hair, red eyes, smile, bangs, skirt, shirt, long_sleeves, hat, dress, bow, holding, closed_mouth, flower, frills, hair_flower, petals, bouquet, holding_flower, center_frills, bonnet, holding_bouquet, flower field, flower field, colorful
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1690640466, Size: 576x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/12.png)
```
impasto,((((1girl)))),Metaverse,original,((an extremely delicate and beautiful)),(cyan theme),((intricate detail)),((((ultra-detailed))),((illustration)),(((masterpiece))),((extremely detailed CG unity 8k wallpaper)),highlight,sharpening,detailed face,((Perfect details)),(binary numbers),Science fiction,sense of digital,cold light,((data in the eyes)),((data adorns hair)),0 and 1 code,digitization,Running data,system screen,mathematical equation,young girl,(solo),(yubao)
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 293734715, Size: 576x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/13.png)
```
masterpiece, best quality, 1girl, solo, long_hair, from top, light smile, panorama, perspective, looking_at_viewer, bangs, skirt, shirt, black_hair, long_sleeves, bow, ribbon, twintails, hair_bow, heart, pantyhose, frills, shoes, choker, blunt_bangs, black_skirt, pink_eyes, frilled_skirt, pink_bow, platform_footwear, pink_theme, jirai_kei, full body, night, street, from behind, looking back, skyscraper, neon trim, panorama, perspective, starry sky, black theme, dark, shadow
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1148006396, Size: 576x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/14.png)
```
masterpiece,1girl,solo,incredibly absurdres,hoodie,headphones, street,outdoors,rain,neon lights, light smile, hood up, hands in pockets, looking away, from side
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3552918625, Size: 576x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/15.png)
```
masterpiece, best quality,1girl, solo, bangs, bare shoulders, bat wings, blonde hair, blush, breasts, bridal gauntlets, seductive smile, eyes visible through hair, fingernails, garter straps, hair ornament, long hair, looking at viewer, pointy ears, red eyes, small breasts, thighhighs, castle, vampire, white thighhighs, wings, night, standing, grin
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3007804048, Size: 576x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/16.png)
```
anirl, best quality, ultra high res, 1girl, hatsune miku, full body, scenery, smile, ocean, sunset, city, barefoot, footprints, sand
Negative prompt: EasyNegative, badhandv4
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3051695426, Size: 576x768, Model hash: ad0e54efe2, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2.5, Hires steps: 10, Hires upscaler: SwinIR_4x
```
![](https://huggingface.co/OedoSoldier/anime-screenshot-like-mix/resolve/main/samples/17.png)

## Models used

Merged with block weights tweaked:

 - 2020s Anime Magazine Illustration Style
 - Anime-like 2D (extracted LoRA)
 - Anime Lineart Style
 - Anime Screencap Style
 - Avas Anime Hamster


 - Epi Noise Offset
 - Hipoly 3D Model Lora

 - Makoto Shinkai Substyles

## See also

Original post on Civitai: https://civitai.com/models/23723