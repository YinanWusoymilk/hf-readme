---
license: "cc-by-nc-4.0"
tags:
- code
- python
- javascript
---

# InCoder 6B

A 6B parameter decoder-only Transformer model trained on code using a causal-masked objective, which allows inserting/infilling code as well as standard left-to-right generation.

The model was trained on public open-source repositories with a permissive, non-copyleft, license (Apache 2.0, MIT, BSD-2 or BSD-3) from GitHub and GitLab, as well as StackOverflow. Repositories primarily contained Python and JavaScript, but also include code from 28 languages, as well as StackOverflow. 

For more information, see our:

- [Demo](https://huggingface.co/spaces/facebook/incoder-demo)
- [Project site](https://sites.google.com/view/incoder-code-models)
- [Examples](https://sites.google.com/view/incoder-code-models/home/examples)
- [Paper](https://arxiv.org/abs/2204.05999)

A smaller, 1B, parameter model is also available at [facebook/incoder-1B](https://huggingface.co/facebook/incoder-1B).

## Requirements

`pytorch`, `tokenizers`, and `transformers`. Our model requires HF's tokenizers >= 0.12.1, due to changes in the pretokenizer.

```
pip install torch
pip install "tokenizers>=0.12.1"
pip install transformers
```

## Usage

### Model

See [https://github.com/dpfried/incoder](https://github.com/dpfried/incoder) for example code.

This 6B model comes in two versions: with weights in full-precision (float32, stored on branch `main`) and weights in half-precision (float16, stored on branch `float16`). The versions can be loaded as follows:

*Full-precision* (float32): This should be used if you are fine-tuning the model (note: this will take a lot of GPU memory, probably multiple GPUs, and we have not tried training the model in `transformers` --- it was trained in Fairseq). Load with:

`model = AutoModelForCausalLM.from_pretrained("facebook/incoder-6B")`

*Half-precision* (float16): This can be used if you are only doing inference (i.e. generating from the model). It will use less GPU memory, and less RAM when loading the model. With this version it should be able to perform inference on a 16 GB GPU (with a batch size of 1, to sequence lengths of at least 256). Load with:

`model = AutoModelForCausalLM.from_pretrained("facebook/incoder-6B", revision="float16", torch_dtype=torch.float16, low_cpu_mem_usage=True)`

### Tokenizer
`tokenizer = AutoTokenizer.from_pretrained("facebook/incoder-6B")`

Note: the incoder-1B and incoder-6B tokenizers are identical, so 'facebook/incoder-1B' could also be used.

When calling `tokenizer.decode`, it's important to pass `clean_up_tokenization_spaces=False` to avoid removing spaces after punctuation:

`tokenizer.decode(tokenizer.encode("from ."), clean_up_tokenization_spaces=False)`

(Note: encoding prepends the `<|endoftext|>` token, as this marks the start of a document to our model. This token can be removed from the decoded output by passing `skip_special_tokens=True` to `tokenizer.decode`.)

## License

CC-BY-NC 4.0

## Credits

The model was developed by Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida Wang, Eric Wallace, Freda Shi, Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer and Mike Lewis.

Thanks to Lucile Saulnier, Leandro von Werra, Nicolas Patry, Suraj Patil, Omar Sanseviero, and others at HuggingFace for help with the model release, and to Naman Goyal and Stephen Roller for the code our demo was based on!