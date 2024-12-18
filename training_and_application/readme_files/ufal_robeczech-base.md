
---
language: cs
license: cc-by-nc-sa-4.0
tags:
- RobeCzech
- Czech
- RoBERTa
- ÚFAL
---

# Model Card for RobeCzech

## Version History

- **version 1.1**: Version 1.1 was released in Jan 2024, with a change to the
  tokenizer described below; the model parameters were mostly kept the same, but
  (a) the embeddings were enlarged (by copying suitable rows) to correspond to
  the updated tokenizer, (b) the pooler was dropped (originally it was only
  randomly initialized).

  The tokenizer in the initial release (a) contained a hole (51959 did not
  correspond to any token), and (b) mapped several tokens (unseen during training
  but required by the BBPE tokenizer) to the same ID as the `[UNK]` token (3).
  That sometimes caused problems, as in https://huggingface.co/ufal/robeczech-base/discussions/4.
  See https://huggingface.co/ufal/robeczech-base/discussions/4#64b8f6a7f1f8e6ea5860b314
  for more information.

  In version 1.1, the tokenizer was modified by (a) removing the hole, (b)
  mapping all tokens to a unique ID. That also required increasing the
  vocabulary size and embeddings weights (by replicating the embedding of the
  `[UNK]` token). Without finetuning, version 1.1 and version 1.0 gives exactly
  the same embeddings on any input (apart from the pooler missing in v1.1),
  and the tokens in version 1.0 that mapped to a different ID than the `[UNK]`
  token map to the same ID in version 1.1.

  However, the sizes of the embeddings (and LM head weights and biases) are
  different, so the weights of the version 1.1 are not compatible with the
  configuration of version 1.0 and vice versa.

- **version 1.0**: Initial version released in May 2021 (with the tokenization
  issues described above).

  If you want to load a pretrained model, configuration, or a tokenizer of
  version 1.0, you can use
  ```python
  from_pretrained("ufal/robeczech-base", revision="v1.0")
  ```
  to create an `AutoModel`, an `AutoConfig`, or an `AutoTokenizer`.

# Model Details

## Model Description

RobeCzech is a monolingual RoBERTa language representation model trained on Czech data.

- **Developed by:** Institute of Formal and Applied Linguistics, Charles University, Prague (UFAL)
- **Shared by:** Hugging Face and [LINDAT/CLARIAH-CZ](https://hdl.handle.net/11234/1-3691)
- **Model type:** Fill-Mask
- **Language(s) (NLP):** cs
- **License:** cc-by-nc-sa-4.0
- **Model Architecture:** RoBERTa
- **Resources for more information:**
  - [RobeCzech: Czech RoBERTa, a Monolingual Contextualized Language Representation Model](https://doi.org/10.1007/978-3-030-83527-9_17)
    - [arXiv preprint is also available](https://arxiv.org/abs/2105.11314)


# Uses

## Direct Use

Fill-Mask tasks.

## Downstream Use

Morphological tagging and lemmatization, dependency parsing, named entity
recognition, and semantic parsing.


# Bias, Risks, and Limitations

Significant research has explored bias and fairness issues with language models
(see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf)
and [Bender et al. (2021)](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)).
Predictions generated by the model may include disturbing and harmful
stereotypes across protected classes; identity characteristics; and sensitive,
social, and occupational groups.

## Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and
limitations of the model. More information needed for further recommendations.


# Training Details

## Training Data

The model creators note in the [associated paper](https://arxiv.org/pdf/2105.11314.pdf):
> We trained RobeCzech on a collection of the following publicly available texts:
> - SYN v4, a large corpus of contemporary written Czech, 4,188M tokens;
> - Czes, a collection of Czech newspaper and magazine articles, 432M tokens;
> - documents with at least 400 tokens from the Czech part of the web corpus.W2C , tokenized with MorphoDiTa, 16M tokens;
> - plain texts extracted from Czech Wikipedia dump 20201020 using WikiEx-tractor, tokenized with MorphoDiTa, 123M tokens

> All these corpora contain whole documents, even if the SYN v4 is
> block-shuffled (blocks with at most 100 words respecting sentence boundaries
> are permuted in a document) and in total contain 4,917M tokens.

## Training Procedure

### Preprocessing

The texts are tokenized into subwords with a byte-level BPE (BBPE) tokenizer,
which was trained on the entire corpus and we limit its vocabulary size to
52,000 items.

### Speeds, Sizes, Times
The model creators note in the [associated paper](https://arxiv.org/pdf/2105.11314.pdf):
> The training batch size is 8,192 and each training batch consists of sentences
> sampled contiguously, even across document boundaries, such that the total
> length of each sample is at most 512 tokens (FULL-SENTENCES setting). We use
> Adam optimizer with β1 = 0.9 and β2 = 0.98 to minimize the masked
> language-modeling objective.

### Software Used
The [Fairseq](https://github.com/facebookresearch/fairseq/tree/main/examples/roberta)
implementation was used for training.


# Evaluation

## Testing Data, Factors & Metrics

### Testing Data
The model creators note in the [associated paper](https://arxiv.org/pdf/2105.11314.pdf):
> We evaluate RobeCzech in five NLP tasks, three of them leveraging frozen
> contextualized word embeddings, two approached with fine-tuning:
> - morphological analysis and lemmatization: frozen contextualized word embeddings,
> - dependency parsing: frozen contextualized word embeddings,
> - named entity recognition: frozen contextualized word embeddings,
> - semantic parsing: fine-tuned,
> - sentiment analysis: fine-tuned.

## Results

| Model     | Morphosynt PDT3.5   (POS) (LAS) | Morphosynt UD2.3  (XPOS) (LAS) | NER CNEC1.1  (nested) (flat) | Semant. PTG  (Avg) (F1) |
|-----------|---------------------------------|--------------------------------|------------------------------|-------------------------|
| RobeCzech | 98.50      91.42                | 98.31    93.77                 | 87.82	           87.47        | 92.36           80.13   |


# Environmental Impact

- **Hardware Type:** 8 QUADRO P5000 GPU
- **Hours used:** 2190 (~3 months)


# Citation

```
@InProceedings{10.1007/978-3-030-83527-9_17,
  author={Straka, Milan and N{\'a}plava, Jakub and Strakov{\'a}, Jana and Samuel, David},
  editor={Ek{\v{s}}tein, Kamil and P{\'a}rtl, Franti{\v{s}}ek and Konop{\'i}k, Miloslav},
  title={{RobeCzech: Czech RoBERTa, a Monolingual Contextualized Language Representation Model}},
  booktitle="Text, Speech, and Dialogue",
  year="2021",
  publisher="Springer International Publishing",
  address="Cham",
  pages="197--209",
  isbn="978-3-030-83527-9"
}
```


# How to Get Started with the Model

Use the code below to get started with the model.

<details>
<summary> Click to expand </summary>

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("ufal/robeczech-base")

model = AutoModelForMaskedLM.from_pretrained("ufal/robeczech-base")
 ```
</details>
