---
inference: false
license: other
language:
- en
tags:
- llama
- self-instruct
- distillation
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

# NousResearch's Nous-Hermes-13B GPTQ

These files are GPTQ 4bit model files for [NousResearch's Nous-Hermes-13B](https://huggingface.co/NousResearch/Nous-Hermes-13b).

It is the result of quantising to 4bit using [GPTQ-for-LLaMa](https://github.com/qwopqwop200/GPTQ-for-LLaMa).

## Other repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/Nous-Hermes-13B-GPTQ)
* [4-bit, 5-bit and 8-bit GGML models for CPU(+GPU) inference](https://huggingface.co/TheBloke/Nous-Hermes-13B-GGML)
* [Unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/NousResearch/Nous-Hermes-13b)

## Prompt Template

The model follows the Alpaca prompt format:
```
### Instruction:

### Response:
```

or

```
### Instruction:

### Input:

### Response:
```

## How to easily download and use this model in text-generation-webui

Please make sure you're using the latest version of text-generation-webui

1. Click the **Model tab**.
2. Under **Download custom model or LoRA**, enter `TheBloke/Nous-Hermes-13B-GPTQ`.
3. Click **Download**.
4. The model will start downloading. Once it's finished it will say "Done"
5. In the top left, click the refresh icon next to **Model**.
6. In the **Model** dropdown, choose the model you just downloaded: `Nous-Hermes-13B-GPTQ`
7. The model will automatically load, and is now ready for use!
8. If you want any custom settings, set them and then click **Save settings for this model** followed by **Reload the Model** in the top right.
  * Note that you do not need to set GPTQ parameters any more. These are set automatically from the file `quantize_config.json`.
9. Once you're ready, click the **Text Generation tab** and enter a prompt to get started!

## How to use this GPTQ model from Python code

First make sure you have [AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ) installed:

`pip install auto-gptq`

Then try the following example code:

```python
from transformers import AutoTokenizer, pipeline, logging
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
import argparse

model_name_or_path = "TheBloke/Nous-Hermes-13B-GPTQ"
model_basename = "nous-hermes-13b-GPTQ-4bit-128g.no-act.order"

use_triton = False

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

model = AutoGPTQForCausalLM.from_quantized(model_name_or_path,
        model_basename=model_basename,
        use_safetensors=True,
        trust_remote_code=True,
        device="cuda:0",
        use_triton=use_triton,
        quantize_config=None)

print("\n\n*** Generate:")

input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
output = model.generate(inputs=input_ids, temperature=0.7, max_new_tokens=512)
print(tokenizer.decode(output[0]))

# Inference can also be done using transformers' pipeline

# Prevent printing spurious transformers error when using pipeline with AutoGPTQ
logging.set_verbosity(logging.CRITICAL)

prompt = "Tell me about AI"
prompt_template=f'''### Human: {prompt}
### Assistant:'''

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

**nous-hermes-13b-GPTQ-4bit-128g.no-act.order.safetensors**

This will work with all versions of GPTQ-for-LLaMa, and with AutoGPTQ.

* `nous-hermes-13b-GPTQ-4bit-128g.no-act.order.safetensors`
  * Works with all versions of GPTQ-for-LLaMa code, both Triton and CUDA branches
  * Works with AutoGPTQ
  * Works with text-generation-webui one-click-installers
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

# Original model card: NousResearch's Nous-Hermes-13B

# Model Card: Nous-Hermes-13b

## Model Description

Nous-Hermes-13b is a state-of-the-art language model fine-tuned on over 300,000 instructions. This model was fine-tuned by Nous Research, with Teknium and Karan4D leading the fine tuning process and dataset curation, Redmond AI sponsoring the compute, and several other contributors. The result is an enhanced Llama 13b model that rivals GPT-3.5-turbo in performance across a variety of tasks.

This model stands out for its long responses, low hallucination rate, and absence of OpenAI censorship mechanisms. The fine-tuning process was performed with a 2000 sequence length on an 8x a100 80GB DGX machine for over 50 hours.

## Model Training

The model was trained almost entirely on synthetic GPT-4 outputs. This includes data from diverse sources such as GPTeacher, the general, roleplay v1&2, code instruct datasets, Nous Instruct & PDACTL (unpublished), CodeAlpaca, Evol_Instruct Uncensored, GPT4-LLM, and Unnatural Instructions.

Additional data inputs came from Camel-AI's Biology/Physics/Chemistry and Math Datasets, Airoboros' GPT-4 Dataset, and more from CodeAlpaca. The total volume of data encompassed over 300,000 instructions.

## Collaborators
The model fine-tuning and the datasets were a collaboration of efforts and resources between Teknium, Karan4D, Nous Research, Huemin Art, and Redmond AI.

Huge shoutout and acknowledgement is deserved for all the dataset creators who generously share their datasets openly.

Special mention goes to @winglian, @erhartford, and @main_horse for assisting in some of the training issues.

Among the contributors of datasets, GPTeacher was made available by Teknium, Wizard LM by nlpxucan, and the Nous Research Instruct Dataset was provided by Karan4D and HueminArt.
The GPT4-LLM and Unnatural Instructions were provided by Microsoft, Airoboros dataset by jondurbin, Camel-AI datasets are from Camel-AI, and CodeAlpaca dataset by Sahil 2801.
If anyone was left out, please open a thread in the community tab.

## Prompt Format

The model follows the Alpaca prompt format:
```
### Instruction:

### Response:
```

or

```
### Instruction:

### Input:

### Response:
```

## Resources for Applied Use Cases:
For an example of a back and forth chatbot using huggingface transformers and discord, check out: https://github.com/teknium1/alpaca-discord
For an example of a roleplaying discord bot, check out this: https://github.com/teknium1/alpaca-roleplay-discordbot

## Future Plans
The model is currently being uploaded in FP16 format, and there are plans to convert the model to GGML and GPTQ 4bit quantizations. The team is also working on a full benchmark, similar to what was done for GPT4-x-Vicuna. We will try to get in discussions to get the model included in the GPT4All.

## Benchmark Results
Benchmark results are coming soon.

## Model Usage
The model is available for download on Hugging Face. It is suitable for a wide range of language tasks, from generating creative text to understanding and following complex instructions.

Compute provided by our project sponsor Redmond AI, thank you!!
