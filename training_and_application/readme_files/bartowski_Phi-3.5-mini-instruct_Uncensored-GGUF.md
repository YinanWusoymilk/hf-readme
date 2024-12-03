---
base_model: SicariusSicariiStuff/Phi-3.5-mini-instruct_Uncensored
license: apache-2.0
pipeline_tag: text-generation
quantized_by: bartowski
---

## Llamacpp imatrix Quantizations of Phi-3.5-mini-instruct_Uncensored

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b3600">b3600</a> for quantization.

Original model: https://huggingface.co/SicariusSicariiStuff/Phi-3.5-mini-instruct_Uncensored

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

Run them in [LM Studio](https://lmstudio.ai/)

## Prompt format

```
<s><|system|> {system_prompt}<|end|><|user|> {prompt}<|end|><|assistant|><|end|>
```

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [Phi-3.5-mini-instruct_Uncensored-f16.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-f16.gguf) | f16 | 7.64GB | false | Full F16 weights. |
| [Phi-3.5-mini-instruct_Uncensored-Q8_0.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q8_0.gguf) | Q8_0 | 4.06GB | false | Extremely high quality, generally unneeded but max available quant. |
| [Phi-3.5-mini-instruct_Uncensored-Q6_K_L.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q6_K_L.gguf) | Q6_K_L | 3.18GB | false | Uses Q8_0 for embed and output weights. Very high quality, near perfect, *recommended*. |
| [Phi-3.5-mini-instruct_Uncensored-Q6_K.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q6_K.gguf) | Q6_K | 3.14GB | false | Very high quality, near perfect, *recommended*. |
| [Phi-3.5-mini-instruct_Uncensored-Q5_K_L.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q5_K_L.gguf) | Q5_K_L | 2.88GB | false | Uses Q8_0 for embed and output weights. High quality, *recommended*. |
| [Phi-3.5-mini-instruct_Uncensored-Q5_K_M.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q5_K_M.gguf) | Q5_K_M | 2.82GB | false | High quality, *recommended*. |
| [Phi-3.5-mini-instruct_Uncensored-Q5_K_S.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q5_K_S.gguf) | Q5_K_S | 2.64GB | false | High quality, *recommended*. |
| [Phi-3.5-mini-instruct_Uncensored-Q4_K_L.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q4_K_L.gguf) | Q4_K_L | 2.47GB | false | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [Phi-3.5-mini-instruct_Uncensored-Q4_K_M.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q4_K_M.gguf) | Q4_K_M | 2.39GB | false | Good quality, default size for must use cases, *recommended*. |
| [Phi-3.5-mini-instruct_Uncensored-Q4_K_S.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q4_K_S.gguf) | Q4_K_S | 2.19GB | false | Slightly lower quality with more space savings, *recommended*. |
| [Phi-3.5-mini-instruct_Uncensored-Q3_K_XL.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q3_K_XL.gguf) | Q3_K_XL | 2.17GB | false | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [Phi-3.5-mini-instruct_Uncensored-Q3_K_L.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q3_K_L.gguf) | Q3_K_L | 2.09GB | false | Lower quality but usable, good for low RAM availability. |
| [Phi-3.5-mini-instruct_Uncensored-IQ4_XS.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-IQ4_XS.gguf) | IQ4_XS | 2.06GB | false | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [Phi-3.5-mini-instruct_Uncensored-Q3_K_M.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q3_K_M.gguf) | Q3_K_M | 1.96GB | false | Low quality. |
| [Phi-3.5-mini-instruct_Uncensored-IQ3_M.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-IQ3_M.gguf) | IQ3_M | 1.86GB | false | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [Phi-3.5-mini-instruct_Uncensored-Q3_K_S.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q3_K_S.gguf) | Q3_K_S | 1.68GB | false | Low quality, not recommended. |
| [Phi-3.5-mini-instruct_Uncensored-IQ3_XS.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-IQ3_XS.gguf) | IQ3_XS | 1.63GB | false | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [Phi-3.5-mini-instruct_Uncensored-Q2_K_L.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q2_K_L.gguf) | Q2_K_L | 1.51GB | false | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [Phi-3.5-mini-instruct_Uncensored-Q2_K.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-Q2_K.gguf) | Q2_K | 1.42GB | false | Very low quality but surprisingly usable. |
| [Phi-3.5-mini-instruct_Uncensored-IQ2_M.gguf](https://huggingface.co/bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF/blob/main/Phi-3.5-mini-instruct_Uncensored-IQ2_M.gguf) | IQ2_M | 1.32GB | false | Relatively low quality, uses SOTA techniques to be surprisingly usable. |

## Embed/output weights

Some of these quants (Q3_K_XL, Q4_K_L etc) are the standard quantization method with the embeddings and output weights quantized to Q8_0 instead of what they would normally default to.

Some say that this improves the quality, others don't notice any difference. If you use these models PLEASE COMMENT with your findings. I would like feedback that these are actually used and useful so I don't keep uploading quants no one is using.

Thanks!

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset

Thank you ZeroWw for the inspiration to experiment with embed/output

## Downloading using huggingface-cli

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF --include "Phi-3.5-mini-instruct_Uncensored-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/Phi-3.5-mini-instruct_Uncensored-GGUF --include "Phi-3.5-mini-instruct_Uncensored-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (Phi-3.5-mini-instruct_Uncensored-Q8_0) or download them all in place (./)

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

