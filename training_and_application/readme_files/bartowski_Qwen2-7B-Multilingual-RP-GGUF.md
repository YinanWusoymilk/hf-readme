---
license: apache-2.0
language:
- en
- ko
- ja
- zh
- es
quantized_by: bartowski
pipeline_tag: text-generation
---

## Llamacpp imatrix Quantizations of Qwen2-7B-Multilingual-RP

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b3266">b3266</a> for quantization.

Original model: https://huggingface.co/maywell/Qwen2-7B-Multilingual-RP

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

## Prompt format

```
<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Description |
| -------- | ---------- | --------- | ----------- |
| [Qwen2-7B-Multilingual-RP-Q8_0_L.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q8_1.gguf) | Q8_0_L | 9.12GB | *Experimental*, uses f16 for embed and output weights. Please provide any feedback of differences. Extremely high quality, generally unneeded but max available quant. |
| [Qwen2-7B-Multilingual-RP-Q8_0.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q8_0.gguf) | Q8_0 | 8.09GB | Extremely high quality, generally unneeded but max available quant. |
| [Qwen2-7B-Multilingual-RP-Q6_K_L.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q6_K_L.gguf) | Q6_K_L | 7.54GB | *Experimental*, uses f16 for embed and output weights. Please provide any feedback of differences. Very high quality, near perfect, *recommended*. |
| [Qwen2-7B-Multilingual-RP-Q6_K.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q6_K.gguf) | Q6_K | 6.25GB | Very high quality, near perfect, *recommended*. |
| [Qwen2-7B-Multilingual-RP-Q5_K_L.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q5_K_L.gguf) | Q5_K_L | 6.80GB | *Experimental*, uses f16 for embed and output weights. Please provide any feedback of differences. High quality, *recommended*. |
| [Qwen2-7B-Multilingual-RP-Q5_K_M.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q5_K_M.gguf) | Q5_K_M | 5.44GB | High quality, *recommended*. |
| [Qwen2-7B-Multilingual-RP-Q5_K_S.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q5_K_S.gguf) | Q5_K_S | 5.31GB | High quality, *recommended*. |
| [Qwen2-7B-Multilingual-RP-Q4_K_L.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q4_K_L.gguf) | Q4_K_L | 6.10GB | *Experimental*, uses f16 for embed and output weights. Please provide any feedback of differences. Good quality, uses about 4.83 bits per weight, *recommended*. |
| [Qwen2-7B-Multilingual-RP-Q4_K_M.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q4_K_M.gguf) | Q4_K_M | 4.68GB | Good quality, uses about 4.83 bits per weight, *recommended*. |
| [Qwen2-7B-Multilingual-RP-Q4_K_S.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q4_K_S.gguf) | Q4_K_S | 4.45GB | Slightly lower quality with more space savings, *recommended*. |
| [Qwen2-7B-Multilingual-RP-IQ4_XS.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-IQ4_XS.gguf) | IQ4_XS | 4.21GB | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [Qwen2-7B-Multilingual-RP-Q3_K_XL.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q3_K_XL.gguf) | Q3_K_XL | 5.58GB | *Experimental*, uses f16 for embed and output weights. Please provide any feedback of differences. Lower quality but usable, good for low RAM availability. |
| [Qwen2-7B-Multilingual-RP-Q3_K_L.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q3_K_L.gguf) | Q3_K_L | 4.08GB | Lower quality but usable, good for low RAM availability. |
| [Qwen2-7B-Multilingual-RP-Q3_K_M.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q3_K_M.gguf) | Q3_K_M | 3.80GB | Even lower quality. |
| [Qwen2-7B-Multilingual-RP-IQ3_M.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-IQ3_M.gguf) | IQ3_M | 3.57GB | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [Qwen2-7B-Multilingual-RP-Q3_K_S.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q3_K_S.gguf) | Q3_K_S | 3.49GB | Low quality, not recommended. |
| [Qwen2-7B-Multilingual-RP-IQ3_XS.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-IQ3_XS.gguf) | IQ3_XS | 3.34GB | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [Qwen2-7B-Multilingual-RP-IQ3_XXS.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-IQ3_XXS.gguf) | IQ3_XXS | 3.11GB | Lower quality, new method with decent performance, comparable to Q3 quants. |
| [Qwen2-7B-Multilingual-RP-Q2_K.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-Q2_K.gguf) | Q2_K | 3.01GB | Very low quality but surprisingly usable. |
| [Qwen2-7B-Multilingual-RP-IQ2_M.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-IQ2_M.gguf) | IQ2_M | 2.78GB | Very low quality, uses SOTA techniques to also be surprisingly usable. |
| [Qwen2-7B-Multilingual-RP-IQ2_S.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-IQ2_S.gguf) | IQ2_S | 2.59GB | Very low quality, uses SOTA techniques to be usable. |
| [Qwen2-7B-Multilingual-RP-IQ2_XS.gguf](https://huggingface.co/bartowski/Qwen2-7B-Multilingual-RP-GGUF/blob/main/Qwen2-7B-Multilingual-RP-IQ2_XS.gguf) | IQ2_XS | 2.46GB | Very low quality, uses SOTA techniques to be usable. |

## Downloading using huggingface-cli

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/Qwen2-7B-Multilingual-RP-GGUF --include "Qwen2-7B-Multilingual-RP-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/Qwen2-7B-Multilingual-RP-GGUF --include "Qwen2-7B-Multilingual-RP-Q8_0.gguf/*" --local-dir Qwen2-7B-Multilingual-RP-Q8_0
```

You can either specify a new local-dir (Qwen2-7B-Multilingual-RP-Q8_0) or download them all in place (./)

## Which file should I choose?

A great write up with charts showing various performances is provided by Artefact2 [here](https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9)

The first thing to figure out is how big a model you can run. To do this, you'll need to figure out how much RAM and/or VRAM you have.

If you want your model running as FAST as possible, you'll want to fit the whole thing on your GPU's VRAM. Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM.

If you want the absolute maximum quality, add both your system RAM and your GPU's VRAM together, then similarly grab a quant with a file size 1-2GB Smaller than that total.

Next, you'll need to decide if you want to use an 'I-quant' or a 'K-quant'.

If you don't want to think too much, grab one of the K-quants. These are in format 'QX_K_X', like Q5_K_M.

If you want to get more into the weeds, you can check out this extremely useful feature chart:

[llama.cpp feature matrix](https://github.com/ggerganov/llama.cpp/wiki/Feature-matrix)

But basically, if you're aiming for below Q4, and you're running cuBLAS (Nvidia) or rocBLAS (AMD), you should look towards the I-quants. These are in format IQX_X, like IQ3_M. These are newer and offer better performance for their size.

These I-quants can also be used on CPU and Apple Metal, but will be slower than their K-quant equivalent, so speed vs performance is a tradeoff you'll have to decide.

The I-quants are *not* compatible with Vulcan, which is also AMD, so if you have an AMD card double check if you're using the rocBLAS build or the Vulcan build. At the time of writing this, LM Studio has a preview with ROCm support, and other inference engines have specific builds for ROCm.

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski
