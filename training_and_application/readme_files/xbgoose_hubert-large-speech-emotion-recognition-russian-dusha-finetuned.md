---
language:
- ru
tags:
- SER
- speech
- audio
- russian
license: apache-2.0
pipeline_tag: audio-classification
base_model: facebook/hubert-large-ls960-ft
datasets:
- xbgoose/dusha
---
# HuBERT fine-tuned on DUSHA dataset for speech emotion recognition in russian language

The pre-trained model is this one - [facebook/hubert-large-ls960-ft](https://huggingface.co/facebook/hubert-large-ls960-ft)

The DUSHA dataset used can be found [here](https://github.com/salute-developers/golos/tree/master/dusha#dataset-structure)

# Fine-tuning

Fine-tuned in Google Colab using Pro account with A100 GPU

Freezed all layers exept projector, classifier and all 24 HubertEncoderLayerStableLayerNorm layers

Used half of the train dataset

# Training parameters

- 2 epochs 
- train batch size = 8 
- eval batch size = 8 
- gradient accumulation steps = 4 
- learning rate = 5e-5 without warm up and decay

# Metrics

Achieved 
- accuracy = 0.86 
- balanced = 0.76 
- macro f1 score = 0.81 
on test set, improving accucary and f1 score compared to dataset baseline

# Usage

```python
from transformers import HubertForSequenceClassification, Wav2Vec2FeatureExtractor
import torchaudio
import torch

feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("facebook/hubert-large-ls960-ft")
model = HubertForSequenceClassification.from_pretrained("xbgoose/hubert-speech-emotion-recognition-russian-dusha-finetuned")
num2emotion = {0: 'neutral', 1: 'angry', 2: 'positive', 3: 'sad', 4: 'other'}

filepath = "path/to/audio.wav"

waveform, sample_rate = torchaudio.load(filepath, normalize=True)
transform = torchaudio.transforms.Resample(sample_rate, 16000)
waveform = transform(waveform)

inputs = feature_extractor(
        waveform, 
        sampling_rate=feature_extractor.sampling_rate, 
        return_tensors="pt",
        padding=True,
        max_length=16000 * 10,
        truncation=True
    )

logits = model(inputs['input_values'][0]).logits
predictions = torch.argmax(logits, dim=-1)
predicted_emotion = num2emotion[predictions.numpy()[0]]
print(predicted_emotion)
```