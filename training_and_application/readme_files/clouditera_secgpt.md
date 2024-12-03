---
license: apache-2.0
datasets:
- w8ay/security-paper-datasets
- TigerResearch/tigerbot-zhihu-zh-10k
pipeline_tag: text-generation
---

Github: https://github.com/Clouditera/secgpt

## 使用
商业模型对于网络安全领域问题大多会有道德限制，所以基于网络安全数据训练了一个模型，模型基于Baichuan 13B，模型参数大小130亿，至少需要30G显存运行，35G最佳。
- transformers
- peft

**模型加载**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from peft import PeftModel
device = 'auto'
tokenizer = AutoTokenizer.from_pretrained("w8ay/secgpt", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("w8ay/secgpt", 
                                             trust_remote_code=True,
                                             device_map=device,
                                             torch_dtype=torch.float16)
print("模型加载成功")

```
**调用**
```python
def reformat_sft(instruction, input):
    if input:
        prefix = (
            "Below is an instruction that describes a task, paired with an input that provides further context. "
            "Write a response that appropriately completes the request.\n"
            f"### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
        )
    else:
        prefix = (
            "Below is an instruction that describes a task. "
            "Write a response that appropriately completes the request.\n"
            f"### Instruction:\n{instruction}\n\n### Response:"
        )
    return prefix

query = '''介绍sqlmap如何使用'''
query = reformat_sft(query,'')

generation_kwargs = {
    "top_p": 0.7,
    "temperature": 0.3,
    "max_new_tokens": 2000,
    "do_sample": True,
    "repetition_penalty":1.1
}

inputs = tokenizer.encode(query, return_tensors='pt', truncation=True)
inputs = inputs.cuda()
generate = model.generate(input_ids=inputs, **generation_kwargs)
output = tokenizer.decode(generate[0])
print(output)
```
