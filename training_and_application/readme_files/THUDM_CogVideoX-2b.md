---
license: apache-2.0
language:
  - en
tags:
  - cogvideox
  - video-generation
  - thudm
  - text-to-video
inference: false
---

# CogVideoX-2B

<p style="text-align: center;">
  <div align="center">
  <img src=https://github.com/THUDM/CogVideo/raw/main/resources/logo.svg width="50%"/>
  </div>
  <p align="center">
  <a href="https://huggingface.co/THUDM/CogVideoX-2b/blob/main/README_zh.md">📄 中文阅读</a> | 
  <a href="https://huggingface.co/spaces/THUDM/CogVideoX-2B-Space">🤗 Huggingface Space</a> |
  <a href="https://github.com/THUDM/CogVideo">🌐 Github </a> | 
  <a href="https://arxiv.org/pdf/2408.06072">📜 arxiv </a>
</p>
<p align="center">
📍 Visit <a href="https://chatglm.cn/video?lang=en?fr=osm_cogvideo">QingYing</a> and <a href="https://open.bigmodel.cn/?utm_campaign=open&_channel_track_key=OWTVNma9">API Platform</a> to experience commercial video generation models.
</p>

## Demo Show

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video Gallery with Captions</title>
    <style>
        .video-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }
        .video-item {
            width: 45%;
            margin-bottom: 20px;
            transition: transform 0.3s;
        }
        .video-item:hover {
            transform: scale(1.1);
        }
        .caption {
            text-align: center;
            margin-top: 10px;
            font-size: 11px;
        }
    </style>
</head>
<body>
    <div class="video-container">
        <div class="video-item">
            <video width="100%" controls>
                <source src="https://github.com/THUDM/CogVideo/raw/main/resources/videos/1.mp4" type="video/mp4">
            </video>
            <div class="caption">A detailed wooden toy ship with intricately carved masts and sails is seen gliding smoothly over a plush, blue carpet that mimics the waves of the sea. The ship's hull is painted a rich brown, with tiny windows. The carpet, soft and textured, provides a perfect backdrop, resembling an oceanic expanse. Surrounding the ship are various other toys and children's items, hinting at a playful environment. The scene captures the innocence and imagination of childhood, with the toy ship's journey symbolizing endless adventures in a whimsical, indoor setting.</div>
        </div>
        <div class="video-item">
            <video width="100%" controls>
                <source src="https://github.com/THUDM/CogVideo/raw/main/resources/videos/2.mp4" type="video/mp4">
            </video>
            <div class="caption">The camera follows behind a white vintage SUV with a black roof rack as it speeds up a steep dirt road surrounded by pine trees on a steep mountain slope, dust kicks up from it’s tires, the sunlight shines on the SUV as it speeds along the dirt road, casting a warm glow over the scene. The dirt road curves gently into the distance, with no other cars or vehicles in sight. The trees on either side of the road are redwoods, with patches of greenery scattered throughout. The car is seen from the rear following the curve with ease, making it seem as if it is on a rugged drive through the rugged terrain. The dirt road itself is surrounded by steep hills and mountains, with a clear blue sky above with wispy clouds.</div>
        </div>
        <div class="video-item">
            <video width="100%" controls>
                <source src="https://github.com/THUDM/CogVideo/raw/main/resources/videos/3.mp4" type="video/mp4">
            </video>
            <div class="caption">A street artist, clad in a worn-out denim jacket and a colorful bandana, stands before a vast concrete wall in the heart, holding a can of spray paint, spray-painting a colorful bird on a mottled wall.</div>
        </div>
        <div class="video-item">
            <video width="100%" controls>
                <source src="https://github.com/THUDM/CogVideo/raw/main/resources/videos/4.mp4" type="video/mp4">
            </video>
            <div class="caption"> In the haunting backdrop of a war-torn city, where ruins and crumbled walls tell a story of devastation, a poignant close-up frames a young girl. Her face is smudged with ash, a silent testament to the chaos around her. Her eyes glistening with a mix of sorrow and resilience, capturing the raw emotion of a world that has lost its innocence to the ravages of conflict.</div>
        </div>
    </div>
</body>
</html>

## Model Introduction

CogVideoX is an open-source version of the video generation model originating
from [QingYing](https://chatglm.cn/video?lang=en?fr=osm_cogvideo). The table below displays the list of video generation
models we currently offer, along with their foundational information.

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">Model Name</th>
    <th style="text-align: center;">CogVideoX-2B (This Repository)</th>
    <th style="text-align: center;">CogVideoX-5B</th>
  </tr>
  <tr>
    <td style="text-align: center;">Model Description</td>
    <td style="text-align: center;">Entry-level model, balancing compatibility. Low cost for running and secondary development.</td>
    <td style="text-align: center;">Larger model with higher video generation quality and better visual effects.</td>
  </tr>
  <tr>
    <td style="text-align: center;">Inference Precision</td>
    <td style="text-align: center;"><b>FP16* (Recommended)</b>, BF16, FP32, FP8*, INT8, no support for INT4</td>
    <td style="text-align: center;"><b>BF16 (Recommended)</b>, FP16, FP32, FP8*, INT8, no support for INT4</td>
  </tr>
  <tr>
    <td style="text-align: center;">Single GPU VRAM Consumption<br></td>
    <td style="text-align: center;"><a href="https://github.com/THUDM/SwissArmyTransformer">SAT</a> FP16: 18GB <br><b>diffusers FP16: starting from 4GB*</b><br><b>diffusers INT8(torchao): starting from 3.6GB*</b></td>
    <td style="text-align: center;"><a href="https://github.com/THUDM/SwissArmyTransformer">SAT</a> BF16: 26GB <br><b>diffusers BF16: starting from 5GB*</b><br><b>diffusers INT8(torchao): starting from 4.4GB*</b></td>
  </tr>
  <tr>
    <td style="text-align: center;">Multi-GPU Inference VRAM Consumption</td>
    <td style="text-align: center;"><b>FP16: 10GB* using diffusers</b></td>
    <td style="text-align: center;"><b>BF16: 15GB* using diffusers</b></td>
  </tr>
  <tr>
    <td style="text-align: center;">Inference Speed<br>(Step = 50, FP/BF16)</td>
    <td style="text-align: center;">Single A100: ~90 seconds<br>Single H100: ~45 seconds</td>
    <td style="text-align: center;">Single A100: ~180 seconds<br>Single H100: ~90 seconds</td>
  </tr>
  <tr>
    <td style="text-align: center;">Fine-tuning Precision</td>
    <td style="text-align: center;"><b>FP16</b></td>
    <td style="text-align: center;"><b>BF16</b></td>
  </tr>
  <tr>
    <td style="text-align: center;">Fine-tuning VRAM Consumption (per GPU)</td>
    <td style="text-align: center;">47 GB (bs=1, LORA)<br> 61 GB (bs=2, LORA)<br> 62GB (bs=1, SFT)</td>
    <td style="text-align: center;">63 GB (bs=1, LORA)<br> 80 GB (bs=2, LORA)<br> 75GB (bs=1, SFT)</td>
  </tr>
  <tr>
    <td style="text-align: center;">Prompt Language</td>
    <td colspan="2" style="text-align: center;">English*</td>
  </tr>
  <tr>
    <td style="text-align: center;">Prompt Length Limit</td>
    <td colspan="2" style="text-align: center;">226 Tokens</td>
  </tr>
  <tr>
    <td style="text-align: center;">Video Length</td>
    <td colspan="2" style="text-align: center;">6 Seconds</td>
  </tr>
  <tr>
    <td style="text-align: center;">Frame Rate</td>
    <td colspan="2" style="text-align: center;">8 Frames per Second</td>
  </tr>
  <tr>
    <td style="text-align: center;">Video Resolution</td>
    <td colspan="2" style="text-align: center;">720 x 480, no support for other resolutions (including fine-tuning)</td>
  </tr>
  <tr>
    <td style="text-align: center;">Positional Encoding</td>
    <td style="text-align: center;">3d_sincos_pos_embed</td>
    <td style="text-align: center;">3d_rope_pos_embed</td>
  </tr>
</table>

**Data Explanation**

+ When testing using the `diffusers` library, all optimizations provided by the `diffusers` library were enabled. This
  solution has not been tested for actual VRAM/memory usage on devices other than **NVIDIA A100 / H100**. Generally,
  this solution can be adapted to all devices with **NVIDIA Ampere architecture** and above. If the optimizations are
  disabled, VRAM usage will increase significantly, with peak VRAM usage being about 3 times higher than the table
  shows. However, speed will increase by 3-4 times. You can selectively disable some optimizations, including:

```
pipe.enable_model_cpu_offload()
pipe.enable_sequential_cpu_offload()
pipe.vae.enable_slicing()
pipe.vae.enable_tiling()
``` 

+ When performing multi-GPU inference, the `enable_model_cpu_offload()` optimization needs to be disabled.
+ Using INT8 models will reduce inference speed. This is to ensure that GPUs with lower VRAM can perform inference
  normally while maintaining minimal video quality loss, though inference speed will decrease significantly.
+ The 2B model is trained with `FP16` precision, and the 5B model is trained with `BF16` precision. We recommend using
  the precision the model was trained with for inference.
+ [PytorchAO](https://github.com/pytorch/ao) and [Optimum-quanto](https://github.com/huggingface/optimum-quanto/) can be
  used to quantize the text encoder, Transformer, and VAE modules to reduce CogVideoX's memory requirements. This makes
  it possible to run the model on a free T4 Colab or GPUs with smaller VRAM! It is also worth noting that TorchAO
  quantization is fully compatible with `torch.compile`, which can significantly improve inference speed. `FP8`
  precision must be used on devices with `NVIDIA H100` or above, which requires installing
  the `torch`, `torchao`, `diffusers`, and `accelerate` Python packages from source. `CUDA 12.4` is recommended.
+ The inference speed test also used the above VRAM optimization scheme. Without VRAM optimization, inference speed
  increases by about 10%. Only the `diffusers` version of the model supports quantization.
+ The model only supports English input; other languages can be translated into English during refinement by a large
  model.

**Note**

+ Using [SAT](https://github.com/THUDM/SwissArmyTransformer)  for inference and fine-tuning of SAT version
  models. Feel free to visit our GitHub for more information.

## Quick Start 🤗

This model supports deployment using the huggingface diffusers library. You can deploy it by following these steps.

**We recommend that you visit our [GitHub](https://github.com/THUDM/CogVideo) and check out the relevant prompt
optimizations and conversions to get a better experience.**

1. Install the required dependencies

```shell
# diffusers>=0.30.1
# transformers>=0.44.0
# accelerate>=0.33.0 (suggest install from source)
# imageio-ffmpeg>=0.5.1
pip install --upgrade transformers accelerate diffusers imageio-ffmpeg 
```

2. Run the code

```python
import torch
from diffusers import CogVideoXPipeline
from diffusers.utils import export_to_video

prompt = "A panda, dressed in a small, red jacket and a tiny hat, sits on a wooden stool in a serene bamboo forest. The panda's fluffy paws strum a miniature acoustic guitar, producing soft, melodic tunes. Nearby, a few other pandas gather, watching curiously and some clapping in rhythm. Sunlight filters through the tall bamboo, casting a gentle glow on the scene. The panda's face is expressive, showing concentration and joy as it plays. The background includes a small, flowing stream and vibrant green foliage, enhancing the peaceful and magical atmosphere of this unique musical performance."

pipe = CogVideoXPipeline.from_pretrained(
    "THUDM/CogVideoX-2b",
    torch_dtype=torch.float16
)

pipe.enable_model_cpu_offload()
pipe.enable_sequential_cpu_offload()
pipe.vae.enable_slicing()
pipe.vae.enable_tiling()
video = pipe(
    prompt=prompt,
    num_videos_per_prompt=1,
    num_inference_steps=50,
    num_frames=49,
    guidance_scale=6,
    generator=torch.Generator(device="cuda").manual_seed(42),
).frames[0]

export_to_video(video, "output.mp4", fps=8)
```

## Quantized Inference

[PytorchAO](https://github.com/pytorch/ao) and [Optimum-quanto](https://github.com/huggingface/optimum-quanto/) can be
used to quantize the Text Encoder, Transformer and VAE modules to lower the memory requirement of CogVideoX. This makes
it possible to run the model on free-tier T4 Colab or smaller VRAM GPUs as well! It is also worth noting that TorchAO
quantization is fully compatible with `torch.compile`, which allows for much faster inference speed.

```diff
# To get started, PytorchAO needs to be installed from the GitHub source and PyTorch Nightly.
# Source and nightly installation is only required until next release.

import torch
from diffusers import AutoencoderKLCogVideoX, CogVideoXTransformer3DModel, CogVideoXPipeline
from diffusers.utils import export_to_video
+ from transformers import T5EncoderModel
+ from torchao.quantization import quantize_, int8_weight_only, int8_dynamic_activation_int8_weight

+ quantization = int8_weight_only

+ text_encoder = T5EncoderModel.from_pretrained("THUDM/CogVideoX-5b", subfolder="text_encoder", torch_dtype=torch.bfloat16)
+ quantize_(text_encoder, quantization())

+ transformer = CogVideoXTransformer3DModel.from_pretrained("THUDM/CogVideoX-5b", subfolder="transformer", torch_dtype=torch.bfloat16)
+ quantize_(transformer, quantization())

+ vae = AutoencoderKLCogVideoX.from_pretrained("THUDM/CogVideoX-2b", subfolder="vae", torch_dtype=torch.bfloat16)
+ quantize_(vae, quantization())

# Create pipeline and run inference
pipe = CogVideoXPipeline.from_pretrained(
    "THUDM/CogVideoX-2b",
+    text_encoder=text_encoder,
+    transformer=transformer,
+    vae=vae,
    torch_dtype=torch.bfloat16,
)
pipe.enable_model_cpu_offload()
pipe.vae.enable_tiling()

prompt = "A panda, dressed in a small, red jacket and a tiny hat, sits on a wooden stool in a serene bamboo forest. The panda's fluffy paws strum a miniature acoustic guitar, producing soft, melodic tunes. Nearby, a few other pandas gather, watching curiously and some clapping in rhythm. Sunlight filters through the tall bamboo, casting a gentle glow on the scene. The panda's face is expressive, showing concentration and joy as it plays. The background includes a small, flowing stream and vibrant green foliage, enhancing the peaceful and magical atmosphere of this unique musical performance."

video = pipe(
    prompt=prompt,
    num_videos_per_prompt=1,
    num_inference_steps=50,
    num_frames=49,
    guidance_scale=6,
    generator=torch.Generator(device="cuda").manual_seed(42),
).frames[0]

export_to_video(video, "output.mp4", fps=8)
```

Additionally, the models can be serialized and stored in a quantized datatype to save disk space when using PytorchAO.
Find examples and benchmarks at these links:

- [torchao](https://gist.github.com/a-r-r-o-w/4d9732d17412888c885480c6521a9897)
- [quanto](https://gist.github.com/a-r-r-o-w/31be62828b00a9292821b85c1017effa)

## Explore the Model

Welcome to our [github](https://github.com/THUDM/CogVideo), where you will find:

1. More detailed technical details and code explanation.
2. Optimization and conversion of prompt words.
3. Reasoning and fine-tuning of SAT version models, and even pre-release.
4. Project update log dynamics, more interactive opportunities.
5. CogVideoX toolchain to help you better use the model.
6. INT8 model inference code support.

## Model License

The CogVideoX-2B model (including its corresponding Transformers module and VAE module) is released under
the [Apache 2.0 License](LICENSE).

The CogVideoX-5B model (Transformers module) is released under
the [CogVideoX LICENSE](https://huggingface.co/THUDM/CogVideoX-5b/blob/main/LICENSE).

## Citation

```
@article{yang2024cogvideox,
  title={CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer},
  author={Yang, Zhuoyi and Teng, Jiayan and Zheng, Wendi and Ding, Ming and Huang, Shiyu and Xu, Jiazheng and Yang, Yuanming and Hong, Wenyi and Zhang, Xiaohan and Feng, Guanyu and others},
  journal={arXiv preprint arXiv:2408.06072},
  year={2024}
}
```