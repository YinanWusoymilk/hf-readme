---
license: other
license_name: mnpl
license_link: https://mistral.ai/licenses/MNPL-0.1.md
tags:
- code
language:
- code
base_model:
- mistralai/Codestral-22B-v0.1
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64a28db2f1968b7d7f357182/TczKSvq0edf6fV4TdbJ5s.png)
*This model was quantized by [SanctumAI](https://sanctum.ai). To leave feedback, join our community in [Discord](https://discord.gg/7ZNE78HJKh).*

# Codestral 22B v0.1 GGUF

**Model creator:** [mistralai](https://huggingface.co/mistralai)<br>
**Original model**: [Codestral-22B-v0.1](https://huggingface.co/mistralai/Codestral-22B-v0.1)<br>

## Model Summary:

Codestrall-22B-v0.1 is trained on a diverse dataset of 80+ programming languages, including the most popular ones, such as Python, Java, C, C++, JavaScript, and Bash (more details in the [Blogpost](https://mistral.ai/news/codestral/)). The model can be queried:

As instruct, for instance to answer any questions about a code snippet (write documentation, explain, factorize) or to generate code following specific indications
As Fill in the Middle (FIM), to predict the middle tokens between a prefix and a suffix (very useful for software development add-ons like in VS Code)

## Prompt Template:

If you're using Sanctum app, simply use `Mistral` model preset.

Prompt template:

```
<s>[INST] {prompt} [/INST]
```

## Hardware Requirements Estimate

| Name | Quant method | Size | Memory (RAM, vRAM) required (for full context of 32k tokens) |
| ---- | ---- | ---- | ---- |
| [codestral-22b-v0.1.Q2_K.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q2_K.gguf) | Q2_K | 8.27 GB | 16.02 GB |
| [codestral-22b-v0.1.Q3_K_S.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q3_K_S.gguf) | Q3_K_S | 9.64 GB | ? |
| [codestral-22b-v0.1.Q3_K_M.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q3_K_M.gguf) | Q3_K_M | 10.76 GB | ? |
| [codestral-22b-v0.1.Q3_K_L.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q3_K_L.gguf) | Q3_K_L | 11.73 GB | ? |
| [codestral-22b-v0.1.Q4_0.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q4_0.gguf) | Q4_0 | 12.57 GB | ? |
| [codestral-22b-v0.1.Q4_K_S.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q4_K_S.gguf) | Q4_K_S | 12.66 GB | ? |
| [codestral-22b-v0.1.Q4_K_M.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q4_K_M.gguf) | Q4_K_M | 13.34 GB | ? |
| [codestral-22b-v0.1.Q4_K.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q4_K.gguf) | Q4_K | 13.34 GB | ? |
| [codestral-22b-v0.1.Q4_1.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q4_1.gguf) | Q4_1 | 13.95 GB | ? |
| [codestral-22b-v0.1.Q5_0.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q5_0.gguf) | Q5_0 | 15.32 GB | ? |
| [codestral-22b-v0.1.Q5_K_S.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q5_K_S.gguf) | Q5_K_S | 15.32 GB | ? |
| [codestral-22b-v0.1.Q5_K_M.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q5_K_M.gguf) | Q5_K_M | 15.72 GB | ? |
| [codestral-22b-v0.1.Q5_K.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q5_K.gguf) | Q5_K | 15.72 GB | ? |
| [codestral-22b-v0.1.Q5_1.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q5_1.gguf) | Q5_1 | 16.7 GB | ? |
| [codestral-22b-v0.1.Q6_K.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q6_K.gguf) | Q6_K | 18.25 GB | ? |
| [codestral-22b-v0.1.Q8_0.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.Q8_0.gguf) | Q8_0 | 23.64 GB | ? |
| [codestral-22b-v0.1.f16.gguf](https://huggingface.co/SanctumAI/Codestral-22B-v0.1-GGUF/blob/main/codestral-22b-v0.1.f16.gguf) | f16 | 44.5 GB | 49.76 GB |

## Disclaimer

Sanctum is not the creator, originator, or owner of any Model featured in the Models section of the Sanctum application. Each Model is created and provided by third parties. Sanctum does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Model listed there. You understand that supported Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Model is the sole responsibility of the person or entity who originated such Model. Sanctum may not monitor or control the Models supported and cannot, and does not, take responsibility for any such Model. Sanctum disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Models. Sanctum further disclaims any warranty that the Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Models, your downloading of any Model, or use of any other Model provided by or through Sanctum.