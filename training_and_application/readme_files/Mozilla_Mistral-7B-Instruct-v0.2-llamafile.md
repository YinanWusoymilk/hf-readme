---
base_model: mistralai/Mistral-7B-Instruct-v0.2
inference: false
license: apache-2.0
model_creator: Mistral AI_
model_name: Mistral 7B Instruct v0.2
model_type: mistral
pipeline_tag: text-generation
prompt_template: |
  <s>[INST] {prompt} [/INST]
quantized_by: jartine
tags:
- finetuned
- llamafile
---

# Mistral 7B Instruct v0.2 - llamafile
- Model creator: [Mistral AI_](https://huggingface.co/mistralai)
- Original model: [Mistral 7B Instruct v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)

<!-- description start -->
## Description

This repo contains llamafile format model files for [Mistral AI_'s Mistral 7B Instruct v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2).

These files were quantised using hardware kindly provided by [Massed Compute](https://massedcompute.com/).

WARNING: This README may contain inaccuracies. It was generated automatically by forking <a href=/TheBloke/Mistral-7B-Instruct-v0.2-GGUF>TheBloke/Mistral-7B-Instruct-v0.2-GGUF</a> and piping the README through sed. Errors should be reported to jartine, and do not reflect TheBloke. You can also support his work on [Patreon](https://www.patreon.com/TheBlokeAI).
<!-- README_llamafile.md-about-llamafile start -->
### About llamafile

llamafile is a new format introduced by Mozilla Ocho on Nov 20th 2023. It uses Cosmopolitan Libc to turn LLM weights into runnable llama.cpp binaries that run on the stock installs of six OSes for both ARM64 and AMD64.

Here is an incomplete list of clients and libraries that are known to support llamafile:

* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for llamafile. Offers a CLI and a server option.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [GPT4All](https://gpt4all.io/index.html), a free and open source local running GUI, supporting Windows, Linux and macOS with full GPU accel.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration. Linux available, in beta as of 27/11/2023.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server. Note, as of time of writing (November 27th 2023), ctransformers has not been updated in a long time and does not support many recent models.

<!-- README_llamafile.md-about-llamafile end -->
<!-- repositories-available start -->
## Repositories available

* [AWQ model(s) for GPU inference.](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit llamafile models for CPU+GPU inference](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile)
* [Mistral AI_'s original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: Mistral

```
<s>[INST] {prompt} [/INST]

```

<!-- prompt-template end -->


<!-- compatibility_llamafile start -->
## Compatibility

These quantised llamafilev2 files are compatible with llama.cpp from August 27th onwards, as of commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221)

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
<!-- compatibility_llamafile end -->

<!-- README_llamafile.md-provided-files start -->
## Provided files

| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| [mistral-7b-instruct-v0.2.Q2_K.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q2_K.llamafile) | Q2_K | 2 | 3.08 GB| 5.58 GB | smallest, significant quality loss - not recommended for most purposes |
| [mistral-7b-instruct-v0.2.Q3_K_S.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q3_K_S.llamafile) | Q3_K_S | 3 | 3.16 GB| 5.66 GB | very small, high quality loss |
| [mistral-7b-instruct-v0.2.Q3_K_M.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q3_K_M.llamafile) | Q3_K_M | 3 | 3.52 GB| 6.02 GB | very small, high quality loss |
| [mistral-7b-instruct-v0.2.Q3_K_L.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q3_K_L.llamafile) | Q3_K_L | 3 | 3.82 GB| 6.32 GB | small, substantial quality loss |
| [mistral-7b-instruct-v0.2.Q4_0.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q4_0.llamafile) | Q4_0 | 4 | 4.11 GB| 6.61 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [mistral-7b-instruct-v0.2.Q4_K_S.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q4_K_S.llamafile) | Q4_K_S | 4 | 4.14 GB| 6.64 GB | small, greater quality loss |
| [mistral-7b-instruct-v0.2.Q4_K_M.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q4_K_M.llamafile) | Q4_K_M | 4 | 4.37 GB| 6.87 GB | medium, balanced quality - recommended |
| [mistral-7b-instruct-v0.2.Q5_0.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q5_0.llamafile) | Q5_0 | 5 | 5.00 GB| 7.50 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [mistral-7b-instruct-v0.2.Q5_K_S.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q5_K_S.llamafile) | Q5_K_S | 5 | 5.00 GB| 7.50 GB | large, low quality loss - recommended |
| [mistral-7b-instruct-v0.2.Q5_K_M.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q5_K_M.llamafile) | Q5_K_M | 5 | 5.13 GB| 7.63 GB | large, very low quality loss - recommended |
| [mistral-7b-instruct-v0.2.Q6_K.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q6_K.llamafile) | Q6_K | 6 | 5.94 GB| 8.44 GB | very large, extremely low quality loss |
| [mistral-7b-instruct-v0.2.Q8_0.llamafile](https://huggingface.co/jartine/Mistral-7B-Instruct-v0.2-llamafile/blob/main/mistral-7b-instruct-v0.2.Q8_0.llamafile) | Q8_0 | 8 | 7.70 GB| 10.20 GB | very large, extremely low quality loss - not recommended |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.



<!-- README_llamafile.md-provided-files end -->

<!-- README_llamafile.md-how-to-download start -->
## How to download llamafile files

**Note for manual downloaders:** You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single file.

The following clients/libraries will automatically download models for you, providing a list of available models to choose from:

* LM Studio
* LoLLMS Web UI
* Faraday.dev

### In `text-generation-webui`

Under Download Model, you can enter the model repo: jartine/Mistral-7B-Instruct-v0.2-llamafile and below it, a specific filename to download, such as: mistral-7b-instruct-v0.2.Q4_K_M.llamafile.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download jartine/Mistral-7B-Instruct-v0.2-llamafile mistral-7b-instruct-v0.2.Q4_K_M.llamafile --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage (click to read)</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download jartine/Mistral-7B-Instruct-v0.2-llamafile --local-dir . --local-dir-use-symlinks False --include='*Q4_K*llamafile'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download jartine/Mistral-7B-Instruct-v0.2-llamafile mistral-7b-instruct-v0.2.Q4_K_M.llamafile --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_llamafile.md-how-to-download end -->

<!-- README_llamafile.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 35 -m mistral-7b-instruct-v0.2.Q4_K_M.llamafile --color -c 32768 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "<s>[INST] {prompt} [/INST]"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 32768` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the llamafile file and set by llama.cpp automatically. Note that longer sequence lengths require much more resources, so you may need to reduce this value.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions can be found in the text-generation-webui documentation, here: [text-generation-webui/docs/04 ‐ Model Tab.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/04%20%E2%80%90%20Model%20Tab.md#llamacpp).

## How to run from Python code

You can use llamafile models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) or [ctransformers](https://github.com/marella/ctransformers) libraries. Note that at the time of writing (Nov 27th 2023), ctransformers has not been updated for some time and is not compatible with some recent models. Therefore I recommend you use llama-cpp-python.

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
  model_path="./mistral-7b-instruct-v0.2.Q4_K_M.llamafile",  # Download the model file first
  n_ctx=32768,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
)

# Simple inference example
output = llm(
  "<s>[INST] {prompt} [/INST]", # Prompt
  max_tokens=512,  # Generate up to 512 tokens
  stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
  echo=True        # Whether to echo the prompt
)

# Chat Completion API

llm = Llama(model_path="./mistral-7b-instruct-v0.2.Q4_K_M.llamafile", chat_format="llama-2")  # Set chat_format according to the model you are using
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

<!-- README_llamafile.md-how-to-run end -->

<!-- footer start -->
<!-- 200823 -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[jartine AI's Discord server](https://discord.gg/FwAVVu7eJ4)

## Thanks, and how to contribute



I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.







And thank you again to mozilla for their generous grant.

<!-- footer end -->

<!-- original-model-card start -->
# Original model card: Mistral AI_'s Mistral 7B Instruct v0.2


# Model Card for Mistral-7B-Instruct-v0.2

The Mistral-7B-Instruct-v0.2 Large Language Model (LLM) is an improved instruct fine-tuned version of [Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1).

For full details of this model please read our [paper](https://arxiv.org/abs/2310.06825) and [release blog post](https://mistral.ai/news/la-plateforme/).

## Instruction format

In order to leverage instruction fine-tuning, your prompt should be surrounded by `[INST]` and `[/INST]` tokens. The very first instruction should begin with a begin of sentence id. The next instructions should not. The assistant generation will be ended by the end-of-sentence token id.

E.g.
```
text = "<s>[INST] What is your favourite condiment? [/INST]"
"Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!</s> "
"[INST] Do you have mayonnaise recipes? [/INST]"
```

This format is available as a [chat template](https://huggingface.co/docs/transformers/main/chat_templating) via the `apply_chat_template()` method:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")

messages = [
    {"role": "user", "content": "What is your favourite condiment?"},
    {"role": "assistant", "content": "Well, I'm quite partial to a good squeeze of fresh lemon juice. It adds just the right amount of zesty flavour to whatever I'm cooking up in the kitchen!"},
    {"role": "user", "content": "Do you have mayonnaise recipes?"}
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
```

## Model Architecture
This instruction model is based on Mistral-7B-v0.1, a transformer model with the following architecture choices:
- Grouped-Query Attention
- Sliding-Window Attention
- Byte-fallback BPE tokenizer

## Troubleshooting
- If you see the following error:
```
Traceback (most recent call last):
File "", line 1, in
File "/transformers/models/auto/auto_factory.py", line 482, in from_pretrained
config, kwargs = AutoConfig.from_pretrained(
File "/transformers/models/auto/configuration_auto.py", line 1022, in from_pretrained
config_class = CONFIG_MAPPING[config_dict["model_type"]]
File "/transformers/models/auto/configuration_auto.py", line 723, in getitem
raise KeyError(key)
KeyError: 'mistral'
```

Installing transformers from source should solve the issue
pip install git+https://github.com/huggingface/transformers

This should not be required after transformers-v4.33.4.

## Limitations

The Mistral 7B Instruct model is a quick demonstration that the base model can be easily fine-tuned to achieve compelling performance.
It does not have any moderation mechanisms. We're looking forward to engaging with the community on ways to
make the model finely respect guardrails, allowing for deployment in environments requiring moderated outputs.

## The Mistral AI Team

Albert Jiang, Alexandre Sablayrolles, Arthur Mensch, Blanche Savary, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Emma Bou Hanna, Florian Bressand, Gianna Lengyel, Guillaume Bour, Guillaume Lample, Lélio Renard Lavaud, Louis Ternon, Lucile Saulnier, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Théophile Gervet, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed.

<!-- original-model-card end -->