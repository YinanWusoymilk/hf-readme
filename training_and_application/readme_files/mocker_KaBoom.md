---
license: creativeml-openrail-m
language:
- en
tags:
- art
---
# In short,

- FaceBomb : Covers from anime to 2.5D style. Suited for general use.
  - recipe : 0.5((0.5(AbyssOrangeMix2_hard) + 0.5(pastelmix-better-vae-fp32)) + 0.5(CounterfeitV25_25)) + 0.5(dalcefoV3Painting_dalcefoV3Painting)

- ColorBomb : FaceBomb + vivid color and lighting. A bit picky about prompts.
  - recipe : dalcefoV3Painting_dalcefoV3Painting + 0.5(ultracolorV4_ultracolorV4 - CounterfeitV25_25)

- HyperBomb : Strong anime style w/ highly saturated color.
  - recipe : 0.5((0.5(AbyssOrangeMix2_hard) + 0.5(pastelmix-better-vae-fp32)) + 0.5(CounterfeitV25_25)) + 0.5(dalcefoV3Painting_dalcefoV3Painting) + 0.3(0.8(pastelMixStylizedAnime_pastelMixPrunedFP16) + 0.2(CounterfeitV25_25) - f222)

# Recommended Setting

## VAE
- If the color appears dull or washed out, try applying VAE. I used `kl-f8-anime2`
- https://huggingface.co/hakurei/waifu-diffusion-v1-4/blob/main/vae/kl-f8-anime2.ckpt

## Sampling method and Hires.fix
1. `DPM++ SDE Karras: 24~32 steps` / `R-ESRGAN 4x+ Anime6B: 2x, 14 steps` / `Denoising strength:0.45 ~ 0.55` 
2.  `DDIM: 24~32 steps` / `Latent: 2x 14 steps` / `Denoising Strength:0.45 ~ 0.7`
- First option yields better result in general. Recommended.
- Second option was 1.5 ~ 2 times faster on my system but the output was questionable. Especially for ColorBomb.

## FaceBomb
- Positive : `(masterpiece, sidelighting, finely detailed beautiful eyes: 1.2), masterpiece*portrait, realistic, 3d face, lustrous skin, `
- Negative : `(worst quality, low quality:1.4), watermark, logo,`

## ColorBomb
- Positive : `(masterpiece, sidelighting, finely detailed beautiful eyes: 1.2), (ultra-detailed, high-resolution: 1.2), beautiful girl, { color } { color } theme, `
	- e.g. black gold theme
- Negative : `(worst quality, low quality:1.4), watermark, logo,`

## HyperBomb
- Positive : `(masterpiece, sidelighting, finely detailed beautiful eyes: 1.2),`
- Negative : `(worst quality, low quality:1.4), watermark, logo,`

# Example
- More pictures in folder. 
- Below are the ideal/intended outputs.

![Alt text](sample/00184-20230207043613___Custom_FaceBombMix-fp16-no-ema_aad629159b.png)
### FaceBomb
	(masterpiece, sidelighting, finely detailed beautiful eyes: 1.2), masterpiece*portrait, realistic, 3d face, glowing eyes, shiny hair, lustrous skin, solo, embarassed  
	Negative prompt: (worst quality, low quality:1.4), watermark, logo,  
	Steps: 32, Sampler: DPM++ SDE Karras, CFG scale: 9, Seed: 3624413002, Size: 512x768, Model hash: aad629159b, Model: __Custom_FaceBombMix-fp16-no-ema, Denoising strength: 0.5, Clip skip: 2, ENSD: 31337, Hires upscale: 2, Hires steps: 14, Hires upscaler: R-ESRGAN 4x+ Anime6B

---

![Alt text](sample/00217-20230207050723___Custom_ColorBomb-fp16-no-ema_627f50eea8.png)
### ColorBomb
	((masterpiece, best quality, ultra-detailed, high-resolution)), solo, beautiful girl, gleaming eye, perfect eye, age 15, black white gold theme,  
	Negative prompt: (worst quality, low quality:1.4), (depth of field, blurry:1.2), (greyscale, monochrome:1.1), 3D face, cropped, lowres, text, jpeg artifacts, signature, watermark, username, blurry, artist name, trademark, watermark, title, (tan, muscular, sd character:1.1), multiple view, Reference sheet, non-linear background, blurred background, bad anatomy, cropped hands, extra digit, fewer digit,  
	Steps: 24, Sampler: DDIM, CFG scale: 7, Seed: 3050494714, Size: 512x768, Model hash: 627f50eea8, Model: __Custom_ColorBomb-fp16-no-ema, Denoising strength: 0.7, Clip skip: 2, ENSD: 31337, Hires upscale: 2, Hires steps: 14, Hires upscaler: Latent

---

![Alt text](sample/00212-20230207050130___Custom_HyperBombMix-fp16-no-ema_16c6ca45b1.png)
### HyperBomb
	(masterpiece, sidelighting, finely detailed beautiful eyes: 1.2),  
	Negative prompt: (worst quality, low quality:1.4), watermark, logo,  
	Steps: 32, Sampler: DDIM, CFG scale: 9, Seed: 2411870881, Size: 768x512, Model hash: 16c6ca45b1, Model: __Custom_HyperBombMix-fp16-no-ema, Denoising strength: 0.7, Clip skip: 2, ENSD: 31337, Hires upscale: 2, Hires steps: 14, Hires upscaler: Latent