---
language:
- en
- zh
- de
- fr
- es
- pt
- ru
- it
- ja
- ko
- vi
- ar
tags:
- pytorch
- text-generation
- causal-lm
- rwkv
license: apache-2.0
datasets:
- EleutherAI/pile
- togethercomputer/RedPajama-Data-1T
---

# RWKV-4 World

## Model Description

RWKV-4 trained on 100+ world languages (70% English, 15% multilang, 15% code).

World = Some_Pile + Some_RedPajama + Some_OSCAR + All_Wikipedia + All_ChatGPT_Data_I_can_find

XXXtuned = finetune of World on MC4, OSCAR, wiki, etc.

How to use:
* use https://github.com/josStorer/RWKV-Runner for GUI
* use latest rwkv pip package (0.8.0+)
* use https://github.com/BlinkDL/ChatRWKV/blob/main/v2/benchmark_world.py and https://github.com/BlinkDL/ChatRWKV/blob/main/API_DEMO_WORLD.py to test it

The differences between World & Raven:
* set pipeline = PIPELINE(model, "rwkv_vocab_v20230424") instead of 20B_tokenizer.json (EXACTLY AS WRITTEN HERE. "rwkv_vocab_v20230424" is included in rwkv 0.7.4+)
* use Question/Answer or User/AI or Human/Bot for chat. **DO NOT USE Bob/Alice or Q/A**

For 0.1/0.4/1.5B models, use **fp32** for first layer (will overflow in fp16 at this moment - fixable in future), or bf16 if you have 30xx/40xx GPUs. Example strategy: cuda fp32 *1 -> cuda fp16

NOTE: the new greedy tokenizer (https://github.com/BlinkDL/ChatRWKV/blob/main/tokenizer/rwkv_tokenizer.py) will tokenize '\n\n' as one single token instead of ['\n','\n']

QA prompt (replace \n\n in xxx to \n):
```
Question: xxx

Answer:
```
and
```
Instruction: xxx

Input: xxx

Response:
```

A good chat prompt (replace \n\n in xxx to \n):
```
User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: xxx

Assistant:
```