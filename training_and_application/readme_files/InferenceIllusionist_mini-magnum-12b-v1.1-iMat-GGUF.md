---
base_model: intervitens/mini-magnum-12b-v1.1
library_name: transformers
quantized_by: InferenceIllusionist
tags:
- iMat
- gguf
- Mistral
license: apache-2.0
---
<img src="https://i.imgur.com/P68dXux.png" width="400"/>

# mini-magnum-12b-v1.1-iMat-GGUF

> [!WARNING]
><b>Important Note:</b> Inferencing in llama.cpp has now been merged in [PR #8604](https://github.com/ggerganov/llama.cpp/pull/8604). Please ensure you are on release [b3438](https://github.com/ggerganov/llama.cpp/releases/tag/b3438) or newer. Text-generation-web-ui (Ooba) is also working as of 7/23. Kobold.cpp working as of  [v1.71](https://github.com/LostRuins/koboldcpp/releases/tag/v1.71). </b>

Quantized from mini-magnum-12b-v1.1 fp16
* Weighted quantizations were creating using fp16 GGUF and groups_merged.txt in 92 chunks and n_ctx=512
* Static fp16 will also be included in repo
* For a brief rundown of iMatrix quant performance please see this [PR](https://github.com/ggerganov/llama.cpp/pull/5747)
* <i>All quants are verified working prior to uploading to repo for your safety and convenience</i>

<b>KL-Divergence Reference Chart</b>
 (Click on image to view in full size)
[<img src="https://i.imgur.com/mV0nYdA.png" width="920"/>](https://i.imgur.com/mV0nYdA.png)

> [!TIP]
><b>Quant-specific Tips:</b>
>* If you are getting a `cudaMalloc failed: out of memory` error, try passing an argument for lower context in llama.cpp, e.g. for 8k: `-c 8192`
>* If you have all ampere generation or newer cards, you can use flash attention like so: `-fa`
>* Provided Flash Attention is enabled you can also use quantized cache to save on VRAM e.g. for 8-bit: `-ctk q8_0 -ctv q8_0`


Original model card can be found [here](https://huggingface.co/intervitens/mini-magnum-12b-v1.1)