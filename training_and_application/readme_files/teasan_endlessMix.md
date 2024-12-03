---
license: creativeml-openrail-m
language:
- ja
tags:
- art
- stable-diffusion
library_name: diffusers
---

# ■endlessMixシリーズについて

![](image/logo.png)

## 概要

このモデルはDefactaをベースにした階層マージモデルです。  
モデル作者である私が勉強用と自分使用目的に制作しました。  
なお、VAEは導入されていないので別途DLしてください。  


## 使い方

モデルをcloneもしくはDLした後、以下に格納してください。

```
  webui\models\Stable-diffusion\
```

### 推奨設定（作者の設定）

#### V9シリーズ

- Sampler: DPM++ 2M Karras
- Step: 20 ~ 50
- CFG scale: 7～15
- Denoising strength: 0.55 ~ 0.6
- Clip skip: 2
- Hires upscale: 2
- Hires steps: 10 ~ 13 or 0
- Hires upscaler: Latent (nearest)
- VAE: <a href="https://huggingface.co/hakurei/waifu-diffusion-v1-4/tree/main/vae" target="_blank">kl-f8-anime2</a>

#### V8シリーズ

- Sampler: DPM++ 2M Karras
- Step: 20 ~ 50
- CFG scale: 7～15
- Denoising strength: 0.55 ~ 0.6
- Clip skip: 2
- Hires upscale: 2
- Hires steps: 10 ~ 13 or 0
- Hires upscaler: Latent (nearest)
- VAE: <a href="https://huggingface.co/hakurei/waifu-diffusion-v1-4/tree/main/vae" target="_blank">kl-f8-anime2</a>

#### V7

- Sampler: DPM++ 2M Karras
- Step: 20 ~ 50
- CFG scale: 7～15
- Denoising strength: 0.55 ~ 0.6
- Clip skip: 2
- Hires upscale: 2
- Hires steps: 10 ~ 13 or 0
- Hires upscaler: Latent (nearest)
- VAE: <a href="https://huggingface.co/hakurei/waifu-diffusion-v1-4/tree/main/vae" target="_blank">kl-f8-anime2</a>

#### V6

- Sampler: DPM++ 2M Karras
- Step: 20 ~ 50
- CFG scale: 7～15
- Denoising strength: 0.55 ~ 0.6
- Clip skip: 2
- Hires upscale: 2
- Hires steps: 10 ~ 13 or 0
- Hires upscaler: Latent (nearest)
- VAE: <a href="https://huggingface.co/hakurei/waifu-diffusion-v1-4/tree/main/vae" target="_blank">kl-f8-anime2</a>

#### V3

- Sampler: DPM++ 2M Karras
- Step: 20 ~ 30
- CFG scale: 7～15
- Denoising strength: 0.55 ~ 0.6
- Clip skip: 2
- Hires upscale: 2
- Hires steps: 10 ~ 13 or 0
- Hires upscaler: Latent (nearest)
- VAE: <a href="https://huggingface.co/hakurei/waifu-diffusion-v1-4/tree/main/vae" target="_blank">kl-f8-anime2</a>

#### V2

- Sampler: DPM++ 2M Karras
- Step: 20 ~ 30
- CFG scale: 11
- Denoising strength: 0.55 ~ 0.6
- Clip skip: 2
- Hires upscale: 2
- Hires steps: 10 ~ 13
- Hires upscaler: Latent (nearest) or R-ESRGAN 4x+
- VAE: <a href="https://huggingface.co/hakurei/waifu-diffusion-v1-4/tree/main/vae" target="_blank">kl-f8-anime2</a> or <a href="https://huggingface.co/sp8999/test_VAE/blob/main/mse840000_klf8anime_klf8anime2.vae.pt" target="_blank">mse840000_klf8anime_klf8anime2</a>

#### V1

- Sampler: DPM++ 2M Karras
- Step: 30
- CFG scale: 11
- Denoising strength: 0.55
- Clip skip: 2
- Hires upscale: 2
- Hires steps: 10
- Hires upscaler: Latent (nearest)
- VAE: <a href="https://huggingface.co/hakurei/waifu-diffusion-v1-4/tree/main/vae" target="_blank">kl-f8-anime2</a>

### 出力サンプル

<details>
<summary>endlessMixV9</summary>
<div>

ALL  
![](image/v9/grid.png)

2dMix  
![](image/v9/01.png)

realMix  
![](image/v9/02.png)

oldFix  
![](image/v9/03.png)

```
  ▲プロンプト
absurdres, highres, 
1girl,
Negative prompt: EasyNegative, [ :(negative_hand-neg:1.2):15 ], (worst quality, low quality:1.4), text, monochrome, nsfw
```


～～～～～～～～～

</div>
</details>

<details>
<summary>endlessMixV8</summary>
<div>

通常版  
![](image/v8/img01.png)

kawaii_fix  
![](image/v8/img02.png)

oldFix  
![](image/v8/img03.png)

```
  ▲プロンプト
absurdres, highres,
(1girl, solo), big eyes,
townscape,
(Water Effects, Light Effects, Fluttering Feathers:1.2),
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, text, grid view, nsfw,
```

通常版  
![](image/v8/img04.png)    

```
  ▲プロンプト
absurdres, highres, (official art, beautiful and aesthetic:1.2),
(1girl:1.45), (fractal art:1.3), zentangle, kaleidoscope, (colorfield painting:1.15), (flower effects:0.8), wild style art,
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, text, grid view, nsfw,
```

kawaii_fix  
![](image/v8/img05.png)    

```
  ▲プロンプト
absurdres, highres,
(1girl, solo),
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, text, grid view, nsfw,
```

通常版  
![](image/v8/img06.png)    

```
  ▲プロンプト
absurdres, highres,
1girl, big eyes,  high ponytail,☺, [ red | orange ] hair,
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, text, grid view, nsfw,
```


～～～～～～～～～

</div>
</details>

<details>
<summary>endlessMixV7</summary>
<div>

![](image/v7/img01.png)

```
  ▲プロンプト
absurdres, highres,  (ultra-detailed background, detailed background), extremly detailed,
(1girl, solo), big eyes, kawaii, toddler, loli,
townscape,
(Water Effects, Light Effects, Fluttering Feathers:1.2),
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, grid view, nsfw,
```

![](image/v7/img02.png)    

```
  ▲プロンプト
absurdres, highres,  (ultra-detailed background, detailed background), extremly detailed,
(1girl, solo:1.2), 🥰,
(colorfield painting:1.3), (zentangle:1.3), flower effects, (fractal art:1.15),
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, grid view, nsfw,
```

![](image/v7/img03.png)    

```
  ▲プロンプト
absurdres, highres,  (ultra-detailed background, detailed background), extremly detailed,
(1girl, solo:1.2), 🥰,
(colorfield painting:1.3), (zentangle:1.3), flower effects, (fractal art:1.15),
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, grid view, nsfw,
```


![](image/v7/img04.png)    

```
  ▲プロンプト
absurdres, highres,  (ultra-detailed background, detailed background), extremly detailed,
1gir, artist style, (Fashion Magazine Cover:1.2), (zentangle:1.3), material effects,
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, grid view, nsfw,
```


～～～～～～～～～

</div>
</details>

<details>
<summary>endlessMixV6</summary>
<div>

![](image/v6/img01.png)

```
  ▲プロンプト
absurdres, highres,  (ultra-detailed background, detailed background), extremly detailed,
(1girl, solo), (kawaii:1.2),
([ water effects | Light Effects | Feathers effects ]:1.3),
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, grid view, nsfw,
```

![](image/v6/img02.png)    

```
  ▲プロンプト
absurdres, highres, ultra detailed, (ultra-detailed background, detailed background), extremly detailed,
(1girl, solo:1.2), 🥰,
(colorfield painting:1.3), (zentangle:1.3), flower effects, (fractal art:1.15),
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, text, grid view, nsfw,
```

![](image/v6/img03.png)    

```
  ▲プロンプト
absurdres, highres, ultra detailed,
1girl, full body, big eye, (toddler, loli, kawaii, expressionless face, cute girl, ( [blue | shining] eye ), small face:1.2), Ruffled Dresses, BREAK 
cel shading, (bold outlines):1.2, flat colors, sharp shadows, graphic style, manga influence, clean 
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, text, grid view, nsfw,
```


![](image/v6/img04.png)    

```
  ▲プロンプト
absurdres, highres, ultra detailed,
1girl, full body, big eye, (toddler, loli, kawaii, expressionless face, cute girl, ( [blue | shining] eye ), small face:1.2), Ruffled Dresses, BREAK 
cel shading, (bold outlines):1.2, flat colors, sharp shadows, graphic style, manga influence, clean 
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, text, grid view, nsfw,
```


～～～～～～～～～

</div>
</details>


<details>
<summary>endlessMixV3.5</summary>
<div>

![](image/v3/img01.png)

```
  ▲プロンプト
absurdres, highres, ultra detailed, Ultra-precise depiction, Ultra-detailed depiction, (ultra-detailed background, detailed background), extremly detailed,
1gir, solo, zentangle, (Fashion Magazine Cover:1.4),
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, text, grid view, nsfw,
```

![](image/v3/img02.png)    

```
  ▲プロンプト
absurdres, highres,  (ultra-detailed background, detailed background), extremly detailed,
1gir, artist style, (Fashion Magazine Cover:1.5), (zentangle:1.3), material effects,
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, grid view, nsfw,
```

![](image/v3/img03.png)    

```
  ▲プロンプト
absurdres, highres,  (ultra-detailed background, detailed background), extremly detailed,
(1girl, solo:1.2), 🥰,
(colorfield painting:1.3), (zentangle:1.3), flower effects, (fractal art:1.15),
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, grid view, nsfw,
```


![](image/v3/img04.png)    

```
  ▲プロンプト
absurdres, highres,  (ultra-detailed background, detailed background), extremly detailed,
(1girl, solo), big eyes, kawaii, toddler, loli,
townscape,
(Water Effects, Light Effects, Fluttering Feathers:1.2),
Negative prompt: EasyNegative, bad-hands-5, (worst quality:2), Bad Anatomy, crumpled limbs, bad hands, bad fingers, missing fingers, missing arms, missing legs, extra digit, watermark, username, artist name, signature, grid view, nsfw,
```


～～～～～～～～～

</div>
</details>

<details>
<summary>endlessMixV2シリーズ</summary>
<div>

![](image/v2/grid.png)

```
  ▲プロンプト
  (masterpiece, top quality, best quality, official art, beautiful and aesthetic:1.2),
(1girl, solo), (kawaii:1.2),
([ water effects | Light Effects | Feathers effects ]:1.3),
Negative prompt: EasyNegative, bad-hands-5, (worst quality:1.4), (low quality:1.4), text, grid view, nsfw, crumpled limbs, Bad Anatomy,
```

![](image/v2/grid02.png)    

```
  ▲プロンプト
  (masterpiece, top quality, best quality, official art, beautiful and aesthetic:1.2),
(1girl, solo), 
Negative prompt: EasyNegative, bad-hands-5, (worst quality:1.4), (low quality:1.4), text, grid view, nsfw, crumpled limbs, Bad Anatomy,
```

～～～～～～～～～

</div>
</details>

<details>
<summary>endlessMixV1</summary>
<div>

![](image/v1/grid.jpg)

～～～～～～～～～

</div>
</details>


----

# 免責事項

- SFWおよびNSFW画像の作成は、個々のクリエイターの判断によります。モデル製作者は責任を負いません。
- このモデルは、公共の場などでNSFWコンテンツを公開するために作られたモデルではありません。

---

# 当モデルの使用にあたって

以下の事項守っていただき、<strong>常識の範囲内</strong>でご使用ください。  

✅ 本モデルで生成した画像を商用利用する行為   
✅ 本モデルを使用したマージモデルを使用または再配布する行為   
✅ 本モデルのクレジット表記をせずに使用する行為   
❌ 本モデルを商用の画像生成サービスで利用する行為　  
❌ 本モデルや本モデルをマージしたモデルを販売する行為  
❌ 本モデルを使用し意図的に違法な出力をする行為   
❌ 本モデルをマージしたモデルに異なる権限を与える行為   
❌ 本モデルをマージしたモデルを配布または本モデルを再配布した際に同じ使用制限を含め、CreativeML OpenRAIL-M のコピーをすべてのユーザーと共有しない行為

---
# Stable Diffusionのライセンスについて

- このモデルはオープンアクセスで誰でも利用可能であり、CreativeML OpenRAIL-Mライセンスでさらに権利と使用方法が規定されています。
- CreativeML OpenRAILライセンスでは、次のように規定されています。
1. このモデルを使用して、違法または有害な出力やコンテンツを意図的に作成したり、共有したりすることはできません。
2. 作者はあなたが生成した出力に対していかなる権利も主張しません。あなたはそれらを自由に使用することができますが、ライセンスで定められた規定を守ってください。利用は自己責任でお願いします。
3. あなたはウェイトを再配布し、モデルを商業的またはサービスとして使用することができます。その場合、ライセンスにあるものと同じ使用制限を含め、CreativeML OpenRAIL-Mのコピーをあなたのすべてのユーザーに共有しなければならないことに注意してください（ライセンスを完全にかつ注意深く読んでください）。
- (ライセンスの全文: [https://huggingface.co/spaces/CompVis/stable-diffusion-license](https://huggingface.co/spaces/CompVis/stable-diffusion-license))

---

# 作者について
twitter：<a href="https://twitter.com/wims_Tea" target="_blank"> https://twitter.com/wims_Tea</a>

---