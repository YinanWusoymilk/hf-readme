---
license: creativeml-openrail-m
language:
- en
library_name: diffusers
pipeline_tag: text-to-video
tags:
- AIGC
- text2video
- image2video
- infinite-length
- human
---


<font size=5>**MuseV: Infinite-length and High Fidelity Virtual Human Video Generation with Visual Conditioned Parallel Denoising**</font>
</br>
Zhiqiang Xia <sup>\*</sup>,
Zhaokang Chen<sup>\*</sup>,
Bin Wu<sup>†</sup>,
Chao Li,
Kwok-Wai Hung,
Chao Zhan,
Yingjie He,
Wenjiang Zhou
(<sup>*</sup>Equal Contribution,  <sup>†</sup>Corresponding Author, benbinwu@tencent.com)
</br>
Lyra Lab, Tencent Music Entertainment

**[github](https://github.com/TMElyralab/MuseV)**    **[huggingface](https://huggingface.co/TMElyralab/MuseV)**  **[HuggingfaceSpace](https://huggingface.co/spaces/AnchorFake/MuseVDemo)**   **[project](comming soon)**    **Technical report (comming soon)**


We have setup **the world simulator vision since March 2023, believing diffusion models can simulate the world**. `MuseV` was a milestone achieved around **July 2023**. Amazed by the progress of Sora, we decided to opensource `MuseV`, hopefully it will benefit the community. Next we will move on to the promising diffusion+transformer scheme.

We will soon release `MuseTalk`, a real-time high quality lip sync model, which can be applied with MuseV as a complete virtual human generation solution. Please stay tuned! 

# Overview
`MuseV` is a diffusion-based virtual human video generation framework, which 
1. supports **infinite length** generation using a novel **Visual Conditioned Parallel Denoising scheme**.
2. checkpoint available for virtual human video generation trained on human dataset.
3. supports Image2Video, Text2Image2Video, Video2Video.
4. compatible with the **Stable Diffusion ecosystem**, including `base_model`, `lora`, `controlnet`, etc. 
5. supports multi reference image technology, including `IPAdapter`, `ReferenceOnly`, `ReferenceNet`, `IPAdapterFaceID`.
6. training codes (comming very soon).


# News
- [03/27/2024] release `MuseV` project and trained model `musev`, `muse_referencenet`, `muse_referencenet_pose`.


## Model
### overview of model structure
![model_structure](data/models/musev_structure.png)
### parallel denoising
![parallel_denoise](data/models/parallel_denoise.png)

## Cases
All frames are generated from text2video model, without any post process.

Bellow Case could be found in `configs/tasks/example.yaml`
### Text/Image2Video

#### Human
 <!-- 2 columns, one image, one video -->

<table class="center">
  <tr style="font-weight: bolder;text-align:center;">
        <td>image</td>
        <td>video </td>
        <td>prompt</td>
  </tr>

  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/cTQX49v7GT7GA-NEHj5vK.jpeg width="200">
    </td>
    <td >
     <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/U4sHVv_fYVbFHveS7Sw7h.mp4"></video>
    </td>
    <td>(masterpiece, best quality, highres:1),(1girl, solo:1),(beautiful face,
    soft skin, costume:1),(eye blinks:{eye_blinks_factor}),(head wave:1.3)
    </td>
  </tr>

  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/SPSgJpptVM4Qm11nqD07C.jpeg width="200">
    </td>
    <td>
    <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/XMya1FCmRs6USzKp9qrAy.mp4"></video>
    </td>
    <td>
    (masterpiece, best quality, highres:1),(1girl, solo:1),(beautiful face,
    soft skin, costume:1),(eye blinks:{eye_blinks_factor}),(head wave:1.3)
    </td>
  </tr>
  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/l6chBPhUKeOLbnXnX-ewG.jpeg width="200">
    </td>
    <td>
      <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/pPnU6QXgWuWxw5SWZdl8N.mp4"></video>
    </td>   
    <td>
    (masterpiece, best quality, highres:1), peaceful beautiful sea scene
    </td>
  </tr>

  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/VQMEeGc1wTuiATtQLJjer.jpeg width="200">
    </td>
    <td>
      <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/_9ZQEebUlmSNtXMJKiGPu.mp4"></video>
    </td>
    <td>
      (masterpiece, best quality, highres:1), peaceful beautiful sea scene
    </td>
  </tr>
  <!-- guitar  -->
  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/Fk_eec7vqq4NfAYVPNLI-.jpeg width="200">
    </td>
    <td>
      <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/p0gWRwZTDOrbPf8mZOphG.mp4"></video>
    </td>
    <td>
       (masterpiece, best quality, highres:1), playing guitar
    </td>
  </tr>
  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/Zcc5xj1-lA_EPS7gvJu99.jpeg width="200">
    </td>
    <td>
      <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/4mT4KL3q4FzyQQKJfgXVG.mp4"></video>
    </td>
    <td>
      (masterpiece, best quality, highres:1), playing guitar
    </td>
  </tr>
  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/iT5OsCpRNnntuS0TH1cG5.jpeg width="200">
    </td>
    <td>
      <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/6RWBw73-oE4rJH808FzIK.mp4">
    </td>
    <td>
      (masterpiece, best quality, highres:1), playing guitar
    </td>
  </tr>
  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/Ym582ZF-MbYkRW1sAE5r3.jpeg width="200">
    </td>
    <td>
      <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/lYqpeRcIiK7WEqRe4d8dZ.mp4"></video>
    </td>
    <td>
    (masterpiece, best quality, highres:1), playing guitar
    </td>
  </tr>
  <!-- famous people -->
  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/JsAjbl4AeYz089kWHjjUJ.jpeg width="200">
    </td>
    <td>
      <video width="400"  controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/KCjF9HutBo7el15gm3YV3.mp4"></video>
    </td>
    <td>
    (masterpiece, best quality, highres:1),(1man, solo:1),(beautiful face,
    soft skin, costume:1),(eye blinks:{eye_blinks_factor}),(head wave:1.3)
    </td>
  </tr>

  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/v-X3Wrkm14YwLGGloNlMK.jpeg width="200">
    </td>
    <td>
      <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/P_Y5jUO1EJ6n3Z4qd1xh1.mp4"></video>
    </td>   
    <td>
    (masterpiece, best quality, highres:1),(1girl, solo:1),(beautiful face,
    soft skin, costume:1),(eye blinks:{eye_blinks_factor}),(head wave:1.3)
    </td>
  </tr>
  <tr>
    <td>
        <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/cNe41NV1OfLF5AmMKD6mi.jpeg width="200">
    </td>
    <td>
      <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/L6mA8uuckRJhzhAJHayJT.mp4"></video>      
    </td>
    <td>
  (masterpiece, best quality, highres:1),(1man, solo:1),(beautiful face,
    soft skin, costume:1),(eye blinks:{eye_blinks_factor}),(head wave:1.3)
    </td>
  </tr>
  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/6iHIaa15eBgop7BsE0Nps.jpeg width="200">
    </td>
    <td>
      <video width="400"  controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/foPX3iRk2TzjRl_V52T21.mp4"></video>
    </td>
    <td>
  (masterpiece, best quality, highres:1),(1girl, solo:1),(beautiful face,
    soft skin, costume:1),(eye blinks:{eye_blinks_factor}),(head wave:1.3)
    </td>
  </tr>
  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/R7rp7t4DPkws0dXRxi0bf.jpeg width="200">
    </td>
    <td>
      <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/tGTSNe9i08pvTMNe6SOBg.mp4"></video>
    </td>
    <td>
      (masterpiece, best quality, highres:1),(1girl, solo:1),(beautiful face,
    soft skin, costume:1),(eye blinks:{eye_blinks_factor}),(head wave:1.3)
    </td>
  </tr>
</table >

#### scene

<table class="center">
    <tr style="font-weight: bolder;text-align:center;">
        <td>image</td>
        <td>video</td>
        <td>prompt</td>
    </tr>

  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/EIembLBwySZTBjFZStFr_.jpeg width="200">
    </td>
    <td>
        <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/jfHV6a186BzAu-Tz0ET1o.mp4"></video>
    </td>
    <td>
      (masterpiece, best quality, highres:1), peaceful beautiful waterfall, an
    endless waterfall
    </td>
  </tr>

  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/u2_mzl5m-Z0nwSYFcTLxs.jpeg width="200">
    </td>
    <td>
        <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/eXrRVejCZs3QaA4-JK6Le.mp4"></video>
    </td>
    <td>(masterpiece, best quality, highres:1), peaceful beautiful river
    </td>
  </tr>

  <tr>
    <td>
      <img src=https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/NIHfIi7onyJ5ELetE2f_Z.jpeg width="200">
    </td>
    <td>
      <video width="400" controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/eaZyhukcfaoY7dIGp2cs6.mp4"></video>
    </td>
    <td>(masterpiece, best quality, highres:1), peaceful beautiful sea scene
    </td>
  </tr>
</table >

### VideoMiddle2Video
**pose2video**

In duffy case, pose of the vision condition frame is not aligned with of the first frame of control video. `posealign` module can solve it.

<table class="center">
    <tr style="font-weight: bolder;text-align:center;">
        <td>image</td>
        <td>video</td>
        <td>prompt</td>
    </tr>
  
  <tr>
    <td>
      <img src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/fX1ND0YqDp1LV0LEh2eFN.png" width="200">
      <img src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/pe2aQt5FU66tplNZCOZaB.png" width="200">
    </td>
    <td>
      <video width="900" src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/IMPIDjR7-w5A_xc6ZHIzT.mp4" controls preload></video>
    </td>
    <td>
      (masterpiece, best quality, highres:1)
    </td>
  </tr>

  <tr>
    <td>
      <img src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/FlLWP8IqM_X2K4hXAOPHO.png" width="200">
    </td>
    <td>
      <video width="900" src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/OT22TR7e7Lcoxci9aoDBA.mp4" controls preload></video>
    </td>
    <td>
      (masterpiece, best quality, highres:1)
    </td>
  </tr>
</table >

### MuseTalk

<table class="center">
    <tr style="font-weight: bolder;">
        <td>name</td>
        <td>video</td>
    </tr>
  <tr>
    <td>
       talk
    </td>
    <td>
      <video width="350" src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/wUhNS7j5UQ28eXu4JVQfF.mp4" controls preload></video>
    </td>
  </tr>
  
  <tr>
    <td>
       talk
    </td>
    <td>
      <video width="350" src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/bH-j15douHJcZXIEvMIDa.mp4" controls preload></video>
    </td>
  </tr>

  <tr>
    <td>
       sing
    </td>
    <td>
      <video width="350" src="https://cdn-uploads.huggingface.co/production/uploads/65f9352ed760cfdf5eb80e16/l5ZTbUQ11gK6FUtoaRz4S.mp4" controls preload></video>
    </td>
  </tr>
</table >



# Quickstart
please refer to [MuseV](https://github.com/TMElyralab/MuseV)


# Acknowledgements

1. MuseV has referred much to [TuneAVideo](https://github.com/showlab/Tune-A-Video), [diffusers](https://github.com/huggingface/diffusers), [Moore-AnimateAnyone](https://github.com/MooreThreads/Moore-AnimateAnyone/tree/master/src/pipelines), [animatediff](https://github.com/guoyww/AnimateDiff), [IP-Adapter](https://github.com/tencent-ailab/IP-Adapter), [AnimateAnyone](https://arxiv.org/abs/2311.17117), [VideoFusion](https://arxiv.org/abs/2303.08320), [insightface](https://github.com/deepinsight/insightface). 
2. MuseV has been built on `ucf101` and `webvid` datasets.

Thanks for open-sourcing!


# Limitation
There are still many limitations, including

1. Lack of generalization ability. Some visual condition image perform well, some perform bad. Some t2i pretraied model perform well, some perform bad.
1. Limited types of video generation and limited motion range, partly because of limited types of training data. The released `MuseV` has been trained on approximately 60K human text-video pairs with resolution `512*320`. `MuseV` has greater motion range while lower video quality at lower resolution. `MuseV` tends to generate less motion range with high video quality. Trained on larger, higher resolution, higher quality text-video dataset may make `MuseV` better.
1. Watermarks may appear because of `webvid`. A cleaner dataset withour watermarks may solve this issue.
1. Limited types of long video generation. Visual Conditioned Parallel Denoise can solve accumulated error of video generation, but the current method is only suitable for relatively fixed camera scenes.
1. Undertrained referencenet and IP-Adapter, beacause of limited time and limited resources.
1. Understructured code. `MuseV`  supports rich and dynamic features, but with complex and unrefacted codes. It takes time to familiarize.

<!-- # Contribution 暂时不需要组织开源共建 -->

# Citation
```bib
@article{musev,
  title={MuseV: Infinite-length and High Fidelity Virtual Human Video Generation with Visual Conditioned Parallel Denoising},
  author={Xia, Zhiqiang and Chen, Zhaokang and Wu, Bin and Li, Chao and Hung, Kwok-Wai and Zhan, Chao and He, Yingjie and Zhou, Wenjiang},
  journal={arxiv},
  year={2024}
}
```
# Disclaimer/License
1. `code`: The code of MuseV is released under the MIT License. There is no limitation for both academic and commercial usage.
1. `model`: The trained model are available for non-commercial research purposes only.
1. `other opensource model`: Other open-source models used must comply with their license, such as `insightface`, `IP-Adapter`, `ft-mse-vae`, etc.
1. The testdata are collected from internet, which are available for non-commercial research purposes only.
1. `AIGC`: This project strives to impact the domain of AI-driven video generation positively. Users are granted the freedom to create videos using this tool, but they are expected to comply with local laws and utilize it responsibly. The developers do not assume any responsibility for potential misuse by users.