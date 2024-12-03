---
language:
- it
pipeline_tag: token-classification
library_name: gliner
license: apache-2.0
datasets:
- DeepMount00/GLINER_ITA
---

# Universal NER for Italian (Zero-Shot)
It's important to note that **this model is universal and operates across all domains**. However, if you are seeking performance metrics close to a 90/99% F1 score for a specific domain, you are encouraged to reach out via email to Michele Montebovi at montebovi.michele@gmail.com. This direct contact allows for the possibility of customizing the model to achieve enhanced performance tailored to your unique entity recognition requirements in the Italian language.

## Try here: [https://huggingface.co/spaces/DeepMount00/universal_ner_ita](https://huggingface.co/spaces/DeepMount00/universal_ner_ita)

## Model Description
This model is designed for Named Entity Recognition (NER) tasks, specifically tailored for the Italian language. It employs a zero-shot learning approach, enabling it to identify a wide range of entities without the need for specific training on those entities. This makes it incredibly versatile for various applications requiring entity extraction from Italian text.

## Model Performance
- **Inference Time:** The model runs on CPUs, with an inference time of 0.01 seconds on a GPU. Performance on a CPU will vary depending on the specific hardware configuration.

## Try It Out
You can test the model directly in your browser through the following Hugging Face Spaces link: [https://huggingface.co/spaces/DeepMount00/universal_ner_ita](https://huggingface.co/spaces/DeepMount00/universal_ner_ita).

# Installation
To use this model, you must download the GLiNER project:

```
!pip install gliner
```

# Usage

```python
from gliner import GLiNER

model = GLiNER.from_pretrained("DeepMount00/universal_ner_ita")

text = """
Il comune di Castelrosso, con codice fiscale 80012345678, ha approvato il finanziamento di 15.000€ destinati alla ristrutturazione del parco giochi cittadino, affidando l'incarico alla società 'Verde Vivo Società Cooperativa', con sede legale in Corso della Libertà 45, Verona, da completarsi entro il 30/09/2024.
"""

labels = ["comune", "codice fiscale", "importo", "società", "indirizzo", "data di completamento"]

entities = model.predict_entities(text, labels)

max_length = max(len(entity["text"]) for entity in entities)

for entity in entities:
    padded_text = entity["text"].ljust(max_length)
    print(f"{padded_text} => {entity['label']}")
```