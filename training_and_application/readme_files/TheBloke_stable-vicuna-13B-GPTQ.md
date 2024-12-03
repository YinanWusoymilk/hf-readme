---
language:
  - en
tags:
  - causal-lm
  - llama
license: cc-by-nc-sa-4.0
datasets:
  - OpenAssistant/oasst1
  - nomic-ai/gpt4all_prompt_generations
  - tatsu-lab/alpaca
inference: false
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

# StableVicuna-13B-GPTQ

This repo contains 4bit GPTQ format quantised models of [CarperAI's StableVicuna 13B](https://huggingface.co/CarperAI/stable-vicuna-13b-delta).

It is the result of first merging the deltas from the above repository with the original Llama 13B weights, then quantising to 4bit using [GPTQ-for-LLaMa](https://github.com/qwopqwop200/GPTQ-for-LLaMa).

## Repositories available

* [4bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/stable-vicuna-13B-GPTQ).
* [4-bit, 5-bit and 8-bit GGML models for CPU (+CUDA) inference](https://huggingface.co/TheBloke/stable-vicuna-13B-GGML).
* [Unquantised float16 model in HF format](https://huggingface.co/TheBloke/stable-vicuna-13B-HF).

## PROMPT TEMPLATE

This model works best with the following prompt template:

```
### Human: your prompt here
### Assistant:
```

## How to easily download and use this model in text-generation-webui

Open the text-generation-webui UI as normal.

1. Click the **Model tab**.
2. Under **Download custom model or LoRA**, enter `TheBloke/stable-vicuna-13B-GPTQ`.
3. Click **Download**.
4. Wait until it says it's finished downloading.
5. Click the **Refresh** icon next to **Model** in the top left.
6. In the **Model drop-down**: choose the model you just downloaded,`stable-vicuna-13B-GPTQ`.
7. Once it says it's loaded, click the **Text Generation tab** and enter a prompt!

## Provided files

I have uploaded two versions of the GPTQ.

**Compatible file - stable-vicuna-13B-GPTQ-4bit.compat.no-act-order.safetensors**

In the `main` branch - the default one - you will find `stable-vicuna-13B-GPTQ-4bit.compat.no-act-order.safetensors`

This will work with all versions of GPTQ-for-LLaMa. It has maximum compatibility

It was created without the `--act-order` parameter. It may have slightly lower inference quality compared to the other file, but is guaranteed to work on all versions of GPTQ-for-LLaMa and text-generation-webui.

* `stable-vicuna-13B-GPTQ-4bit.compat.no-act-order.safetensors`
  * Works with all versions of GPTQ-for-LLaMa code, both Triton and CUDA branches
  * Works with text-generation-webui one-click-installers
  * Parameters: Groupsize = 128g. No act-order.
  * Command used to create the GPTQ:
    ```
    CUDA_VISIBLE_DEVICES=0 python3 llama.py stable-vicuna-13B-HF c4 --wbits 4 --true-sequential --groupsize 128 --save_safetensors stable-vicuna-13B-GPTQ-4bit.no-act-order.safetensors
    ```

**Latest file - stable-vicuna-13B-GPTQ-4bit.latest.act-order.safetensors**

Created for more recent versions of GPTQ-for-LLaMa, and uses the `--act-order` flag for maximum theoretical performance.

To access this file, please switch to the `latest` branch fo this repo and download from there.

* `stable-vicuna-13B-GPTQ-4bit.latest.act-order.safetensors`
  * Only works with recent GPTQ-for-LLaMa code
  * **Does not** work with text-generation-webui one-click-installers
  * Parameters: Groupsize = 128g. **act-order**.
  * Offers highest quality quantisation, but requires recent GPTQ-for-LLaMa code
  * Command used to create the GPTQ:
    ```
    CUDA_VISIBLE_DEVICES=0 python3 llama.py stable-vicuna-13B-HF c4 --wbits 4 --true-sequential --act-order --groupsize 128 --save_safetensors stable-vicuna-13B-GPTQ-4bit.act-order.safetensors
    ```

## Manual instructions for `text-generation-webui`

File `stable-vicuna-13B-GPTQ-4bit.compat.no-act-order.safetensors` can be loaded the same as any other GPTQ file, without requiring any updates to [oobaboogas text-generation-webui](https://github.com/oobabooga/text-generation-webui).

[Instructions on using GPTQ 4bit files in text-generation-webui are here](https://github.com/oobabooga/text-generation-webui/wiki/GPTQ-models-\(4-bit-mode\)).

The other `safetensors` model file was created using `--act-order` to give the maximum possible quantisation quality, but this means it requires that the latest GPTQ-for-LLaMa is used inside the UI.

If you want to use the act-order `safetensors` files and need to update the Triton branch of GPTQ-for-LLaMa, here are the commands I used to clone the Triton branch of GPTQ-for-LLaMa, clone text-generation-webui, and install GPTQ into the UI:
```
# Clone text-generation-webui, if you don't already have it
git clone https://github.com/oobabooga/text-generation-webui
# Make a repositories directory
mkdir text-generation-webui/repositories
cd text-generation-webui/repositories
# Clone the latest GPTQ-for-LLaMa code inside text-generation-webui
git clone https://github.com/qwopqwop200/GPTQ-for-LLaMa
```

Then install this model into `text-generation-webui/models` and launch the UI as follows:
```
cd text-generation-webui
python server.py --model stable-vicuna-13B-GPTQ --wbits 4 --groupsize 128 --model_type Llama # add any other command line args you want
```

The above commands assume you have installed all dependencies for GPTQ-for-LLaMa and text-generation-webui. Please see their respective repositories for further information.

If you can't update GPTQ-for-LLaMa or don't want to, you can use `stable-vicuna-13B-GPTQ-4bit.no-act-order.safetensors` as mentioned above, which should work without any upgrades to text-generation-webui.

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

**Patreon special mentions**: Sam, theTransient, Jonathan Leane, Steven Wood, webtim, Johann-Peter Hartmann, Geoffrey Montalvo, Gabriel Tamborski, Willem Michiel, John Villwock, Derek Yates, Mesiah Bishop, Eugene Pentland, Pieter, Chadd, Stephen Murray, Daniel P. Andersen, terasurfer, Brandon Frisco, Thomas Belote, Sid, Nathan LeClaire, Magnesian, Alps Aficionado, Stanislav Ovsiannikov, Alex, Joseph William Delisle, Nikolai Manek, Michael Davis, Junyu Yang, K, J, Spencer Kim, Stefan Sabev, Olusegun Samson, transmissions 11, Michael Levine, Cory Kujawski, Rainer Wilmers, zynix, Kalila, Luke @flexchar, Ajan Kanaga, Mandus, vamX, Ai Maven, Mano Prime, Matthew Berman, subjectnull, Vitor Caleffi, Clay Pascal, biorpg, alfie_i, 阿明, Jeffrey Morgan, ya boyyy, Raymond Fosdick, knownsqashed, Olakabola, Leonard Tan, ReadyPlayerEmma, Enrico Ros, Dave, Talal Aujan, Illia Dulskyi, Sean Connelly, senxiiz, Artur Olbinski, Elle, Raven Klaugh, Fen Risland, Deep Realms, Imad Khwaja, Fred von Graf, Will Dee, usrbinkat, SuperWojo, Alexandros Triantafyllidis, Swaroop Kallakuri, Dan Guido, John Detwiler, Pedro Madruga, Iucharbius, Viktor Bowallius, Asp the Wyvern, Edmond Seymore, Trenton Dambrowitz, Space Cruiser, Spiking Neurons AB, Pyrater, LangChain4j, Tony Hughes, Kacper Wikieł, Rishabh Srivastava, David Ziegler, Luke Pendergrass, Andrey, Gabriel Puliatti, Lone Striker, Sebastain Graf, Pierre Kircher, Randy H, NimbleBox.ai, Vadim, danny, Deo Leter


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->
# Original StableVicuna-13B model card

## Model Description

StableVicuna-13B is a [Vicuna-13B v0](https://huggingface.co/lmsys/vicuna-13b-delta-v0) model fine-tuned using reinforcement learning from human feedback (RLHF) via Proximal Policy Optimization (PPO) on various conversational and instructional datasets.

## Model Details

* **Trained by**: [Duy Phung](https://github.com/PhungVanDuy) of [CarperAI](https://carper.ai)
* **Model type:**  **StableVicuna-13B** is an auto-regressive language model based on the LLaMA transformer architecture.
* **Language(s)**: English
* **Library**: [trlX](https://github.com/CarperAI/trlx)
* **License for delta weights**: [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
  * *Note*: License for the base LLaMA model's weights is Meta's [non-commercial bespoke license](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md).
* **Contact**: For questions and comments about the model, visit the [CarperAI](https://discord.com/invite/KgfkCVYHdu) and [StableFoundation](https://discord.gg/stablediffusion) Discord servers.

| Hyperparameter            | Value |
|---------------------------|-------|
| \\(n_\text{parameters}\\) | 13B   |
| \\(d_\text{model}\\)      | 5120  |
| \\(n_\text{layers}\\)     | 40    |
| \\(n_\text{heads}\\)      | 40    |

## Training

### Training Dataset

StableVicuna-13B is fine-tuned on a mix of three datasets. [OpenAssistant Conversations Dataset (OASST1)](https://huggingface.co/datasets/OpenAssistant/oasst1), a human-generated, human-annotated assistant-style conversation corpus consisting of 161,443 messages distributed across 66,497 conversation trees, in 35 different languages;
[GPT4All Prompt Generations](https://huggingface.co/datasets/nomic-ai/gpt4all_prompt_generations), a dataset of 400k prompts and responses generated by GPT-4; and [Alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca),  a dataset of 52,000 instructions and demonstrations generated by OpenAI's text-davinci-003 engine.

The reward model used during RLHF was also trained on [OpenAssistant Conversations Dataset (OASST1)](https://huggingface.co/datasets/OpenAssistant/oasst1) along with two other datasets: [Anthropic HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf), a dataset of preferences about AI assistant helpfulness and harmlessness; and [Stanford Human Preferences Dataset](https://huggingface.co/datasets/stanfordnlp/SHP) a dataset of 385K collective human preferences over responses to questions/instructions in 18 different subject areas, from cooking to legal advice.

### Training Procedure

`CarperAI/stable-vicuna-13b-delta` was trained using PPO as implemented in [`trlX`](https://github.com/CarperAI/trlx/blob/main/trlx/trainer/accelerate_ppo_trainer.py) with the following configuration:

|  Hyperparameter   |  Value  |
|-------------------|---------|
| num_rollouts      | 128     |
| chunk_size        | 16      |
| ppo_epochs        | 4       |
| init_kl_coef      | 0.1     |
| target            | 6       |
| horizon           | 10000   |
| gamma             | 1       |
| lam               | 0.95    |
| cliprange         | 0.2     |
| cliprange_value   | 0.2     |
| vf_coef           | 1.0     |
| scale_reward      | None    |
| cliprange_reward  | 10      |
| generation_kwargs |         |
| max_length        | 512     |
| min_length        | 48      |
| top_k             | 0.0     |
| top_p             | 1.0     |
| do_sample         | True    |
| temperature       | 1.0     |

## Use and Limitations

### Intended Use

This model is intended to be used for text generation with a focus on conversational tasks. Users may further fine-tune the model on their own data to improve the model's performance on their specific tasks in accordance with the non-commercial [license](https://creativecommons.org/licenses/by-nc/4.0/).

### Limitations and bias

The base LLaMA model is trained on various data, some of which may contain offensive, harmful, and biased content that can lead to toxic behavior. See Section 5.1 of the LLaMA [paper](https://arxiv.org/abs/2302.13971). We have not performed any studies to determine how fine-tuning on the aforementioned datasets affect the model's behavior and toxicity. Do not treat chat responses from this model as a substitute for human judgment or as a source of truth. Please use responsibly.

## Acknowledgements

This work would not have been possible without the support of [Stability AI](https://stability.ai/).

## Citations

```bibtex
@article{touvron2023llama,
  title={LLaMA: Open and Efficient Foundation Language Models},
  author={Touvron, Hugo and Lavril, Thibaut and Izacard, Gautier and Martinet, Xavier and Lachaux, Marie-Anne and Lacroix, Timoth{\'e}e and Rozi{\`e}re, Baptiste and Goyal, Naman and Hambro, Eric and Azhar, Faisal and Rodriguez, Aurelien and Joulin, Armand and Grave, Edouard and Lample, Guillaume},
  journal={arXiv preprint arXiv:2302.13971},
  year={2023}
}
```

```bibtex
@misc{vicuna2023,
    title = {Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90%* ChatGPT Quality},
    url = {https://vicuna.lmsys.org},
    author = {Chiang, Wei-Lin and Li, Zhuohan and Lin, Zi and Sheng, Ying and Wu, Zhanghao and Zhang, Hao and Zheng, Lianmin and Zhuang, Siyuan and Zhuang, Yonghao and Gonzalez, Joseph E. and Stoica, Ion and Xing, Eric P.},
    month = {March},
    year = {2023}
}
```

```bibtex
@misc{gpt4all,
  author = {Yuvanesh Anand and Zach Nussbaum and Brandon Duderstadt and Benjamin Schmidt and Andriy Mulyar},
  title = {GPT4All: Training an Assistant-style Chatbot with Large Scale Data Distillation from GPT-3.5-Turbo},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/nomic-ai/gpt4all}},
}
```

```bibtex
@misc{alpaca,
  author = {Rohan Taori and Ishaan Gulrajani and Tianyi Zhang and Yann Dubois and Xuechen Li and Carlos Guestrin and Percy Liang and Tatsunori B. Hashimoto },
  title = {Stanford Alpaca: An Instruction-following LLaMA model},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/tatsu-lab/stanford_alpaca}},
}
```

```bibtex
@software{leandro_von_werra_2023_7790115,
  author       = {Leandro von Werra and
                  Alex Havrilla and
                  Max reciprocated and
                  Jonathan Tow and
                  Aman cat-state and
                  Duy V. Phung and
                  Louis Castricato and
                  Shahbuland Matiana and
                  Alan and
                  Ayush Thakur and
                  Alexey Bukhtiyarov and
                  aaronrmm and
                  Fabrizio Milo and
                  Daniel and
                  Daniel King and
                  Dong Shin and
                  Ethan Kim and
                  Justin Wei and
                  Manuel Romero and
                  Nicky Pochinkov and
                  Omar Sanseviero and
                  Reshinth Adithyan and
                  Sherman Siu and
                  Thomas Simonini and
                  Vladimir Blagojevic and
                  Xu Song and
                  Zack Witten and
                  alexandremuzio and
                  crumb},
  title        = {{CarperAI/trlx: v0.6.0: LLaMa (Alpaca), Benchmark
                   Util, T5 ILQL, Tests}},
  month        = mar,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v0.6.0},
  doi          = {10.5281/zenodo.7790115},
  url          = {https://doi.org/10.5281/zenodo.7790115}
}
```
