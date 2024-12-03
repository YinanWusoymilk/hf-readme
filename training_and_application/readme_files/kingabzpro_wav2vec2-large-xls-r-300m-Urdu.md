---
language:
- ur
license: apache-2.0
tags:
- generated_from_trainer
- hf-asr-leaderboard
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
metrics:
- wer
base_model: facebook/wav2vec2-xls-r-300m
model-index:
- name: wav2vec2-large-xls-r-300m-Urdu
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: ur
    metrics:
    - type: wer
      value: 39.89
      name: Test WER
    - type: cer
      value: 16.7
      name: Test CER
---
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-Urdu

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9889
- Wer: 0.5607
- Cer: 0.2370
#### Evaluation Commands
1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id kingabzpro/wav2vec2-large-xls-r-300m-Urdu --dataset mozilla-foundation/common_voice_8_0 --config ur --split test
```


### Inference With LM

```python
from datasets import load_dataset, Audio
from transformers import pipeline
model = "kingabzpro/wav2vec2-large-xls-r-300m-Urdu"
data = load_dataset("mozilla-foundation/common_voice_8_0",
                     "ur",
                     split="test", 
                     streaming=True, 
                     use_auth_token=True)

sample_iter = iter(data.cast_column("path", 
                    Audio(sampling_rate=16_000)))
sample = next(sample_iter)

asr = pipeline("automatic-speech-recognition", model=model)
prediction = asr(sample["path"]["array"], 
                  chunk_length_s=5, 
                  stride_length_s=1)
prediction
# => {'text': 'اب یہ ونگین لمحاتانکھار دلمیں میںفوث کریلیا اجائ'}
```



### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 200

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:------:|:----:|:---------------:|:------:|:------:|
| 3.6398        | 30.77  | 400  | 3.3517          | 1.0    | 1.0    |
| 2.9225        | 61.54  | 800  | 2.5123          | 1.0    | 0.8310 |
| 1.2568        | 92.31  | 1200 | 0.9699          | 0.6273 | 0.2575 |
| 0.8974        | 123.08 | 1600 | 0.9715          | 0.5888 | 0.2457 |
| 0.7151        | 153.85 | 2000 | 0.9984          | 0.5588 | 0.2353 |
| 0.6416        | 184.62 | 2400 | 0.9889          | 0.5607 | 0.2370 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0

### Eval results on Common Voice 8 "test" (WER):

| Without LM | With LM (run `./eval.py`) |
|---|---|
| 52.03 | 39.89 |
