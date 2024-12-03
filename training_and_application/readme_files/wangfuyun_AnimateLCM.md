---
pipeline_tag: text-to-video
---
# AnimateLCM for Fast Video Generation in 4 steps.

[AnimateLCM: Accelerating the Animation of Personalized Diffusion Models and Adapters with Decoupled Consistency Learning](https://arxiv.org/abs/2402.00769) by Fu-Yun Wang et al.

## We also support fast image-to-video generation, please see [AnimateLCM-SVD-xt](https://huggingface.co/wangfuyun/AnimateLCM-SVD-xt) and [AnimateLCM-I2V](https://huggingface.co/wangfuyun/AnimateLCM-I2V).

For more details, please refer to our [[paper](https://arxiv.org/abs/2402.00769)] | [[code](https://github.com/G-U-N/AnimateLCM)] | [[proj-page](https://animatelcm.github.io/)] | [[civitai](https://civitai.com/models/290375/animatelcm-fast-video-generation)].

<video controls autoplay src="https://cdn-uploads.huggingface.co/production/uploads/63e9e92f20c109718713f5eb/KCwSoZCdxkkmtDg1LuXsP.mp4"></video>

## Using AnimateLCM with Diffusers

```python
import torch
from diffusers import AnimateDiffPipeline, LCMScheduler, MotionAdapter
from diffusers.utils import export_to_gif

adapter = MotionAdapter.from_pretrained("wangfuyun/AnimateLCM", torch_dtype=torch.float16)
pipe = AnimateDiffPipeline.from_pretrained("emilianJR/epiCRealism", motion_adapter=adapter, torch_dtype=torch.float16)
pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config, beta_schedule="linear")

pipe.load_lora_weights("wangfuyun/AnimateLCM", weight_name="AnimateLCM_sd15_t2v_lora.safetensors", adapter_name="lcm-lora")
pipe.set_adapters(["lcm-lora"], [0.8])

pipe.enable_vae_slicing()
pipe.enable_model_cpu_offload()

output = pipe(
    prompt="A space rocket with trails of smoke behind it launching into space from the desert, 4k, high resolution",
    negative_prompt="bad quality, worse quality, low resolution",
    num_frames=16,
    guidance_scale=2.0,
    num_inference_steps=6,
    generator=torch.Generator("cpu").manual_seed(0),
)
frames = output.frames[0]
export_to_gif(frames, "animatelcm.gif")
```
