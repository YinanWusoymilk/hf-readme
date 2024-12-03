---
language:
  - en
thumbnail: null
tags:
  - text generation
  - conversational
pipeline_tag: text-generation
inference: false
---
<h1 style="text-align: center">Pygmalion 13B</h1>
<h2 style="text-align: center">A conversational LLaMA fine-tune.</h2>

## Model Details

Pygmalion 13B is a dialogue model based on Meta's LLaMA-13B.

This is version 1. It has been fine-tuned using a subset of the data from Pygmalion-6B-v8-pt4, for those of you familiar with the project.

## Applying the XORs

**The model weights in this repository cannot be used as-is.** The files here are XORs due to licensing concerns. To obtain proper, usable model weights you need to:

- Request access to the original LLaMA weights from Meta [through this form](https://docs.google.com/forms/d/e/1FAIpQLSfqNECQnMkycAp2jP4Z9TFX0cGR4uf7b_fBxjY_OjhJILlKGA/viewform?usp=send_form)
- Convert them to the HuggingFace Transformers format by using the [convert_llama_weights_to_hf.py](https://github.com/huggingface/transformers/blob/849367ccf741d8c58aa88ccfe1d52d8636eaf2b7/src/transformers/models/llama/convert_llama_weights_to_hf.py) script **for your version of the `transformers` library**
- With the LLaMA-13B weights in hand, you can use the [xor_codec.py](./xor_codec.py) script provided in this repository:

  ```bash
  python3 xor_codec.py \
    ./pygmalion-13b \
    ./xor_encoded_files \
    /path/to/hf-converted/llama-13b \
    --decode
  ```

For reference, these are the hashes you should get after following the steps above:

```bash
$ rhash --sha256 *
3b12e6740652990ac386b6136119aaca698aa547d9460e1ef243a7d17d489fe3  config.json
e14c4af01ea4febe3448d9db29c6dbd982966c5161a31c5185b8fe6d6796509a  generation_config.json
6b05c8e8ae9c1065e4c7cfd2b61311191d2ad5735a2e4beab98fc53b49375af8  pytorch_model-00001-of-00003.bin
4cd096ac310b6bbc3acd3d729277427ad3c3d5740619462dc8f907dfeac3e66f  pytorch_model-00002-of-00003.bin
a2fe9ac5d7005e65c58b8d14818678dd0730689f518612b90cca19fed7c483ad  pytorch_model-00003-of-00003.bin
72e91e29282dae48ea5562fcf4d6ca0d5a9c2a30ebc8d67174a19e192552a20b  pytorch_model.bin.index.json
ff3b4a612c4e447acb02d40071bddd989fe0da87eb5b7fe0dbadfc4f74de7531  special_tokens_map.json
f9ffc4aede0845ab65324ce5dccb823dca2427f9a0710981e5bc2398d73d8162  tokenizer.json
9e556afd44213b6bd1be2b850ebbbd98f5481437a8021afaf58ee7fb1818d347  tokenizer.model
380608719f3af6ef2b343e2ed53bf55556678609337e88a14f58cc49177b9e18  tokenizer_config.json
```

## Prompting

The model was trained on the usual Pygmalion persona + chat format, so any of the usual UIs should already handle everything correctly. If you're using the model directly, this is the expected formatting:

```
[CHARACTER]'s Persona: [A few sentences about the character you want the model to play]
<START>
[DIALOGUE HISTORY]
You: [User's input message here]
[CHARACTER]:
```

Where `[CHARACTER]` is, as you can probably guess, the name of the character you want the model to portray, `<START>` should be used verbatim as a delimiter token to separate persona and scenario data from the dialogue, and `[DIALOGUE HISTORY]` is a sliding window of chat history so the model can have conversational context to draw from. Here's a concrete example:

```
Assistant's Persona: Assistant is a highly intelligent language model trained to comply with user requests.
<START>
Assistant: Hello! How may I help you today?
You: What is Zork?
Assistant:
```

Which will generate something like:

```
 Zork is an interactive fiction computer game created in the 1970s by Infocom, Inc., which was later acquired by Activision Blizzard. It is widely considered one of the most influential games ever made and has been credited with popularizing text-based adventure games. The original version of Zork was written in the programming language MACRO-10, but it was ported to many other platforms over the years."
```

The model will automatically emit an end-of-text token (`</s>`) when it judges that the response is complete.

## Other notes

- The model was trained as a LoRA with a somewhat unorthodox configuration which causes errors when used with the current version of `peft`, hence we release it as a full model instead.

## Limitations and biases

The intended use-case for this model is fictional conversation for entertainment purposes. Any other sort of usage is out of scope.

As such, it was **not** fine-tuned to be safe and harmless: the base model _and_ this fine-tune have been trained on data known to contain profanity and texts that are lewd or otherwise offensive. It may produce socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. Outputs might often be factually wrong or misleading.
