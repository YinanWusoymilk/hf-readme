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

# RWKV-4 "Raven"-series Models

[UPDATE: Try RWKV-4-World (https://huggingface.co/BlinkDL/rwkv-4-world) for generation & chat & code in 100+ world languages, with great English zero-shot & in-context learning ability too.]

## Model Description

These are RWKV-4-Pile 1.5/3/7/14B models finetuned on Alpaca, CodeAlpaca, Guanaco, GPT4All, ShareGPT and more. **Even the 1.5B model is surprisingly good for its size.**

Gradio Demo: https://huggingface.co/spaces/BlinkDL/Raven-RWKV-7B and https://huggingface.co/spaces/BlinkDL/ChatRWKV-gradio

RWKV models inference: https://github.com/BlinkDL/ChatRWKV (fast CUDA).

Q8_0 models: only for https://github.com/saharNooby/rwkv.cpp (fast CPU).

See https://github.com/BlinkDL/RWKV-LM for details on the RWKV Language Model (100% RNN).

Best Prompt Format for Raven models, Bob is user, Alice is bot (NOTE: no space after final "Alice:"). You can use \n within xxxxxxxxxxx, but avoid \n\n.
```
Bob: xxxxxxxxxxxxxxxxxx\n\nAlice:
Bob: xxxxxxxxxxxxxxxxxx\n\nAlice: xxxxxxxxxxxxx\n\nBob: xxxxxxxxxxxxxxxx\n\nAlice:
```
New models will be named like Eng99%-Other1%, Eng86%-Chn10%-JpnEspKor2%-Other2%, etc.
Language ratios determined by amount of ChatGPT data. Please share more ChatGPT data to increase the ratio of your language.

Old models:
* RWKV-4-Raven-Eng : 99% English + 1% Multilang
* RWKV-4-Raven-EngAndMore : 96% English + 2% Chn Jpn + 2% Multilang (More Jpn than v6 "EngChnJpn")
* RWKV-4-Raven-ChnEng : 49% English + 50% Chinese + 1% Multilang

License: Apache 2.0
