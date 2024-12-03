---
license: apache-2.0
---
<h1 align='center'>EchoMimic: Lifelike Audio-Driven Portrait Animations through Editable Landmark Conditioning</h1>

<div align='center'>
    <a href='https://github.com/yuange250' target='_blank'>Zhiyuan Chen</a><sup>*</sup>&emsp;
    <a href='https://github.com/JoeFannie' target='_blank'>Jiajiong Cao</a><sup>*</sup>&emsp;
    <a href='https://github.com/octavianChen' target='_blank'>Zhiquan Chen</a><sup></sup>&emsp;
    <a href='https://github.com/lymhust' target='_blank'>Yuming Li</a><sup></sup>&emsp;
    <a href='https://github.com/' target='_blank'>Chenguang Ma</a><sup></sup>
</div>
<div align='center'>
    *Equal Contribution.
</div>

<div align='center'>
Terminal Technology Department, Alipay, Ant Group.
</div>

<div align='center'>
    <a href='https://badtobest.github.io/echomimic.html'><img src='https://img.shields.io/badge/Project-Page-blue'></a>
    <a href='https://github.com/BadToBest/EchoMimic'><img src='https://img.shields.io/github/stars/BadToBest/EchoMimic'></a>
    <a href='https://huggingface.co/spaces/BadToBest/EchoMimic'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Demo-yellow'></a>
</div>

## Model Files

```
./pretrained_models/
├── denoising_unet.pth
├── reference_unet.pth
├── motion_module.pth
├── face_locator.pth
├── sd-vae-ft-mse
│   └── ...
├── sd-image-variations-diffusers
│   └── ...
└── audio_processor
    └── whisper_tiny.pt
```

Some models in this hub can be directly downloaded from it's original hub:
- [sd-vae-ft-mse](https://huggingface.co/stabilityai/sd-vae-ft-mse): Weights are intended to be used with the diffusers library. (_Thanks to [stablilityai](https://huggingface.co/stabilityai)_)
- [sd-image-variations-diffusers](https://huggingface.co/lambdalabs/sd-image-variations-diffusers)
- [audio_processor](https://openaipublic.azureedge.net/main/whisper/models/65147644a518d12f04e32d6f3b26facc3f8dd46e5390956a9424a650c0ce22b9/tiny.pt)

## Gallery
### Audio Driven (Sing)

<table class="center">
    
<tr>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/d014d921-9f94-4640-97ad-035b00effbfe" muted="false"></video>
    </td>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/877603a5-a4f9-4486-a19f-8888422daf78" muted="false"></video>
    </td>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/e0cb5afb-40a6-4365-84f8-cb2834c4cfe7" muted="false"></video>
    </td>
</tr>

</table>

### Audio Driven (English)

<table class="center">
    
<tr>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/386982cd-3ff8-470d-a6d9-b621e112f8a5" muted="false"></video>
    </td>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/5c60bb91-1776-434e-a720-8857a00b1501" muted="false"></video>
    </td>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/1f15adc5-0f33-4afa-b96a-2011886a4a06" muted="false"></video>
    </td>
</tr>

</table>

### Audio Driven (Chinese)

<table class="center">
    
<tr>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/a8092f9a-a5dc-4cd6-95be-1831afaccf00" muted="false"></video>
    </td>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/c8b5c59f-0483-42ef-b3ee-4cffae6c7a52" muted="false"></video>
    </td>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/532a3e60-2bac-4039-a06c-ff6bf06cb4a4" muted="false"></video>
    </td>
</tr>

</table>

### Landmark Driven

<table class="center">
    
<tr>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/1da6c46f-4532-4375-a0dc-0a4d6fd30a39" muted="false"></video>
    </td>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/d4f4d5c1-e228-463a-b383-27fb90ed6172" muted="false"></video>
    </td>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/18bd2c93-319e-4d1c-8255-3f02ba717475" muted="false"></video>
    </td>
</tr>

</table>

### Audio + Selected Landmark Driven

<table class="center">
    
<tr>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/4a29d735-ec1b-474d-b843-3ff0bdf85f55" muted="false"></video>
    </td>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/b994c8f5-8dae-4dd8-870f-962b50dc091f" muted="false"></video>
    </td>
    <td width=30% style="border: none">
        <video controls autoplay loop src="https://github.com/BadToBest/EchoMimic/assets/11451501/955c1d51-07b2-494d-ab93-895b9c43b896" muted="false"></video>
    </td>
</tr>

</table>

**（Some demo images above are sourced from image websites. If there is any infringement, we will immediately remove them and apologize.）**

## Citation

If you find our work useful for your research, please consider citing the paper:

```
@misc{chen2024echomimic,
  title={EchoMimic: Lifelike Audio-Driven Portrait Animations through Editable Landmark Conditioning},
  author={Zhiyuan Chen, Jiajiong Cao, Zhiquan Chen, Yuming Li, Chenguang Ma},
  year={2024},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
```