---
library_name: transformers
pipeline_tag: text-generation
language:
  - en
tags:
  - nvidia
  - llama-3
  - pytorch
license: other
license_name: nvidia-open-model-license
license_link: >-
  https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf
---

# Llama-3_1-Nemotron-51B-instruct



## Model Overview
Llama-3_1-Nemotron-51B-instruct is a model which offers a great tradeoff between model accuracy and efficiency. Efficiency (throughput) directly translates to price, providing great ‘quality-per-dollar’. Using a novel Neural Architecture Search (NAS) approach we greatly reduce the model’s memory footprint, enabling larger workloads, as well as fitting the model on a single GPU at high workloads (H100-80GB). This NAS approach enables the selection of a desired point in the accuracy-efficiency tradeoff. This model is ready for commercial use.


## License
This model is released under the [NVIDIA Open Model License Agreement](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf).
Additional Information: [Llama 3.1 Community License Agreement](https://www.llama.com/llama3_1/license/). Built with Llama.

## How was the model developed

Llama-3_1-Nemotron-51B-instruct is a large language model (LLM) which is a derivative of Llama-3.1-70B-instruct (AKA the reference model). We utilize a block-wise distillation of the reference model, where for each block we create multiple variants providing different tradeoffs of quality vs. computational complexity. We then search over the blocks to create a model which meets the required throughput and memory (optimized for a single H100-80GB GPU) while minimizing the quality degradation. The model then undergoes knowledge distillation (KD), with a focus on English single and multi-turn chat use-cases.
The KD step included 40 billion tokens consisting of a mixture of 3 datasets - FineWeb, Buzz-V1.2 and Dolma.

Links to [NIM](https://build.nvidia.com/nvidia/llama-3_1-nemotron-51b-instruct), [blog](https://developer.nvidia.com/blog/advancing-the-accuracy-efficiency-frontier-with-llama-3-1-nemotron-51b/) and [huggingface](https://huggingface.co/nvidia/Llama-3_1-Nemotron-51B-Instruct)



This results in a final model that is aligned for human chat preferences.

**Model Developers:** NVIDIA

**Model Input:** Text only

**Model Output:** Text only

**Model Dates:** Llama-3_1-Nemotron-51B-instruct was trained between August and September 2024

**Data Freshness:** The pretraining data has a cutoff of 2023

**Sequence Length Used During Distillation:** 8192


## Quick Start
Our code requires the `transformers` package version to be 4.44.2 or higher

See the snippet below for usage with transformers:
```python
import torch
import transformers

model_id = "nvidia/Llama-3_1-Nemotron-51B-Instruct"
model_kwargs = {"torch_dtype": torch.bfloat16, "trust_remote_code": True, "device_map": "auto"}
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)
tokenizer.pad_token_id = tokenizer.eos_token_id

pipeline = transformers.pipeline(
    "text-generation", 
    model=model_id, 
    tokenizer=tokenizer, 
    max_new_tokens=20, 
    **model_kwargs
)
print(pipeline([{"role": "user", "content": "Hey how are you?"}]))
```



## Required Hardware

FP8 Inference (recommended):
- 1x H100-80GB GPU

BF16 Inference:
- 2x H100-80GB GPUs
- 2x A100-80GB GPUs


## Model Architecture
The model is a derivative of Llama-3.1-70B, using Neural Architecture Search (NAS). The NAS algorithm results in non-standard and non-repetitive blocks. This includes the following: 
* Variable Grouped Query Attention (VGQA) - each block can have a different number of KV (keys and values) heads, ranging from 1 to Llama’s typical 8.
* Skip attention - in some blocks the attention is skipped entirely, or replaced with a single linear layer.
* Variable FFN - the expansion/compression ratio in the FFN layer is different between blocks. 


**Architecture Type:** Transformer Decoder (auto-regressive language model)

## Software Integration
**Runtime Engine(s):** 
* NeMo 24.05 <br>


**Supported Hardware Architecture Compatibility:** NVIDIA H100, A100 80GB (BF16 quantization).

**[Preferred/Supported] Operating System(s):** <br>
* Linux <br>

## Intended use

Llama-3_1-Nemotron-51B-Instruct  is a general purpose chat model intended to be used in English and coding languages. Other non-English languages are also supported.

## Evaluation Results

**Data Collection Method by dataset** <br>
* Automated <br>


### MT-Bench

Evaluated using select datasets from the [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/pdf/2306.05685v4)
MT-bench - 8.99


### MMLU

Evaluated using the Multi-task Language Understanding benchmarks as introduced in [Measuring Massive Multitask Language Understanding](https://arxiv.org/pdf/2009.03300)

|MMLU (5-shot) |
| :----------------- |
| 80.2%  | 

### GSM8K

Evaluated using the Grade School Math 8K (GSM8K) benchmark as introduced in [Training Verifiers to Solve Math Word Problems](https://arxiv.org/pdf/2110.14168v2)

|GSM8K (5-shot) |
| :----------------- |
| 91.43%  | 

### Winogrande

|Winogrande (5-shot) |
| :----------------- |
| 84.53%  | 

### Arc-C

|Arc challenge (25-shot) |
| :----------------- |
| 69.20%  | 

### Hellaswag

|Hellaswag (10-shot) |
| :----------------- |
| 85.58%  | 

### Truthful QA

|TruthfulQA (0-shot) |
| :----------------- |
| 58.63%%  | 

## Limitations

The model was trained on data that contains toxic language, unsafe content, and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive.

The model demonstrates weakness to alignment-breaking attacks. Users are advised to deploy language model guardrails alongside this model to prevent potentially harmful outputs.

## Adversarial Testing and Red Teaming Efforts 

The Llama-3_1-Nemotron-51B-instruct model underwent extensive safety evaluation including adversarial testing via three distinct methods: 
* [Garak](https://docs.garak.ai/garak), is an automated LLM vulnerability scanner that probes for common weaknesses, including prompt injection and data leakage. 
* [AEGIS](https://arxiv.org/pdf/2404.05993), is a content safety evaluation dataset and LLM based content safety classifier model, that adheres to a broad taxonomy of 13 categories of critical risks in human-LLM interactions.
* Human Content Red Teaming leveraging human interaction and evaluation of the models' responses.


## Inference
**Engine:** Tensor(RT) <br>
**Test Hardware** H100-80GB <br>


## Ethical Considerations
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. 

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).