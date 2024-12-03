---
language:
- multilingual
tags:
- code
- sentence embedding
license: mit
datasets:
- CodeSearchNet
pipeline_tag: feature-extraction
---

# Model Card for CodeCSE
A simple pre-trained model for code and comment sentence embeddings using contrastive learning. This model was pretrained using [CodeSearchNet](https://huggingface.co/datasets/code_search_net).

Please [**clone the CodeCSE repository**](https://github.com/emu-se/CodeCSE) to get `GraphCodeBERTForCL` and other dependencies to use this pretrained model. https://github.com/emu-se/CodeCSE

Detailed instructions are listed in the repository's README.md. Overall, you will need:

1. GraphCodeBERT (CodeCSE uses GraphCodeBERT's input format for code)
2. GraphCodeBERTForCL defined in [codecse/codecse](https://github.com/emu-se/CodeCSE/tree/main/codecse/codecse)

## Inference example
NL input example: example_nl.json
```json
{
    "original_string": "", 
    "docstring_tokens": ["Save", "model", "to", "a", "pickle", "located", "at", "path"], 
    "url": "https://github.com/openai/baselines/blob/3301089b48c42b87b396e246ea3f56fa4bfc9678/baselines/deepq/deepq.py#L55-L72"
}
```

Code snippet to get the embedding of an NL document ([link to complete code](https://github.com/emu-se/CodeCSE/blob/a04a025c7048204bdfd908fe259fafc55e2df169/inference.py#L105)):
```
nl_json = load_example("example_nl.json")
batch = prepare_inputs(nl_json, tokenizer, args)
nl_inputs = batch[3]
with torch.no_grad():        
    nl_vec = model(input_ids=nl_inputs, sent_emb="nl")[1] 
```