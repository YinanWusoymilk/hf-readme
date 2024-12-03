---
license: gemma
library_name: transformers
pipeline_tag: text-generation
extra_gated_heading: Access Gemma on Hugging Face
extra_gated_prompt: >-
  To access Gemma on Hugging Face, you’re required to review and agree to
  Google’s usage license. To do this, please ensure you’re logged in to Hugging
  Face and click below. Requests are processed immediately.
extra_gated_button_content: Acknowledge license
tags:
- conversational
quantized_by: bartowski
lm_studio:
  param_count: 2b
  use_case: general
  release_date: 31-07-2024
  model_creator: google
  prompt_template: Google Gemma Instruct
  system_prompt: none
  base_model: gemma
  original_repo: google/gemma-2-2b-it
base_model: google/gemma-2-2b-it
---

## 💫 Community Model> Gemma 2 2b Instruct by Google

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [Google](https://huggingface.co/google)<br>
**Original model**: [gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` release [b3496](https://github.com/ggerganov/llama.cpp/releases/tag/b3496)<br>

## Model Summary:
Gemma 2 instruct is a a brand new model from Google in the Gemma family based on the technology from Gemini. Trained on a combination of web documents, code, and mathematics, this model should excel at anything you throw at it.<br>
At only 2b parameters, this is a great size for edge and low power compute, or as an autocomplete or draft model.

## Prompt Template:

Choose the 'Google Gemma Instruct' preset in your LM Studio. 

Under the hood, the model will see a prompt that's formatted like so:

```
<start_of_turn>user
{prompt}<end_of_turn>
<start_of_turn>model
```

Note that this model does not support a System prompt.

## Technical Details

Gemma 2 features the same extremely large vocabulary from release 1.1, which tends to help with multilingual and coding proficiency.

Gemma 2 2b was trained on a wide dataset of 2 trillion tokens, which is an incredible ratio of training tokens to model parameters.

- Web Documents: A diverse collection of web text ensures the model is exposed to a broad range of linguistic styles, topics, and vocabulary. Primarily English-language content.
- Code: Exposing the model to code helps it to learn the syntax and patterns of programming languages, which improves its ability to generate code or understand code-related questions.
- Mathematics: Training on mathematical text helps the model learn logical reasoning, symbolic representation, and to address mathematical queries.

For more details check out their blog post here: https://developers.googleblog.com/en/smaller-safer-more-transparent-advancing-responsible-ai-with-gemma/

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.

🙏 Special thanks to [Kalomaze](https://github.com/kalomaze) and [Dampf](https://github.com/Dampfinchen) for their work on the dataset (linked [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)) that was used for calculating the imatrix for all sizes.

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.