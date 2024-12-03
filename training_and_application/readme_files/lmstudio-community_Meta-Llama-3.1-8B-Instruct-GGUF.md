---
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
pipeline_tag: text-generation
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
license: llama3.1
lm_studio:
  param_count: 8b
  use_case: chat
  release_date: 23-07-2024
  model_creator: Meta
  prompt_template: Llama 3
  base_model: llama
  original_repo: meta-llama/Meta-Llama-3.1-8B-Instruct
base_model: meta-llama/Meta-Llama-3.1-8B-Instruct
---

## 💫 Community Model> Llama 3.1 8B Instruct by Meta

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [meta-llama](https://huggingface.co/meta-llama)<br>
**Original model**: [Meta-Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` release [b3472](https://github.com/ggerganov/llama.cpp/releases/tag/b3441)<br>

<span style="font-size:1.5em;"><b>Important:</b> Requires LM Studio version 0.2.29, available now [here](https://lmstudio.ai/)!</span>

## Model Summary:

Llama 3.1 is an update to the previously released family of Llama 3 models. It has improved performance across the board, especially in multilingual tasks.<br>
It is the current state of the art for open source and can be used for basically any task you throw at it.

## Prompt Template:

Choose the 'Llama 3' preset in your LM Studio. 

Under the hood, the model will see a prompt that's formatted like so:

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

```

## Technical Details

Llama 3.1 features an improved 128k context window.

It has been trained on 15T tokens, including 25 million synthetically generated samples.

For more details, check their blog post [here](https://ai.meta.com/blog/meta-llama-3-1/)

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.

🙏 Special thanks to [Kalomaze](https://github.com/kalomaze) for his dataset (linked [here](https://github.com/ggerganov/llama.cpp/discussions/5263)) that was used for calculating the imatrix for these quants, which improves the overall quality!

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.
