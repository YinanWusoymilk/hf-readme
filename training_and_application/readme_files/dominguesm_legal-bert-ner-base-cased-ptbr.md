---
thumbnail: "https://i.imgur.com/tpI1iT5.jpg"
license: cc-by-4.0
language: 
- pt
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: checkpoints
  results:
  - task:
      name: Token Classification
      type: token-classification
    metrics:
    - name: F1
      type: f1
      value: 0.9525622169191057
    - name: Precision
      type: precision
      value: 0.9438680702115613
    - name: Recall
      type: recall
      value: 0.961418019517758
    - name: Accuracy
      type: accuracy
      value: 0.9894253721279602
    - name: Loss
      type: loss
      value: 0.030161771923303604
widget:
- text: "Ao Instituto Médico Legal da jurisdição do acidente ou da residência cumpre fornecer, no prazo de 90 dias, laudo à vítima (art. 5, § 5, Lei n. 6.194/74  de 19 de dezembro de 1974), função técnica que pode ser suprida por prova pericial realizada por ordem do juízo da causa, ou por prova técnica realizada no âmbito administrativo que se mostre coerente com os demais elementos de prova constante dos autos."
- text: "Acrescento que não há de se falar em violação do artigo 114, § 3º, da Constituição Federal, posto que referido dispositivo revela-se impertinente, tratando da possibilidade de ajuizamento de dissídio coletivo pelo Ministério Público do Trabalho nos casos de greve em atividade essencial."
- text: "Dispõe sobre o estágio de estudantes; altera a redação do art. 428 da Consolidação das Leis do Trabalho – CLT, aprovada pelo Decreto-Lei no 5.452, de 1o de maio de 1943, e a Lei no 9.394, de 20 de dezembro de 1996; revoga as Leis nos 6.494, de 7 de dezembro de 1977, e 8.859, de 23 de março de 1994, o parágrafo único do art. 82 da Lei no 9.394, de 20 de dezembro de 1996, e o art. 6o da Medida Provisória  no 2.164-41, de 24 de agosto de 2001; e dá outras providências."
---

## (BERT base) NER model in the legal domain in Portuguese

**README under construction**

**ner-legal-bert-base-cased-ptbr** is a NER model (token classification) in the legal domain in Portuguese that was finetuned from the model [dominguesm/legal-bert-base-cased-ptbr](https://huggingface.co/dominguesm/legal-bert-base-cased-ptbr) by using a NER objective.

The model is intended to assist NLP research in the legal field, computer law and legal technology applications. Several legal texts in Portuguese (more information below) were used with the following labels: 

* `PESSOA`
* `ORGANIZACAO`
* `LOCAL`
* `TEMPO`
* `LEGISLACAO`
* `JURISPRUDENCIA`

The labels were inspired by the [LeNER_br](https://huggingface.co/datasets/lener_br) dataset.
## Training Dataset


The dataset of **ner-legal-bert-base-cased-ptbr** include:

* 971932 examples of miscellaneous legal documents (train split) 
* 53996 examples of miscellaneous legal documents (valid split) 
* 53997 examples of miscellaneous legal documents (test split) 

The data used was provided by the BRAZILIAN SUPREME FEDERAL TRIBUNAL, through the terms of use: [LREC 2020](https://ailab.unb.br/victor/lrec2020). 

The results of this project do not imply in any way the position of the BRAZILIAN SUPREME FEDERAL TRIBUNAL, all being the sole and exclusive responsibility of the author of the model.

## Using the model for inference in production

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

# parameters
model_name = "dominguesm/ner-legal-bert-base-cased-ptbr"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

input_text = "Acrescento que não há de se falar em violação do artigo 114, § 3º, da Constituição Federal, posto que referido dispositivo revela-se impertinente, tratando da possibilidade de ajuizamento de dissídio coletivo pelo Ministério Público do Trabalho nos casos de greve em atividade essencial."

# tokenization
inputs = tokenizer(input_text, max_length=512, truncation=True, return_tensors="pt")
tokens = inputs.tokens()

# get predictions
outputs = model(**inputs).logits
predictions = torch.argmax(outputs, dim=2)

# print predictions
for token, prediction in zip(tokens, predictions[0].numpy()):
    print((token, model.config.id2label[prediction]))
```

You can use pipeline, too. However, it seems to have an issue regarding to the max_length of the input sequence.

```python
from transformers import pipeline

model_name = "dominguesm/ner-legal-bert-base-cased-ptbr"

ner = pipeline(
    "ner",
    model=model_name
) 

ner(input_text, aggregation_strategy="average")
```

## Training procedure

### Hyperparameters

#### batch, learning rate...
- per_device_batch_size = 64
- gradient_accumulation_steps = 2
- learning_rate = 2e-5 
- num_train_epochs = 3
- weight_decay = 0.01
- optimizer = torch.optim.AdamW
- epsilon = 1e-08
- lr_scheduler_type = linear

#### save model & load best model
- save_total_limit = 3
- logging_steps = 1000
- eval_steps = logging_steps
- evaluation_strategy = 'steps'
- logging_strategy = 'steps'
- save_strategy = 'steps'
- save_steps = logging_steps
- load_best_model_at_end = True
- fp16 = True

### Training results

```
Num examples = 971932
Num Epochs = 3
Instantaneous batch size per device = 64
Total train batch size (w. parallel, distributed & accumulation) = 128
Gradient Accumulation steps = 2
Total optimization steps = 22779
Evaluation Infos:
  Num examples = 53996
  Batch size = 128
```

| Step | Training Loss | Validation Loss | Precision | Recall | F1 Accuracy |
| ---- | ------------- | --------------- | --------- | ------ | ----------- |
|1000  |0.113900 | 	0.057008 |	0.898600| 	0.938444| 	0.918090| 	0.980961|
|2000 	|0.052800 |	0.048254 |	0.917243 |	0.941188 |	0.929062 |	0.983854|
|3000 	|0.046200 |	0.043833 |	0.919706 |	0.948411 |	0.933838 |	0.984931|
|4000 	|0.043500 |	0.039796 |	0.928439 |	0.947058 |	0.937656 |	0.985891|
|5000 	|0.041400 |	0.039421 |	0.926103 |	0.952857 |	0.939290 |	0.986130|
|6000 	|0.039700 |	0.038599 |	0.922376 |	0.956257 |	0.939011 |	0.986093|
|7000 	|0.037800 |	0.036463 |	0.935125 |	0.950937 |	0.942964 |	0.987030|
|8000 	|0.035900 |	0.035706 |	0.934638 |	0.954147 |	0.944292 |	0.987433|
|9000 	|0.033800 |	0.034518 |	0.940354 |	0.951991 |	0.946136 |	0.987866|
|10000 	|0.033600 |	0.033454 |	0.938170 |	0.956097 |	0.947049 |	0.988066|
|11000 	|0.032700 |	0.032899 |	0.934130 |	0.959491 |	0.946641 |	0.988092|
|12000 	|0.032200 |	0.032477 |	0.937400 |	0.959150 |	0.948151 |	0.988305|
|13000 	|0.031200 |	0.033207 |	0.937058 |	0.960506 |	0.948637 |	0.988340|
|14000 	|0.031400 |	0.031711 |	0.938765 |	0.959711 |	0.949123 |	0.988635|
|15000 	|0.030600 |	0.031519 |	0.940488 |	0.959413 |	0.949856 |	0.988709|
|16000 	|0.028500 |	0.031618 |	0.943643 |	0.957693 |	0.950616 |	|0.988891|
|17000 	|0.028000 |	0.031106 |	0.941109 |	0.960687 |	0.950797 |	|0.989016|
|18000 	|0.027800 |	0.030712 |	0.942821 |	0.960528 |	0.951592 |	|0.989198|
|19000 	|0.027500 |	0.030523 |	0.942950 |	0.960947 |	0.951864 |	|0.989348|
|20000 	|0.027400 |	0.030577 |	0.942462 |	0.961754 |	0.952010 |	|0.989295|
|21000 	|0.027000 |	0.030025 |	0.944483 |	0.960497 |	0.952422 |	|0.989445|
|22000 	|0.026800 |	0.030162 |	0.943868 |	0.961418 |	0.952562 |	|0.989425|


 ### Validation metrics by Named Entity (Test Dataset)


* **Num examples = 53997**
* `overall_precision`: 0.9432396865925381
* `overall_recall`: 0.9614334116769161
* `overall_f1`: 0.9522496545298874
* `overall_accuracy`': 0.9894741602608071

| Label | Precision | Recall | F1 Accuracy | Entity Examples |
| ----- | --------- | ------ | ----------- | --------------- |
| JURISPRUDENCIA| 0.8795197115548148| 0.9037275221501844 | 0.8914593047810311 | 57223 |
| LEGISLACAO | 0.9405395935529082 | 0.9514071028567378 | 0.9459421362370934 | 84642 |
| LOCAL | 0.9011495452253004 | 0.9132358124779697 | 0.9071524233856495 | 56740 |
| ORGANIZACAO | 0.9239028155165304 | 0.954964947845235 | 0.9391771163875446 | 183013 |
| PESSOA | 0.9651685220572037 | 0.9738545198908279 | 0.9694920661875761 | 193456 |
| TEMPO | 0.973704616066295 | 0.9918808401799004 | 0.9827086882453152 | 186103 |

## Notes

* For the production of this `readme`, i used the `readme` written by Pierre Guillou (available [here](https://huggingface.co/pierreguillou/ner-bert-large-cased-pt-lenerbr)) as a basis, reproducing some parts entirely.