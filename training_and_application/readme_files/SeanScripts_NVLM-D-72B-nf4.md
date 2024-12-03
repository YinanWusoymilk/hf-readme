---
license: cc-by-nc-4.0
base_model:
- nvidia/NVLM-D-72B
pipeline_tag: image-text-to-text
library_name: transformers
---

Converted using BitsAndBytes to NF4 (with double quantization) from [nvidia/NVLM-D-72B](https://huggingface.co/nvidia/NVLM-D-72B). The model belongs to Nvidia and has the Creative Commons Attribution Non Commercial 4.0 license.

This quantization seems to work fine when only using text, but I haven't been able to get coherent responses when an image is included. Work in progress, I could use some help figuring this out.

I made a slight modification to the `modeling_intern_vit.py` file by replacing a few occurrences like `torch.matmul(x, linearmodule.weight.t()) + linearmodule.bias` with `linearmodule(x)`. I'm not sure why these linear module applications were written this way, when it's equivalent but fails when the module is quantized because it's accessing the weight directly instead of using the module. Making this change makes the model "work" by at least not giving any errors when trying to run it, but I still haven't been able to get coherent outputs when sending images.

It might have something to do with how the QKV modules were packed, not playing well with quantization. I'll look into how they can be split into regular Q, K, and V tensors later. Or maybe someone else would like to help.

I also modified the generate call in `modeling_nvlm_d.py` slightly by having it not force `use_cache=True`, because this was causing an issue for me with cache tensors being on the wrong GPU if I tried to use the model more than once.

Requires at least 48 GB of VRAM. Probably still can't have very long context with only 48 GB though.