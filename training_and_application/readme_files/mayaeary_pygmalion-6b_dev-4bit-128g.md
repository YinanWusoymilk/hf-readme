---
license: creativeml-openrail-m
tags:
- text generation
- conversational
- gptq
- 4bit
inference: false
language:
- en
pipeline_tag: text-generation
---

GPTQ quantization of https://huggingface.co/PygmalionAI/pygmalion-6b/commit/30e2405100eac6bd53f75964cc7345eeafd19f7d

Using this repository: https://github.com/mayaeary/GPTQ-for-LLaMa/tree/gptj-v2

Command: 
```
python3 gptj.py models/pygmalion-6b_dev c4 --wbits 4 --groupsize 128 --save_safetensors models/pygmalion-6b_dev-4bit-128g.safetensors
```