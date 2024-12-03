---
license: cc-by-nc-sa-4.0
datasets:
- camel-ai/code
- ehartford/wizard_vicuna_70k_unfiltered
- anon8231489123/ShareGPT_Vicuna_unfiltered
- teknium1/GPTeacher/roleplay-instruct-v2-final
- teknium1/GPTeacher/codegen-isntruct
- timdettmers/openassistant-guanaco
- camel-ai/math
- project-baize/baize-chatbot/medical_chat_data
- project-baize/baize-chatbot/quora_chat_data
- project-baize/baize-chatbot/stackoverflow_chat_data
- camel-ai/biology
- camel-ai/chemistry
- camel-ai/ai_society
- jondurbin/airoboros-gpt4-1.2
- LongConversations
- camel-ai/physics
tags:
- Composer
- MosaicML
- llm-foundry
inference: false
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

# MosaicML's MPT-30B-Chat GGML

These files are GGML format model files for [MosaicML's MPT-30B-Chat](https://huggingface.co/mosaicml/mpt-30b-chat).

Please note that these GGMLs are **not compatible with llama.cpp, or currently with text-generation-webui**. Please see below for a list of tools known to work with these model files.

[KoboldCpp](https://github.com/LostRuins/koboldcpp) just added GPU accelerated (OpenCL) support for MPT models, so that is the client I recommend using for these models.

**Note**: Please make sure you're using KoboldCpp version 1.32.3 or later, as a number of MPT-related bugs are fixed.

## Repositories available

* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU+GPU inference](https://huggingface.co/TheBloke/mpt-30B-chat-GGML)
* [Unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/mosaicml/mpt-30b-chat)

## Prompt template

Based on the code for the MPT 30B Chat Space, I believe this is the correct prompt template:

```
<|im_start|>system
A conversation between a user and an LLM-based AI assistant. The assistant gives helpful and honest answers.<|im_end|>
<|im_start|>user
prompt goes here<|im_end|>
<|im_start|>assistant
```

## A note regarding context length: 8K

The base model has an 8K context length. It is not yet confirmed if the 8K context of this model works with the quantised files.

If it does, [KoboldCpp](https://github.com/LostRuins/koboldcpp) supports 8K context if you manually set it to 8K by adjusting the text box above the slider:
![.](https://i.imgur.com/tEbpeJqm.png)

It is currently unknown as to increased context is compatible with other MPT GGML clients.

If you have feedback on this, please let me know.

<!-- compatibility_ggml start -->
## Compatibilty

These files are **not** compatible with text-generation-webui, llama.cpp, or llama-cpp-python.

Currently they can be used with:
* KoboldCpp, a powerful inference engine based on llama.cpp, with good UI and GPU accelerated support for MPT models: [KoboldCpp](https://github.com/LostRuins/koboldcpp)
* The ctransformers Python library, which includes LangChain support: [ctransformers](https://github.com/marella/ctransformers)
* The LoLLMS Web UI which uses ctransformers: [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui)
* [rustformers' llm](https://github.com/rustformers/llm)
* The example `mpt` binary provided with [ggml](https://github.com/ggerganov/ggml)

As other options become available I will endeavour to update them here (do let me know in the Community tab if I've missed something!)

## Tutorial for using LoLLMS Web UI

* [Text tutorial, written by **Lucas3DCG**](https://huggingface.co/TheBloke/MPT-7B-Storywriter-GGML/discussions/2#6475d914e9b57ce0caa68888)
* [Video tutorial, by LoLLMS Web UI's author **ParisNeo**](https://www.youtube.com/watch?v=ds_U0TDzbzI)

<!-- compatibility_ggml end -->

## Provided files
| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| mpt-30b-chat.ggmlv0.q4_0.bin | q4_0 | 4 | 16.85 GB | 19.35 GB | 4-bit. |
| mpt-30b-chat.ggmlv0.q4_1.bin | q4_1 | 4 | 18.73 GB | 21.23 GB | 4-bit. Higher accuracy than q4_0 but not as high as q5_0. However has quicker inference than q5 models. |
| mpt-30b-chat.ggmlv0.q5_0.bin | q5_0 | 5 | 20.60 GB | 23.10 GB | 5-bit. Higher accuracy, higher resource usage and slower inference. |
| mpt-30b-chat.ggmlv0.q5_1.bin | q5_1 | 5 | 22.47 GB | 24.97 GB | 5-bit. Even higher accuracy, resource usage and slower inference. |
| mpt-30b-chat.ggmlv0.q8_0.bin | q8_0 | 8 | 31.83 GB | 34.33 GB | 8-bit. Almost indistinguishable from float16. High resource use and slow. Not recommended for most users. |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

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

**Patreon special mentions**: Mano Prime, Fen Risland, Derek Yates, Preetika Verma, webtim, Sean Connelly, Alps Aficionado, Karl Bernard, Junyu Yang, Nathan LeClaire, Chris McCloskey, Lone Striker, Asp the Wyvern, Eugene Pentland, Imad Khwaja, trip7s trip, WelcomeToTheClub, John Detwiler, Artur Olbinski, Khalefa Al-Ahmad, Trenton Dambrowitz, Talal Aujan, Kevin Schuppel, Luke Pendergrass, Pyrater, Joseph William Delisle, terasurfer , vamX, Gabriel Puliatti, David Flickinger, Jonathan Leane, Iucharbius , Luke, Deep Realms, Cory Kujawski, ya boyyy, Illia Dulskyi, senxiiz, Johann-Peter Hartmann, John Villwock, K, Ghost , Spiking Neurons AB, Nikolai Manek, Rainer Wilmers, Pierre Kircher, biorpg, Space Cruiser, Ai Maven, subjectnull, Willem Michiel, Ajan Kanaga, Kalila, chris gileta, Oscar Rangel.

Thank you to all my generous patrons and donaters!

<!-- footer end -->

# Original model card: MosaicML's MPT-30B-chat


# MPT-30B-Chat

MPT-30B-Chat is a chatbot-like model for dialogue generation.
It was built by finetuning [MPT-30B](https://huggingface.co/mosaicml/mpt-30b) on the [ShareGPT-Vicuna](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered), [Camel-AI](https://huggingface.co/camel-ai),
 [GPTeacher](https://github.com/teknium1/GPTeacher), [Guanaco](https://huggingface.co/datasets/timdettmers/openassistant-guanaco), [Baize](https://github.com/project-baize/baize-chatbot) and some generated datasets.
  * License: _CC-By-NC-SA-4.0_ (non-commercial use only)
  * [Demo on Hugging Face Spaces](https://huggingface.co/spaces/mosaicml/mpt-30b-chat)


This model was trained by [MosaicML](https://www.mosaicml.com) and follows a modified decoder-only transformer architecture.

## Model Date

June 22, 2023

## Model License

_CC-By-NC-SA-4.0_ (non-commercial use only)

## Documentation

* [Blog post: Raising the bar for open-source foundation models](https://www.mosaicml.com/blog/mpt-30b)
* [Codebase (mosaicml/llm-foundry repo)](https://github.com/mosaicml/llm-foundry/)
* Questions: Feel free to contact us via the [MosaicML Community Slack](https://mosaicml.me/slack)!

### Example Dialogue

**ksreenivasan**:
> I want you to come up with a tweet based on this summary of the article:
> 
> We are excited to extend the MosaicML Foundation Series with MPT-30B, a new commercially licensed open-source model that is significantly more powerful, and outperforms the
> original GPT-3. In addition, we are releasing two fine-tuned models, MPT-30B-Instruct and MPT-30B-Chat, that are built on top of MPT-30B and excel at short-form instruction
> following and multi-turn conversations, respectively.
> All MPT-30B models come with special features that differentiate them from other LLMs, including an 8k token context window (which can be further extended via finetuning;
> see MPT-7B-StoryWriter), support for context-length extrapolation via ALiBi, and efficient inference + training performance via FlashAttention. It also has strong coding
> abilities thanks to its pretraining data mixture.



**MPT-30B-Chat**:
> "Revolutionize your AI capabilities with MosaicML's latest addition, MPT-30B! Outperforming GPT-3, this open-source model is significantly more powerful and comes with
> finely-tuned models for exceptional instruction following and multi-turn conversations. Unleash the potential of an 8k token context window, ALiBi support, and FlashAttention.
> Experience the future of AI with MosaicML! #AI #ML #innovation"

**ksreenivasan**:
> Is there anything you want to say to MosaicML about this exciting news?

**MPT-30B-Chat**:
> As your AI marketing assistant, I would say that this is truly exciting news for the AI community! MosaicML's latest addition, MPT-30B, is poised to revolutionize the industry with its powerful open-source capabilities and finely-tuned models for instruction following and multi-turn conversations.
> The special features, including the 8k token context window, ALiBi support, and FlashAttention, are sure to set MosaicML's MPT-30B apart from other LLMs.
> Congratulations to the MosaicML team on this incredible achievement!

## How to Use

This model is best used with the MosaicML [llm-foundry repository](https://github.com/mosaicml/llm-foundry) for training and finetuning.

```python
import transformers
model = transformers.AutoModelForCausalLM.from_pretrained(
  'mosaicml/mpt-30b-chat',
  trust_remote_code=True
)
```
Note: This model requires that `trust_remote_code=True` be passed to the `from_pretrained` method.
This is because we use a custom `MPT` model architecture that is not yet part of the Hugging Face `transformers` package.
`MPT` includes options for many training efficiency features such as [FlashAttention](https://arxiv.org/pdf/2205.14135.pdf), [ALiBi](https://arxiv.org/abs/2108.12409), [QK LayerNorm](https://arxiv.org/abs/2010.04245), and more.

To use the optimized [triton implementation](https://github.com/openai/triton) of FlashAttention, you can load the model on GPU (`cuda:0`) with `attn_impl='triton'` and with `bfloat16` precision:
```python
import torch
import transformers

name = 'mosaicml/mpt-30b-chat'

config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True)
config.attn_config['attn_impl'] = 'triton'  # change this to use triton-based FlashAttention
config.init_device = 'cuda:0' # For fast initialization directly on GPU!

model = transformers.AutoModelForCausalLM.from_pretrained(
  name,
  config=config,
  torch_dtype=torch.bfloat16, # Load model weights in bfloat16
  trust_remote_code=True
)
```

The model was trained initially with a sequence length of 4096 with an additional pretraining stage for sequence length adapation up to 8192. However, ALiBi enables users to increase the maximum sequence length even further during finetuning and/or inference. For example:

```python
import transformers

name = 'mosaicml/mpt-30b-chat'

config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True)
config.max_seq_len = 16384 # (input + output) tokens can now be up to 16384

model = transformers.AutoModelForCausalLM.from_pretrained(
  name,
  config=config,
  trust_remote_code=True
)
```

This model was trained with the MPT-30B tokenizer which is based on the [EleutherAI/gpt-neox-20b](https://huggingface.co/EleutherAI/gpt-neox-20b) tokenizer and includes additional padding and eos tokens.

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('mosaicml/mpt-30b')
```

The model can then be used, for example, within a text-generation pipeline.  
Note: when running Torch modules in lower precision, it is best practice to use the [torch.autocast context manager](https://pytorch.org/docs/stable/amp.html).

```python
from transformers import pipeline

with torch.autocast('cuda', dtype=torch.bfloat16):
    inputs = tokenizer('Here is a recipe for vegan banana bread:\n', return_tensors="pt").to('cuda')
    outputs = model.generate(**inputs, max_new_tokens=100)
    print(tokenizer.batch_decode(outputs, skip_special_tokens=True))

# or using the HF pipeline
pipe = pipeline('text-generation', model=model, tokenizer=tokenizer, device='cuda:0')
with torch.autocast('cuda', dtype=torch.bfloat16):
    print(
        pipe('Here is a recipe for vegan banana bread:\n',
            max_new_tokens=100,
            do_sample=True,
            use_cache=True))
```

## Model Description

The architecture is a modification of a standard decoder-only transformer.

The model has been modified from a standard transformer in the following ways:
* It uses [FlashAttention](https://arxiv.org/pdf/2205.14135.pdf)
* It uses [ALiBi (Attention with Linear Biases)](https://arxiv.org/abs/2108.12409) and does not use positional embeddings
* It does not use biases


| Hyperparameter | Value |
|----------------|-------|
|n_parameters | 29.95B |
|n_layers | 48 |
| n_heads | 64 |
| d_model | 7168 |
| vocab size | 50432 |
| sequence length | 8192 |

## Data Mix

The model was trained on the following data mix:

| Data Source | Number of Tokens in Source | Proportion | 
|-------------|----------------------------|------------|
| Airoboros/GPT4 | 26.4M | 1.71% |
| Baize | 55.0M | 3.57% |
| Camel	| 301M | 19.54% | 
| GPTeacher	| 7.56M | 0.49% | 
| Guanaco | 15.6M | 1.02% | 
| LongCoversations | 18.4M | 1.19% | 
| ShareGPT | 821M | 53.24% |
| WizardLM | 297M | 19.23% |

"LongConversations" is a GPT3.5/4-generated dataset, details of which will be released at a later date.

### Training Configuration

This model was trained on 64 H100s for about 7.6 hours using the [MosaicML Platform](https://www.mosaicml.com/platform).
The model was trained with sharded data parallelism using [FSDP](https://pytorch.org/docs/stable/fsdp.html) and used the AdamW optimizer.

## Limitations and Biases

_The following language is modified from [EleutherAI's GPT-NeoX-20B](https://huggingface.co/EleutherAI/gpt-neox-20b)_

MPT-30B-Chat can produce factually incorrect output, and should not be relied on to produce factually accurate information.
MPT-30B-Chat was trained on various public datasets.
While great efforts have been taken to clean the pretraining data, it is possible that this model could generate lewd, biased or otherwise offensive outputs.

## Acknowledgements

This model was finetuned by Sam Havens and the MosaicML NLP team

## Disclaimer

The license on this model does not constitute legal advice. We are not responsible for the actions of third parties who use this model. Please consult an attorney before using this model for commercial purposes.


## MosaicML Platform

If you're interested in [training](https://www.mosaicml.com/training) and [deploying](https://www.mosaicml.com/inference) your own MPT or LLMs on the MosaicML Platform, [sign up here](https://forms.mosaicml.com/demo?utm_source=huggingface&utm_medium=referral&utm_campaign=mpt-7b).


## Citation

Please cite this model using the following format:

```
@online{MosaicML2023Introducing,
    author    = {MosaicML NLP Team},
    title     = {Introducing MPT-30B: Raising the bar
for open-source foundation models},
    year      = {2023},
    url       = {www.mosaicml.com/blog/mpt-30b},
    note      = {Accessed: 2023-06-22},
    urldate   = {2023-06-22}
}
```
