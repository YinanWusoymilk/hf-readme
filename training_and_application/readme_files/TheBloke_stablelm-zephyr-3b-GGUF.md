---
base_model: stabilityai/stablelm-zephyr-3b
datasets:
- HuggingFaceH4/ultrachat_200k
- HuggingFaceH4/ultrafeedback_binarized
- meta-math/MetaMathQA
- WizardLM/WizardLM_evol_instruct_V2_196k
- Intel/orca_dpo_pairs
inference: false
language:
- en
license: other
model_creator: Stability AI
model_name: StableLM Zephyr 3B
model_type: stablelm
prompt_template: '<|user|>

  {prompt}<|endoftext|>

  <|assistant|>

  '
quantized_by: TheBloke
tags:
- causal-lm
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

# StableLM Zephyr 3B - GGUF
- Model creator: [Stability AI](https://huggingface.co/stabilityai)
- Original model: [StableLM Zephyr 3B](https://huggingface.co/stabilityai/stablelm-zephyr-3b)

<!-- description start -->
## Description

This repo contains GGUF format model files for [Stability AI's StableLM Zephyr 3B](https://huggingface.co/stabilityai/stablelm-zephyr-3b).

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

* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF)
* [Stability AI's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/stabilityai/stablelm-zephyr-3b)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: StableLM-Zephyr

```
<|user|>
{prompt}<|endoftext|>
<|assistant|>

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
| [stablelm-zephyr-3b.Q2_K.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q2_K.gguf) | Q2_K | 2 | 1.20 GB| 3.70 GB | smallest, significant quality loss - not recommended for most purposes |
| [stablelm-zephyr-3b.Q3_K_S.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q3_K_S.gguf) | Q3_K_S | 3 | 1.25 GB| 3.75 GB | very small, high quality loss |
| [stablelm-zephyr-3b.Q3_K_M.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q3_K_M.gguf) | Q3_K_M | 3 | 1.39 GB| 3.89 GB | very small, high quality loss |
| [stablelm-zephyr-3b.Q3_K_L.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q3_K_L.gguf) | Q3_K_L | 3 | 1.51 GB| 4.01 GB | small, substantial quality loss |
| [stablelm-zephyr-3b.Q4_0.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q4_0.gguf) | Q4_0 | 4 | 1.61 GB| 4.11 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [stablelm-zephyr-3b.Q4_K_S.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q4_K_S.gguf) | Q4_K_S | 4 | 1.62 GB| 4.12 GB | small, greater quality loss |
| [stablelm-zephyr-3b.Q4_K_M.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q4_K_M.gguf) | Q4_K_M | 4 | 1.71 GB| 4.21 GB | medium, balanced quality - recommended |
| [stablelm-zephyr-3b.Q5_0.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q5_0.gguf) | Q5_0 | 5 | 1.94 GB| 4.44 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [stablelm-zephyr-3b.Q5_K_S.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q5_K_S.gguf) | Q5_K_S | 5 | 1.94 GB| 4.44 GB | large, low quality loss - recommended |
| [stablelm-zephyr-3b.Q5_K_M.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q5_K_M.gguf) | Q5_K_M | 5 | 1.99 GB| 4.49 GB | large, very low quality loss - recommended |
| [stablelm-zephyr-3b.Q6_K.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q6_K.gguf) | Q6_K | 6 | 2.30 GB| 4.80 GB | very large, extremely low quality loss |
| [stablelm-zephyr-3b.Q8_0.gguf](https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/blob/main/stablelm-zephyr-3b.Q8_0.gguf) | Q8_0 | 8 | 2.97 GB| 5.47 GB | very large, extremely low quality loss - not recommended |

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

Under Download Model, you can enter the model repo: TheBloke/stablelm-zephyr-3b-GGUF and below it, a specific filename to download, such as: stablelm-zephyr-3b.Q4_K_M.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download TheBloke/stablelm-zephyr-3b-GGUF stablelm-zephyr-3b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage (click to read)</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download TheBloke/stablelm-zephyr-3b-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/stablelm-zephyr-3b-GGUF stablelm-zephyr-3b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 35 -m stablelm-zephyr-3b.Q4_K_M.gguf --color -c 4096 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "<|user|>\n{prompt}<|endoftext|>\n<|assistant|>"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 4096` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically. Note that longer sequence lengths require much more resources, so you may need to reduce this value.

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
  model_path="./stablelm-zephyr-3b.Q4_K_M.gguf",  # Download the model file first
  n_ctx=4096,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
)

# Simple inference example
output = llm(
  "<|user|>\n{prompt}<|endoftext|>\n<|assistant|>", # Prompt
  max_tokens=512,  # Generate up to 512 tokens
  stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
  echo=True        # Whether to echo the prompt
)

# Chat Completion API

llm = Llama(model_path="./stablelm-zephyr-3b.Q4_K_M.gguf", chat_format="llama-2")  # Set chat_format according to the model you are using
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
# Original model card: Stability AI's StableLM Zephyr 3B

# `StableLM Zephyr 3B`

## Model Description

`StableLM Zephyr 3B` is a 3 billion parameter instruction tuned inspired by [HugginFaceH4's Zephyr 7B](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) training pipeline this model was trained on a mix of publicly available datasets, synthetic datasets using [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290), evaluation for this model based on
[MT Bench](https://tatsu-lab.github.io/alpaca_eval/) and [Alpaca Benchmark](https://tatsu-lab.github.io/alpaca_eval/)

## Usage

`StableLM Zephyr 3B` uses the following instruction format:
```
<|user|>
List 3 synonyms for the word "tiny"<|endoftext|>
<|assistant|>
1. Dwarf
2. Little
3. Petite<|endoftext|>
```

This format is also available through the tokenizer's `apply_chat_template` method:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('stabilityai/stablelm-zephyr-3b')
model = AutoModelForCausalLM.from_pretrained(
    'stabilityai/stablelm-zephyr-3b',
    trust_remote_code=True,
    device_map="auto"
)

prompt = [{'role': 'user', 'content': 'List 3 synonyms for the word "tiny"'}]
inputs = tokenizer.apply_chat_template(
    prompt,
    add_generation_prompt=True,
    return_tensors='pt'
)

tokens = model.generate(
    inputs.to(model.device),
    max_new_tokens=1024,
    temperature=0.8,
    do_sample=True
)

print(tokenizer.decode(tokens[0], skip_special_tokens=False))
```

You can also see how to run a performance optimized version of this model [here](https://github.com/eaidova/openvino_notebooks/blob/ea/stateful_chatbot/notebooks/273-stable-zephyr-3b-chatbot/273-stable-zephyr-3b-chatbot.ipynb) using [OpenVINO](https://docs.openvino.ai/2023.2/home.html) from Intel.

## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: `StableLM Zephyr 3B` model is an auto-regressive language model based on the transformer decoder architecture.
* **Language(s)**: English
* **Library**: [Alignment Handbook](https://github.com/huggingface/alignment-handbook.git)
* **Finetuned from model**: [stabilityai/stablelm-3b-4e1t](https://huggingface.co/stabilityai/stablelm-3b-4e1t)
* **License**: [StabilityAI Non-Commercial Research Community License](https://huggingface.co/stabilityai/stablelm-zephyr-3b/raw/main/LICENSE)
* **Contact**: For questions and comments about the model, please email `lm@stability.ai`

### Training Dataset

The dataset is comprised of a mixture of open datasets large-scale datasets available on the [HuggingFace Hub](https://huggingface.co/datasets):
1. SFT Datasets
- HuggingFaceH4/ultrachat_200k
- meta-math/MetaMathQA
- WizardLM/WizardLM_evol_instruct_V2_196k
- Open-Orca/SlimOrca
2. Preference Datasets:
- HuggingFaceH4/ultrafeedback_binarized
- Intel/orca_dpo_pairs

## Performance

### MT-Bench and Alpaca Bench


<img src="https://cdn-uploads.huggingface.co/production/uploads/6310474ca119d49bc1eb0d80/8WIZS6dAlu5kSH-382pMl.png" alt="mt_bench_plot" width="600"/>

| Model | Size | Alignment | MT-Bench (score) | AlpacaEval (win rate %) |
|-------------|-----|----|---------------|--------------|
| **StableLM Zephyr 3B** 🪁 | 3B | DPO | 6.64 | 76.00 |
| StableLM Zephyr (SFT only) | 3B | SFT | 6.04 | 71.15 |
| Capybara v1.9 | 3B | dSFT | 5.94 | - |
| MPT-Chat |  7B |dSFT |5.42| -|
| Xwin-LM v0.1 | 7B| dPPO| 6.19| 87.83|
| Mistral-Instruct v0.1 | 7B|  - | 6.84 |-|
| Zephyr-7b-α |7B|  dDPO| 6.88| -|
| Zephyr-7b-β| 7B | dDPO | 7.34 | 90.60 |
| Falcon-Instruct |  40B |dSFT |5.17 |45.71|
| Guanaco | 65B |  SFT |6.41| 71.80|
| Llama2-Chat |  70B |RLHF |6.86| 92.66|
| Vicuna v1.3 |  33B |dSFT |7.12 |88.99|
| WizardLM v1.0 |  70B |dSFT |7.71 |-|
| Xwin-LM v0.1 |   70B |dPPO |- |95.57|
| GPT-3.5-turbo | - |RLHF |7.94 |89.37|
| Claude 2 |  - |RLHF |8.06| 91.36|
| GPT-4 |  -| RLHF |8.99| 95.28|

## Other benchmarks:
| Task                | Value                     |
|-----------------------|---------------------------|
| ARC (25-shot)         |  47.0       |
| HellaSwag (10-shot)   | 74.2    |
| MMLU (5-shot)        |   46.3     |
| TruthfulQA (0-shot)   |   46.5 |
| Winogrande (5-shot)   |   65.5 |
| GSM8K (5-shot)        | 42.3        |
| BigBench (Avg) | 35.26 |
| AGI Benchmark (Avg) | 33.23 |

### Training Infrastructure

* **Hardware**: `StableLM Zephyr 3B` was trained on the Stability AI cluster across 8 nodes with 8 A100 80GBs GPUs for each nodes.
* **Code Base**: We use our internal script for SFT steps and used [HuggingFace Alignment Handbook script](https://github.com/huggingface/alignment-handbook) for DPO training.

## Commitment to Ethical AI
In line with our responsibility towards ethical AI development, `StableLM Zephyr 3B` is released with a focus on ensuring safety, reliability, and appropriateness in its applications. To this end, we have evaluated `StableLM Zephyr 3B` on 488 malicious prompts and used standard protocols to assess the harmfulness of its outputs. Compared to Zephyr-7b-β, `StableLM Zephyr 3B` reduces the number of harmful outputs as assessed by GPT-4 by 55. Additionally, we performed an internal red teaming event targeting the following abuse areas:
* **Self-Harm Methods**: (Suicide Methods, Encouragement of Self-Harm, Methods and encouragement of Eating Disorders)
* **Misinformation**: (Health, Conspiracy Theories, Social Unrest/Conflict, Political Misinformation, & Climate change)
* **Hate Speech**: (Race, Stereotypes, Immigrants, Gender,  Personally Identifiable Information such as Social security numbers, Full names, ID numbers, Email addresses, and telephone numbers)

We have incorporated the findings of our malicious prompts evaluation and red teaming event into our release. Users are encouraged to fine-tune and evaluate the model to suit their specific needs, considering the potential biases and limitations found in `StableLM Zephyr 3B` and inherent in other LLM models.

## Use and Limitations

### Intended Use

The model is intended to be used as a foundational base model for application-specific fine-tuning. Developers must evaluate and fine-tune the model for safe performance in downstream applications.

### Limitations and Bias
​
This model is not trained against adversarial inputs. We strongly recommend pairing this model with an input and output classifier to prevent harmful responses.

Through our internal red teaming, we discovered that while the model will not output harmful information if not prompted to do so, it is willing to output potentially harmful outputs or misinformation when the user requests it. Using this model will require guardrails around your inputs and outputs to ensure that any outputs returned are not misinformation or harmful. Additionally, as each use case is unique, we recommend running your own suite of tests to ensure proper performance of this model. Finally, do not use the models if they are unsuitable for your application, or for any applications that may cause deliberate or unintentional harm to others.

<!-- original-model-card end -->
