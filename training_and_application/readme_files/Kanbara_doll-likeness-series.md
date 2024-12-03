---
license: creativeml-openrail-m
---


# Doll Series by Kbr

The 'Doll-Series' is a set of LORA focused on realistic Asian faces, with incredible levels of beauty and aesthetics.

My Pixiv: https://www.pixiv.net/en/users/92373922

My Twitter: https://twitter.com/KbrLoras

---

# Table of Contents

- [License](#license)
- [Disclaimer](#disclaimer)
- [Used Models](#used-models)
- [LORA Detail](#lora-detail)
  - [KoreanDollLikeness](#koreandolllikeness)
    - [KoreanDollLikeness_v10](#koreandolllikeness_v10)
    - [KoreanDollLikeness_v15](#koreandolllikeness_v15)
    - [KoreanDollLikeness_v20](#koreandolllikeness_v20)
  - [JapaneseDollLikeness](#japanesedolllikeness)
    - [JapaneseDollLikeness_v10](#japanesedolllikeness_v10)
    - [JapaneseDollLikeness_v15](#japanesedolllikeness_v15)
  - [TaiwanDollLikeness](#taiwandolllikeness)
    - [TaiwanDollLikeness_v15](#taiwandolllikeness_v15)
    - [TaiwanDollLikeness_v20](#taiwandolllikeness_v20)
  - [ChinaDollLikeness](#chinadolllikeness)
    - [ChinaDollLikeness_v10](#chinadolllikeness_v10)
  - [ThaiDollLikeness](#thaidolllikeness)
    - [ThaiDollLikeness_v10](#Thaidolllikeness_v10)

- [FAQ](#faq)



---
# License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
(Full license here: https://huggingface.co/spaces/CompVis/stable-diffusion-license)

# Additional Add-ons to license/notes
1. You shall take full responsibility for any creative work that uses this model
2. Refrain from using this model for malicious intent, harm, defamation, scam or political usages. It may impair and discourage the author from producing more works.

# Disclaimer

- Creation of SFW and NSFW images is user's decision, user has complete control over to generate NSFW content whether or not.

---

# Used Models

* Chilled_re_generic_v2

  - https://github.com/wibus-wee/stable_diffusion_chilloutmix_ipynb

* chilloutmix_cilloutmixNi

  - https://civitai.com/models/6424/chilloutmix
    

  # Recommended settings:
- Make sure you are aware on the usage instructions of LORA

- VAE: vae-ft-mse-840000-ema-pruned (For realistic models)

- Sampler: DPM++ SDE Karras (Recommended for best quality, you may try other samplers)
- Steps: 20 to 35
- Clipskip: 1 or 2
- Upscaler : Latent (bicubic antialiased)
- CFG Scale : 5 to 9
- LORA weight for txt2img: anywhere between 0.2 to 0.7 are recommended
- Denoise strength for img2img: 0.4 to 0.7


---
# LORA Detail
---
## KoreanDollLikeness

The first version that is widely used by many authors/AI artist/creators

### KoreanDollLikeness_v10

  - KoreanDollLikeness_v10:

<img src="https://files.catbox.moe/r61ozj.png" width="" height="">

### KoreanDollLikeness_v15

  - KoreanDollLikeness_v15:

<img src="https://files.catbox.moe/pgcfhc.png" widht="" height="">

### KoreanDollLikeness_v20

  - KoreanDollLikeness_v20:

<img src="https://files.catbox.moe/thehrt.png" widht="" height="">

---

## JapaneseDollLikeness

The Japanese variant version, subjected for v15 in the future

### JapaneseDollLikeness_v10

  - JapaneseDollLikeness_v10:

<img src="https://files.catbox.moe/cfypot.png" width="" height="">

### JapaneseDollLikeness_v15

  - JapaneseDollLikeness_v15:

<img src="https://files.catbox.moe/doa0n2.png" width="" height="">

---

## TaiwanDollLikeness

The Taiwan variant version, I have decided to discontinue v10, it is still out there somewhere in the internet, you may still find it.

### TaiwanDollLikeness_v15

  - TaiwanDollLikeness_v15:

<img src="https://files.catbox.moe/5vr2z4.png" width="" height="">

### TaiwanDollLikeness_v20

This version is a huge overhaul and remake, instead of building upon v10 or v15, I took small amount of samples from v10 and introduced a new pool of training images.

  - TaiwanDollLikeness_v20:

<img src="https://files.catbox.moe/f8c9mb.png" width="" height="">

---

## ChinaDollLikeness

The China variant version, took awhile despite the requests, will probably make more versions of it in the future.

### ChinaDollLikeness_v10

<img src="https://files.catbox.moe/zpj9ov.png" width="" height="">

---

## ThaiDollLikeness

The Thai variant version, took me a long time to make this, many versions were made but this version is the one I've deemed the best out of all. Might update in the future.

### ThaiDollLikeness_v10

<img src="https://files.catbox.moe/imtxsm.png" width="" height="">


# FAQ
- # Q: Why can't I produce the same pictures as you?
- A: Sorry I don't share my prompt, you may check the recommended settings, but you may ask me for advice on Twitter or Pixiv
  
- # Q: What is the difference of each version upgrade?
- A: Version upgrade does not mean it will fix hands or legs, it is mainly difference of the face of the LORA, newer versions have wider range of faces.

- # Q: Will you release all your other LORAs?
- A: Yes, maybe, but I would like to keep certain LORA to be exclusive to fans or supporters in the future through fanbox/ko-fi

- # Q: Do you take requests or commissions on making custom LORAs?
- A: I might do community voting for requests, if you are somehow interested in a custom/exclusive LORA, you may contact my through Pixiv or Twitter for discussion

---
