---
license: creativeml-openrail-m
language:
- en
pretty_name: Hololive vtuber LoRAs and TIs
task_categories:
- question-answering
tags:
- stable-diffusion
- vtuber
- hololive
- stable diffusion 1.5
- textual-inversion
- lora
- character
- text-to-image
pipeline_tag: text-to-image
metrics:
- character
---

<img src="https://huggingface.co/hollowstrawberry/holotard/resolve/main/out.jpg" width="800"/>

# Preamble

These resources are intended to be used with [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui/). If you don't know what it is or how to use it effectively, [here's an extensive guide about it](https://huggingface.co/hollowstrawberry/stable-diffusion-guide/blob/main/README.md#index).

Recommended additional resources:

* [blessed2.vae.pt](https://huggingface.co/NoCrypt/blessed_vae/blob/main/blessed2.vae.pt) - without a VAE selected in the settings your colors will look faded.
* [TagComplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete) to view all available anime tags as you write your prompt.
* [Image Browser (updated fork)](https://github.com/AlUlkesh/stable-diffusion-webui-images-browser) to view your past images and their prompt metadata.
* [Lycoris extension](https://github.com/KohakuBlueleaf/a1111-sd-webui-locon) to be able to use locons and lohas, which are new types of lora.
* [EasyNegative](https://huggingface.co/datasets/gsdf/EasyNegative/blob/main/EasyNegative.safetensors) - put it in your `stable-diffusion-webui/embeddings` folder and write `EasyNegative` in your **negative** prompt to drastically improve your images.

I make Loras of my own, particularly multi-outfit or multi-character Loras. Many of the Loras found in this repo are made by me or my peers. [Here are some other Loras I made](https://huggingface.co/hollowstrawberry/multicharloras).

&nbsp;

# Models

I merged these with hll4-p3-ep8, which is the newest vtuber-finetuned model. They have blessed2 VAE baked in. Many more mixes can be found [here](https://huggingface.co/grugger/chubas).

* [HeavenOrangeVtubers_hll4_final](https://huggingface.co/hollowstrawberry/holotard/blob/main/models/HeavenOrangeVtubers_hll4_final.safetensors)
* [AOM3_hll4_final](https://huggingface.co/hollowstrawberry/holotard/blob/main/models/AOM3_hll4_final.safetensors)
* [AOM2hard_hll4_final](https://huggingface.co/hollowstrawberry/holotard/blob/main/models/AOM2hard_hll4_final.safetensors)
* [Grapefruit4.1_hll4_final](https://huggingface.co/hollowstrawberry/holotard/blob/main/models/Grapefruit4.1_hll4_final.safetensors)

<details>
<summary>Click here for a comparison</summary>

![A comparison of different vtuber checkpoints](comparison3.png)
</details>

&nbsp;

# Loras

Most useful holo Loras will be linked to and backed up here. Put them in your `stable-diffusion-webui/models/Lora` folder. Use them in your prompt like this: `<lora:filename:1>`  
Most Loras work well with a weight of `1.0`, but some older ones work best at `0.7`.

Learn to make your own Loras [with my guide](https://civitai.com/models/22530).

&nbsp;

## Multi Outfit Loras

These are the most modern and have several outfits of each talent in a single Lora, or the main outfit if no other options are available. Check the model page / text files for examples.

### HoloEN

* [Mori Calliope ×9](https://civitai.com/models/173344)
* [Takanashi Kiara ×3](https://civitai.com/models/48195)
* [Ninomae Ina'nis ×5](https://civitai.com/models/17922)
* [Gawr Gura ×6](https://civitai.com/models/20447)
* [Amelia Watson ×4](https://civitai.com/models/27398)
* [Irys x4](https://civitai.com/models/111029)
* [Ceres Fauna ×3](https://civitai.com/models/97377)
* [Ouro Kronii ×3](https://civitai.com/models/124507)
* [Nanashi Mumei ×4](https://civitai.com/models/124549)
* [Hakos Baelz ×5](https://civitai.com/models/6080)
* [Tsukumo Sana ×1](https://civitai.com/models/20175)
* [Shiori Novella x1](https://civitai.com/models/116558)
* [Koseki Bijou x1](https://civitai.com/models/129972)
* [Nerissa Ravencroft x1](https://civitai.com/models/141707)
* [Fuwawa Abyssgard x1](https://civitai.com/models/132928)
* [Mococo Abyssgard x1](https://civitai.com/models/132419)

### HoloID

* [Ayunda Risu ×2](https://civitai.com/models/21209)
* [Moona Hoshinova ×1](https://civitai.com/models/124535)
* [Airani Iofifteen ×1](https://civitai.com/models/27558)
* [Kureiji Ollie ×4](https://civitai.com/models/28686)
* [Anya Melfissa ×3](https://civitai.com/models/27935)
* [Pavolia Reine ×3](https://civitai.com/models/15981)
* [Vestia Zeta ×3](https://civitai.com/models/52609)
* [Kaela Kovalskia ×1](https://civitai.com/models/28355)
* [Kobo Kanaeru ×3](https://civitai.com/models/145897)

### HoloJP

* [Tokino Sora ×3](https://civitai.com/models/19432)
* [Roboco-san ×4](https://civitai.com/models/154115)
* [Sakura Miko ×4](https://civitai.com/models/33471)
* [Hoshimachi Suisei ×8](https://civitai.com/models/11765)
* [Azki ×2](https://civitai.com/models/26419)
* [Yozora Mel ×3](https://civitai.com/models/21431)
* [Shirakami Fubuki ×9](https://civitai.com/models/156406)
* [Natsuiro Matsuri ×5](https://civitai.com/models/23883?modelVersionId=28543)
* [Akai Haato ×5](https://civitai.com/models/6489)
* [Aki Rosenthal ×2](https://civitai.com/models/124521)
* [Minato Aqua ×11](https://civitai.com/models/17816)
* [Murasaki Shion ×4](https://civitai.com/models/105212)
* [Nakiri Ayame ×6](https://civitai.com/models/12658)
* [Yuzuki Choco ×1](https://civitai.com/models/20305)
* [Oozora Subaru ×8](https://civitai.com/models/22332) 
* [Ookami Mio ×6](https://civitai.com/models/156824)
* [Nekomata Okayu ×6](https://civitai.com/models/23962)
* [Inugami Korone ×7](https://civitai.com/models/153356)
* [Usada Pekora ×9](https://civitai.com/models/27247)
* [Shiranui Flare ×2](https://civitai.com/models/20509)
* [Shirogane Noel ×6](https://civitai.com/models/114191)
* [Houshou Marine ×8](https://civitai.com/models/47510)
* [Uruha Rushia ×9](https://civitai.com/models/36097)
* [Amane Kanata ×7](https://civitai.com/models/124532)
* [Tsunomaki Watame ×5](https://civitai.com/models/9430)
* [Tokoyami Towa ×6](https://civitai.com/models/156139)
* [Himemori Luna ×2](https://civitai.com/models/124564)
* [Kiryu Coco ×5](https://civitai.com/models/97114)
* [Yukihana Lamy ×4](https://civitai.com/models/16876)
* [Momosuzu Nene ×4](https://civitai.com/models/40437)
* [Shishiro Botan ×4](https://civitai.com/models/10390)  
* [Omaru Polka ×3](https://civitai.com/models/124570)
* [La+ Darknesss ×1](https://civitai.com/models/14019)
* [Takane Lui ×1](https://civitai.com/models/17673)
* [Hakui Koyori ×3](https://civitai.com/models/21233)
* [Sakamata Chloe ×4](https://civitai.com/models/124502)
* [Kazama Iroha ×3](https://civitai.com/models/149755)

### Others

* [A-chan](https://civitai.com/models/27927)
* [Harusaki Nodoka](https://civitai.com/models/33130)
* [Mano Aloe](https://civitai.com/models/35099)

&nbsp;

## Small Loras

Some older Loras were manually scaled down from 144 MB to 18 MB or 36 MB and perform almost the same. They need a higher weight than the original to preserve detail.

This works because dim 128 used to be the default setting for making Loras but that was completely overkill and dim 8/16/32 work just as well.
