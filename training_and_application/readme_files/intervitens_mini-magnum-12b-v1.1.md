---
license: apache-2.0
language:
  - en
  - fr
  - de
  - es
  - it
  - pt
  - ru
  - zh
  - ja
---

![](mini-magnum.png)

# 🔥 New version is available! [anthracite-org/magnum-12b-v2](https://huggingface.co/anthracite-org/magnum-12b-v2) 🔥

This model is the miniature version of [alpindale/magnum-72b-v1](https://huggingface.co/alpindale/magnum-72b-v1), a second entry in a series of models designed to replicate the prose quality of the Claude 3 models, specifically Sonnet and Opus. This model is fine-tuned on top of [Mistral-Nemo-Base-2407](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407). 
A new general purpose instruction dataset by kalomaze was added to the training mix for better coherence and general alignment. We are working on improving our dataset and training procedures, so expect new versions to come out soon.


## Prompting
Model has been Instruct tuned with the Mistral formatting. A typical input would look like this:

```py
"""[INST] Hi there! [/INST]Nice to meet you!</s>[INST] Can I ask a question? [/INST]
"""
```

## Credits

This model has been a team effort, credits go to:

- [Sao10K](https://huggingface.co/Sao10K) and [kalomaze](https://huggingface.co/kalomaze) for help with (and cleaning up!) the dataset.
- [alpindale](https://huggingface.co/alpindale) for the training.
- Various other people for their continued help as we tuned the parameters, restarted failed runs. In no particular order: [Doctor Shotgun](https://huggingface.co/Doctor-Shotgun), [Lucy](https://huggingface.co/lucyknada), [Nopm](https://huggingface.co/nopm), [Mango](https://huggingface.co/MangoMango69420), [Intervitens](https://huggingface.co/intervitens), and the rest of the Silly Tilly.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## Safety
...

