---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
- diffusers
- safetensors
language:
- ja
---

# このモデルは何？
- 個人的な普段遣いのためにマージしたモデルです、癖が強いと思います。
- 頭身低めの女の子を出力するように調整していますので他のモデルより年齢操作の加減が必要かもしれません。また女の子以外の出力には期待しないでください。
- （個人的こだわりで）できるだけ目のハイライトを失わないようにマージしてあります。指の描写にも気を使ったつもりですがプロンプト次第で簡単に破綻します。
- VAEは外部のものを使用するなりご自身で焼き込んでください。サンプルは基本AnythingのVAEを使用しています。個人的に普段はclearVAEシリーズを使っています。
- 既存のLoRAとのマッチングについては個人的にLoRAをあまり使わないため未検証です。上手く反映されないことのほうが多いでしょう。
- Samplerは何でも大丈夫だと思いますが、すべてDPM++ 2M Karrasで調整しましたので困ったらそれで。
- Hires.fixで一部の色味が化ける場合はHires stepsを0（自動）か10以上の数値を取ってみてください。（lamettaに限ったことではないと思いますが）

- 推奨？プロンプト<br>
プロンプトは短めな方が結果が良いです。まずは短めに指定して必要なものを付け足して調整するような使い方が良いでしょう。<br>
クオリティタグは雑に出力して楽しむ分には必ずしも必須ではないように感じます。Hires.fixするならなくても良いかも？<br>
"chibi"でちびキャラが出ては来ると思いますが上手くデフォルメしきれていない気がします。<br>
LoRAはキャラものが苦手との声をお聞きしました。他のモデルと比較してかなりデフォルメの強い顔立ちですからたしかになあと思います。<br>
LoRA Block Weightを活用してIN01-02,OUT07-11をカットすると多少緩和するかも？<br>

- 推奨ネガティブプロンプト<br>
"(low quality, worst quality:1.4)"　は推奨ですがネガティブTIなどで置き換えて、もしくは重ねて使用するのも良いと思います。<br>
TIのおすすめは "verybadimagenegative_v1.3"や"bad_pictures3"とかを実際使ってみたりしていますが、世にあるものを全て網羅できていませんのでもっとオススメがあったら教えてください。<br>
アレコレ書いてますが自由に使ってみて良い結果が得られたらこっそり教えてください。<br>

- なんでこんなにいっぱいあるの？どれ使えばいいの？<br>
それぞれの違いは例えるなら飲み物のフレーバーの違いのようなものなので、新しい風味が必ずしもあなたの好みに合うとは限りません。<br>
新しいものを美味しいと感じることもあれば以前のほうがしっくり来ることもあるでしょうし、ケースバイケースで使い分けてみるのも面白いでしょう。<br>
迷ったら最新のv2012を試してみてね。<br>

- 以前アップされていたモデルは [lametta_old](https://huggingface.co/Lasorco/lametta_old)  に移してありますのでそちらからダウンロードしてください。<br>

---


# 出力例
サンプルは少々ガチャを回してだいたい作画意図になったものをあげています<br>
細部のおかしな点もこのモデルの特性ですのでそのままの掲載です<br>

![01924-1419831433.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/U7urJlgwel2kokMV0O3fe.png)
**v2012**　： v17系の改良バージョン

<details><summary><b>20xx系詳細</b></summary>

## v2012
v17系の改良を目指してマージしましたが、v17とv19を統合したモデルと言った立ち位置になりました。（v19もv17もほぼおんなじじゃん！ハイその通りかもしれません…）<br>
いつでもだいたい丸い目の出力のモデルのそれを踏まえつつ前よりも多少表情が変わるようになった感じ（を目指したんだけどそうなってるよね？）です。<br>
とはいえlamettaなのでだいたいいつも通りの雰囲気は継承していると思います。<br>
内包VAEはClearVAE Variantですがお好みのVAEを設定して使用していただいて問題有りません。<br>

マージレシピは<br>
v1745 x v1922 = A<br>
Simple ink-prt x A = B<br>
CookieCutter Flex v3.5 x A = C<br>
B x C = D<br>
A x D(tensor merge) = F<br>
A x F(cosine) = G <br>
v1930 x F = H<br>
spekulatius_v1 x v412(modified) = I<br>
H x I = J<br>
Rabbit_v6 x J = K<br>
G x K = v2012<br>
<br>
改めてマージ履歴追ってみたら随分ごちゃごちゃ混ぜてますね…<br>
lamettaの骨格にspekulatiusの細かい表現とCookieCutterのオブジェクトの多さを足してSimple ink-prtとabbit_v6でうるさくなりすぎないようにした。とは後付けな解説ですけどまあ多分そんな感じです。<br>

![01907-729192073.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/SP84uFxpwP-6eDlsY2Pa9.png)
```
1girl,loli,thick eyebrows,black short hair,v-shaped eyebrows,overall,shirt,straw hat,open mouth,waving,looking at viewer,wheat field,cowboy shot,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 729192073, Size: 512x768, Model hash: 8e5e393bdd, Model: lametta_v2012_fp16,
Denoising strength: 0.4, Clip skip: 2, Hires upscale: 2, Hires upscaler: 4x_foolhardy_Remacri, Version: v1.6.0
```
 
![01917-1329736539.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/y9_krwiOt4LhML-c2U5bf.png)
```
1girl,loli,large breasts,smile,short hair,(curly hair:1.1),blue maid costume,lace trim blue thighhighs,maid headdress,lace trim elbow gloves,looking at viewer,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1329736539, Size: 512x768, Model hash: 8e5e393bdd, Model: lametta_v2012_fp16,
Denoising strength: 0.4, Clip skip: 2, Hires upscale: 2, Hires upscaler: 4x_BooruGan_650k, Version: v1.6.0
```

![01918-4280876389.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/B6shRDoIin82_RXsMOJTv.png)
```
watercolor,pastelcolor,colorful,fairy,fairy wings,flowers,plants,mushroom,light particles,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 4280876389, Size: 768x512, Model hash: 8e5e393bdd, Model: lametta_v2012_fp16,
Denoising strength: 0.6, Clip skip: 2, Hires upscale: 2, Hires upscaler: Latent (nearest-exact), Version: v1.6.0
```
なんか今回サンプルがClipskip:2での掲載ですけど1でももちろん楽しめます。

</details>
<br>

---   

![v19xx.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/fNinpu3KP3pl5xt1wpzKx.png)
**v1921** ,v1922 ,**v1930**　： アニメ塗りっぽい出力のモデル

<details><summary><b>19xx系詳細</b></summary>

## v1930
v1921をベースにしてv1745をマージしました。v1604とボツにして表に出していないv1810も隠し味に混ぜ込んであります。<br>
内包しているVAEは昔マージして忘れ去っていたVAEです。<br>
VAE内包は生成初心者さん向けへの対応です。これが最良というわけではないのでお好みのVAEを設定して使ってください。<br>

![02116-2003955719.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/Ltbhgtcfbk7VcEVtg-Pj9.png)
```
1girl,loli,hands on own cheek,happy,open mouth,spoken heart,parfait,cafe,
Negative prompt: (worst quality, low quality:1.4),
Steps: 30, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2003955719, Size: 512x768, Model hash: 95bc5b7f2b, Model: lametta_v1930_fp16,
Denoising strength: 0.4, Hires upscale: 2, Hires upscaler: 4x_Valar_v1, Version: v1.6.0
```
 
![02107-2160317488.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/_XHrNQutnnJM0QDKLDoAZ.png)
```
1girl,huge breasts,:d,(animal kigurumi pajamas:1.2),bedroom,
Negative prompt: (worst quality,low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2160317488, Size: 512x768, Model hash: 95bc5b7f2b, Model: lametta_v1930_fp16,
Denoising strength: 0.4, Hires upscale: 2, Hires upscaler: 4x-UltraSharp, Version: v1.6.0
```

![02157-1020516930.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/n5MnxbuipMjKXdEH8cY3D.png)
```
1girl,open coat,loli,autumn maple forest,light smile,
Negative prompt: verybadimagenegative_v1.3,
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1020516930, Size: 768x512, Model hash: 95bc5b7f2b, Model: lametta_v1930_fp16,
Denoising strength: 0.7, ADetailer model: face_yolov8n.pt, ADetailer confidence: 0.3, ADetailer dilate/erode: 4, ADetailer mask blur: 4,
ADetailer denoising strength: 0.4, ADetailer inpaint only masked: True, ADetailer inpaint padding: 32, ADetailer version: 23.9.3,
Hires upscale: 2, Hires steps: 40, Hires upscaler: Latent (nearest-exact), TI hashes: "verybadimagenegative_v1.3: d70463f87042",Version: v1.6.0
```

![00003-3965509510.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/COgdgJtOMVrdevBaiqn-h.png)
sketch風に遊べるモデルという要望をもらったので対応してみたつもりですがどうなんでしょう？よくわからない<br>

---

## v1922
v1921のリミックス版です<br>
もとより再マージしようとは思っていましたがマージ履歴csvをロストしたため全階層再構築となっています。<br>
base部も配分変更されたためv1921とは出力が結構変わったと思いますがどうでしょう？<br>
いつも通り1921、1922ともに好みの方を使ってもらえたらと思います。<br> 

![00575-842203328.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/p_OVKsjoOal0I1KAvsrkq.png)
```
1girl,loli,school uniform,autumn leaves,cowboy shot,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 842203328, Size: 512x768, Model hash: 945c2bdaad,
Model: lametta_v1922_fp16, Denoising strength: 0.4, Hires upscale: 2, Hires upscaler: R-ESRGAN 4x+ Anime6B, Version: v1.6.0
```
 
![00583-4178983340.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/diw8v1eadQI05DT6V4v9I.png)
```
1girl,loli,large breasts,angel wings,angel,halo,night,city lights,flying,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 4178983340, Size: 512x768, Model hash: 945c2bdaad,
Model: lametta_v1922_fp16, Denoising strength: 0.4, Hires upscale: 2, Hires upscaler: 4x_Valar_v1, Version: v1.6.0
```

![00571-2476768054.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/so40V0L5DoHSslvNyYW8q.png)
```
2girls,looking at viewer,outdoors,forest,dappled sunlight,hug,
ADDCOMM loli,mint Fishtail braid,mint dress,puffy short sleeves,hair flower,hairband,pointy ears,smile,
ADDCOL loli,brown hair,(dark skin:1.2),open mouth,loincloth,navel,Tropical costume,
Negative prompt: verybadimagenegative_v1.3,
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2476768054, Size: 768x512, Model hash: 945c2bdaad,
Model: lametta_v1922_fp16, Denoising strength: 0.4, RP Active: True, RP Divide mode: Matrix, RP Matrix submode: Horizontal,
RP Mask submode: Mask, RP Prompt submode: Prompt, RP Calc Mode: Attention, RP Ratios: "1,1", RP Base Ratios: 0.2, RP Use Base: False,
RP Use Common: True, RP Use Ncommon: False, RP Change AND: False, RP LoRA Neg Te Ratios: 0, RP LoRA Neg U Ratios: 0, RP threshold: 0.4,
RP LoRA Stop Step: 0, RP LoRA Hires Stop Step: 0, RP Flip: False, Hires upscale: 2, Hires upscaler: 4x_foolhardy_Remacri,
TI hashes: "verybadimagenegative_v1.3: d70463f87042", Version: v1.6.0
```
※いつも出力テストに付き合ってもらっているキャラクターです

---

## v1921
以前からの何と言うか2.25次元？っぽいような塗りではなく、もうちょいアニメ塗りっぽいのがほしいなあと前々から思っていました。<br>
ある時フラットでアニメなモデルをマージされている方からご厚意でそのモデルを提供くださり（本当に感謝）、その塗りを元にしてアレコレしたのが今回です。<br>
欲張っていたら調整が難航してしまいまだ煮詰め足らずな気もしていますのでおおらかに楽しんでいただけたらと思います。（ゴメンね！）<br>
素の出力では以前と変化が乏しい感もありますのでアニメ系のアップスケーラーでHires.fixして使ってください。サンプルもHiresしてのものになります。<br>
また今回はVAE（ClearVAE Variant）を内包させてみました。もちろんお好みのVAEを設定して使用していただいて問題ありません。<br>

今回使用したモデルは

- S-flat-nullpo-testBBB4 @nullpox
- NuipeniMix ver.2 @McSionnaigh
- WateryAbyss @The_Missing_Models
- lametta_v1745,v1605,1604

S-flat-nullpo-testBBB4から塗りを中心に主にOUT層を、NuipeniMix ver.2からはTextEncoderをちょっとつまませてもらい、WateryAbyssからTextEncoderとOUT7-11付近を隠し味程度にもらってきました。<br>
特にS-flat-nullpo-testBBB4は過去のlamettaとかけ合わせたものを多重マージしてあるのでこのモデルが今回のキーになります。<br>

![02196-390773643.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/kmJgMsIH0xIYWxfc29shH.png)
```
1girl,large breasts,short hair,small breasts,sailor dress,sailor hat,happy,smile,open mouth,skin fang,dappled sunlight,
Negative prompt: verybadimagenegative_v1.3,covered navel,
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 390773643, Size: 512x768, Model hash: 20aa249203,
Model: lametta_v1921_fp16, Denoising strength: 0.4, Hires upscale: 2, Hires upscaler: 4x_foolhardy_Remacri, Version: v1.6.0
```
※後で見たらお胸の大きさLargeとSmallで2回唱えててダメだった
 
![02218-2410852180.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/oaNLvS1K3LmBtuFS7Uw98.png)
```
watercolor,pastelcolor,colorful,fairy,fairy wings,flowers,plants,mushroom,light particles,
Negative prompt: (worst quality:1.4),(low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2410852180, Size: 512x768, Model hash: 20aa249203,
Model: lametta_v1921_fp16, Denoising strength: 0.6, ADetailer model: face_yolov8n.pt, ADetailer confidence: 0.4,
ADetailer dilate/erode: 4, ADetailer mask blur: 4, ADetailer denoising strength: 0.5, ADetailer inpaint only masked: True,
ADetailer inpaint padding: 32, ADetailer use separate steps: True, ADetailer steps: 46, ADetailer model 2nd: hand_yolov8n.pt,
ADetailer confidence 2nd: 0.5, ADetailer dilate/erode 2nd: 4, ADetailer mask blur 2nd: 4, ADetailer denoising strength 2nd: 0.6,
ADetailer inpaint only masked 2nd: True, ADetailer inpaint padding 2nd: 32, ADetailer version: 23.9.1, Hires upscale: 2,
Hires upscaler: Latent (nearest-exact), Version: v1.6.0
```

![02199-2269500953.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/eF0i9x799AMqaWXEO_O0E.png)
```
1girl,loli,rabbit girl,rabbit ears,all fours,happy,open mouth,outdoors,floral background,pink flower field,looking at viewer,
Negative prompt: (verybadimagenegative_v1.3:0.8),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2269500953, Size: 768x512, Model hash: 20aa249203,
Model: lametta_v1921_fp16, Denoising strength: 0.4, Hires upscale: 2, Hires upscaler: 4x-UltraSharp,
TI hashes: "verybadimagenegative_v1.3: d70463f87042", Version: v1.6.0
```

</details>
<br>

---                                    

![v17xx.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/cpVdPSIkAzTnb0_OvesZv.png)
**v1745** ,**v1721** , v1720 ： v13、v15系列の改良型を目指したモデル

<details><summary><b>17xx系詳細</b></summary>

## v1745
変化がほしくて古いlamettaとToraFurryMix v2.0が隠し味として混ぜてあります。<br>
何が変わったの？と言われると答えに困るところではありますが、Hires.fix時の指の破綻は少なめかもしれません。<br>
モデルの調整は何かを得意にすると何かが不得手になります。新しいモデルが必ずしも良いとは限らないですのでフィーリングに合うモデルを採用してください。<br>
Hires.fix推奨です。<br>

![00546-2422261728.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/q7x8-QUOoDNYYYysNT4ok.png)
```
best quality, detailed cg ,1girl,(loli:1.2),frilled camisole,pink short hair,wavy hair,pink twintails,ahoge, (skin fang:0.9), open mouth,park bench, looking at viewer,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2422261728, Size: 512x768, Model hash: 0d13d0d3a4,
Model: lametta_v1745_fp16, Version: v1.5.1
```
 
![00547-4071717840.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/Olp6T62624UbIdoN_RU1J.png)
```
best quality, detailed cg, 1girl, large breasts, cleavage, sheep girl, sheep ears, elbow gloves, green eyes, circlet, happy, open mouth, sweat, dappled sunlight, cowboy shot,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 4071717840, Size: 512x768, Model hash: 0d13d0d3a4,
Model: lametta_v1745_fp16, Version: v1.5.1
```

![00565-967433583.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/DiDu0jqP5bfGjpZYnWHxM.png)
```
best quality,detailed cg,1girl,loli,moon,night,reading book,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 967433583, Size: 768x512, Model hash: 0d13d0d3a4,
Model: lametta_v1745_fp16, Version: v1.5.1
```

---

## v1721
v1720の更に改良版？です。<br>
全体的なマージ比率を見直ししてもう少し言うことを効きやすくしてみました。<br>
素材は一緒なのであまり変わらないとも言えるし、CLIP部分にも手を入れたので結構変わったとも。<br>
やはりHires.fixして使用する調整です<br>

![00318-3790556145.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/DF0KsweRfTEJ16eLETJa4.png)
```
best quality, detailed cg, 1girl,loli,happy, smile,open mouth,pink sundress, cowboy shot,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3790556145, Size: 512x768, Model hash: e5edfc60bb,
Model: lametta_v1721_fp16, Version: v1.5.1
```
 
![00312-2279767147.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/NY5drJoeay4KEqAif4hMc.png)
```
best quality, detailed cg, 1girl, (dark skin:1.4), large breasts, cleavage, elf, holding harp, elbow gloves, green eyes, circlet, sweat, dappled sunlight, cowboy shot,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2279767147, Size: 512x768, Model hash: e5edfc60bb,
Model: lametta_v1721_fp16, Version: v1.5.1
```

![00306-3476143409.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/bT9zvZVesO4PzCHLUZycW.png)
```
best quality, detailed cg, 1girl, loli, rabbit girl, white hair, blue moon, night sky, cowboy shot,
Negative prompt: bad anatomy, (worst quality, low quality:1.4), nsfw,
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3476143409, Size: 768x512, Model hash: e5edfc60bb,
Model: lametta_v1721_fp16, Version: v1.5.1
```

---

## v1720
v13とv15系の間を取りつつ出力の汎用性アップを目指したモデルです。lamettaの癖を少しだけ薄めて扱いやすくした感じでしょうか。<br>
v15系ではHires.fixした時にまつ毛がうるさくなりすぎるきらいがありましたがv17ではあっさりめ傾向です。<br>
目もやや小さめにバランスよく？としていますので必要に応じて"big eyes"やLoRAで補ってください。<br>
サンプルは素の出力ですが、基本的にはHires.fixして使用する調整としてあります。<br>

![00786-3781391533.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/3bmJshQJNpaqA67khHoN1.png)
```
best quality, detailed cg, 1girl, twin braid, loli, huge breasts, happy, smile, open mouth, pinafore dress, cowboy shot,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3781391533, Size: 512x768, Model hash: 34065c40e3,
Model: lametta_v1720_fp16, Version: v1.5.1
```
 
![00891-2382167223.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/B7n4oEHIDp7dP62qGpEt0.png)
```
best quality, detailed illustration, 1girl, (loli:1.2), sleeveless dress, cowboy shot, night, cityscape, from above, starry sky,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2382167223, Size: 512x768, Model hash: 34065c40e3,
Model: lametta_v1720_fp16, Version: v1.5.1
```

![00880-1722069721.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/FB_fdYwJhLDDl4ne9obUl.png)
```
best quality, detailed cg, 1girl, smile, mint hair, (parfait:1.2), mint color, blue cream, mint chocolate chip,
Negative prompt: bad anatomy, (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1722069721, Size: 768x512, Model hash: 34065c40e3,
Model: lametta_v1720_fp16, Version: v1.5.1
```
</details>
<br>

---

![16xx.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/uoI3cMves6dnnV5lPCHHR.png)
v1601 , **v1602** , **v1604** , **v1605**：デフォルメチックな絵を出力する方向性です

<details><summary><b>16xx系詳細</b></summary>

## v1605
v1574をベースにしてCookieCutter Flexをマージしました。<br>
よりanimeっぽくなりより頭身が下がったそんな感じのモデルです。<br>
個人的に "thick eyebrows, v-shaped eyebrows" がよく似合うのではないかと思います。<br>
描写が甘い点はHires.fixにて解決してみてください。<br>

![01174-2142905500.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/mHhBxLg2V4cmkxOYErPN-.png)
```
best quality, detailed cg, 1girl, (loli:1.2), thick eyebrows, black short hair, (v-shaped eyebrows:0.9), cowboy shot, happy, smile, sleeveless pink dress, outdoors, forest, from above,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2142905500, Size: 512x768, Model hash: de7db98725,
Model: lametta_v1605.fp16, Version: v1.4.1
```

![01172-581597326.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/YRGPxbytAmGCaV-mqZq4a.png)
```
best quality, detailed illustration, loli, sheep girl, grin, sheep ears, standing, wavy short hair, outdoors, farm, cowboy shot,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 581597326, Size: 512x768, Model hash: de7db98725,
Model: lametta_v1605.fp16, Version: v1.4.1
```

![01173-3145055862.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/iEkopra1472FIf6nFatQg.png)
```
best quality, detailed cg, 2girls, symmetrical, (animal kigurumi pajamas:1.2), (loli:1.2), twintail, blonde hair, cowboy shot, smile, night, bedroom,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3145055862, Size: 768x512, Model hash: de7db98725,
Model: lametta_v1605.fp16, Version: v1.4.1
```

---

## v1604
v1601のベースをv1574へ差し替えとともにマージ比率を見直したものです。<br>
v16xxというよりはアニメ塗りっぽくなったv15xxみたいな感じになりました。<br>
例によってAnythingのVAEによる出力サンプルですが、clearVAE_V1.1などのほうが好結果になると思います。<br>
あれ...結局16シリーズは拇指姑娘v2.0マージシリーズなんじゃ...<br>

![00940-1818502218.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/q9lmRFzc-MoQ0QF-oQg4Z.png)
```
best quality, detailed cg, 1girl, smile, (loli:0.8), kimono maid, holding tray,
Negative prompt: (worst quality, low quality:1.4),
Steps: 30, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1818502218, Size: 512x768, Model hash: ea9dc7d27b,
Model: lametta_v1604_fp16, Version: v1.3.2
```

![00944-468116084.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/GZOiiITwrIJAmqjPGtK6P.png)
```
best quality, detailed illustration, (loli:1.2),rabbit girl, sleeveless polka dot dress,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 468116084, Size: 512x768, Model hash: ea9dc7d27b,
Model: lametta_v1604_fp16, Version: v1.3.2
```

![00935-528650716.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/ffYOmKaXGYmLkOb3UZ1Gz.png)
```
best quality, detailed illustration,1girl,solo,alice \(alice in wonderland\), (loli:1.2),blonde hair, hair ribbon, frilled dress, frilled skirt, frilled sleeves, blue eyes, very long hair,castle background,
Negative prompt: bad anatomy,(low quality, worst quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 528650716, Size: 768x512, Model hash: ea9dc7d27b,
Model: lametta_v1604_fp16, Version: v1.3.2
```

---

## v1602
v1601のマージ比率と素材を見直して更にデフォルメ感をアップさせました<br>
なんだか以前のlamettaっぽさがなくなったような？ "detail eyes"を唱えるとlamettaの遺伝子を少し思い出すかも<br>
同じSEEDでもSampling stepsなどの出力パラメータでどんどん細部が変わります（拇指姑娘v2.0マージしたものはそうなりやすいような？）<br>
手足や背景の破綻はパラメータの見直しやHires.fixにて解決してみてください。<br>


![01250-2089126768.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/E0_8lU2zfdsoywrL5j3MU.png)
```
best quality, detailed illustration, 1girl, (loli:1.2), sleeveless dress, cowboy shot, night, starry sky, cityscape, chain-link fence, from above,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2089126768, Size: 512x768, Model hash: a355fdc3d9,
Model: lametta_v1602_fp16, Denoising strength: 0.5, Hires upscale: 1.5, Hires steps: 8, Hires upscaler: 4x_fatal_Anime_500000_G, Version: v1.4.1
```

![01254-3089771647.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/hGpe9z1OuW_kXGGf6iUT4.png)
```
best quality, detailed cg, (loli:1.2), full body, bob cut, gently smile, closed mouth, little red riding hood girl, picnic basket, over knee socks, brown lace-up boots, brown corset,looking at viewer, out door, dappled sunlight,
Negative prompt: (worst quality, low quality:1.4),
Steps: 30, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3089771647, Size: 768x512, Model hash: a355fdc3d9,
Model: lametta_v1602_fp16, Denoising strength: 0.5, Hires upscale: 1.5, Hires steps: 8, Hires upscaler: 4x_fatal_Anime_500000_G, Version: v1.4.1
```

![01257-3148478248.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/hifPWtcKFiSxXaJZbHlzx.png)
```
6+girls, (chibi:1.2), sheep girl,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3148478248, Size: 768x512, Model hash: a355fdc3d9,
Model: lametta_v1602_fp16, Denoising strength: 0.5, Hires upscale: 1.5, Hires steps: 8, Hires upscaler: 4x_fatal_Anime_500000_G, Version: v1.4.1
```

---

## v1601
v15xx系レシピを再構築したものに拇指姑娘v2.0をマージしました<br>
絵本の中のような雰囲気が出たら良いなあというアプローチです<br>
出力はClipskip2推奨です。1は大きく黄色へ転びますがこれもこれで面白いと思います<br>

![01263-3444924025.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/pql87gLhRe1KNImA2y2a6.png)
```
best quality, detailed illustration, 1girl, loli, child body, wolf girl, open mouth, skin fang, paw pose, outdoors, forest, night, full moon,
Negative prompt: (worst quality, low quality:1.4),
Steps: 30, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 3444924025, Size: 512x768, Model hash: 2f57da9663,
Model: lametta_v1601_fp16, Clip skip: 2, Version: v1.4.1
```

![01264-268483016.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/hXuHrDDl-nWrO1wj71CfS.png)
```
best quality, detailed illustration, 1girl, twin braid, blunt bangs,(loli:1.2),huge breasts, happy, smile,open mouth, pinafore dress, cowboy shot, rural, garden, dappled sunlight,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 268483016, Size: 512x768, Model hash: 2f57da9663,
Model: lametta_v1601_fp16, Clip skip: 2, Version: v1.4.1
```

![01272-4052602564.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/e2Z6TtCmw5mHdkNUA1HsR.png)
```
best quality, detailed illustration, 1girl, loli, side ponytail, blonde hair short twintails, white dress, puffy short sleeves, happy, grin, train interior, suitcase, sitting,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 4052602564, Size: 768x512, Model hash: 2f57da9663,
Model: lametta_v1601_fp16, Clip skip: 2, Version: v1.4.1
```
</details>
<br>

---

![15xx.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/KnJFAxlgZwZVZFMaOE3fv.png)
**v1504** , v1555, **v1574**：目が丸くて大きい主力モデル

<details><summary><b>15xx系詳細</b></summary>

## v1574
v1555をベースにしてCLIP周りの見直しをしたものになります<br>
横長画面での安定性などを解決しようとしましたが、眼を見張るほどの改善はなく結局は "bad anatomy" などをネガに入れて使う形と思います<br>
v1504以降は小改修的なバージョンアップばかりですのでこのシリーズはこれを以ってマージ終了かなと思っています<br>

![01276-466810223.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/pwB9-m7VEWFkORlg-j980.png)
```
best quality, detailed illustration, 1gir,loli, blonde hair short twintails, white dress, puffy short sleeves, happy, grin, see-through, peace sign, outdoors, cityscape, cowboy shot, sunset,
Negative prompt: (worst quality, low quality:1.4), covered navel,
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 466810223, Size: 512x768, Model hash: 776f5e5678,
Model: lametta_v1574_fp16, Version: v1.4.1
```

![01277-1146276385.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/FATEfMMTQ5LqWatUvNqsJ.png)
```
best quality, detailed illustration,1girl, solo, loli, bright room, pillows, seiza on bed, curtains,white short hair, purple eyes, white apron, light blue puffy short sleeves, light blue dress, hug stuffed bear,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1146276385, Size: 512x768, Model hash: 776f5e5678,
Model: lametta_v1574_fp16, Version: v1.4.1
```

![01281-2894811173.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/gCYWibdqEF10C3olUqhNI.png)
```
best quality, detailed illustration,1girl, large breasts, hair flower, hairband, pointy ears, open mouth, happy, smile, mint polka dot bikini, light blush, water field, outdoors,
Negative prompt: (worst quality, low quality:1.4), bad anatomy,
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2894811173, Size: 768x512, Model hash: 776f5e5678,
Model: lametta_v1574_fp16, Version: v1.4.1
```

---

## v1555
v15xxシリーズを抜本的な部分からfixしてみたのですが正直v1504と大差ありません<br>
特定のLoRAを組み合わせたときや特定のプロンプトの出力結果が向上していますがあくまでごく一部です<br>
副作用としてv1504より目が小さめになりました、プロンプトで "big eyes" や目が大きくなるLoRAなどで補えば以前とほぼ同じようになると思います<br>

![01285-4103269264.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/xPtkbRI9gtM6LrNysYDZc.png)
```
best quality, detailed illustration, loli, (brown rabbit girl:1.1), happy, smile, picnic basket, picnic seat,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 4103269264, Size: 512x768, Model hash: fc287aa054,
Model: lametta_v1555_fp16, Version: v1.4.1
```

![01287-1169474282.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/MDDrzY4Laukou67Yq9Teg.png)
```
best quality, detailed illustration,1girl,loli, nurse, standing, hands on hips, (hospital:1.2), White Pantyhose, cowboy shot,
Negative prompt: (worst quality, low quality:1.4),(red cross:1.2), covered navel,
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1169474282, Size: 512x768, Model hash: fc287aa054,
Model: lametta_v1555_fp16, Version: v1.4.1
```

![01289-318480518.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/ATrPqU4a5ZHSCGw1SgKx3.png)
```
best quality, detailed illustration, 1girl, loli, fairy, fairy wings, floating, (floral background:1.2), flowers, nature, lake, blue sky,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 318480518, Size: 768x512, Model hash: fc287aa054,
Model: lametta_v1555_fp16, Version: v1.4.1
```

---
 
## v1504
骨格はv13xx系をそのままに丸いタレ目な出力が特徴のモデルで、v1503（lametta_old側にあります）をfixしたものとなります<br>
切れ長な目元の女の子モデルは簡単に見つかるのに呪文指定せずともまんまるお目々の女の子を出力してくれるモデルがなかなか無いね？じゃあ作るか！がlamettaの目的の一つだったのでやっとひとつのゴールに行き着いた感があります<br>
（今は丸くてかわいいお目々のモデル結構あるよね！）<br>

![00617-2686433535.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/jrOIc2O2CiMSRhDbCbjEq.png)
```
best quality, detailed illustration,1girl, flat_chest,(loli:1.2),(child body:1.1), blond long hair, blue eyes, ( polka dot sleeveless dress:1.2), white wide brim hat, outdoor, lifted by self,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 2686433535, Size: 512x768, Model hash: 1b0a6619fa,
Model: lametta_v1504_fp16, Version: v1.4.1
```

![00616-1170522170.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/0hvt2dikrPUSQKT-iZ7UE.png)
```
best quality, detailed cg, 1girl, (loli:1.1), pajamas, yawning, one eye closed, hand on own mouth, fuzzy hair,
Negative prompt: (worst quality, low quality:1.4),
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1170522170, Size: 512x768, Model hash: 1b0a6619fa,
Model: lametta_v1504_fp16, Version: v1.4.1
```

![00615-1069866765.png](https://cdn-uploads.huggingface.co/production/uploads/64172e2f1f1f3b0fa80ce889/FgekuoqPDk1tHoKTgzxvW.png)
```
best quality, detailed illustration,1girl,(loli:1.2), pink twintails, pointy ears, ahoge, grin, black dress, on stomach, on bed,
Negative prompt: (worst quality, low quality:1.4), bad anatomy,
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1069866765, Size: 768x512, Model hash: 1b0a6619fa,
Model: lametta_v1504_fp16, Version: v1.4.1
```

</details>
<br><br>

---

**lametta Merge Model**　： lamettaをマージしたモデルのご紹介

こちらで把握できたものだけ、どれもまた一味違うのでより好みが見つかるかも

## nadenade氏
- [nadenadesitai](https://civitai.com/models/79846/) lamettaの姉妹モデル
- [surisurisitai](https://civitai.com/models/82885/) nadenadeがジト目になってやってきた
- [funifunisitai](https://civitai.com/models/113985/) surisuriがデフォルメされてより可愛くなった！

## Yntec氏
- [lamettaRemix](https://huggingface.co/Yntec/lamettaRemix)  v1745とv1602のマージモデル
- [LAMEanime & lamettaSEXTILION](https://huggingface.co/Yntec/LAMEanime) lamettaRemixとanimeSEXTILLIONのマージモデル

素材としても使ってもらえるのは本当に嬉しいです。
<br>




---
# クレジット
マージに使用させていただいたモデル（敬称略）

- ACertainty　@JosephusCheung (LoRA)
- Counterfeit-V2.2　@gsdf (v1,v2,v3)
- SSSSLLDDLL v1　@kgmkm (v9)
- CoffeeNSFW v1.0　@CoffeeCoffee (v2)
- Anime Chibi Model　@AiRetard (v412,v413)
- DDosMix_v2　@DiaryOfSta (v5,v9,v13)
- AniDosMix_A　@DiaryOfSta (v9,v13)
- QteaMix　@chenxluo (v13系)
- NeatNess Fluffy Fur Mix v1.0,v2.0,v3.0,Unicorn edition,Infinity,　@NeatNess (v9,v13)
- mix-proV3,V3.5,V4,V4.5+ColorBox,　@P317cm (v13,v1503,v1504)
- CuteYukiMix v1.0,v3.0　@newlifezfztty761 (v1503,v1504)
- Ares Mix v0.1　@rocp (v1503,v1504)
- Doll Like Anime　@PromptSharingSamaritan (v1523)
- Grilled_Lamprey v2627　@Liquidn2 (v1523)
- Yuzu v1.0　@Ikena (v1523)
- Defacta3th v1.0　@Aihub_tokyo (v1555)
- Coconut furry mix　@YukiLaneige (FU)
- Sweet Factory　@RIXYN (v1555)
- AkkaiMix　@Akkairosu (v1574)
- 拇指姑娘（Thumbelina）v2.0　@Cinsdia (v1601,v1602,v1604)
- CookieCutter Flex v1.01,Flex v3.5　@Kybalico (v1605@1.01,v2012@v3.5)
- SweetParfait　@sleepotimer (v1720)
- ToraFurryMix v2.0　@tlano (v1745)
- S-flat-nullpo-testBBB4 @nullpox (v1921,v1922)
- NuipeniMix ver.2 @McSionnaigh (v1921,v1922)
- WateryAbyss @The_Missing_Models (v1921,v1922)
- Simple ink-prt @Yuno779　(v2012)
- Rabbit v6 @Rabbit_YourMajesty (v2012)
- ClearVAE v1.1(Variant) @RedRayz (v19,v20)
- flat1,flat2,boldline,bigeye,hanme @2vXpSwA7 (V13,FD)

全モデルにこれらすべてがマージされているわけではありませんが一括してクレジット記載させていただきます。<br>
記憶とマージ履歴から追えるものは括弧書きに入れてみましたが古いモデルはあまり正確ではないかも。<br>
v2から旧バージョンを秘伝のタレみたいに継ぎ足し使いv9までで一旦区切り、v13から新規で秘伝のタレを作り継ぎ足すようなレシピになっています。<br>


<br><br>
# 利用に際して（ライセンスなど）
アップロードされているモデル全てにおいて[creativeml-openrail-m](https://huggingface.co/spaces/CompVis/stable-diffusion-license)に準じます。
詳しくは「creativeml-openrail-m」で検索してもらえれば翻訳された解説などが確認できると思います。<br>
Attachment Aの補足として、特定の作品や作風などを模倣してその権利者等に迷惑となるような使用は禁止とさせていただきます。<br>

<br>
civitai風な表記ですと以下の通り<br>

<span class="text-green-500">OK</span>　クレジットを入れずにモデルを使用する<br>（Use the model without crediting the creator）<br>
生成画像にクレジットの有無は問いません、マージ素材としても有無は問いませんがあると喜びます

<span class="text-green-500">OK</span>　生成した画像を販売する<br>（Sell images they generate）<br>
生成した画像はあなたの作画意図が込められていますからあなたのものです

<span class="text-green-500">OK</span>　有償の画像を生成するサービスを運営する<br>（Run on services that generate images for money）<br>
モデル名の表記をしていただければ問題ありません、末尾の "_fp16" は省略して構いません

<span class="text-green-500">OK</span>　このモデルを使ったマージモデルを共有する<br>（Share merges using this model）<br>
自由に行っていただいて問題ありません、上記の通りクレジットの有無は問いませんがしていただけると喜びます

<span class="text-red-500">NG</span>　このモデルまたはこのモデルを使ったマージモデルを販売する<br>（Sell this model or merges using this model）<br>
このモデルは当方に無断で販売は出来ません、このモデルを素材としたマージモデルについては手を加えた方の責任としてこちらは一切関与いたしません

<span class="text-green-500">OK</span>　マージモデルを共有する際に異なる権限を持たせる<br>（Have different permissions when sharing merges）<br>
問題ありませんが上記の通り手を加えた方の責任として有利不利に関わらずこちらは一切の関与をいたしません
<br><br>
以上

