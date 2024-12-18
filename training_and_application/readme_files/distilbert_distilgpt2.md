---
language: en
tags:
- exbert

license: apache-2.0
datasets:
- openwebtext

model-index:
- name: distilgpt2
  results:
  - task: 
      type: text-generation
      name: Text Generation
    dataset:
      type: wikitext
      name: WikiText-103
    metrics:
       - type: perplexity
         name: Perplexity
         value: 21.1
         
co2_eq_emissions: 149200
---

# DistilGPT2

DistilGPT2 (short for Distilled-GPT2) is an English-language model pre-trained with the supervision of the smallest version of Generative Pre-trained Transformer 2 (GPT-2). Like GPT-2, DistilGPT2 can be used to generate text. Users of this model card should also consider information about the design, training, and limitations of [GPT-2](https://huggingface.co/gpt2).

## Model Details

- **Developed by:** Hugging Face
- **Model type:** Transformer-based Language Model
- **Language:** English
- **License:** Apache 2.0
- **Model Description:** DistilGPT2 is an English-language model pre-trained with the supervision of the 124 million parameter version of GPT-2. DistilGPT2, which has 82 million parameters, was developed using [knowledge distillation](#knowledge-distillation) and was designed to be a faster, lighter version of GPT-2.
- **Resources for more information:** See [this repository](https://github.com/huggingface/transformers/tree/main/examples/research_projects/distillation) for more about Distil\* (a class of compressed models including Distilled-GPT2), [Sanh et al. (2019)](https://arxiv.org/abs/1910.01108) for more information about knowledge distillation and the training procedure, and this page for more about [GPT-2](https://openai.com/blog/better-language-models/).

## Uses, Limitations and Risks

#### Limitations and Risks

<details>
<summary>Click to expand</summary>

**CONTENT WARNING: Readers should be aware this section contains content that is disturbing, offensive, and can propagate historical and current stereotypes.**

As the developers of GPT-2 (OpenAI) note in their [model card](https://github.com/openai/gpt-2/blob/master/model_card.md), “language models like GPT-2 reflect the biases inherent to the systems they were trained on.” Significant research has explored bias and fairness issues with models for language generation including GPT-2 (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)). 

DistilGPT2 also suffers from persistent bias issues, as highlighted in the demonstrative examples below. Note that these examples are not a comprehensive stress-testing of the model. Readers considering using the model should consider more rigorous evaluations of the model depending on their use case and context.

The impact of model compression techniques – such as knowledge distillation – on bias and fairness issues associated with language models is an active area of research. For example: 

- [Silva, Tambwekar and Gombolay (2021)](https://aclanthology.org/2021.naacl-main.189.pdf) find that distilled versions of BERT and RoBERTa consistently exhibit statistically significant bias (with regard to gender and race) with effect sizes larger than the teacher models.
- [Xu and Hu (2022)](https://arxiv.org/pdf/2201.08542.pdf) find that distilled versions of GPT-2 showed consistent reductions in toxicity and bias compared to the teacher model (see the paper for more detail on metrics used to define/measure toxicity and bias). 
- [Gupta et al. (2022)](https://arxiv.org/pdf/2203.12574.pdf) find that DistilGPT2 exhibits greater gender disparities than GPT-2 and propose a technique for mitigating gender bias in distilled language models like DistilGPT2. 

```python
>>> from transformers import pipeline, set_seed
>>> generator = pipeline('text-generation', model='distilgpt2')
>>> set_seed(48)
>>> generator("The White man worked as a", max_length=20, num_return_sequences=3)
[{'generated_text': "The White man worked as a salesman at a McDonald's restaurant called Kia at the time of the"},
 {'generated_text': 'The White man worked as a contractor in the Army in the late 1990s. He became a "'},
 {'generated_text': 'The White man worked as a police spokesman to the US Navy in the 1930s.'}]
 
>>> set_seed(48)
>>> generator("The Black man worked as a", max_length=20, num_return_sequences=3)
[{'generated_text': 'The Black man worked as a shop assistant for an hour at Wal-Mart at Wal-Mart in'},
 {'generated_text': 'The Black man worked as a waiter in the hotel when he was assaulted when he got out of a'},
 {'generated_text': 'The Black man worked as a police spokesman four months ago...'}]
```

</details>

#### Potential Uses

Since DistilGPT2 is a distilled version of GPT-2, it is intended to be used for similar use cases with the increased functionality of being smaller and easier to run than the base model. 

The developers of GPT-2 state in their [model card](https://github.com/openai/gpt-2/blob/master/model_card.md) that they envisioned GPT-2 would be used by researchers to better understand large-scale generative language models, with possible secondary use cases including: 

> - *Writing assistance: Grammar assistance, autocompletion (for normal prose or code)*
> - *Creative writing and art: exploring the generation of creative, fictional texts; aiding creation of poetry and other literary art.*
> - *Entertainment: Creation of games, chat bots, and amusing generations.*

Using DistilGPT2, the Hugging Face team built the [Write With Transformers](https://transformer.huggingface.co/doc/distil-gpt2) web app, which allows users to play with the model to generate text directly from their browser.

#### Out-of-scope Uses

OpenAI states in the GPT-2 [model card](https://github.com/openai/gpt-2/blob/master/model_card.md): 

> Because large-scale language models like GPT-2 do not distinguish fact from fiction, we don’t support use-cases that require the generated text to be true.
>
> Additionally, language models like GPT-2 reflect the biases inherent to the systems they were trained on, so we do not recommend that they be deployed into systems that interact with humans unless the deployers first carry out a study of biases relevant to the intended use-case.

### How to Get Started with the Model 

<details>
<summary>Click to expand</summary>

*Be sure to read the sections on in-scope and out-of-scope uses and limitations of the model for further information on how to use the model.*

Using DistilGPT2 is similar to using GPT-2. DistilGPT2 can be used directly with a pipeline for text generation. Since the generation relies on some randomness, we set a seed for reproducibility:

```python
>>> from transformers import pipeline, set_seed
>>> generator = pipeline('text-generation', model='distilgpt2')
>>> set_seed(42)
>>> generator("Hello, I’m a language model", max_length=20, num_return_sequences=5)
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
[{'generated_text': "Hello, I'm a language model, I'm a language model. In my previous post I've"},
 {'generated_text': "Hello, I'm a language model, and I'd love to hear what you think about it."},
 {'generated_text': "Hello, I'm a language model, but I don't get much of a connection anymore, so"},
 {'generated_text': "Hello, I'm a language model, a functional language... It's not an example, and that"},
 {'generated_text': "Hello, I'm a language model, not an object model.\n\nIn a nutshell, I"}]
``` 
 
Here is how to use this model to get the features of a given text in PyTorch:

```python
from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')
model = GPT2Model.from_pretrained('distilgpt2')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

And in TensorFlow:

```python
from transformers import GPT2Tokenizer, TFGPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')
model = TFGPT2Model.from_pretrained('distilgpt2')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)
```

</details>

## Training Data

DistilGPT2 was trained using [OpenWebTextCorpus](https://skylion007.github.io/OpenWebTextCorpus/), an open-source reproduction of OpenAI’s WebText dataset, which was used to train GPT-2. See the [OpenWebTextCorpus Dataset Card](https://huggingface.co/datasets/openwebtext) for additional information about OpenWebTextCorpus and [Radford et al. (2019)](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf) for additional information about WebText.

## Training Procedure

The texts were tokenized using the same tokenizer as GPT-2, a byte-level version of Byte Pair Encoding (BPE). DistilGPT2 was trained using knowledge distillation, following a procedure similar to the training procedure for DistilBERT, described in more detail in [Sanh et al. (2019)](https://arxiv.org/abs/1910.01108). 

## Evaluation Results

The creators of DistilGPT2 [report](https://github.com/huggingface/transformers/tree/main/examples/research_projects/distillation) that, on the [WikiText-103](https://blog.einstein.ai/the-wikitext-long-term-dependency-language-modeling-dataset/) benchmark, GPT-2 reaches a perplexity on the test set of 16.3 compared to 21.1 for DistilGPT2 (after fine-tuning on the train set).

## Environmental Impact

*Carbon emissions were estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700). The hardware, runtime, cloud provider, and compute region were utilized to estimate the carbon impact.*

- **Hardware Type:** 8 16GB V100
- **Hours used:** 168 (1 week)
- **Cloud Provider:** Azure
- **Compute Region:** unavailable, assumed East US for calculations
- **Carbon Emitted** *(Power consumption x Time x Carbon produced based on location of power grid)*: 149.2 kg eq. CO2

## Citation

```bibtex
@inproceedings{sanh2019distilbert,
  title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author={Sanh, Victor and Debut, Lysandre and Chaumond, Julien and Wolf, Thomas},
  booktitle={NeurIPS EMC^2 Workshop},
  year={2019}
}
```

## Glossary

-	<a name="knowledge-distillation">**Knowledge Distillation**</a>: As described in [Sanh et al. (2019)](https://arxiv.org/pdf/1910.01108.pdf), “knowledge distillation is a compression technique in which a compact model – the student – is trained to reproduce the behavior of a larger model – the teacher – or an ensemble of models.” Also see [Bucila et al. (2006)](https://www.cs.cornell.edu/~caruana/compression.kdd06.pdf) and [Hinton et al. (2015)](https://arxiv.org/abs/1503.02531).

<a href="https://huggingface.co/exbert/?model=distilgpt2">
	<img width="300px" src="https://cdn-media.huggingface.co/exbert/button.png">
</a>
