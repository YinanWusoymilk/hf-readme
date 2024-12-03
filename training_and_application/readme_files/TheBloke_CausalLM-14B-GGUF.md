---
base_model: CausalLM/14B
datasets:
- JosephusCheung/GuanacoDataset
- Open-Orca/OpenOrca
- stingning/ultrachat
- meta-math/MetaMathQA
- liuhaotian/LLaVA-Instruct-150K
- jondurbin/airoboros-3.1
- WizardLM/WizardLM_evol_instruct_V2_196k
- RyokoAI/ShareGPT52K
- RyokoAI/Fandom23K
- milashkaarshif/MoeGirlPedia_wikitext_raw_archive
- wikipedia
- wiki_lingua
- fnlp/moss-003-sft-data
- garage-bAInd/Open-Platypus
- LDJnr/Puffin
- openbmb/llava_zh
- BAAI/COIG
- TigerResearch/tigerbot-zhihu-zh-10k
- liwu/MNBVC
- teknium/openhermes
inference: false
language:
- en
- zh
license: wtfpl
model_creator: CausalLM
model_name: CausalLM 14B
model_type: llama
pipeline_tag: text-generation
prompt_template: '<|im_start|>system

  {system_message}<|im_end|>

  <|im_start|>user

  {prompt}<|im_end|>

  <|im_start|>assistant

  '
quantized_by: TheBloke
tags:
- llama
- llama2
- qwen
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

# CausalLM 14B - GGUF
- Model creator: [CausalLM](https://huggingface.co/CausalLM)
- Original model: [CausalLM 14B](https://huggingface.co/CausalLM/14B)

<!-- description start -->
## Description

This repo contains GGUF format model files for [CausalLM's CausalLM 14B](https://huggingface.co/CausalLM/14B).

**NOTE**: The GGUFs originally uploaded here did not work due to a vocab issue.  This was fixed on 23rd October, 15:00 UTC.  The files uploaded now are confirmed to work.

Please re-download the GGUFs if you had downloaded the originally uploaded GGUF file(s).

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

* [AWQ model(s) for GPU inference.](https://huggingface.co/TheBloke/CausalLM-14B-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/CausalLM-14B-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/CausalLM-14B-GGUF)
* [CausalLM's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/CausalLM/14B)
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
<!-- licensing start -->
## Licensing

The creator of the source model has listed its license as `wtfpl`, and this quantization has therefore used that same license.

As this model is based on Llama 2, it is also subject to the Meta Llama 2 license terms, and the license files for that are additionally included. It should therefore be considered as being claimed to be licensed under both licenses. I contacted Hugging Face for clarification on dual licensing but they do not yet have an official position. Should this change, or should Meta provide any feedback on this situation, I will update this section accordingly.

In the meantime, any questions regarding licensing, and in particular how these two licenses might interact, should be directed to the original model repository: [CausalLM's CausalLM 14B](https://huggingface.co/CausalLM/14B).
<!-- licensing end -->
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
| [causallm_14b.Q4_0.gguf](https://huggingface.co/TheBloke/CausalLM-14B-GGUF/blob/main/causallm_14b.Q4_0.gguf) | Q4_0 | 4 | 8.18 GB| 10.68 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [causallm_14b.Q4_1.gguf](https://huggingface.co/TheBloke/CausalLM-14B-GGUF/blob/main/causallm_14b.Q4_1.gguf) | Q4_1 | 4 | 9.01 GB| 11.51 GB | legacy; small, substantial quality loss - lprefer using Q3_K_L |
| [causallm_14b.Q5_0.gguf](https://huggingface.co/TheBloke/CausalLM-14B-GGUF/blob/main/causallm_14b.Q5_0.gguf) | Q5_0 | 5 | 9.85 GB| 12.35 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [causallm_14b.Q5_1.gguf](https://huggingface.co/TheBloke/CausalLM-14B-GGUF/blob/main/causallm_14b.Q5_1.gguf) | Q5_1 | 5 | 10.69 GB| 13.19 GB | legacy; medium, low quality loss - prefer using Q5_K_M |
| [causallm_14b.Q8_0.gguf](https://huggingface.co/TheBloke/CausalLM-14B-GGUF/blob/main/causallm_14b.Q8_0.gguf) | Q8_0 | 8 | 15.06 GB| 17.56 GB | very large, extremely low quality loss - not recommended |

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

Under Download Model, you can enter the model repo: TheBloke/CausalLM-14B-GGUF and below it, a specific filename to download, such as: causallm_14b.Q4_K_M.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download TheBloke/CausalLM-14B-GGUF causallm_14b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download TheBloke/CausalLM-14B-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/CausalLM-14B-GGUF causallm_14b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 32 -m causallm_14b.Q4_K_M.gguf --color -c 4096 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "<|im_start|>system\n{system_message}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 4096` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically.

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
llm = AutoModelForCausalLM.from_pretrained("TheBloke/CausalLM-14B-GGUF", model_file="causallm_14b.Q4_K_M.gguf", model_type="llama", gpu_layers=50)

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
# Original model card: CausalLM's CausalLM 14B

![](https://huggingface.co/JosephusCheung/tmp/resolve/main/14.17b.png)

*Image drawn by GPT-4 DALL·E 3* TL;DR: Perhaps better than all existing models < 70B, in most quantitative evaluations...

# Please Stop Using WRONG unofficial quant models unless you know what you're doing

GPTQ quants require a good dataset for calibration, and the default C4 dataset is not capable.

**llama.cpp GGUF models**
GPT2Tokenizer fixed by [Kerfuffle](https://github.com/KerfuffleV2) on [https://github.com/ggerganov/llama.cpp/pull/3743](https://github.com/ggerganov/llama.cpp/pull/3743), new models to be reuploaded.

# Read Me:

Also see [7B Version](https://huggingface.co/CausalLM/7B)

This model was trained based on the model weights of Qwen (and LLaMA2 was used, yes, for calculating some initial weights), you may also need to comply with the commercial use restrictions of these two models depending on the situation. The training process utilized a model structure that was identical to LLaMA2, using the same attention calculation method as the original MHA LLaMA2 models, and no additional scaling applied to the Relative Positional Encoding (RoPE).

We manually curated a SFT dataset of 1.3B tokens for training, utilizing open source datasets from Hugging Face. For most of these sentences, we performed manual or synthetic rewrites and generated alternate language versions using larger language models. Additionally, we conducted augmented text training using carefully selected entries from Wikipedia, as well as featured entries from Fandom and filtered entries from Moegirlpedia. In order to strike a balance between efficiency and quality, 100% of the data used for training was synthetic data, no direct use of text from the internet or original texts from publicly available datasets was employed for fine-tuning.

The 7B version of the model is a distilled version of the 14B model, specifically designed for speculative sampling. Therefore, it is important to exercise caution when directly using the model, as it may produce hallucinations or unreliable outputs.

Please note that the model was trained on unfiltered internet data. Since we do not have the capacity to vet all of it, there may be a substantial amount of objectionable content, pornography, violence, and offensive language present that we are unable to remove. Therefore, you will still need to complete your own checks on the model's safety and filter keywords in the output. Due to computational resource constraints, we are presently unable to implement RLHF for the model's ethics and safety, nor training on SFT samples that refuse to answer certain questions for restrictive fine-tuning.

Bonus: The model underwent some fine-tuning on the prompt format introduced in LLaVA1.5 that is unrelated to image attention calculation. Therefore, aligning the ViT Projection module with frozen LM under visual instructions would enable rapid implementation of effective multimodal capabilities.

## PROMPT FORMAT:
[chatml](https://github.com/openai/openai-python/blob/main/chatml.md)

**System Prompt must not be empty!**

## MMLU:
stem ACC: 64.19

Humanities ACC: 61.40

other ACC: 71.64

social ACC: 75.37

**AVERAGE ACC:67.36** (Outperforms ALL models under 70B, very close to those best 70B fine-tunes)


## CEval (Val):
STEM ACC: 66.71

Social Science ACC: 85.10

Humanities ACC: 76.68

Other ACC: 70.23

Hard ACC:54.71

**AVERAGE ACC:73.10** (Outperforms Qwen-14B, and GPT-4)

## GSM8K

**Zero-shot ACC 0.7012888551933283** (Outperforms MetaMath-13B, Qwen-14B)

## AlpacaEval Leaderboard
|              | win_rate | standard_error | n_wins | n_wins_base | n_draws | n_total | mode      | avg_length |
| ------------ | -------- | -------------- | ------ | ----------- | ------- | ------- | --------- | ---------- |
| causallm-14b | **88.26087** | 1.116333       | 705    | 89          | 11      | 805     | community | 1391       |


Win rate **88.26%**	on [AlpacaEval Leaderboard](https://tatsu-lab.github.io/alpaca_eval/) [view raw](https://github.com/tatsu-lab/alpaca_eval/blob/3a47dcd81c56f6a8e6a5711f2754013919fbe90a/results/causallm-14b/model_outputs.json)

**GPT2Tokenizer 上的 llama.cpp 存在一些问题，会尽快修复...**

**llama.cpp GGUF models**
GPT2Tokenizer 支持由 [Kerfuffle](https://github.com/KerfuffleV2) 修复于 [https://github.com/ggerganov/llama.cpp/pull/3743](https://github.com/ggerganov/llama.cpp/pull/3743)，新模型稍后上传。

## 请读我：

另请参阅[7B版本](https://huggingface.co/CausalLM/7B)

该模型是基于Qwen的权重（并使用了LLaMA2权重，是的，用于计算一些权重初始化），您根据情况可能还需要遵守这两个模型的商业使用限制。训练过程中使用了与LLaMA2相同的模型结构，使用原始MHA LLaMA2模型的相同注意力计算方法，对相对位置编码（RoPE）没有进行额外的缩放。

我们手动筛选了一个包含13亿个标记的SFT数据集进行训练，利用了Hugging Face的开源数据集。对于大多数句子，我们进行了手动或合成改写，并使用更大的语言模型生成了其他语言版本。此外，我们还使用了精心挑选的来自维基百科的条目、来自Fandom的精选条目以及来自萌娘百科的过滤条目进行增强文本训练。为了在效率和质量之间取得平衡，训练所使用的100%数据都是合成数据，没有直接使用来自互联网或公开可用数据集的原始文本进行微调。

7B版本的模型是14B模型的精简版本，专门设计用于推测抽样。因此，在直接使用模型时，需要谨慎行事，因为它可能会产生幻觉或不可靠的输出。

请注意，模型是在未经过滤的互联网数据上进行训练的。由于我们无法审核所有数据，可能会出现大量不良内容、色情、暴力和冒犯性语言，我们无法删除这些内容。因此，您仍然需要对模型的安全性进行自己的检查，并对输出中的关键词进行过滤。由于计算资源的限制，我们目前无法为模型的伦理和安全实施RLHF，也无法对拒绝回答某些问题的SFT样本进行训练以进行限制性微调。

额外奖励：模型在LLaVA1.5中引入的提示格式上进行了一些微调，与图像注意力计算无关。因此，将ViT投影模块与冻结的LM对齐，并根据视觉指令实施快速实现有效的多模态能力。

## 提示格式：
[chatml](https://github.com/openai/openai-python/blob/main/chatml.md)

**系统提示不能为空！**


## MMLU：
STEM准确率：64.19

人文及艺术学科准确率：61.40

其他学科准确率：71.64

社会学科准确率：75.37

**平均准确率：67.36**（超过所有70B以下的模型，非常接近最佳70B微调模型）

## CEval（验证集）：
STEM准确率：66.71

社会科学准确率：85.10

人文学科准确率：76.68

其他学科准确率：70.23

困难准确率：54.71

**平均准确率：73.10**（超过Qwen-14B和GPT-4）

## GSM8K

**零样本准确率0.7012888551933283**（超过MetaMath-13B和Qwen-14B）

## AlpacaEval Leaderboard
|              | win_rate | standard_error | n_wins | n_wins_base | n_draws | n_total | mode      | avg_length |
| ------------ | -------- | -------------- | ------ | ----------- | ------- | ------- | --------- | ---------- |
| causallm-14b | **88.26087** | 1.116333       | 705    | 89          | 11      | 805     | community | 1391       |

在 [AlpacaEval Leaderboard](https://tatsu-lab.github.io/alpaca_eval/) 胜率 **88.26%** [view raw](https://github.com/tatsu-lab/alpaca_eval/blob/3a47dcd81c56f6a8e6a5711f2754013919fbe90a/results/causallm-14b/model_outputs.json)

<!-- original-model-card end -->
