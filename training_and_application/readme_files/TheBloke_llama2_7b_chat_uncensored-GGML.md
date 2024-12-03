---
license: other
datasets:
- ehartford/wizard_vicuna_70k_unfiltered
model_name: Llama2 7B Chat Uncensored
inference: false
model_creator: George Sung
model_link: https://huggingface.co/georgesung/llama2_7b_chat_uncensored
model_type: llama
quantized_by: TheBloke
base_model: georgesung/llama2_7b_chat_uncensored
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://discord.gg/theblokeai">Chat & support: TheBloke's Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<div style="text-align:center; margin-top: 0em; margin-bottom: 0em"><p style="margin-top: 0.25em; margin-bottom: 0em;">TheBloke's LLM work is generously supported by a grant from <a href="https://a16z.com">andreessen horowitz (a16z)</a></p></div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Llama2 7B Chat Uncensored - GGML
- Model creator: [George Sung](https://huggingface.co/georgesung)
- Original model: [Llama2 7B Chat Uncensored](https://huggingface.co/georgesung/llama2_7b_chat_uncensored)

## Description

This repo contains GGML format model files for [George Sung's Llama2 7B Chat Uncensored](https://huggingface.co/georgesung/llama2_7b_chat_uncensored).

### Important note regarding GGML files.

The GGML format has now been superseded by GGUF. As of August 21st 2023, [llama.cpp](https://github.com/ggerganov/llama.cpp) no longer supports GGML models. Third party clients and libraries are expected to still support it for a time, but many may also drop support.

Please use the GGUF models instead.
### About GGML

GGML files are for CPU + GPU inference using [llama.cpp](https://github.com/ggerganov/llama.cpp) and libraries and UIs which support this format, such as:
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most popular web UI. Supports NVidia CUDA GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a powerful GGML web UI with GPU acceleration on all platforms (CUDA and OpenCL). Especially good for story telling.
* [LM Studio](https://lmstudio.ai/), a fully featured local GUI with GPU acceleration on both Windows (NVidia and AMD), and macOS.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with CUDA GPU acceleration via the c_transformers backend.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.

## Repositories available

* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGUF)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU+GPU inference (deprecated)](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML)
* [George Sung's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/georgesung/llama2_7b_chat_uncensored)

## Prompt template: Human-Response

```
### HUMAN:
{prompt}

### RESPONSE:

```

<!-- compatibility_ggml start -->
## Compatibility

These quantised GGML files are compatible with llama.cpp between June 6th (commit `2d43387`) and August 21st 2023.

For support with latest llama.cpp, please use GGUF files instead.

The final llama.cpp commit with support for GGML was: [dadbed99e65252d79f81101a392d0d6497b86caa](https://github.com/ggerganov/llama.cpp/commit/dadbed99e65252d79f81101a392d0d6497b86caa)

As of August 23rd 2023 they are still compatible with all UIs, libraries and utilities which use GGML. This may change in the future.

## Explanation of the new k-quant methods
<details>
  <summary>Click to see details</summary>

The new methods available are:
* GGML_TYPE_Q2_K - "type-1" 2-bit quantization in super-blocks containing 16 blocks, each block having 16 weight. Block scales and mins are quantized with 4 bits. This ends up effectively using 2.5625 bits per weight (bpw)
* GGML_TYPE_Q3_K - "type-0" 3-bit quantization in super-blocks containing 16 blocks, each block having 16 weights. Scales are quantized with 6 bits. This end up using 3.4375 bpw.
* GGML_TYPE_Q4_K - "type-1" 4-bit quantization in super-blocks containing 8 blocks, each block having 32 weights. Scales and mins are quantized with 6 bits. This ends up using 4.5 bpw.
* GGML_TYPE_Q5_K - "type-1" 5-bit quantization. Same super-block structure as GGML_TYPE_Q4_K resulting in 5.5 bpw
* GGML_TYPE_Q6_K - "type-0" 6-bit quantization. Super-blocks with 16 blocks, each block having 16 weights. Scales are quantized with 8 bits. This ends up using 6.5625 bpw
* GGML_TYPE_Q8_K - "type-0" 8-bit quantization. Only used for quantizing intermediate results. The difference to the existing Q8_0 is that the block size is 256. All 2-6 bit dot products are implemented for this quantization type.

Refer to the Provided Files table below to see what files use which methods, and how.
</details>
<!-- compatibility_ggml end -->

## Provided files

| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| [llama2_7b_chat_uncensored.ggmlv3.q2_K.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q2_K.bin) | q2_K | 2 | 2.87 GB| 5.37 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.vw and feed_forward.w2 tensors, GGML_TYPE_Q2_K for the other tensors. |
| [llama2_7b_chat_uncensored.ggmlv3.q3_K_S.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q3_K_S.bin) | q3_K_S | 3 | 2.95 GB| 5.45 GB | New k-quant method. Uses GGML_TYPE_Q3_K for all tensors |
| [llama2_7b_chat_uncensored.ggmlv3.q3_K_M.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q3_K_M.bin) | q3_K_M | 3 | 3.28 GB| 5.78 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| [llama2_7b_chat_uncensored.ggmlv3.q3_K_L.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q3_K_L.bin) | q3_K_L | 3 | 3.60 GB| 6.10 GB | New k-quant method. Uses GGML_TYPE_Q5_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| [llama2_7b_chat_uncensored.ggmlv3.q4_0.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q4_0.bin) | q4_0 | 4 | 3.79 GB| 6.29 GB | Original quant method, 4-bit. |
| [llama2_7b_chat_uncensored.ggmlv3.q4_K_S.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q4_K_S.bin) | q4_K_S | 4 | 3.83 GB| 6.33 GB | New k-quant method. Uses GGML_TYPE_Q4_K for all tensors |
| [llama2_7b_chat_uncensored.ggmlv3.q4_K_M.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q4_K_M.bin) | q4_K_M | 4 | 4.08 GB| 6.58 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q4_K |
| [llama2_7b_chat_uncensored.ggmlv3.q4_1.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q4_1.bin) | q4_1 | 4 | 4.21 GB| 6.71 GB | Original quant method, 4-bit. Higher accuracy than q4_0 but not as high as q5_0. However has quicker inference than q5 models. |
| [llama2_7b_chat_uncensored.ggmlv3.q5_0.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q5_0.bin) | q5_0 | 5 | 4.63 GB| 7.13 GB | Original quant method, 5-bit. Higher accuracy, higher resource usage and slower inference. |
| [llama2_7b_chat_uncensored.ggmlv3.q5_K_S.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q5_K_S.bin) | q5_K_S | 5 | 4.65 GB| 7.15 GB | New k-quant method. Uses GGML_TYPE_Q5_K for all tensors |
| [llama2_7b_chat_uncensored.ggmlv3.q5_K_M.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q5_K_M.bin) | q5_K_M | 5 | 4.78 GB| 7.28 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q5_K |
| [llama2_7b_chat_uncensored.ggmlv3.q5_1.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q5_1.bin) | q5_1 | 5 | 5.06 GB| 7.56 GB | Original quant method, 5-bit. Even higher accuracy, resource usage and slower inference. |
| [llama2_7b_chat_uncensored.ggmlv3.q6_K.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q6_K.bin) | q6_K | 6 | 5.53 GB| 8.03 GB | New k-quant method. Uses GGML_TYPE_Q8_K for all tensors - 6-bit quantization |
| [llama2_7b_chat_uncensored.ggmlv3.q8_0.bin](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML/blob/main/llama2_7b_chat_uncensored.ggmlv3.q8_0.bin) | q8_0 | 8 | 7.16 GB| 9.66 GB | Original quant method, 8-bit. Almost indistinguishable from float16. High resource use and slow. Not recommended for most users. |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

## How to run in `llama.cpp`

Make sure you are using `llama.cpp` from commit [dadbed99e65252d79f81101a392d0d6497b86caa](https://github.com/ggerganov/llama.cpp/commit/dadbed99e65252d79f81101a392d0d6497b86caa) or earlier.

For compatibility with latest llama.cpp, please use GGUF files instead.

```
./main -t 10 -ngl 32 -m llama2_7b_chat_uncensored.ggmlv3.q4_K_M.bin --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "### HUMAN:\n{prompt}\n\n### RESPONSE:"
```
Change `-t 10` to the number of physical CPU cores you have. For example if your system has 8 cores/16 threads, use `-t 8`.

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 2048` to the desired sequence length for this model. For example, `-c 4096` for a Llama 2 model.  For models that use RoPE, add `--rope-freq-base 10000 --rope-freq-scale 0.5` for doubled context, or `--rope-freq-base 10000 --rope-freq-scale 0.25` for 4x context.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions here: [text-generation-webui/docs/llama.cpp.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/llama.cpp.md).

<!-- footer start -->
<!-- 200823 -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[TheBloke AI's Discord server](https://discord.gg/theblokeai)

## Thanks, and how to contribute

Thanks to the [chirper.ai](https://chirper.ai) team!

Thanks to Clay from [gpus.llm-utils.org](llm-utils)!

I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.

Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.

* Patreon: https://patreon.com/TheBlokeAI
* Ko-Fi: https://ko-fi.com/TheBlokeAI

**Special thanks to**: Aemon Algiz.

**Patreon special mentions**: Russ Johnson, J, alfie_i, Alex, NimbleBox.ai, Chadd, Mandus, Nikolai Manek, Ken Nordquist, ya boyyy, Illia Dulskyi, Viktor Bowallius, vamX, Iucharbius, zynix, Magnesian, Clay Pascal, Pierre Kircher, Enrico Ros, Tony Hughes, Elle, Andrey, knownsqashed, Deep Realms, Jerry Meng, Lone Striker, Derek Yates, Pyrater, Mesiah Bishop, James Bentley, Femi Adebogun, Brandon Frisco, SuperWojo, Alps Aficionado, Michael Dempsey, Vitor Caleffi, Will Dee, Edmond Seymore, usrbinkat, LangChain4j, Kacper Wikieł, Luke Pendergrass, John Detwiler, theTransient, Nathan LeClaire, Tiffany J. Kim, biorpg, Eugene Pentland, Stanislav Ovsiannikov, Fred von Graf, terasurfer, Kalila, Dan Guido, Nitin Borwankar, 阿明, Ai Maven, John Villwock, Gabriel Puliatti, Stephen Murray, Asp the Wyvern, danny, Chris Smitley, ReadyPlayerEmma, S_X, Daniel P. Andersen, Olakabola, Jeffrey Morgan, Imad Khwaja, Caitlyn Gatomon, webtim, Alicia Loh, Trenton Dambrowitz, Swaroop Kallakuri, Erik Bjäreholt, Leonard Tan, Spiking Neurons AB, Luke @flexchar, Ajan Kanaga, Thomas Belote, Deo Leter, RoA, Willem Michiel, transmissions 11, subjectnull, Matthew Berman, Joseph William Delisle, David Ziegler, Michael Davis, Johann-Peter Hartmann, Talal Aujan, senxiiz, Artur Olbinski, Rainer Wilmers, Spencer Kim, Fen Risland, Cap'n Zoog, Rishabh Srivastava, Michael Levine, Geoffrey Montalvo, Sean Connelly, Alexandros Triantafyllidis, Pieter, Gabriel Tamborski, Sam, Subspace Studios, Junyu Yang, Pedro Madruga, Vadim, Cory Kujawski, K, Raven Klaugh, Randy H, Mano Prime, Sebastain Graf, Space Cruiser


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->

# Original model card: George Sung's Llama2 7B Chat Uncensored


# Overview
Fine-tuned [Llama-2 7B](https://huggingface.co/TheBloke/Llama-2-7B-fp16) with an uncensored/unfiltered Wizard-Vicuna conversation dataset [ehartford/wizard_vicuna_70k_unfiltered](https://huggingface.co/datasets/ehartford/wizard_vicuna_70k_unfiltered).
Used QLoRA for fine-tuning. Trained for one epoch on a 24GB GPU (NVIDIA A10G) instance, took ~19 hours to train.

The version here is the fp16 HuggingFace model.

## GGML & GPTQ versions
Thanks to [TheBloke](https://huggingface.co/TheBloke), he has created the GGML and GPTQ versions:
* https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML
* https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GPTQ

# Prompt style
The model was trained with the following prompt style:
```
### HUMAN:
Hello

### RESPONSE:
Hi, how are you?

### HUMAN:
I'm fine.

### RESPONSE:
How can I help you?
...
```

# Training code
Code used to train the model is available [here](https://github.com/georgesung/llm_qlora).

To reproduce the results:
```
git clone https://github.com/georgesung/llm_qlora
cd llm_qlora
pip install -r requirements.txt
python train.py configs/llama2_7b_chat_uncensored.yaml
```

# Fine-tuning guide
https://georgesung.github.io/ai/qlora-ift/
