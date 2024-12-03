---
base_model: microsoft/mdeberta-v3-base
model-index:
- name: mdeberta-v3-base_finetuned_ai4privacy_v2
  results: []
datasets:
- ai4privacy/pii-masking-200k
- Isotonic/pii-masking-200k
language:
- en
- de
- fr
- it
metrics:
- accuracy
- f1
- precision
- recall
library_name: transformers
pipeline_tag: token-classification
license: cc-by-nc-4.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

🌟 Buying me coffee is a direct way to show support for this project. 
<a href="https://www.buymeacoffee.com/isotonic"><img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-1.svg" alt=""></a>


# mdeberta-v3-base_finetuned_ai4privacy_v2

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on the [ai4privacy/pii-masking-200k](https://huggingface.co/datasets/ai4privacy/pii-masking-200k) dataset.
It achieves the following results on the evaluation set:

- Loss: 0.0323
- Overall Precision: 0.9636
- Overall Recall: 0.9731
- Overall F1: 0.9683
- Overall Accuracy: 0.9896

## Useage
GitHub Implementation: [Ai4Privacy](https://github.com/Sripaad/ai4privacy)

## Model description

More information needed

## Intended uses & limitations

The license depends on the nature of your business, you're given the right to use Ai4Privacy for your projects. Independent users and small businesses (3 staff maximum) can use Ai4Privacy’s dataset and models in their product and solutions for free, and conditionally for commercial terms. However, larger, profit-oriented organizations require a company license which can be requested by [licensing@ai4privacy.com](mailto:licensing@ai4privacy.com).
This two-level system helps fund our project, while keeping the source code accessible and the software free for most users. For the exact usage conditions, please read the detailed terms below.

- Free license
- Corporate license

### Free License
Copyright © 2023 Ai4Privacy

#### Qualification Criteria
You're qualified to use Ai4Privacy at no cost if you're:

An individual
A for-profit entity with a staff count of up to 3
A non-profit or not-for-profit organization


### Prohibited Use Cases
It's not permissible to duplicate or alter Ai4Privacy's code with the intention to distribute, sell, rent, license, re-license, or sublicense your own derivative of Ai4Privacy's contribution work.

### Warranty Notice
The dataset and code comes "as is", without any express or implied warranties, including but not limited to warranties of saleability, suitability for a specific use, and non-infringement. The authors or copyright holders shall not be responsible for any claim, damage or other liability, whether in a contract, tort or otherwise, arising from or in connection with the dataset and model or its use or other dealings.

### Support
Support is offered as best as we can manage through GitHub Issues and our Discord. Corporate licensees receive dedicated support.

### Corporate License
Should your entity not fall under the category eligible for a free license, you must procure a corporate license to use Ai4Privacy. This license will authorize you to use Ai4Privacy for the use cases outlined in the free license and provide you with access to priority support..

Please refer to [licensing@ai4privacy.com](mailto:licensing@ai4privacy.com) for details on pricing and licensing.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-06
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_ratio: 0.2
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Overall Precision | Overall Recall | Overall F1 | Overall Accuracy | Accountname F1 | Accountnumber F1 | Age F1 | Amount F1 | Bic F1 | Bitcoinaddress F1 | Buildingnumber F1 | City F1 | Companyname F1 | County F1 | Creditcardcvv F1 | Creditcardissuer F1 | Creditcardnumber F1 | Currency F1 | Currencycode F1 | Currencyname F1 | Currencysymbol F1 | Date F1 | Dob F1 | Email F1 | Ethereumaddress F1 | Eyecolor F1 | Firstname F1 | Gender F1 | Height F1 | Iban F1 | Ip F1  | Ipv4 F1 | Ipv6 F1 | Jobarea F1 | Jobtitle F1 | Jobtype F1 | Lastname F1 | Litecoinaddress F1 | Mac F1 | Maskednumber F1 | Middlename F1 | Nearbygpscoordinate F1 | Ordinaldirection F1 | Password F1 | Phoneimei F1 | Phonenumber F1 | Pin F1 | Prefix F1 | Secondaryaddress F1 | Sex F1 | Ssn F1 | State F1 | Street F1 | Time F1 | Url F1 | Useragent F1 | Username F1 | Vehiclevin F1 | Vehiclevrm F1 | Zipcode F1 |
|:-------------:|:-----:|:-----:|:---------------:|:-----------------:|:--------------:|:----------:|:----------------:|:--------------:|:----------------:|:------:|:---------:|:------:|:-----------------:|:-----------------:|:-------:|:--------------:|:---------:|:----------------:|:-------------------:|:-------------------:|:-----------:|:---------------:|:---------------:|:-----------------:|:-------:|:------:|:--------:|:------------------:|:-----------:|:------------:|:---------:|:---------:|:-------:|:------:|:-------:|:-------:|:----------:|:-----------:|:----------:|:-----------:|:------------------:|:------:|:---------------:|:-------------:|:----------------------:|:-------------------:|:-----------:|:------------:|:--------------:|:------:|:---------:|:-------------------:|:------:|:------:|:--------:|:---------:|:-------:|:------:|:------------:|:-----------:|:-------------:|:-------------:|:----------:|
| 0.0622        | 1.0   | 10463 | 0.0541          | 0.9247            | 0.9384         | 0.9315     | 0.9770           | 0.9949         | 0.9917           | 0.9812 | 0.9224    | 0.9847 | 0.9592            | 0.9056            | 0.9595  | 0.9802         | 0.9775    | 0.9350           | 0.9971              | 0.8939              | 0.7380      | 0.9664          | 0.0843          | 0.9721            | 0.7784  | 0.6363 | 0.9993   | 0.9877             | 0.9833      | 0.9696       | 0.9866    | 0.9716    | 0.9914  | 0.0    | 0.8238  | 0.8025  | 0.9882     | 0.9874      | 0.9878     | 0.8820      | 0.9085             | 0.9869 | 0.8831          | 0.8686        | 0.9984                 | 0.9958              | 0.9786      | 0.9971       | 0.9885         | 0.9482 | 0.9455    | 0.9934              | 0.9956 | 0.9860 | 0.9673   | 0.9799    | 0.9916  | 0.9958 | 0.9995       | 0.9875      | 0.9555        | 0.9819        | 0.9311     |
| 0.0492        | 2.0   | 20926 | 0.0445          | 0.9376            | 0.9494         | 0.9434     | 0.9788           | 0.9970         | 0.9979           | 0.9883 | 0.9492    | 0.9949 | 0.9626            | 0.9548            | 0.9819  | 0.9911         | 0.9922    | 0.9740           | 0.9985              | 0.9057              | 0.5805      | 0.9771          | 0.4872          | 0.9734            | 0.8257  | 0.7479 | 0.9989   | 0.9944             | 0.9960      | 0.9819       | 0.9933    | 0.9958    | 0.9962  | 0.1521 | 0.7969  | 0.8083  | 0.9957     | 0.9972      | 0.9970     | 0.9335      | 0.8953             | 0.9967 | 0.8786          | 0.9232        | 1.0                    | 0.9980              | 0.9868      | 0.9985       | 0.9967         | 0.9808 | 0.9708    | 0.9969              | 0.9979 | 0.9980 | 0.9921   | 0.9913    | 0.9979  | 1.0    | 1.0          | 0.9914      | 0.9788        | 0.9859        | 0.9622     |
| 0.0392        | 3.0   | 31389 | 0.0395          | 0.9458            | 0.9584         | 0.9521     | 0.9815           | 0.9988         | 0.9971           | 0.9861 | 0.9573    | 0.9955 | 0.9764            | 0.9518            | 0.9836  | 0.9914         | 0.9921    | 0.9802           | 0.9985              | 0.9300              | 0.8115      | 0.9862          | 0.5935          | 0.9821            | 0.8684  | 0.7870 | 0.9994   | 0.9972             | 0.9976      | 0.9860       | 0.9956    | 0.9981    | 0.9964  | 0.3002 | 0.8302  | 0.7274  | 0.9863     | 0.9968      | 0.9979     | 0.9528      | 0.9208             | 0.9881 | 0.9195          | 0.9269        | 0.9992                 | 0.9980              | 0.9894      | 0.9998       | 0.9984         | 0.9750 | 0.9767    | 0.9971              | 0.9972 | 0.9978 | 0.9927   | 0.9952    | 0.9966  | 1.0    | 0.9997       | 0.9962      | 0.9942        | 0.9937        | 0.9653     |
| 0.0311        | 4.0   | 41852 | 0.0341          | 0.9537            | 0.9667         | 0.9601     | 0.9855           | 0.9998         | 0.9986           | 0.9869 | 0.9545    | 0.9961 | 0.9774            | 0.9632            | 0.9885  | 0.9952         | 0.9940    | 0.9838           | 0.9985              | 0.9392              | 0.8567      | 0.9863          | 0.7015          | 0.9853            | 0.9158  | 0.8687 | 1.0      | 0.9979             | 0.9984      | 0.9875       | 0.9971    | 1.0       | 0.9962  | 0.4882 | 0.8664  | 0.6966  | 0.9927     | 0.9973      | 0.9967     | 0.9583      | 0.9251             | 0.9979 | 0.9275          | 0.9351        | 1.0                    | 0.9988              | 0.9932      | 0.9998       | 0.9980         | 0.9852 | 0.9760    | 0.9983              | 0.9980 | 0.9985 | 0.9932   | 0.9952    | 0.9966  | 0.9996 | 1.0          | 0.9969      | 0.9955        | 0.9942        | 0.9685     |
| 0.0196        | 5.0   | 52315 | 0.0323          | 0.9636            | 0.9731         | 0.9683     | 0.9896           | 0.9998         | 0.9973           | 0.9878 | 0.9495    | 0.9932 | 0.9704            | 0.9648            | 0.9887  | 0.9942         | 0.9940    | 0.9820           | 0.9985              | 0.9570              | 0.8750      | 0.9888          | 0.7416          | 0.9819            | 0.9295  | 0.8946 | 0.9998   | 0.9965             | 0.9984      | 0.9886       | 0.9962    | 1.0       | 0.9966  | 0.6284 | 0.8884  | 0.8015  | 0.9940     | 0.9973      | 0.9970     | 0.9653      | 0.9109             | 0.9992 | 0.9524          | 0.9347        | 1.0                    | 0.9984              | 0.9936      | 0.9998       | 0.9992         | 0.9857 | 0.9801    | 0.9988              | 0.9979 | 0.9983 | 0.9944   | 0.9953    | 0.9974  | 1.0    | 1.0          | 0.9966      | 0.9936        | 0.9917        | 0.9727     |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.16.1
- Tokenizers 0.15.0