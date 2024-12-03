---
pipeline_tag: text-generation
base_model: ibm-granite/granite-8b-code-base
inference: false
license: apache-2.0
datasets:
- bigcode/commitpackft
- TIGER-Lab/MathInstruct
- meta-math/MetaMathQA
- glaiveai/glaive-code-assistant-v3
- glaive-function-calling-v2
- bugdaryan/sql-create-context-instruction
- garage-bAInd/Open-Platypus
- nvidia/HelpSteer
metrics:
- code_eval
library_name: transformers
tags:
- code
- granite
model-index:
- name: granite-8b-code-instruct
  results:
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack 
        name: HumanEvalSynthesis(Python)
    metrics:
    - name: pass@1
      type: pass@1
      value: 57.9
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name: HumanEvalSynthesis(JavaScript)
    metrics:
    - name: pass@1
      type: pass@1
      value: 52.4
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name: HumanEvalSynthesis(Java)
    metrics:
    - name: pass@1
      type: pass@1
      value: 58.5
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name: HumanEvalSynthesis(Go)
    metrics:
    - name: pass@1
      type: pass@1
      value: 43.3
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name: HumanEvalSynthesis(C++)
    metrics:
    - name: pass@1
      type: pass@1
      value: 48.2
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name: HumanEvalSynthesis(Rust)
    metrics:
    - name: pass@1
      type: pass@1
      value: 37.2
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalExplain(Python)
    metrics:
    - name: pass@1
      type: pass@1
      value: 53.0
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalExplain(JavaScript)
    metrics:
    - name: pass@1
      type: pass@1
      value: 42.7
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalExplain(Java)
    metrics:
    - name: pass@1
      type: pass@1
      value: 52.4
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalExplain(Go)
    metrics:
    - name: pass@1
      type: pass@1
      value: 36.6
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalExplain(C++)
    metrics:
    - name: pass@1
      type: pass@1
      value: 43.9
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalExplain(Rust)
    metrics:
    - name: pass@1
      type: pass@1
      value: 16.5
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(Python)
    metrics:
    - name: pass@1
      type: pass@1
      value: 39.6
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(JavaScript)
    metrics:
    - name: pass@1
      type: pass@1
      value: 40.9
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(Java)
    metrics:
    - name: pass@1
      type: pass@1
      value: 48.2
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(Go)
    metrics:
    - name: pass@1
      type: pass@1
      value: 41.5
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(C++)
    metrics:
    - name: pass@1
      type: pass@1
      value: 39.0 
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(Rust)
    metrics:
    - name: pass@1
      type: pass@1
      value: 32.9
      veriefied: false
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64a28db2f1968b7d7f357182/rOiYpb6GH0VhWZRmwcOCP.png)
*This model was quantized by [SanctumAI](https://sanctum.ai). To leave feedback, join our community in [Discord](https://discord.gg/7ZNE78HJKh).*

# Granite 8B Code Instruct GGUF

**Model creator:** [ibm-granite](https://huggingface.co/ibm-granite)<br>
**Original model**: [granite-8b-code-instruct](https://huggingface.co/ibm-granite/granite-8b-code-instruct)<br>

## Model Summary:

**Granite-8B-Code-Instruct** is a 8B parameter model fine tuned from *Granite-8B-Code-Base* on a combination of **permissively licensed** instruction data to enhance instruction following capabilities including logical reasoning and problem-solving skills.

- **Developers:** IBM Research
- **GitHub Repository:** [ibm-granite/granite-code-models](https://github.com/ibm-granite/granite-code-models)
- **Paper:** [Granite Code Models: A Family of Open Foundation Models for Code Intelligence](https://arxiv.org/abs/2405.04324)
- **Release Date**: May 6th, 2024
- **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Prompt Template:

If you're using Sanctum app, simply use `IBM Granite Code` model preset.

Prompt template:

```
System:
{system_prompt}
Question:
{prompt}
Answer:

```

## Hardware Requirements Estimate

| Name | Quant method | Size | Memory (RAM, vRAM) required |
| ---- | ---- | ---- | ---- |
| [granite-8b-code-instruct.Q2_K.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q2_K.gguf) | Q2_K | 3.06 GB | 7.47 GB |
| [granite-8b-code-instruct.Q3_K_S.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q3_K_S.gguf) | Q3_K_S | 3.55 GB | ? |
| [granite-8b-code-instruct.Q3_K_M.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q3_K_M.gguf) | Q3_K_M | 3.94 GB | ? |
| [granite-8b-code-instruct.Q3_K_L.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q3_K_L.gguf) | Q3_K_L | 4.29 GB | ? |
| [granite-8b-code-instruct.Q4_0.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q4_0.gguf) | Q4_0 | 4.59 GB | ? |
| [granite-8b-code-instruct.Q4_K_S.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q4_K_S.gguf) | Q4_K_S | 4.62 GB | ? |
| [granite-8b-code-instruct.Q4_K_M.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q4_K_M.gguf) | Q4_K_M | 4.88 GB | ? |
| [granite-8b-code-instruct.Q4_K.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q4_K.gguf) | Q4_K | 4.88 GB | ? |
| [granite-8b-code-instruct.Q4_1.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q4_1.gguf) | Q4_1 | 5.08 GB | ? |
| [granite-8b-code-instruct.Q5_0.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q5_0.gguf) | Q5_0 | 5.57 GB | ? |
| [granite-8b-code-instruct.Q5_K_S.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q5_K_S.gguf) | Q5_K_S | 5.57 GB | ? |
| [granite-8b-code-instruct.Q5_K_M.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q5_K_M.gguf) | Q5_K_M | 5.72 GB | ? |
| [granite-8b-code-instruct.Q5_K.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q5_K.gguf) | Q5_K | 5.72 GB | ? |
| [granite-8b-code-instruct.Q5_1.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q5_1.gguf) | Q5_1 | 6.06 GB | ? |
| [granite-8b-code-instruct.Q6_K.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q6_K.gguf) | Q6_K | 6.62 GB | ? |
| [granite-8b-code-instruct.Q8_0.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.Q8_0.gguf) | Q8_0 | 8.57 GB | ? |
| [granite-8b-code-instruct.f16.gguf](https://huggingface.co/SanctumAI/granite-8b-code-instruct-GGUF/blob/main/granite-8b-code-instruct.f16.gguf) | f16 | 16.12 GB | 19.62 GB |

## Disclaimer

Sanctum is not the creator, originator, or owner of any Model featured in the Models section of the Sanctum application. Each Model is created and provided by third parties. Sanctum does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Model listed there. You understand that supported Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Model is the sole responsibility of the person or entity who originated such Model. Sanctum may not monitor or control the Models supported and cannot, and does not, take responsibility for any such Model. Sanctum disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Models. Sanctum further disclaims any warranty that the Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Models, your downloading of any Model, or use of any other Model provided by or through Sanctum.