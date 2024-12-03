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
<h1 style="text-align: center">Pygmalion 7B</h1>
<h2 style="text-align: center">A conversational LLaMA fine-tune.</h2>

## Model Details

Pygmalion 7B is a dialogue model based on Meta's LLaMA-7B.

This is version 1. It has been fine-tuned using a subset of the data from Pygmalion-6B-v8-pt4, for those of you familiar with the project.

## Applying the XORs

**The model weights in this repository cannot be used as-is.** The files here are XORs due to licensing concerns. To obtain proper, usable model weights you need to:

- Request access to the original LLaMA weights from Meta [through this form](https://docs.google.com/forms/d/e/1FAIpQLSfqNECQnMkycAp2jP4Z9TFX0cGR4uf7b_fBxjY_OjhJILlKGA/viewform?usp=send_form)
- Convert them to the HuggingFace Transformers format by using the [convert_llama_weights_to_hf.py](https://github.com/huggingface/transformers/blob/849367ccf741d8c58aa88ccfe1d52d8636eaf2b7/src/transformers/models/llama/convert_llama_weights_to_hf.py) script **for your version of the `transformers` library**
- With the LLaMA-7B weights in hand, you can use the [xor_codec.py](./xor_codec.py) script provided in this repository:

  ```bash
  python3 xor_codec.py \
    ./pygmalion-7b \
    ./xor_encoded_files \
    /path/to/hf-converted/llama-7b \
    --decode
  ```

```bash
$ rhash -M *
4608facb4910118f8dfa80f090cbc4dc  config.json
2917a1cafb895cf57e746cfd7696bfe5  generation_config.json
98764eb949eea16f8e2e1c2d3dea0066  pytorch_model-00001-of-00002.bin
be9ba2f37228a0a9ea0eaf6530aba4de  pytorch_model-00002-of-00002.bin
81648ef3915ed2e83d49fed93122d53e  pytorch_model.bin.index.json
6b2e0a735969660e720c27061ef3f3d3  special_tokens_map.json
fdb311c39b8659a5d5c1991339bafc09  tokenizer.json
eeec4125e9c7560836b4873b6f8e3025  tokenizer.model
9b3cf7b8c0e4783dbc1419b4cafe8e1e  tokenizer_config.json
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

## Limitations and biases

The intended use-case for this model is fictional conversation for entertainment purposes. Any other sort of usage is out of scope.

As such, it was **not** fine-tuned to be safe and harmless: the base model _and_ this fine-tune have been trained on data known to contain profanity and texts that are lewd or otherwise offensive. It may produce socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. Outputs might often be factually wrong or misleading.
