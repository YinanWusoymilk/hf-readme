---
pipeline_tag: text-generation
base_model: ibm-granite/granite-34b-code-base-8k
inference: true
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
- name: granite-34b-code-instruct-8k
  results:
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack 
        name: HumanEvalSynthesis(Python)
    metrics:
    - name: pass@1
      type: pass@1
      value: 62.2
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name: HumanEvalSynthesis(JavaScript)
    metrics:
    - name: pass@1
      type: pass@1
      value: 56.7
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name: HumanEvalSynthesis(Java)
    metrics:
    - name: pass@1
      type: pass@1
      value: 62.8
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name: HumanEvalSynthesis(Go)
    metrics:
    - name: pass@1
      type: pass@1
      value: 47.6
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name: HumanEvalSynthesis(C++)
    metrics:
    - name: pass@1
      type: pass@1
      value: 57.9
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name: HumanEvalSynthesis(Rust)
    metrics:
    - name: pass@1
      type: pass@1
      value: 41.5
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
      value: 45.1
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalExplain(Java)
    metrics:
    - name: pass@1
      type: pass@1
      value: 50.6
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalExplain(Go)
    metrics:
    - name: pass@1
      type: pass@1
      value: 36.0
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalExplain(C++)
    metrics:
    - name: pass@1
      type: pass@1
      value: 42.7
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalExplain(Rust)
    metrics:
    - name: pass@1
      type: pass@1
      value: 23.8
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(Python)
    metrics:
    - name: pass@1
      type: pass@1
      value: 54.9
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(JavaScript)
    metrics:
    - name: pass@1
      type: pass@1
      value: 47.6
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(Java)
    metrics:
    - name: pass@1
      type: pass@1
      value: 55.5
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(Go)
    metrics:
    - name: pass@1
      type: pass@1
      value: 51.2
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(C++)
    metrics:
    - name: pass@1
      type: pass@1
      value: 47.0
      veriefied: false
  - task:
      type: text-generation
    dataset:
        type: bigcode/humanevalpack  
        name:  HumanEvalFix(Rust)
    metrics:
    - name: pass@1
      type: pass@1
      value: 45.1
      veriefied: false
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/62cd5057674cdb524450093d/1hzxoPwqkBJXshKVVe6_9.png)

# Granite-34B-Code-Instruct-8K

## Model Summary
**Granite-34B-Code-Instruct-8K** is a 34B parameter model fine tuned from *Granite-34B-Code-Base* on a combination of **permissively licensed** instruction data to enhance instruction following capabilities including logical reasoning and problem-solving skills.

- **Developers:** IBM Research
- **GitHub Repository:** [ibm-granite/granite-code-models](https://github.com/ibm-granite/granite-code-models)
- **Paper:** [Granite Code Models: A Family of Open Foundation Models for Code Intelligence](https://arxiv.org/abs/2405.04324)
- **Release Date**: May 6th, 2024
- **License:** [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Usage
### Intended use
The model is designed to respond to coding related instructions and can be used to build coding assistants.

<!-- TO DO: Check starcoder2 instruct code example that includes the template https://huggingface.co/bigcode/starcoder2-15b-instruct-v0.1 -->

### Generation
This is a simple example of how to use **Granite-34B-Code-Instruct-8K** model.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda" # or "cpu"
model_path = "ibm-granite/granite-34b-code-instruct-8k"
tokenizer = AutoTokenizer.from_pretrained(model_path)
# drop device_map if running on CPU
model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device)
model.eval()
# change input text as desired
chat = [
    { "role": "user", "content": "Write a code to find the maximum value in a list of numbers." },
]
chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
# tokenize the text
input_tokens = tokenizer(chat, return_tensors="pt")
# transfer tokenized inputs to the device
for i in input_tokens:
    input_tokens[i] = input_tokens[i].to(device)
# generate output tokens
output = model.generate(**input_tokens, max_new_tokens=100)
# decode output tokens into text
output = tokenizer.batch_decode(output)
# loop over the batch to print, in this example the batch size is 1
for i in output:
    print(i)
```


<!-- TO DO: Check this part -->
## Training Data
Granite Code Instruct models are trained on the following types of data.
* Code Commits Datasets: we sourced code commits data from the [CommitPackFT](https://huggingface.co/datasets/bigcode/commitpackft) dataset, a filtered version of the full CommitPack dataset. From CommitPackFT dataset, we only consider data for 92 programming languages. Our inclusion criteria boils down to selecting programming languages common across CommitPackFT and the 116 languages that we considered to pretrain the code-base model (*Granite-34B-Code-Base*). 
* Math Datasets: We consider two high-quality math datasets, [MathInstruct](https://huggingface.co/datasets/TIGER-Lab/MathInstruct) and [MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA). Due to license issues, we filtered out GSM8K-RFT and Camel-Math from MathInstruct dataset. 
* Code Instruction Datasets: We use [Glaive-Code-Assistant-v3](https://huggingface.co/datasets/glaiveai/glaive-code-assistant-v3), [Glaive-Function-Calling-v2](https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2), [NL2SQL11](https://huggingface.co/datasets/bugdaryan/sql-create-context-instruction) and a small collection of synthetic API calling datasets.
* Language Instruction Datasets: We include high-quality datasets such as [HelpSteer](https://huggingface.co/datasets/nvidia/HelpSteer) and an open license-filtered version of [Platypus](https://huggingface.co/datasets/garage-bAInd/Open-Platypus). We also include a collection of hardcoded prompts to ensure our model generates correct outputs given inquiries about its name or developers.

## Infrastructure
We train the Granite Code models using two of IBM's super computing clusters, namely Vela and Blue Vela, both outfitted with NVIDIA A100 and H100 GPUs respectively. These clusters provide a scalable and efficient infrastructure for training our models over thousands of GPUs.

## Ethical Considerations and Limitations
Granite code instruct models are primarily finetuned using instruction-response pairs across a specific set of programming languages. Thus, their performance may be limited with out-of-domain programming languages. In this situation, it is beneficial providing few-shot examples to steer the model's output. Moreover, developers should perform safety testing and target-specific tuning before deploying these models on critical applications. The model also inherits ethical considerations and limitations from its base model. For more information, please refer to *[Granite-34B-Code-Base-8K](https://huggingface.co/ibm-granite/granite-34b-code-base-8k)* model card.
