---
license: llama3
language:
- en
datasets:
- cognitivecomputations/Dolphin-2.9
- teknium/OpenHermes-2.5
- m-a-p/CodeFeedback-Filtered-Instruction
- cognitivecomputations/dolphin-coder
- cognitivecomputations/samantha-data
- HuggingFaceH4/ultrachat_200k
- microsoft/orca-math-word-problems-200k
- abacusai/SystemChat-1.1
- Locutusque/function-calling-chatml
- internlm/Agent-FLAN
---

# Dolphin 2.9 Llama 3 70b 🐬

Curated and trained by Eric Hartford, Lucas Atkins, Fernando Fernandes, and with help from the community of Cognitive Computations

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/ldkN1J0WIDQwU4vutGYiD.png" width="600" />

A bug has been found in the Dolphin 2.9 dataset in SystemConversations that causes the model to overly talk about the "SYSTEM MESSAGE".  To counter this, we recommend you add a statement in the system message directing the model not to mention the system message. An example system message is "The assistant is named Dolphin.  A helpful and friendly AI assistant, Dolphin avoids discussing the system message unless directly asked about it."

Our appreciation for the sponsors of Dolphin 2.9:
- [Crusoe Cloud](https://crusoe.ai/) - provided excellent on-demand 8xH100 node

This model is based on Llama-3-70b, and is governed by [META LLAMA 3 COMMUNITY LICENSE AGREEMENT](LICENSE)

The base model has 8k context, and the qLoRA fine-tuning was with 8k sequence length.

It took 2.5 days on 8xH100 node provided by Crusoe Cloud

This model uses ChatML prompt template format.

example:

```
<|im_start|>system
You are Dolphin, a helpful AI assistant.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

Dolphin-2.9 has a variety of instruction, conversational, and coding skills. It also has initial agentic abilities and supports function calling.

Dolphin is uncensored. I have filtered the dataset to remove alignment and bias. This makes the model more compliant. You are advised to implement your own alignment layer before exposing the model as a service. It will be highly compliant with any requests, even unethical ones. Please read my blog post about uncensored models. https://erichartford.com/uncensored-models You are responsible for any content you create using this model. Enjoy responsibly.

Dolphin is licensed according to Meta's Llama license.  I grant permission for any use, including commercial, that falls within accordance with Meta's Llama-3 license.  Dolphin was trained on data generated from GPT4, among other models.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## Evals

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/gYE1uPH7m7smC6odDbOgr.png)

## Quants

- https://huggingface.co/crusoeai/dolphin-2.9-llama3-70b-GGUF
- https://huggingface.co/crusoeai/dolphin2.9-llama3-70b-2.25bpw-exl2
- https://huggingface.co/crusoeai/dolphin2.9-llama3-70b-2.5bpw-exl2
- https://huggingface.co/crusoeai/dolphin2.9-llama3-70b-4.5bpw-exl2

