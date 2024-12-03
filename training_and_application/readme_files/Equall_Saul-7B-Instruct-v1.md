---
library_name: transformers
tags:
- legal
license: mit
language:
- en
---

# Equall/Saul-Instruct-v1

This is the instruct model for Equall/Saul-Instruct-v1, a large instruct language model tailored for Legal domain. This model is obtained by continue pretraining of Mistral-7B.

Checkout our website and register https://equall.ai/ 


![image/png](https://cdn-uploads.huggingface.co/production/uploads/644a900e3a619fe72b14af0f/OU4Y3s-WckYKMN4fQkNiS.png)

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:**  Equall.ai in collaboration with CentraleSupelec, Sorbonne Université, Instituto Superior Técnico and NOVA School of Law
- **Model type:** 7B
- **Language(s) (NLP):** English
- **License:** MIT

### Model Sources

<!-- Provide the basic links for the model. -->

- **Paper:** https://arxiv.org/abs/2403.03883

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
You can use it for legal use cases that involves generation.

Here's how you can run the model using the pipeline() function from 🤗 Transformers:

```python

# Install transformers from source - only needed for versions <= v4.34
# pip install git+https://github.com/huggingface/transformers.git
# pip install accelerate

import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="Equall/Saul-Instruct-v1", torch_dtype=torch.bfloat16, device_map="auto")
# We use the tokenizer’s chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {"role": "user", "content": "[YOUR QUERY GOES HERE]"},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=256, do_sample=False)
print(outputs[0]["generated_text"])
```

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->


This model is built upon the technology of LLM, which comes with inherent limitations. It may occasionally generate inaccurate or nonsensical outputs. Furthermore, being a 7B model, it's anticipated to exhibit less robust performance compared to larger models, such as the 70B variant.

## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**


```bibtex
@misc{colombo2024saullm7b,
      title={SaulLM-7B: A pioneering Large Language Model for Law}, 
      author={Pierre Colombo and Telmo Pessoa Pires and Malik Boudiaf and Dominic Culver and Rui Melo and Caio Corro and Andre F. T. Martins and Fabrizio Esposito and Vera Lúcia Raposo and Sofia Morgado and Michael Desa},
      year={2024},
      eprint={2403.03883},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```