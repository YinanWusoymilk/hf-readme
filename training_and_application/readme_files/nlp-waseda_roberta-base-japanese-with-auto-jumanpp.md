---
language: ja
license: cc-by-sa-4.0
datasets:
- wikipedia
- cc100
mask_token: "[MASK]"
widget:
- text: "早稲田大学で自然言語処理を[MASK]する。"
---

# nlp-waseda/roberta-base-japanese-with-auto-jumanpp

## Model description

This is a Japanese RoBERTa base model pretrained on Japanese Wikipedia and the Japanese portion of CC-100.

## How to use

You can use this model for masked language modeling as follows:
```python
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("nlp-waseda/roberta-base-japanese-with-auto-jumanpp")
model = AutoModelForMaskedLM.from_pretrained("nlp-waseda/roberta-base-japanese-with-auto-jumanpp")

sentence = '早稲田大学で自然言語処理を[MASK]する。'
encoding = tokenizer(sentence, return_tensors='pt')
...
```

You can fine-tune this model on downstream tasks.

## Tokenization

`BertJapaneseTokenizer` now supports automatic tokenization for [Juman++](https://github.com/ku-nlp/jumanpp). However, if your dataset is large, you may take a long time since `BertJapaneseTokenizer` still does not supoort fast tokenization. You can still do the Juman++ tokenization by your self and use the old model [nlp-waseda/roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese).

Juman++ 2.0.0-rc3 was used for pretraining. Each word is tokenized into tokens by [sentencepiece](https://github.com/google/sentencepiece).

## Vocabulary

The vocabulary consists of 32000 tokens including words ([JumanDIC](https://github.com/ku-nlp/JumanDIC)) and subwords induced by the unigram language model of [sentencepiece](https://github.com/google/sentencepiece).

## Training procedure

This model was trained on Japanese Wikipedia (as of 20210920) and the Japanese portion of CC-100. It took a week using eight NVIDIA A100 GPUs.

The following hyperparameters were used during pretraining:
- learning_rate: 1e-4
- per_device_train_batch_size: 256
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 2
- total_train_batch_size: 4096
- max_seq_length: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 700000
- warmup_steps: 10000
- mixed_precision_training: Native AMP

## Performance on JGLUE

See the [Baseline Scores](https://github.com/yahoojapan/JGLUE#baseline-scores) of JGLUE.
