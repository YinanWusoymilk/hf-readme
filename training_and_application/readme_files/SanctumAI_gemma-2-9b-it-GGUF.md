---
license: gemma
pipeline_tag: text-generation
tags:
- conversational
base_model:
- google/gemma-2-9b-it
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64a28db2f1968b7d7f357182/u7s05Lc_DIwrI3mY_Hzwn.png)
*This model was quantized by [SanctumAI](https://sanctum.ai). To leave feedback, join our community in [Discord](https://discord.gg/7ZNE78HJKh).*

# Gemma 2 9B IT GGUF

**Model creator:** [google](https://huggingface.co/google)<br>
**Original model**: [gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it)<br>

## Model Summary:

Gemma is a family of lightweight, state-of-the-art open models from Google, built from the same research and technology used to create the Gemini models. They are text-to-text, decoder-only large language models, available in English, with open weights for both pre-trained variants and instruction-tuned variants. Gemma models are well-suited for a variety of text generation tasks, including question answering, summarization, and reasoning. Their relatively small size makes it possible to deploy them in environments with limited resources such as a laptop, desktop or your own cloud infrastructure, democratizing access to state of the art AI models and helping foster innovation for everyone.

## Prompt Template:

If you're using Sanctum app, simply use `Gemma` model preset.

Prompt template:

```
<start_of_turn>user
{prompt}<end_of_turn>
<|start_of_turn|>model
```

## Hardware Requirements Estimate

| Name | Quant method | Size | Memory (RAM, vRAM) required |
| ---- | ---- | ---- | ---- |
| [gemma-2-9b-it.Q2_K.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q2_K.gguf) | Q2_K | 3.81 GB | 15.14 GB |
| [gemma-2-9b-it.Q3_K_S.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q3_K_S.gguf) | Q3_K_S | 4.34 GB | 15.64 GB |
| [gemma-2-9b-it.Q3_K_M.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q3_K_M.gguf) | Q3_K_M | 4.76 GB | 16.04 GB |
| [gemma-2-9b-it.Q3_K_L.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q3_K_L.gguf) | Q3_K_L | 5.13 GB | 16.38 GB |
| [gemma-2-9b-it.Q4_0.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q4_0.gguf) | Q4_0 | 5.44 GB | 16.67 GB |
| [gemma-2-9b-it.Q4_K_S.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q4_K_S.gguf) | Q4_K_S | 5.48 GB | 16.70 GB |
| [gemma-2-9b-it.Q4_K_M.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q4_K_M.gguf) | Q4_K_M | 5.76 GB | 16.97 GB |
| [gemma-2-9b-it.Q4_K.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q4_K.gguf) | Q4_K | 5.76 GB | 16.97 GB |
| [gemma-2-9b-it.Q4_1.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q4_1.gguf) | Q4_1 | 5.96 GB | 17.15 GB |
| [gemma-2-9b-it.Q5_0.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q5_0.gguf) | Q5_0 | 6.48 GB | 17.64 GB |
| [gemma-2-9b-it.Q5_K_S.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q5_K_S.gguf) | Q5_K_S | 6.48 GB | 17.64 GB |
| [gemma-2-9b-it.Q5_K_M.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q5_K_M.gguf) | Q5_K_M | 6.65 GB | 17.79 GB |
| [gemma-2-9b-it.Q5_K.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q5_K.gguf) | Q5_K | 6.65 GB | 17.79 GB |
| [gemma-2-9b-it.Q5_1.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q5_1.gguf) | Q5_1 | 7.00 GB | 18.12 GB |
| [gemma-2-9b-it.Q6_K.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q6_K.gguf) | Q6_K | 7.59 GB | 18.67 GB |
| [gemma-2-9b-it.Q8_0.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.Q8_0.gguf) | Q8_0 | 9.83 GB | 20.75 GB |
| [gemma-2-9b-it.f16.gguf](https://huggingface.co/SanctumAI/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it.f16.gguf) | f16 | 18.49 GB | 28.82 GB |

## Disclaimer

Sanctum is not the creator, originator, or owner of any Model featured in the Models section of the Sanctum application. Each Model is created and provided by third parties. Sanctum does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Model listed there. You understand that supported Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Model is the sole responsibility of the person or entity who originated such Model. Sanctum may not monitor or control the Models supported and cannot, and does not, take responsibility for any such Model. Sanctum disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Models. Sanctum further disclaims any warranty that the Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Models, your downloading of any Model, or use of any other Model provided by or through Sanctum.