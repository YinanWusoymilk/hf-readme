---
language:
- en
datasets:
- Open-Orca/OpenOrca
- GAIR/lima
- WizardLM/WizardLM_evol_instruct_V2_196k
metrics:
- accuracy
pipeline_tag: text-generation
tags:
- finance
---

# Adapting LLMs to Domains via Continual Pre-Training (ICLR 2024)
This repo contains the domain-specific base model developed from **LLaMA-1-7B**, using the method in our paper [Adapting Large Language Models via Reading Comprehension](https://huggingface.co/papers/2309.09530).

We explore **continued pre-training on domain-specific corpora** for large language models. While this approach enriches LLMs with domain knowledge, it significantly hurts their prompting ability for question answering. Inspired by human learning via reading comprehension, we propose a simple method to **transform large-scale pre-training corpora into reading comprehension texts**, consistently improving prompting performance across tasks in biomedicine, finance, and law domains. **Our 7B model competes with much larger domain-specific models like BloombergGPT-50B**. 

### [2024/6/21] 🤗 We release the 2nd version of AdaptLLM at [Instruction-Pretrain](https://huggingface.co/instruction-pretrain), effective for both pre-training from scratch and continual pre-training 🤗

**************************** **Updates** ****************************
* 2024/8/29: Updated [guidelines](https://huggingface.co/datasets/AdaptLLM/finance-tasks) on evaluating any 🤗Huggingface models on the domain-specific tasks
* 2024/6/22: Released the [benchmarking code](https://github.com/microsoft/LMOps/tree/main/adaptllm)
* 2024/6/21: Released the 2nd version of AdaptLLM at [Instruction-Pretrain](https://huggingface.co/instruction-pretrain)
* 2024/4/2: Released the [raw data splits (train and test)](https://huggingface.co/datasets/AdaptLLM/ConvFinQA) of all the evaluation datasets
* 2024/1/16: Our [research paper](https://huggingface.co/papers/2309.09530) has been accepted by ICLR 2024
* 2023/12/19: Released our [13B base models](https://huggingface.co/AdaptLLM/law-LLM-13B) developed from LLaMA-1-13B
* 2023/12/8: Released our [chat models](https://huggingface.co/AdaptLLM/law-chat) developed from LLaMA-2-Chat-7B
* 2023/9/18: Released our [paper](https://huggingface.co/papers/2309.09530), [code](https://github.com/microsoft/LMOps), [data](https://huggingface.co/datasets/AdaptLLM/law-tasks), and [base models](https://huggingface.co/AdaptLLM/law-LLM) developed from LLaMA-1-7B


## 1. Domain-Specific Models
### LLaMA-1-7B
In our paper, we develop three domain-specific models from LLaMA-1-7B, which are also available in Huggingface: [Biomedicine-LLM](https://huggingface.co/AdaptLLM/medicine-LLM), [Finance-LLM](https://huggingface.co/AdaptLLM/finance-LLM) and [Law-LLM](https://huggingface.co/AdaptLLM/law-LLM), the performances of our AdaptLLM compared to other domain-specific LLMs are:

<p align='center'>
    <img src="https://cdn-uploads.huggingface.co/production/uploads/650801ced5578ef7e20b33d4/6efPwitFgy-pLTzvccdcP.png" width="700">
</p>

### LLaMA-1-13B
Moreover, we scale up our base model to LLaMA-1-13B to see if **our method is similarly effective for larger-scale models**, and the results are consistently positive too: [Biomedicine-LLM-13B](https://huggingface.co/AdaptLLM/medicine-LLM-13B), [Finance-LLM-13B](https://huggingface.co/AdaptLLM/finance-LLM-13B) and [Law-LLM-13B](https://huggingface.co/AdaptLLM/law-LLM-13B).

### LLaMA-2-Chat
Our method is also effective for aligned models! LLaMA-2-Chat requires a [specific data format](https://huggingface.co/blog/llama2#how-to-prompt-llama-2), and our **reading comprehension can perfectly fit the data format** by transforming the reading comprehension into a multi-turn conversation. We have also open-sourced chat models in different domains: [Biomedicine-Chat](https://huggingface.co/AdaptLLM/medicine-chat), [Finance-Chat](https://huggingface.co/AdaptLLM/finance-chat) and [Law-Chat](https://huggingface.co/AdaptLLM/law-chat).

For example, to chat with the finance base model (🤗we highly recommend switching to the [chat model](https://huggingface.co/AdaptLLM/finance-chat) for better response quality):
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("AdaptLLM/finance-LLM")
tokenizer = AutoTokenizer.from_pretrained("AdaptLLM/finance-LLM", use_fast=False)

# Put your input here:
user_input = '''Use this fact to answer the question: Title of each class Trading Symbol(s) Name of each exchange on which registered
Common Stock, Par Value $.01 Per Share MMM New York Stock Exchange
MMM Chicago Stock Exchange, Inc.
1.500% Notes due 2026 MMM26 New York Stock Exchange
1.750% Notes due 2030 MMM30 New York Stock Exchange
1.500% Notes due 2031 MMM31 New York Stock Exchange

Which debt securities are registered to trade on a national securities exchange under 3M's name as of Q2 of 2023?'''

# Simply use your input as the prompt for base models
prompt = user_input

inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).input_ids.to(model.device)
outputs = model.generate(input_ids=inputs, max_length=2048)[0]

answer_start = int(inputs.shape[-1])
pred = tokenizer.decode(outputs[answer_start:], skip_special_tokens=True)

print(pred)
```

### LLaMA-3-8B (💡New!)
In our recent research on [Instruction-Pretrain](https://huggingface.co/papers/2406.14491), we developed a context-based instruction synthesizer to augment the raw corpora with instruction-response pairs, **enabling Llama3-8B to be comparable to or even outperform Llama3-70B**: [Finance-Llama3-8B](https://huggingface.co/instruction-pretrain/finance-Llama3-8B), [Biomedicine-Llama3-8B](https://huggingface.co/instruction-pretrain/medicine-Llama3-8B).

## 2. Domain-Specific Tasks

### Pre-templatized Testing Splits
To easily reproduce our prompting results, we have uploaded the filled-in zero/few-shot input instructions and output completions of the test each domain-specific task: [biomedicine-tasks](https://huggingface.co/datasets/AdaptLLM/medicine-tasks), [finance-tasks](https://huggingface.co/datasets/AdaptLLM/finance-tasks), and [law-tasks](https://huggingface.co/datasets/AdaptLLM/law-tasks).

Note: those filled-in instructions are specifically tailored for models before alignment and do NOT fit for the specific data format required for chat models.

### Evaluating Any Huggingface LMs on Domain-Specific Tasks (💡New!)
You can use the following script to reproduce our results and evaluate any other Huggingface models on domain-specific tasks. Note that the script is NOT applicable to models that require specific prompt templates (e.g., Llama2-chat, Llama3-Instruct).

1). **Set Up Dependencies**
   ```bash
   git clone https://github.com/microsoft/LMOps
   cd LMOps/adaptllm
   pip install -r requirements.txt
   ```

2). **Evaluate the Model**
   ```bash
   # Select the domain from ['biomedicine', 'finance', 'law']
   DOMAIN='finance'
  
   # Specify any Huggingface model name (Not applicable to chat models)
   MODEL='AdaptLLM/finance-LLM'
  
   # Model parallelization:
   # - Set MODEL_PARALLEL=False if the model fits on a single GPU. 
   #   We observe that LMs smaller than 10B always meet this requirement.
   # - Set MODEL_PARALLEL=True if the model is too large and encounters OOM on a single GPU.
   MODEL_PARALLEL=False
  
   # Choose the number of GPUs from [1, 2, 4, 8]
   N_GPU=1
  
   # Whether to add a BOS token at the beginning of the prompt input:
   # - Set to False for AdaptLLM.
   # - Set to True for instruction-pretrain models.
   # If unsure, we recommend setting it to False, as this is suitable for most LMs.
   add_bos_token=False

   # Run the evaluation script
   bash scripts/inference.sh ${DOMAIN} ${MODEL} ${add_bos_token} ${MODEL_PARALLEL} ${N_GPU}
   ```

### Raw Datasets
We have also uploaded the raw training and testing splits, for facilitating fine-tuning or other usages: [ChemProt](https://huggingface.co/datasets/AdaptLLM/ChemProt), [RCT](https://huggingface.co/datasets/AdaptLLM/RCT), [ConvFinQA](https://huggingface.co/datasets/AdaptLLM/ConvFinQA), [FiQA_SA](https://huggingface.co/datasets/AdaptLLM/FiQA_SA), [Headline](https://huggingface.co/datasets/AdaptLLM/Headline), [NER](https://huggingface.co/datasets/AdaptLLM/NER), [FPB](https://huggingface.co/datasets/AdaptLLM/FPB)

### Domain Knowledge Probing
Our pre-processed knowledge probing datasets are available at: [med_knowledge_prob](https://huggingface.co/datasets/AdaptLLM/med_knowledge_prob) and [law_knowledge_prob](https://huggingface.co/datasets/AdaptLLM/law_knowledge_prob)

## Citation
If you find our work helpful, please cite us:
```bibtex
@inproceedings{
cheng2024adapting,
title={Adapting Large Language Models via Reading Comprehension},
author={Daixuan Cheng and Shaohan Huang and Furu Wei},
booktitle={The Twelfth International Conference on Learning Representations},
year={2024},
url={https://openreview.net/forum?id=y886UXPEZ0}
}
```