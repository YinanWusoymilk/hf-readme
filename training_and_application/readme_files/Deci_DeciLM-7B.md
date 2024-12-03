---
license: apache-2.0
language:
- en
---
# DeciLM-7B

DeciLM-7B is a 7.04 billion parameter decoder-only text generation model, released under the Apache 2.0 license. At the time of release, DeciLM-7B is the top-performing 7B base language model on the Open LLM Leaderboard. With support for an 8K-token sequence length, this highly efficient model uses variable Grouped-Query Attention (GQA) to achieve a superior balance between accuracy and computational efficiency. The model's architecture was generated using Deci's proprietary Neural Architecture Search technology, AutoNAC. 


## Model Details

### Model Description

Deci developed and released the DeciLM-7B language model, a pre-trained, high-efficiency text generation model with 7 billion parameters. DeciLM-7B is not only the most accurate 7B base model, but it also outpaces all models in its class with a throughput that is up to 4.4x that of Mistral-7B's. An instruct version [DeciLM-7B-instruct](https://huggingface.co/Deci/DeciLM-7B-instruct) has also been released.

- **Developed by:** [Deci](https://deci.ai/?utm_campaign=repos&utm_source=hugging-face&utm_medium=model-card&utm_content=decilm-7b)
- **Model type:** DeciLM is an auto-regressive language model using an optimized transformer decoder architecture that includes variable Grouped-Query Attention.
- **Language(s) (NLP):** English
- **License:** Apache 2.0

## Model Architecture

| Parameters | Layers | Heads  | Sequence Length  | GQA num_key_value_heads*  |
|:----------|:----------|:----------|:----------|:----------|
| 7.04 billion    | 32    | 32    | 8192   | Variable  |

*AutoNAC was employed to optimize the selection of the GQA num_key_value_heads for each layer.


### Model Sources

- **Blog:** [DeciLM-7B Technical Blog](https://deci.ai/blog/introducing-DeciLM-7B-the-fastest-and-most-accurate-7b-large-language-model-to-date/?utm_campaign=repos&utm_source=hugging-face&utm_medium=model-card&utm_content=decilm-7b)
- **Demo:** [DeciLM-7B-instruct Demo](https://huggingface.co/spaces/Deci/DeciLM-7B-instruct)
- **Finetuning Notebook:** [DeciLM-7B Finetuning Notebook](https://colab.research.google.com/drive/1kEV6i96AQ94xTCvSd11TxkEaksTb5o3U?usp=sharing)
- **Text Generation Notebook:** [DeciLM-7B-instruct Text Generation Notebook](https://bit.ly/declm-7b-instruct)

## Uses

The model is intended for commercial and research use in English and can be fine-tuned for various tasks and languages.

## How to Get Started with the Model

Use the code below to get started with the model.

```bibtex
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Deci/DeciLM-7B"
device = "cuda" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", trust_remote_code=True).to(device)

inputs = tokenizer.encode("In a shocking finding, scientists discovered a herd of unicorns living in", return_tensors="pt").to(device)
outputs = model.generate(inputs, max_new_tokens=100, do_sample=True, top_p=0.95)
print(tokenizer.decode(outputs[0]))

# The model can also be used via the text-generation pipeline interface
from transformers import pipeline
generator = pipeline("text-generation", "Deci/DeciLM-7B", torch_dtype="auto", trust_remote_code=True, device=device)
outputs = generator("In a shocking finding, scientists discovered a herd of unicorns living in", max_new_tokens=100, do_sample=True, top_p=0.95)
print(outputs[0]["generated_text"])
```

## Evaluation

Below are DeciLM-7B and DeciLM-7B-instruct's Open LLM Leaderboard results.

| Model | Average | ARC | HellaSwag | MMLU | TruthfulQA | Winogrande | GSM8K | 
|:----------|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
| DecilLM-7B | 61.55    | 59.39    | 82.51    | 59.76  | 40.33    | 79.95    | 47.38    | 
| DecilLM-7B-instruct | 63.19    | 61.01    | 82.37    | 60.24  | 49.75    | 79.72    | 46.02    | 

### Runtime Benchmarks

| Inference Tool | Hardware | Prompt length | Generation length | Generated tokens/sec | Batch Size | Number of Prompts |
|:----------|:----------|:---------:|:---------:|:---------:|:---------:|:---------:|
| HuggingFace (PyTorch) | A100 (SXM4-80GB-400W) | 512 | 512 | **1174** |  352 | 352 | 
| HuggingFace (PyTorch) | A100 (SXM4-80GB-400W) | 2048 | 2048 | **328** | 72 | 72 |
| Infery-LLM | A100 (SXM4-80GB-400W)| 512 | 512 | **4559**  | 1024 | 4096 |
| Infery-LLM | A100 (SXM4-80GB-400W) | 2048 | 2048 | **3997** | 512 | 2048 | 
| Infery-LLM | A10 | 512 | 512 | **1345** | 128 | 512 |  
| Infery-LLM | A10 | 2048 | 2048 | **599** | 32 | 128 | 

- In order to replicate the results of the Hugging Face benchmarks, you can use this [code example](https://huggingface.co/Deci/DeciLM-7B/blob/main/benchmark_hf_model.py).
- Infery-LLM, Deci's inference engine, features a suite of optimization algorithms, including selective quantization, optimized beam search, continuous batching, and custom CUDA kernels. To explore the capabilities of Infery-LLM, [schedule a live demo](https://deci.ai/infery-llm-book-a-demo/?utm_campaign=DeciLM%207B%20Launch&utm_source=HF&utm_medium=decilm7b-model-card&utm_term=infery-demo).

## Ethical Considerations and Limitations

DeciLM-7B is a new technology that comes with inherent risks associated with its use. The testing conducted so far has been primarily in English and does not encompass all possible scenarios. Like those of all large language models, DeciLM-7B's outputs are unpredictable, and the model may generate responses that are inaccurate, biased, or otherwise objectionable. Consequently, developers planning to use DeciLM-7B should undertake thorough safety testing and tuning designed explicitly for their intended applications of the model before deployment.

## How to Cite

Please cite this model using this format.

```bibtex
@misc{DeciFoundationModels,
title = {DeciLM-7B},
author = {DeciAI Research Team},
year = {2023}
url={https://huggingface.co/Deci/DeciLM-7B},
}
```