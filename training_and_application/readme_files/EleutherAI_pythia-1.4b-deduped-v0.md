---
language:
- en
tags:
- pytorch
- causal-lm
- pythia
- pythia_v0
license: apache-2.0
datasets:
- EleutherAI/the_pile_deduplicated
---

The *Pythia Scaling Suite* is a collection of models developed to facilitate 
interpretability research. It contains two sets of eight models of sizes 
70M, 160M, 410M, 1B, 1.4B, 2.8B, 6.9B, and 12B. For each size, there are two 
models: one trained on the Pile, and one trained on the Pile after the dataset 
has been globally deduplicated. All 8 model sizes are trained on the exact 
same data, in the exact same order. All Pythia models are available 
[on Hugging Face](https://huggingface.co/models?other=pythia).

The Pythia model suite was deliberately designed to promote scientific 
research on large language models, especially interpretability research. 
Despite not centering downstream performance as a design goal, we find the 
models <a href="#evaluations">match or exceed</a> the performance of 
similar and same-sized models, such as those in the OPT and GPT-Neo suites.

Please note that all models in the *Pythia* suite were renamed in January 
2023. For clarity, a <a href="#naming-convention-and-parameter-count">table 
comparing the old and new names</a> is provided in this model card, together 
with exact parameter counts.

## Pythia-1.4B-deduped

### Model Details

- Developed by: [EleutherAI](http://eleuther.ai)
- Model type: Transformer-based Language Model
- Language: English
- Learn more: [Pythia's GitHub repository](https://github.com/EleutherAI/pythia)
 for training procedure, config files, and details on how to use.
- Library: [GPT-NeoX](https://github.com/EleutherAI/gpt-neox)
- License: Apache 2.0
- Contact: to ask questions about this model, join the [EleutherAI 
Discord](https://discord.gg/zBGx3azzUn), and post them in `#release-discussion`.
 Please read the existing *Pythia* documentation before asking about it in the 
 EleutherAI Discord. For general correspondence: [contact@eleuther.
 ai](mailto:contact@eleuther.ai).

<figure>

| Pythia model | Non-Embedding Params | Layers | Model Dim | Heads | Batch Size | Learning Rate         | Equivalent Models      |
| -----------: | -------------------: | :----: | :-------: | :---: | :--------: | :-------------------: | :--------------------: |
| 70M          | 18,915,328           | 6      | 512       | 8     | 2M         | 1.0 x 10<sup>-3</sup> | —                      |
| 160M         | 85,056,000           | 12     | 768       | 12    | 4M         | 6.0 x 10<sup>-4</sup> | GPT-Neo 125M, OPT-125M |
| 410M         | 302,311,424          | 24     | 1024      | 16    | 4M         | 3.0 x 10<sup>-4</sup> | OPT-350M               |
| 1.0B         | 805,736,448          | 16     | 2048      | 8     | 2M         | 3.0 x 10<sup>-4</sup> | —                      |
| 1.4B         | 1,208,602,624        | 24     | 2048      | 16    | 4M         | 2.0 x 10<sup>-4</sup> | GPT-Neo 1.3B, OPT-1.3B |
| 2.8B         | 2,517,652,480        | 32     | 2560      | 32    | 2M         | 1.6 x 10<sup>-4</sup> | GPT-Neo 2.7B, OPT-2.7B |
| 6.9B         | 6,444,163,072        | 32     | 4096      | 32    | 2M         | 1.2 x 10<sup>-4</sup> | OPT-6.7B               |
| 12B          | 11,327,027,200       | 36     | 5120      | 40    | 2M         | 1.2 x 10<sup>-4</sup> | —                      |
<figcaption>Engineering details for the <i>Pythia Suite</i>. Deduped and 
non-deduped models of a given size have the same hyperparameters. “Equivalent” 
models have <b>exactly</b> the same architecture, and the same number of 
non-embedding parameters.</figcaption>
</figure>

### Uses and Limitations

#### Intended Use

The primary intended use of Pythia is research on the behavior, functionality, 
and limitations of large language models. This suite is intended to provide 
a controlled setting for performing scientific experiments. To enable the 
study of how language models change in the course of training, we provide 
143 evenly spaced intermediate checkpoints per model. These checkpoints are 
hosted on Hugging Face as branches. Note that branch `143000` corresponds 
exactly to the model checkpoint on the `main` branch of each model.

You may also further fine-tune and adapt Pythia-1.4B-deduped for deployment, 
as long as your use is in accordance with the Apache 2.0 license. Pythia 
models work with the Hugging Face [Transformers 
Library](https://huggingface.co/docs/transformers/index). If you decide to use 
pre-trained Pythia-1.4B-deduped as a basis for your fine-tuned model, please 
conduct your own risk and bias assessment. 

#### Out-of-scope use

The Pythia Suite is **not** intended for deployment. It is not a in itself 
a product and cannot be used for human-facing interactions. 

Pythia models are English-language only, and are not suitable for translation 
or generating text in other languages.

Pythia-1.4B-deduped has not been fine-tuned for downstream contexts in which 
language models are commonly deployed, such as writing genre prose, 
or commercial chatbots. This means Pythia-1.4B-deduped will **not** 
respond to a given prompt the way a product like ChatGPT does. This is because,
 unlike this model, ChatGPT was fine-tuned using methods such as Reinforcement 
Learning from Human Feedback (RLHF) to better “understand” human instructions.

#### Limitations and biases

The core functionality of a large language model is to take a string of text 
and predict the next token. The token deemed statistically most likely by the 
model need not produce the most “accurate” text. Never rely on 
Pythia-1.4B-deduped to produce factually accurate output.

This model was trained on [the Pile](https://pile.eleuther.ai/), a dataset 
known to contain profanity and texts that are lewd or otherwise offensive. 
See [Section 6 of the Pile paper](https://arxiv.org/abs/2101.00027) for a 
discussion of documented biases with regards to gender, religion, and race. 
Pythia-1.4B-deduped may produce socially unacceptable or undesirable text, 
*even if* the prompt itself does not include anything explicitly offensive. 

If you plan on using text generated through, for example, the Hosted Inference 
API, we recommend having a human curate the outputs of this language model 
before presenting it to other people. Please inform your audience that the 
text was generated by Pythia-1.4B-deduped.

### Quickstart

Pythia models can be loaded and used via the following code, demonstrated here 
for the third `pythia-70m-deduped` checkpoint:

```python
from transformers import GPTNeoXForCausalLM, AutoTokenizer

model = GPTNeoXForCausalLM.from_pretrained(
  "EleutherAI/pythia-70m-deduped",
  revision="step3000",
  cache_dir="./pythia-70m-deduped/step3000",
)

tokenizer = AutoTokenizer.from_pretrained(
  "EleutherAI/pythia-70m-deduped",
  revision="step3000",
  cache_dir="./pythia-70m-deduped/step3000",
)

inputs = tokenizer("Hello, I am", return_tensors="pt")
tokens = model.generate(**inputs)
tokenizer.decode(tokens[0])
```

Revision/branch `step143000` corresponds exactly to the model checkpoint on 
the `main` branch of each model.<br>
For more information on how to use all Pythia models, see [documentation on 
GitHub](https://github.com/EleutherAI/pythia).

### Training

#### Training data

Pythia-1.4B-deduped was trained on the Pile **after the dataset has been 
globally deduplicated**.<br>
[The Pile](https://pile.eleuther.ai/) is a 825GiB general-purpose dataset in 
English. It was created by EleutherAI specifically for training large language 
models. It contains texts from 22 diverse sources, roughly broken down into 
five categories: academic writing (e.g. arXiv), internet (e.g. CommonCrawl), 
prose (e.g. Project Gutenberg), dialogue (e.g. YouTube subtitles), and 
miscellaneous (e.g. GitHub, Enron Emails). See [the Pile 
paper](https://arxiv.org/abs/2101.00027) for a breakdown of all data sources, 
methodology, and a discussion of ethical implications. Consult [the 
datasheet](https://arxiv.org/abs/2201.07311) for more detailed documentation 
about the Pile and its component datasets. The Pile can be downloaded from 
the [official website](https://pile.eleuther.ai/), or from a [community 
mirror](https://the-eye.eu/public/AI/pile/).

#### Training procedure

All models were trained on the exact same data, in the exact same order. Each 
model saw 299,892,736,000 tokens during training, and 143 checkpoints for each 
model are saved every 2,097,152,000 tokens, spaced evenly throughout training. 
This corresponds to training for just under 1 epoch on the Pile for 
non-deduplicated models, and about 1.5 epochs on the deduplicated Pile.

All *Pythia* models trained for the equivalent of 143000 steps at a batch size 
of 2,097,152 tokens. Two batch sizes were used: 2M and 4M. Models with a batch 
size of 4M tokens listed were originally trained for 71500 steps instead, with 
checkpoints every 500 steps. The checkpoints on Hugging Face are renamed for 
consistency with all 2M batch models, so `step1000` is the first checkpoint 
for `pythia-1.4b` that was saved (corresponding to step 500 in training), and 
`step1000` is likewise the first `pythia-6.9b` checkpoint that was saved 
(corresponding to 1000 “actual” steps).<br>
See [GitHub](https://github.com/EleutherAI/pythia) for more details on training 
procedure, including [how to reproduce 
it](https://github.com/EleutherAI/pythia/blob/main/README.md#reproducing-training).<br>
Pythia uses the same tokenizer as [GPT-NeoX-
20B](https://huggingface.co/EleutherAI/gpt-neox-20b).

### Evaluations

All 16 *Pythia* models were evaluated using the [LM Evaluation 
Harness](https://github.com/EleutherAI/lm-evaluation-harness). You can access 
the results by model and step at `results/json/*` in the [GitHub 
repository](https://github.com/EleutherAI/pythia/tree/main/results/json).<br>
Expand the sections below to see plots of evaluation results for all 
Pythia and Pythia-deduped models compared with OPT and BLOOM.

<details>
  <summary>LAMBADA – OpenAI</summary>
  <img src="/EleutherAI/pythia-12b/resolve/main/eval_plots/lambada_openai.png" style="width:auto"/>
</details>

<details>
  <summary>Physical Interaction: Question Answering (PIQA)</summary>
  <img src="/EleutherAI/pythia-12b/resolve/main/eval_plots/piqa.png" style="width:auto"/>
</details>

<details>
  <summary>WinoGrande</summary>
  <img src="/EleutherAI/pythia-12b/resolve/main/eval_plots/winogrande.png" style="width:auto"/>
</details>

<details>
  <summary>AI2 Reasoning Challenge – Challenge Set</summary>
  <img src="/EleutherAI/pythia-12b/resolve/main/eval_plots/arc_challenge.png" style="width:auto"/>
</details>

<details>
  <summary>SciQ</summary>
  <img src="/EleutherAI/pythia-12b/resolve/main/eval_plots/sciq.png" style="width:auto"/>
</details>

### Naming convention and parameter count

*Pythia* models were renamed in January 2023. It is possible that the old 
naming convention still persists in some documentation by accident. The 
current naming convention (70M, 160M, etc.) is based on total parameter count. 

<figure style="width:32em">
  
| current Pythia suffix | old suffix | total params   | non-embedding params |
| --------------------: | ---------: | -------------: | -------------------: |
| 70M                   | 19M        | 70,426,624     | 18,915,328           |
| 160M                  | 125M       | 162,322,944    | 85,056,000           |
| 410M                  | 350M       | 405,334,016    | 302,311,424          |
| 1B                    | 800M       | 1,011,781,632  | 805,736,448          |
| 1.4B                  | 1.3B       | 1,414,647,808  | 1,208,602,624        |
| 2.8B                  | 2.7B       | 2,775,208,960  | 2,517,652,480        |
| 6.9B                  | 6.7B       | 6,857,302,016  | 6,444,163,072        |
| 12B                   | 13B        | 11,846,072,320 | 11,327,027,200       |
</figure>