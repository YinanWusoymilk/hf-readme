---
license: other
license_name: stabilityai-ai-community
license_link: LICENSE.md
base_model:
- stabilityai/stable-diffusion-3-medium
pipeline_tag: text-to-video
tags:
- image-to-video
---

# ⚡️Pyramid Flow⚡️

[[Paper]](https://arxiv.org/abs/2410.05954) [[Project Page ✨]](https://pyramid-flow.github.io) [[Code 🚀]](https://github.com/jy0205/Pyramid-Flow) [[demo 🤗](https://huggingface.co/spaces/Pyramid-Flow/pyramid-flow)]

This is the official repository for Pyramid Flow, a training-efficient **Autoregressive Video Generation** method based on **Flow Matching**. By training only on open-source datasets, it generates high-quality 10-second videos at 768p resolution and 24 FPS, and naturally supports image-to-video generation.

<table class="center" border="0" style="width: 100%; text-align: left;">
<tr>
  <th>10s, 768p, 24fps</th>
  <th>5s, 768p, 24fps</th>
  <th>Image-to-video</th>
</tr>
<tr>
  <td><video src="https://pyramid-flow.github.io/static/videos/t2v_10s/fireworks.mp4" autoplay muted loop playsinline></video></td>
  <td><video src="https://pyramid-flow.github.io/static/videos/t2v/trailer.mp4" autoplay muted loop playsinline></video></td>
  <td><video src="https://pyramid-flow.github.io/static/videos/i2v/sunday.mp4" autoplay muted loop playsinline></video></td>
</tr>
</table>

## News

* `COMING SOON` ⚡️⚡️⚡️ Training code and new model checkpoints trained from scratch.
* `2024.10.11`  🤗🤗🤗 [Hugging Face demo](https://huggingface.co/spaces/Pyramid-Flow/pyramid-flow) is available. Thanks [@multimodalart](https://huggingface.co/multimodalart) for the commit! 
* `2024.10.10`  🚀🚀🚀 We release the [technical report](https://arxiv.org/abs/2410.05954), [project page](https://pyramid-flow.github.io) and [model checkpoint](https://huggingface.co/rain1011/pyramid-flow-sd3) of Pyramid Flow.

## Installation

We recommend setting up the environment with conda. The codebase currently uses Python 3.8.10 and PyTorch 2.1.2, and we are actively working to support a wider range of versions.

```bash
git clone https://github.com/jy0205/Pyramid-Flow
cd Pyramid-Flow

# create env using conda
conda create -n pyramid python==3.8.10
conda activate pyramid
pip install -r requirements.txt
```

Then, you can directly download the model from [Huggingface](https://huggingface.co/rain1011/pyramid-flow-sd3). We provide both model checkpoints for 768p and 384p video generation. The 384p checkpoint supports 5-second video generation at 24FPS, while the 768p checkpoint supports up to 10-second video generation at 24FPS.

```python
from huggingface_hub import snapshot_download

model_path = 'PATH'   # The local directory to save downloaded checkpoint
snapshot_download("rain1011/pyramid-flow-sd3", local_dir=model_path, local_dir_use_symlinks=False, repo_type='model')
```

## Usage

To use our model, please follow the inference code in `video_generation_demo.ipynb` at [this link](https://github.com/jy0205/Pyramid-Flow/blob/main/video_generation_demo.ipynb). We further simplify it into the following two-step procedure. First, load the downloaded model:

```python
import torch
from PIL import Image
from pyramid_dit import PyramidDiTForVideoGeneration
from diffusers.utils import load_image, export_to_video

torch.cuda.set_device(0)
model_dtype, torch_dtype = 'bf16', torch.bfloat16   # Use bf16 (not support fp16 yet)

model = PyramidDiTForVideoGeneration(
    'PATH',                                         # The downloaded checkpoint dir
    model_dtype,
    model_variant='diffusion_transformer_768p',     # 'diffusion_transformer_384p'
)

model.vae.to("cuda")
model.dit.to("cuda")
model.text_encoder.to("cuda")
model.vae.enable_tiling()
```

Then, you can try text-to-video generation on your own prompts:

```python
prompt = "A movie trailer featuring the adventures of the 30 year old space man wearing a red wool knitted motorcycle helmet, blue sky, salt desert, cinematic style, shot on 35mm film, vivid colors"

with torch.no_grad(), torch.cuda.amp.autocast(enabled=True, dtype=torch_dtype):
    frames = model.generate(
        prompt=prompt,
        num_inference_steps=[20, 20, 20],
        video_num_inference_steps=[10, 10, 10],
        height=768,     
        width=1280,
        temp=16,                    # temp=16: 5s, temp=31: 10s
        guidance_scale=9.0,         # The guidance for the first frame, set it to 7 for 384p variant
        video_guidance_scale=5.0,   # The guidance for the other video latent
        output_type="pil",
        save_memory=True,           # If you have enough GPU memory, set it to `False` to improve vae decoding speed
    )

export_to_video(frames, "./text_to_video_sample.mp4", fps=24)
```

As an autoregressive model, our model also supports (text conditioned) image-to-video generation:

```python
image = Image.open('assets/the_great_wall.jpg').convert("RGB").resize((1280, 768))
prompt = "FPV flying over the Great Wall"

with torch.no_grad(), torch.cuda.amp.autocast(enabled=True, dtype=torch_dtype):
    frames = model.generate_i2v(
        prompt=prompt,
        input_image=image,
        num_inference_steps=[10, 10, 10],
        temp=16,
        video_guidance_scale=4.0,
        output_type="pil",
        save_memory=True,           # If you have enough GPU memory, set it to `False` to improve vae decoding speed
    )

export_to_video(frames, "./image_to_video_sample.mp4", fps=24)
```

We also support CPU offloading to allow inference with **less than 12GB** of GPU memory by adding a `cpu_offloading=True` parameter. This feature was contributed by [@Ednaordinary](https://github.com/Ednaordinary), see [#23](https://github.com/jy0205/Pyramid-Flow/pull/23) for details.

## Usage tips

* The `guidance_scale` parameter controls the visual quality. We suggest using a guidance within [7, 9] for the 768p checkpoint during text-to-video generation, and 7 for the 384p checkpoint.
* The `video_guidance_scale` parameter controls the motion. A larger value increases the dynamic degree and mitigates the autoregressive generation degradation, while a smaller value stabilizes the video.
* For 10-second video generation, we recommend using a guidance scale of 7 and a video guidance scale of 5.

## Gallery

The following video examples are generated at 5s, 768p, 24fps. For more results, please visit our [project page](https://pyramid-flow.github.io).

<table class="center" border="0" style="width: 100%; text-align: left;">
<tr>
  <td><video src="https://pyramid-flow.github.io/static/videos/t2v/tokyo.mp4" autoplay muted loop playsinline></video></td>
  <td><video src="https://pyramid-flow.github.io/static/videos/t2v/eiffel.mp4" autoplay muted loop playsinline></video></td>
</tr>
<tr>
  <td><video src="https://pyramid-flow.github.io/static/videos/t2v/waves.mp4" autoplay muted loop playsinline></video></td>
  <td><video src="https://pyramid-flow.github.io/static/videos/t2v/rail.mp4" autoplay muted loop playsinline></video></td>
</tr>
</table>

## Acknowledgement

We are grateful for the following awesome projects when implementing Pyramid Flow:

* [SD3 Medium](https://huggingface.co/stabilityai/stable-diffusion-3-medium) and [Flux 1.0](https://huggingface.co/black-forest-labs/FLUX.1-dev): State-of-the-art image generation models based on flow matching.
* [Diffusion Forcing](https://boyuan.space/diffusion-forcing) and [GameNGen](https://gamengen.github.io): Next-token prediction meets full-sequence diffusion.
* [WebVid-10M](https://github.com/m-bain/webvid), [OpenVid-1M](https://github.com/NJU-PCALab/OpenVid-1M) and [Open-Sora Plan](https://github.com/PKU-YuanGroup/Open-Sora-Plan): Large-scale datasets for text-to-video generation.
* [CogVideoX](https://github.com/THUDM/CogVideo): An open-source text-to-video generation model that shares many training details.
* [Video-LLaMA2](https://github.com/DAMO-NLP-SG/VideoLLaMA2): An open-source video LLM for our video recaptioning.

## Citation

Consider giving this repository a star and cite Pyramid Flow in your publications if it helps your research.
```
@article{jin2024pyramidal,
  title={Pyramidal Flow Matching for Efficient Video Generative Modeling},
  author={Jin, Yang and Sun, Zhicheng and Li, Ningyuan and Xu, Kun and Xu, Kun and Jiang, Hao and Zhuang, Nan and Huang, Quzhe and Song, Yang and Mu, Yadong and Lin, Zhouchen},
  jounal={arXiv preprint arXiv:2410.05954},
  year={2024}
}
```