---
language:
- en
tags:
- pytorch
- text-generation
- causal-lm
- rwkv
license: apache-2.0
datasets:
- the_pile

---

# RWKV-4 Novel Models

## Model Description

These are RWKV-4-Pile models finetuned on novels.

Currently I am doing it for Chn novels. More languages to come.

Use https://github.com/BlinkDL/ChatRWKV to run them.

See https://github.com/BlinkDL/RWKV-LM for details on the RWKV Language Model (100% RNN).

* RWKV-4-Novel-ChnEng : 50% Chinese + 50% Pile
* RWKV-4-Novel-ChnEng-ChnPro : RWKV-4-Novel-ChnEng finetuned on high-quality professional Chn novels
* RWKV-4-Novel-Chn : 100% Chinese
