---
language: it
license: apache-2.0
datasets:
- common_voice
- mozilla-foundation/common_voice_6_0
metrics:
- wer
- cer
tags:
- audio
- automatic-speech-recognition
- hf-asr-leaderboard
- it
- mozilla-foundation/common_voice_6_0
- robust-speech-event
- speech
- xlsr-fine-tuning-week
model-index:
- name: XLSR Wav2Vec2 Italian by Jonatas Grosman
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice it
      type: common_voice
      args: it
    metrics:
    - name: Test WER
      type: wer
      value: 9.41
    - name: Test CER
      type: cer
      value: 2.29
    - name: Test WER (+LM)
      type: wer
      value: 6.91
    - name: Test CER (+LM)
      type: cer
      value: 1.83
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: it
    metrics:
    - name: Dev WER
      type: wer
      value: 21.78
    - name: Dev CER
      type: cer
      value: 7.94
    - name: Dev WER (+LM)
      type: wer
      value: 15.82
    - name: Dev CER (+LM)
      type: cer
      value: 6.83
---

# Fine-tuned XLSR-53 large model for speech recognition in Italian

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on Italian using the train and validation splits of [Common Voice 6.1](https://huggingface.co/datasets/common_voice).
When using this model, make sure that your speech input is sampled at 16kHz.

This model has been fine-tuned thanks to the GPU credits generously given by the [OVHcloud](https://www.ovhcloud.com/en/public-cloud/ai-training/) :)

The script used for training can be found here: https://github.com/jonatasgrosman/wav2vec2-sprint

## Usage

The model can be used directly (without a language model) as follows...

Using the [HuggingSound](https://github.com/jonatasgrosman/huggingsound) library:

```python
from huggingsound import SpeechRecognitionModel

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-italian")
audio_paths = ["/path/to/file.mp3", "/path/to/another_file.wav"]

transcriptions = model.transcribe(audio_paths)
```

Writing your own inference script:

```python
import torch
import librosa
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

LANG_ID = "it"
MODEL_ID = "jonatasgrosman/wav2vec2-large-xlsr-53-italian"
SAMPLES = 10

test_dataset = load_dataset("common_voice", LANG_ID, split=f"test[:{SAMPLES}]")

processor = Wav2Vec2Processor.from_pretrained(MODEL_ID)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_ID)

# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = librosa.load(batch["path"], sr=16_000)
    batch["speech"] = speech_array
    batch["sentence"] = batch["sentence"].upper()
    return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)
inputs = processor(test_dataset["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():
    logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)
predicted_sentences = processor.batch_decode(predicted_ids)

for i, predicted_sentence in enumerate(predicted_sentences):
    print("-" * 100)
    print("Reference:", test_dataset[i]["sentence"])
    print("Prediction:", predicted_sentence)
```

| Reference  | Prediction |
| ------------- | ------------- |
| POI LEI MORÌ. | POI LEI MORÌ |
| IL LIBRO HA SUSCITATO MOLTE POLEMICHE A CAUSA DEI SUOI CONTENUTI. | IL LIBRO HA SUSCITATO MOLTE POLEMICHE A CAUSA DEI SUOI CONTENUTI |
| "FIN DALL'INIZIO LA SEDE EPISCOPALE È STATA IMMEDIATAMENTE SOGGETTA ALLA SANTA SEDE." | FIN DALL'INIZIO LA SEDE EPISCOPALE È STATA IMMEDIATAMENTE SOGGETTA ALLA SANTA SEDE |
| IL VUOTO ASSOLUTO? | IL VUOTO ASSOLUTO |
| DOPO ALCUNI ANNI, EGLI DECISE DI TORNARE IN INDIA PER RACCOGLIERE ALTRI INSEGNAMENTI. | DOPO ALCUNI ANNI EGLI DECISE DI TORNARE IN INDIA PER RACCOGLIERE ALTRI INSEGNAMENTI |
| SALVATION SUE | SALVATION SOO |
| IN QUESTO MODO, DECIO OTTENNE IL POTERE IMPERIALE. | IN QUESTO MODO DECHO OTTENNE IL POTERE IMPERIALE |
| SPARTA NOVARA ACQUISISCE IL TITOLO SPORTIVO PER GIOCARE IN PRIMA CATEGORIA. | PARCANOVARACFILISCE IL TITOLO SPORTIVO PER GIOCARE IN PRIMA CATEGORIA |
| IN SEGUITO, KYGO E SHEAR HANNO PROPOSTO DI CONTINUARE A LAVORARE SULLA CANZONE. | IN SEGUITO KIGO E SHIAR HANNO PROPOSTO DI CONTINUARE A LAVORARE SULLA CANZONE |
| ALAN CLARKE | ALAN CLARK |

## Evaluation

1. To evaluate on `mozilla-foundation/common_voice_6_0` with split `test`

```bash
python eval.py --model_id jonatasgrosman/wav2vec2-large-xlsr-53-italian --dataset mozilla-foundation/common_voice_6_0 --config it --split test
```

2. To evaluate on `speech-recognition-community-v2/dev_data`

```bash
python eval.py --model_id jonatasgrosman/wav2vec2-large-xlsr-53-italian --dataset speech-recognition-community-v2/dev_data --config it --split validation --chunk_length_s 5.0 --stride_length_s 1.0
```

## Citation
If you want to cite this model you can use this:

```bibtex
@misc{grosman2021xlsr53-large-italian,
  title={Fine-tuned {XLSR}-53 large model for speech recognition in {I}talian},
  author={Grosman, Jonatas},
  howpublished={\url{https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-italian}},
  year={2021}
}
```
