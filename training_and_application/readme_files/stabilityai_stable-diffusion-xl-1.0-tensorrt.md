---
license: openrail++
base_model: stabilityai/stable-diffusion-xl-base-1.0
language:
  - en
tags:
  - stable-diffusion
  - stable-diffusion-xl
  - stable-diffusion-xl-lcm
  - stable-diffusion-xl-lcmlora
  - tensorrt
  - text-to-image
---

# Stable Diffusion XL 1.0 TensorRT

## Introduction

This repository hosts the TensorRT versions(sdxl, sdxl-lcm, sdxl-lcmlora) of **Stable Diffusion XL 1.0** created in collaboration with [NVIDIA](https://huggingface.co/nvidia). The optimized versions give substantial improvements in speed and efficiency.

See the [usage instructions](#usage-example) for how to run the SDXL pipeline with the ONNX files hosted in this repository. 


![examples](./examples.jpg)

## Model Description

- **Developed by:** Stability AI
- **Model type:** Diffusion-based text-to-image generative model
- **License:** [CreativeML Open RAIL++-M License](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/blob/main/LICENSE.md)
- **Model Description:** This is a conversion of the [SDXL base 1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) and [SDXL refiner 1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) models for [NVIDIA TensorRT](https://developer.nvidia.com/tensorrt) optimized inference


## Performance Comparison

#### Timings for 30 steps at 1024x1024

| Accelerator | Baseline (non-optimized) | NVIDIA TensorRT (optimized) | Percentage improvement |
|-------------|--------------------------|-----------------------------|------------------------|
| A10         | 9399 ms                  | 8160 ms                     | ~13%                   |
| A100        | 3704 ms                  | 2742 ms                     | ~26%                   |
| H100        | 2496 ms                  | 1471 ms                     | ~41%                   |

#### Image throughput for 30 steps at 1024x1024

| Accelerator | Baseline (non-optimized) | NVIDIA TensorRT (optimized) | Percentage improvement |
|-------------|--------------------------|-----------------------------|------------------------|
| A10         | 0.10 images/sec          | 0.12 images/sec             | ~20%                   |
| A100        | 0.27 images/sec          | 0.36 images/sec             | ~33%                   |
| H100        | 0.40 images/sec          | 0.68 images/sec             | ~70%                   |

#### Timings for Latent Consistency Model(LCM) version for 4 steps at 1024x1024

| Accelerator | CLIP                     | Unet                        | VAE                    |Total                   |
|-------------|--------------------------|-----------------------------|------------------------|------------------------|
| A100        | 1.08 ms                  | 192.02 ms                   | 228.34 ms              | 426.16 ms              |
| H100        | 0.78 ms                  | 102.8 ms                    | 126.95 ms              | 234.22 ms              |


## Usage Example

1. Following the [setup instructions](https://github.com/rajeevsrao/TensorRT/blob/release/9.2/demo/Diffusion/README.md) on launching a TensorRT NGC container.
```shell
git clone https://github.com/rajeevsrao/TensorRT.git
cd TensorRT
git checkout release/9.2
docker run --rm -it --gpus all -v $PWD:/workspace nvcr.io/nvidia/pytorch:23.11-py3 /bin/bash
```

2. Download the SDXL TensorRT files from this repo
```shell
git lfs install 
git clone https://huggingface.co/stabilityai/stable-diffusion-xl-1.0-tensorrt
cd stable-diffusion-xl-1.0-tensorrt
git lfs pull
cd ..
```

3. Install libraries and requirements
```shell
cd demo/Diffusion
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 -m pip install --pre --upgrade --extra-index-url https://pypi.nvidia.com tensorrt
```

4. Perform TensorRT optimized inference:

  - **SDXL**
    
    The first invocation produces plan files in `engine_xl_base` and `engine_xl_refiner` specific to the accelerator being run on and are reused for later invocations. 

    ```
    python3 demo_txt2img_xl.py \
      "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k" \
      --build-static-batch \
      --use-cuda-graph \
      --num-warmup-runs 1 \
      --width 1024 \
      --height 1024 \
      --denoising-steps 30 \
      --onnx-base-dir /workspace/stable-diffusion-xl-1.0-tensorrt/sdxl-1.0-base \
      --onnx-refiner-dir /workspace/stable-diffusion-xl-1.0-tensorrt/sdxl-1.0-refiner
    ```

  - **SDXL-LCM**
    
    The first invocation produces plan files in --engine-dir specific to the accelerator being run on and are reused for later invocations. 
    ```
    python3 demo_txt2img_xl.py \
      ""Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"" \
      --version=xl-1.0 \
      --onnx-dir /workspace/stable-diffusion-xl-1.0-tensorrt/lcm \
      --engine-dir /workspace/stable-diffusion-xl-1.0-tensorrt/lcm/engine-sdxl-lcm-nocfg \
      --scheduler LCM \
      --denoising-steps 4 \
      --guidance-scale 0.0 \
      --seed 42
    
    ```
  - **SDXL-LCMLORA**

    The first invocation produces plan files in --engine-dir specific to the accelerator being run on and are reused for later invocations. 

    ```
    python3 demo_txt2img_xl.py \
      ""Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"" \
      --version=xl-1.0 \
      --onnx-dir /workspace/stable-diffusion-xl-1.0-tensorrt/lcmlora \
      --engine-dir /workspace/stable-diffusion-xl-1.0-tensorrt/lcm/engine-sdxl-lcmlora-nocfg \
      --scheduler LCM \
      --lora-path latent-consistency/lcm-lora-sdxl \
      --lora-scale 1.0 \
      --denoising-steps 4 \
      --guidance-scale 0.0 \
      --seed 42
    
    ```