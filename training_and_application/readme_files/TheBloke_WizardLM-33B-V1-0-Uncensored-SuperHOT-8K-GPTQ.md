---
inference: false
license: other
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

# Panchovix's merge of WizardLM 33B V1.0 Uncensored and SuperHOT 8K GPTQ

These files are GPTQ 4bit model files for [Panchovix's merge of WizardLM 33B V1.0 Uncensored and SuperHOT 8K](https://huggingface.co/Panchovix/WizardLM-33B-V1.0-Uncensored-SuperHOT-8k).

It is the result of quantising to 4bit using [GPTQ-for-LLaMa](https://github.com/qwopqwop200/GPTQ-for-LLaMa).

**This is an experimental new GPTQ which offers up to 8K context size**

The increased context is tested to work with [ExLlama](https://github.com/turboderp/exllama), via the latest release of [text-generation-webui](https://github.com/oobabooga/text-generation-webui).

It has also been tested from Python code using AutoGPTQ, and `trust_remote_code=True`.

Code credits:
- Original concept and code for increasing context length: [kaiokendev](https://huggingface.co/kaiokendev)
- Updated Llama modelling code that includes this automatically via trust_remote_code: [emozilla](https://huggingface.co/emozilla).

Please read carefully below to see how to use it.

**NOTE**: Using the full 8K context on a 30B model will exceed 24GB VRAM.

GGML versions are not yet provided, as there is not yet support for SuperHOT in llama.cpp. This is being investigated and will hopefully come soon.

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/WizardLM-33B-V1-0-Uncensored-SuperHOT-8K-GPTQ)
* [Panchovix's unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/Panchovix/WizardLM-33B-V1.0-Uncensored-SuperHOT-8k)

GGML quants are not yet provided, as there is not yet support for SuperHOT in llama.cpp. This is being investigated and will hopefully come soon.

## How to easily download and use this model in text-generation-webui with ExLlama

Please make sure you're using the latest version of text-generation-webui

1. Click the **Model tab**.
2. Under **Download custom model or LoRA**, enter `TheBloke/WizardLM-33B-V1.0-Uncensored-SuperHOT-8K-GPTQ`.
3. Click **Download**.
4. The model will start downloading. Once it's finished it will say "Done"
5. Untick **Autoload the model**
6. In the top left, click the refresh icon next to **Model**.
7. In the **Model** dropdown, choose the model you just downloaded: `WizardLM-33B-V1.0-Uncensored-SuperHOT-8K-GPTQ`
8. To use the increased context, set the **Loader** to **ExLlama**, set **max_seq_len** to 8192 or 4096, and set **compress_pos_emb** to **4** for 8192 context, or to **2** for 4096 context.
9. Now click **Save Settings** followed by **Reload**
10. The model will automatically load, and is now ready for use!
11. Once you're ready, click the **Text Generation tab** and enter a prompt to get started!

## How to use this GPTQ model from Python code with AutoGPTQ

First make sure you have AutoGPTQ and Einops installed:

```
pip3 install einops auto-gptq
```

Then run the following code. Note that in order to get this to work, `config.json` has been hardcoded to a sequence length of 8192.

If you want to try 4096 instead to reduce VRAM usage, please manually edit `config.json` to set `max_position_embeddings` to the value you want.

```python
from transformers import AutoTokenizer, pipeline, logging
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
import argparse

model_name_or_path = "TheBloke/WizardLM-33B-V1-0-Uncensored-SuperHOT-8K-GPTQ"
model_basename = "wizardlm-33b-v1.0-uncensored-superhot-8k-GPTQ-4bit--1g.act.order"

use_triton = False

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

model = AutoGPTQForCausalLM.from_quantized(model_name_or_path,
        model_basename=model_basename,
        use_safetensors=True,
        trust_remote_code=True,
        device_map='auto',
        use_triton=use_triton,
        quantize_config=None)

model.seqlen = 8192

# Note: check the prompt template is correct for this model.
prompt = "Tell me about AI"
prompt_template=f'''USER: {prompt}
ASSISTANT:'''

print("\n\n*** Generate:")

input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
output = model.generate(inputs=input_ids, temperature=0.7, max_new_tokens=512)
print(tokenizer.decode(output[0]))

# Inference can also be done using transformers' pipeline

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

## Using other UIs: monkey patch

Provided in the repo is `llama_rope_scaled_monkey_patch.py`, written by @kaiokendev.

It can be theoretically be added to any Python UI or custom code to enable the same result as `trust_remote_code=True`.  I have not tested this, and it should be superseded by using `trust_remote_code=True`, but I include it for completeness and for interest.


## Provided files

**wizardlm-33b-v1.0-uncensored-superhot-8k-GPTQ-4bit--1g.act.order.safetensors**

This will work with AutoGPTQ, ExLlama, and CUDA versions of GPTQ-for-LLaMa. There are reports of issues with Triton mode of recent GPTQ-for-LLaMa. If you have issues, please use AutoGPTQ instead.

It was created without group_size to lower VRAM requirements, and with --act-order (desc_act) to boost inference accuracy as much as possible.

* `wizardlm-33b-v1.0-uncensored-superhot-8k-GPTQ-4bit--1g.act.order.safetensors`
  * Works with AutoGPTQ in CUDA or Triton modes.
  * LLaMa models also work with [ExLlama](https://github.com/turboderp/exllama}, which usually provides much higher performance, and uses less VRAM, than AutoGPTQ.
  * Works with GPTQ-for-LLaMa in CUDA mode.  May have issues with GPTQ-for-LLaMa Triton mode.
  * Works with text-generation-webui, including one-click-installers.
  * Parameters: Groupsize = -1. Act Order / desc_act = True.

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

# Original model card: Panchovix's merge of WizardLM 33B V1.0 Uncensored and SuperHOT 8K

[WizardLM-33B-V1.0-Uncensored](https://huggingface.co/ehartford/WizardLM-33B-V1.0-Uncensored) merged with kaiokendev's [33b SuperHOT 8k LoRA](https://huggingface.co/kaiokendev/superhot-30b-8k-no-rlhf-test), without quant. (Full FP16 model)
