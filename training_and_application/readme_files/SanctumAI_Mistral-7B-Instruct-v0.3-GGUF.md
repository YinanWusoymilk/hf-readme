---
pipeline_tag: text-generation
license: apache-2.0
base_model:
- mistralai/Mistral-7B-Instruct-v0.3
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64a28db2f1968b7d7f357182/9aQRkm59XY_qSEXe86IJb.png)
*This model was quantized by [SanctumAI](https://sanctum.ai). To leave feedback, join our community in [Discord](https://discord.gg/7ZNE78HJKh).*

# Mistral 7B Instruct v0.3 GGUF

**Model creator:** [mistralai](https://huggingface.co/mistralai)<br>
**Original model**: [Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)<br>

## Model Summary:

The Mistral-7B-Instruct-v0.3 Large Language Model (LLM) is an instruct fine-tuned version of the Mistral-7B-v0.3.

Mistral-7B-v0.3 has the following changes compared to [Mistral-7B-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2/edit/main/README.md)
- Extended vocabulary to 32768
- Supports v3 Tokenizer
- Supports function calling

## Prompt Template:

If you're using Sanctum app, simply use `Mistral` model preset.

Prompt template:

```
<s>[INST] {prompt} [/INST]
```

## Hardware Requirements Estimate

| Name | Quant method | Size | Memory (RAM, vRAM) required (for full context of 32k tokens) |
| ---- | ---- | ---- | ---- |
| [mistral-7b-instruct-v0.3.Q2_K.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q2_K.gguf) | Q2_K | 2.72 GB | 6.78 GB |
| [mistral-7b-instruct-v0.3.Q3_K_S.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q3_K_S.gguf) | Q3_K_S | 3.17 GB | 7.19 GB |
| [mistral-7b-instruct-v0.3.Q3_K_M.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q3_K_M.gguf) | Q3_K_M | 3.52 GB | 7.52 GB |
| [mistral-7b-instruct-v0.3.Q3_K_L.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q3_K_L.gguf) | Q3_K_L | 3.83 GB | 7.80 GB |
| [mistral-7b-instruct-v0.3.Q4_0.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q4_0.gguf) | Q4_0 | 4.11 GB | 8.07 GB |
| [mistral-7b-instruct-v0.3.Q4_K_S.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q4_K_S.gguf) | Q4_K_S | 4.14 GB | 8.10 GB |
| [mistral-7b-instruct-v0.3.Q4_K_M.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q4_K_M.gguf) | Q4_K_M | 4.37 GB | 8.31 GB |
| [mistral-7b-instruct-v0.3.Q4_K.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q4_K.gguf) | Q4_K | 4.37 GB | 8.31 GB |
| [mistral-7b-instruct-v0.3.Q4_1.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q4_1.gguf) | Q4_1 | 4.56 GB | 8.48 GB |
| [mistral-7b-instruct-v0.3.Q5_0.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q5_0.gguf) | Q5_0 | 5.00 GB | 8.90 GB |
| [mistral-7b-instruct-v0.3.Q5_K_S.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q5_K_S.gguf) | Q5_K_S | 5.00 GB | 8.90 GB |
| [mistral-7b-instruct-v0.3.Q5_K_M.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q5_K_M.gguf) | Q5_K_M | 5.14 GB | 9.02 GB |
| [mistral-7b-instruct-v0.3.Q5_K.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q5_K.gguf) | Q5_K | 5.14 GB | 9.02 GB |
| [mistral-7b-instruct-v0.3.Q5_1.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q5_1.gguf) | Q5_1 | 5.45 GB | 9.31 GB |
| [mistral-7b-instruct-v0.3.Q6_K.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q6_K.gguf) | Q6_K | 5.95 GB | 9.78 GB |
| [mistral-7b-instruct-v0.3.Q8_0.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.Q8_0.gguf) | Q8_0 | 7.70 GB | 11.41 GB |
| [mistral-7b-instruct-v0.3.f16.gguf](https://huggingface.co/SanctumAI/Mistral-7B-Instruct-v0.3-GGUF/blob/main/mistral-7b-instruct-v0.3.f16.gguf) | f16 | 14.50 GB | 17.74 GB |

## Disclaimer

Sanctum is not the creator, originator, or owner of any Model featured in the Models section of the Sanctum application. Each Model is created and provided by third parties. Sanctum does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Model listed there. You understand that supported Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Model is the sole responsibility of the person or entity who originated such Model. Sanctum may not monitor or control the Models supported and cannot, and does not, take responsibility for any such Model. Sanctum disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Models. Sanctum further disclaims any warranty that the Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Models, your downloading of any Model, or use of any other Model provided by or through Sanctum.