---
license: cc-by-sa-4.0
model_name: Luna AI Llama2 Uncensored
base_model: Tap-M/Luna-AI-Llama2-Uncensored
inference: false
model_creator: Tap
model_type: llama
prompt_template: 'USER: {prompt}

  ASSISTANT:

  '
quantized_by: TheBloke
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

# Luna AI Llama2 Uncensored - GGUF
- Model creator: [Tap](https://huggingface.co/Tap-M)
- Original model: [Luna AI Llama2 Uncensored](https://huggingface.co/Tap-M/Luna-AI-Llama2-Uncensored)

<!-- description start -->
## Description

This repo contains GGUF format model files for [Tap-M's Luna AI Llama2 Uncensored](https://huggingface.co/Tap-M/Luna-AI-Llama2-Uncensored).

Many thanks to William Beauchamp from [Chai](https://chai-research.com/) for providing the hardware used to make and upload these files!

<!-- description end -->
<!-- README_GGUF.md-about-gguf start -->
### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp. GGUF offers numerous advantages over GGML, such as better tokenisation, and support for special tokens. It is also supports metadata, and is designed to be extensible.

Here is an incomplate list of clients and libraries that are known to support GGUF:

* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for GGUF. Offers a CLI and a server option.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.

<!-- README_GGUF.md-about-gguf end -->
<!-- repositories-available start -->
## Repositories available

* [AWQ model(s) for GPU inference.](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF)
* [Tap's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/Tap-M/Luna-AI-Llama2-Uncensored)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: User-Assistant

```
USER: {prompt}
ASSISTANT:

```

<!-- prompt-template end -->
<!-- licensing start -->
## Licensing

The creator of the source model has listed its license as `cc-by-sa-4.0`, and this quantization has therefore used that same license.

As this model is based on Llama 2, it is also subject to the Meta Llama 2 license terms, and the license files for that are additionally included. It should therefore be considered as being claimed to be licensed under both licenses. I contacted Hugging Face for clarification on dual licensing but they do not yet have an official position. Should this change, or should Meta provide any feedback on this situation, I will update this section accordingly.

In the meantime, any questions regarding licensing, and in particular how these two licenses might interact, should be directed to the original model repository: [Tap-M's Luna AI Llama2 Uncensored](https://huggingface.co/Tap-M/Luna-AI-Llama2-Uncensored).
<!-- licensing end -->
<!-- compatibility_gguf start -->
## Compatibility

These quantised GGUFv2 files are compatible with llama.cpp from August 27th onwards, as of commit [d0cee0d36d5be95a0d9088b674dbb27354107221](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221)

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
| [luna-ai-llama2-uncensored.Q2_K.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q2_K.gguf) | Q2_K | 2 | 2.83 GB| 5.33 GB | smallest, significant quality loss - not recommended for most purposes |
| [luna-ai-llama2-uncensored.Q3_K_S.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q3_K_S.gguf) | Q3_K_S | 3 | 2.95 GB| 5.45 GB | very small, high quality loss |
| [luna-ai-llama2-uncensored.Q3_K_M.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q3_K_M.gguf) | Q3_K_M | 3 | 3.30 GB| 5.80 GB | very small, high quality loss |
| [luna-ai-llama2-uncensored.Q3_K_L.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q3_K_L.gguf) | Q3_K_L | 3 | 3.60 GB| 6.10 GB | small, substantial quality loss |
| [luna-ai-llama2-uncensored.Q4_0.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q4_0.gguf) | Q4_0 | 4 | 3.83 GB| 6.33 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [luna-ai-llama2-uncensored.Q4_K_S.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q4_K_S.gguf) | Q4_K_S | 4 | 3.86 GB| 6.36 GB | small, greater quality loss |
| [luna-ai-llama2-uncensored.Q4_K_M.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q4_K_M.gguf) | Q4_K_M | 4 | 4.08 GB| 6.58 GB | medium, balanced quality - recommended |
| [luna-ai-llama2-uncensored.Q5_0.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q5_0.gguf) | Q5_0 | 5 | 4.65 GB| 7.15 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [luna-ai-llama2-uncensored.Q5_K_S.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q5_K_S.gguf) | Q5_K_S | 5 | 4.65 GB| 7.15 GB | large, low quality loss - recommended |
| [luna-ai-llama2-uncensored.Q5_K_M.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q5_K_M.gguf) | Q5_K_M | 5 | 4.78 GB| 7.28 GB | large, very low quality loss - recommended |
| [luna-ai-llama2-uncensored.Q6_K.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q6_K.gguf) | Q6_K | 6 | 5.53 GB| 8.03 GB | very large, extremely low quality loss |
| [luna-ai-llama2-uncensored.Q8_0.gguf](https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGUF/blob/main/luna-ai-llama2-uncensored.Q8_0.gguf) | Q8_0 | 8 | 7.16 GB| 9.66 GB | very large, extremely low quality loss - not recommended |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.



<!-- README_GGUF.md-provided-files end -->

<!-- README_GGUF.md-how-to-download start -->
## How to download GGUF files

**Note for manual downloaders:** You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single file.

The following clients/libraries will automatically download models for you, providing a list of available models to choose from:
- LM Studio
- LoLLMS Web UI
- Faraday.dev

### In `text-generation-webui`

Under Download Model, you can enter the model repo: TheBloke/Luna-AI-Llama2-Uncensored-GGUF and below it, a specific filename to download, such as: luna-ai-llama2-uncensored.q4_K_M.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub>=0.17.1
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download TheBloke/Luna-AI-Llama2-Uncensored-GGUF luna-ai-llama2-uncensored.q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download TheBloke/Luna-AI-Llama2-Uncensored-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HUGGINGFACE_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/Luna-AI-Llama2-Uncensored-GGUF luna-ai-llama2-uncensored.q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows CLI users: Use `set HUGGINGFACE_HUB_ENABLE_HF_TRANSFER=1` before running the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d36d5be95a0d9088b674dbb27354107221](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 32 -m luna-ai-llama2-uncensored.q4_K_M.gguf --color -c 4096 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "USER: {prompt}\nASSISTANT:"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 4096` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions here: [text-generation-webui/docs/llama.cpp.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/llama.cpp.md).

## How to run from Python code

You can use GGUF models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) or [ctransformers](https://github.com/marella/ctransformers) libraries.

### How to load this model from Python using ctransformers

#### First install the package

```bash
# Base ctransformers with no GPU acceleration
pip install ctransformers>=0.2.24
# Or with CUDA GPU acceleration
pip install ctransformers[cuda]>=0.2.24
# Or with ROCm GPU acceleration
CT_HIPBLAS=1 pip install ctransformers>=0.2.24 --no-binary ctransformers
# Or with Metal GPU acceleration for macOS systems
CT_METAL=1 pip install ctransformers>=0.2.24 --no-binary ctransformers
```

#### Simple example code to load one of these GGUF models

```python
from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Luna-AI-Llama2-Uncensored-GGUF", model_file="luna-ai-llama2-uncensored.q4_K_M.gguf", model_type="llama", gpu_layers=50)

print(llm("AI is going to"))
```

## How to use with LangChain

Here's guides on using llama-cpp-python or ctransformers with LangChain:

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

**Patreon special mentions**: Alicia Loh, Stephen Murray, K, Ajan Kanaga, RoA, Magnesian, Deo Leter, Olakabola, Eugene Pentland, zynix, Deep Realms, Raymond Fosdick, Elijah Stavena, Iucharbius, Erik Bjäreholt, Luis Javier Navarrete Lozano, Nicholas, theTransient, John Detwiler, alfie_i, knownsqashed, Mano Prime, Willem Michiel, Enrico Ros, LangChain4j, OG, Michael Dempsey, Pierre Kircher, Pedro Madruga, James Bentley, Thomas Belote, Luke @flexchar, Leonard Tan, Johann-Peter Hartmann, Illia Dulskyi, Fen Risland, Chadd, S_X, Jeff Scroggin, Ken Nordquist, Sean Connelly, Artur Olbinski, Swaroop Kallakuri, Jack West, Ai Maven, David Ziegler, Russ Johnson, transmissions 11, John Villwock, Alps Aficionado, Clay Pascal, Viktor Bowallius, Subspace Studios, Rainer Wilmers, Trenton Dambrowitz, vamX, Michael Levine, 준교 김, Brandon Frisco, Kalila, Trailburnt, Randy H, Talal Aujan, Nathan Dryer, Vadim, 阿明, ReadyPlayerEmma, Tiffany J. Kim, George Stoitzev, Spencer Kim, Jerry Meng, Gabriel Tamborski, Cory Kujawski, Jeffrey Morgan, Spiking Neurons AB, Edmond Seymore, Alexandros Triantafyllidis, Lone Striker, Cap'n Zoog, Nikolai Manek, danny, ya boyyy, Derek Yates, usrbinkat, Mandus, TL, Nathan LeClaire, subjectnull, Imad Khwaja, webtim, Raven Klaugh, Asp the Wyvern, Gabriel Puliatti, Caitlyn Gatomon, Joseph William Delisle, Jonathan Leane, Luke Pendergrass, SuperWojo, Sebastain Graf, Will Dee, Fred von Graf, Andrey, Dan Guido, Daniel P. Andersen, Nitin Borwankar, Elle, Vitor Caleffi, biorpg, jjj, NimbleBox.ai, Pieter, Matthew Berman, terasurfer, Michael Davis, Alex, Stanislav Ovsiannikov


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->

<!-- original-model-card start -->
# Original model card: Tap-M's Luna AI Llama2 Uncensored


<div style="width: 800px; margin: auto;">

<h2>Model Description</h2>
<p>“Luna AI Llama2 Uncensored” is a Llama2 based Chat model <br />fine-tuned on over 40,000 long form chat discussions <br />
  This model was fine-tuned by Tap, the creator of Luna AI. <br />

<h2>Model Training</h2>
<p>The fine-tuning process was performed on an 8x a100 80GB machine.
  <br />The model was trained on synthetic outputs which include multiple rounds of chats between Human & AI.
</p>

<a rel="noopener nofollow" href="https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GPTQ">4bit GPTQ Version provided by @TheBloke - for GPU inference</a><br />
<a rel="noopener nofollow" href="https://huggingface.co/TheBloke/Luna-AI-Llama2-Uncensored-GGML">GGML Version provided by @TheBloke - For CPU inference</a>


<h2>Prompt Format</h2>
<p>The model follows the Vicuna 1.1/ OpenChat format:</p>

```
USER: I have difficulties in making friends, and I really need someone to talk to. Would you be my friend?

ASSISTANT: Of course! Friends are always here for each other. What do you like to do?

```

<h2>Benchmark Results</h2>

||||||
|---:|---:|---:|---:|---:|
|Task|Version| Metric |Value |Stderr|
|arc_challenge|0|acc_norm|0.5512|0.0146|
|hellaswag|0||||
|mmlu|1|acc_norm|0.46521|0.036|
|truthfulqa_mc|1|mc2|0.4716|0.0155|
|Average|-|-|0.5114|0.0150|

</div>



<!-- original-model-card end -->
