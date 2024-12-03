---
datasets:
- migtissera/Synthia-v1.3
- meta-math/MetaMathQA
- LDJnr/Capybara
language:
- en
library_name: transformers
pipeline_tag: text-generation
model_creator: DiscoResearch
model_type: mixtral
Tags:
- mixtral
- moe
- discoresearch
license: apache-2.0
---


![image/png](https://cdn-uploads.huggingface.co/production/uploads/62e3b6ab0c2a907c388e4965/IP6ULgm4XLcK_JLRz-WV4.png)
*Eight french experts sitting at a table. There's lots of wind.*

# DiscoLM Mixtral 8x7b alpha

**DiscoLM Mixtral 8x7b alpha** is an experimental 8x7b MoE model based on [Mistral AI´s Mixtral 8x7b](https://twitter.com/MistralAI/status/1733150512395038967).
This model is based on experimental code converting the model weights to huggingface format and enabling Transformers-based inference. 
It was then finetuned on the Synthia, MethaMathQA und Capybara datasets. 
DiscoLM Mixtral 8x7b alpha is a [DiscoResearch](https://huggingface.co/DiscoResearch) project and was created by [Björn Plüster](https://huggingface.co/bjoernp) with lots of support from the community.

**Many thanks to [HessianAI](https://hessian.ai/) for providing the compute resources for this project and to the great people at [LAION](https://laion.ai) without whom this project would not have been possible!**


## Table of Contents

1. [Download](#download)
2. [Benchmarks](#benchmarks)
3. [Prompt Format](#prompt-format)
4. [Dataset](#datasets)
5. [Acknowledgements](#acknowledgements)
6. [Contact](#contact)
7. [About DiscoResearch](#about-discoresearch)
8. [Disclaimer](#disclaimer)

## Download 

**Please note that you have to run the model with `trust_remote_code=True` until the new arch is merged into transformers!**

| Huggingface    | GPTQ  | GGUF  | AWQ   | *Base Model* |
|-------|-------|-------|-------|-------|
| [Link](https://huggingface.co/DiscoResearch/DiscoLM-Mixtral-8x7b) | tbc | tbc | tbc | tbc |

## Benchmarks

### Huggingface Leaderboard

This model is still an early Alpha with experimental code and we can't guarantee that there all values are correct. 
The following are the scores from our own evaluation.

| Metric | Value |
|-----------------------|-------|
| ARC (25-shot)         | 67.32 |
| HellaSwag (10-shot)   |  86.25 |
| MMLU (5-shot)         | 70.72 |
| TruthfulQA (0-shot)   | 54.17 |
| Winogrande (5-shot)   | 80.72 |
| GSM8k (5-shot)   |  25.09 (bad score. no clue why)|
| **Avg.**                  | **64.05** |


We use [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) to run the benchmark tests above, using the same version as the HuggingFace LLM Leaderboard.

### FastEval

```
{
    "gsm8k": 0.656,
    "math": 0.242,
    "bbh": {
        "average": 0.5807843137254902
    },
    "mmlu": {
        "average": 0.6245614035087719
    },
    "total": 0.4690691434468524
}
```

### MTBench

```
{
  "first_turn": 7.89375,
  "second_turn": 7.5125,
  "categories": {
      "writing": 9.25,
      "roleplay": 8.425,
      "reasoning": 5.7,
      "math": 5.85,
      "coding": 4.45,
      "extraction": 8.75,
      "stem": 9.45,
      "humanities": 9.75
  },
  "average": 7.703125
}
```

## Prompt Format

**Please note that you have to run the model with `trust_remote_code=True` until the new arch is merged into transformers!**

This model follows the ChatML format:

```
<|im_start|>system
You are DiscoLM, a helpful assistant.
<|im_end|>
<|im_start|>user
Please tell me possible reasons to call a research collective "Disco Research"<|im_end|>
<|im_start|>assistant
```

This formatting is also available via a pre-defined Transformers chat template, which means that lists of messages can be formatted for you with the apply_chat_template() method:

```python
chat = [
  {"role": "system", "content": "You are DiscoLM, a helpful assistant."},
  {"role": "user", "content": "Please tell me possible reasons to call a research collective Disco Research"}
]
tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
```

If you use `tokenize=True` and `return_tensors="pt"` instead, then you will get a tokenized and formatted conversation ready to pass to `model.generate()`.

Basic inference code:
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("DiscoResearch/DiscoLM-mixtral-8x7b-v2", low_cpu_mem_usage=True, device_map="auto", trust_remote_code=True)
tok = AutoTokenizer.from_pretrained("DiscoResearch/DiscoLM-mixtral-8x7b-v2")
chat = [
  {"role": "system", "content": "You are DiscoLM, a helpful assistant."},
  {"role": "user", "content": "Please tell me possible reasons to call a research collective Disco Research"}
]
x = tok.apply_chat_template(chat, tokenize=True, return_tensors="pt", add_generation_prompt=True).cuda()
x = model.generate(x, max_new_tokens=128).cpu()
print(tok.batch_decode(x))
```

## Datasets

The following datasets were used for training DiscoLM Mixtral 8x7b alpha:

* [Synthia](https://huggingface.co/datasets/migtissera/Synthia-v1.3)
* [MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA)
* Capybara Dataset by [LDJnr](https://huggingface.co/LDJnr)

Many thanks for all dataset providers/curators!

## Contact

Best way to reach us is on our [Discord](https://discord.gg/S8W8B5nz3v).

## About DiscoResearch

DiscoResearch is an aspiring open research community. Disco should be a place where researchers from many communities can come together to combine their expertise and create innovative and groundbreaking LLMs. Come join our Discord, share your opinions and ideas, and advance open LLM research with us!

## Acknowledgements

Many thanks first and foremost to [Mistral AI](https://huggingface.co/mistralai) for releasing another awesome model and their release strategy that is much fun for the whole community. 
Additionally, many thanks in particular to [Dmytro Dzhulgakov](https://huggingface.co/dzhulgakov) who was the first one with a running [inference implementation](https://github.com/dzhulgakov/llama-mistral), [Vik](https://huggingface.co/vikhyatk) who spotted a critical bug in our first implementation (he actually read the paper!), [winglian](https://huggingface.co/winglian) for helpful advice and Axolotl which was used to finetune the model, [MigTissera](https://huggingface.co/migtissera), [MetaMath](https://huggingface.co/meta-math) and [LDJnr](https://huggingface.co/LDJnr) for their great datasets, and everyone who participated in this awesome speedrun on either our, the [Nous Research](https://huggingface.co/NousResearch) or one of the other Discords (please contact us if we forgot to mention you here!). 

**DiscoLM Mixtral is a [DiscoResearch](https://huggingface.co/DiscoResearch) project and was created by [Björn Plüster](https://huggingface.co/bjoernp). 
The model was trained with compute provided by [HessianAI](https://hessian.ai/); many thanks as well to [LAION](https://laion.ai) for their coordination and providing invaluable contacts + advice.**

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## Disclaimer

The license on this model does not constitute legal advice. We are not responsible for the actions of third parties who use this model.
This model should only be used for research purposes.