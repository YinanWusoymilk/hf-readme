---
language:
- en
license: llama2
model_name: MythoMax L2 13B
inference: false
model_creator: Gryphe
model_link: https://huggingface.co/Gryphe/MythoMax-L2-13b
model_type: llama
quantized_by: TheBloke
base_model: Gryphe/MythoMax-L2-13b
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

# MythoMax L2 13B - GGML
- Model creator: [Gryphe](https://huggingface.co/Gryphe)
- Original model: [MythoMax L2 13B](https://huggingface.co/Gryphe/MythoMax-L2-13b)

## Description

This repo contains GGML format model files for [Gryphe's MythoMax L2 13B](https://huggingface.co/Gryphe/MythoMax-L2-13b).

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

* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/MythoMax-L2-13B-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGUF)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU+GPU inference (deprecated)](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML)
* [Gryphe's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/Gryphe/MythoMax-L2-13b)

## Prompt template: Custom

```
{system_message}

### Instruction:
{prompt}
(For roleplay purposes, I suggest the following - Write <CHAR NAME>'s next reply in a chat between <YOUR NAME> and <CHAR NAME>. Write a single reply only.)

### Response:

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
| [mythomax-l2-13b.ggmlv3.q2_K.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q2_K.bin) | q2_K | 2 | 5.51 GB| 8.01 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.vw and feed_forward.w2 tensors, GGML_TYPE_Q2_K for the other tensors. |
| [mythomax-l2-13b.ggmlv3.q3_K_S.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q3_K_S.bin) | q3_K_S | 3 | 5.66 GB| 8.16 GB | New k-quant method. Uses GGML_TYPE_Q3_K for all tensors |
| [mythomax-l2-13b.ggmlv3.q3_K_M.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q3_K_M.bin) | q3_K_M | 3 | 6.31 GB| 8.81 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| [mythomax-l2-13b.ggmlv3.q3_K_L.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q3_K_L.bin) | q3_K_L | 3 | 6.93 GB| 9.43 GB | New k-quant method. Uses GGML_TYPE_Q5_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| [mythomax-l2-13b.ggmlv3.q4_0.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q4_0.bin) | q4_0 | 4 | 7.37 GB| 9.87 GB | Original quant method, 4-bit. |
| [mythomax-l2-13b.ggmlv3.q4_K_S.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q4_K_S.bin) | q4_K_S | 4 | 7.37 GB| 9.87 GB | New k-quant method. Uses GGML_TYPE_Q4_K for all tensors |
| [mythomax-l2-13b.ggmlv3.q4_K_M.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q4_K_M.bin) | q4_K_M | 4 | 7.87 GB| 10.37 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q4_K |
| [mythomax-l2-13b.ggmlv3.q4_1.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q4_1.bin) | q4_1 | 4 | 8.17 GB| 10.67 GB | Original quant method, 4-bit. Higher accuracy than q4_0 but not as high as q5_0. However has quicker inference than q5 models. |
| [mythomax-l2-13b.ggmlv3.q5_0.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q5_0.bin) | q5_0 | 5 | 8.97 GB| 11.47 GB | Original quant method, 5-bit. Higher accuracy, higher resource usage and slower inference. |
| [mythomax-l2-13b.ggmlv3.q5_K_S.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q5_K_S.bin) | q5_K_S | 5 | 8.97 GB| 11.47 GB | New k-quant method. Uses GGML_TYPE_Q5_K for all tensors |
| [mythomax-l2-13b.ggmlv3.q5_K_M.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q5_K_M.bin) | q5_K_M | 5 | 9.23 GB| 11.73 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q5_K |
| [mythomax-l2-13b.ggmlv3.q5_1.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q5_1.bin) | q5_1 | 5 | 9.78 GB| 12.28 GB | Original quant method, 5-bit. Even higher accuracy, resource usage and slower inference. |
| [mythomax-l2-13b.ggmlv3.q6_K.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q6_K.bin) | q6_K | 6 | 10.68 GB| 13.18 GB | New k-quant method. Uses GGML_TYPE_Q8_K for all tensors - 6-bit quantization |
| [mythomax-l2-13b.ggmlv3.q8_0.bin](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML/blob/main/mythomax-l2-13b.ggmlv3.q8_0.bin) | q8_0 | 8 | 13.79 GB| 16.29 GB | Original quant method, 8-bit. Almost indistinguishable from float16. High resource use and slow. Not recommended for most users. |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

## How to run in `llama.cpp`

Make sure you are using `llama.cpp` from commit [dadbed99e65252d79f81101a392d0d6497b86caa](https://github.com/ggerganov/llama.cpp/commit/dadbed99e65252d79f81101a392d0d6497b86caa) or earlier.

For compatibility with latest llama.cpp, please use GGUF files instead.

```
./main -t 10 -ngl 32 -m mythomax-l2-13b.ggmlv3.q4_K_M.bin --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "```\nYou are a story writing assistant.\n\n### Instruction:\nWrite a story about llamas\n(For roleplay purposes, I suggest the following - Write <CHAR NAME>'s next reply in a chat between <YOUR NAME> and <CHAR NAME>. Write a single reply only.)\n\n### Response:\n\n```"
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

## Thanks, and how to contribute.

Thanks to the [chirper.ai](https://chirper.ai) team!

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

# Original model card: Gryphe's MythoMax L2 13B

An improved, potentially even perfected variant of MythoMix, my [MythoLogic-L2](https://huggingface.co/Gryphe/MythoLogic-L2-13b) and [Huginn](https://huggingface.co/The-Face-Of-Goonery/Huginn-13b-FP16) merge using a highly experimental tensor type merge technique. The main difference with MythoMix is that I allowed more of Huginn to intermingle with the single tensors located at the front and end of a model, resulting in increased coherency across the entire structure.

The script and the acccompanying templates I used to produce both can [be found here](https://github.com/Gryphe/BlockMerge_Gradient/tree/main/YAML).

This model is proficient at both roleplaying and storywriting due to its unique nature.

Quantized models are available from TheBloke: [GGML](https://huggingface.co/TheBloke/MythoMax-L2-13B-GGML) - [GPTQ](https://huggingface.co/TheBloke/MythoMax-L2-13B-GPTQ) (You're the best!)

## Model details

The idea behind this merge is that each layer is composed of several tensors, which are in turn responsible for specific functions. Using MythoLogic-L2's robust understanding as its input and Huginn's extensive writing capability as its output seems to have resulted in a model that exceeds at both, confirming my theory. (More details to be released at a later time)

This type of merge is incapable of being illustrated, as each of its 363 tensors had an unique ratio applied to it. As with my prior merges, gradients were part of these ratios to further finetune its behaviour.

## Prompt Format

This model primarily uses Alpaca formatting, so for optimal model performance, use:
```
<System prompt/Character Card>

### Instruction:
Your instruction or question here.
For roleplay purposes, I suggest the following - Write <CHAR NAME>'s next reply in a chat between <YOUR NAME> and <CHAR NAME>. Write a single reply only.

### Response:
```
 
---
license: other
---
