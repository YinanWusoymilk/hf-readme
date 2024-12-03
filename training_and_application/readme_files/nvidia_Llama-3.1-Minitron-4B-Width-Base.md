---
license: other
license_name: nvidia-open-model-license
license_link: >-
  https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf
---
# Llama-3.1-Minitron-4B-Width-Base

## Model Overview

Llama-3.1-Minitron-4B-Width-Base is a base text-to-text model that can be adopted for a variety of natural language generation tasks.
It is obtained by pruning Llama-3.1-8B; specifically, we prune model embedding size and MLP intermediate dimension.
Following pruning, we perform continued training with distillation using 94 billion tokens to arrive at the final model; we use the continuous pre-training data corpus used in Nemotron-4 15B for this purpose. Please refer to our [technical report](https://arxiv.org/abs/2408.11796) for more details.

This model is ready for commercial use.

**Model Developer:** NVIDIA 

**Model Dates:** Llama-3.1-Minitron-4B-Width-Base was trained between July 29, 2024 and Aug 3, 2024.

## License 

This model is released under the [NVIDIA Open Model License Agreement](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf).

## Model Architecture

Llama-3.1-Minitron-4B-Width-Base uses a model embedding size of 3072, 32 attention heads, MLP intermediate dimension of 9216, with 32 layers in total. Additionally, it uses Grouped-Query Attention (GQA) and Rotary Position Embeddings (RoPE). 

**Architecture Type:** Transformer Decoder (Auto-Regressive Language Model)

**Network Architecture:** Llama-3.1

**Input Type(s):** Text 

**Input Format(s):** String 

**Input Parameters:** None

**Other Properties Related to Input:** Works well within 8k characters or less. 
  
**Output Type(s):** Text

**Output Format:** String

**Output Parameters:** 1D

**Other Properties Related to Output:** None


## Usage
Support for this model will be added in the upcoming `transformers` release. In the meantime, please install the library from source:
```
pip install git+https://github.com/huggingface/transformers
```
We can now run inference on this model:

```python
import torch
from transformers import AutoTokenizer, LlamaForCausalLM

# Load the tokenizer and model
model_path = "nvidia/Llama-3.1-Minitron-4B-Width-Base"
tokenizer = AutoTokenizer.from_pretrained(model_path)

device = 'cuda'
dtype = torch.bfloat16
model = LlamaForCausalLM.from_pretrained(model_path, torch_dtype=dtype, device_map=device)

# Prepare the input text
prompt = 'Complete the paragraph: our solar system is'
inputs = tokenizer.encode(prompt, return_tensors='pt').to(model.device)

# Generate the output
outputs = model.generate(inputs, max_length=20)

# Decode and print the output
output_text = tokenizer.decode(outputs[0])
print(output_text)
```

## Software Integration
**Runtime Engine(s):**
* NeMo 24.05

**Supported Hardware Microarchitecture Compatibility:** <br>
* NVIDIA Ampere
* NVIDIA Blackwell
* NVIDIA Hopper
* NVIDIA Lovelace


**[Preferred/Supported] Operating System(s):** <br>
* Linux

## Dataset & Training

**Data Collection Method by Dataset:** Automated

**Labeling Method by Dataset:** Not Applicable

**Properties:**
The training corpus for Llama-3.1-Minitron-4B-Width-Base consists of English and multilingual text, as well as code. Our sources cover a variety of document types such as: webpages, dialogue, articles, and other written materials. The corpus spans domains including legal, math, science, finance, and more. In our continued training set, we introduce a small portion of question-answering, and alignment style data to improve model performance. 

**Data Freshness:** The pretraining data has a cutoff of June 2023. 

## Evaluation Results

### Overview
_5-shot performance._ Language Understanding evaluated using [Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300):

| Average |
| :---- |
| 60.5 | 

_Zero-shot performance._ Evaluated using select datasets from the [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) with additions:

| HellaSwag | Winogrande | GSM8K| ARC-Challenge | XLSum |
| :---- | :---- | :---- | :---- | :---- |
| 76.1 | 73.5 | 41.2 | 55.6 | 28.7 

_Code generation performance._ Evaluated using [MBPP](https://github.com/google-research/google-research/tree/master/mbpp):
 | Score |
 | :---- |
 | 32.0 | 

## Inference

**Engine:** TensorRT-LLM 

**Test Hardware:** NVIDIA A100 

**DType:** BFloat16


## Limitations

The model was trained on data that contains toxic language, unsafe content, and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. 

## Ethical Considerations 

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. 

Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/). 

## References

* [Compact Language Models via Pruning and Knowledge Distillation](https://arxiv.org/abs/2407.14679)
* [LLM Pruning and Distillation in Practice: The Minitron Approach](https://arxiv.org/abs/2408.11796)