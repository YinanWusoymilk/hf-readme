---
pipeline_tag: video-to-video
license: cc-by-nc-4.0
---
![model example](https://i.imgur.com/ze1DGOJ.png)
[example outputs](https://www.youtube.com/watch?v=HO3APT_0UA4) (courtesy of [dotsimulate](https://www.instagram.com/dotsimulate/))

# zeroscope_v2 XL
A watermark-free Modelscope-based video model capable of generating high quality video at 1024 x 576. This model was trained from the [original weights](https://huggingface.co/damo-vilab/modelscope-damo-text-to-video-synthesis) with offset noise using 9,923 clips and 29,769 tagged frames at 24 frames, 1024x576 resolution.<br />
zeroscope_v2_XL is specifically designed for upscaling content made with [zeroscope_v2_576w](https://huggingface.co/cerspense/zeroscope_v2_567w) using vid2vid in the [1111 text2video](https://github.com/kabachuha/sd-webui-text2video) extension by [kabachuha](https://github.com/kabachuha). Leveraging this model as an upscaler allows for superior overall compositions at higher resolutions, permitting faster exploration in 576x320 (or 448x256) before transitioning to a high-resolution render.<br />

zeroscope_v2_XL uses 15.3gb of vram when rendering 30 frames at 1024x576

### Using it with the 1111 text2video extension
1. Download files in the zs2_XL folder.
2. Replace the respective files in the 'stable-diffusion-webui\models\ModelScope\t2v' directory.
### Upscaling recommendations
For upscaling, it's recommended to use the 1111 extension. It works best at 1024x576 with a denoise strength between 0.66 and 0.85. Remember to use the same prompt that was used to generate the original clip.

### Usage in 🧨 Diffusers

Let's first install the libraries required:

```bash
$ pip install git+https://github.com/huggingface/diffusers.git
$ pip install transformers accelerate torch
```

Now, let's first generate a low resolution video using [cerspense/zeroscope_v2_576w](https://huggingface.co/cerspense/zeroscope_v2_576w).

```py
import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_576w", torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()
pipe.enable_vae_slicing()
pipe.unet.enable_forward_chunking(chunk_size=1, dim=1) # disable if enough memory as this slows down significantly

prompt = "Darth Vader is surfing on waves"
video_frames = pipe(prompt, num_inference_steps=40, height=320, width=576, num_frames=36).frames
video_path = export_to_video(video_frames)
```

Next, we can upscale it using [cerspense/zeroscope_v2_XL](https://huggingface.co/cerspense/zeroscope_v2_XL).

```py
pipe = DiffusionPipeline.from_pretrained("cerspense/zeroscope_v2_XL", torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_model_cpu_offload()
pipe.enable_vae_slicing()

video = [Image.fromarray(frame).resize((1024, 576)) for frame in video_frames]

video_frames = pipe(prompt, video=video, strength=0.6).frames
video_path = export_to_video(video_frames, output_video_path="/home/patrick/videos/video_1024_darth_vader_36.mp4")
```

Here are some results:

<table>
    <tr>
        Darth vader is surfing on waves.
        <br>
        <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/darth_vader_36_1024.gif"
            alt="Darth vader surfing in waves."
            style="width: 576;" />
        </center></td>
    </tr>
</table>


### Known issues
Rendering at lower resolutions or fewer than 24 frames could lead to suboptimal outputs. <br />


Thanks to [camenduru](https://github.com/camenduru), [kabachuha](https://github.com/kabachuha), [ExponentialML](https://github.com/ExponentialML), [dotsimulate](https://www.instagram.com/dotsimulate/), [VANYA](https://twitter.com/veryVANYA), [polyware](https://twitter.com/polyware_ai), [tin2tin](https://github.com/tin2tin)<br />