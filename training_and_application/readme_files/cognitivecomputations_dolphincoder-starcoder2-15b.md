---
datasets:
- cognitivecomputations/dolphin
- jondurbin/airoboros-2.2.1
- cognitivecomputations/dolphin-coder
- teknium/openhermes
- ise-uiuc/Magicoder-OSS-Instruct-75K
- ise-uiuc/Magicoder-Evol-Instruct-110K
- m-a-p/Code-Feedback
- m-a-p/CodeFeedback-Filtered-Instruction
language:
- en
license: bigcode-openrail-m
---

DolphinCoder StarCoder2 15b 🐬

sponsored by [latitude.sh](https://www.latitude.sh/).

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations 

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/ldkN1J0WIDQwU4vutGYiD.png" width="600" />

This model is based on StarCoder2-15b and is subject to bigcode-openrail-m license.

This Dolphin is *really good* at coding, I trained with a lot of coding data.  

This model is uncensored.  I have filtered the dataset to remove alignment and bias.  This makes the model more compliant.  You are advised to implement your own alignment layer before exposing the model as a service.  It will be highly compliant to any requests, even unethical ones.  Please read my blog post about uncensored models.  https://erichartford.com/uncensored-models
You are responsible for any content you create using this model.  Enjoy responsibly.

## Training
It took 3 days to train 3 epochs on 8x H100s using qLoRA and Axolotl

Prompt format:
This model uses ChatML prompt format.
```
<|im_start|>system
You are DolphinCoder, a helpful AI programming assistant.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

Example:
```
<|im_start|>system
You are DolphinCoder, a master at software engineering and coding in any programming language.
<|im_start|>user
Please write me a program in golang that parses all the lines in a file, and reverses them character-wise, and saves it to a new file.
<|im_start|>assistant
```

## Quantized models

- [gguf](https://huggingface.co/dagbs/dolphincoder-starcoder2-15b-GGUF)

- [ExLlamaV2](https://huggingface.co/bartowski/dolphincoder-starcoder2-15b-exl2)

## Gratitude
- This model was made possible by the generous sponsorship of [latitude.sh](https://www.latitude.sh/).
- Huge thank you to [BigCode](https://www.bigcode-project.org/) for training and publishing the weights of StarCoder2
- HUGE Thank you to the dataset authors: @ise-uiuc, @teknium, @m-a-p
- And HUGE thanks to @winglian and the Axolotl contributors for making the best training framework!
- [<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
- Thank you to all the other people in the Open Source AI community who have taught me and helped me along the way.

## Example Output

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/9Yhoy6PYoreqX8KocaDWb.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/lz0fXODictCmW5pNultqq.png)

[If you would like to financially support my efforts](https://ko-fi.com/erichartford)

[swag](https://fa7113.myshopify.com/)