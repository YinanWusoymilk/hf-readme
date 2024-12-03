---
base_model: google/t5-v1_1-xxl
library_name: gguf
license: apache-2.0
quantized_by: city96
language: en
---

This is a GGUF conversion of Google's T5 v1.1 XXL encoder model.

The weights can be used with [`./llama-embedding`](https://github.com/ggerganov/llama.cpp/tree/master/examples/embedding) or with the [ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF) custom node together with image generation models.

This is a **non imatrix** quant as llama.cpp doesn't support imatrix creation for T5 models at the time of writing. It's therefore recommended to use **Q5_K_M or larger** for the best results, although smaller models may also still provide decent results in resource constrained scenarios.
