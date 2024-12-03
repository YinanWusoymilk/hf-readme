---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
- finance
- intent-classification
datasets:
- banking77
metrics:
- accuracy
pipeline_tag: text-classification
base_model: distilbert-base-uncased
model-index:
- name: banking-intent-distilbert-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# banking-intent-distilbert-classifier

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the banking77 dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.2885
- eval_accuracy: 0.9244
- eval_runtime: 1.9357
- eval_samples_per_second: 1591.148
- eval_steps_per_second: 99.705
- epoch: 10.0
- step: 3130

_Note: This is just a simple example of fine-tuning a DistilBERT model for 
multi-class classification task to see how much it costs to train this 
model on Google Cloud (using a T4 GPU). It costs me about 1.07 SGD and 
takes less than 20 mins to complete the training. Although my intention was just 
to test it out on Google Cloud, the model has been appropriately trained 
and is now ready to be used. Hopefully, it is what you're looking for._

## Inference example
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("lxyuan/banking-intent-distilbert-classifier")
model = AutoModelForSequenceClassification.from_pretrained("lxyuan/banking-intent-distilbert-classifier")

banking_intend_classifier = TextClassificationPipeline(
  model=model,
  tokenizer=tokenizer,
  device=0
)

banking_intend_classifier("How to report lost card?")
>>> [{'label': 'lost_or_stolen_card', 'score': 0.9518502950668335}]

```

## Training and evaluation data

The BANKING77 dataset consists of online banking queries labeled with their corresponding intents, 
offering a comprehensive collection of 77 finely categorized intents within the banking domain. 
With a total of 13,083 customer service queries, it specifically emphasizes precise intent detection
within a single domain.

## Training procedure
- To reproduce the result, please refer to this [notebook](https://github.com/LxYuan0420/nlp/blob/main/notebooks/distillbert-intent-classification-banking.ipynb)
- To run the evaluation, please refer to this [evaluation notebook](https://github.com/LxYuan0420/nlp/blob/main/notebooks/Evaluator_from_Huggingface.ipynb)

### Evaluation
<details>
<summary>Evaluation result</summary>

Classification Report:
                                                   precision    recall  f1-score   support

                                activate_my_card     1.0000    0.9750    0.9873        40
                                       age_limit     0.9756    1.0000    0.9877        40
                         apple_pay_or_google_pay     1.0000    1.0000    1.0000        40
                                     atm_support     0.9750    0.9750    0.9750        40
                                automatic_top_up     1.0000    0.9000    0.9474        40
         balance_not_updated_after_bank_transfer     0.8205    0.8000    0.8101        40
        balance_not_updated_after_cheque_or_cash_deposit     1.0000    0.9750    0.9873        40
                         beneficiary_not_allowed     0.9250    0.9250    0.9250        40
                                 cancel_transfer     1.0000    0.9750    0.9873        40
                            card_about_to_expire     0.9756    1.0000    0.9877        40
                                 card_acceptance     0.9189    0.8500    0.8831        40
                                    card_arrival     0.9459    0.8750    0.9091        40
                          card_delivery_estimate     0.8605    0.9250    0.8916        40
                                    card_linking     0.9302    1.0000    0.9639        40
                                card_not_working     0.8478    0.9750    0.9070        40
                        card_payment_fee_charged     0.7917    0.9500    0.8636        40
                     card_payment_not_recognised     0.9231    0.9000    0.9114        40
                card_payment_wrong_exchange_rate     0.9048    0.9500    0.9268        40
                                  card_swallowed     1.0000    0.8750    0.9333        40
                          cash_withdrawal_charge     0.9744    0.9500    0.9620        40
                  cash_withdrawal_not_recognised     0.8667    0.9750    0.9176        40
                                      change_pin     0.9302    1.0000    0.9639        40
                                compromised_card     0.8889    0.8000    0.8421        40
                         contactless_not_working     1.0000    0.9000    0.9474        40
                                 country_support     0.9512    0.9750    0.9630        40
                           declined_card_payment     0.8125    0.9750    0.8864        40
                        declined_cash_withdrawal     0.7843    1.0000    0.8791        40
                               declined_transfer     0.9667    0.7250    0.8286        40
             direct_debit_payment_not_recognised     0.9444    0.8500    0.8947        40
                          disposable_card_limits     0.8974    0.8750    0.8861        40
                           edit_personal_details     0.9302    1.0000    0.9639        40
                                 exchange_charge     0.9722    0.8750    0.9211        40
                                   exchange_rate     0.9091    1.0000    0.9524        40
                                exchange_via_app     0.8085    0.9500    0.8736        40
                       extra_charge_on_statement     1.0000    0.9500    0.9744        40
                                 failed_transfer     0.8333    0.8750    0.8537        40
                           fiat_currency_support     0.8718    0.8500    0.8608        40
                     get_disposable_virtual_card     0.9722    0.8750    0.9211        40
                               get_physical_card     0.9756    1.0000    0.9877        40
                              getting_spare_card     0.9500    0.9500    0.9500        40
                            getting_virtual_card     0.8667    0.9750    0.9176        40
                             lost_or_stolen_card     0.8261    0.9500    0.8837        40
                            lost_or_stolen_phone     0.9750    0.9750    0.9750        40
                             order_physical_card     0.9231    0.9000    0.9114        40
                              passcode_forgotten     1.0000    1.0000    1.0000        40
                            pending_card_payment     0.9500    0.9500    0.9500        40
                         pending_cash_withdrawal     1.0000    0.9500    0.9744        40
                                  pending_top_up     0.9268    0.9500    0.9383        40
                                pending_transfer     0.8611    0.7750    0.8158        40
                                     pin_blocked     0.9714    0.8500    0.9067        40
                                 receiving_money     1.0000    0.9250    0.9610        40
                           Refund_not_showing_up     1.0000    0.9250    0.9610        40
                                  request_refund     0.9512    0.9750    0.9630        40
                          reverted_card_payment?     0.9286    0.9750    0.9512        40
                  supported_cards_and_currencies     0.9744    0.9500    0.9620        40
                               terminate_account     0.9302    1.0000    0.9639        40
                  top_up_by_bank_transfer_charge     1.0000    0.8250    0.9041        40
                           top_up_by_card_charge     0.9286    0.9750    0.9512        40
                        top_up_by_cash_or_cheque     0.8810    0.9250    0.9024        40
                                   top_up_failed     0.9024    0.9250    0.9136        40
                                   top_up_limits     0.9286    0.9750    0.9512        40
                                 top_up_reverted     0.9706    0.8250    0.8919        40
                              topping_up_by_card     0.8421    0.8000    0.8205        40
                       transaction_charged_twice     0.9302    1.0000    0.9639        40
                            transfer_fee_charged     0.9024    0.9250    0.9136        40
                           transfer_into_account     0.9167    0.8250    0.8684        40
              transfer_not_received_by_recipient     0.7778    0.8750    0.8235        40
                                 transfer_timing     0.8372    0.9000    0.8675        40
                       unable_to_verify_identity     0.9250    0.9250    0.9250        40
                              verify_my_identity     0.7955    0.8750    0.8333        40
                          verify_source_of_funds     0.9524    1.0000    0.9756        40
                                   verify_top_up     1.0000    1.0000    1.0000        40
                        virtual_card_not_working     1.0000    0.9250    0.9610        40
                              visa_or_mastercard     0.9737    0.9250    0.9487        40
                             why_verify_identity     0.9118    0.7750    0.8378        40
                   wrong_amount_of_cash_received     1.0000    0.8750    0.9333        40
         wrong_exchange_rate_for_cash_withdrawal     0.9730    0.9000    0.9351        40

                                        accuracy                         0.9244      3080
                                       macro avg     0.9282    0.9244    0.9243      3080
                                    weighted avg     0.9282    0.9244    0.9243      3080

</details>

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.29.2
- Pytorch 1.9.0+cu111
- Datasets 2.12.0
- Tokenizers 0.13.3