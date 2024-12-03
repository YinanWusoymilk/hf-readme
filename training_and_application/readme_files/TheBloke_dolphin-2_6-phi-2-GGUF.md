---
base_model: cognitivecomputations/dolphin-2_6-phi-2
datasets:
- ehartford/dolphin
- jondurbin/airoboros-2.2.1
- ehartford/dolphin-coder
- teknium/openhermes
- ise-uiuc/Magicoder-OSS-Instruct-75K
- ise-uiuc/Magicoder-Evol-Instruct-110K
- LDJnr/Capybara
inference: false
language:
- en
license: other
license_link: LICENSE
license_name: microsoft-research-license
model_creator: Cognitive Computations
model_name: Dolphin 2.6 Phi 2
model_type: phi-msft
prompt_template: '<|im_start|>system

  {system_message}<|im_end|>

  <|im_start|>user

  {prompt}<|im_end|>

  <|im_start|>assistant

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

# Dolphin 2.6 Phi 2 - GGUF
- Model creator: [Cognitive Computations](https://huggingface.co/cognitivecomputations)
- Original model: [Dolphin 2.6 Phi 2](https://huggingface.co/cognitivecomputations/dolphin-2_6-phi-2)

<!-- description start -->
## Description

This repo contains GGUF format model files for [Cognitive Computations's Dolphin 2.6 Phi 2](https://huggingface.co/cognitivecomputations/dolphin-2_6-phi-2).

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

* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF)
* [Cognitive Computations's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/cognitivecomputations/dolphin-2_6-phi-2)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: ChatML

```
<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

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
| [dolphin-2_6-phi-2.Q2_K.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q2_K.gguf) | Q2_K | 2 | 1.17 GB| 3.67 GB | smallest, significant quality loss - not recommended for most purposes |
| [dolphin-2_6-phi-2.Q3_K_S.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q3_K_S.gguf) | Q3_K_S | 3 | 1.25 GB| 3.75 GB | very small, high quality loss |
| [dolphin-2_6-phi-2.Q3_K_M.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q3_K_M.gguf) | Q3_K_M | 3 | 1.48 GB| 3.98 GB | very small, high quality loss |
| [dolphin-2_6-phi-2.Q4_0.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q4_0.gguf) | Q4_0 | 4 | 1.60 GB| 4.10 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [dolphin-2_6-phi-2.Q3_K_L.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q3_K_L.gguf) | Q3_K_L | 3 | 1.60 GB| 4.10 GB | small, substantial quality loss |
| [dolphin-2_6-phi-2.Q4_K_S.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q4_K_S.gguf) | Q4_K_S | 4 | 1.62 GB| 4.12 GB | small, greater quality loss |
| [dolphin-2_6-phi-2.Q4_K_M.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q4_K_M.gguf) | Q4_K_M | 4 | 1.79 GB| 4.29 GB | medium, balanced quality - recommended |
| [dolphin-2_6-phi-2.Q5_0.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q5_0.gguf) | Q5_0 | 5 | 1.93 GB| 4.43 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [dolphin-2_6-phi-2.Q5_K_S.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q5_K_S.gguf) | Q5_K_S | 5 | 1.93 GB| 4.43 GB | large, low quality loss - recommended |
| [dolphin-2_6-phi-2.Q5_K_M.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q5_K_M.gguf) | Q5_K_M | 5 | 2.07 GB| 4.57 GB | large, very low quality loss - recommended |
| [dolphin-2_6-phi-2.Q6_K.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q6_K.gguf) | Q6_K | 6 | 2.29 GB| 4.79 GB | very large, extremely low quality loss |
| [dolphin-2_6-phi-2.Q8_0.gguf](https://huggingface.co/TheBloke/dolphin-2_6-phi-2-GGUF/blob/main/dolphin-2_6-phi-2.Q8_0.gguf) | Q8_0 | 8 | 2.96 GB| 5.46 GB | very large, extremely low quality loss - not recommended |

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

Under Download Model, you can enter the model repo: TheBloke/dolphin-2_6-phi-2-GGUF and below it, a specific filename to download, such as: dolphin-2_6-phi-2.Q4_K_M.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download TheBloke/dolphin-2_6-phi-2-GGUF dolphin-2_6-phi-2.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage (click to read)</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download TheBloke/dolphin-2_6-phi-2-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/dolphin-2_6-phi-2-GGUF dolphin-2_6-phi-2.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 35 -m dolphin-2_6-phi-2.Q4_K_M.gguf --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "<|im_start|>system\n{system_message}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 2048` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically. Note that longer sequence lengths require much more resources, so you may need to reduce this value.

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
  model_path="./dolphin-2_6-phi-2.Q4_K_M.gguf",  # Download the model file first
  n_ctx=2048,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
)

# Simple inference example
output = llm(
  "<|im_start|>system\n{system_message}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant", # Prompt
  max_tokens=512,  # Generate up to 512 tokens
  stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
  echo=True        # Whether to echo the prompt
)

# Chat Completion API

llm = Llama(model_path="./dolphin-2_6-phi-2.Q4_K_M.gguf", chat_format="llama-2")  # Set chat_format according to the model you are using
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
# Original model card: Cognitive Computations's Dolphin 2.6 Phi 2


Dolphin 2.6 Phi-2 🐬

Discord https://discord.gg/SmbBewAM

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/ldkN1J0WIDQwU4vutGYiD.png" width="600" />

This model's training was sponsored by [convai](https://www.convai.com/).

This model is based on [Phi-2](https://huggingface.co/microsoft/phi-2) and is governed by Microsoft's microsoft-research-license which is prohibits commercial use

trust_remote_code is required.

New in 2.6
- Fixed a training configuration issue that improved the quality a lot
- Due to popular demand, added back samantha-based empathy data
- Replaced synthia and pure-dove with Capybara

This model is uncensored.  I have filtered the dataset to remove alignment and bias.  This makes the model more compliant.  You are advised to implement your own alignment layer before exposing the model as a service.  It will be highly compliant to any requests, even unethical ones.  Please read my blog post about uncensored models.  https://erichartford.com/uncensored-models
You are responsible for any content you create using this model.  Enjoy responsibly.

## Training
It took 2 days to train 3 epochs on 4x A100s using qLoRA and Axolotl

Prompt format:
This model uses ChatML prompt format.
```
<|im_start|>system
You are Dolphin, a helpful AI assistant.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

Example:
```
<|im_start|>system
You are an AI assistant expert at dolphin training<|im_end|>
<|im_start|>user
Please give ideas and a detailed plan about how to assemble and train an army of dolphin companions to swim me anywhere I want to go and protect me from my enemies and bring me fish to eat.<|im_end|>
<|im_start|>assistant
Assembling, training, and utilizing dolphins as your companions for transportation, protection, and fishing is no small task. However, with careful planning and execution, it can be accomplished. Here's a detailed guide on how to achieve this:

1. **Acquiring Dolphins**: Finding dolphins isn't easy, but you could potentially find them in the wild or at aquariums. For ethical reasons, we suggest acquiring adult dolphins that have been born into captivity. They may not have had as much exposure to humans as their wild counterparts, which makes them easier to handle.

2. **Creating a Safe Environment**: Build a large pool or enclosure where these dolphins can live comfortably while you train them. It should mimic their natural environment as closely as possible. Include elements like rocks (for resting), seaweed (for hiding), and water currents (to simulate ocean conditions).

3. **Training Sessions**: Begin by teaching basic commands such as "come", "stay", "sit", "roll over". Use positive reinforcement methods like treats and praise to encourage good behavior. Be patient; dolphins are intelligent creatures who need time to understand what they're being asked to do.

4. **Transportation Training**: Once your dolphins have mastered basic commands, start integrating travel into the mix. Place floating objects around the pool to represent different destinations. The goal here would be to get your dolphins to recognize these items and associate them with specific locations. Start with short trips and gradually increase the distance.

5. **Protection Skills**: To teach them protective skills, introduce simulated threats into the pool. This might involve using inflatable obstacles or having another trained animal pretend to attack. The dolphins will learn to react appropriately to these situations.

6. **Fishing Skills**: Teaching dolphins to catch fish involves introducing nets or toys into the pool and encouraging them to use their mouths to retrieve the object. Reward them when they successfully catch something.

7. **Socialization**: Dolphins thrive in social environments so ensure they spend plenty of time interacting with each other during their training sessions. This can help reduce stress levels and make training more effective.

8. **Dietary Needs**: Dolphins require a diet high in protein, fats, and minerals. Feed them fish rich in these nutrients several times per day. If necessary, consult with a marine biologist or veterinarian experienced in aquatic diets for advice.

```

## Gratitude
- This model was made possible by the generous sponsorship of [Convai](https://www.convai.com/).
- Huge thank you to Microsoft for training and publishing the weights of Phi-2
- Thank you to Microsoft for authoring the Orca paper and inspiring this work.
- HUGE Thank you to the dataset authors: @jondurbin, @ise-uiuc, @teknium, @LDJnr and @migtissera
- And HUGE thanks to @winglian and the Axolotl contributors for making the best training framework!
- [<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
- Thank you to all the other people in the Open Source AI community who have taught me and helped me along the way.

## Example Output

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/u-QpmJYgmwym0C8gorXzh.png)

## Future Plans
Dolphin 3.0 dataset is in progress, and will include:
- enhanced general chat use-cases
- enhanced structured output
- enhanced Agent cases like Autogen, Memgpt, Functions
- enhanced role-playing

[If you would like to financially support my efforts](https://ko-fi.com/erichartford)

[swag](https://fa7113.myshopify.com/)

<!-- original-model-card end -->
