---
base_model: liuhaotian/llava-v1.5-7b
inference: false
library_name: transformers
license: llama2
model_creator: liuhaotian
model_name: Llava v1.5 7B
quantized_by: Second State Inc.
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://github.com/LlamaEdge/LlamaEdge/raw/dev/assets/logo.svg" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Llava-v1.5-7B-GGUF

## Original Model

[liuhaotian/llava-v1.5-7b](https://huggingface.co/liuhaotian/llava-v1.5-7b)

## Run with LlamaEdge

- LlamaEdge version: comming soon

- Prompt template

  - Prompt type: `vicuna-llava`

  - Prompt string

    ```text
    <system_prompt>\nUSER:<image_embeddings>\n<textual_prompt>\nASSISTANT:
    ```

- Context size: `4096`

- Run as LlamaEdge service

  ```bash
  wasmedge --dir .:. \
    --nn-preload default:GGML:AUTO:llava-v1.5-7b-Q5_K_M.gguf \
    llama-api-server.wasm \
    --prompt-template vicuna-llava \
    --ctx-size 4096 \
    --llava-mmproj llava-v1.5-7b-mmproj-model-f16.gguf \
    --model-name llava-v1.5
  ```

## Quantized GGUF Models

| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [llava-v1.5-7b-Q2_K.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q2_K.gguf)     | Q2_K   | 2 | 2.53 GB| smallest, significant quality loss - not recommended for most purposes |
| [llava-v1.5-7b-Q3_K_L.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q3_K_L.gguf) | Q3_K_L | 3 | 3.6 GB| small, substantial quality loss |
| [llava-v1.5-7b-Q3_K_M.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q3_K_M.gguf) | Q3_K_M | 3 | 3.3 GB| very small, high quality loss |
| [llava-v1.5-7b-Q3_K_S.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q3_K_S.gguf) | Q3_K_S | 3 | 2.95 GB| very small, high quality loss |
| [llava-v1.5-7b-Q4_0.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q4_0.gguf)     | Q4_0   | 4 | 3.83 GB| legacy; small, very high quality loss - prefer using Q3_K_M |
| [llava-v1.5-7b-Q4_K_M.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q4_K_M.gguf) | Q4_K_M | 4 | 4.08 GB| medium, balanced quality - recommended |
| [llava-v1.5-7b-Q4_K_S.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q4_K_S.gguf) | Q4_K_S | 4 | 3.86 GB| small, greater quality loss |
| [llava-v1.5-7b-Q5_0.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q5_0.gguf)     | Q5_0   | 5 | 4.65 GB| legacy; medium, balanced quality - prefer using Q4_K_M |
| [llava-v1.5-7b-Q5_K_M.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q5_K_M.gguf) | Q5_K_M | 5 | 4.78 GB| large, very low quality loss - recommended |
| [llava-v1.5-7b-Q5_K_S.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q5_K_S.gguf) | Q5_K_S | 5 | 4.65 GB| large, low quality loss - recommended |
| [llava-v1.5-7b-Q6_K.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q6_K.gguf)     | Q6_K   | 6 | 5.53 GB| very large, extremely low quality loss |
| [llava-v1.5-7b-Q8_0.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-Q8_0.gguf)     | Q8_0   | 8 | 7.16 GB| very large, extremely low quality loss - not recommended |
| [llava-v1.5-7b-mmproj-model-f16.gguf](https://huggingface.co/second-state/Llava-v1.5-7B-GGUF/blob/main/llava-v1.5-7b-mmproj-model-f16.gguf)     | f16   | 8 | 624 MB|  |

*Quantized with llama.cpp b2230*
