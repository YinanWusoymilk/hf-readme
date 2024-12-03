---
language:
- en
- zh
- fr
- es
- de
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
- cerebras/SlimPajama-627B
- EleutherAI/pile
- bigcode/starcoderdata
- oscar-corpus/OSCAR-2301
---

# RWKV-5 World

Use rwkv pip package 0.8.22+ for RWKV-5 inference: https://pypi.org/project/rwkv/ (pipeline = PIPELINE(model, "rwkv_vocab_v20230424") for rwkv-world models)

Online 7B Demo: https://huggingface.co/spaces/BlinkDL/RWKV-Gradio-2

Online 1.5B Demo: https://huggingface.co/spaces/BlinkDL/RWKV-Gradio-1

GUI: https://github.com/josStorer/RWKV-Runner (see Releases)

Convert to HF formet: https://github.com/BBuf/RWKV-World-HF-Tokenizer

For developer: https://github.com/BlinkDL/ChatRWKV/blob/main/API_DEMO_CHAT.py

https://github.com/BlinkDL/ChatRWKV/blob/main/RWKV_v5_demo.py

How it works: https://twitter.com/BlinkDL_AI/status/1685230712247795713

https://www.rwkv.com/

## Model Description

RWKV-5 trained on 100+ world languages (70% English, 15% multilang, 15% code).

World = Some_Pile + Some_SlimPajama + Some_StarCoder + Some_OSCAR + All_Wikipedia + All_ChatGPT_Data_I_can_find

RWKV-5 training: set --my_testing "r2r4" in latest RWKV-LM v4neo: https://github.com/BlinkDL/RWKV-LM

World v1 = 0.59T tokens

World v2 = 1.12T tokens

Imagine what happens when we use more data :)

Recommended fine-tuning format (use \n for newlines):
```
User: xxxxxxxxxxxxxxx

Assistant: xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx

User: xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx

Assistant: xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx
```

A good chat prompt (better replace \n\n in xxx to \n, such that there will be no newlines in xxx):
```
User: hi

Assistant: Hi. I am your assistant and I will provide expert full response in full details. Please feel free to ask any question and I will always answer it.

User: xxx

Assistant:
```
QA prompt (better replace \n\n in xxx to \n, such that there will be no newlines in xxx):
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

!!! There should not be any space after your final ":" or you will upset the tokenizer and see non-English reponse !!!

!!! There should not be any space after your final ":" or you will upset the tokenizer and see non-English reponse !!!

!!! There should not be any space after your final ":" or you will upset the tokenizer and see non-English reponse !!!
