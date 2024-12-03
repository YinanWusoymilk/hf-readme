---
language: fa
datasets:
- shemo
tags:
- audio
- speech
- speech-gender-recognition
license: apache-2.0
---

# Emotion Recognition in Persian (fa) Speech using HuBERT


## How to use

### Requirements

```bash
# requirement packages
!pip install git+https://github.com/huggingface/datasets.git
!pip install git+https://github.com/huggingface/transformers.git
!pip install torchaudio
!pip install librosa
```

```bash
!git clone https://github.com/m3hrdadfi/soxan.git .
```

### Prediction

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchaudio
from transformers import AutoConfig, Wav2Vec2FeatureExtractor
from src.models import Wav2Vec2ForSpeechClassification, HubertForSpeechClassification

import librosa
import IPython.display as ipd
import numpy as np
import pandas as pd
```

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name_or_path = "m3hrdadfi/hubert-base-persian-speech-gender-recognition"
config = AutoConfig.from_pretrained(model_name_or_path)
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(model_name_or_path)
sampling_rate = feature_extractor.sampling_rate
model = HubertForSpeechClassification.from_pretrained(model_name_or_path).to(device)
```

```python
def speech_file_to_array_fn(path, sampling_rate):
    speech_array, _sampling_rate = torchaudio.load(path)
    resampler = torchaudio.transforms.Resample(_sampling_rate)
    speech = resampler(speech_array).squeeze().numpy()
    return speech


def predict(path, sampling_rate):
    speech = speech_file_to_array_fn(path, sampling_rate)
    inputs = feature_extractor(speech, sampling_rate=sampling_rate, return_tensors="pt", padding=True)
    inputs = {key: inputs[key].to(device) for key in inputs}

    with torch.no_grad():
        logits = model(**inputs).logits

    scores = F.softmax(logits, dim=1).detach().cpu().numpy()[0]
    outputs = [{"Label": config.id2label[i], "Score": f"{round(score * 100, 3):.1f}%"} for i, score in enumerate(scores)]
    return outputs
```

```python
path = "/path/to/female.wav"
outputs = predict(path, sampling_rate)
```

```bash
[{'Label': 'F', 'Score': '98.2%'}, {'Label': 'M', 'Score': '1.8%'}]
```


## Evaluation
The following tables summarize the scores obtained by model overall and per each class.


| Emotions | precision | recall | f1-score | accuracy |
|----------|-----------|--------|----------|----------|
| F        | 0.98      | 0.97   | 0.98     |          |
| M        | 0.98      | 0.99   | 0.98     |          |
|          |           |        | Overal   | 0.98     |


## Questions?
Post a Github issue from [HERE](https://github.com/m3hrdadfi/soxan/issues).