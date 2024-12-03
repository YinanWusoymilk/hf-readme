---
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

# WizardLM: An Instruction-following LLM Using Evol-Instruct

These files are the result of merging the [delta weights](https://huggingface.co/victor123/WizardLM) with the original Llama7B model.

The code for merging is provided in the [WizardLM official Github repo](https://github.com/nlpxucan/WizardLM).

The original WizardLM deltas are in float32, and this results in producing an HF repo that is also float32, and is much larger than a normal 7B Llama model.

Therefore for this repo I converted the merged model to float16, to produce a standard size 7B model.

This was achieved by running **`model = model.half()`** prior to saving.

## WizardLM-7B HF

This repo contains the full unquantised model files in HF format for GPU inference and as a base for quantisation/conversion.

## Other repositories available

* [4bit GGML models for CPU inference](https://huggingface.co/TheBloke/wizardLM-7B-GGML)
* [4bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/wizardLM-7B-GPTQ)

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

**Patreon special mentions**: Aemon Algiz, Dmitriy Samsonov, Nathan LeClaire, Trenton Dambrowitz, Mano Prime, David Flickinger, vamX, Nikolai Manek, senxiiz, Khalefa Al-Ahmad, Illia Dulskyi, Jonathan Leane, Talal Aujan, V. Lukas, Joseph William Delisle, Pyrater, Oscar Rangel, Lone Striker, Luke Pendergrass, Eugene Pentland, Sebastain Graf, Johann-Peter Hartman.

Thank you to all my generous patrons and donaters!
<!-- footer end -->
# Original model info

## Full details in the model's Github page

[WizardLM official Github repo](https://github.com/nlpxucan/WizardLM).

## Overview of Evol-Instruct

Evol-Instruct is a novel method using LLMs instead of humans to automatically mass-produce open-domain instructions of various difficulty levels and skills range, to improve the performance of LLMs.

Although on our complexity-balanced test set, WizardLM-7B outperforms ChatGPT in the high-complexity instructions, it still lag behind ChatGPT on the entire test set, and we also consider WizardLM to still be in a baby state. This repository will continue to improve WizardLM, train on larger scales, add more training data, and innovate more advanced large-model training methods.

![info](https://github.com/nlpxucan/WizardLM/raw/main/imgs/git_overall.png)
![info](https://github.com/nlpxucan/WizardLM/raw/main/imgs/git_running.png)
