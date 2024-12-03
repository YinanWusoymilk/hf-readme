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

# Eric Hartford's Wizard Vicuna 13B Uncensored GPTQ

These files are GPTQ 4bit model files for [Eric Hartford's Wizard Vicuna 13B Uncensored](https://huggingface.co/ehartford/Wizard-Vicuna-13B-Uncensored) merged with [Kaio Ken's SuperHOT 8K](https://huggingface.co/kaiokendev/superhot-13b-8k-no-rlhf-test).

It is the result of quantising to 4bit using [GPTQ-for-LLaMa](https://github.com/qwopqwop200/GPTQ-for-LLaMa).

**This is an experimental new GPTQ which offers up to 8K context size**

The increased context is tested to work with [ExLlama](https://github.com/turboderp/exllama), via the latest release of [text-generation-webui](https://github.com/oobabooga/text-generation-webui).

It has also been tested from Python code using AutoGPTQ, and `trust_remote_code=True`.

Code credits:
- Original concept and code for increasing context length: [kaiokendev](https://huggingface.co/kaiokendev)
- Updated Llama modelling code that includes this automatically via trust_remote_code: [emozilla](https://huggingface.co/emozilla).

Please read carefully below to see how to use it.

GGML versions are not yet provided, as there is not yet support for SuperHOT in llama.cpp. This is being investigated and will hopefully come soon.

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/Wizard-Vicuna-13B-Uncensored-SuperHOT-8K-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGML models for CPU inference](https://huggingface.co/TheBloke/Wizard-Vicuna-13B-Uncensored-SuperHOT-8K-GGML)
* [Unquantised SuperHOT fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/TheBloke/Wizard-Vicuna-13B-Uncensored-SuperHOT-8K-fp16)
* [Unquantised base fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/ehartford/Wizard-Vicuna-13B-Uncensored)

## How to easily download and use this model in text-generation-webui with ExLlama

Please make sure you're using the latest version of text-generation-webui

1. Click the **Model tab**.
2. Under **Download custom model or LoRA**, enter `TheBloke/Wizard-Vicuna-13B-Uncensored-SuperHOT-8K-GPTQ`.
3. Click **Download**.
4. The model will start downloading. Once it's finished it will say "Done"
5. Untick **Autoload the model**
6. In the top left, click the refresh icon next to **Model**.
7. In the **Model** dropdown, choose the model you just downloaded: `Wizard-Vicuna-13B-Uncensored-SuperHOT-8K-GPTQ`
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

model_name_or_path = "TheBloke/Wizard-Vicuna-13B-Uncensored-SuperHOT-8K-GPTQ"
model_basename = "wizard-vicuna-13b-uncensored-superhot-8k-GPTQ-4bit-128g.no-act.order"

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

**wizard-vicuna-13b-uncensored-superhot-8k-GPTQ-4bit-128g.no-act.order.safetensors**

This will work with AutoGPTQ, ExLlama, and CUDA versions of GPTQ-for-LLaMa. There are reports of issues with Triton mode of recent GPTQ-for-LLaMa. If you have issues, please use AutoGPTQ instead.

It was created with group_size 128 to increase inference accuracy, but without --act-order (desc_act) to increase compatibility and improve inference speed.

* `wizard-vicuna-13b-uncensored-superhot-8k-GPTQ-4bit-128g.no-act.order.safetensors`
  * Works for use with ExLlama with increased context (4096 or 8192)
  * Works with AutoGPTQ in Python code, including with increased context, if `trust_remote_code=True` is set.
  * Should work with GPTQ-for-LLaMa in CUDA mode, but unknown if increased context works - TBC.  May have issues with GPTQ-for-LLaMa Triton mode.
  * Works with text-generation-webui, including one-click-installers.
  * Parameters: Groupsize = 128. Act Order / desc_act = False.

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

# Original model card: Kaio Ken's SuperHOT 8K

### SuperHOT Prototype 2 w/ 8K Context

This is a second prototype of SuperHOT, this time 30B with 8K context and no RLHF, using the same technique described in [the github blog](https://kaiokendev.github.io/til#extending-context-to-8k).
Tests have shown that the model does indeed leverage the extended context at 8K.

You will need to **use either the monkeypatch** or, if you are already using the monkeypatch, **change the scaling factor to 0.25 and the maximum sequence length to 8192**

#### Looking for Merged & Quantized Models?
- 30B 4-bit CUDA: [tmpupload/superhot-30b-8k-4bit-safetensors](https://huggingface.co/tmpupload/superhot-30b-8k-4bit-safetensors)
- 30B 4-bit CUDA 128g: [tmpupload/superhot-30b-8k-4bit-128g-safetensors](https://huggingface.co/tmpupload/superhot-30b-8k-4bit-128g-safetensors)


#### Training Details
I trained the LoRA with the following configuration:
- 1200 samples (~400 samples over 2048 sequence length)
- learning rate of 3e-4
- 3 epochs
- The exported modules are:
    - q_proj
    - k_proj
    - v_proj
    - o_proj
    - no bias
- Rank = 4
- Alpha = 8
- no dropout
- weight decay of 0.1
- AdamW beta1 of 0.9 and beta2 0.99, epsilon of 1e-5
- Trained on 4-bit base model

# Original model card: Eric Hartford's Wizard Vicuna 13B Uncensored


This is [wizard-vicuna-13b](https://huggingface.co/junelee/wizard-vicuna-13b) trained with a subset of the dataset - responses that contained alignment / moralizing were removed. The intent is to train a WizardLM that doesn't have alignment built-in, so that alignment (of any sort) can be added separately with for example with a RLHF LoRA.

Shout out to the open source AI/ML community, and everyone who helped me out.

Note:

An uncensored model has no guardrails.

You are responsible for anything you do with the model, just as you are responsible for anything you do with any dangerous object such as a knife, gun, lighter, or car.

Publishing anything this model generates is the same as publishing it yourself.

You are responsible for the content you publish, and you cannot blame the model any more than you can blame the knife, gun, lighter, or car for what you do with it.
