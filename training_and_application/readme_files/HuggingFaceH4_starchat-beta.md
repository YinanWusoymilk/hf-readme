---
tags:
- generated_from_trainer
widget:
- text: "How can I write a Python function to generate the nth Fibonacci number?"
- text: "How do I get the current date using shell commands? Explain how it works."
model-index:
- name: starchat-beta
  results: []
license: bigcode-openrail-m
---


<img src="https://huggingface.co/HuggingFaceH4/starchat-beta/resolve/main/model_logo.png" alt="StarChat Beta Logo" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

# Model Card for StarChat-β

StarChat is a series of language models that are trained to act as helpful coding assistants. StarChat-β is the second model in the series, and is a fine-tuned version of [StarCoderPlus](https://huggingface.co/bigcode/starcoderplus) that was trained on an ["uncensored"](https://erichartford.com/uncensored-models) variant of the [`openassistant-guanaco` dataset](https://huggingface.co/datasets/timdettmers/openassistant-guanaco). We found that removing the in-built alignment of the OpenAssistant dataset boosted performance on the [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) and made the model more helpful at coding tasks. However, this means that model is likely to generate problematic text when prompted to do so and should only be used for educational and research purposes.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Model type:** A 16B parameter GPT-like model fine-tuned on an ["uncensored"](https://erichartford.com/uncensored-models) variant of the [`openassistant-guanaco` dataset](https://huggingface.co/datasets/timdettmers/openassistant-guanaco).
- **Language(s) (NLP):** Primarily English and 80+ programming languages.
- **License:** BigCode Open RAIL-M v1
- **Finetuned from model:** [bigcode/starcoderplus](https://huggingface.co/bigcode/starcoderplus)

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/bigcode-project/starcoder
- **Demo:** https://huggingface.co/spaces/HuggingFaceH4/starchat-playground


## Intended uses & limitations

The model was fine-tuned on a variant of the [`OpenAssistant/oasst1`](https://huggingface.co/datasets/OpenAssistant/oasst1) dataset, which contains a diverse range of dialogues in over 35 languages. As a result, the model can be used for chat and you can check out our [demo](https://huggingface.co/spaces/HuggingFaceH4/starchat-playground) to test its coding capabilities. 

Here's how you can run the model using the `pipeline()` function from 🤗 Transformers:

```python
import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="HuggingFaceH4/starchat-beta", torch_dtype=torch.bfloat16, device_map="auto")

# We use a variant of ChatML to format each message
prompt_template = "<|system|>\n<|end|>\n<|user|>\n{query}<|end|>\n<|assistant|>"
prompt = prompt_template.format(query="How do I sort a list in Python?")
# We use a special <|end|> token with ID 49155 to denote ends of a turn
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.2, top_k=50, top_p=0.95, eos_token_id=49155)
# You can sort a list in Python by using the sort() method. Here's an example:\n\n```\nnumbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]\nnumbers.sort()\nprint(numbers)\n```\n\nThis will sort the list in place and print the sorted list.
```

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

StarChat-β has not been aligned to human preferences with techniques like RLHF or deployed with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). 
Models trained primarily on code data will also have a more skewed demographic bias commensurate with the demographics of the GitHub community, for more on this see the [StarCoder dataset](https://huggingface.co/datasets/bigcode/starcoderdata) which is derived from The Stack.

Since the base model was pretrained on a large corpus of code, it may produce code snippets that are syntactically valid but semantically incorrect. 
For example, it may produce code that does not compile or that produces incorrect results.  
It may also produce code that is vulnerable to security exploits.  
We have observed the model also has a tendency to produce false URLs which should be carefully inspected before clicking.

StarChat-β was fine-tuned from the base model [StarCoderPlus](https://huggingface.co/bigcode/starcoderplus), please refer to its model card's [Limitations Section](https://huggingface.co/bigcode/starcoderplus#limitations) for relevant information. 
In particular, the model was evaluated on some categories of gender biases, propensity for toxicity, and risk of suggesting code completions with known security flaws; these evaluations are reported in its [technical report](https://drive.google.com/file/d/1cN-b9GnWtHzQRoE7M7gAEyivY0kl4BYs/view).

## Training and evaluation data

StarChat-β is trained on an ["uncensored"](https://erichartford.com/uncensored-models) variant of the [`openassistant-guanaco` dataset](https://huggingface.co/datasets/timdettmers/openassistant-guanaco). We applied the same [recipe](https://huggingface.co/datasets/ehartford/WizardLM_alpaca_evol_instruct_70k_unfiltered/blob/main/wizardlm_clean.py) used to filter the ShareGPT datasets behind the [WizardLM](https://huggingface.co/datasets/ehartford/WizardLM_alpaca_evol_instruct_70k_unfiltered).

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.5321        | 0.98  | 15   | 1.2856          |
| 1.2071        | 1.97  | 30   | 1.2620          |
| 1.0162        | 2.95  | 45   | 1.2853          |
| 0.8484        | 4.0   | 61   | 1.3274          |
| 0.6981        | 4.98  | 76   | 1.3994          |
| 0.5668        | 5.9   | 90   | 1.4720          |


### Framework versions

- Transformers 4.28.1
- Pytorch 2.0.1+cu118
- Datasets 2.12.0
- Tokenizers 0.13.3

## Citation

Although there isn't a blog post or paper associated with StarChat-β, you can find details on the earlier version in the blog post below:

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