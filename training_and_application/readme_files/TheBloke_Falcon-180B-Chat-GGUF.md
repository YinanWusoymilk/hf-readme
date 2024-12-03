---
base_model: tiiuae/falcon-180B-chat
datasets:
- tiiuae/falcon-refinedweb
inference: false
language:
- en
- de
- es
- fr
license: unknown
model_creator: Technology Innovation Institute
model_name: Falcon 180B Chat
model_type: falcon
prompt_template: 'User: {prompt}

  Assistant:

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

# Falcon 180B Chat - GGUF
- Model creator: [Technology Innovation Institute](https://huggingface.co/tiiuae)
- Original model: [Falcon 180B Chat](https://huggingface.co/tiiuae/falcon-180B-chat)

<!-- description start -->
## Description

This repo contains GGUF format model files for [Technology Innovation Institute's Falcon 180B Chat](https://huggingface.co/tiiuae/falcon-180B-chat).

<!-- description end -->
<!-- README_GGUF.md-about-gguf start -->
### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.

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

* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/Falcon-180B-Chat-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/Falcon-180B-Chat-GGUF)
* [Technology Innovation Institute's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/tiiuae/falcon-180B-chat)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: Falcon

```
User: {prompt}
Assistant:

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
| falcon-180b-chat.Q2_K.gguf | Q2_K | 2 | 73.97 GB| 76.47 GB | smallest, significant quality loss - not recommended for most purposes |
| falcon-180b-chat.Q3_K_S.gguf | Q3_K_S | 3 | 77.77 GB| 80.27 GB | very small, high quality loss |
| falcon-180b-chat.Q3_K_M.gguf | Q3_K_M | 3 | 85.18 GB| 87.68 GB | very small, high quality loss |
| falcon-180b-chat.Q3_K_L.gguf | Q3_K_L | 3 | 91.99 GB| 94.49 GB | small, substantial quality loss |
| falcon-180b-chat.Q4_0.gguf | Q4_0 | 4 | 101.48 GB| 103.98 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| falcon-180b-chat.Q4_K_S.gguf | Q4_K_S | 4 | 101.48 GB| 103.98 GB | small, greater quality loss |
| falcon-180b-chat.Q4_K_M.gguf | Q4_K_M | 4 | 108.48 GB| 110.98 GB | medium, balanced quality - recommended |
| falcon-180b-chat.Q5_0.gguf | Q5_0 | 5 | 123.80 GB| 126.30 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| falcon-180b-chat.Q5_K_S.gguf | Q5_K_S | 5 | 123.80 GB| 126.30 GB | large, low quality loss - recommended |
| falcon-180b-chat.Q5_K_M.gguf | Q5_K_M | 5 | 130.99 GB| 133.49 GB | large, very low quality loss - recommended |
| falcon-180b-chat.Q6_K.gguf | Q6_K | 6 | 147.52 GB| 150.02 GB | very large, extremely low quality loss |
| falcon-180b-chat.Q8_0.gguf | Q8_0 | 8 | 190.76 GB| 193.26 GB | very large, extremely low quality loss - not recommended |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

### Q6_K and Q8_0 files are split and require joining

**Note:** HF does not support uploading files larger than 50GB. Therefore I have uploaded the Q6_K and Q8_0 files as split files.

<details>
  <summary>Click for instructions regarding Q6_K and Q8_0 files</summary>
   
### q6_K 
Please download:
* `falcon-180b-chat.Q6_K.gguf-split-a`
* `falcon-180b-chat.Q6_K.gguf-split-b`

### q8_0
Please download:
* `falcon-180b-chat.Q8_0.gguf-split-a`
* `falcon-180b-chat.Q8_0.gguf-split-b`

To join the files, do the following:

Linux and macOS:
```
cat falcon-180b-chat.Q6_K.gguf-split-* > falcon-180b-chat.Q6_K.gguf && rm falcon-180b-chat.Q6_K.gguf-split-*
cat falcon-180b-chat.Q8_0.gguf-split-* > falcon-180b-chat.Q8_0.gguf && rm falcon-180b-chat.Q8_0.gguf-split-*
```
Windows command line:
```
COPY /B falcon-180b-chat.Q6_K.gguf-split-a + falcon-180b-chat.Q6_K.gguf-split-b falcon-180b-chat.Q6_K.gguf
del falcon-180b-chat.Q6_K.gguf-split-a falcon-180b-chat.Q6_K.gguf-split-b

COPY /B falcon-180b-chat.Q8_0.gguf-split-a + falcon-180b-chat.Q8_0.gguf-split-b falcon-180b-chat.Q8_0.gguf
del falcon-180b-chat.Q8_0.gguf-split-a falcon-180b-chat.Q8_0.gguf-split-b
```

</details>
<!-- README_GGUF.md-provided-files end -->

<!-- README_GGUF.md-how-to-download start -->
## How to download GGUF files

**Note for manual downloaders:** You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single file.

The following clients/libraries will automatically download models for you, providing a list of available models to choose from:
- LM Studio
- LoLLMS Web UI
- Faraday.dev

### In `text-generation-webui`

Under Download Model, you can enter the model repo: TheBloke/Falcon-180B-Chat-GGUF and below it, a specific filename to download, such as: falcon-180b-chat.Q4_K_M.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download TheBloke/Falcon-180B-Chat-GGUF falcon-180b-chat.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download TheBloke/Falcon-180B-Chat-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/Falcon-180B-Chat-GGUF falcon-180b-chat.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 32 -m falcon-180b-chat.Q4_K_M.gguf --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "User: {prompt}\nAssistant:"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 2048` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions here: [text-generation-webui/docs/llama.cpp.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/llama.cpp.md).

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
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Falcon-180B-Chat-GGUF", model_file="falcon-180b-chat.Q4_K_M.gguf", model_type="falcon", gpu_layers=50)

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

**Patreon special mentions**: Pierre Kircher, Stanislav Ovsiannikov, Michael Levine, Eugene Pentland, Andrey, 준교 김, Randy H, Fred von Graf, Artur Olbinski, Caitlyn Gatomon, terasurfer, Jeff Scroggin, James Bentley, Vadim, Gabriel Puliatti, Harry Royden McLaughlin, Sean Connelly, Dan Guido, Edmond Seymore, Alicia Loh, subjectnull, AzureBlack, Manuel Alberto Morcote, Thomas Belote, Lone Striker, Chris Smitley, Vitor Caleffi, Johann-Peter Hartmann, Clay Pascal, biorpg, Brandon Frisco, sidney chen, transmissions 11, Pedro Madruga, jinyuan sun, Ajan Kanaga, Emad Mostaque, Trenton Dambrowitz, Jonathan Leane, Iucharbius, usrbinkat, vamX, George Stoitzev, Luke Pendergrass, theTransient, Olakabola, Swaroop Kallakuri, Cap'n Zoog, Brandon Phillips, Michael Dempsey, Nikolai Manek, danny, Matthew Berman, Gabriel Tamborski, alfie_i, Raymond Fosdick, Tom X Nguyen, Raven Klaugh, LangChain4j, Magnesian, Illia Dulskyi, David Ziegler, Mano Prime, Luis Javier Navarrete Lozano, Erik Bjäreholt, 阿明, Nathan Dryer, Alex, Rainer Wilmers, zynix, TL, Joseph William Delisle, John Villwock, Nathan LeClaire, Willem Michiel, Joguhyik, GodLy, OG, Alps Aficionado, Jeffrey Morgan, ReadyPlayerEmma, Tiffany J. Kim, Sebastain Graf, Spencer Kim, Michael Davis, webtim, Talal Aujan, knownsqashed, John Detwiler, Imad Khwaja, Deo Leter, Jerry Meng, Elijah Stavena, Rooh Singh, Pieter, SuperWojo, Alexandros Triantafyllidis, Stephen Murray, Ai Maven, ya boyyy, Enrico Ros, Ken Nordquist, Deep Realms, Nicholas, Spiking Neurons AB, Elle, Will Dee, Jack West, RoA, Luke @flexchar, Viktor Bowallius, Derek Yates, Subspace Studios, jjj, Toran Billups, Asp the Wyvern, Fen Risland, Ilya, NimbleBox.ai, Chadd, Nitin Borwankar, Emre, Mandus, Leonard Tan, Kalila, K, Trailburnt, S_X, Cory Kujawski


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->

<!-- original-model-card start -->
# Original model card: Technology Innovation Institute's Falcon 180B Chat


# 🚀 Falcon-180B-Chat

**Falcon-180B-Chat is a 180B parameters causal decoder-only model built by [TII](https://www.tii.ae) based on [Falcon-180B](https://huggingface.co/tiiuae/falcon-180B) and finetuned on a mixture of [Ultrachat](https://huggingface.co/datasets/stingning/ultrachat), [Platypus](https://huggingface.co/datasets/garage-bAInd/Open-Platypus) and [Airoboros](https://huggingface.co/datasets/jondurbin/airoboros-2.1). It is made available under the [Falcon-180B TII License](https://huggingface.co/tiiuae/falcon-180B-chat/blob/main/LICENSE.txt) and [Acceptable Use Policy](https://huggingface.co/tiiuae/falcon-180B-chat/blob/main/ACCEPTABLE_USE_POLICY.txt).**

*Paper coming soon* 😊


🤗 To get started with Falcon (inference, finetuning, quantization, etc.), we recommend reading [this great blogpost from HF](https://hf.co/blog/falcon-180b) or this [one](https://huggingface.co/blog/falcon) from the release of the 40B!
Note that since the 180B is larger than what can easily be handled with `transformers`+`acccelerate`, we recommend using [Text Generation Inference](https://github.com/huggingface/text-generation-inference).

You will need **at least 400GB of memory** to swiftly run inference with Falcon-180B.

## Why use Falcon-180B-chat?

* ✨ **You are looking for a ready-to-use chat/instruct model based on [Falcon-180B](https://huggingface.co/tiiuae/falcon-180B).**
* **It is the best open-access model currently available, and one of the best model overall.** Falcon-180B outperforms [LLaMA-2](https://huggingface.co/meta-llama/Llama-2-70b-hf), [StableLM](https://github.com/Stability-AI/StableLM), [RedPajama](https://huggingface.co/togethercomputer/RedPajama-INCITE-Base-7B-v0.1), [MPT](https://huggingface.co/mosaicml/mpt-7b), etc. See the [OpenLLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard).
* **It features an architecture optimized for inference**, with multiquery ([Shazeer et al., 2019](https://arxiv.org/abs/1911.02150)).
* **It is made available under a permissive license allowing for commercial use**.

💬 **This is a Chat model, which may not be ideal for further finetuning.** If you are interested in building your own instruct/chat model, we recommend starting from [Falcon-180B](https://huggingface.co/tiiuae/falcon-180b).

💸 **Looking for a smaller, less expensive model?** [Falcon-7B-Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct) and [Falcon-40B-Instruct](https://huggingface.co/tiiuae/falcon-40b-instruct) are Falcon-180B-Chat's little brothers!

💥 **Falcon LLMs require PyTorch 2.0 for use with `transformers`!**


# Model Card for Falcon-180B-Chat

## Model Details

### Model Description

- **Developed by:** [https://www.tii.ae](https://www.tii.ae);
- **Model type:** Causal decoder-only;
- **Language(s) (NLP):** English, German, Spanish, French (and limited capabilities in Italian, Portuguese, Polish, Dutch, Romanian, Czech, Swedish);
- **License:** [Falcon-180B TII License](https://huggingface.co/tiiuae/falcon-180B-chat/blob/main/LICENSE.txt) and [Acceptable Use Policy](https://huggingface.co/tiiuae/falcon-180B-chat/blob/main/ACCEPTABLE_USE_POLICY.txt).

### Model Source

- **Paper:** *coming soon*.

## Uses

See the [acceptable use policy](https://huggingface.co/tiiuae/falcon-180B-chat/blob/main/ACCEPTABLE_USE_POLICY.txt).

### Direct Use

Falcon-180B-Chat has been finetuned on a chat dataset.

### Out-of-Scope Use

Production use without adequate assessment of risks and mitigation; any use cases which may be considered irresponsible or harmful.

## Bias, Risks, and Limitations

Falcon-180B-Chat is mostly trained on English data, and will not generalize appropriately to other languages. Furthermore, as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

### Recommendations

We recommend users of Falcon-180B-Chat to develop guardrails and to take appropriate precautions for any production use.

## How to Get Started with the Model

To run inference with the model in full `bfloat16` precision you need approximately 8xA100 80GB or equivalent.



```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-180b-chat"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)
sequences = pipeline(
   "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:",
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

```


## Training Details

**Falcon-180B-Chat is  based on [Falcon-180B](https://huggingface.co/tiiuae/falcon-180B).**

### Training Data
Falcon-180B-Chat is finetuned on a mixture of [Ultrachat](https://huggingface.co/datasets/stingning/ultrachat), [Platypus](https://huggingface.co/datasets/garage-bAInd/Open-Platypus) and [Airoboros](https://huggingface.co/datasets/jondurbin/airoboros-2.1).

The data was tokenized with the Falcon tokenizer.


## Evaluation

*Paper coming soon.*

See the [OpenLLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) for early results.


## Technical Specifications

### Model Architecture and Objective

Falcon-180B-Chat is a causal decoder-only model trained on a causal language modeling task (i.e., predict the next token).

The architecture is broadly adapted from the GPT-3 paper ([Brown et al., 2020](https://arxiv.org/abs/2005.14165)), with the following differences:

* **Positionnal embeddings:** rotary ([Su et al., 2021](https://arxiv.org/abs/2104.09864));
* **Attention:** multiquery ([Shazeer et al., 2019](https://arxiv.org/abs/1911.02150)) and FlashAttention ([Dao et al., 2022](https://arxiv.org/abs/2205.14135));
* **Decoder-block:** parallel attention/MLP with a two layer norms.

For multiquery, we are using an internal variant which uses independent key and values per tensor parallel degree.

| **Hyperparameter** | **Value** | **Comment**                            |
|--------------------|-----------|----------------------------------------|
| Layers             | 80        |                                        |
| `d_model`          | 14848      |                                        |
| `head_dim`         | 64        | Reduced to optimise for FlashAttention |
| Vocabulary         | 65024     |                                        |
| Sequence length    | 2048      |                                        |

### Compute Infrastructure

#### Hardware

Falcon-180B-Chat was trained on AWS SageMaker, on up to 4,096 A100 40GB GPUs in P4d instances.

#### Software

Falcon-180B-Chat was trained a custom distributed training codebase, Gigatron. It uses a 3D parallelism approach combined with ZeRO and high-performance Triton kernels (FlashAttention, etc.)


## Citation

*Paper coming soon* 😊. In the meanwhile, you can use the following information to cite:
```
@article{falcon,
  title={The Falcon Series of Language Models:Towards Open Frontier Models},
  author={Almazrouei, Ebtesam and Alobeidli, Hamza and Alshamsi, Abdulaziz and Cappelli, Alessandro and Cojocaru, Ruxandra and Debbah, Merouane and Goffinet, Etienne and Heslow, Daniel and Launay, Julien and Malartic, Quentin and Noune, Badreddine and Pannier, Baptiste and Penedo, Guilherme},
  year={2023}
}
```

To learn more about the pretraining dataset, see the 📓 [RefinedWeb paper](https://arxiv.org/abs/2306.01116).

```
@article{refinedweb,
  title={The {R}efined{W}eb dataset for {F}alcon {LLM}: outperforming curated corpora with web data, and web data only},
  author={Guilherme Penedo and Quentin Malartic and Daniel Hesslow and Ruxandra Cojocaru and Alessandro Cappelli and Hamza Alobeidli and Baptiste Pannier and Ebtesam Almazrouei and Julien Launay},
  journal={arXiv preprint arXiv:2306.01116},
  eprint={2306.01116},
  eprinttype = {arXiv},
  url={https://arxiv.org/abs/2306.01116},
  year={2023}
}
```


## Contact
falconllm@tii.ae

<!-- original-model-card end -->
