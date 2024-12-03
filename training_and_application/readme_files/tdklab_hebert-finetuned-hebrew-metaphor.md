---

language: he
datasets:
- tdklab/HebrewMetaphors
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: hebert-finetuned-hebrew-metaphor
  results: []
widget:
- text: "לבשל [SEP] שישי בבוקר זה זמן טוב כדי לבשל ארוחה יפה"
- text: "לטחון [SEP] להכנת קפה במקינטה יש לטחון את הקפה טחינה גסה יותר מאשר קפה לאספרסו"
- text: "לטחון [SEP] תעירו אותי כשיקרה עוד משהו מעניין, בינתיים אין מה לטחון את זה"
- text: "לבשל [SEP]  השחקן השתמש ביכולותיו הפיזיות, הגובה והקפיצה שלו, כדי לבשל ולהבקיע שערים"
---

# hebert-finetuned-hebrew-metaphor

The model is fine-tuned to determine if a word in a sentence is used metaphorically or literally.

The model was trained for the following verbs:
לחלום, לחתוך, לעוף, לפרק, להדליק, לכבס, לכופף, לרסק, לבשל, למחוק, לקפוץ, לקרוע, לקצור, לרקוד, לשבור, לשדוד, לשתות, לטחון, לתפור, לזרוע

This model is a fine-tuned version of [avichr/heBERT](https://huggingface.co/avichr/heBERT) on HebrewMetaphors dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4682
- Accuracy: 0.9510

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 389  | 0.1813          | 0.9379   |
| 0.2546        | 2.0   | 778  | 0.2309          | 0.9479   |
| 0.08          | 3.0   | 1167 | 0.3342          | 0.9492   |
| 0.0298        | 4.0   | 1556 | 0.4076          | 0.9460   |
| 0.0298        | 5.0   | 1945 | 0.3803          | 0.9485   |
| 0.0105        | 6.0   | 2334 | 0.3674          | 0.9454   |
| 0.0077        | 7.0   | 2723 | 0.5356          | 0.9410   |
| 0.0088        | 8.0   | 3112 | 0.4776          | 0.9422   |
| 0.0044        | 9.0   | 3501 | 0.4258          | 0.9504   |
| 0.0044        | 10.0  | 3890 | 0.4305          | 0.9523   |
| 0.001         | 11.0  | 4279 | 0.4357          | 0.9548   |
| 0.0031        | 12.0  | 4668 | 0.4770          | 0.9473   |
| 0.0015        | 13.0  | 5057 | 0.4604          | 0.9523   |
| 0.0015        | 14.0  | 5446 | 0.4670          | 0.9510   |
| 0.0022        | 15.0  | 5835 | 0.4682          | 0.9510   |


### Framework versions

- Transformers 4.30.2
- Pytorch 2.0.1+cu118
- Datasets 2.13.1
- Tokenizers 0.13.3



### About Us
Created by Doron Ben-chorin, Matan Ben-chorin, Tomer Tzipori, Guided by Dr. Oren Mishali. This is our project as part of computer engineering studies in the Faculty of Electrical Engineering combined with Computer Science at Technion, Israel Institute of Technology. For more cooperation, please contact email: 

Doron Ben-chorin: doronbh7@gmail.com 

Matan Ben-chorin: matan.bh1@gmail.com 

Tomer Tzipori: TomerTzipori@gmail.com


