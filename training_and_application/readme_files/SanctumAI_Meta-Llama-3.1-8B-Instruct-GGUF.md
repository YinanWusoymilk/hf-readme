---
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
pipeline_tag: text-generation
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
license: llama3.1
license_name: llama3
license_link: LICENSE
base_model:
- meta-llama/Meta-Llama-3.1-8B-Instruct
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64a28db2f1968b7d7f357182/vsZwOOUWI-NK6sFuJls40.png)
*This model was quantized by [SanctumAI](https://sanctum.ai). To leave feedback, join our community in [Discord](https://discord.gg/7ZNE78HJKh).*

# Meta Llama 3 8B Instruct GGUF

**Model creator:** [meta-llama](https://huggingface.co/meta-llama)<br>
**Original model**: [Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)<br>

## Model Summary:

The Meta Llama 3.1 collection of multilingual large language models (LLMs) is a collection of pretrained and instruction tuned generative models in 8B, 70B and 405B sizes (text in/text out). The Llama 3.1 instruction tuned text only models (8B, 70B, 405B) are optimized for multilingual dialogue use cases and outperform many of the available open source and closed chat models on common industry benchmarks.

## Prompt Template:

If you're using Sanctum app, simply use `Llama 3` model preset.

Prompt template:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

```

## Hardware Requirements Estimate

| Name | Quant method | Size | Memory (RAM, vRAM) required |
| ---- | ---- | ---- | ---- |
| [meta-llama-3.1-8b-instruct.Q2_K.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q2_K.gguf) | Q2_K | 3.18 GB | 7.20 GB |
| [meta-llama-3.1-8b-instruct.Q3_K_S.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q3_K_S.gguf) | Q3_K_S | 3.67 GB | 7.65 GB |
| [meta-llama-3.1-8b-instruct.Q3_K_M.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q3_K_M.gguf) | Q3_K_M | 4.02 GB | 7.98 GB |
| [meta-llama-3.1-8b-instruct.Q3_K_L.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q3_K_L.gguf) | Q3_K_L | 4.32 GB | 8.27 GB |
| [meta-llama-3.1-8b-instruct.Q4_0.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q4_0.gguf) | Q4_0 | 4.66 GB | 8.58 GB |
| [meta-llama-3.1-8b-instruct.Q4_K_S.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q4_K_S.gguf) | Q4_K_S | 4.69 GB | 8.61 GB |
| [meta-llama-3.1-8b-instruct.Q4_K_M.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q4_K_M.gguf) | Q4_K_M | 4.92 GB | 8.82 GB |
| [meta-llama-3.1-8b-instruct.Q4_K.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q4_K.gguf) | Q4_K | 4.92 GB | 8.82 GB |
| [meta-llama-3.1-8b-instruct.Q4_1.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q4_1.gguf) | Q4_1 | 5.13 GB | 9.02 GB |
| [meta-llama-3.1-8b-instruct.Q5_0.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q5_0.gguf) | Q5_0 | 5.60 GB | 9.46 GB |
| [meta-llama-3.1-8b-instruct.Q5_K_S.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q5_K_S.gguf) | Q5_K_S | 5.60 GB | 9.46 GB |
| [meta-llama-3.1-8b-instruct.Q5_K_M.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q5_K_M.gguf) | Q5_K_M | 5.73 GB | 9.58 GB |
| [meta-llama-3.1-8b-instruct.Q5_K.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q5_K.gguf) | Q5_K | 5.73 GB | 9.58 GB |
| [meta-llama-3.1-8b-instruct.Q5_1.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q5_1.gguf) | Q5_1 | 6.07 GB | 9.89 GB |
| [meta-llama-3.1-8b-instruct.Q6_K.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q6_K.gguf) | Q6_K | 6.60 GB | 10.38 GB |
| [meta-llama-3.1-8b-instruct.Q8_0.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.Q8_0.gguf) | Q8_0 | 8.54 GB | 12.19 GB |
| [meta-llama-3.1-8b-instruct.f16.gguf](https://huggingface.co/SanctumAI/Meta-Llama-3.1-8B-Instruct-GGUF/blob/main/meta-llama-3.1-8b-instruct.f16.gguf) | f16 | 16.07 GB | 19.21 GB |

## Disclaimer

Sanctum is not the creator, originator, or owner of any Model featured in the Models section of the Sanctum application. Each Model is created and provided by third parties. Sanctum does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Model listed there. You understand that supported Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Model is the sole responsibility of the person or entity who originated such Model. Sanctum may not monitor or control the Models supported and cannot, and does not, take responsibility for any such Model. Sanctum disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Models. Sanctum further disclaims any warranty that the Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Models, your downloading of any Model, or use of any other Model provided by or through Sanctum.