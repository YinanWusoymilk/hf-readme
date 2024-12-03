---
base_model: NousResearch/Nous-Capybara-34B
datasets:
- LDJnr/LessWrong-Amplify-Instruct
- LDJnr/Pure-Dove
- LDJnr/Verified-Camel
inference: false
language:
- eng
license:
- mit
model_creator: NousResearch
model_name: Nous Capybara 34B
model_type: yi
prompt_template: 'USER: {prompt} ASSISTANT:

  '
quantized_by: TheBloke
tags:
- sft
- Yi-34B-200K
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

# Nous Capybara 34B - GGUF
- Model creator: [NousResearch](https://huggingface.co/NousResearch)
- Original model: [Nous Capybara 34B](https://huggingface.co/NousResearch/Nous-Capybara-34B)

<!-- description start -->
## Description

This repo contains GGUF format model files for [NousResearch's Nous Capybara 34B](https://huggingface.co/NousResearch/Nous-Capybara-34B).

These files were quantised using hardware kindly provided by [Massed Compute](https://massedcompute.com/).

<!-- description end -->
<!-- README_GGUF.md-about-gguf start -->
### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.

Here is an incomplete list of clients and libraries that are known to support GGUF:

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

* [AWQ model(s) for GPU inference.](https://huggingface.co/TheBloke/Nous-Capybara-34B-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/Nous-Capybara-34B-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF)
* [NousResearch's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/NousResearch/Nous-Capybara-34B)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: User-Assistant

```
USER: {prompt} ASSISTANT:

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
| [nous-capybara-34b.Q2_K.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q2_K.gguf) | Q2_K | 2 | 14.56 GB| 17.06 GB | smallest, significant quality loss - not recommended for most purposes |
| [nous-capybara-34b.Q3_K_S.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q3_K_S.gguf) | Q3_K_S | 3 | 14.96 GB| 17.46 GB | very small, high quality loss |
| [nous-capybara-34b.Q3_K_M.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q3_K_M.gguf) | Q3_K_M | 3 | 16.64 GB| 19.14 GB | very small, high quality loss |
| [nous-capybara-34b.Q3_K_L.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q3_K_L.gguf) | Q3_K_L | 3 | 18.14 GB| 20.64 GB | small, substantial quality loss |
| [nous-capybara-34b.Q4_0.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q4_0.gguf) | Q4_0 | 4 | 19.47 GB| 21.97 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [nous-capybara-34b.Q4_K_S.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q4_K_S.gguf) | Q4_K_S | 4 | 19.54 GB| 22.04 GB | small, greater quality loss |
| [nous-capybara-34b.Q4_K_M.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q4_K_M.gguf) | Q4_K_M | 4 | 20.66 GB| 23.16 GB | medium, balanced quality - recommended |
| [nous-capybara-34b.Q5_0.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q5_0.gguf) | Q5_0 | 5 | 23.71 GB| 26.21 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [nous-capybara-34b.Q5_K_S.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q5_K_S.gguf) | Q5_K_S | 5 | 23.71 GB| 26.21 GB | large, low quality loss - recommended |
| [nous-capybara-34b.Q5_K_M.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q5_K_M.gguf) | Q5_K_M | 5 | 24.32 GB| 26.82 GB | large, very low quality loss - recommended |
| [nous-capybara-34b.Q6_K.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q6_K.gguf) | Q6_K | 6 | 28.21 GB| 30.71 GB | very large, extremely low quality loss |
| [nous-capybara-34b.Q8_0.gguf](https://huggingface.co/TheBloke/Nous-Capybara-34B-GGUF/blob/main/nous-capybara-34b.Q8_0.gguf) | Q8_0 | 8 | 36.54 GB| 39.04 GB | very large, extremely low quality loss - not recommended |

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

Under Download Model, you can enter the model repo: TheBloke/Nous-Capybara-34B-GGUF and below it, a specific filename to download, such as: nous-capybara-34b.Q4_K_M.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download TheBloke/Nous-Capybara-34B-GGUF nous-capybara-34b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download TheBloke/Nous-Capybara-34B-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/Nous-Capybara-34B-GGUF nous-capybara-34b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 32 -m nous-capybara-34b.Q4_K_M.gguf --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "USER: {prompt} ASSISTANT:"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 2048` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions can be found in the text-generation-webui documentation, here: [text-generation-webui/docs/04 ‐ Model Tab.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/04%20%E2%80%90%20Model%20Tab.md#llamacpp).

## How to run from Python code

You can use GGUF models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) or [ctransformers](https://github.com/marella/ctransformers) libraries.

### How to load this model in Python code, using ctransformers

#### First install the package

Run one of the following commands, according to your system:

```shell
# Base ctransformers with no GPU acceleration
pip install ctransformers
# Or with CUDA GPU acceleration
pip install ctransformers[cuda]
# Or with AMD ROCm GPU acceleration (Linux only)
CT_HIPBLAS=1 pip install ctransformers --no-binary ctransformers
# Or with Metal GPU acceleration for macOS systems only
CT_METAL=1 pip install ctransformers --no-binary ctransformers
```

#### Simple ctransformers example code

```python
from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Nous-Capybara-34B-GGUF", model_file="nous-capybara-34b.Q4_K_M.gguf", model_type="yi", gpu_layers=50)

print(llm("AI is going to"))
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

**Patreon special mentions**: Brandon Frisco, LangChain4j, Spiking Neurons AB, transmissions 11, Joseph William Delisle, Nitin Borwankar, Willem Michiel, Michael Dempsey, vamX, Jeffrey Morgan, zynix, jjj, Omer Bin Jawed, Sean Connelly, jinyuan sun, Jeromy Smith, Shadi, Pawan Osman, Chadd, Elijah Stavena, Illia Dulskyi, Sebastain Graf, Stephen Murray, terasurfer, Edmond Seymore, Celu Ramasamy, Mandus, Alex, biorpg, Ajan Kanaga, Clay Pascal, Raven Klaugh, 阿明, K, ya boyyy, usrbinkat, Alicia Loh, John Villwock, ReadyPlayerEmma, Chris Smitley, Cap'n Zoog, fincy, GodLy, S_X, sidney chen, Cory Kujawski, OG, Mano Prime, AzureBlack, Pieter, Kalila, Spencer Kim, Tom X Nguyen, Stanislav Ovsiannikov, Michael Levine, Andrey, Trailburnt, Vadim, Enrico Ros, Talal Aujan, Brandon Phillips, Jack West, Eugene Pentland, Michael Davis, Will Dee, webtim, Jonathan Leane, Alps Aficionado, Rooh Singh, Tiffany J. Kim, theTransient, Luke @flexchar, Elle, Caitlyn Gatomon, Ari Malik, subjectnull, Johann-Peter Hartmann, Trenton Dambrowitz, Imad Khwaja, Asp the Wyvern, Emad Mostaque, Rainer Wilmers, Alexandros Triantafyllidis, Nicholas, Pedro Madruga, SuperWojo, Harry Royden McLaughlin, James Bentley, Olakabola, David Ziegler, Ai Maven, Jeff Scroggin, Nikolai Manek, Deo Leter, Matthew Berman, Fen Risland, Ken Nordquist, Manuel Alberto Morcote, Luke Pendergrass, TL, Fred von Graf, Randy H, Dan Guido, NimbleBox.ai, Vitor Caleffi, Gabriel Tamborski, knownsqashed, Lone Striker, Erik Bjäreholt, John Detwiler, Leonard Tan, Iucharbius


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->

<!-- original-model-card start -->
# Original model card: NousResearch's Nous Capybara 34B


## **Nous-Capybara-34B V1.9**

**This is trained on the Yi-34B model with 200K context length, for 3 epochs on the Capybara dataset!**

**First 34B Nous model and first 200K context length Nous model!**

The Capybara series is the first Nous collection of models made by fine-tuning mostly on data created by Nous in-house.

We leverage our novel data synthesis technique called Amplify-instruct (Paper coming soon), the seed distribution and synthesis method are comprised of a synergistic combination of top performing existing data synthesis techniques and distributions used for SOTA models such as Airoboros, Evol-Instruct(WizardLM), Orca, Vicuna, Know_Logic, Lamini, FLASK and others, all into one lean holistically formed methodology for the dataset and model. The seed instructions used for the start of synthesized conversations are largely based on highly regarded datasets like Airoboros, Know logic, EverythingLM, GPTeacher and even entirely new seed instructions derived from posts on the website LessWrong, as well as being supplemented with certain in-house multi-turn datasets like Dove(A successor to Puffin).

While performing great in it's current state, the current dataset used for fine-tuning is entirely contained within 20K training examples, this is 10 times smaller than many similar performing current models, this is signficant when it comes to scaling implications for our next generation of models once we scale our novel syntheiss methods to significantly more examples.

## Process of creation and special thank yous!

This model was fine-tuned by Nous Research as part of the Capybara/Amplify-Instruct project led by Luigi D.(LDJ) (Paper coming soon), as well as significant dataset formation contributions by J-Supha and general compute and experimentation management by Jeffrey Q. during ablations.

Special thank you to **A16Z** for sponsoring our training, as well as **Yield Protocol** for their support in financially sponsoring resources during the R&D of this project.

## Thank you to those of you that have indirectly contributed!

While most of the tokens within Capybara are newly synthsized and part of datasets like Puffin/Dove, we would like to credit the single-turn datasets we leveraged as seeds that are used to generate the multi-turn data as part of the Amplify-Instruct synthesis.

The datasets shown in green below are datasets that we sampled from to curate seeds that are used during Amplify-Instruct synthesis for this project.

Datasets in Blue are in-house curations that previously existed prior to Capybara.

![Capybara](https://i.imgur.com/yB58OoD.jpeg)


## Prompt Format

The reccomended model usage is:


Prefix: ``USER:``

Suffix: ``ASSISTANT:``

Stop token: ``</s>``


## Mutli-Modality!

 - We currently have a Multi-modal model based on Capybara V1.9!
https://huggingface.co/NousResearch/Obsidian-3B-V0.5
it is currently only available as a 3B sized model but larger versions coming!


## Notable Features:

 - Uses Yi-34B model as the base which is trained for 200K context length!

 - Over 60% of the dataset is comprised of multi-turn conversations.(Most models are still only trained for single-turn conversations and no back and forths!)

 - Over 1,000 tokens average per conversation example! (Most models are trained on conversation data that is less than 300 tokens per example.)

 - Able to effectively do complex summaries of advanced topics and studies. (trained on hundreds of advanced difficult summary tasks developed in-house)

 - Ability to recall information upto late 2022 without internet.

 - Includes a portion of conversational data synthesized from less wrong posts, discussing very in-depth details and philosophies about the nature of reality, reasoning, rationality, self-improvement and related concepts.

## Example Outputs from Capybara V1.9 7B version! (examples from 34B coming soon):

![Capybara](https://img001.prntscr.com/file/img001/T9yYxR1xQSaK_UGdy3t2Cw.png)

![Capybara](https://img001.prntscr.com/file/img001/DQXqmKbsQQOIcgny1eoGNA.png)

![Capybara](https://img001.prntscr.com/file/img001/85X3L9ZxTsOKo3fUQ7GRVA.png)

## Benchmarks! (Coming soon!)


## Future model sizes

Capybara V1.9 now currently has a 3B, 7B and 34B size, and we plan to eventually have a 13B and 70B version in the future, as well as a potential 1B version based on phi-1.5 or Tiny Llama.

## How you can help!

In the near future we plan on leveraging the help of domain specific expert volunteers to eliminate any mathematically/verifiably incorrect answers from our training curations.

If you have at-least a bachelors in mathematics, physics, biology or chemistry and would like to volunteer even just 30 minutes of your expertise time, please contact LDJ on discord!

## Dataset contamination.

We have checked the capybara dataset for contamination for several of the most popular datasets and can confirm that there is no contaminaton found.

We leveraged minhash to check for 100%, 99%, 98% and 97% similarity matches between our data and the questions and answers in benchmarks, we found no exact matches, nor did we find any matches down to the 97% similarity level.

The following are benchmarks we checked for contamination against our dataset:

- HumanEval

- AGIEval

- TruthfulQA

- MMLU

- GPT4All

<!-- original-model-card end -->
