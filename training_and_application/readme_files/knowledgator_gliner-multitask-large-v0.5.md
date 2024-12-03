---
license: apache-2.0
language:
- en
metrics:
- f1
- precision
- recall
tags:
- NER
- information extraction
- relation extraction
- summarization
- sentiment extraction
- question-answering
pipeline_tag: token-classification
library_name: gliner
datasets:
- knowledgator/GLINER-multi-task-synthetic-data
---
🚀 Meet the first multi-task prompt-tunable GLiNER model 🚀

**GLiNER-Multitask** is a model designed to extract various pieces of information from plain text based on a user-provided custom prompt. This versatile model leverages a bidirectional transformer encoder, similar to BERT, which ensures both high generalization and compute efficiency despite its compact size.

The `gliner-multitask-large` variant achieves state-of-the-art performance on NER zero-shot benchmarks, demonstrating its robustness and flexibility. It excels not only in named entity recognition but also in handling various other information extraction tasks, making it a powerful tool for diverse natural language processing applications.

### Supported tasks:
* **Named Entity Recognition (NER)**: Identifies and categorizes entities such as names, organizations, dates, and other specific items in the text.
* **Relation Extraction**: Detects and classifies relationships between entities within the text.
* **Summarization**: Extract the most important sentences that summarize the input text, capturing the essential information.
* **Sentiment Extraction**: Identify parts of the text that signalize a positive, negative, or neutral sentiment;
* **Key-Phrase Extraction**: Identifies and extracts important phrases and keywords from the text.
* **Question-answering**: Finding an answer in the text given a question;
* **Open Information Extraction**: Extracts pieces of text given an open prompt from a user, for example, product description extraction;


### Installation 	
To use this model, you must install the [GLiNER Python library](https://github.com/urchade/GLiNER):

```bash
pip install gliner
```

Once you've downloaded the GLiNER library, you can import the GLiNER class. You can then load this model using GLiNER.from_pretrained.

**How to use for NER:**

```python
from gliner import GLiNER

model = GLiNER.from_pretrained("knowledgator/gliner-multitask-large-v0.5")

text = """
Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975 to develop and sell BASIC interpreters for the Altair 8800. During his career at Microsoft, Gates held the positions of chairman, chief executive officer, president and chief software architect, while also being the largest individual shareholder until May 2014.
"""

labels = ["founder", "computer", "software", "position", "date"]

entities = model.predict_entities(text, labels)

for entity in entities:
    print(entity["text"], "=>", entity["label"])
```

**How to use for relation extraction:**

```python
text = """
Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975 to develop and sell BASIC interpreters for the Altair 8800. During his career at Microsoft, Gates held the positions of chairman, chief executive officer, president and chief software architect, while also being the largest individual shareholder until May 2014.
"""

labels = ["Microsoft <> founder", "Microsoft <> inception date", "Bill Gates <> held position"]

entities = model.predict_entities(text, labels)

for entity in entities:
    print(entity["label"], "=>", entity["text"])
```
### Construct relations extraction pipeline with [utca](https://github.com/Knowledgator/utca)
First of all, we need import neccessary components of the library and initalize predictor - GLiNER model and construct pipeline that combines NER and realtions extraction:
```python
from utca.core import RenameAttribute
from utca.implementation.predictors import (
    GLiNERPredictor,
    GLiNERPredictorConfig
)
from utca.implementation.tasks import (
    GLiNER,
    GLiNERPreprocessor,
    GLiNERRelationExtraction,
    GLiNERRelationExtractionPreprocessor,
)

predictor = GLiNERPredictor( # Predictor manages the model that will be used by tasks
    GLiNERPredictorConfig(
        model_name = "knowledgator/gliner-multitask-large-v0.5", # Model to use
        device = "cuda:0", # Device to use
    )
)

pipe = (
    GLiNER( # GLiNER task produces classified entities that will be at the "output" key.
        predictor=predictor,
        preprocess=GLiNERPreprocessor(threshold=0.7) # Entities threshold
    ) 
    | RenameAttribute("output", "entities") # Rename output entities from GLiNER task to use them as inputs in GLiNERRelationExtraction
    | GLiNERRelationExtraction( # GLiNERRelationExtraction is used for relation extraction.
        predictor=predictor,
        preprocess=(
            GLiNERPreprocessor(threshold=0.5) # Relations threshold
            | GLiNERRelationExtractionPreprocessor()
        )
    )
)
```

To run pipeline we need to specify entity types and relations with their parameters:

```python
r = pipe.run({
    "text": text, # Text to process
    "labels": ["organisation", "founder", "position", "date"],
    "relations": [{ # Relation parameters
        "relation": "founder", # Relation label. Required parameter.
        "pairs_filter": [("organisation", "founder")], # Optional parameter. It specifies possible members of relations by their entity labels.
        "distance_threshold": 100, # Optional parameter. It specifies the max distance between spans in the text (i.e., the end of the span that is closer to the start of the text and the start of the next one).
    }, {
        "relation": "inception date",
        "pairs_filter": [("organisation", "date")],
    }, {
        "relation": "held position",
        "pairs_filter": [("founder", "position")],
    }]
})

print(r["output"])
```

**How to use for open information extraction:**

```python
prompt = """Find all positive aspects about the product:\n"""
text = """
I recently purchased the Sony WH-1000XM4 Wireless Noise-Canceling Headphones from Amazon and I must say, I'm thoroughly impressed. The package arrived in New York within 2 days, thanks to Amazon Prime's expedited shipping.

The headphones themselves are remarkable. The noise-canceling feature works like a charm in the bustling city environment, and the 30-hour battery life means I don't have to charge them every day. Connecting them to my Samsung Galaxy S21 was a breeze, and the sound quality is second to none.

I also appreciated the customer service from Amazon when I had a question about the warranty. They responded within an hour and provided all the information I needed.

However, the headphones did not come with a hard case, which was listed in the product description. I contacted Amazon, and they offered a 10% discount on my next purchase as an apology.

Overall, I'd give these headphones a 4.5/5 rating and highly recommend them to anyone looking for top-notch quality in both product and service.
"""

input_ = prompt+text

labels = ["match"]

matches = model.predict_entities(input_, labels)

for match in matches:
    print(match["text"], "=>", match["score"])
```

**How to use for question-answering:**

```python
question = "Who was the CEO of Microsoft?"
text = """
Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975, to develop and sell BASIC interpreters for the Altair 8800. During his career at Microsoft, Gates held the positions of chairman, chief executive officer, president and chief software architect, while also being the largest individual shareholder until May 2014.
"""

labels = ["answer"]

input_ = question+text
answers = model.predict_entities(input_, labels)

for answer in answers:
    print(answer["text"], "=>", answer["score"])
```

**How to use for summarization:**

With threshold parameters, you can control how much information you want to extract.

```python
prompt = "Summarize the given text, highlighting the most important information:\n"

text = """
Several studies have reported its pharmacological activities, including anti-inflammatory, antimicrobial, and antitumoral effects.
The effect of E-anethole was studied in the osteosarcoma MG-63 cell line, and the antiproliferative activity was evaluated by an MTT assay.
It showed a GI50 value of 60.25 μM with apoptosis induction through the mitochondrial-mediated pathway. Additionally, it induced cell cycle arrest at the G0/G1 phase, up-regulated the expression of p53, caspase-3, and caspase-9, and down-regulated Bcl-xL expression.
Moreover, the antitumoral activity of anethole was assessed against oral tumor Ca9-22 cells, and the cytotoxic effects were evaluated by MTT and LDH assays.
It demonstrated a LD50 value of 8 μM, and cellular proliferation was 42.7% and 5.2% at anethole concentrations of 3 μM and 30 μM, respectively.
It was reported that it could selectively and in a dose-dependent manner decrease cell proliferation and induce apoptosis, as well as induce autophagy, decrease ROS production, and increase glutathione activity. The cytotoxic effect was mediated through NF-kB, MAP kinases, Wnt, caspase-3 and -9, and PARP1 pathways. Additionally, treatment with anethole inhibited cyclin D1 oncogene expression, increased cyclin-dependent kinase inhibitor p21WAF1, up-regulated p53 expression, and inhibited the EMT markers.
"""

labels = ["summary"]

input_ = prompt+text

threshold = 0.5
summaries = model.predict_entities(input_, labels, threshold=threshold)

for summary in summaries:
    print(summary["text"], "=>", summary["score"])
```

### Benchmarks:

![Model Performance](gliner_multitask_performance.png)

Our multitask model demonstrates comparable performance on different zero-shot benchmarks to dedicated models to NER task (all labels were lowecased in this testing):

| Model                              | Dataset            | Precision | Recall | F1 Score | F1 Score (Decimal) |
|------------------------------------|--------------------|-----------|--------|----------|--------------------|
| numind/NuNER_Zero-span             | CrossNER_AI        | 63.82%    | 56.82% | 60.12%   | 0.6012             |
|                                    | CrossNER_literature| 73.53%    | 58.06% | 64.89%   | 0.6489             |
|                                    | CrossNER_music     | 72.69%    | 67.40% | 69.95%   | 0.6995             |
|                                    | CrossNER_politics  | 77.28%    | 68.69% | 72.73%   | 0.7273             |
|                                    | CrossNER_science   | 70.08%    | 63.12% | 66.42%   | 0.6642             |
|                                    | mit-movie          | 63.00%    | 48.88% | 55.05%   | 0.5505             |
|                                    | mit-restaurant     | 54.81%    | 37.62% | 44.62%   | 0.4462             |
|                                    | **Average**        |           |        |          | **0.6196**         |
| knowledgator/gliner-multitask-v0.5 | CrossNER_AI         | 51.00%    | 51.11% | 51.05%   | 0.5105             |
|                                    | CrossNER_literature | 72.65%    | 65.62% | 68.96%   | 0.6896             |
|                                    | CrossNER_music      | 74.91%    | 73.70% | 74.30%   | 0.7430             |
|                                    | CrossNER_politics   | 78.84%    | 77.71% | 78.27%   | 0.7827             |
|                                    | CrossNER_science    | 69.20%    | 65.48% | 67.29%   | 0.6729             |
|                                    | mit-movie           | 61.29%    | 52.59% | 56.60%   | 0.5660             |
|                                    | mit-restaurant      | 50.65%    | 38.13% | 43.51%   | 0.4351             |
|                                    | **Average**        |           |        |          | **0.6276**         |
| urchade/gliner_large-v2.1          | CrossNER_AI        | 54.98%    | 52.00% | 53.45%   | 0.5345             |
|                                    | CrossNER_literature| 59.33%    | 56.47% | 57.87%   | 0.5787             |
|                                    | CrossNER_music     | 67.39%    | 66.77% | 67.08%   | 0.6708             |
|                                    | CrossNER_politics  | 66.07%    | 63.76% | 64.90%   | 0.6490             |
|                                    | CrossNER_science   | 61.45%    | 62.56% | 62.00%   | 0.6200             |
|                                    | mit-movie          | 55.94%    | 47.36% | 51.29%   | 0.5129             |
|                                    | mit-restaurant     | 53.34%    | 40.83% | 46.25%   | 0.4625             |
|                                    | **Average**        |           |        |          | **0.5754**         |
| EmergentMethods/gliner_large_news-v2.1| CrossNER_AI    | 59.60%    | 54.55% | 56.96%   | 0.5696             |
|                                    | CrossNER_literature| 65.41%    | 56.16% | 60.44%   | 0.6044             |
|                                    | CrossNER_music     | 67.47%    | 63.08% | 65.20%   | 0.6520             |
|                                    | CrossNER_politics  | 66.05%    | 60.07% | 62.92%   | 0.6292             |
|                                    | CrossNER_science   | 68.44%    | 63.57% | 65.92%   | 0.6592             |
|                                    | mit-movie          | 65.85%    | 49.59% | 56.57%   | 0.5657             |
|                                    | mit-restaurant     | 54.71%    | 35.94% | 43.38%   | 0.4338             |
|                                    | **Average**        |           |        |          | **0.5876**         |


### Join Our Discord

Connect with our community on Discord for news, support, and discussion about our models. Join [Discord](https://discord.gg/dkyeAgs9DG).

### Citation:
```
@misc{stepanov2024gliner,
      title={GLiNER multi-task: Generalist Lightweight Model for Various Information Extraction Tasks}, 
      author={Ihor Stepanov and Mykhailo Shtopko},
      year={2024},
      eprint={2406.12925},
      archivePrefix={arXiv},
      primaryClass={id='cs.LG' full_name='Machine Learning' is_active=True alt_name=None in_archive='cs' is_general=False description='Papers on all aspects of machine learning research (supervised, unsupervised, reinforcement learning, bandit problems, and so on) including also robustness, explanation, fairness, and methodology. cs.LG is also an appropriate primary category for applications of machine learning methods.'}
}
```