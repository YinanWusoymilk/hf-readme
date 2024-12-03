---
license: agpl-3.0
---

# Cafe Instagram Unofficial Test v2

This is a test model created to assess the Waifu Diffusion training code, and not intended to be a full-featured or official release.

This model has been trained from `runwayml/stable-diffusion-v1-5` for approximately 1.6 epochs on 1.2m images total from various Instagram accounts (primarily Japanese). As the model is undertrained, its performance is marginal. Mixing the model is recommended for better performance.

Natural language descriptions (using BLIP), as well as [booru tags](https://huggingface.co/SmilingWolf/wd-v1-4-vit-tagger) have been used to assist in captioning. Any Instagram hashtags were also included in the caption data.

*Note: Training was done using various aspect ratios, with a base resolution of 768x768, as well as the penultimate CLIP layer. Clip skip of 2 and a resolution of 768x768 or higher is recommended for generations.*

![Example](https://huggingface.co/cafeai/cafe-instagram-sd-1-5-v6/resolve/main/example.jpg)

Example:
```
waifu, instagram, cute girl, japaneseidol, idol, アイドル, 自撮り女子, photorealistic, photo, 可愛い, kawaii, cute, gravure, fashion, 1girl, solo, cleavage, cowboy shot
Negative prompt: (((mutated hands and fingers))), ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed face))), ((ugly)), ((bad anatomy)), (((bad proportions))), (((extra limbs))), extra face, ((double head)), ((extra head)), (big breast), (((extra feet))), monster, (text), (logo), (blurry), text, english text, watermark, logo, (((anime)))
```

This model is released under the aGPL. You can use this for whatever you like. If you make changes, share them.
