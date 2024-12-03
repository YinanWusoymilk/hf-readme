---
base_model: mattshumer/Reflection-Llama-3.1-70B
library_name: transformers
license: llama3.1
pipeline_tag: text-generation
quantized_by: bartowski
---

# DO NOT DOWNLOAD

It has been rediscovered that these are again the wrong weights, this warning will go away when the proper files are up

https://x.com/mattshumer_/status/1832424499054309804?s=46

## Llamacpp imatrix Quantizations of Reflection-Llama-3.1-70B

<b>Yes, this is with the fix to the tokenizer!</b>

If you want to make sure it's using the thought and output tokens, be sure to enable rendering of special tokens (in llama.cpp this is the `--special` tag)

It is able to use them without rendering them, much like chat tokens, this will just let you *see* them as they're getting used by the model.

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b3658">b3658</a> for quantization.

Original model: https://huggingface.co/mattshumer/Reflection-Llama-3.1-70B

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

Run them in [LM Studio](https://lmstudio.ai/)

## Prompt format

For improved reasoning, its suggested you use this system prompt:

```
You are a world-class AI system, capable of complex reasoning and reflection. Reason through the query inside <thinking> tags, and then provide your final response inside <output> tags. If you detect that you made a mistake in your reasoning at any point, correct yourself inside <reflection> tags.<|eot_id|><|start_header_id|>user<|end_header_id|>
```

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [Reflection-Llama-3.1-70B-Q8_0.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/tree/main/Reflection-Llama-3.1-70B-Q8_0) | Q8_0 | 74.98GB | true | Extremely high quality, generally unneeded but max available quant. |
| [Reflection-Llama-3.1-70B-Q6_K_L.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/tree/main/Reflection-Llama-3.1-70B-Q6_K_L) | Q6_K_L | 58.40GB | true | Uses Q8_0 for embed and output weights. Very high quality, near perfect, *recommended*. |
| [Reflection-Llama-3.1-70B-Q6_K.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/tree/main/Reflection-Llama-3.1-70B-Q6_K) | Q6_K | 57.89GB | true | Very high quality, near perfect, *recommended*. |
| [Reflection-Llama-3.1-70B-Q5_K_L.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/tree/main/Reflection-Llama-3.1-70B-Q5_K_L) | Q5_K_L | 50.60GB | true | Uses Q8_0 for embed and output weights. High quality, *recommended*. |
| [Reflection-Llama-3.1-70B-Q5_K_M.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/tree/main/Reflection-Llama-3.1-70B-Q5_K_M) | Q5_K_M | 49.95GB | true | High quality, *recommended*. |
| [Reflection-Llama-3.1-70B-Q5_K_S.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-Q5_K_S.gguf) | Q5_K_S | 48.66GB | false | High quality, *recommended*. |
| [Reflection-Llama-3.1-70B-Q4_K_L.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-Q4_K_L.gguf) | Q4_K_L | 43.30GB | false | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [Reflection-Llama-3.1-70B-Q4_K_M.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-Q4_K_M.gguf) | Q4_K_M | 42.52GB | false | Good quality, default size for must use cases, *recommended*. |
| [Reflection-Llama-3.1-70B-Q4_K_S.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-Q4_K_S.gguf) | Q4_K_S | 40.35GB | false | Slightly lower quality with more space savings, *recommended*. |
| [Reflection-Llama-3.1-70B-Q4_0.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-Q4_0.gguf) | Q4_0 | 40.12GB | false | Legacy format, generally not worth using over similarly sized formats |
| [Reflection-Llama-3.1-70B-Q3_K_XL.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-Q3_K_XL.gguf) | Q3_K_XL | 38.06GB | false | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [Reflection-Llama-3.1-70B-IQ4_XS.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-IQ4_XS.gguf) | IQ4_XS | 37.90GB | false | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [Reflection-Llama-3.1-70B-Q3_K_L.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-Q3_K_L.gguf) | Q3_K_L | 37.14GB | false | Lower quality but usable, good for low RAM availability. |
| [Reflection-Llama-3.1-70B-Q3_K_M.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-Q3_K_M.gguf) | Q3_K_M | 34.27GB | false | Low quality. |
| [Reflection-Llama-3.1-70B-IQ3_M.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-IQ3_M.gguf) | IQ3_M | 31.94GB | false | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [Reflection-Llama-3.1-70B-Q3_K_S.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-Q3_K_S.gguf) | Q3_K_S | 30.91GB | false | Low quality, not recommended. |
| [Reflection-Llama-3.1-70B-IQ3_XS.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-IQ3_XS.gguf) | IQ3_XS | 29.31GB | false | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [Reflection-Llama-3.1-70B-Q2_K_L.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-Q2_K_L.gguf) | Q2_K_L | 27.40GB | false | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [Reflection-Llama-3.1-70B-Q2_K.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-Q2_K.gguf) | Q2_K | 26.38GB | false | Very low quality but surprisingly usable. |
| [Reflection-Llama-3.1-70B-IQ2_M.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-IQ2_M.gguf) | IQ2_M | 24.12GB | false | Relatively low quality, uses SOTA techniques to be surprisingly usable. |
| [Reflection-Llama-3.1-70B-IQ2_S.gguf](https://huggingface.co/bartowski/Reflection-Llama-3.1-70B-GGUF/blob/main/Reflection-Llama-3.1-70B-IQ2_S.gguf) | IQ2_S | 22.24GB | false | Low quality, uses SOTA techniques to be usable. |

## Embed/output weights

Some of these quants (Q3_K_XL, Q4_K_L etc) are the standard quantization method with the embeddings and output weights quantized to Q8_0 instead of what they would normally default to.

Some say that this improves the quality, others don't notice any difference. If you use these models PLEASE COMMENT with your findings. I would like feedback that these are actually used and useful so I don't keep uploading quants no one is using.

Thanks!

## Downloading using huggingface-cli

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/Reflection-Llama-3.1-70B-GGUF --include "Reflection-Llama-3.1-70B-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/Reflection-Llama-3.1-70B-GGUF --include "Reflection-Llama-3.1-70B-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (Reflection-Llama-3.1-70B-Q8_0) or download them all in place (./)

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

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset

Thank you ZeroWw for the inspiration to experiment with embed/output

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski
