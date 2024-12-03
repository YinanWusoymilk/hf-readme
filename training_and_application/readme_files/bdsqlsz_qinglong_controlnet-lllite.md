---
license: cc-by-nc-sa-4.0
library_name: diffusers
---

Thank you for support my work.

<a href="https://www.buymeacoffee.com/bdsqlsz"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a new graphics card&emoji=😋&slug=bdsqlsz&button_colour=40DCA5&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00" /></a>

https://www.buymeacoffee.com/bdsqlsz

Support list will show in main page.

# Support List

```
DiamondShark
Yashamon
t4ggno
Someone
kgmkm_mkgm
yacong
```

Pre-trained models and output samples of ControlNet-LLLite form bdsqlsz

# Inference with ComfyUI: https://github.com/kohya-ss/ControlNet-LLLite-ComfyUI Not Controlnet Nodes!

For 1111's Web UI, [sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet) extension supports ControlNet-LLLite.

Training: https://github.com/kohya-ss/sd-scripts/blob/sdxl/docs/train_lllite_README.md

The recommended preprocessing for the animeface model is [Anime-Face-Segmentation](https://github.com/siyeong0/Anime-Face-Segmentation)

# Models

## Trained on anime model

AnimeFaceSegment、Normal、T2i-Color/Shuffle、lineart_anime_denoise、recolor_luminance

Base Model use[Kohaku-XL](https://civitai.com/models/136389?modelVersionId=150441)

MLSD 

Base Model use[ProtoVision XL - High Fidelity 3D](https://civitai.com/models/125703?modelVersionId=144229)

# Japanese Introduction

https://note.com/kagami_kami/n/nf71099b6abe3

Thank kgmkm_mkgm for introducing these controlllite models and testing.

# Samples

## AnimeFaceSegmentV2

![source 1](./sample/00015-882327104.png)

![sample 1](./sample/grid-0000-656896882.png)

![source 2](./sample/00081-882327170.png)

![sample 2](./sample/grid-0000-2857388239.png)

## DepthV2_(Marigold)

![source](./sample/00011-2938929216.png)

![preprocess 1](./sample/下载.png)

![sample 1](./sample/xyz_grid-0011-2712986504.jpg)

![sample 2](./sample/xyz_grid-0021-1285985674.jpg)

## MLSDV2

![source 1](./sample/0-73.png)

![preprocess 1](./sample/mlsd-0000.png)

![sample 1](./sample/grid-0001-496872924.png)

![source 2](./sample/0-151.png)

![preprocess 2](./sample/mlsd-0001.png)

![sample 2](./sample/grid-0002-906633402.png)

## Normal_Dsine

![source](./sample/f49e5ae5b9c86ffab78f48e71d72f2f151248e33f10c54c498c7ca4be0dc5025.jpg)

![preprocess 1](./sample/normal_dsine-0022.png)

![sample 1](./sample/grid-0018-3079334279.png)

![sample 2](./sample/grid-0002-1006844163.png)

## T2i-Color/Shuffle

![source 1](./sample/sample_0_525_c9a3a20fa609fe4bbf04.png)

![preprocess 1](./sample/color-0008.png)

![sample 1](./sample/grid-0017-751452001.jpg)

![source 2](./sample/F8LQ75WXoAETQg3.jpg)

![preprocess 2](./sample/color-0009.png)

![sample 2](./sample/grid-0018-2976518185.jpg)

## Lineart_Anime_Denoise

![source 1](./sample/20230826131545.png)

![preprocess 1](./sample/lineart_anime_denoise-1308.png)

![sample 1](./sample/grid-0028-1461058306.png)

![source 2](./sample/Snipaste_2023-08-10_23-33-53.png)

![preprocess 2](./sample/lineart_anime_denoise-1309.png)

![sample 2](./sample/grid-0030-1612754720.png)

## Recolor_Luminance

![source 1](./sample/F8LQ75WXoAETQg3.jpg)

![preprocess 1](./sample/recolor_luminance-0014.png)

![sample 1](./sample/grid-0060-2359545755.png)

![source 2](./sample/Snipaste_2023-08-15_02-38-05.png)

![preprocess 2](./sample/recolor_luminance-0016.png)

![sample 2](./sample/grid-0061-448628292.png)

## Canny

![source 1](./sample/Snipaste_2023-08-10_23-33-53.png)

![preprocess 1](./sample/canny-0034.png)

![sample 1](./sample/grid-0100-2599077425.png)

![source 2](./sample/00021-210474367.jpeg)

![preprocess 2](./sample/canny-0021.png)

![sample 2](./sample/grid-0084-938772089.png)

## DW_OpenPose

![preprocess 1](./sample/dw_openpose_full-0015.png)

![sample 1](./sample/grid-0015-4163265662.png)

![preprocess 2](./sample/dw_openpose_full-0030.png)

![sample 2](./sample/grid-0030-2839828192.png)

## Tile_Anime

![source 1](./sample/03476-424776255.png)

![sample 1](./sample/grid-0008-3461355229.png)

![sample 2](./sample/grid-0016-1162724588.png)

![sample 3](./sample/00094-188618111.png)

和其他模型不同，我需要简单解释一下tile模型的用法。
总的来说，tile模型有三个用法， 
1、不输入任何提示词，它可以直接还原参考图的大致效果，然后略微重新修改局部细节，可以用于V2V。(图2)
2、权重设定为0.55~0.75,它可以保持原本构图和姿势的基础上，接受提示词和LoRA的修改。(图3)
3、使用配合放大效果，对每个tiling进行细节增加的同时保持一致性。(图4)

因为训练时使用的数据集为动漫2D/2.5D模型，所以目前对真实摄影风格的重绘效果并不好，需要等待完成最终版本。

Unlike other models, I need to briefly explain the usage of the tile model.
In general, there are three uses for the tile model,
1. Without entering any prompt words, it can directly restore the approximate effect of the reference image and then slightly modify local details. It can be used for V2V (Figure 2).
2. With a weight setting of 0.55~0.75, it can maintain the original composition and pose while accepting modifications from prompt words and LoRA (Figure 3).
3. Use in conjunction with magnification effects to increase detail for each tiling while maintaining consistency (Figure 4).

Since the dataset used during training is an anime 2D/2.5D model, currently, its repainting effect on real photography styles is not good; we will have to wait until completing its final version.

![xyz](./sample/xyz_grid-0001-3957894094.png)

目前释放出了α和β两个版本，分别对应1、2以及1、3的用法。
其中α用于姿势、构图迁移，它的泛化性很强，可以和其他LoRA结合使用。
而β用于保持一致性和高清放大，它对条件图片更敏感。
好吧，α是prompt更重要的版本，而β是controlnet更重要的版本。

Currently, two versions, α and β, have been released, corresponding to the usage of 1、2 and 1、3 respectively. 

The α version is used for pose and composition transfer, with strong generalization capabilities that can be combined with other LoRA systems. 

On the other hand, the β version is used for maintaining consistency and high-definition magnification; it is more sensitive to conditional images. 

In summary, α is a more important version for prompts while β is a more important version for controlnet.

## Tile_Realistic

Thank for all my supporter.

```
DiamondShark
Yashamon
t4ggno
Someone
kgmkm_mkgm
```

Even though I broke my foot last week, I still insisted on training the realistic version out.

![source 1](./sample/OIP.jpg)

![sample 1](./sample/grid-0000.png)

You can compared with SD1.5 tile below here↓

![sample 2](./sample/grid-0002.png)

For base model using juggernautXL series，so i recommend use their model or merge with it.

Here is comparing with other SDXL model.

![sample 2](./sample/xyz_grid-0000-948596933.png)