---
base_model: []
library_name: transformers
tags:
- mergekit
- merge
---

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/6550b16f7490049d6237f200/zYBXSewLbIxWHZdB3oEHs.jpeg)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6550b16f7490049d6237f200/eRwPcd9Ox03hn_WRnsotj.png)

# Information
## Details

Okay, I tried really hard to improve my ChatML merges, but that has gone terribly wrong. Everyone is adding special tokens with different IDs so can't even make a proper union tokenizer for them, damn. Not to mention, I made some... interesting discoveres in regards to some models' context lenghts. You can watch the breakdown of how it went down here: https://www.captiongenerator.com/v/2303039/marinaraspaghetti's-merging-experience.

This one feels a bit different to my previous attempts and seems less prone to repetition, especially on higher contexts, which is great for me! I'll probably improve on it even further, but for now, it feels rather nice. Great for RP and storytelling. All credits and thanks go to the amazing MistralAI, Intervitens, Sao10K and Nbeerbower for their amazing models! Plus, special shoutouts to Parasitic Rogue for ideas and Prodeus Unity and Statuo for cool exl2 quants of my previous merges. Cheers to folks over at the Drummer's server! Have a good one, everyone.

## Instruct

![image/gif](https://cdn-uploads.huggingface.co/production/uploads/6550b16f7490049d6237f200/JtOSIRNnMdGNycWACobO2.gif)

*Sigh,* Mistral Instruct, I'm afraid.

UPDATE: WE HAD THE WRONG FORMAT ALL ALONG, JUST RECEIVED HOW IT'S SUPPOSED TO LOOK LIKE FROM THE OFFICIAL MISTRALAI TEAM MEMBER.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6550b16f7490049d6237f200/lAGz_ITUkVaLMvm_0AXuj.png)

...This had made me question everything I thought I knew.

```
<s>[INST]{system}[/INST]{response}</s>[INST]{user's message}[/INST]{response}</s>
```

## Parameters

I recommend running Temperature 1.0-1.25 with 0.1 Top A or 0.01-0.1 Min P, and with 0.8/1.75/2/0 DRY. Also works with lower Temperatures below 1.0. Nothing more needed.

### Settings

You can use my exact settings from here (use the ones from the Mistral Base/Customized folder, I also recommend checking the Mistral Improved folder): https://huggingface.co/MarinaraSpaghetti/SillyTavern-Settings/tree/main.

## GGUF

https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF

## EXL2

https://huggingface.co/Statuo/NemoMix-Unleashed-EXL2-8bpw

# NemoMix-Unleashed-12B

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the della_linear merge method using E:\mergekit\mistralaiMistral-Nemo-Base-2407 as a base.

### Models Merged

The following models were included in the merge:
* E:\mergekit\intervitens_mini-magnum-12b-v1.1
* E:\mergekit\nbeerbower_mistral-nemo-bophades-12B
* E:\mergekit\Sao10K_MN-12B-Lyra-v1
* E:\mergekit\nbeerbower_mistral-nemo-gutenberg-12B
* E:\mergekit\mistralaiMistral-Nemo-Instruct-2407

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: E:\mergekit\mistralaiMistral-Nemo-Instruct-2407
    parameters:
      weight: 0.1
      density: 0.4
  - model: E:\mergekit\nbeerbower_mistral-nemo-bophades-12B
    parameters:
      weight: 0.12
      density: 0.5
  - model: E:\mergekit\nbeerbower_mistral-nemo-gutenberg-12B
    parameters:
      weight: 0.2
      density: 0.6
  - model: E:\mergekit\Sao10K_MN-12B-Lyra-v1
    parameters:
      weight: 0.25
      density: 0.7
  - model: E:\mergekit\intervitens_mini-magnum-12b-v1.1
    parameters:
      weight: 0.33
      density: 0.8
merge_method: della_linear
base_model: E:\mergekit\mistralaiMistral-Nemo-Base-2407
parameters:
  epsilon: 0.05
  lambda: 1
dtype: bfloat16
tokenizer_source: base
```

# Ko-fi
## Enjoying what I do? Consider donating here, thank you!

https://ko-fi.com/spicy_marinara