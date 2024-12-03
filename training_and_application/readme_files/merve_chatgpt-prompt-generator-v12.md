---
license: apache-2.0
tags:
- generated_from_keras_callback
model-index:
- name: chatgpt-prompt-generator-v12
  results: []
datasets:
- fka/awesome-chatgpt-prompts
---


# ChatGPT Prompt Generator v12

This model is a fine-tuned version of [BART-large](https://huggingface.co/facebook/bart-large) on a ChatGPT prompts dataset.
It achieves the following results on the evaluation set:
It achieves the following results on the evaluation set:
- Train Loss: 2.4800
- Validation Loss: 2.7320
- Epoch: 4


## Intended uses & limitations

You can use this to generate ChatGPT personas. Simply input a persona like below:

```
from transformers import BartForConditionalGeneration, BartTokenizer

example_english_phrase = "photographer"
batch = tokenizer(example_english_phrase, return_tensors="pt")
generated_ids = model.generate(batch["input_ids"], max_new_tokens=150)
output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
```

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 5.3808     | 3.3133          | 0     |
| 3.2642     | 3.0104          | 1     |
| 2.8886     | 2.8600          | 2     |
| 2.6594     | 2.7949          | 3     |
| 2.4800     | 2.7320          | 4     |


### Framework versions

- Transformers 4.26.1
- TensorFlow 2.11.0
- Datasets 2.10.1
- Tokenizers 0.13.2