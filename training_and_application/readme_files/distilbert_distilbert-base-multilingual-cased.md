---
language: 
- multilingual
- af
- sq
- ar
- an
- hy
- ast
- az
- ba
- eu
- bar
- be
- bn
- inc
- bs
- br
- bg
- my
- ca
- ceb
- ce
- zh
- cv
- hr
- cs
- da
- nl
- en
- et
- fi
- fr
- gl
- ka
- de
- el
- gu
- ht
- he
- hi
- hu
- is
- io
- id
- ga
- it
- ja
- jv
- kn
- kk
- ky
- ko
- la
- lv
- lt
- roa
- nds
- lm
- mk
- mg
- ms
- ml
- mr
- mn
- min
- ne
- new
- nb
- nn
- oc
- fa
- pms
- pl
- pt
- pa
- ro
- ru
- sco
- sr
- hr
- scn
- sk
- sl
- aze
- es
- su
- sw
- sv
- tl
- tg
- th
- ta
- tt
- te
- tr
- uk
- ud
- uz
- vi
- vo
- war
- cy
- fry
- pnb
- yo
license: apache-2.0
datasets:
- wikipedia
---

# Model Card for DistilBERT base multilingual (cased)

# Table of Contents

1. [Model Details](#model-details)
2. [Uses](#uses)
3. [Bias, Risks, and Limitations](#bias-risks-and-limitations)
4. [Training Details](#training-details)
5. [Evaluation](#evaluation)
6. [Environmental Impact](#environmental-impact)
7. [Citation](#citation)
8. [How To Get Started With the Model](#how-to-get-started-with-the-model)

# Model Details

## Model Description

This model is a distilled version of the [BERT base multilingual model](https://huggingface.co/bert-base-multilingual-cased/). The code for the distillation process can be found [here](https://github.com/huggingface/transformers/tree/main/examples/research_projects/distillation). This model is cased: it does make a difference between english and English.

The model is trained on the concatenation of Wikipedia in 104 different languages listed [here](https://github.com/google-research/bert/blob/master/multilingual.md#list-of-languages).
The model has 6 layers, 768 dimension and 12 heads, totalizing 134M parameters (compared to 177M parameters for mBERT-base).
On average, this model, referred to as DistilmBERT, is twice as fast as mBERT-base.

We encourage potential users of this model to check out the [BERT base multilingual model card](https://huggingface.co/bert-base-multilingual-cased) to learn more about usage, limitations and potential biases.

- **Developed by:** Victor Sanh, Lysandre Debut, Julien Chaumond, Thomas Wolf (Hugging Face)
- **Model type:** Transformer-based language model
- **Language(s) (NLP):** 104 languages; see full list [here](https://github.com/google-research/bert/blob/master/multilingual.md#list-of-languages)
- **License:** Apache 2.0
- **Related Models:** [BERT base multilingual model](https://huggingface.co/bert-base-multilingual-cased)
- **Resources for more information:** 
  - [GitHub Repository](https://github.com/huggingface/transformers/blob/main/examples/research_projects/distillation/README.md)
  - [Associated Paper](https://arxiv.org/abs/1910.01108)

# Uses

## Direct Use and Downstream Use

You can use the raw model for either masked language modeling or next sentence prediction, but it's mostly intended to be fine-tuned on a downstream task. See the [model hub](https://huggingface.co/models?filter=bert) to look for fine-tuned versions on a task that interests you.

Note that this model is primarily aimed at being fine-tuned on tasks that use the whole sentence (potentially masked) to make decisions, such as sequence classification, token classification or question answering. For tasks such as text generation you should look at model like GPT2.

## Out of Scope Use

The model should not be used to intentionally create hostile or alienating environments for people. The model was not trained to be factual or true representations of people or events, and therefore using the models to generate such content is out-of-scope for the abilities of this model.

# Bias, Risks, and Limitations

Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf) and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)). Predictions generated by the model may include disturbing and harmful stereotypes across protected classes; identity characteristics; and sensitive, social, and occupational groups.

## Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model.

# Training Details

- The model was pretrained with the supervision of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the concatenation of Wikipedia in 104 different languages
- The model has 6 layers, 768 dimension and 12 heads, totalizing 134M parameters.
- Further information about the training procedure and data is included in the [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) model card.

# Evaluation

The model developers report the following accuracy results for DistilmBERT (see [GitHub Repo](https://github.com/huggingface/transformers/blob/main/examples/research_projects/distillation/README.md)): 

> Here are the results on the test sets for 6 of the languages available in XNLI. The results are computed in the zero shot setting (trained on the English portion and evaluated on the target language portion):

| Model                        | English | Spanish | Chinese | German | Arabic  | Urdu |
| :---:                        | :---:   | :---:   | :---:   | :---:  | :---:   | :---:|
| mBERT base cased (computed)  | 82.1    | 74.6    | 69.1    | 72.3   | 66.4    | 58.5 |
| mBERT base uncased (reported)| 81.4    | 74.3    | 63.8    | 70.5   | 62.1    | 58.3 |
| DistilmBERT                  | 78.2    | 69.1    | 64.0    | 66.3   | 59.1    | 54.7 |

# Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** More information needed
- **Hours used:** More information needed
- **Cloud Provider:** More information needed
- **Compute Region:** More information needed
- **Carbon Emitted:** More information needed

# Citation

```bibtex
@article{Sanh2019DistilBERTAD,
  title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author={Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},
  journal={ArXiv},
  year={2019},
  volume={abs/1910.01108}
}
```

APA
- Sanh, V., Debut, L., Chaumond, J., & Wolf, T. (2019). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. arXiv preprint arXiv:1910.01108.

# How to Get Started With the Model

You can use the model directly with a pipeline for masked language modeling: 

```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='distilbert-base-multilingual-cased')
>>> unmasker("Hello I'm a [MASK] model.")

[{'score': 0.040800247341394424,
  'sequence': "Hello I'm a virtual model.",
  'token': 37859,
  'token_str': 'virtual'},
 {'score': 0.020015988498926163,
  'sequence': "Hello I'm a big model.",
  'token': 22185,
  'token_str': 'big'},
 {'score': 0.018680453300476074,
  'sequence': "Hello I'm a Hello model.",
  'token': 31178,
  'token_str': 'Hello'},
 {'score': 0.017396586015820503,
  'sequence': "Hello I'm a model model.",
  'token': 13192,
  'token_str': 'model'},
 {'score': 0.014229810796678066,
  'sequence': "Hello I'm a perfect model.",
  'token': 43477,
  'token_str': 'perfect'}]
```