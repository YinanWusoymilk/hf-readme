---
language: fa
datasets:
- ShEMO
tags:
- audio
- automatic-speech-recognition
- speech
- speech-emotion-recognition
license: apache-2.0
---

# Emotion Recognition in Persian (Farsi - fa) Speech using Wav2Vec 2.0


## How to use

### Requirements

```bash
# requirement packages
!pip install git+https://github.com/huggingface/datasets.git
!pip install git+https://github.com/huggingface/transformers.git
!pip install torchaudio
!pip install librosa
```

### Prediction

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchaudio
from transformers import AutoConfig, Wav2Vec2FeatureExtractor

import librosa
import IPython.display as ipd
import numpy as np
import pandas as pd
```

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name_or_path = "m3hrdadfi/wav2vec2-xlsr-persian-speech-emotion-recognition"
config = AutoConfig.from_pretrained(model_name_or_path)
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(model_name_or_path)
sampling_rate = feature_extractor.sampling_rate
model = Wav2Vec2ForSpeechClassification.from_pretrained(model_name_or_path).to(device)
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
path = "/path/to/sadness.wav"
outputs = predict(path, sampling_rate)
```

```bash
[
{'Label': 'Anger', 'Score': '0.0%'},
{'Label': 'Fear', 'Score': '0.0%'},
{'Label': 'Happiness', 'Score': '0.0%'},
{'Label': 'Neutral', 'Score': '0.0%'},
{'Label': 'Sadness', 'Score': '99.9%'},
{'Label': 'Surprise', 'Score': '0.0%'}
]
```


## Evaluation
The following tables summarize the scores obtained by model overall and per each class.


|  Emotions | precision | recall | f1-score | accuracy |
|:---------:|:---------:|:------:|:--------:|:--------:|
|   Anger   |    0.95   |  0.95  |   0.95   |          |
|    Fear   |    0.33   |  0.17  |   0.22   |          |
| Happiness |    0.69   |  0.69  |   0.69   |          |
|  Neutral  |    0.91   |  0.94  |   0.93   |          |
|  Sadness  |    0.92   |  0.85  |   0.88   |          |
|  Surprise |    0.81   |  0.88  |   0.84   |          |
|           |           |        |  Overal  |   0.90   |


## Questions?
Post a Github issue from [HERE](https://github.com/m3hrdadfi/soxan/issues).