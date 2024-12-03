---
license: other
license_name: nvidia-open-model-license
license_link: >-
  https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf
---

# Model Overview

Minitron-4B-Base is a large language model (LLM) obtained by pruning Nemotron-4 15B; specifically, we prune model embedding size, number of attention heads, and MLP intermediate dimension. Following pruning, we perform continued training with distillation using 94 billion tokens to arrive at the final model; we use the continuous pre-training data corpus used in Nemotron-4 15B for this purpose.

Deriving the Minitron 8B and 4B models from the base 15B model using our approach requires up to **40x fewer training tokens** per model compared to training from scratch; this results in **compute cost savings of 1.8x** for training the full model family (15B, 8B, and 4B). Minitron models exhibit up to a 16% improvement in MMLU scores compared to training from scratch, perform comparably to other community models such as Mistral 7B, Gemma 7B and Llama-3 8B, and outperform state-of-the-art compression techniques from the literature. Please refer to our [arXiv paper](https://arxiv.org/abs/2407.14679) for more details.

This model is for research and development only.

**Model Developer:** NVIDIA 

**Model Dates:** Minitron-4B-Base was trained between February 2024 and June 2024.

## License

Minitron-4B-Base is released under the [NVIDIA Open Model License Agreement](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf).

## Model Architecture

Minitron-4B-Base uses a model embedding size of 3072, 32 attention heads, and an MLP intermediate dimension of 9216.
It also uses Grouped-Query Attention (GQA) and Rotary Position Embeddings (RoPE). 

**Architecture Type:** Transformer Decoder (auto-regressive language model) 

**Network Architecture:** Nemotron-4 

**Input Type:** Text

**Input Format:** String

**Input Parameters:** None

**Other Properties Related to Input:** None

**Output Type:** Text

**Output Format:** String

**Output Parameters:** None

**Other Properties Related to Output:** None

## Usage

Support for Nemotron models will be added in the upcoming transformers library release. In the meantime, please install the library from source:

```
pip install git+https://github.com/huggingface/transformers
```

The following code provides an example of how to load the Minitron-4B-Base model and use it to perform text generation.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
model_path = 'nvidia/Minitron-4B-Base'
tokenizer  = AutoTokenizer.from_pretrained(model_path)

device = 'cuda'
dtype  = torch.bfloat16
model  = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=dtype, device_map=device)

# Prepare the input text
prompt = 'Complete the paragraph: our solar system is'
inputs = tokenizer.encode(prompt, return_tensors='pt').to(model.device)

# Generate the output
outputs = model.generate(inputs, max_length=20)

# Decode and print the output
output_text = tokenizer.decode(outputs[0])
print(output_text)
```

## Dataset & Training

**Data Collection Method:** Hybrid

**Labeling Method:** Not Applicable

**Properties:** The training corpus for Minitron-4B-Base consists of English and multilingual text, as well as code. Our sources cover a variety of document types such as: webpages, dialogue, articles, and other written materials. The corpus spans domains including legal, math, science, finance, and more. In our continued training set, we introduce a small portion of question-answering, and alignment style data to improve model performance. 

**Data Freshness:** The pretraining data has a cutoff of June 2023. 

## Evaluation Results

*5-shot performance.* Language Understanding evaluated using [Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300):

| Average |
| :---- |
| 58.6 |

*Zero-shot performance.* Evaluated using select datasets from the [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) with additions:

| HellaSwag | Winogrande | GSM8K| ARC-C | XLSum |
| :------------- | :------------- | :------------- | :------------- | :------------- |
| 75.0 | 74.0 | 24.1  | 50.9 | 29.5


*Code generation performance*. Evaluated using [HumanEval](https://github.com/openai/human-eval):

| p@1, 0-Shot |
| :------------- |
| 23.3 |

Please refer to our [paper](https://arxiv.org/abs/2407.14679) for the full set of results.

## Inference
**Engine:** TensorRT-LLM

**Test Hardware:** NVIDIA A100

**DType:** Float16/BFloat16

## Limitations 

The model was trained on data that contains toxic language, unsafe content, and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. 

## Ethical Considerations 

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/). 


## Citation

If you find our work helpful, please consider citing our paper:
```
@article{minitron2024,
      title={Compact Language Models via Pruning and Knowledge Distillation}, 
      author={Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
      journal={arXiv preprint arXiv:2407.14679},
      year={2024},
      url={https://arxiv.org/abs/2407.14679}, 
}
```
