---
license: creativeml-openrail-m
language:
- ja
tags:
- stable-diffusion
- text-to-image
---

## VAE

VAEは不要です。<br>

VAE is unneccessary.

<hr>

# ◆ SE_V3_A sample
![通常使用](https://huggingface.co/Deyo/SEmix/resolve/main/sample4.png)

```
Prompt:
(best quality:1.4),(1girl:1.3),(bob cut:1.2),silver hair,off shoulder white dress,ribbon on side hair, blue eyes,hair ribbon red ribbon on side hair

Negative:
EasyNegativeV2,(worst quality:1.4),(low quality:1.4),(monochrome:1.1)

Steps: 30
Sampler: DPM++ 2M Karras
CFG scale: 7
Clip skip: 2

```
<br>

![応用例](https://huggingface.co/Deyo/SEmix/resolve/main/sample3.png)
```
応用例
```


# ◆ SE_V1_A

**SE_V1_AはEmiPhaV4をベースに改良を加えたモデルです。<br>
NegativeにEasyNegativeを使用することを推奨します。

**SE_V1_A is an improved model based on EmiPhaV4.  
It is recommended that you use EasyNegative embedding as negative.

## VAE

VAEは不要です。<br>

VAE is unneccessary.

<hr>

![メイドちゃん](https://huggingface.co/Deyo/SEmix/resolve/main/sample1.png)

```
Prompt:
1 girl,cat ears, maid,

Negative:
EasyNegative,(worst quality,low quality,monochrome:1.2),(bad hands:1.3),

Steps: 30
Sampler:  DPM++ SDE Karras
CFG Scale: 9
Size: 768x1024
Seed: 2062380749
Clip skip: 2

```

<br>

# ◆ SE_V1_A sample
![銀髪ちゃん](https://huggingface.co/Deyo/SEmix/resolve/main/sample2.png)

```
Prompt:
1 girl,schooluniform,silver hair,blue eyes,

Negative:
EasyNegative,(worst quality,low quality,monochrome:1.2),(bad hands:1.3),

Steps: 30
Sampler: DPM++ SDE Karras
CFG Scale: 9
Size: 768x1024
Seed: 3175303220
Clip skip: 2


```

# ◆ Licence

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
<hr>

Twiter: [@Deyoyoyo](https://twitter.com/Deyoyoyo)

Twiter: [@narinrain](https://twitter.com/narinrain)
