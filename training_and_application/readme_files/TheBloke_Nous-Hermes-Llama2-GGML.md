---
language:
- en
license: llama2
tags:
- llama-2
- self-instruct
- distillation
- synthetic instruction
model_name: Nous Hermes Llama 2 13B
inference: false
model_creator: NousResearch
model_link: https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b
model_type: llama
quantized_by: TheBloke
base_model: NousResearch/Nous-Hermes-Llama2-13b
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

# Nous Hermes Llama 2 13B - GGML
- Model creator: [NousResearch](https://huggingface.co/NousResearch)
- Original model: [Nous Hermes Llama 2 13B](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b)

## Description

This repo contains GGML format model files for [Nous Research's Nous Hermes Llama 2 13B](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b).

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

* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGUF)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU+GPU inference (deprecated)](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML)
* [NousResearch's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b)

## Prompt template: Alpaca

```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

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
| [nous-hermes-llama2-13b.ggmlv3.q2_K.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q2_K.bin) | q2_K | 2 | 5.74 GB| 8.24 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.vw and feed_forward.w2 tensors, GGML_TYPE_Q2_K for the other tensors. |
| [nous-hermes-llama2-13b.ggmlv3.q3_K_S.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q3_K_S.bin) | q3_K_S | 3 | 5.87 GB| 8.37 GB | New k-quant method. Uses GGML_TYPE_Q3_K for all tensors |
| [nous-hermes-llama2-13b.ggmlv3.q3_K_M.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q3_K_M.bin) | q3_K_M | 3 | 6.53 GB| 9.03 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| [nous-hermes-llama2-13b.ggmlv3.q3_K_L.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q3_K_L.bin) | q3_K_L | 3 | 7.14 GB| 9.64 GB | New k-quant method. Uses GGML_TYPE_Q5_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| [nous-hermes-llama2-13b.ggmlv3.q4_0.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q4_0.bin) | q4_0 | 4 | 7.32 GB| 9.82 GB | Original quant method, 4-bit. |
| [nous-hermes-llama2-13b.ggmlv3.q4_K_S.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q4_K_S.bin) | q4_K_S | 4 | 7.56 GB| 10.06 GB | New k-quant method. Uses GGML_TYPE_Q4_K for all tensors |
| [nous-hermes-llama2-13b.ggmlv3.q4_K_M.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q4_K_M.bin) | q4_K_M | 4 | 8.06 GB| 10.56 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q4_K |
| [nous-hermes-llama2-13b.ggmlv3.q4_1.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q4_1.bin) | q4_1 | 4 | 8.14 GB| 10.64 GB | Original quant method, 4-bit. Higher accuracy than q4_0 but not as high as q5_0. However has quicker inference than q5 models. |
| [nous-hermes-llama2-13b.ggmlv3.q5_0.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q5_0.bin) | q5_0 | 5 | 8.95 GB| 11.45 GB | Original quant method, 5-bit. Higher accuracy, higher resource usage and slower inference. |
| [nous-hermes-llama2-13b.ggmlv3.q5_K_S.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q5_K_S.bin) | q5_K_S | 5 | 9.15 GB| 11.65 GB | New k-quant method. Uses GGML_TYPE_Q5_K for all tensors |
| [nous-hermes-llama2-13b.ggmlv3.q5_K_M.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q5_K_M.bin) | q5_K_M | 5 | 9.40 GB| 11.90 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q5_K |
| [nous-hermes-llama2-13b.ggmlv3.q5_1.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q5_1.bin) | q5_1 | 5 | 9.76 GB| 12.26 GB | Original quant method, 5-bit. Even higher accuracy, resource usage and slower inference. |
| [nous-hermes-llama2-13b.ggmlv3.q6_K.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q6_K.bin) | q6_K | 6 | 10.83 GB| 13.33 GB | New k-quant method. Uses GGML_TYPE_Q8_K for all tensors - 6-bit quantization |
| [nous-hermes-llama2-13b.ggmlv3.q8_0.bin](https://huggingface.co/TheBloke/Nous-Hermes-Llama2-GGML/blob/main/nous-hermes-llama2-13b.ggmlv3.q8_0.bin) | q8_0 | 8 | 13.83 GB| 16.33 GB | Original quant method, 8-bit. Almost indistinguishable from float16. High resource use and slow. Not recommended for most users. |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

## How to run in `llama.cpp`

Make sure you are using `llama.cpp` from commit [dadbed99e65252d79f81101a392d0d6497b86caa](https://github.com/ggerganov/llama.cpp/commit/dadbed99e65252d79f81101a392d0d6497b86caa) or earlier.

For compatibility with latest llama.cpp, please use GGUF files instead.

```
./main -t 10 -ngl 32 -m nous-hermes-llama2-13b.ggmlv3.q4_K_M.bin --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{prompt}\n\n### Response:"
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

# Original model card: Nous Research's Nous Hermes Llama 2 13B


# Model Card: Nous-Hermes-Llama2-13b

Compute provided by our project sponsor Redmond AI, thank you! Follow RedmondAI on Twitter @RedmondAI.

## Model Description

Nous-Hermes-Llama2-13b is a state-of-the-art language model fine-tuned on over 300,000 instructions. This model was fine-tuned by Nous Research, with Teknium and Emozilla leading the fine tuning process and dataset curation, Redmond AI sponsoring the compute, and several other contributors.

This Hermes model uses the exact same dataset as Hermes on Llama-1. This is to ensure consistency between the old Hermes and new, for anyone who wanted to keep Hermes as similar to the old one, just more capable.

This model stands out for its long responses, lower hallucination rate, and absence of OpenAI censorship mechanisms. The fine-tuning process was performed with a 4096 sequence length on an 8x a100 80GB DGX machine.

## Example Outputs:
![Example4](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b/resolve/main/example5.png "Example 4")
![Example1](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b/resolve/main/Example1.png "Example 1")
![Example2](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b/resolve/main/example2.png "Example 2")
![Example3](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b/resolve/main/example3.png "Example 3")

## Model Training

The model was trained almost entirely on synthetic GPT-4 outputs. Curating high quality GPT-4 datasets enables incredibly high quality in knowledge, task completion, and style.

This includes data from diverse sources such as GPTeacher, the general, roleplay v1&2, code instruct datasets, Nous Instruct & PDACTL (unpublished), and several others, detailed further below

## Collaborators
The model fine-tuning and the datasets were a collaboration of efforts and resources between Teknium, Karan4D, Emozilla, Huemin Art, and Redmond AI. 
  
Special mention goes to @winglian for assisting in some of the training issues.

Huge shoutout and acknowledgement is deserved for all the dataset creators who generously share their datasets openly. 

Among the contributors of datasets:
- GPTeacher was made available by Teknium
- Wizard LM by nlpxucan
- Nous Research Instruct Dataset was provided by Karan4D and HueminArt.  
- GPT4-LLM and Unnatural Instructions were provided by Microsoft
- Airoboros dataset by jondurbin
- Camel-AI's domain expert datasets are from Camel-AI
- CodeAlpaca dataset by Sahil 2801.

If anyone was left out, please open a thread in the community tab.

## Prompt Format

The model follows the Alpaca prompt format:
```
### Instruction:
<prompt>

### Response:
<leave a newline blank for model to respond>

```

or 

```
### Instruction:
<prompt>

### Input:
<additional context>

### Response:
<leave a newline blank for model to respond>

```  

## Benchmark Results
AGI-Eval
```
|             Task             |Version| Metric |Value |   |Stderr|
|agieval_aqua_rat              |      0|acc     |0.2362|±  |0.0267|
|                              |       |acc_norm|0.2480|±  |0.0272|
|agieval_logiqa_en             |      0|acc     |0.3425|±  |0.0186|
|                              |       |acc_norm|0.3472|±  |0.0187|
|agieval_lsat_ar               |      0|acc     |0.2522|±  |0.0287|
|                              |       |acc_norm|0.2087|±  |0.0269|
|agieval_lsat_lr               |      0|acc     |0.3510|±  |0.0212|
|                              |       |acc_norm|0.3627|±  |0.0213|
|agieval_lsat_rc               |      0|acc     |0.4647|±  |0.0305|
|                              |       |acc_norm|0.4424|±  |0.0303|
|agieval_sat_en                |      0|acc     |0.6602|±  |0.0331|
|                              |       |acc_norm|0.6165|±  |0.0340|
|agieval_sat_en_without_passage|      0|acc     |0.4320|±  |0.0346|
|                              |       |acc_norm|0.4272|±  |0.0345|
|agieval_sat_math              |      0|acc     |0.2909|±  |0.0307|
|                              |       |acc_norm|0.2727|±  |0.0301|
```
GPT-4All Benchmark Set
```
|    Task     |Version| Metric |Value |   |Stderr|
|arc_challenge|      0|acc     |0.5102|±  |0.0146|
|             |       |acc_norm|0.5213|±  |0.0146|
|arc_easy     |      0|acc     |0.7959|±  |0.0083|
|             |       |acc_norm|0.7567|±  |0.0088|
|boolq        |      1|acc     |0.8394|±  |0.0064|
|hellaswag    |      0|acc     |0.6164|±  |0.0049|
|             |       |acc_norm|0.8009|±  |0.0040|
|openbookqa   |      0|acc     |0.3580|±  |0.0215|
|             |       |acc_norm|0.4620|±  |0.0223|
|piqa         |      0|acc     |0.7992|±  |0.0093|
|             |       |acc_norm|0.8069|±  |0.0092|
|winogrande   |      0|acc     |0.7127|±  |0.0127|
```
BigBench Reasoning Test
```
|                      Task                      |Version|       Metric        |Value |   |Stderr|

|bigbench_causal_judgement                       |      0|multiple_choice_grade|0.5526|±  |0.0362|
|bigbench_date_understanding                     |      0|multiple_choice_grade|0.7344|±  |0.0230|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|0.2636|±  |0.0275|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|0.0195|±  |0.0073|
|                                                |       |exact_str_match      |0.0000|±  |0.0000|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|0.2760|±  |0.0200|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|0.2100|±  |0.0154|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|0.4400|±  |0.0287|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|0.2440|±  |0.0192|
|bigbench_navigate                               |      0|multiple_choice_grade|0.4950|±  |0.0158|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|0.5570|±  |0.0111|
|bigbench_ruin_names                             |      0|multiple_choice_grade|0.3728|±  |0.0229|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|0.1854|±  |0.0123|
|bigbench_snarks                                 |      0|multiple_choice_grade|0.6298|±  |0.0360|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|0.6156|±  |0.0155|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|0.3140|±  |0.0147|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|0.2032|±  |0.0114|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|0.1406|±  |0.0083|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|0.4400|±  |0.0287|
```

These are the highest benchmarks Hermes has seen on every metric, achieving the following average scores:
- GPT4All benchmark average is now 70.0 - from 68.8 in Hermes-Llama1
- 0.3657 on BigBench, up from 0.328 on hermes-llama1
- 0.372 on AGIEval, up from 0.354 on Hermes-llama1

These benchmarks currently have us at #1 on ARC-c, ARC-e, Hellaswag, and OpenBookQA, and 2nd place on Winogrande, comparing to GPT4all's benchmarking list, supplanting Hermes 1 for the new top position. 

## Resources for Applied Use Cases:
Check out LM Studio for a nice chatgpt style interface here: https://lmstudio.ai/
For an example of a back and forth chatbot using huggingface transformers and discord, check out: https://github.com/teknium1/alpaca-discord  
For an example of a roleplaying discord chatbot, check out this: https://github.com/teknium1/alpaca-roleplay-discordbot  

## Future Plans
We plan to continue to iterate on both more high quality data, and new data filtering techniques to eliminate lower quality data going forward. 

## Model Usage
The model is available for download on Hugging Face. It is suitable for a wide range of language tasks, from generating creative text to understanding and following complex instructions.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
