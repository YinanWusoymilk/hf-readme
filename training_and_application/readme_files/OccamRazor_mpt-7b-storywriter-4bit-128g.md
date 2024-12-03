---
license: apache-2.0
tags:
- Composer
- MosaicML
- llm-foundry
datasets:
- the_pile_books3
inference: false
---

# MPT-7B-StoryWriter-65k+

Quantized for [KoboldAI (4bit-fork)](https://github.com/0cc4m/koboldAI)

MPT-7B-StoryWriter-65k+ is a model designed to read and write fictional stories with super long context lengths.
It was built by finetuning MPT-7B with a context length of 65k tokens on a filtered fiction subset of the [books3 dataset](https://huggingface.co/datasets/the_pile_books3).
At inference time, thanks to [ALiBi](https://arxiv.org/abs/2108.12409), MPT-7B-StoryWriter-65k+ can extrapolate even beyond 65k tokens.
We demonstrate generations as long as 84k tokens on a single node of 8 A100-80GB GPUs in our [blogpost](www.mosaicml.com/blog/mpt-7b).
  * License: _Apache-2.0_ (commercial use permitted)

This model was trained by [MosaicML](https://www.mosaicml.com) and follows a modified decoder-only transformer architecture.

## Model Date

May 5, 2023

## Model License

Apache-2.0 (commercial use permitted)

## Documentation

* [Blog post: Introducing MPT-7B: A New Standard for Open-Source, Commercially Usable LLMs](https://www.mosaicml.com/blog/mpt-7b)
* [Codebase (mosaicml/llm-foundry repo)](https://github.com/mosaicml/llm-foundry/)
* Questions: Feel free to contact us via the [MosaicML Community Slack](https://join.slack.com/t/mosaicml-community/shared_invite/zt-1btms90mc-GipE2ufuPkKY0QBrmF3LSA)!


## How to Use

Note: This model requires that `trust_remote_code=True` be passed to the `from_pretrained` method. This is because we use a custom model architecture that is not yet part of the `transformers` package.

It includes options for many training efficiency features such as [FlashAttention (Dao et al. 2022)](https://arxiv.org/pdf/2205.14135.pdf), [ALiBi](https://arxiv.org/abs/2108.12409), QK LayerNorm, and more.

```python
import transformers
model = transformers.AutoModelForCausalLM.from_pretrained(
  'mosaicml/mpt-7b-storywriter',
  trust_remote_code=True
)
```

To use the optimized [triton implementation](https://github.com/openai/triton) of FlashAttention, you can load the model with `attn_impl='triton'` and move the model to `bfloat16`:
```python
config = transformers.AutoConfig.from_pretrained(
  'mosaicml/mpt-7b-storywriter',
  trust_remote_code=True
)
config.attn_config['attn_impl'] = 'triton'

model = transformers.AutoModelForCausalLM.from_pretrained(
  'mosaicml/mpt-7b-storywriter',
  config=config,
  torch_dtype=torch.bfloat16,
  trust_remote_code=True
)
model.to(device='cuda:0')
```

Although the model was trained with a sequence length of 2048 and finetuned with a sequence length of 65536, 
ALiBi enables users to increase the maximum sequence length during finetuning and/or inference. For example:

```python
config = transformers.AutoConfig.from_pretrained(
  'mosaicml/mpt-7b-storywriter',
  trust_remote_code=True
)
config.update({"max_seq_len": 83968})
model = transformers.AutoModelForCausalLM.from_pretrained(
  'mosaicml/mpt-7b-storywriter',
  config=config,
  trust_remote_code=True
)
```

This model was trained with the [EleutherAI/gpt-neox-20b](https://huggingface.co/EleutherAI/gpt-neox-20b) tokenizer.

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
```

## Example Epilogue

The full text of the _The Great Gatsby_ (67873 tokens) was fed to the model, followed by the text "EPILOGUE"

**TheRealFitzgerald233**:

> ...
>
> So we beat on, boats against the current, borne back ceaselessly into the past
>
> EPILOGUE

**MPT-7B-StoryWriter**:

>I have lived so long in the shadow of this dream that I may never see the bright sunlight of reality. I may look up some morning and find that I am six feet under, and that Gatsby, who gave me the dream and everything else, will have vanished behind me.
>
>And so it was. I had hardly crossed the threshold of the old world when my eye caught the headlines of a newspaper, and I knew at once that my dream was over. I knew that Gatsby was dead.
>
>And I knew that day that I didn't love her.
>
>That night I took the last train for West Egg, and when I reached home I went directly to my attic and brought down all Gatsby's letters.
>
>I have sorted them by date and placed them in the order in which they were written. They are very few in number.
>
>They are dated between April of nineteen eighteen and January of nineteen nineteen, and the last one I have here is the one that told me he was dead.
>
>There is something in that last letter that frightens me. It is the sense of a finality, of a completeness. I never heard of him after that, and I was glad.
>
>But a few months ago I read somewhere that he had been seen in New York. He had become a great man.
>
>And I knew that he had not changed at all.

## Model Description

The architecture is a modification of a standard decoder-only transformer.

The model has been modified from a standard transformer in the following ways:
* It uses [FlashAttention](https://arxiv.org/pdf/2205.14135.pdf)
* It uses [ALiBi (Attention with Linear Biases)](https://arxiv.org/abs/2108.12409) and does not use positional embeddings
* It does not use biases


| Hyperparameter | Value |
|----------------|-------|
|n_parameters | 6.7B |
|n_layers | 32 |
| n_heads | 32 |
| d_model | 4096 |
| vocab size | 50432 |
| sequence length | **65536** |

## PreTraining Data

For more details on the pretraining process, see [MPT-7B](https://huggingface.co/mosaicml/mpt-7b).

The data was tokenized using the [EleutherAI/gpt-neox-20b](https://huggingface.co/EleutherAI/gpt-neox-20b) tokenizer.

## Limitations and Biases

_The following language is modified from [EleutherAI's GPT-NeoX-20B](https://huggingface.co/EleutherAI/gpt-neox-20b)_

MPT-7B-StoryWriter can produce factually incorrect output, and should not be relied on to produce factually accurate information.
MPT-7B-StoryWriter was trained on various public datasets.
While great efforts have been taken to clean the pretraining data, it is possible that this model could generate lewd, biased or otherwise offensive outputs.


## Acknowledgements

This model was finetuned by Alex Trott and the MosaicML NLP team

## MosaicML Platform

If you're interested in [training](https://www.mosaicml.com/training) and [deploying](https://www.mosaicml.com/inference) your own MPT or LLMs on the MosaicML Platform, [sign up here](https://forms.mosaicml.com/demo).


## Citation

Please cite this model using the following format:

```
@online{MosaicML2023Introducing,
    author    = {MosaicML NLP Team},
    title     = {Introducing MPT-7B: A New Standard for Open-Source, Commercially Usable LLMs},
    year      = {2023},
    url       = {www.mosaicml.com/blog/mpt-7b},
    note      = {Accessed: 2023-03-28}, % change this date
    urldate   = {2023-03-28} % change this date
}
```
