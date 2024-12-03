---
license: cc0-1.0
tags:
  - stable-diffusion
  - text-to-image
---
---
## -Specializing in Japanese girls
## -Merged photo-real model mixed 5000+ Twitter images.

for Stable Diffusion Webui Automatic1111</br>
type: .safetensors(ckpt)</br>
CFG Scale: middle-low</br>

## Negative prompts are rarely needed.
example.</br>
low quality, worst quality, bad anatomy, bad proportions

## Recommended Sampler
UniPC, Dpm++ (2M/SDE) Karras, DDIM<br/>
Steps: 10～24

## Recommended VAE
vae-ft-mse-840000-ema-pruned
<br/>
<br/>
---
# Zipang XL version
-
[->here](https://huggingface.co/deadman44/SDXL_Photoreal_Merged_Models)
---
# El Zipang LL
-For LCM & LoRA<br/>
[Download](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/zipang_ll.fp16.safetensors?download=true)<br/>
### *** important ***
-When using LCM, you should<br/>
<<lora:pytorch_lora_weights:0.2>> [(Download)](https://huggingface.co/latent-consistency/lcm-lora-sdv1-5/blob/main/pytorch_lora_weights.safetensors)<br/>
sampler: DPM++ 2S a Karras (not LCM sampler)<br/>
step:6<br/>
CFG Scale:3<br/>
<br/><br/>
-When using [Myxx series Lora](https://civitai.com/user/aiai1570/models), you should<br/>
example:<<lora:myjc_v3n:0.5:0.1>>
<br/><br/>
-no Lora
[<img src=https://img92.pixhost.to/images/327/431342128_20240102210509_zipang_ll-fp16_2170481835.jpg  style="max-width: 256px;" width="50%" />](https://img92.pixhost.to/images/327/431342128_20240102210509_zipang_ll-fp16_2170481835.jpg)
-myxx Lora
[<img src=https://img92.pixhost.to/images/327/431342133_20240102211256_zipang_ll-fp16_1515340153.jpg  style="max-width: 256px;" width="50%" />](https://img92.pixhost.to/images/327/431342133_20240102211256_zipang_ll-fp16_1515340153.jpg)
-refer to pnginfo
<br/>
---
# El Zipang K
-Suitable for LoRA

[Download](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/zipangk.fp16.safetensors)<br/>

[LoRA](https://civitai.com/user/aiai1570/models)<br/>

## example
-refer to pnginfo

[<img src=https://img90.pixhost.to/images/32/387703136_myjc_v3_512.jpg  style="max-width: 256px;" width="50%" />](https://pixhost.to/show/32/387703136_myjc_v3_512.jpg)
[<img src=https://img90.pixhost.to/images/32/387703133_jpface_v2.jpg  style="max-width: 128px;" width="25%" />](https://pixhost.to/show/32/387703133_jpface_v2.jpg)
[<img src=https://img90.pixhost.to/images/32/387703139_myjk_v2.jpg  style="max-width: 128px;" width="25%" />](https://pixhost.to/show/32/387703139_myjk_v2.jpg)
[<img src=https://img90.pixhost.to/images/32/387703134_myjc_v3.jpg  style="max-width: 128px;" width="25%" />](https://pixhost.to/show/32/387703134_myjc_v3.jpg)
[<img src=https://img90.pixhost.to/images/32/387703140_myjs_v3.jpg  style="max-width: 128px;" width="25%" />](https://pixhost.to/show/32/387703140_myjs_v3.jpg)
[<img src=https://img90.pixhost.to/images/292/392534496_20231021202213_zipangk-fp16_4130861072.jpg  style="max-width: 128px;" width="25%" />](https://img90.pixhost.to/images/292/392534496_20231021202213_zipangk-fp16_4130861072.jpg)
---
# El Zipang
-Mixed 5000+images

[Download](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/El%20Zipang_pruned_fp16.safetensors)<br/>
- Photo-Real</br>
photo realistic:+++++</br>
portrait:++++</br>
pose:+++</br>
hand:++</br>

[<img src=https://i.imgur.com/bh1To6tm.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/bh1To6t)[<img src=https://i.imgur.com/Zk5rWc0m.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/Zk5rWc0)[<img src=https://i.imgur.com/oKi7o17m.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/oKi7o17)[<img src=https://i.imgur.com/Of7YoTxm.png.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/Of7YoTx)[<img src=https://i.imgur.com/t11u8xfm.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/t11u8xf)[<img src=https://i.imgur.com/J74LwDMm.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/J74LwDM)

## example
```jsx
realistic, photorealistic, detailed, beautiful, RAW photo, film grain, (natural lighting :1.2), (wrinkled skin:1.1),
japanese, 1girl, happy, short black hair, brown eyes, bangs, camisole, close-up, facing viewer, photo background
Negative prompt: (worst quality, low quality, normal quality:1.8), painting, drawing
Steps: 28, Sampler: UniPC, CFG scale: 3.5, Seed: 2272109148, Size: 512x768, Model hash: b7cbea183c, Denoising strength: 0.18, Hires upscale: 2, Hires upscaler: SwinIR_4x
```
-Recommended prompt: (photoreal tips)
```jsx
realistic, photorealistic, detailed, beautiful, RAW photo, film grain, (natural lighting, perfect lighting:1.5), wrinkled skin, day,
Negative prompt:
(worst quality, low quality, normal quality:1.8), painting, drawing, greyscale
CFG scale: 3
Hires: 2-4x
```
-
Anything4.5(base trained) + uncanny valley(my other model:Any3.0+EZ test series) Brock Weight Merged
---
# Optional (LoRA)

## JP Face_v2: [Download](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/jpface_v2.safetensors)<br/>
768x768 dim512<br/>
## JP Face: [Download](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/jpface.safetensors)<br/>
512x512 dim128<br/>

-trigger: japanese

[<img src=https://i.imgur.com/BeMNpuW.jpg  style="max-width: 256px;" width="50%" />](https://i.imgur.com/BeMNpuW)[<img src=https://i.imgur.com/z3tEvu0.jpg  style="max-width: 256px;" width="50%" />](https://i.imgur.com/z3tEvu0)
```jsx
cute, realistic, photorealistic, detailed, beautiful, RAW photo, film grain, wrinkled skin, (natural lighting:1.4)
japanese, 1girl, solo, black hair, head tilt, brick wall, looking at viewer, lips, long brown hair, smile, bangs, upper body, turtleneck, long sleeves, white ribbed sweater, brown eyes <lora:jpface:1>
Negative prompt: (worst quality:1.5), bad anatomy, extra digit, greyscale
Steps: 34, Sampler: DPM++ 2M SDE Karras, CFG scale: 4, Seed: 1789550705, Size: 768x512, Model hash: b7cbea183c, Denoising strength: 0.3, Clip skip: 2, Token merging ratio: 0.5, Token merging ratio hr: 0.5, Hires upscale: 2, Hires steps: 30, Hires upscaler: R-ESRGAN 4x+ Anime6B, Lora hashes: jpface: bc0b0c346d61, Version: v1.3.0
```

How to use:
```jsx
<lora:jpface:1>
```

---
---

# OLD TestVersion
-Specializing in Japanese girls Test Model
-Merged photo-real model mixed 1000+ Twitter images.


# El Zipang_test1.4
-Mixed 2000+images<br/>
-The composition and the human body are even less fragile. Maybe...

[test_no_zipang.safetensors](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/test_no_zipang.safetensors) + [El Zipang_test1.3.safetensors](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/El%20Zipang_test1.3.safetensors) -> Simple Merge!!!

-
test no Zipang
Anything3.0(base trained) + EZ test1.0 Brock Weight Merged
----

# El Zipang_test1.3
[Download](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/El%20Zipang_test1.3.safetensors)<br/>
-Just changed the block-weighted merge ratio.<br/>
-Better hands and better poses than 1.0. Maybe...<br/>
thanks, supermerger!!!<br/>
http://github.com/hako-mikan/sd-webui-supermerger/<br/>

[<img src=https://i.imgur.com/GyKs8Up.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/GyKs8Up)
[<img src=https://i.imgur.com/sXnAGF8.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/sXnAGF8)
[<img src=https://i.imgur.com/zE77vws.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/zE77vws)

-
EZ test1.0 + Anything3.0 Merged
----

# El Zipang_test1.0(test01)
[Download](https://huggingface.co/deadman44/SD_Photoreal_Merged_Models/resolve/main/El%20Zipang_test01.safetensors)<br/>
- Photo-Real</br>
photo realistic:+++++</br>
portrait:+++++</br>
pose:+</br>
hand:+</br>

[<img src=https://i.imgur.com/MK6MUu0.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/MK6MUu0)[<img src=https://i.imgur.com/HmSC45w.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/HmSC45w)[<img src=https://i.imgur.com/Qs1DJyS.png  style="max-width: 128px;" width="25%" />](https://i.imgur.com/Qs1DJyS)[<img src=https://i.imgur.com/G0KhpMu.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/G0KhpMu)[<img src=https://i.imgur.com/wk69lFK.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/wk69lFK)[<img src=https://i.imgur.com/dYG6xTp.png   style="max-width: 128px;" width="25%" />](https://i.imgur.com/dYG6xTp)

## example
<img src=https://i.imgur.com/KuWcOxX.png>

```jsx
japanese, 1girl, solo, looking at viewer, long hair, couch, black hair, smile, realistic, bangs, long sleeves, black eyes, brown eyes, upper body, sitting, fingernails, lips, school uniform, closed mouth
Negative prompt: low contrast, lowers, normal quality, low quality, worst quality, bad anatomy, bad proportions
Steps: 10, Sampler: DPM++ SDE Karras, CFG scale: 5, Seed: 185236819, Size: 512x768, Model hash: c785dff0
```
-Recommended prompt:
```jsx
japanese, realistic, 1girl, 
Negative prompt:
normal quality, low quality, worst quality, bad anatomy, bad proportions, 
CFG scale: 4-8
```
-
SD1.5(base trained) + F222 + Cafe Insta Merged
----






