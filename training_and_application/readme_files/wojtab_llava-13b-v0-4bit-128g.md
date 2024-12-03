4-bit quant of llama part of llava https://github.com/haotian-liu/LLaVA https://huggingface.co/liuhaotian/LLaVA-13b-delta-v0

quantized by:
```
CUDA_VISIBLE_DEVICES=0 python llama.py /workspace/LLaVA-13B-v0/ c4 --wbits 4 --true-sequential --groupsize 128 --save_safetensors llava-13b-v0-4bit-128g.safetensors
```

on https://github.com/oobabooga/GPTQ-for-LLaMa CUDA branch of GPTQ (commit `57a2629`)

YOU CAN NOW RUN IT IN [TEXT-GENERATION-WEBUI](https://github.com/oobabooga/text-generation-webui) with `llava` extension (see: https://github.com/oobabooga/text-generation-webui/tree/main/extensions/llava)

---
license: other
---
