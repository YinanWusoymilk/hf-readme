---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: KoELECTRA-small-v3-modu-ner
  results: []
language:
- ko
pipeline_tag: token-classification
widget:
- text: "서울역으로 안내해줘."
  example_title: "Example 1"
- text: "에어컨 온도 3도 올려줘."
  example_title: "Example 2"
- text: "아이유 노래 검색해줘."
  example_title: "Example 3"
---

# KoELECTRA-small-v3-modu-ner

This model is a fine-tuned version of [monologg/koelectra-small-v3-discriminator](https://huggingface.co/monologg/koelectra-small-v3-discriminator) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1431
- Precision: 0.8232
- Recall: 0.8449
- F1: 0.8339
- Accuracy: 0.9628

## Model description

태깅 시스템 : BIO 시스템
- B-(begin) : 개체명이 시작할 때
- I-(inside) : 토큰이 개체명 중간에 있을 때
- O(outside) : 토큰이 개체명이 아닐 경우

한국정보통신기술협회(TTA) 대분류 기준을 따르는 15 가지의 태그셋

| 분류          | 표기 | 정의        |
|:------------:|:---:|:-----------|
| ARTIFACTS    | AF  | 사람에 의해 창조된 인공물로 문화재, 건물, 악기, 도로, 무기, 운송수단, 작품명, 공산품명이 모두 이에 해당 |
| ANIMAL       | AM  | 사람을 제외한 짐승 |
| CIVILIZATION | CV  | 문명/문화 |
| DATE         | DT  | 기간 및 계절, 시기/시대 |
| EVENT        | EV  | 특정 사건/사고/행사 명칭 |
| STUDY_FIELD  | FD  | 학문 분야, 학파 및 유파 |
| LOCATION     | LC  | 지역/장소와 지형/지리 명칭 등을 모두 포함 |
| MATERIAL     | MT  | 원소 및 금속, 암석/보석, 화학물질 |
| ORGANIZATION | OG  | 기관 및 단체 명칭 |
| PERSON       | PS  | 인명 및 인물의 별칭 (유사 인물 명칭 포함) |
| PLANT        | PT  | 꽃/나무, 육지식물, 해초류, 버섯류, 이끼류 |
| QUANTITY     | QT  | 수량/분량, 순서/순차, 수사로 이루어진 표현 |
| TIME         | TI  | 시계상으로 나타나는 시/시각, 시간 범위 |
| TERM         | TM  | 타 개체명에서 정의된 세부 개체명 이외의 개체명 |
| THEORY       | TR  | 특정 이론, 법칙 원리 등 |

## Intended uses & limitations

### How to use
You can use this model with Transformers *pipeline* for NER.
```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("Leo97/KoELECTRA-small-v3-modu-ner")
model = AutoModelForTokenClassification.from_pretrained("Leo97/KoELECTRA-small-v3-modu-ner")
ner = pipeline("ner", model=model, tokenizer=tokenizer)

example = "서울역으로 안내해줘."
ner_results = ner(example)
print(ner_results)
```

## Training and evaluation data

개체명 인식(NER) 모델 학습 데이터 셋
- 문화체육관광부 > 국립국어원 > 모두의 말뭉치 > 개체명 분석 말뭉치 2021
- https://corpus.korean.go.kr/request/reausetMain.do

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 15151
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 3788  | 0.3978          | 0.5986    | 0.5471 | 0.5717 | 0.9087   |
| No log        | 2.0   | 7576  | 0.2319          | 0.6986    | 0.6953 | 0.6969 | 0.9345   |
| No log        | 3.0   | 11364 | 0.1838          | 0.7363    | 0.7612 | 0.7486 | 0.9444   |
| No log        | 4.0   | 15152 | 0.1610          | 0.7762    | 0.7745 | 0.7754 | 0.9509   |
| No log        | 5.0   | 18940 | 0.1475          | 0.7862    | 0.8011 | 0.7936 | 0.9545   |
| No log        | 6.0   | 22728 | 0.1417          | 0.7857    | 0.8181 | 0.8016 | 0.9563   |
| No log        | 7.0   | 26516 | 0.1366          | 0.8022    | 0.8196 | 0.8108 | 0.9584   |
| No log        | 8.0   | 30304 | 0.1346          | 0.8093    | 0.8236 | 0.8164 | 0.9596   |
| No log        | 9.0   | 34092 | 0.1328          | 0.8085    | 0.8299 | 0.8190 | 0.9602   |
| No log        | 10.0  | 37880 | 0.1332          | 0.8110    | 0.8368 | 0.8237 | 0.9608   |
| No log        | 11.0  | 41668 | 0.1323          | 0.8157    | 0.8347 | 0.8251 | 0.9612   |
| No log        | 12.0  | 45456 | 0.1353          | 0.8118    | 0.8402 | 0.8258 | 0.9611   |
| No log        | 13.0  | 49244 | 0.1370          | 0.8152    | 0.8416 | 0.8282 | 0.9616   |
| No log        | 14.0  | 53032 | 0.1368          | 0.8164    | 0.8415 | 0.8287 | 0.9616   |
| No log        | 15.0  | 56820 | 0.1378          | 0.8187    | 0.8438 | 0.8310 | 0.9621   |
| No log        | 16.0  | 60608 | 0.1389          | 0.8217    | 0.8438 | 0.8326 | 0.9626   |
| No log        | 17.0  | 64396 | 0.1380          | 0.8266    | 0.8426 | 0.8345 | 0.9631   |
| No log        | 18.0  | 68184 | 0.1428          | 0.8216    | 0.8445 | 0.8329 | 0.9625   |
| No log        | 19.0  | 71972 | 0.1431          | 0.8232    | 0.8455 | 0.8342 | 0.9628   |
| 0.1712        | 20.0  | 75760 | 0.1431          | 0.8232    | 0.8449 | 0.8339 | 0.9628   |


### Framework versions

- Transformers 4.27.4
- Pytorch 2.0.0+cu118
- Datasets 2.11.0
- Tokenizers 0.13.3
