---
language: 
- multilingual
- en
- fr
- es
- de
- el
- bg
- ru
- tr
- ar
- vi
- th
- zh
- hi
- sw
- ur
tags:
- text-classification
- pytorch
- tensorflow
datasets:
- multi_nli
- xnli
license: mit
pipeline_tag: zero-shot-classification
widget:
- text: "За кого вы голосуете в 2020 году?"
  candidate_labels: "politique étrangère, Europe, élections, affaires, politique"
  multi_class: true
- text: "لمن تصوت في 2020؟"
  candidate_labels: "السياسة الخارجية, أوروبا, الانتخابات, الأعمال, السياسة"
  multi_class: true
- text: "2020'de kime oy vereceksiniz?"
  candidate_labels: "dış politika, Avrupa, seçimler, ticaret, siyaset"
  multi_class: true
---

# xlm-roberta-large-xnli

## Model Description

This model takes [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) and fine-tunes it on a combination of NLI data in 15 languages. It is intended to be used for zero-shot text classification, such as with the Hugging Face [ZeroShotClassificationPipeline](https://huggingface.co/transformers/master/main_classes/pipelines.html#transformers.ZeroShotClassificationPipeline).

## Intended Usage

This model is intended to be used for zero-shot text classification, especially in languages other than English. It is fine-tuned on XNLI, which is a multilingual NLI dataset. The model can therefore be used with any of the languages in the XNLI corpus:

- English
- French
- Spanish
- German
- Greek
- Bulgarian
- Russian
- Turkish
- Arabic
- Vietnamese
- Thai
- Chinese
- Hindi
- Swahili
- Urdu

Since the base model was pre-trained trained on 100 different languages, the
model has shown some effectiveness in languages beyond those listed above as
well. See the full list of pre-trained languages in appendix A of the
[XLM Roberata paper](https://arxiv.org/abs/1911.02116)

For English-only classification, it is recommended to use
[bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli) or
[a distilled bart MNLI model](https://huggingface.co/models?filter=pipeline_tag%3Azero-shot-classification&search=valhalla).

#### With the zero-shot classification pipeline

The model can be loaded with the `zero-shot-classification` pipeline like so:

```python
from transformers import pipeline
classifier = pipeline("zero-shot-classification",
                      model="joeddav/xlm-roberta-large-xnli")
```

You can then classify in any of the above languages. You can even pass the labels in one language and the sequence to
classify in another:

```python
# we will classify the Russian translation of, "Who are you voting for in 2020?"
sequence_to_classify = "За кого вы голосуете в 2020 году?"
# we can specify candidate labels in Russian or any other language above:
candidate_labels = ["Europe", "public health", "politics"]
classifier(sequence_to_classify, candidate_labels)
# {'labels': ['politics', 'Europe', 'public health'],
#  'scores': [0.9048484563827515, 0.05722189322113991, 0.03792969882488251],
#  'sequence': 'За кого вы голосуете в 2020 году?'}
```

The default hypothesis template is the English, `This text is {}`. If you are working strictly within one language, it
may be worthwhile to translate this to the language you are working with:

```python
sequence_to_classify = "¿A quién vas a votar en 2020?"
candidate_labels = ["Europa", "salud pública", "política"]
hypothesis_template = "Este ejemplo es {}."
classifier(sequence_to_classify, candidate_labels, hypothesis_template=hypothesis_template)
# {'labels': ['política', 'Europa', 'salud pública'],
#  'scores': [0.9109585881233215, 0.05954807624220848, 0.029493311420083046],
#  'sequence': '¿A quién vas a votar en 2020?'}
```

#### With manual PyTorch

```python
# pose sequence as a NLI premise and label as a hypothesis
from transformers import AutoModelForSequenceClassification, AutoTokenizer
nli_model = AutoModelForSequenceClassification.from_pretrained('joeddav/xlm-roberta-large-xnli')
tokenizer = AutoTokenizer.from_pretrained('joeddav/xlm-roberta-large-xnli')

premise = sequence
hypothesis = f'This example is {label}.'

# run through model pre-trained on MNLI
x = tokenizer.encode(premise, hypothesis, return_tensors='pt',
                     truncation_strategy='only_first')
logits = nli_model(x.to(device))[0]

# we throw away "neutral" (dim 1) and take the probability of
# "entailment" (2) as the probability of the label being true 
entail_contradiction_logits = logits[:,[0,2]]
probs = entail_contradiction_logits.softmax(dim=1)
prob_label_is_true = probs[:,1]
```

## Training

This model was pre-trained on set of 100 languages, as described in
[the original paper](https://arxiv.org/abs/1911.02116). It was then fine-tuned on the task of NLI on the concatenated
MNLI train set and the XNLI validation and test sets. Finally, it was trained for one additional epoch on only XNLI
data where the translations for the premise and hypothesis are shuffled such that the premise and hypothesis for
each example come from the same original English example but the premise and hypothesis are of different languages.
