---
license: mit
base_model: roberta-base
tags:
- generated_from_trainer
metrics:
- accuracy
- recall
- precision
- f1
model-index:
- name: roberta-base-suicide-prediction-phr
  results:
  - task:
      type: text-classification
      name: Suicidal Tendency Prediction in text 
    dataset:
      type: vibhorag101/roberta-base-suicide-prediction-phr
      name: Suicide Prediction Dataset
      split: test
    metrics:
      - type: accuracy
        value: 0.9652972367116438
      - type: f1
        value: 0.9651921995935487
      - type: recall
        value: 0.966571403827834
      - type: precision
        value: 0.9638169257340242
datasets:
- vibhorag101/suicide_prediction_dataset_phr
language:
- en
library_name: transformers
---

# roberta-base-suicide-prediction-phr

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on this [dataset](https://huggingface.co/datasets/vibhorag101/suicide_prediction_dataset_phr)   sourced from Reddit. 
It achieves the following results on the evaluation/validation set:
- Loss: 0.1543
- Accuracy: 0.9652972367116438
- Recall: 0.966571403827834
- Precision: 0.9638169257340242
- F1: 0.9651921995935487

It achieves the following result on validation partition of this updated [dataset](vibhorag101/phr_suicide_prediction_dataset_clean_light)
- Loss: 0.08761
- Accuracy: 0.97065
- Recall: 0.96652
- Precision: 0.97732
- F1: 0.97189

## Model description
This model is a finetune of roberta-base to detect suicidal tendencies in a given text.

## Training and evaluation data
- The dataset is sourced from Reddit and is available on [Kaggle](https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch).
- The dataset contains text with binary labels for suicide or non-suicide. 
- The dataset was cleaned, and following steps were applied
  - Converted to lowercase
  - Removed numbers and special characters.
  - Removed URLs, Emojis and accented characters.
  - Removed any word contractions.
  - Remove any extra white spaces and any extra spaces after a single space.
  - Removed any consecutive characters repeated more than 3 times.
  - Tokenised the text, then lemmatized it and then removed the stopwords (excluding not).
- The cleaned dataset can be found [here](https://huggingface.co/datasets/vibhorag101/suicide_prediction_dataset_phr)   
- The evaluation set had ~23000 samples, while the training set had ~186k samples, i.e. a 80:10:10 (train:test:val) split.

## Training procedure
- The model was trained on an RTXA5000 GPU.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy                         | Recall                         | Precision                         | F1                         |
|:-------------:|:-----:|:-----:|:---------------:|:--------------------------------:|:------------------------------:|:---------------------------------:|:--------------------------:|
| 0.2023        | 0.09  | 1000  | 0.1868          | {'accuracy': 0.9415010561710566} | {'recall': 0.9389451805663809} | {'precision': 0.943274752044545}  | {'f1': 0.9411049867627274} |
| 0.1792        | 0.17  | 2000  | 0.1465          | {'accuracy': 0.9528387291460103} | {'recall': 0.9615484541439335} | {'precision': 0.9446949714966392} | {'f1': 0.9530472103004292} |
| 0.1596        | 0.26  | 3000  | 0.1871          | {'accuracy': 0.9523645298961072} | {'recall': 0.9399844115354637} | {'precision': 0.9634297887448962} | {'f1': 0.9515627054749485} |
| 0.1534        | 0.34  | 4000  | 0.1563          | {'accuracy': 0.9518041126007674} | {'recall': 0.974971854161254}  | {'precision': 0.9314139157772814} | {'f1': 0.9526952695269527} |
| 0.1553        | 0.43  | 5000  | 0.1691          | {'accuracy': 0.9513730223735828} | {'recall': 0.93141075604053}   | {'precision': 0.9697051663510955} | {'f1': 0.950172276702889}  |
| 0.1537        | 0.52  | 6000  | 0.1347          | {'accuracy': 0.9568478682588266} | {'recall': 0.9644063393089114} | {'precision': 0.9496844618795839} | {'f1': 0.9569887852876723} |
| 0.1515        | 0.6   | 7000  | 0.1276          | {'accuracy': 0.9565461050997974} | {'recall': 0.9426690915389279} | {'precision': 0.9691924138545098} | {'f1': 0.9557467732022126} |
| 0.1453        | 0.69  | 8000  | 0.1351          | {'accuracy': 0.960210372030866}  | {'recall': 0.9589503767212263} | {'precision': 0.961031070994619}  | {'f1': 0.959989596428107}  |
| 0.1526        | 0.78  | 9000  | 0.1423          | {'accuracy': 0.9610725524852352} | {'recall': 0.9612020438209059} | {'precision': 0.9606196988056085} | {'f1': 0.9609107830829834} |
| 0.1437        | 0.86  | 10000 | 0.1365          | {'accuracy': 0.9599948269172738} | {'recall': 0.9625010825322594} | {'precision': 0.9573606684468946} | {'f1': 0.9599239937813093} |
| 0.1317        | 0.95  | 11000 | 0.1275          | {'accuracy': 0.9616760788032935} | {'recall': 0.9653589676972374} | {'precision': 0.9579752492265383} | {'f1': 0.9616529353405513} |
| 0.125         | 1.03  | 12000 | 0.1428          | {'accuracy': 0.9608138983489244} | {'recall': 0.9522819780029445} | {'precision': 0.9684692619341201} | {'f1': 0.9603074101567617} |
| 0.1135        | 1.12  | 13000 | 0.1627          | {'accuracy': 0.960770789326206}  | {'recall': 0.9544470425218672} | {'precision': 0.966330556773345}  | {'f1': 0.9603520390379923} |
| 0.1096        | 1.21  | 14000 | 0.1240          | {'accuracy': 0.9624520412122257} | {'recall': 0.9566987096215467} | {'precision': 0.9675074443860571} | {'f1': 0.962072719355541}  |
| 0.1213        | 1.29  | 15000 | 0.1502          | {'accuracy': 0.9616760788032935} | {'recall': 0.9659651857625358} | {'precision': 0.9574248927038627} | {'f1': 0.9616760788032936} |
| 0.1166        | 1.38  | 16000 | 0.1574          | {'accuracy': 0.958873992326594}  | {'recall': 0.9438815276695246} | {'precision': 0.9726907630522088} | {'f1': 0.9580696202531646} |
| 0.1214        | 1.47  | 17000 | 0.1626          | {'accuracy': 0.9562443419407682} | {'recall': 0.9773101238416905} | {'precision': 0.9374480810765908} | {'f1': 0.9569641721433114} |
| 0.1064        | 1.55  | 18000 | 0.1653          | {'accuracy': 0.9624089321895073} | {'recall': 0.9622412747899888} | {'precision': 0.9622412747899888} | {'f1': 0.9622412747899888} |
| 0.1046        | 1.64  | 19000 | 0.1608          | {'accuracy': 0.9640039660300901} | {'recall': 0.9697756993158396} | {'precision': 0.9584046559397467} | {'f1': 0.9640566484438896} |
| 0.1043        | 1.72  | 20000 | 0.1556          | {'accuracy': 0.960770789326206}  | {'recall': 0.9493374902572097} | {'precision': 0.9712058119961017} | {'f1': 0.9601471489883507} |
| 0.0995        | 1.81  | 21000 | 0.1646          | {'accuracy': 0.9602534810535845} | {'recall': 0.9752316619035247} | {'precision': 0.9465411448264268} | {'f1': 0.9606722402320423} |
| 0.1065        | 1.9   | 22000 | 0.1721          | {'accuracy': 0.9627106953485365} | {'recall': 0.9710747380271932} | {'precision': 0.9547854223433242} | {'f1': 0.9628611910179897} |
| 0.1204        | 1.98  | 23000 | 0.1214          | {'accuracy': 0.9629693494848471} | {'recall': 0.961028838659392}  | {'precision': 0.9644533286980705} | {'f1': 0.9627380384331756} |
| 0.0852        | 2.07  | 24000 | 0.1583          | {'accuracy': 0.9643919472345562} | {'recall': 0.9624144799515025} | {'precision': 0.9659278574532811} | {'f1': 0.9641679680721846} |
| 0.0812        | 2.16  | 25000 | 0.1594          | {'accuracy': 0.9635728758029055} | {'recall': 0.9572183251060882} | {'precision': 0.9692213258505787} | {'f1': 0.9631824321380331} |
| 0.0803        | 2.24  | 26000 | 0.1629          | {'accuracy': 0.9639177479846532} | {'recall': 0.9608556334978783} | {'precision': 0.9664634146341463} | {'f1': 0.963651365787988}  |
| 0.0832        | 2.33  | 27000 | 0.1570          | {'accuracy': 0.9631417855757209} | {'recall': 0.9658785831817788} | {'precision': 0.9603065266058206} | {'f1': 0.9630844954881052} |
| 0.0887        | 2.41  | 28000 | 0.1551          | {'accuracy': 0.9623227141440703} | {'recall': 0.9669178141508616} | {'precision': 0.9577936004117698} | {'f1': 0.9623340803309774} |
| 0.084         | 2.5   | 29000 | 0.1585          | {'accuracy': 0.9644350562572747} | {'recall': 0.9613752489824197} | {'precision': 0.96698606271777}   | {'f1': 0.9641724931602031} |
| 0.0807        | 2.59  | 30000 | 0.1601          | {'accuracy': 0.9639177479846532} | {'recall': 0.9699489044773534} | {'precision': 0.9580838323353293} | {'f1': 0.9639798597065025} |
| 0.079         | 2.67  | 31000 | 0.1645          | {'accuracy': 0.9628400224166919} | {'recall': 0.9558326838139777} | {'precision': 0.9690929844586882} | {'f1': 0.9624171607952564} |
| 0.0913        | 2.76  | 32000 | 0.1560          | {'accuracy': 0.9642626201664009} | {'recall': 0.964752749631939}  | {'precision': 0.9635011243729459} | {'f1': 0.9641265307888701} |
| 0.0927        | 2.85  | 33000 | 0.1491          | {'accuracy': 0.9649523645298961} | {'recall': 0.9659651857625358} | {'precision': 0.9637117677553136} | {'f1': 0.9648371610224472} |
| 0.0882        | 2.93  | 34000 | 0.1543          | {'accuracy': 0.9652972367116438} | {'recall': 0.966571403827834}  | {'precision': 0.9638169257340242} | {'f1': 0.9651921995935487} |


### Framework versions

- Transformers 4.31.0
- Pytorch 2.1.0+cu121
- Datasets 2.14.5
- Tokenizers 0.13.3