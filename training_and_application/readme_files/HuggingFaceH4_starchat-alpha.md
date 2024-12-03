---
license: bigcode-openrail-m
datasets:
- OpenAssistant/oasst1
- databricks/databricks-dolly-15k
language:
- en
library_name: transformers
tags:
- code
---

# Model Card for StarChat Alpha

<!-- Provide a quick summary of what the model is/does. -->
_Note, you may be interested in the Beta version of StarChat [here](https://huggingface.co/HuggingFaceH4/starchat-beta)._

StarChat is a series of language models that are fine-tuned from StarCoder to act as helpful coding assistants. StarChat Alpha is the first of these models, and as an alpha release is only intended for educational or research purpopses. In particular, the model has not been aligned to human preferences with techniques like RLHF, so may generate problematic content (especially when prompted to do so).

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Model type:** A 16B parameter GPT-like model fine-tuned on a blend of the [`oasst1`](https://huggingface.co/datasets/OpenAssistant/oasst1) and [`databricks-dolly-15k`](https://huggingface.co/datasets/databricks/databricks-dolly-15k) datasets.
- **Language(s) (NLP):** English
- **License:** BigCode Open RAIL-M v1
- **Finetuned from model:** [bigcode/starcoderbase](https://huggingface.co/bigcode/starcoderbase)

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/bigcode-project/starcoder
- **Demo:** https://huggingface.co/spaces/HuggingFaceH4/starchat-playground

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

StarChat Alpha is intended for educational and/or research purposes and in that respect can be used to probe the programming capabilities of open-source language models.

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

StarChat Alpha has not been aligned to human preferences with techniques like RLHF or deployed with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). 
Models trained primarily on code data will also have a more skewed demographic bias commensurate with the demographics of the GitHub community, for more on this see the [StarCoder dataset](https://huggingface.co/datasets/bigcode/starcoderdata) which is derived from The Stack.


Since the base model was pretrained on a large corpus of code, it may produce code snippets that are syntactically valid but semantically incorrect. 
For example, it may produce code that does not compile or that produces incorrect results.  
It may also produce code that is vulnerable to security exploits.  
We have observed the model also has a tendency to produce false URLs which should be carefully inspected before clicking.

StarChat Alpha was fine-tuned from the base model [StarCoder Base](https://huggingface.co/bigcode/starcoderbase), please refer to its model card's [Limitations Section](https://huggingface.co/bigcode/starcoderbase#limitations) for relevant information. 
In particular, the model was evaluated on some categories of gender biases, propensity for toxicity, and risk of suggesting code completions with known security flaws; these evaluations are reported in its [technical report](https://drive.google.com/file/d/1cN-b9GnWtHzQRoE7M7gAEyivY0kl4BYs/view).

## How to Get Started with the Model

Use the code below to get started with the model.

Here's how you can run the model using the `pipeline()` function from 🤗 Transformers:

```python
import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="HuggingFaceH4/starchat-alpha", torch_dtype=torch.bfloat16, device_map="auto")

prompt_template = "<|system|>\n<|end|>\n<|user|>\n{query}<|end|>\n<|assistant|>"
prompt = prompt_template.format(query="How do I sort a list in Python?")
# We use a special <|end|> token with ID 49155 to denote ends of a turn
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.2, top_k=50, top_p=0.95, eos_token_id=49155)
# You can sort a list in Python by using the sort() method. Here's an example:\n\n```\nnumbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]\nnumbers.sort()\nprint(numbers)\n```\n\nThis will sort the list in place and print the sorted list.
```



## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```
@article{Tunstall2023starchat-alpha,
  author = {Tunstall, Lewis and Lambert, Nathan and Rajani, Nazneen and Beeching, Edward and Le Scao, Teven and von Werra, Leandro and Han, Sheon and Schmid, Philipp and Rush, Alexander},
  title = {Creating a Coding Assistant with StarCoder},
  journal = {Hugging Face Blog},
  year = {2023},
  note = {https://huggingface.co/blog/starchat},
}
```