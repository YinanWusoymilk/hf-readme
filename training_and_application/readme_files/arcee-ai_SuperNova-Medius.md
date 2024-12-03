---
base_model:
- Qwen/Qwen2.5-14B
library_name: transformers
tags:
- mergekit
- merge
license: apache-2.0
---

# Arcee-SuperNova-Medius

Arcee-SuperNova-Medius is a 14B parameter language model developed by Arcee.ai, built on the Qwen2.5-14B-Instruct architecture. This unique model is the result of a cross-architecture distillation pipeline, combining knowledge from both the Qwen2.5-72B-Instruct model and the Llama-3.1-405B-Instruct model. By leveraging the strengths of these two distinct architectures, SuperNova-Medius achieves high-quality instruction-following and complex reasoning capabilities in a mid-sized, resource-efficient form.

SuperNova-Medius is designed to excel in a variety of business use cases, including customer support, content creation, and technical assistance, while maintaining compatibility with smaller hardware configurations. It’s an ideal solution for organizations looking for advanced capabilities without the high resource requirements of larger models like our SuperNova-70B.

## Distillation Overview

The development of SuperNova-Medius involved a sophisticated multi-teacher, cross-architecture distillation process, with the following key steps:

1. **Logit Distillation from Llama 3.1 405B**:
   - We distilled the logits of Llama 3.1 405B using an offline approach.
   - The top K logits for each token were stored to capture most of the probability mass while managing storage requirements.

2. **Cross-Architecture Adaptation**:
   - Using `mergekit-tokensurgeon`, we created a version of Qwen2.5-14B that uses the vocabulary of Llama 3.1 405B.
   - This allowed for the use of Llama 3.1 405B logits in training the Qwen-based model.

3. **Distillation to Qwen Architecture**:
   - The adapted Qwen2.5-14B model was trained using the stored 405B logits as the target.

4. **Parallel Qwen Distillation**:
   - In a separate process, Qwen2-72B was distilled into a 14B model.

5. **Final Fusion and Fine-Tuning**:
   - The Llama-distilled Qwen model's vocabulary was reverted to Qwen vocabulary.
   - After re-aligning the vocabularies, a final fusion and fine-tuning step was conducted, using a specialized dataset from [EvolKit](https://github.com/arcee-ai/EvolKit) to ensure that SuperNova-Medius maintained coherence, fluency, and context understanding across a broad range of tasks.

## Performance Evaluation

Below are the benchmark results of SuperNova-Medius compared to similar models in its class:

| Model | Average | IFEval | BBH | GPQA | MMLU Pro | MuSR | Math Level 5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Mistral-Small 2409 | 0.423 | 0.628 | 0.581 | 0.333 | 0.410 | 0.406 | 0.181 |
| Supernova-Lite | 0.427 | 0.786 | 0.511 | 0.306 | 0.388 | 0.415 | 0.155 |
| Qwen2.5-14B-Instruct | 0.450 | 0.827 | 0.623 | 0.358 | 0.490 | 0.403 | 0.000 |
| Supernova-Medius | **0.480** | **0.832** | **0.631** | **0.359** | **0.502** | **0.402** | **0.152** |

SuperNova-Medius performs exceptionally well in instruction-following (IFEval) and complex reasoning tasks (BBH), demonstrating its capability to handle a variety of real-world scenarios. It outperforms Qwen2.5-14B and SuperNova-Lite in multiple benchmarks, making it a powerful yet efficient choice for high-quality generative AI applications.

## Model Use Cases

Arcee-SuperNova-Medius is suitable for a range of applications, including:

- **Customer Support**: With its robust instruction-following and dialogue management capabilities, SuperNova-Medius can handle complex customer interactions, reducing the need for human intervention.
- **Content Creation**: The model’s advanced language understanding and generation abilities make it ideal for creating high-quality, coherent content across diverse domains.
- **Technical Assistance**: SuperNova-Medius has a deep reservoir of technical knowledge, making it an excellent assistant for programming, technical documentation, and other expert-level content creation.

## Deployment Options

SuperNova-Medius is available for use under the Apache-2.0 license. For those who need even higher performance, the full-size 70B SuperNova model can be accessed via an Arcee-hosted API or for local deployment. To learn more or explore deployment options, please reach out to [sales@arcee.ai](mailto:sales@arcee.ai).

## Technical Specifications

- **Model Architecture**: Qwen2.5-14B-Instruct
- **Distillation Sources**: Qwen2.5-72B-Instruct, Llama-3.1-405B-Instruct
- **Parameter Count**: 14 billion
- **Training Dataset**: Custom instruction dataset generated with [EvolKit](https://github.com/arcee-ai/EvolKit)
- **Distillation Technique**: Multi-architecture offline logit distillation with cross-architecture vocabulary alignment.

## Summary

Arcee-SuperNova-Medius provides a unique balance of power, efficiency, and versatility. By distilling knowledge from two top-performing teacher models into a single 14B parameter model, SuperNova-Medius achieves results that rival larger models while maintaining a compact size ideal for practical deployment. Whether for customer support, content creation, or technical assistance, SuperNova-Medius is the perfect choice for organizations looking to leverage advanced language model capabilities in a cost-effective and accessible form.
