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

# RWKV-6 World

RWKV-6 paper: https://arxiv.org/abs/2404.05892

Use rwkv pip package 0.8.24+ for RWKV-6 inference: https://pypi.org/project/rwkv/ (pipeline = PIPELINE(model, "rwkv_vocab_v20230424") for rwkv-world models)

Online Demo 1: https://huggingface.co/spaces/BlinkDL/RWKV-Gradio-2

Online Demo 2: https://huggingface.co/spaces/BlinkDL/RWKV-Gradio-1

GUI: https://github.com/josStorer/RWKV-Runner (see Releases)

For developer: https://github.com/BlinkDL/ChatRWKV/blob/main/API_DEMO_CHAT.py

https://github.com/BlinkDL/ChatRWKV/blob/main/RWKV_v6_demo.py

How it works: https://twitter.com/BlinkDL_AI/status/1685230712247795713

https://www.rwkv.com/

RWKV-6 7B MMLU = 46.7%: https://github.com/Jellyfish042/rwkv_mmlu

RWKV-6 0.1B (using pythia-160m tokenizer): https://huggingface.co/BlinkDL/temp-latest-training-models/blob/main/temp/rwkv-x060-173m-pile-20240515-ctx4k.pth

## Model Description

RWKV-6 trained on 100+ world languages (70% English, 15% multilang, 15% code).

World = Some_Pile + Some_SlimPajama + Some_StarCoder + Some_OSCAR + All_Wikipedia + All_ChatGPT_Data_I_can_find

World v1 = 0.59T tokens

World v2 = 1.12T tokens

World v2.1 = 1.42T tokens

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
