---
license: mit
language:
- en
---
# **Introduction**
MoMo-72B is trained via Supervised Fine-Tuning (SFT) using [LoRA](https://arxiv.org/abs/2106.09685), with the QWEN-72B model as its base-model.  
Note that we did not exploit any form of weight merge.  
For leaderboard submission, the trained weight is realigned for compatibility with llama.  
MoMo-72B is trained using **[Moreh](https://moreh.io/)**'s [MoAI platform](https://moreh.io/product), which simplifies the training of large-scale models, and AMD's MI250 GPU.


## Details
### Used Librarys
- torch
- peft
### Used Datasets
- Open-Orca/SlimOrca
- No other dataset was used
- No benchmark test set or the training set are used
  - [data contamination check](https://github.com/swj0419/detect-pretrain-code-contamination) result
    
| Model                        | ARC   | MMLU | TruthfulQA | GSM8K |
|------------------------------|-------|-------|-------|-------|
| **V1.4(result < 0.1, %)**| TBU |0.73 | 0.71 | TBU |
### Used Environments
- AMD MI250 & MoAI platform
- Please visit https://moreh.io/product for more information about MoAI platform
- Or, contact us directly [contact@moreh.io](mailto:contact@moreh.io)

## How to use

```python
# pip install transformers==4.35.2
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("moreh/MoMo-72B-LoRA-V1.4")
model = AutoModelForCausalLM.from_pretrained(
    "moreh/MoMo-72B-LoRA-V1.4"
)
```