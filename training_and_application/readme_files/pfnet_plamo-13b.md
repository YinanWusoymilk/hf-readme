---
language:
- en
- ja
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
---

# PLaMo-13B

## Model Description
PLaMo-13B is a LLaMA-based 13B model pre-trained on English and Japanese open datasets, developed by Preferred Networks, Inc.
PLaMo-13B is released under Apache v2.0 license.

[PLaMo-13B Release blog (Japanese)](https://tech.preferred.jp/ja/blog/llm-plamo/)

## Usage

### Requirements

- numpy
- sentencepiece
- torch
- transformers

### Use a pipeline as a high-level helper
```python
import transformers
pipeline = transformers.pipeline("text-generation", model="pfnet/plamo-13b", trust_remote_code=True)
print(pipeline("The future of artificial intelligence technology is ", max_new_tokens=32))
```

### Load model directly
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("pfnet/plamo-13b", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("pfnet/plamo-13b", trust_remote_code=True)
text = "これからの人工知能技術は"
input_ids = tokenizer(text, return_tensors="pt").input_ids
generated_tokens = model.generate(
    inputs=input_ids,
    max_new_tokens=32,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    temperature=1.0,
)[0]
generated_text = tokenizer.decode(generated_tokens)
print(generated_text)
```

## Model Details

- Model size: 13B
- Trained tokens: 1.5T tokens (English: 1.32T tokens, Japanese: 0.18T tokens)
- Context length: 4096
- Developed by: Preferred Networks, Inc
- Model type: Causal decoder-only
- Language(s): English, Japanese
- License: Apache v2.0

## Training Dataset

### English

- C4 - English
- Project Gutenberg
- RedPajama - Arxiv
- RedPajama - CommonCrawl - English
- RedPajama - Github
- RedPajama - StackExchange
- RedPajama - Wikipedia

### Japanese

- mC4 - Japanese
- Wikipedia - Japanese

## Tokenizer
PLaMo-13B uses sentencepiece tokenizer which is trained on a subset of the datasets for model pre-training.

## Bias, Risks, and Limitations
PLaMo-13B is a new technology that carries risks with use. Testing conducted to date has been in English and Japanese, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, PLaMo-13B’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of PLaMo-13B, developers should perform safety testing and tuning tailored to their specific applications of the model.

## How to cite
```tex
@online{PLaMo2023Introducing,
    author    = {Preferred Networks, Inc},
    title     = {PLaMo-13B},
    year      = {2023},
    url       = {https://huggingface.co/pfnet/plamo-13b},
    urldate   = {2023-09-28}
}
```

## Citations
```tex
@article{touvron2023llama,
  title={LLaMA: Open and Efficient Foundation Language Models},
  author={Touvron, Hugo and Lavril, Thibaut and Izacard, Gautier and Martinet, Xavier and Lachaux, Marie-Anne and Lacroix, Timoth{\'e}e and Rozi{\`e}re, Baptiste and Goyal, Naman and Hambro, Eric and Azhar, Faisal and Rodriguez, Aurelien and Joulin, Armand and Grave, Edouard and Lample, Guillaume},
  journal={arXiv preprint arXiv:2302.13971},
  year={2023}
}
```
