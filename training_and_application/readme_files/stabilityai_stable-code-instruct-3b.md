---
license: other
language:
- en
tags:
- causal-lm
- code
metrics:
- code_eval
library_name: transformers
model-index:
- name: stabilityai/stable-code-instruct-3b
  results:
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Python)
    metrics:
    - name: pass@1
      type: pass@1
      value: 32.4
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (C++)
    metrics:
    - name: pass@1
      type: pass@1
      value: 30.9
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Java)
    metrics:
    - name: pass@1
      type: pass@1
      value: 32.1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (JavaScript)
    metrics:
    - name: pass@1
      type: pass@1
      value: 32.1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (PHP)
    metrics:
    - name: pass@1
      type: pass@1
      value: 24.2
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Rust)
    metrics:
    - name: pass@1
      type: pass@1
      value: 23.0
      verified: false
---
# **Stable Code Instruct 3B**

[Try it out here: https://huggingface.co/spaces/stabilityai/stable-code-instruct-3b](https://huggingface.co/spaces/stabilityai/stable-code-instruct-3b)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63466107f7bd6326925fc770/O7ZkLgqoJprQEWAttX7Hj.png)

## Model Description

`stable-code-instruct-3b` is a 2.7B billion parameter decoder-only language model tuned from [`stable-code-3b`](https://huggingface.co/stabilityai/stable-code-3b/). This model was trained on a mix of publicly available datasets, synthetic datasets using [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290). 

This instruct tune demonstrates state-of-the-art performance (compared to models of similar size) on the MultiPL-E metrics across multiple programming languages tested using [BigCode's Evaluation Harness](https://github.com/bigcode-project/bigcode-evaluation-harness/tree/main), and on the code portions of
[MT Bench](https://klu.ai/glossary/mt-bench-eval).
The model is finetuned to make it useable in tasks like,
  - General purpose Code/Software Engineering like conversations.
  - SQL related generation and conversation.

Please note: For commercial use, please refer to https://stability.ai/license.

## Usage
Here's how you can run the model use the model:

```python

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("stabilityai/stable-code-instruct-3b", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("stabilityai/stable-code-instruct-3b", torch_dtype=torch.bfloat16, trust_remote_code=True)
model.eval()
model = model.cuda()

messages = [
    {
        "role": "system",
        "content": "You are a helpful and polite assistant",
    },
    {
        "role": "user",
        "content": "Write a simple website in HTML. When a user clicks the button, it shows a random joke from a list of 4 jokes."
    },
]

prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)

inputs = tokenizer([prompt], return_tensors="pt").to(model.device)

tokens = model.generate(
    **inputs,
    max_new_tokens=1024,
    temperature=0.5,
    top_p=0.95,
    top_k=100,
    do_sample=True,
    use_cache=True
)

output = tokenizer.batch_decode(tokens[:, inputs.input_ids.shape[-1]:], skip_special_tokens=False)[0]
```

## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: `Stable Code Instruct 3B` model is an auto-regressive language model based on the transformer decoder architecture.
* **Language(s)**: English
* **Paper**: [Stable Code Technical Report](https://drive.google.com/file/d/16-DGsR5-qwoPztZ6HcM7KSRUxIXrjlSm/view)
* **Library**: [Alignment Handbook](https://github.com/huggingface/alignment-handbook.git)
* **Finetuned from model**: [https://huggingface.co/stabilityai/stable-code-3b](https://huggingface.co/stabilityai/stable-code-3b)
* **License**: [StabilityAI Community License](https://huggingface.co/stabilityai/stable-code-instruct-3b/blob/main/LICENSE.md).
* **Commercial License**: to use this model commercially, please refer to https://stability.ai/license
* **Contact**: For questions and comments about the model, please email `lm@stability.ai`


## Performance
### Multi-PL Benchmark:
| Model                        | Size | Avg  | Python | C++  | JavaScript | Java | PHP  | Rust |
|------------------------------|------|------|--------|------|------------|------|------|------|
| Codellama Instruct           | 7B   | 0.30 | 0.33   | 0.31 | 0.31       | 0.29 | 0.31 | 0.25 |
| Deepseek Instruct            | 1.3B | 0.44 | 0.52   | **0.52** | 0.41       | **0.46** | 0.45 | 0.28 |
| Stable Code Instruct (SFT)   | 3B   | 0.44 | 0.55   | 0.45 | 0.42       | 0.42 | 0.44 | 0.32 |
| Stable Code Instruct (DPO)   | 3B   | **0.47** | **0.59**   | 0.49 | **0.49**       | 0.44 | **0.45** | **0.37** |

### MT-Bench Coding:
| Model                       | Size | Score |
|-----------------------------|------|-----------------|
| DeepSeek Coder              | 1.3B | 4.6             |
| Stable Code Instruct (DPO)  | 3B   | **5.8**(ours)             |
| Stable Code Instruct (SFT)  | 3B   | 5.5             |
| DeepSeek Coder              | 6.7B | **6.9**             |
| CodeLlama Instruct          | 7B   | 3.55            |
| StarChat2                   | 15B  | 5.7             |

### SQL Performance
| Model                       | Size | Date  | Group By | Order By | Ratio | Join  | Where |
|-----------------------------|------|-------|----------|----------|-------|-------|-------|
| Stable Code Instruct (DPO)  | 3B   | 24.0% | 54.2%    | 68.5%    | 40.0% | 54.2% | 42.8% |
| DeepSeek-Coder Instruct     | 1.3B | 24.0% | 37.1%    | 51.4%    | 34.3% | 45.7% | 45.7% |
| SQLCoder                    | 7B   | 64.0% | 82.9%    | 74.3%    | 54.3% | 74.3% | 74.3% |




## How to Cite
```bibtex
@misc{stable-code-instruct-3b,
      url={[https://huggingface.co/stabilityai/stable-code-3b](https://huggingface.co/stabilityai/stable-code-instruct-3b)},
      title={Stable Code 3B},
      author={Phung, Duy, and Pinnaparaju, Nikhil and Adithyan, Reshinth and Zhuravinskyi, Maksym and Tow, Jonathan and Cooper, Nathan}
}
```