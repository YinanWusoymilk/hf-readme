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
pipeline_tag: text-generation
quantized_by: anthracite-org
base_model: anthracite-org/magnum-v2-12b
tags:
- chat
---

## This repo contains GGUF quants of the model. If you need the original weights, please find them [here](https://huggingface.co/anthracite-org/magnum-12b-v2).
This is the fourth in a series of models designed to replicate the prose quality of the Claude 3 models, specifically Sonnet and Opus. This model is fine-tuned on top of [Mistral-Nemo-Base-2407](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/658a46cbfb9c2bdfae75b3a6/A9n8EJBDQziJWnXhOYeEE.png)

## Prompting
Model has been Instruct tuned with the ChatML formatting. A typical input would look like this:

```py
"""<|im_start|>user
Hi there!<|im_end|>
<|im_start|>assistant
Nice to meet you!<|im_end|>
<|im_start|>user
Can I ask a question?<|im_end|>
<|im_start|>assistant
"""
```

## Credits
- Stheno dataset (filtered)
- [kalomaze/Opus_Instruct_25k](https://huggingface.co/datasets/kalomaze/Opus_Instruct_25k)
- [Nopm/Opus_WritingStruct](https://huggingface.co/datasets/Nopm/Opus_WritingStruct)
- [Gryphe/Sonnet3.5-SlimOrcaDedupCleaned](https://huggingface.co/datasets/Gryphe/Sonnet3.5-SlimOrcaDedupCleaned) (A ~16k rows subset)
- [kalomaze/Opus_Instruct_3k](https://huggingface.co/datasets/kalomaze/Opus_Instruct_3k)

This model has been a team effort, and the credits goes to all members of Anthracite.

## Training
The training was done for 2 epochs. We used 8x [NVIDIA H100 Tensor Core](https://www.nvidia.com/en-us/data-center/h100/) GPUs for the full-parameter fine-tuning of the model.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## Safety
...