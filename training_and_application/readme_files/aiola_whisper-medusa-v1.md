---
license: mit
datasets:
- openslr/librispeech_asr
tags:
- ASR
- Automatic Speech Recognition
- Whisper
- Medusa
- Speech
- Speculative Decoding
---

# Whisper Medusa

Whisper is an advanced encoder-decoder model for speech transcription and 
translation, processing audio through encoding and decoding stages. Given 
its large size and slow inference speed, various optimization strategies like 
Faster-Whisper and Speculative Decoding have been proposed to enhance performance. 
Our Medusa model builds on Whisper by predicting multiple tokens per iteration, 
which significantly improves speed with small degradation in WER. We train and 
evaluate our model on the LibriSpeech dataset, demonstrating speed improvements.

---------

## Training Details
`aiola/whisper-medusa-v1` was trained on the LibriSpeech dataset to perform audio translation. 
The Medusa heads were optimized for English, so for optimal performance and speed improvements, please use English audio only. 

---------

## Usage
To use `whisper-medusa-v1` install [`whisper-medusa`](https://github.com/aiola-lab/whisper-medusa) repo following the README instructions.

Inference can be done using the following code:
```python
import torch
import torchaudio

from whisper_medusa import WhisperMedusaModel
from transformers import WhisperProcessor

model_name = "aiola/whisper-medusa-v1"
model = WhisperMedusaModel.from_pretrained(model_name)
processor = WhisperProcessor.from_pretrained(model_name)

path_to_audio = "path/to/audio.wav"
SAMPLING_RATE = 16000
language = "en"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

input_speech, sr = torchaudio.load(path_to_audio)
if sr != SAMPLING_RATE:
    input_speech = torchaudio.transforms.Resample(sr, SAMPLING_RATE)(input_speech)

input_features = processor(input_speech.squeeze(), return_tensors="pt", sampling_rate=SAMPLING_RATE).input_features
input_features = input_features.to(device)

model = model.to(device)
model_output = model.generate(
    input_features,
    language=language,
)
predict_ids = model_output[0]
pred = processor.decode(predict_ids, skip_special_tokens=True)
print(pred)

```
