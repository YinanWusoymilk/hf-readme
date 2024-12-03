---
license: mit
pipeline_tag: text-generation
tags: [ONNX, DML, ONNXRuntime, phi3, nlp, conversational, custom_code]
inference: false
---

# Phi-3 Mini-4K-Instruct ONNX models

<!-- Provide a quick summary of what the model is/does. -->
This repository hosts the optimized versions of [Phi-3-mini-4k-instruct](https://aka.ms/phi3-mini-4k-instruct) to accelerate inference with ONNX Runtime.

Phi-3 Mini is a lightweight, state-of-the-art open model built upon datasets used for Phi-2 - synthetic data and filtered websites - with a focus on very high-quality, reasoning dense data. The model belongs to the Phi-3 model family, and the mini version comes in two variants: 4K and 128K which is the context length (in tokens) it can support. The model underwent a rigorous enhancement process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.

Optimized Phi-3 Mini models are published here in [ONNX](https://onnx.ai) format to run with [ONNX Runtime](https://onnxruntime.ai/) on CPU and GPU across devices, including server platforms, Windows, Linux and Mac desktops, and mobile CPUs, with the precision best suited to each of these targets.

[DirectML](https://aka.ms/directml) support lets developers bring hardware acceleration to Windows devices at scale across AMD, Intel, and NVIDIA GPUs. Along with DirectML, ONNX Runtime provides cross platform support for Phi-3 Mini across a range of devices for CPU, GPU, and mobile.

To easily get started with Phi-3, you can use our newly introduced ONNX Runtime Generate() API. See [here](https://aka.ms/generate-tutorial) for instructions on how to run it.

## ONNX Models 

Here are some of the optimized configurations we have added:  

1. ONNX model for int4 DML: ONNX model for AMD, Intel, and NVIDIA GPUs on Windows, quantized to int4 using [AWQ](https://arxiv.org/abs/2306.00978).
2. ONNX model for fp16 CUDA: ONNX model you can use to run for your NVIDIA GPUs.
3. ONNX model for int4 CUDA: ONNX model for NVIDIA GPUs using int4 quantization via RTN.
4. ONNX model for int4 CPU and Mobile: ONNX model for CPU and mobile using int4 quantization via RTN. There are two versions uploaded to balance latency vs. accuracy.
   Acc=1 is targeted at improved accuracy, while Acc=4 is for improved perf. For mobile devices, we recommend using the model with acc-level-4.
   

More updates on AMD, and additional optimizations on CPU and Mobile will be added with the official ORT 1.18 release in early May. Stay tuned!

## Hardware Supported

The models are tested on:
- GPU SKU: RTX 4090 (DirectML)
- GPU SKU: 1 A100 80GB GPU, SKU: Standard_ND96amsr_A100_v4 (CUDA)
- CPU SKU: Standard F64s v2 (64 vcpus, 128 GiB memory) 
- Mobile SKU: Samsung Galaxy S21

Minimum Configuration Required:
- Windows: DirectX 12-capable GPU and a minimum of 4GB of combined RAM
- CUDA: NVIDIA GPU with [Compute Capability](https://developer.nvidia.com/cuda-gpus) >= 7.0

### Model Description

- **Developed by:**  Microsoft
- **Model type:** ONNX
- **Language(s) (NLP):** Python, C, C++
- **License:** MIT
- **Model Description:** This is a conversion of the Phi-3 Mini-4K-Instruct model for ONNX Runtime inference.

## Additional Details
- [**ONNX Runtime Optimizations Blog Link**](https://aka.ms/phi3-optimizations) 
- [**Phi-3 Model Blog Link**](https://aka.ms/phi3blog-april)
- [**Phi-3 Model Card**]( https://aka.ms/phi3-mini-4k-instruct)
- [**Phi-3 Technical Report**](https://aka.ms/phi3-tech-report)

## How to Get Started with the Model
To make running of the Phi-3 models across a range of devices and platforms across various execution provider backends possible, we introduce a new API to wrap several aspects of generative AI inferencing. This API make it easy to drag and drop LLMs straight into your app. For running the early version of these models with ONNX Runtime, follow the steps [here](http://aka.ms/generate-tutorial).

For example:

```python
python model-qa.py -m /*{YourModelPath}*/onnx/cpu_and_mobile/phi-3-mini-4k-instruct-int4-cpu -k 40 -p 0.95 -t 0.8 -r 1.0
```

```
*Input:*  <|user|>Tell me a joke<|end|><|assistant|>

*Output:*  Why don't scientists trust atoms?
           Because they make up everything!

This joke plays on the double meaning of "make up." In science, atoms are the fundamental building blocks of matter, literally making up everything. However, in a colloquial sense, "to make up" can mean to fabricate or lie, hence the humor.
```
## Performance Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->
### DirectML on Windows
We measured the performance of DirectML and ONNX Runtime's new Generate() API with Phi-3 Mini quantized with Activation-Aware Quantization ([AWQ](https://arxiv.org/abs/2306.00978)) and with a block size of 128 on Windows. Our test machine had an NVIDIA GeForce RTX 4090 GPU and an Intel Core i9-13900K CPU. DirectML lets developers not only achieve great performance but also lets developers deploy models across the entire Windows ecosystem with support from AMD, Intel, and NVIDIA. Best of all, AWQ means that developers get this scale while also maintaining high model accuracy.

Stay tuned for additional performance improvements in the coming weeks thanks to optimized drivers from our hardware partners, along with additional updates to the ONNX Runtime Generate() API.


| Batch Size, Prompt Length | Generation Length | Wall Clock Throughput (tps) |
|---------------------------|-------------------|-----------------------------|
| 1, 16 | 256  | 266.65 |
| 1, 16 | 512  | 251.63 |
| 1, 16 | 1024 | 238.87 |
| 1, 16 | 2048 | 217.5  |
| 1, 32 | 256  | 278.53 |
| 1, 32 | 512  | 259.73 |
| 1, 32 | 1024 | 241.72 |
| 1, 32 | 2048 | 219.3  |
| 1, 64 | 256  | 308.26 |
| 1, 64 | 512  | 272.47 |
| 1, 64 | 1024 | 245.67 |


### CUDA

Phi-3 Mini-4K-Instruct performs better in ONNX Runtime than PyTorch for all batch size, prompt length combinations. For FP16 CUDA, ORT performs up to 5X faster than PyTorch, while with INT4 CUDA it's up to 10X faster than PyTorch. It is also up to 3X faster than Llama.cpp for large batch sizes. 

The table below shows the average throughput of the first 256 tokens generated (tps) for FP16 and INT4 precisions on CUDA as measured on [1 A100 80GB GPU, SKU: Standard_ND96amsr_A100_v4](https://learn.microsoft.com/en-us/azure/virtual-machines/ndm-a100-v4-series).


| Batch Size, Prompt Length | ORT FP16 CUDA | PyTorch Compile FP16 CUDA | Llama.cpp | Speed Up ORT/PyTorch | Speed Up ORT/Llama.cpp |
|---------------------------|---------------|---------------------------|-----------|----------------------|------------------------|
| 1, 16    | 124.74  | 23.95  | 109.47 | 5.21 | 1.14 |
| 1, 64    | 123.38  | 26.66  | 110.26 | 4.63 | 1.12 |
| 1, 256   | 116.17  | 29.66  | 109.42 | 3.92 | 1.06 |
| 1, 1024  | 103.27  | 29.67  | 105.60 | 3.48 | 0.98 |
| 1, 2048  | 92.11   | 27.74  | 102.00 | 3.32 | 0.90 |
| 1, 4096  | 83.24   | 27.71  | 95.17  | 3.00 | 0.87 |
| 4, 16    | 507.16  | 113.82 | 349.56 | 4.46 | 1.45 |
| 4, 64    | 492.15  | 111.63 | 342.45 | 4.41 | 1.44 |
| 4, 256   | 446.25  | 112.85 | 317.02 | 3.95 | 1.41 |
| 4, 1024  | 338.82  | 114.57 | 246.32 | 2.96 | 1.38 |
| 4, 2048  | 262.85  | 105.71 | 189.34 | 2.49 | 1.39 |
| 4, 4096  | 200.46  | 81.36  | 131.16 | 2.46 | 1.53 |
| 16, 16   | 1648.33 | 481.10 | 893.34 | 3.43 | 1.85 |
| 16, 64   | 1533.04 | 470.57 | 802.73 | 3.26 | 1.91 |
| 16, 256  | 1206.64 | 482.87 | 575.24 | 2.50 | 2.10 |
| 16, 1024 | 672.45  | 342.86 | 262.41 | 1.96 | 2.56 |
| 16, 2048 | 437.28  | 156.48 | 148.79 | 2.79 | 2.94 |
| 16, 4096 | 291.14  | OOM    | 79.72  |      | 3.65 |


| Batch Size, Prompt Length | ORT INT4 CUDA | PyTorch Eager INT4 CUDA | Llama.cpp INT4 CUDA | Speed Up ORT/PyTorch | Speed Up ORT/Llama.cpp |
|---------------------------|---------------|-------------------------|---------------------|----------------------|------------------------|
| 1, 16    | 218.43  | 20.85  | 146.84 | 10.48 | 1.49 |
| 1, 64    | 213.41  | 20.86  | 149.35 | 10.23 | 1.43 |
| 1, 256   | 192.29  | 20.90  | 147.82 | 9.20  | 1.30 |
| 1, 1024  | 158.60  | 20.86  | 141.03 | 7.60  | 1.12 |
| 1, 2048  | 132.74  | 19.99  | 135.32 | 6.64  | 0.98 |
| 1, 4096  | 115.44  | 18.34  | 123.29 | 6.30  | 0.94 |
| 4, 16    | 291.75  | 68.45  | 378.89 | 4.26  | 0.77 |
| 4, 64    | 286.83  | 68.63  | 370.86 | 4.18  | 0.77 |
| 4, 256   | 269.77  | 68.27  | 341.23 | 3.95  | 0.79 |
| 4, 1024  | 224.34  | 68.47  | 260.11 | 3.28  | 0.86 |
| 4, 2048  | 187.09  | 65.53  | 196.91 | 2.86  | 0.95 |
| 4, 4096  | 153.44  | 54.88  | 134.73 | 2.80  | 1.14 |
| 16, 16   | 1030.87 | 272.84 | 648.29 | 3.78  | 1.59 |
| 16, 64   | 982.78  | 272.66 | 598.96 | 3.60  | 1.64 |
| 16, 256  | 835.82  | 273.95 | 461.85 | 3.05  | 1.81 |
| 16, 1024 | 540.11  | 226.96 | 235.99 | 2.38  | 2.29 |
| 16, 2048 | 377.84  | 127.05 | 139.97 | 2.97  | 2.70 |
| 16, 4096 | 263.52  | OOM    | 77.11  |       | 3.42 |


### CPU

The table below shows the average throughput of the first 256 tokens generated (tps) for INT4 precision on CPU as measured on a [Standard F64s v2 (64 vcpus, 128 GiB memory)](https://learn.microsoft.com/en-us/azure/virtual-machines/fsv2-series).

| Batch Size, Prompt Length | ORT INT4 CPU | Llama.cpp | Speed Up ORT/Llama.cpp |
|---------------------------|--------------|-----------|------------------------|
| 1, 16   | 14.97 | 13.57 | 1.10 |
| 1, 64   | 14.47 | 10.39 | 1.39 |
| 1, 256  | 13.32 | 10.31 | 1.29 |
| 1, 1024 | 10.14 | 9.83  | 1.03 |
| 1, 2048 | 7.58  | 9.11  | 0.83 |


### Package Versions

| Pip package name           | Version  |
|----------------------------|----------|
| torch                      | 2.2.0    |
| triton                     | 2.2.0    |
| onnxruntime-gpu            | 1.18.0   |
| onnxruntime-genai          | 0.2.0    |
| onnxruntime-genai-cuda     | 0.2.0    |
| onnxruntime-genai-directml | 0.2.0    |
| transformers               | 4.39.0   |
| bitsandbytes               | 0.42.0   |


## Appendix

### Activation Aware Quantization

AWQ works by identifying the top 1% most salient weights that are most important for maintaining accuracy and quantizing the remaining 99% of weights. This leads to less accuracy loss from quantization compared to many other quantization techniques. For more on AWQ, see [here](https://arxiv.org/abs/2306.00978).


## Model Card Contact
parinitarahi, kvaishnavi, natke

## Contributors
Kunal Vaishnavi, Sunghoon Choi, Yufeng Li, Akshay Sonawane, Sheetal Arun Kadam, Rui Ren, Edward Chen, Scott McKay, Ryan Hill, Emma Ning, Natalie Kershaw, Parinita Rahi, Patrice Vignola, Chai Chaoweeraprasit, Logan Iyer, Vicente Rivera, Jacques Van Rhyn