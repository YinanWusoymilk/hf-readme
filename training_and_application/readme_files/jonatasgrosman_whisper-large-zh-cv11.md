---
language:
- zh
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
- cer
model-index:
- name: Whisper Large Chinese (Mandarin)
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 zh-CN
      type: mozilla-foundation/common_voice_11_0
      config: zh-CN
      split: test
      args: zh-CN
    metrics:
    - name: WER
      type: wer
      value: 55.02141421204441
    - name: CER
      type: cer
      value: 9.550758567294045
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: google/fleurs cmn_hans_cn
      type: google/fleurs
      config: cmn_hans_cn
      split: test
      args: cmn_hans_cn
    metrics:
    - name: WER
      type: wer
      value: 70.62596203181118
    - name: CER
      type: cer
      value: 11.761282471826888
---

# Whisper Large Chinese (Mandarin)

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on Chinese (Mandarin) using the train and validation splits of [Common Voice 11](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0). Not all validation split data were used during training, I extracted 1k samples from the validation split to be used for evaluation during fine-tuning.

## Usage

```python

from transformers import pipeline

transcriber = pipeline(
  "automatic-speech-recognition", 
  model="jonatasgrosman/whisper-large-zh-cv11"
)

transcriber.model.config.forced_decoder_ids = (
  transcriber.tokenizer.get_decoder_prompt_ids(
    language="zh", 
    task="transcribe"
  )
)

transcription = transcriber("path/to/my_audio.wav")

```

## Evaluation

I've performed the evaluation of the model using the test split of two datasets, the [Common Voice 11](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0) (same dataset used for the fine-tuning) and the [Fleurs](https://huggingface.co/datasets/google/fleurs) (dataset not seen during the fine-tuning). As Whisper can transcribe casing and punctuation, I've performed the model evaluation in 2 different scenarios, one using the raw text and the other using the normalized text (lowercase + removal of punctuations). Additionally, for the Fleurs dataset, I've evaluated the model in a scenario where there are no transcriptions of numerical values since the way these values are described in this dataset is different from how they are described in the dataset used in fine-tuning (Common Voice), so it is expected that this difference in the way of describing numerical values will affect the performance of the model for this type of transcription in Fleurs.

### Common Voice 11

| | CER | WER |
| --- | --- | --- |
| [jonatasgrosman/whisper-large-zh-cv11](https://huggingface.co/jonatasgrosman/whisper-large-zh-cv11) | 9.31 | 55.94 |
| [jonatasgrosman/whisper-large-zh-cv11](https://huggingface.co/jonatasgrosman/whisper-large-zh-cv11) + text normalization | 9.55 | 55.02 |
| [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) | 33.33 | 101.80 |
| [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) + text normalization | 29.90 | 95.91 |

### Fleurs

| | CER | WER |
| --- | --- | --- |
| [jonatasgrosman/whisper-large-zh-cv11](https://huggingface.co/jonatasgrosman/whisper-large-zh-cv11) | 15.00 | 93.45 |
| [jonatasgrosman/whisper-large-zh-cv11](https://huggingface.co/jonatasgrosman/whisper-large-zh-cv11) + text normalization | 11.76 | 70.63 |
| [jonatasgrosman/whisper-large-zh-cv11](https://huggingface.co/jonatasgrosman/whisper-large-zh-cv11) + keep only non-numeric samples | 10.95 | 87.91 |
| [jonatasgrosman/whisper-large-zh-cv11](https://huggingface.co/jonatasgrosman/whisper-large-zh-cv11) + text normalization + keep only non-numeric samples | 7.83 | 62.12 |
| [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) | 23.49 | 101.28 |
| [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) + text normalization | 17.58 | 83.22 |
| [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) + keep only non-numeric samples | 21.03 | 101.95 |
| [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) + text normalization + keep only non-numeric samples | 15.22 | 79.28 |
