---
inference: false
language:
- en
license: other
model_type: llama
pipeline_tag: text-generation
tags:
- facebook
- meta
- pytorch
- llama
- llama-2
---

<!-- header start -->
<div style="width: 100%;">
    <img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p><a href="https://discord.gg/theblokeai">Chat & support: my new Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<!-- header end -->

# Llama 2 70B - GGML
- Model creator: [Meta](https://huggingface.co/meta-llama)
- Original model: [Llama 2 70B](https://huggingface.co/meta-llama/Llama-2-70b)

## Description

This repo contains GGML format model files for [Meta's Llama 2 70B](https://huggingface.co/meta-llama/Llama-2-70b).

## Only compatible with latest llama.cpp

To use these files you need:

1. llama.cpp as of [commit `e76d630`](https://github.com/ggerganov/llama.cpp/commit/e76d630df17e235e6b9ef416c45996765d2e36fb) or later.
 - For users who don't want to compile from source, you can use the binaries from [release master-e76d630](https://github.com/ggerganov/llama.cpp/releases/tag/master-e76d630)
2. to add new command line parameter `-gqa 8`

Example command:
```
./main -m llama-2-70b/ggml/llama-2-70b.ggmlv3.q4_0.bin -gqa 8 -t 13 -p "Llamas are"
```

There is no CUDA support at this time, but it should be coming soon.

There is no support in third-party UIs (eg. text-generation-webui, KoboldCpp), or Python libraries (llama-cpp-python, ctransformers) yet. That will come in due course.

## Repositories available

* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/Llama-2-70B-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU+GPU inference](https://huggingface.co/TheBloke/Llama-2-70B-GGML)
* [Meta's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/meta-llama/Llama-2-70b)

## Prompt template: None

```
{prompt}
```

**Remeber that this is a foundation model, not a fine tuned one. It may not be good at answering questions or following instructions.**

<!-- compatibility_ggml start -->
## Compatibility

### Only compatible with llama.cpp as of commit `e76d630`

Compatible with llama.cpp as of [commit `e76d630`](https://github.com/ggerganov/llama.cpp/commit/e76d630df17e235e6b9ef416c45996765d2e36fb) or later.

For a pre-compiled release, use [release master-e76d630](https://github.com/ggerganov/llama.cpp/releases/tag/master-e76d630) or later.

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
| llama-2-70b.ggmlv3.q2_K.bin | q2_K | 2 | 28.59 GB| 31.09 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.vw and feed_forward.w2 tensors, GGML_TYPE_Q2_K for the other tensors. |
| llama-2-70b.ggmlv3.q3_K_L.bin | q3_K_L | 3 | 36.15 GB| 38.65 GB | New k-quant method. Uses GGML_TYPE_Q5_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| llama-2-70b.ggmlv3.q3_K_M.bin | q3_K_M | 3 | 33.04 GB| 35.54 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| llama-2-70b.ggmlv3.q3_K_S.bin | q3_K_S | 3 | 29.75 GB| 32.25 GB | New k-quant method. Uses GGML_TYPE_Q3_K for all tensors |
| llama-2-70b.ggmlv3.q4_0.bin | q4_0 | 4 | 38.87 GB| 41.37 GB | Original quant method, 4-bit. |
| llama-2-70b.ggmlv3.q4_1.bin | q4_1 | 4 | 43.17 GB| 45.67 GB | Original quant method, 4-bit. Higher accuracy than q4_0 but not as high as q5_0. However has quicker inference than q5 models. |
| llama-2-70b.ggmlv3.q4_K_M.bin | q4_K_M | 4 | 41.38 GB| 43.88 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q4_K |
| llama-2-70b.ggmlv3.q4_K_S.bin | q4_K_S | 4 | 38.87 GB| 41.37 GB | New k-quant method. Uses GGML_TYPE_Q4_K for all tensors |
| llama-2-70b.ggmlv3.q5_0.bin | q5_0 | 5 | 47.46 GB| 49.96 GB | Original quant method, 5-bit. Higher accuracy, higher resource usage and slower inference. |
| llama-2-70b.ggmlv3.q5_K_M.bin | q5_K_M | 5 | 48.75 GB| 51.25 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q5_K |
| llama-2-70b.ggmlv3.q5_K_S.bin | q5_K_S | 5 | 47.46 GB| 49.96 GB | New k-quant method. Uses GGML_TYPE_Q5_K for all tensors |
| llama-2-70b.ggmlv3.q6_K.bin | q6_K | 6 | 56.59 GB | 59.09 GB | New k-quant method. Uses GGML_TYPE_Q8_K - 6-bit quantization - for all tensors |
| llama-2-70b.ggmlv3.q8_0.bin | q8_0 | 8 | 73.23 GB | 75.73 GB | Original llama.cpp quant method, 8-bit. Almost indistinguishable from float16. High resource use and slow. Not recommended for most users. |

### q6_K and q8_0 files require expansion from archive

**Note:** HF does not support uploading files larger than 50GB. Therefore I have uploaded the q6_K and q8_0 files as multi-part ZIP files. They are not compressed, they are just for storing a .bin file in two parts.

### q6_K 
Please download:
* `llama-2-70b.ggmlv3.q6_K.zip`
* `llama-2-70b.ggmlv3.q6_K.z01`

### q8_0
Please download:
* `llama-2-70b.ggmlv3.q8_0.zip`
* `llama-2-70b.ggmlv3.q8_0.z01`

Then extract the .zip archive. This will will expand both parts automatically. On Linux I found I had to use `7zip` - the basic `unzip` tool did not work. Example:
```
sudo apt update -y && sudo apt install 7zip
7zz x llama-2-70b.ggmlv3.q6_K.zip
```

Once the `.bin` is extracted you can delete the `.zip` and `.z01` files.

## How to run in `llama.cpp`

I use the following command line; adjust for your tastes and needs:

```
./main -m llama-2-70b.ggmlv3.q4_0.bin -gqa 8 -t 13 -p "Llamas are"
```
Change `-t 13` to the number of physical CPU cores you have. For example if your system has 8 cores/16 threads, use `-t 8`.

No GPU support is possible yet, but it is coming soon.

<!-- footer start -->
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

**Special thanks to**: Luke from CarbonQuill, Aemon Algiz.

**Patreon special mentions**: Slarti, Chadd, John Detwiler, Pieter, zynix, K, Mano Prime, ReadyPlayerEmma, Ai Maven, Leonard Tan, Edmond Seymore, Joseph William Delisle, Luke @flexchar, Fred von Graf, Viktor Bowallius, Rishabh Srivastava, Nikolai Manek, Matthew Berman, Johann-Peter Hartmann, ya boyyy, Greatston Gnanesh, Femi Adebogun, Talal Aujan, Jonathan Leane, terasurfer, David Flickinger, William Sang, Ajan Kanaga, Vadim, Artur Olbinski, Raven Klaugh, Michael Levine, Oscar Rangel, Randy H, Cory Kujawski, RoA, Dave, Alex, Alexandros Triantafyllidis, Fen Risland, Eugene Pentland, vamX, Elle, Nathan LeClaire, Khalefa Al-Ahmad, Rainer Wilmers, subjectnull, Junyu Yang, Daniel P. Andersen, SuperWojo, LangChain4j, Mandus, Kalila, Illia Dulskyi, Trenton Dambrowitz, Asp the Wyvern, Derek Yates, Jeffrey Morgan, Deep Realms, Imad Khwaja, Pyrater, Preetika Verma, biorpg, Gabriel Tamborski, Stephen Murray, Spiking Neurons AB, Iucharbius, Chris Smitley, Willem Michiel, Luke Pendergrass, Sebastain Graf, senxiiz, Will Dee, Space Cruiser, Karl Bernard, Clay Pascal, Lone Striker, transmissions 11, webtim, WelcomeToTheClub, Sam, theTransient, Pierre Kircher, chris gileta, John Villwock, Sean Connelly, Willian Hasse


Thank you to all my generous patrons and donaters!

<!-- footer end -->

# Original model card: Meta's Llama 2 70B

# **Llama 2**
Llama 2 is a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. This is the repository for the 70B pretrained model. Links to other models can be found in the index at the bottom.

## Model Details
*Note: Use of this model is governed by the Meta license. In order to download the model weights and tokenizer, please visit the [website](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) and accept our License before requesting access here.*

Meta developed and publicly released the Llama 2 family of large language models (LLMs), a collection of pretrained and fine-tuned generative text models ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called Llama-2-Chat, are optimized for dialogue use cases. Llama-2-Chat models outperform open-source chat models on most benchmarks we tested, and in our human evaluations for helpfulness and safety, are on par with some popular closed-source models like ChatGPT and PaLM.

**Model Developers** Meta

**Variations** Llama 2 comes in a range of parameter sizes — 7B, 13B, and 70B — as well as pretrained and fine-tuned variations.

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture** Llama 2 is an auto-regressive language model that uses an optimized transformer architecture. The tuned versions use supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align to human preferences for helpfulness and safety.


||Training Data|Params|Content Length|GQA|Tokens|LR|
|---|---|---|---|---|---|---|
|Llama 2|*A new mix of publicly available online data*|7B|4k|&#10007;|2.0T|3.0 x 10<sup>-4</sup>|
|Llama 2|*A new mix of publicly available online data*|13B|4k|&#10007;|2.0T|3.0 x 10<sup>-4</sup>|
|Llama 2|*A new mix of publicly available online data*|70B|4k|&#10004;|2.0T|1.5 x 10<sup>-4</sup>|

*Llama 2 family of models.* Token counts refer to pretraining data only. All models are trained with a global batch-size of 4M tokens. Bigger models -  70B -- use Grouped-Query Attention (GQA) for improved inference scalability.

**Model Dates** Llama 2 was trained between January 2023 and July 2023.

**Status** This is a static model trained on an offline dataset. Future versions of the tuned models will be released as we improve model safety with community feedback.

**License** A custom commercial license is available at: [https://ai.meta.com/resources/models-and-libraries/llama-downloads/](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)

**Research Paper** ["Llama-2: Open Foundation and Fine-tuned Chat Models"](arxiv.org/abs/2307.09288)

## Intended Use
**Intended Use Cases** Llama 2 is intended for commercial and research use in English. Tuned models are intended for assistant-like chat, whereas pretrained models can be adapted for a variety of natural language generation tasks.

To get the expected features and performance for the chat versions, a specific formatting needs to be followed, including the `INST` and `<<SYS>>` tags, `BOS` and `EOS` tokens, and the whitespaces and breaklines in between (we recommend calling `strip()` on inputs to avoid double-spaces). See our reference code in github for details: [`chat_completion`](https://github.com/facebookresearch/llama/blob/main/llama/generation.py#L212).

**Out-of-scope Uses** Use in any manner that violates applicable laws or regulations (including trade compliance laws).Use in languages other than English. Use in any other way that is prohibited by the Acceptable Use Policy and Licensing Agreement for Llama 2.

## Hardware and Software
**Training Factors** We used custom training libraries, Meta's Research Super Cluster, and production clusters for pretraining. Fine-tuning, annotation, and evaluation were also performed on third-party cloud compute.

**Carbon Footprint** Pretraining utilized a cumulative 3.3M GPU hours of computation on hardware of type A100-80GB (TDP of 350-400W). Estimated total emissions were 539 tCO2eq, 100% of which were offset by Meta’s sustainability program.

||Time (GPU hours)|Power Consumption (W)|Carbon Emitted(tCO<sub>2</sub>eq)|
|---|---|---|---|
|Llama 2 7B|184320|400|31.22|
|Llama 2 13B|368640|400|62.44|
|Llama 2 70B|1720320|400|291.42|
|Total|3311616||539.00|

**CO<sub>2</sub> emissions during pretraining.** Time: total GPU time required for training each model. Power Consumption: peak power capacity per GPU device for the GPUs used adjusted for power usage efficiency. 100% of the emissions are directly offset by Meta's sustainability program, and because we are openly releasing these models, the pretraining costs do not need to be incurred by others.

## Training Data
**Overview** Llama 2 was pretrained on 2 trillion tokens of data from publicly available sources. The fine-tuning data includes publicly available instruction datasets, as well as over one million new human-annotated examples. Neither the pretraining nor the fine-tuning datasets include Meta user data.

**Data Freshness** The pretraining data has a cutoff of September 2022, but some tuning data is more recent, up to July 2023.

## Evaluation Results

In this section, we report the results for the Llama 1 and Llama 2 models on standard academic benchmarks.For all the evaluations, we use our internal evaluations library.

|Model|Size|Code|Commonsense Reasoning|World Knowledge|Reading Comprehension|Math|MMLU|BBH|AGI Eval|
|---|---|---|---|---|---|---|---|---|---|
|Llama 1|7B|14.1|60.8|46.2|58.5|6.95|35.1|30.3|23.9|
|Llama 1|13B|18.9|66.1|52.6|62.3|10.9|46.9|37.0|33.9|
|Llama 1|33B|26.0|70.0|58.4|67.6|21.4|57.8|39.8|41.7|
|Llama 1|65B|30.7|70.7|60.5|68.6|30.8|63.4|43.5|47.6|
|Llama 2|7B|16.8|63.9|48.9|61.3|14.6|45.3|32.6|29.3|
|Llama 2|13B|24.5|66.9|55.4|65.8|28.7|54.8|39.4|39.1|
|Llama 2|70B|**37.5**|**71.9**|**63.6**|**69.4**|**35.2**|**68.9**|**51.2**|**54.2**|

**Overall performance on grouped academic benchmarks.** *Code:* We report the average pass@1 scores of our models on HumanEval and MBPP. *Commonsense Reasoning:* We report the average of PIQA, SIQA, HellaSwag, WinoGrande, ARC easy and challenge, OpenBookQA, and CommonsenseQA. We report 7-shot results for CommonSenseQA and 0-shot results for all other benchmarks. *World Knowledge:* We evaluate the 5-shot performance on NaturalQuestions and TriviaQA and report the average. *Reading Comprehension:* For reading comprehension, we report the 0-shot average on SQuAD, QuAC, and BoolQ. *MATH:* We report the average of the GSM8K (8 shot) and MATH (4 shot) benchmarks at top 1.

|||TruthfulQA|Toxigen|
|---|---|---|---|
|Llama 1|7B|27.42|23.00|
|Llama 1|13B|41.74|23.08|
|Llama 1|33B|44.19|22.57|
|Llama 1|65B|48.71|21.77|
|Llama 2|7B|33.29|**21.25**|
|Llama 2|13B|41.86|26.10|
|Llama 2|70B|**50.18**|24.60|

**Evaluation of pretrained LLMs on automatic safety benchmarks.** For TruthfulQA, we present the percentage of generations that are both truthful and informative (the higher the better). For ToxiGen, we present the percentage of toxic generations (the smaller the better).


|||TruthfulQA|Toxigen|
|---|---|---|---|
|Llama-2-Chat|7B|57.04|**0.00**|
|Llama-2-Chat|13B|62.18|**0.00**|
|Llama-2-Chat|70B|**64.14**|0.01|

**Evaluation of fine-tuned LLMs on different safety datasets.** Same metric definitions as above.

## Ethical Considerations and Limitations
Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their specific applications of the model.

Please see the Responsible Use Guide available at [https://ai.meta.com/llama/responsible-use-guide/](https://ai.meta.com/llama/responsible-use-guide)

## Reporting Issues
Please report any software “bug,” or other problems with the models through one of the following means:
- Reporting issues with the model: [github.com/facebookresearch/llama](http://github.com/facebookresearch/llama)
- Reporting problematic content generated by the model: [developers.facebook.com/llama_output_feedback](http://developers.facebook.com/llama_output_feedback)
- Reporting bugs and security concerns: [facebook.com/whitehat/info](http://facebook.com/whitehat/info)

## Llama Model Index
|Model|Llama2|Llama2-hf|Llama2-chat|Llama2-chat-hf|
|---|---|---|---|---|
|7B| [Link](https://huggingface.co/llamaste/Llama-2-7b) | [Link](https://huggingface.co/llamaste/Llama-2-7b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-7b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-7b-chat-hf)|
|13B| [Link](https://huggingface.co/llamaste/Llama-2-13b) | [Link](https://huggingface.co/llamaste/Llama-2-13b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-13b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-13b-hf)|
|70B| [Link](https://huggingface.co/llamaste/Llama-2-70b) | [Link](https://huggingface.co/llamaste/Llama-2-70b-hf) | [Link](https://huggingface.co/llamaste/Llama-2-70b-chat) | [Link](https://huggingface.co/llamaste/Llama-2-70b-hf)|
