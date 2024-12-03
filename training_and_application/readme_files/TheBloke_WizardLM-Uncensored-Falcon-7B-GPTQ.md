---
license: apache-2.0
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

# Eric Hartford's WizardLM-Uncensored-Falcon-7B GPTQ

This repo contains an experimantal GPTQ 4bit model for [Eric Hartford's WizardLM-Uncensored-Falcon-7B](https://huggingface.co/ehartford/WizardLM-Uncensored-Falcon-7b).

It is the result of quantising to 4bit using [AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ).

## Repositories available

* [4-bit GPTQ model for GPU inference](https://huggingface.co/TheBloke/WizardLM-Uncensored-Falcon-7B-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU+GPU inference](https://huggingface.co/TheBloke/WizardLM-Uncensored-Falcon-7B-GGML)
* [Eric's unquantised bf16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/ehartford/WizardLM-Uncensored-Falcon-7b)

## Prompt template

Prompt format is WizardLM:

```
What is a falcon?  Can I keep one as a pet?
### Response:
```

## EXPERIMENTAL

Please note this is an experimental GPTQ model. Support for it is currently quite limited.

It is also expected to be **SLOW**. This is currently unavoidable, but is being looked at.

## AutoGPTQ

AutoGPTQ 0.2.0 is required: `pip install auto-gptq`

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
4. Under **Download custom model or LoRA**, enter `TheBloke/WizardLM-Uncensored-Falcon-7B-GPTQ`.
5. Click **Download**.
6. Wait until it says it's finished downloading.
7. Click the **Refresh** icon next to **Model** in the top left.
8. In the **Model drop-down**: choose the model you just downloaded, `WizardLM-Uncensored-Falcon-7B-GPTQ`.
9. Make sure **Loader** is set to **AutoGPTQ**. This model will not work with ExLlama or GPTQ-for-LLaMa.
10. Tick **Trust Remote Code**, followed by **Save Settings**
11. Click **Reload**.
12. Once it says it's loaded, click the **Text Generation tab** and enter a prompt!

## Try it for free on Google Colab

Thanks to user [lucianosb](https://huggingface.co/lucianosb), here is a Google Colab notebook that can be used to try this model for free:

https://colab.research.google.com/drive/16C4H9heewOrgUMFYNhxz1AvO12yPHyEq?usp=sharing

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
import torch
from transformers import AutoTokenizer
from auto_gptq import AutoGPTQForCausalLM

# Download the model from HF and store it locally, then reference its location here:
quantized_model_dir = "/path/to/TheBloke_WizardLM-Uncensored-Falcon-7B-GPTQ"

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(quantized_model_dir, use_fast=False)

model = AutoGPTQForCausalLM.from_quantized(quantized_model_dir, device="cuda:0", use_triton=False, use_safetensors=True, torch_dtype=torch.float32, trust_remote_code=True)

prompt = "Write a story about llamas"
prompt_template = f"### Instruction: {prompt}\n### Response:"

tokens = tokenizer(prompt_template, return_tensors="pt").to("cuda:0").input_ids
output = model.generate(input_ids=tokens, max_new_tokens=100, do_sample=True, temperature=0.8)
print(tokenizer.decode(output[0]))
```

## Provided files

**gptq_model-4bit-64g.safetensors**

This will work with AutoGPTQ as of commit `3cb1bf5` (`3cb1bf5a6d43a06dc34c6442287965d1838303d3`)

It was created with groupsize 64 to give higher inference quality, and without `desc_act` (act-order) to increase inference speed.

* `gptq_model-4bit-64g.safetensors`
  * Works only with latest AutoGPTQ CUDA, compiled from source as of commit `3cb1bf5`
    * At this time it does not work with AutoGPTQ Triton, but support will hopefully be added in time.
  * Works with text-generation-webui using `--autogptq --trust_remote_code`
    * At this time it does NOT work with one-click-installers
  * Does not work with any version of GPTQ-for-LLaMa
  * Parameters: Groupsize = 64. No act-order.

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

# ✨ Original model card: Eric Hartford's WizardLM-Uncensored-Falcon-7B

This is WizardLM trained on top of tiiuae/falcon-7b, with a subset of the dataset - responses that contained alignment / moralizing were removed. The intent is to train a WizardLM that doesn't have alignment built-in, so that alignment (of any sort) can be added separately with for example with a RLHF LoRA.

Shout out to the open source AI/ML community, and everyone who helped me out.

Note:
An uncensored model has no guardrails.
You are responsible for anything you do with the model, just as you are responsible for anything you do with any dangerous object such as a knife, gun, lighter, or car. Publishing anything this model generates is the same as publishing it yourself. You are responsible for the content you publish, and you cannot blame the model any more than you can blame the knife, gun, lighter, or car for what you do with it.

Prompt format is Wizardlm.

```
What is a falcon?  Can I keep one as a pet?
### Response:
```
