---
inference: false
license: other
---

<!-- header start -->
<div style="width: 100%;">
    <img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p><a href="https://discord.gg/Jq4vkcDakD">Chat & support: my new Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<!-- header end -->

# CarperAI's Stable Vicuna 13B GGML

These files are GGML format model files for [CarperAI's Stable Vicuna 13B](https://huggingface.co/CarperAI/stable-vicuna-13b-delta).

GGML files are for CPU + GPU inference using [llama.cpp](https://github.com/ggerganov/llama.cpp) and libraries and UIs which support this format, such as:
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui)
* [KoboldCpp](https://github.com/LostRuins/koboldcpp)
* [ParisNeo/GPT4All-UI](https://github.com/ParisNeo/gpt4all-ui)
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
* [ctransformers](https://github.com/marella/ctransformers)

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/stable-vicuna-13B-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU+GPU inference](https://huggingface.co/TheBloke/stable-vicuna-13B-GGML)
* [Unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/TheBloke/stable-vicuna-13B-HF)

<!-- compatibility_ggml start -->
## Compatibility

### Original llama.cpp quant methods: `q4_0, q4_1, q5_0, q5_1, q8_0`

I have quantized these 'original' quantisation methods using an older version of llama.cpp so that they remain compatible with llama.cpp as of May 19th, commit `2d5db48`.

They should be compatible with all current UIs and libraries that use llama.cpp, such as those listed at the top of this README.

### New k-quant methods: `q2_K, q3_K_S, q3_K_M, q3_K_L, q4_K_S, q4_K_M, q5_K_S, q6_K`

These new quantisation methods are only compatible with llama.cpp as of June 6th, commit `2d43387`.

They will NOT be compatible with koboldcpp, text-generation-ui, and other UIs and libraries yet. Support is expected to come over the next few days.

## Explanation of the new k-quant methods

The new methods available are:
* GGML_TYPE_Q2_K - "type-1" 2-bit quantization in super-blocks containing 16 blocks, each block having 16 weight. Block scales and mins are quantized with 4 bits. This ends up effectively using 2.5625 bits per weight (bpw)
* GGML_TYPE_Q3_K - "type-0" 3-bit quantization in super-blocks containing 16 blocks, each block having 16 weights. Scales are quantized with 6 bits. This end up using 3.4375 bpw.
* GGML_TYPE_Q4_K - "type-1" 4-bit quantization in super-blocks containing 8 blocks, each block having 32 weights. Scales and mins are quantized with 6 bits. This ends up using 4.5 bpw.
* GGML_TYPE_Q5_K - "type-1" 5-bit quantization. Same super-block structure as GGML_TYPE_Q4_K resulting in 5.5 bpw
* GGML_TYPE_Q6_K - "type-0" 6-bit quantization. Super-blocks with 16 blocks, each block having 16 weights. Scales are quantized with 8 bits. This ends up using 6.5625 bpw
* GGML_TYPE_Q8_K - "type-0" 8-bit quantization. Only used for quantizing intermediate results. The difference to the existing Q8_0 is that the block size is 256. All 2-6 bit dot products are implemented for this quantization type.

Refer to the Provided Files table below to see what files use which methods, and how.
<!-- compatibility_ggml end -->

## Provided files
| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| stable-vicuna-13B.ggmlv3.q2_K.bin | q2_K | 2 | 5.43 GB | 7.93 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.vw and feed_forward.w2 tensors, GGML_TYPE_Q2_K for the other tensors. |
| stable-vicuna-13B.ggmlv3.q3_K_L.bin | q3_K_L | 3 | 6.87 GB | 9.37 GB | New k-quant method. Uses GGML_TYPE_Q5_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| stable-vicuna-13B.ggmlv3.q3_K_M.bin | q3_K_M | 3 | 6.25 GB | 8.75 GB | New k-quant method. Uses GGML_TYPE_Q4_K for the attention.wv, attention.wo, and feed_forward.w2 tensors, else GGML_TYPE_Q3_K |
| stable-vicuna-13B.ggmlv3.q3_K_S.bin | q3_K_S | 3 | 5.59 GB | 8.09 GB | New k-quant method. Uses GGML_TYPE_Q3_K for all tensors |
| stable-vicuna-13B.ggmlv3.q4_0.bin | q4_0 | 4 | 7.32 GB | 9.82 GB | Original llama.cpp quant method, 4-bit. |
| stable-vicuna-13B.ggmlv3.q4_1.bin | q4_1 | 4 | 8.14 GB | 10.64 GB | Original llama.cpp quant method, 4-bit. Higher accuracy than q4_0 but not as high as q5_0. However has quicker inference than q5 models. |
| stable-vicuna-13B.ggmlv3.q4_K_M.bin | q4_K_M | 4 | 7.82 GB | 10.32 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q4_K |
| stable-vicuna-13B.ggmlv3.q4_K_S.bin | q4_K_S | 4 | 7.32 GB | 9.82 GB | New k-quant method. Uses GGML_TYPE_Q4_K for all tensors |
| stable-vicuna-13B.ggmlv3.q5_0.bin | q5_0 | 5 | 8.95 GB | 11.45 GB | Original llama.cpp quant method, 5-bit. Higher accuracy, higher resource usage and slower inference. |
| stable-vicuna-13B.ggmlv3.q5_1.bin | q5_1 | 5 | 9.76 GB | 12.26 GB | Original llama.cpp quant method, 5-bit. Even higher accuracy, resource usage and slower inference. |
| stable-vicuna-13B.ggmlv3.q5_K_M.bin | q5_K_M | 5 | 9.21 GB | 11.71 GB | New k-quant method. Uses GGML_TYPE_Q6_K for half of the attention.wv and feed_forward.w2 tensors, else GGML_TYPE_Q5_K |
| stable-vicuna-13B.ggmlv3.q5_K_S.bin | q5_K_S | 5 | 8.95 GB | 11.45 GB | New k-quant method. Uses GGML_TYPE_Q5_K for all tensors |
| stable-vicuna-13B.ggmlv3.q6_K.bin | q6_K | 6 | 10.68 GB | 13.18 GB | New k-quant method. Uses GGML_TYPE_Q8_K - 6-bit quantization - for all tensors |
| stable-vicuna-13B.ggmlv3.q8_0.bin | q8_0 | 8 | 13.83 GB | 16.33 GB | Original llama.cpp quant method, 8-bit. Almost indistinguishable from float16. High resource use and slow. Not recommended for most users. |


**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

## How to run in `llama.cpp`

I use the following command line; adjust for your tastes and needs:

```
./main -t 10 -ngl 32 -m stable-vicuna-13B.ggmlv3.q5_0.bin --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "### Instruction: Write a story about llamas\n### Response:"
```
Change `-t 10` to the number of physical CPU cores you have. For example if your system has 8 cores/16 threads, use `-t 8`.

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

## How to run in `text-generation-webui`

Further instructions here: [text-generation-webui/docs/llama.cpp-models.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/llama.cpp-models.md).

<!-- footer start -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[TheBloke AI's Discord server](https://discord.gg/Jq4vkcDakD)

## Thanks, and how to contribute.

Thanks to the [chirper.ai](https://chirper.ai) team!

I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.

Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.

* Patreon: https://patreon.com/TheBlokeAI
* Ko-Fi: https://ko-fi.com/TheBlokeAI

**Special thanks to**: Luke from CarbonQuill, Aemon Algiz, Dmitriy Samsonov.

**Patreon special mentions**: Oscar Rangel, Eugene Pentland, Talal Aujan, Cory Kujawski, Luke, Asp the Wyvern, Ai Maven, Pyrater, Alps Aficionado, senxiiz, Willem Michiel, Junyu Yang, trip7s trip, Sebastain Graf, Joseph William Delisle, Lone Striker, Jonathan Leane, Johann-Peter Hartmann, David Flickinger, Spiking Neurons AB, Kevin Schuppel, Mano Prime, Dmitriy Samsonov, Sean Connelly, Nathan LeClaire, Alain Rossmann, Fen Risland, Derek Yates, Luke Pendergrass, Nikolai Manek, Khalefa Al-Ahmad, Artur Olbinski, John Detwiler, Ajan Kanaga, Imad Khwaja, Trenton Dambrowitz, Kalila, vamX, webtim, Illia Dulskyi.

Thank you to all my generous patrons and donaters!

<!-- footer end -->

# Original model card: CarperAI's Stable Vicuna 13B


# StableVicuna-13B

## Model Description

StableVicuna-13B is a [Vicuna-13B v0](https://huggingface.co/lmsys/vicuna-13b-delta-v0) model fine-tuned using reinforcement learning from human feedback (RLHF) via Proximal Policy Optimization (PPO) on various conversational and instructional datasets.

### Apply Delta Weights

StableVicuna-13B cannot be used from the `CarperAI/stable-vicuna-13b-delta` weights alone. To obtain the correct model, one must add back the difference between LLaMA 13B and `CarperAI/stable-vicuna-13b-delta` weights. We provide the [`apply_delta.py`](https://huggingface.co/CarperAI/stable-vicuna-13b-delta/raw/main/apply_delta.py) script to automate the conversion, which you can run as:

```sh
python3 apply_delta.py --base /path/to/model_weights/llama-13b --target stable-vicuna-13b --delta CarperAI/stable-vicuna-13b-delta
```


## Usage

Once the delta weights are applied, get started chatting with the model by using the [`transformers`](https://huggingface.co/docs/transformers) library. Following a suggestion from Vicuna Team with Vicuna v0 you should install transformers with this version:

```sh
pip install git+https://github.com/huggingface/transformers@c612628045822f909020f7eb6784c79700813eda
```

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("path/to/stable-vicuna-13b-applied")
model = AutoModelForCausalLM.from_pretrained("path/to/stable-vicuna-13b-applied")
model.half().cuda()

prompt = """\
### Human: Write a Python script for text classification using Transformers and PyTorch
### Assistant:\
"""

inputs = tokenizer(prompt, return_tensors='pt').to('cuda')
tokens = model.generate(
 **inputs,
 max_new_tokens=256,
 do_sample=True,
 temperature=1.0,
 top_p=1.0,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
```

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
