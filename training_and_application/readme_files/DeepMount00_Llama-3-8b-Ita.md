---
language:
- it
- en
license: llama3
library_name: transformers
base_model: meta-llama/Meta-Llama-3-8B
datasets:
- DeepMount00/llm_ita_ultra
model-index:
- name: Llama-3-8b-Ita
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: IFEval (0-Shot)
      type: HuggingFaceH4/ifeval
      args:
        num_few_shot: 0
    metrics:
    - type: inst_level_strict_acc and prompt_level_strict_acc
      value: 75.3
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=DeepMount00/Llama-3-8b-Ita
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: BBH (3-Shot)
      type: BBH
      args:
        num_few_shot: 3
    metrics:
    - type: acc_norm
      value: 28.08
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=DeepMount00/Llama-3-8b-Ita
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MATH Lvl 5 (4-Shot)
      type: hendrycks/competition_math
      args:
        num_few_shot: 4
    metrics:
    - type: exact_match
      value: 5.36
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=DeepMount00/Llama-3-8b-Ita
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GPQA (0-shot)
      type: Idavidrein/gpqa
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 7.38
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=DeepMount00/Llama-3-8b-Ita
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MuSR (0-shot)
      type: TAUR-Lab/MuSR
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 11.68
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=DeepMount00/Llama-3-8b-Ita
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU-PRO (5-shot)
      type: TIGER-Lab/MMLU-Pro
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 31.69
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=DeepMount00/Llama-3-8b-Ita
      name: Open LLM Leaderboard
---
## Model Architecture
- **Base Model:** [Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B)
- **Specialization:** Italian Language

## Evaluation

For a detailed comparison of model performance, check out the [Leaderboard for Italian Language Models](https://huggingface.co/spaces/FinancialSupport/open_ita_llm_leaderboard).

Here's a breakdown of the performance metrics:

| Metric                      | hellaswag_it acc_norm | arc_it acc_norm | m_mmlu_it 5-shot acc | Average |
|:----------------------------|:----------------------|:----------------|:---------------------|:--------|
| **Accuracy Normalized**     | 0.6518                | 0.5441        | 0.5729              | 0.5896  |

---

## How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

MODEL_NAME = "DeepMount00/Llama-3-8b-Ita"

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16).eval()
model.to(device)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def generate_answer(prompt):
    messages = [
        {"role": "user", "content": prompt},
    ]
    model_inputs = tokenizer.apply_chat_template(messages, return_tensors="pt").to(device)
    generated_ids = model.generate(model_inputs, max_new_tokens=200, do_sample=True,
                                          temperature=0.001)
    decoded = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return decoded[0]

prompt = "Come si apre un file json in python?"
answer = generate_answer(prompt)
print(answer)
```
---
## Developer
[Michele Montebovi]
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_DeepMount00__Llama-3-8b-Ita)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |26.58|
|IFEval (0-Shot)    |75.30|
|BBH (3-Shot)       |28.08|
|MATH Lvl 5 (4-Shot)| 5.36|
|GPQA (0-shot)      | 7.38|
|MuSR (0-shot)      |11.68|
|MMLU-PRO (5-shot)  |31.69|

