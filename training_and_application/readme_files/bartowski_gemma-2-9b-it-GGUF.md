---
base_model: google/gemma-2-9b-it
library_name: transformers
license: gemma
pipeline_tag: text-generation
tags:
- conversational
quantized_by: bartowski
extra_gated_heading: Access Gemma on Hugging Face
extra_gated_prompt: To access Gemma on Hugging Face, you’re required to review and
  agree to Google’s usage license. To do this, please ensure you’re logged in to Hugging
  Face and click below. Requests are processed immediately.
extra_gated_button_content: Acknowledge license
---

## Llamacpp imatrix Quantizations of gemma-2-9b-it

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b3389">b3389</a> for quantization.

Original model: https://huggingface.co/google/gemma-2-9b-it

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

## Prompt format

```
<start_of_turn>user
{prompt}<end_of_turn>
<start_of_turn>model
<end_of_turn>
<start_of_turn>model

```

Note that this model does not support a System prompt.

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [gemma-2-9b-it-f32.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-f32.gguf) | f32 | 36.97GB | false | Full F32 weights. |
| [gemma-2-9b-it-Q8_0.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q8_0.gguf) | Q8_0 | 9.83GB | false | Extremely high quality, generally unneeded but max available quant. |
| [gemma-2-9b-it-Q6_K_L.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q6_K_L.gguf) | Q6_K_L | 7.81GB | false | Uses Q8_0 for embed and output weights. Very high quality, near perfect, *recommended*. |
| [gemma-2-9b-it-Q6_K.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q6_K.gguf) | Q6_K | 7.59GB | false | Very high quality, near perfect, *recommended*. |
| [gemma-2-9b-it-Q5_K_L.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q5_K_L.gguf) | Q5_K_L | 6.87GB | false | Uses Q8_0 for embed and output weights. High quality, *recommended*. |
| [gemma-2-9b-it-Q5_K_M.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q5_K_M.gguf) | Q5_K_M | 6.65GB | false | High quality, *recommended*. |
| [gemma-2-9b-it-Q5_K_S.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q5_K_S.gguf) | Q5_K_S | 6.48GB | false | High quality, *recommended*. |
| [gemma-2-9b-it-Q4_K_L.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q4_K_L.gguf) | Q4_K_L | 5.98GB | false | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [gemma-2-9b-it-Q4_K_M.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q4_K_M.gguf) | Q4_K_M | 5.76GB | false | Good quality, default size for must use cases, *recommended*. |
| [gemma-2-9b-it-Q4_K_S.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q4_K_S.gguf) | Q4_K_S | 5.48GB | false | Slightly lower quality with more space savings, *recommended*. |
| [gemma-2-9b-it-IQ4_XS.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-IQ4_XS.gguf) | IQ4_XS | 5.18GB | false | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [gemma-2-9b-it-Q3_K_L.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q3_K_L.gguf) | Q3_K_L | 5.13GB | false | Lower quality but usable, good for low RAM availability. |
| [gemma-2-9b-it-Q3_K_M.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q3_K_M.gguf) | Q3_K_M | 4.76GB | false | Low quality. |
| [gemma-2-9b-it-IQ3_M.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-IQ3_M.gguf) | IQ3_M | 4.49GB | false | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [gemma-2-9b-it-Q3_K_S.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q3_K_S.gguf) | Q3_K_S | 4.34GB | false | Low quality, not recommended. |
| [gemma-2-9b-it-IQ3_XS.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-IQ3_XS.gguf) | IQ3_XS | 4.14GB | false | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [gemma-2-9b-it-Q2_K_L.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q2_K_L.gguf) | Q2_K_L | 4.03GB | false | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [gemma-2-9b-it-Q2_K.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-Q2_K.gguf) | Q2_K | 3.81GB | false | Very low quality but surprisingly usable. |
| [gemma-2-9b-it-IQ3_XXS.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-IQ3_XXS.gguf) | IQ3_XXS | 3.80GB | false | Lower quality, new method with decent performance, comparable to Q3 quants. |
| [gemma-2-9b-it-IQ2_M.gguf](https://huggingface.co/bartowski/gemma-2-9b-it-GGUF/blob/main/gemma-2-9b-it-IQ2_M.gguf) | IQ2_M | 3.43GB | false | Relatively low quality, uses SOTA techniques to be surprisingly usable. |

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
huggingface-cli download bartowski/gemma-2-9b-it-GGUF --include "gemma-2-9b-it-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/gemma-2-9b-it-GGUF --include "gemma-2-9b-it-Q8_0.gguf/*" --local-dir gemma-2-9b-it-Q8_0
```

You can either specify a new local-dir (gemma-2-9b-it-Q8_0) or download them all in place (./)

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

