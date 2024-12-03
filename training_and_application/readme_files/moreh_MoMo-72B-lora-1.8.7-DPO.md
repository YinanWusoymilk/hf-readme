---
license: mit
language:
- en

metrics:
- accuracy
library_name: pytorch
---

# 24/04/05 update
We introduce [Moreh AI Model Hub with AMD GPU](https://model-hub.moreh.io/), an ai model host platform powered by AMD MI250 GPUs.
You can now test live-inference of this model at Moreh AI Model Hub. 

# **Introduction**
MoMo-72B-lora-1.8.7-DPO is trained via Direct Preference Optimization([DPO](https://arxiv.org/abs/2305.18290)) from [MoMo-72B-LoRA-V1.4](https://huggingface.co/moreh/MoMo-72B-LoRA-V1.4) as its base model, with several optimizations in hyperparameters.  
[MoMo-72B-LoRA-V1.4](https://huggingface.co/moreh/MoMo-72B-LoRA-V1.4) is trained via Supervised Fine-Tuning (SFT) using [LoRA](https://arxiv.org/abs/2106.09685), with the QWEN-72B model as its base-model.  
Note that we did not exploit any form of weight merge.  
For leaderboard submission, the trained weight is realigned for compatibility with llama.  
MoMo-72B is trained using **[Moreh](https://moreh.io/)**'s [MoAI platform](https://moreh.io/product), which simplifies the training of large-scale models, and AMD's MI250 GPU.
# 

## Details
### Used Librarys
- torch
- peft
### Used Datasets
- [slimorca](Open-Orca/SlimOrca)
- [truthy](https://huggingface.co/datasets/jondurbin/truthy-dpo-v0.1)
- [orca_dpo_pairs](https://huggingface.co/datasets/Intel/orca_dpo_pairs)
- No other dataset was used
- No benchmark test set or the training set are used
  - [data contamination check](https://github.com/swj0419/detect-pretrain-code-contamination) result
    
| Model                        | ARC   | MMLU | TruthfulQA | GSM8K |
|------------------------------|-------|-------|-------|-------|
| **V1.8.7(result < 0.1, %)**| TBU |TBU | 0.44 | 0.47 |
### Used Environments
- AMD MI250 & MoAI platform
- Please visit https://moreh.io/product for more information about MoAI platform
- Or, contact us directly [contact@moreh.io](mailto:contact@moreh.io)

## How to use

```python
# pip install transformers==4.35.2
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("moreh/MoMo-72B-lora-1.8.7-DPO")
model = AutoModelForCausalLM.from_pretrained(
    "moreh/MoMo-72B-lora-1.8.7-DPO"
)
```