---
language:
- ko
datasets:
- kyujinpy/KOR-OpenOrca-Platypus-v3
library_name: transformers
pipeline_tag: text-generation
license: cc-by-nc-sa-4.0
---

# **Ko-PlatYi-6B**  
<img src='./Ko-PlatYi.png' width=256>

## Model Details

**Model Developers** Kyujin Han (kyujinpy)

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture**   
Ko-PlatYi-6B is an auto-regressive language model based on the Yi-34B transformer architecture.

**Blog Link**  
Blog: [Coming soon...]  
Github: [Coming soon...]  

**Base Model**    
[beomi/Yi-Ko-6B](https://huggingface.co/beomi/Yi-Ko-6B)   

**Training Dataset**    
[kyujinpy/KOR-OpenOrca-Platypus-v3](https://huggingface.co/datasets/kyujinpy/KOR-OpenOrca-Platypus-v3).   
 
# **Model Benchmark**

## Open leaderboard  
> Follow up as [link](https://huggingface.co/spaces/upstage/open-ko-llm-leaderboard).  
  
| Model | Average | ARC | HellaSwag | MMLU | TruthfulQA | CommonGen-V2 |
| --- | --- | --- | --- | --- | --- | --- |  
| Ko-PlatYi-6B-O | 49.00 | 43.52 | 53.59 | 47.47 | 41.01 | 59.39 |  
| Ko-PlatYi-6B-kiwi | 48.75 | 41.98 | 53.61 | 46.10 | 38.30 | 63.75 |  
| Ko-PlatYi-6B-gu | 48.76 | 42.75 | 54.00 | 44.66 | 41.22 | 61.16 |  
| **Ko-PlatYi-6B** | 49.97 | 43.00 | 53.55 | 46.50 | 40.31 | 66.47 |
| Yi-Ko-6B | 48.79 | 41.04 | 53.39 | 46.28 | 41.64 | 61.63 
   
--- 
## AI-Harness Evaluation  
> AI-Harness evaluation; [link](https://github.com/Beomi/ko-lm-evaluation-harness)   
  
| Model | BoolQ | Copa | HellaSwag | Sentineg | 
| --- | --- | --- | --- | --- | 
|  | *Zero-shot* ||||
| Ko-PlatYi-6B-O | 0.3343 | 0.7687 | 0.4833 | 0.5794 | 
| Ko-PlatYi-6B-kiwi | 0.3343 | 0.7665 | 0.4746 | **0.6248** | 
| Ko-PlatYi-6B-gu | **0.7077** | **0.7696** | 0.4797 | 0.3979 | 
| **Ko-PlatYi-6B** | 0.3343 | 0.7684 | **0.4917** | 0.5226 | 
| Yi-Ko-6B | **0.7070** | 0.7696 | **0.5009** | 0.4044 | 
  
---
# Implementation Code

```python
### KO-Platypus
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

repo = "kyujinpy/Ko-PlatYi-6B"
OpenOrca = AutoModelForCausalLM.from_pretrained(
        repo,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map='auto'
)
OpenOrca_tokenizer = AutoTokenizer.from_pretrained(repo)
```
