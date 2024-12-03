---
base_model: ise-uiuc/Magicoder-S-DS-6.7B
datasets:
- ise-uiuc/Magicoder-OSS-Instruct-75K
- ise-uiuc/Magicoder-Evol-Instruct-110K
inference: false
library_name: transformers
license: other
license_name: deepseek
model_creator: Intellligent Software Engineering (iSE
model_name: Magicoder S DS 6.7B
model_type: deepseek
pipeline_tag: text-generation
prompt_template: 'You are an exceptionally intelligent coding assistant that consistently
  delivers accurate and reliable responses to user instructions.


  @@ Instruction

  {prompt}


  @@ Response

  '
quantized_by: TheBloke
---
<!-- markdownlint-disable MD041 -->

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

# Magicoder S DS 6.7B - GGUF
- Model creator: [Intellligent Software Engineering (iSE](https://huggingface.co/ise-uiuc)
- Original model: [Magicoder S DS 6.7B](https://huggingface.co/ise-uiuc/Magicoder-S-DS-6.7B)

<!-- description start -->
## Description

This repo contains GGUF format model files for [Intellligent Software Engineering (iSE's Magicoder S DS 6.7B](https://huggingface.co/ise-uiuc/Magicoder-S-DS-6.7B).

These files were quantised using hardware kindly provided by [Massed Compute](https://massedcompute.com/).

<!-- description end -->
<!-- README_GGUF.md-about-gguf start -->
### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.

Here is an incomplete list of clients and libraries that are known to support GGUF:

* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for GGUF. Offers a CLI and a server option.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [GPT4All](https://gpt4all.io/index.html), a free and open source local running GUI, supporting Windows, Linux and macOS with full GPU accel.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration. Linux available, in beta as of 27/11/2023.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server. Note, as of time of writing (November 27th 2023), ctransformers has not been updated in a long time and does not support many recent models.

<!-- README_GGUF.md-about-gguf end -->
<!-- repositories-available start -->
## Repositories available

* [AWQ model(s) for GPU inference.](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF)
* [Intellligent Software Engineering (iSE's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/ise-uiuc/Magicoder-S-DS-6.7B)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: Magicoder

```
You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.

@@ Instruction
{prompt}

@@ Response

```

<!-- prompt-template end -->


<!-- compatibility_gguf start -->
## Compatibility

These quantised GGUFv2 files are compatible with llama.cpp from August 27th onwards, as of commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221)

They are also compatible with many third party UIs and libraries - please see the list at the top of this README.

## Explanation of quantisation methods

<details>
  <summary>Click to see details</summary>

The new methods available are:

* GGML_TYPE_Q2_K - "type-1" 2-bit quantization in super-blocks containing 16 blocks, each block having 16 weight. Block scales and mins are quantized with 4 bits. This ends up effectively using 2.5625 bits per weight (bpw)
* GGML_TYPE_Q3_K - "type-0" 3-bit quantization in super-blocks containing 16 blocks, each block having 16 weights. Scales are quantized with 6 bits. This end up using 3.4375 bpw.
* GGML_TYPE_Q4_K - "type-1" 4-bit quantization in super-blocks containing 8 blocks, each block having 32 weights. Scales and mins are quantized with 6 bits. This ends up using 4.5 bpw.
* GGML_TYPE_Q5_K - "type-1" 5-bit quantization. Same super-block structure as GGML_TYPE_Q4_K resulting in 5.5 bpw
* GGML_TYPE_Q6_K - "type-0" 6-bit quantization. Super-blocks with 16 blocks, each block having 16 weights. Scales are quantized with 8 bits. This ends up using 6.5625 bpw

Refer to the Provided Files table below to see what files use which methods, and how.
</details>
<!-- compatibility_gguf end -->

<!-- README_GGUF.md-provided-files start -->
## Provided files

| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| [magicoder-s-ds-6.7b.Q2_K.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q2_K.gguf) | Q2_K | 2 | 2.83 GB| 5.33 GB | smallest, significant quality loss - not recommended for most purposes |
| [magicoder-s-ds-6.7b.Q3_K_S.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q3_K_S.gguf) | Q3_K_S | 3 | 2.95 GB| 5.45 GB | very small, high quality loss |
| [magicoder-s-ds-6.7b.Q3_K_M.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q3_K_M.gguf) | Q3_K_M | 3 | 3.30 GB| 5.80 GB | very small, high quality loss |
| [magicoder-s-ds-6.7b.Q3_K_L.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q3_K_L.gguf) | Q3_K_L | 3 | 3.60 GB| 6.10 GB | small, substantial quality loss |
| [magicoder-s-ds-6.7b.Q4_0.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q4_0.gguf) | Q4_0 | 4 | 3.83 GB| 6.33 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [magicoder-s-ds-6.7b.Q4_K_S.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q4_K_S.gguf) | Q4_K_S | 4 | 3.86 GB| 6.36 GB | small, greater quality loss |
| [magicoder-s-ds-6.7b.Q4_K_M.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q4_K_M.gguf) | Q4_K_M | 4 | 4.08 GB| 6.58 GB | medium, balanced quality - recommended |
| [magicoder-s-ds-6.7b.Q5_0.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q5_0.gguf) | Q5_0 | 5 | 4.65 GB| 7.15 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [magicoder-s-ds-6.7b.Q5_K_S.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q5_K_S.gguf) | Q5_K_S | 5 | 4.65 GB| 7.15 GB | large, low quality loss - recommended |
| [magicoder-s-ds-6.7b.Q5_K_M.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q5_K_M.gguf) | Q5_K_M | 5 | 4.79 GB| 7.29 GB | large, very low quality loss - recommended |
| [magicoder-s-ds-6.7b.Q6_K.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q6_K.gguf) | Q6_K | 6 | 5.53 GB| 8.03 GB | very large, extremely low quality loss |
| [magicoder-s-ds-6.7b.Q8_0.gguf](https://huggingface.co/TheBloke/Magicoder-S-DS-6.7B-GGUF/blob/main/magicoder-s-ds-6.7b.Q8_0.gguf) | Q8_0 | 8 | 7.16 GB| 9.66 GB | very large, extremely low quality loss - not recommended |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.



<!-- README_GGUF.md-provided-files end -->

<!-- README_GGUF.md-how-to-download start -->
## How to download GGUF files

**Note for manual downloaders:** You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single file.

The following clients/libraries will automatically download models for you, providing a list of available models to choose from:

* LM Studio
* LoLLMS Web UI
* Faraday.dev

### In `text-generation-webui`

Under Download Model, you can enter the model repo: TheBloke/Magicoder-S-DS-6.7B-GGUF and below it, a specific filename to download, such as: magicoder-s-ds-6.7b.Q4_K_M.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download TheBloke/Magicoder-S-DS-6.7B-GGUF magicoder-s-ds-6.7b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage (click to read)</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download TheBloke/Magicoder-S-DS-6.7B-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/Magicoder-S-DS-6.7B-GGUF magicoder-s-ds-6.7b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 35 -m magicoder-s-ds-6.7b.Q4_K_M.gguf --color -c 16384 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.\n\n@@ Instruction\n{prompt}\n\n@@ Response"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 16384` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically. Note that longer sequence lengths require much more resources, so you may need to reduce this value.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions can be found in the text-generation-webui documentation, here: [text-generation-webui/docs/04 ‐ Model Tab.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/04%20%E2%80%90%20Model%20Tab.md#llamacpp).

## How to run from Python code

You can use GGUF models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) or [ctransformers](https://github.com/marella/ctransformers) libraries. Note that at the time of writing (Nov 27th 2023), ctransformers has not been updated for some time and is not compatible with some recent models. Therefore I recommend you use llama-cpp-python.

### How to load this model in Python code, using llama-cpp-python

For full documentation, please see: [llama-cpp-python docs](https://abetlen.github.io/llama-cpp-python/).

#### First install the package

Run one of the following commands, according to your system:

```shell
# Base ctransformers with no GPU acceleration
pip install llama-cpp-python
# With NVidia CUDA acceleration
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
# Or with OpenBLAS acceleration
CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
# Or with CLBLast acceleration
CMAKE_ARGS="-DLLAMA_CLBLAST=on" pip install llama-cpp-python
# Or with AMD ROCm GPU acceleration (Linux only)
CMAKE_ARGS="-DLLAMA_HIPBLAS=on" pip install llama-cpp-python
# Or with Metal GPU acceleration for macOS systems only
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python

# In windows, to set the variables CMAKE_ARGS in PowerShell, follow this format; eg for NVidia CUDA:
$env:CMAKE_ARGS = "-DLLAMA_OPENBLAS=on"
pip install llama-cpp-python
```

#### Simple llama-cpp-python example code

```python
from llama_cpp import Llama

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = Llama(
  model_path="./magicoder-s-ds-6.7b.Q4_K_M.gguf",  # Download the model file first
  n_ctx=16384,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
)

# Simple inference example
output = llm(
  "You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.\n\n@@ Instruction\n{prompt}\n\n@@ Response", # Prompt
  max_tokens=512,  # Generate up to 512 tokens
  stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
  echo=True        # Whether to echo the prompt
)

# Chat Completion API

llm = Llama(model_path="./magicoder-s-ds-6.7b.Q4_K_M.gguf", chat_format="llama-2")  # Set chat_format according to the model you are using
llm.create_chat_completion(
    messages = [
        {"role": "system", "content": "You are a story writing assistant."},
        {
            "role": "user",
            "content": "Write a story about llamas."
        }
    ]
)
```

## How to use with LangChain

Here are guides on using llama-cpp-python and ctransformers with LangChain:

* [LangChain + llama-cpp-python](https://python.langchain.com/docs/integrations/llms/llamacpp)
* [LangChain + ctransformers](https://python.langchain.com/docs/integrations/providers/ctransformers)

<!-- README_GGUF.md-how-to-run end -->

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

**Patreon special mentions**: Michael Levine, 阿明, Trailburnt, Nikolai Manek, John Detwiler, Randy H, Will Dee, Sebastain Graf, NimbleBox.ai, Eugene Pentland, Emad Mostaque, Ai Maven, Jim Angel, Jeff Scroggin, Michael Davis, Manuel Alberto Morcote, Stephen Murray, Robert, Justin Joy, Luke @flexchar, Brandon Frisco, Elijah Stavena, S_X, Dan Guido, Undi ., Komninos Chatzipapas, Shadi, theTransient, Lone Striker, Raven Klaugh, jjj, Cap'n Zoog, Michel-Marie MAUDET (LINAGORA), Matthew Berman, David, Fen Risland, Omer Bin Jawed, Luke Pendergrass, Kalila, OG, Erik Bjäreholt, Rooh Singh, Joseph William Delisle, Dan Lewis, TL, John Villwock, AzureBlack, Brad, Pedro Madruga, Caitlyn Gatomon, K, jinyuan sun, Mano Prime, Alex, Jeffrey Morgan, Alicia Loh, Illia Dulskyi, Chadd, transmissions 11, fincy, Rainer Wilmers, ReadyPlayerEmma, knownsqashed, Mandus, biorpg, Deo Leter, Brandon Phillips, SuperWojo, Sean Connelly, Iucharbius, Jack West, Harry Royden McLaughlin, Nicholas, terasurfer, Vitor Caleffi, Duane Dunston, Johann-Peter Hartmann, David Ziegler, Olakabola, Ken Nordquist, Trenton Dambrowitz, Tom X Nguyen, Vadim, Ajan Kanaga, Leonard Tan, Clay Pascal, Alexandros Triantafyllidis, JM33133, Xule, vamX, ya boyyy, subjectnull, Talal Aujan, Alps Aficionado, wassieverse, Ari Malik, James Bentley, Woland, Spencer Kim, Michael Dempsey, Fred von Graf, Elle, zynix, William Richards, Stanislav Ovsiannikov, Edmond Seymore, Jonathan Leane, Martin Kemka, usrbinkat, Enrico Ros


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->

<!-- original-model-card start -->
# Original model card: Intellligent Software Engineering (iSE's Magicoder S DS 6.7B

# 🎩 Magicoder: Source Code Is All You Need

> Refer to our GitHub repo [ise-uiuc/magicoder](https://github.com/ise-uiuc/magicoder/) for an up-to-date introduction to the Magicoder family!

* 🎩**Magicoder** is a model family empowered by 🪄**OSS-Instruct**, a novel approach to enlightening LLMs with open-source code snippets for generating *low-bias* and *high-quality* instruction data for code.
* 🪄**OSS-Instruct** mitigates the *inherent bias* of the LLM-synthesized instruction data by empowering them with *a wealth of open-source references* to produce more diverse, realistic, and controllable data.

![Overview of OSS-Instruct](assets/overview.svg)
![Overview of Result](assets/result.png)

## Model Details

### Model Description

* **Developed by:**
[Yuxiang Wei](https://yuxiang.cs.illinois.edu),
[Zhe Wang](https://github.com/zhewang2001),
[Jiawei Liu](https://jiawei-site.github.io),
[Yifeng Ding](https://yifeng-ding.com),
[Lingming Zhang](https://lingming.cs.illinois.edu)
* **License:** [DeepSeek](https://github.com/deepseek-ai/DeepSeek-Coder/blob/main/LICENSE-MODEL)
* **Finetuned from model:** [deepseek-coder-6.7b-base](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-base)

### Model Sources

* **Repository:** <https://github.com/ise-uiuc/magicoder>
* **Paper:** <https://arxiv.org/abs/2312.02120>
* **Demo (powered by [Gradio](https://www.gradio.app)):**
<https://github.com/ise-uiuc/magicoder/tree/main/demo>

### Training Data

* [Magicoder-OSS-Instruct-75K](https://huggingface.co/datasets/ise-uiuc/Magicoder_oss_instruct_75k): generated through **OSS-Instruct** using `gpt-3.5-turbo-1106` and used to train both Magicoder and Magicoder-S series.
* [Magicoder-Evol-Instruct-110K](https://huggingface.co/datasets/ise-uiuc/Magicoder_evol_instruct_110k): decontaminated and redistributed from [theblackcat102/evol-codealpaca-v1](https://huggingface.co/datasets/theblackcat102/evol-codealpaca-v1), used to further finetune Magicoder series and obtain Magicoder-S models.

## Uses

### Direct Use

Magicoders are designed and best suited for **coding tasks**.

### Out-of-Scope Use

Magicoders may not work well in non-coding tasks.

## Bias, Risks, and Limitations

Magicoders may sometimes make errors, producing misleading contents, or struggle to manage tasks that are not related to coding.

### Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model.

## How to Get Started with the Model

Use the code below to get started with the model. Make sure you installed the [transformers](https://huggingface.co/docs/transformers/index) library.

```python
from transformers import pipeline
import torch

MAGICODER_PROMPT = """You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.

@@ Instruction
{instruction}

@@ Response
"""

instruction = <Your code instruction here>

prompt = MAGICODER_PROMPT.format(instruction=instruction)
generator = pipeline(
    model="ise-uiuc/Magicoder-S-DS-6.7B",
    task="text-generation",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
result = generator(prompt, max_length=1024, num_return_sequences=1, temperature=0.0)
print(result[0]["generated_text"])
```

## Technical Details

Refer to our GitHub repo: [ise-uiuc/magicoder](https://github.com/ise-uiuc/magicoder/).

## Citation

```bibtex
@misc{magicoder,
    title={Magicoder: Source Code Is All You Need},
    author={Yuxiang Wei and Zhe Wang and Jiawei Liu and Yifeng Ding and Lingming Zhang},
    year={2023},
    eprint={2312.02120},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

## Acknowledgements

* [WizardCoder](https://github.com/nlpxucan/WizardLM/tree/main/WizardCoder): Evol-Instruct
* [DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder): Base model for Magicoder-DS
* [CodeLlama](https://ai.meta.com/research/publications/code-llama-open-foundation-models-for-code/): Base model for Magicoder-CL
* [StarCoder](https://arxiv.org/abs/2305.06161): Data decontamination

## Important Note

Magicoder models are trained on the synthetic data generated by OpenAI models. Please pay attention to OpenAI's [terms of use](https://openai.com/policies/terms-of-use) when using the models and the datasets. Magicoders will not compete with OpenAI's commercial products.

<!-- original-model-card end -->
