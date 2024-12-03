---
library_name: transformers
license: cc-by-nc-nd-4.0
base_model: microsoft/mdeberta-v3-base
tags:
- generated_from_trainer
- pii
- privacy
- personaldata
- redaction
- piidetection
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: piiranha-1
  results: []
datasets:
- ai4privacy/pii-masking-400k
language:
- en
- it
- fr
- de
- nl
- es
pipeline_tag: token-classification
---

# Piiranha-v1: Protect your personal information!
<a target="_blank" href="https://colab.research.google.com/github/williamgao1729/piiranha-quickstart/blob/main/piiranha_quickstart%20(1).ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Piiranha (cc-by-nc-nd-4.0 license) is trained to **detect 17 types** of Personally Identifiable Information (PII) across six languages. It successfully **catches 98.27% of PII** tokens, with an overall classification **accuracy of 99.44%**.
Piiranha is especially accurate at detecting passwords, emails (100%), phone numbers, and usernames.

Performance on PII vs. Non PII classification task:
- **Precision: 98.48%** (98.48% of tokens classified as PII are actually PII)
- **Recall: 98.27%** (correctly identifies 98.27% of PII tokens)
- **Specificity: 99.84%** (correctly identifies 99.84% of Non PII tokens)

<img src="https://cloud-3i4ld6u5y-hack-club-bot.vercel.app/0home.png" alt="Akash Network logo" width="250"/>

Piiranha was trained on H100 GPUs generously sponsored by the [Akash Network](https://akash.network)

## Model Description
Piiranha is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base).
The context length is 256 Deberta tokens. If your text is longer than that, just split it up.

Supported languages: English, Spanish, French, German, Italian, Dutch

Supported PII types: Account Number, Building Number, City, Credit Card Number, Date of Birth, Driver's License, Email, First Name, Last Name, ID Card, Password, Social Security Number, Street Address, Tax Number, Phone Number, Username, Zipcode. 

It achieves the following results on a test set of ~73,000 sentences containing PII:
- Accuracy: 99.44%
- Loss: 0.0173
- Precision: 93.16%
- Recall: 93.08%
- F1: 93.12%

Note that the above metrics factor in the eighteen possible categories (17 PII and 1 Non PII), so the metrics are lower than the metrics for just PII vs. Non PII (binary classification).

## Performance by PII type
Reported performance metrics are lower than the overall accuracy of 99.44% due to class imbalance (most tokens are not PII).
However, the model is more useful than the below results suggest, due to the intent behind PII detection. The model sometimes misclassifies one PII type for another, but at the end of the day, it still recognizes the token as PII.
For instance, the model often confuses first names for last names, but that's fine because it still flags the name as PII.

| Entity              | Precision | Recall | F1-Score | Support |
|---------------------|-----------|--------|----------|---------|
| ACCOUNTNUM          | 0.84      | 0.87   | 0.85     | 3575    |
| BUILDINGNUM         | 0.92      | 0.90   | 0.91     | 3252    |
| CITY                | 0.95      | 0.97   | 0.96     | 7270    |
| CREDITCARDNUMBER    | 0.94      | 0.96   | 0.95     | 2308    |
| DATEOFBIRTH         | 0.93      | 0.85   | 0.89     | 3389    |
| DRIVERLICENSENUM    | 0.96      | 0.96   | 0.96     | 2244    |
| EMAIL               | 1.00      | 1.00   | 1.00     | 6892    |
| GIVENNAME           | 0.87      | 0.93   | 0.90     | 12150   |
| IDCARDNUM           | 0.89      | 0.94   | 0.91     | 3700    |
| PASSWORD            | 0.98      | 0.98   | 0.98     | 2387    |
| SOCIALNUM           | 0.93      | 0.94   | 0.93     | 2709    |
| STREET              | 0.97      | 0.95   | 0.96     | 3331    |
| SURNAME             | 0.89      | 0.78   | 0.83     | 8267    |
| TAXNUM              | 0.97      | 0.89   | 0.93     | 2322    |
| TELEPHONENUM        | 0.99      | 1.00   | 0.99     | 5039    |
| USERNAME            | 0.98      | 0.98   | 0.98     | 7680    |
| ZIPCODE             | 0.94      | 0.97   | 0.95     | 3191    |
| **micro avg**       | 0.93      | 0.93   | 0.93     | 79706   |
| **macro avg**       | 0.94      | 0.93   | 0.93     | 79706   |
| **weighted avg**    | 0.93      | 0.93   | 0.93     | 79706   |

## Intended uses & limitations

Piiranha can be used to assist with redacting PII from texts. Use at your own risk. We do not accept responsibility for any incorrect model predictions.
## Training and evaluation data

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2984        | 0.0983 | 250  | 0.1005          | 0.5446    | 0.6111 | 0.5759 | 0.9702   |
| 0.0568        | 0.1965 | 500  | 0.0464          | 0.7895    | 0.8459 | 0.8167 | 0.9849   |
| 0.0441        | 0.2948 | 750  | 0.0400          | 0.8346    | 0.8669 | 0.8504 | 0.9869   |
| 0.0368        | 0.3931 | 1000 | 0.0320          | 0.8531    | 0.8784 | 0.8656 | 0.9891   |
| 0.0323        | 0.4914 | 1250 | 0.0293          | 0.8779    | 0.8889 | 0.8834 | 0.9903   |
| 0.0287        | 0.5896 | 1500 | 0.0269          | 0.8919    | 0.8836 | 0.8877 | 0.9907   |
| 0.0282        | 0.6879 | 1750 | 0.0276          | 0.8724    | 0.9012 | 0.8866 | 0.9903   |
| 0.0268        | 0.7862 | 2000 | 0.0254          | 0.8890    | 0.9041 | 0.8965 | 0.9914   |
| 0.0264        | 0.8844 | 2250 | 0.0236          | 0.8886    | 0.9040 | 0.8962 | 0.9915   |
| 0.0243        | 0.9827 | 2500 | 0.0232          | 0.8998    | 0.9033 | 0.9015 | 0.9917   |
| 0.0213        | 1.0810 | 2750 | 0.0237          | 0.9115    | 0.9040 | 0.9077 | 0.9923   |
| 0.0213        | 1.1792 | 3000 | 0.0222          | 0.9123    | 0.9143 | 0.9133 | 0.9925   |
| 0.0217        | 1.2775 | 3250 | 0.0222          | 0.8999    | 0.9169 | 0.9083 | 0.9924   |
| 0.0209        | 1.3758 | 3500 | 0.0212          | 0.9111    | 0.9133 | 0.9122 | 0.9928   |
| 0.0204        | 1.4741 | 3750 | 0.0206          | 0.9054    | 0.9203 | 0.9128 | 0.9926   |
| 0.0183        | 1.5723 | 4000 | 0.0212          | 0.9126    | 0.9160 | 0.9143 | 0.9927   |
| 0.0191        | 1.6706 | 4250 | 0.0192          | 0.9122    | 0.9192 | 0.9157 | 0.9929   |
| 0.0185        | 1.7689 | 4500 | 0.0195          | 0.9200    | 0.9191 | 0.9196 | 0.9932   |
| 0.018         | 1.8671 | 4750 | 0.0188          | 0.9136    | 0.9215 | 0.9176 | 0.9933   |
| 0.0183        | 1.9654 | 5000 | 0.0191          | 0.9179    | 0.9212 | 0.9196 | 0.9934   |
| 0.0147        | 2.0637 | 5250 | 0.0188          | 0.9246    | 0.9242 | 0.9244 | 0.9937   |
| 0.0149        | 2.1619 | 5500 | 0.0184          | 0.9188    | 0.9254 | 0.9221 | 0.9937   |
| 0.0143        | 2.2602 | 5750 | 0.0193          | 0.9187    | 0.9224 | 0.9205 | 0.9932   |
| 0.014         | 2.3585 | 6000 | 0.0190          | 0.9246    | 0.9280 | 0.9263 | 0.9936   |
| 0.0146        | 2.4568 | 6250 | 0.0190          | 0.9225    | 0.9277 | 0.9251 | 0.9936   |
| 0.0148        | 2.5550 | 6500 | 0.0175          | 0.9297    | 0.9306 | 0.9301 | 0.9942   |
| 0.0136        | 2.6533 | 6750 | 0.0172          | 0.9191    | 0.9329 | 0.9259 | 0.9938   |
| 0.0137        | 2.7516 | 7000 | 0.0166          | 0.9299    | 0.9312 | 0.9306 | 0.9942   |
| 0.014         | 2.8498 | 7250 | 0.0167          | 0.9285    | 0.9313 | 0.9299 | 0.9942   |
| 0.0128        | 2.9481 | 7500 | 0.0166          | 0.9271    | 0.9326 | 0.9298 | 0.9943   |
| 0.0113        | 3.0464 | 7750 | 0.0171          | 0.9286    | 0.9347 | 0.9316 | 0.9946   |
| 0.0103        | 3.1447 | 8000 | 0.0172          | 0.9284    | 0.9383 | 0.9334 | 0.9945   |
| 0.0104        | 3.2429 | 8250 | 0.0169          | 0.9312    | 0.9406 | 0.9359 | 0.9947   |
| 0.0094        | 3.3412 | 8500 | 0.0166          | 0.9368    | 0.9359 | 0.9364 | 0.9948   |
| 0.01          | 3.4395 | 8750 | 0.0166          | 0.9289    | 0.9387 | 0.9337 | 0.9944   |
| 0.0099        | 3.5377 | 9000 | 0.0162          | 0.9335    | 0.9332 | 0.9334 | 0.9947   |
| 0.0099        | 3.6360 | 9250 | 0.0160          | 0.9321    | 0.9380 | 0.9350 | 0.9947   |
| 0.01          | 3.7343 | 9500 | 0.0168          | 0.9306    | 0.9389 | 0.9347 | 0.9947   |
| 0.0101        | 3.8325 | 9750 | 0.0159          | 0.9339    | 0.9350 | 0.9344 | 0.9947   |

### Contact
william (at) integrinet [dot] org
 
### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.0
- Tokenizers 0.19.1