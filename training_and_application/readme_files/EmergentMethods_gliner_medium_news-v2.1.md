---
license: apache-2.0
datasets:
- EmergentMethods/AskNews-NER-v0
tags:
- gliner
language:
- en
pipeline_tag: token-classification
---
# Model Card for gliner_medium_news-v2.1

This model is a fine-tune of [GLiNER](https://huggingface.co/urchade/gliner_medium-v2.1) aimed at improving accuracy across a broad range of topics, especially with respect to long-context news entity extraction. As shown in the table below, these fine-tunes improved upon the base GLiNER model zero-shot accuracy by up to 7.5% across 18 benchmark datasets.

![results table](assets/zero-shot_18_table.png)

The underlying dataset, [AskNews-NER-v0](https://huggingface.co/datasets/EmergentMethods/AskNews-NER-v0) was engineered with the objective of diversifying global perspectives by enforcing country/language/topic/temporal diversity. All data used to fine-tune this model was synthetically generated. WizardLM 13B v1.2 was used for translation/summarization of open-web news articles, while Llama3 70b instruct was used for entity extraction. Both the diversification and fine-tuning methods are presented in a our paper on [ArXiv](https://arxiv.org/abs/2406.10258).

# Usage

```python
from gliner import GLiNER

model = GLiNER.from_pretrained("EmergentMethods/gliner_medium_news-v2.1")

text = """
The Chihuahua State Public Security Secretariat (SSPE) arrested 35-year-old Salomón C. T. in Ciudad Juárez, found in possession of a stolen vehicle, a white GMC Yukon, which was reported stolen in the city's streets. The arrest was made by intelligence and police analysis personnel during an investigation in the border city. The arrest is related to a previous detention on February 6, which involved armed men in a private vehicle. The detainee and the vehicle were turned over to the Chihuahua State Attorney General's Office for further investigation into the case. 
"""

labels = ["person", "location", "date", "event", "facility", "vehicle", "number", "organization"]

entities = model.predict_entities(text, labels)

for entity in entities:
    print(entity["text"], "=>", entity["label"])
```

Output:

```
Chihuahua State Public Security Secretariat => organization
SSPE => organization
35-year-old => number
Salomón C. T. => person
Ciudad Juárez => location
GMC Yukon => vehicle
February 6 => date
Chihuahua State Attorney General's Office => organization
```

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

The synthetic data underlying this news fine-tune was pulled from the [AskNews API](https://docs.asknews.app). We enforced diveristy across country/language/topic/time.

Countries:

![country distribution](assets/countries_distribution.png)

Entity types:

![entities](assets/entity-types_limited.png)

Topics:

![topics](assets/topics_fig_connected.png)


- **Developed by:** [Emergent Methods](https://emergentmethods.ai/)
- **Funded by:** [Emergent Methods](https://emergentmethods.ai/)
- **Shared by:** [Emergent Methods](https://emergentmethods.ai/)
- **Model type:** microsoft/deberta
- **Language(s) (NLP):** English (en) (English texts and translations from Spanish (es), Portuguese (pt), German (de), Russian (ru), French (fr), Arabic (ar), Italian (it), Ukrainian (uk), Norwegian (no), Swedish (sv), Danish (da)).
- **License:** Apache 2.0
- **Finetuned from model:** [GLiNER](https://huggingface.co/urchade/gliner_medium-v2.1)

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** To be added
- **Paper:** To be added
- **Demo:** To be added

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

As the name suggests, this model is aimed at generalist entity extraction. Although we used news to fine-tune this model, it improved accuracy across 18 benchmark datasets by up to 7.5%. This means that the broad and diversified underlying dataset has helped it to recognize and extract more entity types.

This model is shockingly compact, and can be used for high-throughput production usecases. This is another reason we have licensed this as Apache 2.0. Currently, [AskNews](https://asknews.app) is using this fine-tune for entity extraction in their system.


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

Although the goal of the dataset is to reduce bias, and improve diversity, it is still biased to western languages and countries. This limitation originates from the abilities of Llama2 for the translation and summary generations. Further, any bias originating in Llama2 training data will also be present in this dataset, since Llama2 was used to summarize the open-web articles. Further, any biases present in Llama3 will be present in the present dataaset since Llama3 was used to extract entities from the summaries.

![countries distribution](figures/topics_fig_connected.png)


## How to Get Started with the Model

Use the code below to get started with the model.



## Training Details

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

The training dataset is [AskNews-NER-v0](https://huggingface.co/datasets/EmergentMethods/AskNews-NER-v0).

Other training details can be found in the [companion paper](https://linktoarxiv.org).



## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

- **Hardware Type:** 1xA4500
- **Hours used:** 10
- **Carbon Emitted:** 0.6 kg (According to [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute))


## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

To be added

**APA:**

To be added

## Model Authors

Elin Törnquist, Emergent Methods elin at emergentmethods.ai
Robert Caulk, Emergent Methods rob at emergentmethods.ai


## Model Contact

Elin Törnquist, Emergent Methods elin at emergentmethods.ai
Robert Caulk, Emergent Methods rob at emergentmethods.ai