---
license: cc-by-nc-4.0
tags:
- not-for-all-audiences
- nsfw
---
## Lumimaid 0.2
<img src="https://cdn-uploads.huggingface.co/production/uploads/63ab1241ad514ca8d1430003/ep3ojmuMkFS-GmgRuI9iB.png" alt="Image" style="display: block; margin-left: auto; margin-right: auto; width: 65%;">
<div style="text-align: center; font-size: 30px;">
    <a href="https://huggingface.co/NeverSleep/Lumimaid-v0.2-8B">8b</a> -
    <a href="https://huggingface.co/NeverSleep/Lumimaid-v0.2-12B">[12b]</a> -
    <a href="https://huggingface.co/NeverSleep/Lumimaid-v0.2-70B">70b</a> -
    <a href="https://huggingface.co/NeverSleep/Lumimaid-v0.2-123B">123b</a>
</div>

### This model is based on: [Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)
Wandb: https://wandb.ai/undis95/Lumi-Mistral-Nemo?nw=nwuserundis95

NOTE: As explained on [Mistral-Nemo-Instruct-2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) repo, it's recommended to use a low temperature, please experiment!

Lumimaid 0.1 -> 0.2 is a HUGE step up dataset wise.

As some people have told us our models are sloppy, Ikari decided to say fuck it and literally nuke all chats out with most slop.

Our dataset stayed the same since day one, we added data over time, cleaned them, and repeat. After not releasing model for a while because we were never satisfied, we think it's time to come back!

# Prompt template: Mistral

```
<s>[INST] {input} [/INST] {output}</s>
```

## Credits:
- Undi
- IkariDev

## Training data we used to make our dataset:

- [Epiculous/Gnosis](https://huggingface.co/Epiculous/Gnosis)
- [ChaoticNeutrals/Luminous_Opus](https://huggingface.co/datasets/ChaoticNeutrals/Luminous_Opus)
- [ChaoticNeutrals/Synthetic-Dark-RP](https://huggingface.co/datasets/ChaoticNeutrals/Synthetic-Dark-RP)
- [ChaoticNeutrals/Synthetic-RP](https://huggingface.co/datasets/ChaoticNeutrals/Synthetic-RP)
- [Gryphe/Sonnet3.5-SlimOrcaDedupCleaned](https://huggingface.co/datasets/Gryphe/Sonnet3.5-SlimOrcaDedupCleaned)
- [Gryphe/Opus-WritingPrompts](https://huggingface.co/datasets/Gryphe/Opus-WritingPrompts)
- [meseca/writing-opus-6k](https://huggingface.co/datasets/meseca/writing-opus-6k)
- [meseca/opus-instruct-9k](https://huggingface.co/datasets/meseca/opus-instruct-9k)
- [PJMixers/grimulkan_theory-of-mind-ShareGPT](https://huggingface.co/datasets/PJMixers/grimulkan_theory-of-mind-ShareGPT)
- [NobodyExistsOnTheInternet/ToxicQAFinal](https://huggingface.co/datasets/NobodyExistsOnTheInternet/ToxicQAFinal)
- [Undi95/toxic-dpo-v0.1-sharegpt](https://huggingface.co/datasets/Undi95/toxic-dpo-v0.1-sharegpt)
- [cgato/SlimOrcaDedupCleaned](https://huggingface.co/datasets/cgato/SlimOrcaDedupCleaned)
- [kalomaze/Opus_Instruct_25k](https://huggingface.co/datasets/kalomaze/Opus_Instruct_25k)
- [Doctor-Shotgun/no-robots-sharegpt](https://huggingface.co/datasets/Doctor-Shotgun/no-robots-sharegpt)
- [Norquinal/claude_multiround_chat_30k](https://huggingface.co/datasets/Norquinal/claude_multiround_chat_30k)
- [nothingiisreal/Claude-3-Opus-Instruct-15K](https://huggingface.co/datasets/nothingiisreal/Claude-3-Opus-Instruct-15K)
- All the Aesirs dataset, cleaned, unslopped
- All le luminae dataset, cleaned, unslopped
- Small part of Airoboros reduced

We sadly didn't find the sources of the following, DM us if you recognize your set !

- Opus_Instruct-v2-6.5K-Filtered-v2-sharegpt
- claude_sharegpt_trimmed
- CapybaraPure_Decontaminated-ShareGPT_reduced

## Datasets credits:
- Epiculous
- ChaoticNeutrals
- Gryphe
- meseca
- PJMixers
- NobodyExistsOnTheInternet
- cgato
- kalomaze
- Doctor-Shotgun
- Norquinal
- nothingiisreal

## Others

Undi: If you want to support us, you can [here](https://ko-fi.com/undiai).

IkariDev: Visit my [retro/neocities style website](https://ikaridevgit.github.io/) please kek