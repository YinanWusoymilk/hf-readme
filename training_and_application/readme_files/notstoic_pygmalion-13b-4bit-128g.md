---
language: en
license: other
commercial: no
inference: false
---
# pygmalion-13b-4bit-128g
## Model description
**Warning: THIS model is NOT suitable for use by minors. The model will output X-rated content.**

Quantized from the decoded pygmalion-13b xor format.
**https://huggingface.co/PygmalionAI/pygmalion-13b**

In safetensor format.

### Quantization Information
GPTQ CUDA quantized with: https://github.com/0cc4m/GPTQ-for-LLaMa
```
python llama.py --wbits 4 models/pygmalion-13b c4 --true-sequential --groupsize 128 --save_safetensors models/pygmalion-13b/4bit-128g.safetensors
```