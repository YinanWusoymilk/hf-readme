---
datasets:
- tiiuae/falcon-refinedweb
license: apache-2.0
language:
- en
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

# Falcon-40B-Instruct 4bit GPTQ

This repo contains an experimantal GPTQ 4bit model for [Falcon-40B-Instruct](https://huggingface.co/tiiuae/falcon-40b-instruct).

It is the result of quantising to 4bit using [AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ).

## Repositories available

* [4-bit GPTQ model for GPU inference](https://huggingface.co/TheBloke/falcon-40b-instruct-GPTQ)
* [3-bit GPTQ model for GPU inference](https://huggingface.co/TheBloke/falcon-40b-instruct-3bit-GPTQ)
* [2, 3, 4, 5, 6, 8-bit GGML models for CPU+GPU inference](https://huggingface.co/TheBloke/falcon-40b-instruct-GGML)
* [Unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/tiiuae/falcon-40b-instruct)

## Prompt template

```
A helpful assistant who helps the user with any questions asked.
User: prompt
Assistant:
```

## EXPERIMENTAL

Please note this is an experimental GPTQ model. Support for it is currently quite limited.

It is also expected to be **VERY SLOW**. This is currently unavoidable, but is being looked at.

This 4bit model requires at least 35GB VRAM to load. It can be used on 40GB or 48GB cards, but not less.

Please be aware that you should currently expect around 0.7 tokens/s on 40B Falcon GPTQ.

## AutoGPTQ

AutoGPTQ is required: `pip install auto-gptq`

AutoGPTQ provides pre-compiled wheels for Windows and Linux, with CUDA toolkit 11.7 or 11.8.

If you are running CUDA toolkit 12.x, you will need to compile your own by following these instructions:

```
git clone https://github.com/PanQiWei/AutoGPTQ
cd AutoGPTQ
pip install .
```

These manual steps will require that you have the [Nvidia CUDA toolkit](https://developer.nvidia.com/cuda-12-0-1-download-archive) installed.

## text-generation-webui

There is provisional AutoGPTQ support in text-generation-webui.

This requires text-generation-webui as of commit 204731952ae59d79ea3805a425c73dd171d943c3.

So please first update text-genration-webui to the latest version.

## How to download and use this model in text-generation-webui

1. Launch text-generation-webui
2. Click the **Model tab**.
3. Untick **Autoload model**
4. Under **Download custom model or LoRA**, enter `TheBloke/falcon-40B-instruct-GPTQ`.
5. Click **Download**.
6. Wait until it says it's finished downloading.
7. Click the **Refresh** icon next to **Model** in the top left.
8. In the **Model drop-down**: choose the model you just downloaded, `falcon-40B-instruct-GPTQ`.
9. Make sure **Loader** is set to **AutoGPTQ**. This model will not work with ExLlama or GPTQ-for-LLaMa.
10. Tick **Trust Remote Code**, followed by **Save Settings**
11. Click **Reload**.
12. Once it says it's loaded, click the **Text Generation tab** and enter a prompt!

## About `trust_remote_code`

Please be aware that this command line argument causes Python code provided by Falcon to be executed on your machine.

This code is required at the moment because Falcon is too new to be supported by Hugging Face transformers. At some point in the future transformers will support the model natively, and then `trust_remote_code` will no longer be needed.

In this repo you can see two `.py` files - these are the files that get executed. They are copied from the base repo at [Falcon-7B-Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct).

## Simple Python example code

To run this code you need to install AutoGPTQ and einops:
```
pip install auto-gptq
pip install einops
```

You can then run this example code:
```python
from transformers import AutoTokenizer, pipeline, logging
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
import argparse

model_name_or_path = "TheBloke/falcon-40b-instruct-GPTQ"
# You could also download the model locally, and access it there
# model_name_or_path = "/path/to/TheBloke_falcon-40b-instruct-GPTQ"

model_basename = "model"

use_triton = False

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

model = AutoGPTQForCausalLM.from_quantized(model_name_or_path,
        model_basename=model_basename,
        use_safetensors=True,
        trust_remote_code=True,
        device="cuda:0",
        use_triton=use_triton,
        quantize_config=None)

prompt = "Tell me about AI"
prompt_template=f'''A helpful assistant who helps the user with any questions asked.
User: {prompt}
Assistant:''

print("\n\n*** Generate:")

input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
output = model.generate(inputs=input_ids, temperature=0.7, max_new_tokens=512)
print(tokenizer.decode(output[0]))

# Inference can also be done using transformers' pipeline
# Note that if you use pipeline, you will see a spurious error message saying the model type is not supported
# This can be ignored!  Or you can hide it with the following logging line:
# Prevent printing spurious transformers error when using pipeline with AutoGPTQ
logging.set_verbosity(logging.CRITICAL)

print("*** Pipeline:")
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.15
)

print(pipe(prompt_template)[0]['generated_text'])
```

## Provided files

**gptq_model-4bit--1g.safetensors**

This will work with AutoGPTQ 0.2.0 and later.

It was created without groupsize to reduce VRAM requirements, and with `desc_act` (act-order) to improve inference quality.

* `gptq_model-4bit--1g.safetensors`
  * Works AutoGPTQ 0.2.0 and later.
    * At this time it does not work with AutoGPTQ Triton, but support will hopefully be added in time.
  * Works with text-generation-webui using `--trust-remote-code`
  * Does not work with any version of GPTQ-for-LLaMa
  * Parameters: Groupsize = None. Act order (desc_act)

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

# ✨ Original model card: Falcon-40B-Instruct

# ✨ Falcon-40B-Instruct

**Falcon-40B-Instruct is a 40B parameters causal decoder-only model built by [TII](https://www.tii.ae) based on [Falcon-40B](https://huggingface.co/tiiuae/falcon-40b) and finetuned on a mixture of [Baize](https://github.com/project-baize/baize-chatbot). It is made available under the [TII Falcon LLM License](https://huggingface.co/tiiuae/falcon-40b-instruct/blob/main/LICENSE.txt).**

*Paper coming soon 😊.*

## Why use Falcon-40B-Instruct?

* **You are looking for a ready-to-use chat/instruct model based on [Falcon-40B](https://huggingface.co/tiiuae/falcon-40b).**
* **Falcon-40B is the best open-source model available.** It outperforms [LLaMA](https://github.com/facebookresearch/llama), [StableLM](https://github.com/Stability-AI/StableLM), [RedPajama](https://huggingface.co/togethercomputer/RedPajama-INCITE-Base-7B-v0.1), [MPT](https://huggingface.co/mosaicml/mpt-7b), etc. See the [OpenLLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard).
* **It features an architecture optimized for inference**, with FlashAttention ([Dao et al., 2022](https://arxiv.org/abs/2205.14135)) and multiquery ([Shazeer et al., 2019](https://arxiv.org/abs/1911.02150)).

💬 **This is an instruct model, which may not be ideal for further finetuning.** If you are interested in building your own instruct/chat model, we recommend starting from [Falcon-40B](https://huggingface.co/tiiuae/falcon-40b).

💸 **Looking for a smaller, less expensive model?** [Falcon-7B-Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct) is Falcon-40B-Instruct's small brother!

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-40b-instruct"

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

# Model Card for Falcon-40B-Instruct

## Model Details

### Model Description

- **Developed by:** [https://www.tii.ae](https://www.tii.ae);
- **Model type:** Causal decoder-only;
- **Language(s) (NLP):** English and French;
- **License:** [TII Falcon LLM License](https://huggingface.co/tiiuae/falcon-7b-instruct/blob/main/LICENSE.txt);
- **Finetuned from model:** [Falcon-7B](https://huggingface.co/tiiuae/falcon-7b).

### Model Source

- **Paper:** *coming soon*.

## Uses

### Direct Use

Falcon-40B-Instruct has been finetuned on a chat dataset.

### Out-of-Scope Use

Production use without adequate assessment of risks and mitigation; any use cases which may be considered irresponsible or harmful.

## Bias, Risks, and Limitations

Falcon-40B-Instruct is mostly trained on English data, and will not generalize appropriately to other languages. Furthermore, as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

### Recommendations

We recommend users of Falcon-40B-Instruct to develop guardrails and to take appropriate precautions for any production use.

## How to Get Started with the Model


```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-40b-instruct"

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

### Training Data

Falcon-40B-Instruct was finetuned on a 150M tokens from [Bai ze](https://github.com/project-baize/baize-chatbot) mixed with 5% of [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb) data.


The data was tokenized with the Falcon-[7B](https://huggingface.co/tiiuae/falcon-7b)/[40B](https://huggingface.co/tiiuae/falcon-40b) tokenizer.


## Evaluation

*Paper coming soon.*

See the [OpenLLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) for early results.


## Technical Specifications

For more information about pretraining, see [Falcon-40B](https://huggingface.co/tiiuae/falcon-40b).

### Model Architecture and Objective

Falcon-40B is a causal decoder-only model trained on a causal language modeling task (i.e., predict the next token).

The architecture is broadly adapted from the GPT-3 paper ([Brown et al., 2020](https://arxiv.org/abs/2005.14165)), with the following differences:

* **Positionnal embeddings:** rotary ([Su et al., 2021](https://arxiv.org/abs/2104.09864));
* **Attention:** multiquery ([Shazeer et al., 2019](https://arxiv.org/abs/1911.02150)) and FlashAttention ([Dao et al., 2022](https://arxiv.org/abs/2205.14135));
* **Decoder-block:** parallel attention/MLP with a single layer norm.

For multiquery, we are using an internal variant which uses independent key and values per tensor parallel degree.

| **Hyperparameter** | **Value** | **Comment**                            |
|--------------------|-----------|----------------------------------------|
| Layers             | 60        |                                        |
| `d_model`          | 8192      |                                        |
| `head_dim`         | 64        | Reduced to optimise for FlashAttention |
| Vocabulary         | 65024     |                                        |
| Sequence length    | 2048      |                                        |

### Compute Infrastructure

#### Hardware

Falcon-40B-Instruct was trained on AWS SageMaker, on 64 A100 40GB GPUs in P4d instances.

#### Software

Falcon-40B-Instruct was trained a custom distributed training codebase, Gigatron. It uses a 3D parallelism approach combined with ZeRO and high-performance Triton kernels (FlashAttention, etc.)


## Citation

*Paper coming soon 😊.*

## License

Falcon-40B-Instruct is made available under the [TII Falcon LLM License](https://huggingface.co/tiiuae/falcon-40b-instruct/blob/main/LICENSE.txt). Broadly speaking,
* You can freely use our models for research and/or personal purpose;
* You are allowed to share and build derivatives of these models, but you are required to give attribution and to share-alike with the same license;
* For commercial use, you are exempt from royalties payment if the attributable revenues are inferior to $1M/year, otherwise you should enter in a commercial agreement with TII.


## Contact
falconllm@tii.ae

