---
license: apache-2.0
tags:
- llava
pipeline_tag: image-text-to-text
---

# GGUF Quantized LLaVA 1.6 Mistral 7B

Updated quants and projector from [PR #5267](https://github.com/ggerganov/llama.cpp/pull/5267)

## Provided files
| Name | Quant method | Bits | Size | Use case |
| ---- | ---- | ---- | ---- | ----- |
| [llava-v1.6-mistral-7b.Q3_K_XS.gguf](https://huggingface.co/cjpais/llava-1.6-mistral-7b-gguf/blob/main/llava-v1.6-mistral-7b.Q3_K_XS.gguf) | Q3_K_XS | 3 | 2.99 GB| very small, high quality loss |
| [llava-v1.6-mistral-7b.Q3_K_M.gguf](https://huggingface.co/cjpais/llava-1.6-mistral-7b-gguf/blob/main/llava-v1.6-mistral-7b.Q3_K_M.gguf) | Q3_K_M | 3 | 3.52 GB| very small, high quality loss |
| [llava-v1.6-mistral-7b.Q4_K_M.gguf](https://huggingface.co/cjpais/llava-1.6-mistral-7b-gguf/blob/main/llava-v1.6-mistral-7b.Q4_K_M.gguf) | Q4_K_M | 4 | 4.37 GB| medium, balanced quality - recommended |
| [llava-v1.6-mistral-7b.Q5_K_S.gguf](https://huggingface.co/cjpais/llava-1.6-mistral-7b-gguf/blob/main/llava-v1.6-mistral-7b.Q5_K_S.gguf) | Q5_K_S | 5 | 5.00 GB| large, low quality loss - recommended |
| [llava-v1.6-mistral-7b.Q5_K_M.gguf](https://huggingface.co/cjpais/llava-1.6-mistral-7b-gguf/blob/main/llava-v1.6-mistral-7b.Q5_K_M.gguf) | Q5_K_M | 5 | 5.13 GB| large, very low quality loss - recommended |
| [llava-v1.6-mistral-7b.Q6_K.gguf](https://huggingface.co/cjpais/llava-1.6-mistral-7b-gguf/blob/main/llava-v1.6-mistral-7b.Q6_K.gguf) | Q6_K | 6 | 5.94 GB| very large, extremely low quality loss |
| [llava-v1.6-mistral-7b.Q8_0.gguf](https://huggingface.co/cjpais/llava-1.6-mistral-7b-gguf/blob/main/llava-v1.6-mistral-7b.Q8_0.gguf) | Q8_0 | 8 | 7.7 GB| very large, extremely low quality loss - not recommended |

<br>
<br>

# ORIGINAL LLaVA Model Card

## Model details

**Model type:**
LLaVA is an open-source chatbot trained by fine-tuning LLM on multimodal instruction-following data.
It is an auto-regressive language model, based on the transformer architecture.
Base LLM: [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)

**Model date:**
LLaVA-v1.6-Mistral-7B was trained in December 2023.

**Paper or resources for more information:**
https://llava-vl.github.io/

## License
[mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) license.

**Where to send questions or comments about the model:**
https://github.com/haotian-liu/LLaVA/issues

## Intended use
**Primary intended uses:**
The primary use of LLaVA is research on large multimodal models and chatbots.

**Primary intended users:**
The primary intended users of the model are researchers and hobbyists in computer vision, natural language processing, machine learning, and artificial intelligence.

## Training dataset
- 558K filtered image-text pairs from LAION/CC/SBU, captioned by BLIP.
- 158K GPT-generated multimodal instruction-following data.
- 500K academic-task-oriented VQA data mixture.
- 50K GPT-4V data mixture.
- 40K ShareGPT data.

## Evaluation dataset
A collection of 12 benchmarks, including 5 academic VQA benchmarks and 7 recent benchmarks specifically proposed for instruction-following LMMs.