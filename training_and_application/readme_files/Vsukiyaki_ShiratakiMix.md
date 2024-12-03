---
license: creativeml-openrail-m
language:
- ja
tags:
- stable-diffusion
- text-to-image
---
# ◆ ShiratakiMix

<img src="https://huggingface.co/Vsukiyaki/ShiratakiMix/resolve/main/imgs/header.jpg">

##　概要 / Overview

- **ShiratakiMix**は、2D風の画風に特化したマージモデルです。 / **ShiratakiMix** is a merge model that specializes in 2D-style painting styles.
- VAEはお好きなものをお使いください。VAEを含んだモデルも提供しています。 / You can use whatever VAE you like. I also offer models that include VAE.

  
=> **ShiratakiMix-add-VAE.safetensors**
<hr>

## ギャラリー / gallery
<div>
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="https://huggingface.co/Vsukiyaki/ShiratakiMix/resolve/main/imgs/sample1.png" style="width: 50%">
        <img src="https://huggingface.co/Vsukiyaki/ShiratakiMix/resolve/main/imgs/sample2.png" style="width: 50%">
    </div>
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="https://huggingface.co/Vsukiyaki/ShiratakiMix/resolve/main/imgs/sample3.png" style="width: 50%">
        <img src="https://huggingface.co/Vsukiyaki/ShiratakiMix/resolve/main/imgs/sample4.png" style="width: 50%">
    </div>
</div>

<hr>

## 推奨設定 / Recommended Settings

<pre style="margin: 1em 0; padding: 1em; border-radius: 5px; background: #25292f; color: #fff; white-space: pre-line;">
  Steps: 20 ~ 60
  Sampler: DPM++ SDE Karras
  CFG scale: 7.5
  Denoising strength: 0.55
  Hires steps: 20
  Hires upscaler: Latent or R-ESRGAN 4x+ Anime6B
  Clip skip: 2
</pre>

Negative:
<pre style="margin: 1em 0; padding: 1em; border-radius: 5px; background: #25292f; color: #fff; white-space: pre-line;">
  (easynegative:1.0),(worst quality,low quality:1.2),(bad anatomy:1.4),(realistic:1.1),nose,lips,adult,fat,sad, (inaccurate limb:1.2),extra digit,fewer digits,six fingers,(monochrome:0.95)
</pre>

<hr>

## 例 / Examples

<details>
<summary>サンプル1</summary>
<img src="https://huggingface.co/Vsukiyaki/ShiratakiMix/resolve/main/imgs/sample5.png" style="width: 768px">

<pre style="margin: 1em 0; padding: 1em; border-radius: 5px; background: #25292f; color: #fff; white-space: pre-line;">
  Prompt:
  cute girl,outdoor,scenery
  
  Negative prompt:
  (easynegative:1.0),(worst quality,low quality:1.2),(bad anatomy:1.4),(realistic:1.1),nose,lips,adult,fat,sad, (inaccurate limb:1.2),extra digit,fewer digits,six fingers,(monochrome:0.95)
  
  Steps: 28
  Sampler: DPM++ SDE Karras
  CFG scale: 7.5
  Seed: 3585317650
  Size: 768x544
  Denoising strength: 0.55
  Clip skip: 2
  Hires upscale: 2.5
  Hires steps: 20
  Hires upscaler: Latent
</pre>

</details>
<br>
<details>
<summary>サンプル2</summary>
<img src="https://huggingface.co/Vsukiyaki/ShiratakiMix/resolve/main/imgs/sample6.png" style="width: 768px">

<pre style="margin: 1em 0; padding: 1em; border-radius: 5px; background: #25292f; color: #fff; white-space: pre-line;">
  Prompt:
  cute girl,indoors,antique shop,many antique goods,shop counter,display shelf,apron,happy smile,perspective
  
  Negative prompt:
  (easynegative:1.0),(worst quality,low quality:1.2),(bad anatomy:1.4),(realistic:1.1),nose,lips,adult,fat,sad, (inaccurate limb:1.2),extra digit,fewer digits,six fingers,(monochrome:0.95)
  
  Steps: 40
  Sampler: DPM++ SDE Karras
  CFG scale: 7.5
  Seed: 4267597555
  Size: 768x544
  Denoising strength: 0.55
  Clip skip: 2
  Hires upscale: 2.5
  Hires steps: 20
  Hires upscaler: Latent
</pre>
</details>
<br>
<details>
<summary>サンプル3</summary>
<img src="https://huggingface.co/Vsukiyaki/ShiratakiMix/resolve/main/imgs/sample7.png" style="width: 768px">
  
<pre style="margin: 1em 0; padding: 1em; border-radius: 5px; background: #25292f; color: #fff; white-space: pre-line;">
  Prompt:
  cute little girl standing in a Mediterranean port town street,wind,pale-blonde hair, blue eyes,very long twintails,white dress,white hat,blue sky,laugh,double tooth,closed eyes,looking at viewer,lens flare,dramatic, coastal
  
  Negative prompt:
  (easynegative:1.0),(worst quality,low quality:1.2),(bad anatomy:1.4),(realistic:1.1),nose,lips,adult,fat,sad, (inaccurate limb:1.2),extra digit,fewer digits,six fingers,(monochrome:0.95)
  
  Steps: 60
  Sampler: DPM++ SDE Karras
  CFG scale: 7.5
  Seed: 265342725
  Size: 768x544
  Denoising strength: 0.55
  Clip skip: 2
  Hires upscale: 2.5
  Hires steps: 20
  Hires upscaler: Latent
</pre>
</details>
<br>
<details>
<summary>サンプル4</summary>
<img src="https://huggingface.co/Vsukiyaki/ShiratakiMix/resolve/main/imgs/sample8.png" style="width: 512px">

<pre style="margin: 1em 0; padding: 1em; border-radius: 5px; background: #25292f; color: #fff; white-space: pre-line;">
  Prompt:
  (solo), cute little (1girl) walking,path,[from below:1.2],brown hair,sine short hair,brown eyes,puddle,Water Reflection,rain,floating water drop,hydrangea,(blurry foreground),dynamic angle,asphalt,(blue sky),lens flare,school uniform,(glitter:1.2)
  
  Negative prompt:
  (easynegative:1.0),(worst quality,low quality:1.2),(bad anatomy:1.4),(realistic:1.1),nose,lips,adult,fat,sad, (inaccurate limb:1.2),extra digit,fewer digits,six fingers,(monochrome:0.95)
  
  Steps: 28
  Sampler: DPM++ SDE Karras
  CFG scale: 7.5
  Seed: 415644494
  Size: 544x768
  Denoising strength: 0.55
  Clip skip: 2
  Hires upscale: 2.5
  Hires steps: 20
  Hires upscaler: Latent
</pre>

</details>



<hr>

## ライセンス / License

<div class="px-2">
  <table class="table-fixed border mt-0 text-xs">
    <tbody>
      <tr>
        <td class="px-4 text-base text-bold" colspan="2">
          <a href="https://huggingface.co/spaces/CompVis/stable-diffusion-license">
            CreativeML OpenRAIL-M ライセンス / CreativeML OpenRAIL-M license
          </a>
        </td>
      </tr>
      <tr>
        <td class="align-middle px-2 w-8">
          <span style="font-size: 18px;">
            ✅
          </span>
        </td>
        <td>
          このモデルのクレジットを入れずに使用する<br>
          Use the model without crediting the creator
        </td>
      </tr>
      <tr>
        <td class="align-middle px-2 w-8">
          <span style="font-size: 18px;">
            ✅
          </span>
        </td>
        <td>
          このモデルで生成した画像を商用利用する<br>
          Sell images they generate
        </td>
      </tr>
      <tr class="bg-danger-100">
        <td class="align-middle px-2 w-8">
          <span style="font-size: 18px;">
            ✅
          </span>
        </td>
        <td>
          このモデルを商用の画像生成サービスで利用する</br>
          Run on services that generate images for money
        </td>
      </tr>
      <tr>
        <td class="align-middle px-2 w-8">
          <span style="font-size: 18px;">
            ✅
          </span>
        </td>
        <td>
          このモデルを使用したマージモデルを共有する<br>
          Share merges using this model
        </td>
      </tr>
      <tr class="bg-danger-100">
        <td class="align-middle px-2 w-8">
          <span style="font-size: 18px;">
            ✅
          </span>
        </td>
        <td>
          このモデル、またはこのモデルをマージしたモデルを販売する</br>
          Sell this model or merges using this model
        </td>
      </tr>
      <tr class="bg-danger-100">
        <td class="align-middle px-2 w-8">
          <span style="font-size: 18px;">
            ✅
          </span>
        </td>
        <td>
          このモデルをマージしたモデルに異なる権限を設定する</br>
          Have different permissions when sharing merges
        </td>
      </tr>
    </tbody>
  </table>
</div>

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage. The CreativeML OpenRAIL License specifies:

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content

2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license

3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully) Please read the full license here ：https://huggingface.co/spaces/CompVis/stable-diffusion-license

<br>

#### 【和訳】

このモデルはオープンアクセスであり、すべての人が利用できます。CreativeML OpenRAIL-M ライセンスにより、権利と使用方法がさらに規定されています。CreativeML OpenRAIL ライセンスでは、次のことが規定されています。

1. モデルを使用して、違法または有害な出力またはコンテンツを意図的に作成または共有することはできません。

2. 作成者は、あなたが生成した出力に対していかなる権利も主張しません。あなたはそれらを自由に使用でき、ライセンスに設定された規定に違反してはならない使用について説明責任を負います。

3. 重みを再配布し、モデルを商用および/またはサービスとして使用することができます。その場合、ライセンスに記載されているのと同じ使用制限を含め、CreativeML OpenRAIL-M のコピーをすべてのユーザーと共有する必要があることに注意してください。 (ライセンスを完全にかつ慎重にお読みください。) [こちらからライセンス全文をお読みください。](https://huggingface.co/spaces/CompVis/stable-diffusion-license)

<hr>

## マージ元モデル / Merged models

<dl>
  <dt><a href="https://civitai.com/models/21200/color-box-model">・ Color Box Model / CreativeML OpenRAIL M</a>
  </dt>
    <dd>└ colorBoxModel_colorBOX</dd>
  <dt><a href="https://huggingface.co/Printemps/ProllyMix">・ ProllyMix / CreativeML OpenRAIL M</a>
  </dt>
    <dd>└ IceProllyMix-v1</dd>
  <dt><a href="https://huggingface.co/haor/Evt_M">・ Evt_M / CreativeML OpenRAIL M</a>
  </dt>
    <dd>└ Evt_M_fp16</dd>
  <dt><a href="https://huggingface.co/natsusakiyomi/SakuraMix">・ SakuraMix / CreativeML OpenRAIL M</a>
  </dt>
    <dd>└ SakuraMix-v2</dd>
  <dt><a href="https://huggingface.co/ploughB660/BalorMix-V4">・ BalorMix-V4 / CreativeML OpenRAIL M</a>
  </dt>
    <dd>└ BalorMix-V4.2featACT</dd>
</dl>
<hr>

## レシピ / Recipe

<details>

### Step: 1 ｜ 階層マージ

Tool: Merge Block Weighted
| Model: A |      Model: B      | Base alpha | Skip/Reset CLIP position_ids |     Merge Name     |
| :------: | :----------------: | :--------: | :--------------------------: | :----------------: |
|  colorBoxModel_colorBOX   | IceProllyMix-v1 |    0.42     |             None             | ShiratakiMix-baseA |

Weight:
<pre style="margin: 1em 0; padding: 1em; border-radius: 5px; white-space: pre-line;">
  1,0.9166666667,0.8333333333,0.75,0.6666666667,0.5833333333,0.5,0.4166666667,0.3333333333,0.25,0.1666666667,0.0833333333,
  0,
  0.0833333333,0.1666666667,0.25,0.3333333333,0.4166666667,0.5,0.5833333333,0.6666666667,0.75,0.8333333333,0.9166666667,1.0
</pre>
<br>

### Step: 2 ｜ 階層マージ
Tool: Merge Block Weighted
| Model: A |      Model: B      | Base alpha | Skip/Reset CLIP position_ids |     Merge Name     |
| :------: | :----------------: | :--------: | :--------------------------: | :----------------: |
|  Evt_M   | ShiratakiMix-baseA |    1.0     |             None             | ShiratakiMix-baseB |

Weight:
<pre style="margin: 1em 0; padding: 1em; border-radius: 5px; white-space: pre-line;">
  1,0.9166666667,0.8333333333,0.75,0.6666666667,0.5833333333,0.5,0.4166666667,0.3333333333,0.25,0.1666666667,0.0833333333,
  0,
  0.0833333333,0.1666666667,0.25,0.3333333333,0.4166666667,0.5,0.5833333333,0.6666666667,0.75,0.8333333333,0.9166666667,1.0
</pre>

<br>

### Step: 3 ｜ 階層マージ
Tool: Toolkit / Merge Block Weighted

**◆ Converted model.**


 SakuraMixV2.ckpt[afbd69c0cd] ==> **SakuraMixV2.safetensors[79b4a1d065]**
|     Model: A     |      Model: B      | Base alpha | Skip/Reset CLIP position_ids |     Merge Name     |
| :--------------: | :----------------: | :--------: | :--------------------------: | :----------------: |
| SakuraMixV2 | ShiratakiMix-baseB |    1.0    |             None             | ShiratakiMix-baseC |

Weight:
<pre style="margin: 1em 0; padding: 1em; border-radius: 5px; white-space: pre-line;">
  1,0.97974537037037,0.921296296296296,0.828125,0.703703703703704,0.55150462962963,0.375,0.177662037037037,0.0370370370370372,0.265625,0.50462962962963,0.750578703703704,
  1.0,
  0.750578703703704,0.504629629629629,0.265624999999999,0.0370370370370372,0.177662037037038,0.375,0.551504629629631,0.703703703703703,0.828125,0.921296296296298,0.979745370370369,1
</pre>

<br>

### Step: 4 ｜ 階層マージ

Tool: Merge Block Weighted
|      Model: A      |     Model: B      | Base alpha | Skip/Reset CLIP position_ids |    Merge Name     |
| :----------------: | :---------------: | :--------: | :--------------------------: | :---------------: |
| ShiratakiMix-baseC | BalorMix-V4.2featACT |     0.05      |             None             | ShiratakiMix |

Weight:
<pre style="margin: 1em 0; padding: 1em; border-radius: 5px; white-space: pre-line;">
  0.1,0.1,0,0,0,0,0,0,0.1,0.1,0,0,0,0.1,0.1,0,0,0,0,0,0,0,0,0.1,0.1
</pre>

=> **ShiratakiMix.safetensors [d3849c69d9]**

<br>

### Step: 5 ｜ 修復
Tool: Toolkit
<pre style="margin: 1em 0; padding: 1em; border-radius: 5px; white-space: pre-line;">
  Contains no junk data. CLIP had incorrect positions, fixed: 7, 14, 19, 28, 33, 38, 43, 56, 61.

  Model will be fixed (9 changes).
</pre>

=> **ShiratakiMix-fixed.safetensors [ded0c94f95]**
</details>

<hr>

Twiter: [@Vsukiyaki_AIArt](https://twitter.com/Vsukiyaki_AIArt)


<a
  href="https://twitter.com/Vsukiyaki_AIArt"
  class="mb-2 inline-block rounded px-6 py-2.5 text-white shadow-md"
  style="background-color: #1da1f2">
  <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="currentColor" viewBox="0 0 24 24">
    <path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z" />
  </svg>
</a>