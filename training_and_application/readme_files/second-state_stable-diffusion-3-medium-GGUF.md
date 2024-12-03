---
base_model: stabilityai/stable-diffusion-3-medium
license: other
license_name: stabilityai-ai-community
license_link: LICENSE.md
model_creator: stabilityai
model_name: stable-diffusion-3-medium
quantized_by: Second State Inc.
tags:
- text-to-image
- stable-diffusion
- diffusion-single-file
inference: false
language:
- en
pipeline_tag: text-to-image
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# stable-diffusion-3-medium-GGUF

## Original Model

[stabilityai/stable-diffusion-3-medium](https://huggingface.co/stabilityai/stable-diffusion-3-medium)

## Run with `sd-api-server`

Go to the [sd-api-server](https://github.com/LlamaEdge/sd-api-server/blob/main/README.md) repository for more information.

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [sd3-medium-Q4_0.gguf](https://huggingface.co/second-state/stable-diffusion-3-medium-GGUF/blob/main/sd3-medium-Q4_0.gguf) | Q4_0 | 4 | 4.55 GB | |
| [sd3-medium-Q4_1.gguf](https://huggingface.co/second-state/stable-diffusion-3-medium-GGUF/blob/main/sd3-medium-Q4_1.gguf) | Q4_1 | 4 | 5.04 GB | |
| [sd3-medium-Q5_0.gguf](https://huggingface.co/second-state/stable-diffusion-3-medium-GGUF/blob/main/sd3-medium-Q5_0.gguf) | Q5_0 | 5 | 5.53 GB | |
| [sd3-medium-Q5_1.gguf](https://huggingface.co/second-state/stable-diffusion-3-medium-GGUF/blob/main/sd3-medium-Q5_1.gguf) | Q5_1 | 5 | 6.03 GB | |
| [sd3-medium-Q8_0.gguf](https://huggingface.co/second-state/stable-diffusion-3-medium-GGUF/blob/main/sd3-medium-Q8_0.gguf) | Q8_0 | 8 | 8.45 GB | |
| [sd3-medium-f16.gguf](https://huggingface.co/second-state/stable-diffusion-3-medium-GGUF/blob/main/sd3-medium-f16.gguf)   | f16  | 16 | 15.8 GB | |
| [sd3-medium-f32.gguf](https://huggingface.co/second-state/stable-diffusion-3-medium-GGUF/blob/main/sd3-medium-f32.gguf)   | f32  | 32 | 31.5 GB | |

**Quantized with stable-diffusion.cpp `master-697d000`.**