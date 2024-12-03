---
language: ro
datasets:
- common_voice
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: Romanian XLSR Wav2Vec2 Large 53 by Anton Lozhkov
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice ro
      type: common_voice
      args: ro
    metrics:
       - name: Test WER
         type: wer
         value: 24.84
---

# Wav2Vec2-Large-XLSR-53-Romanian

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on Romanian using the [Common Voice](https://huggingface.co/datasets/common_voice) dataset.
When using this model, make sure that your speech input is sampled at 16kHz.

## Usage

The model can be used directly (without a language model) as follows:

```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

test_dataset = load_dataset("common_voice", "ro", split="test[:2%]")

processor = Wav2Vec2Processor.from_pretrained("anton-l/wav2vec2-large-xlsr-53-romanian")
model = Wav2Vec2ForCTC.from_pretrained("anton-l/wav2vec2-large-xlsr-53-romanian")

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = resampler(speech_array).squeeze().numpy()
    return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)
inputs = processor(test_dataset["speech"][:2], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():
    logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)

print("Prediction:", processor.batch_decode(predicted_ids))
print("Reference:", test_dataset["sentence"][:2])
```


## Evaluation

The model can be evaluated as follows on the Romanian test data of Common Voice.

```python
import torch
import torchaudio
import urllib.request
import tarfile
import pandas as pd
from tqdm.auto import tqdm
from datasets import load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# Download the raw data instead of using HF datasets to save disk space 
data_url = "https://voice-prod-bundler-ee1969a6ce8178826482b88e843c335139bd3fb4.s3.amazonaws.com/cv-corpus-6.1-2020-12-11/ro.tar.gz"
filestream = urllib.request.urlopen(data_url)
data_file = tarfile.open(fileobj=filestream, mode="r|gz")
data_file.extractall()

wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("anton-l/wav2vec2-large-xlsr-53-romanian")
model = Wav2Vec2ForCTC.from_pretrained("anton-l/wav2vec2-large-xlsr-53-romanian")
model.to("cuda")

cv_test = pd.read_csv("cv-corpus-6.1-2020-12-11/ro/test.tsv", sep='\t')
clips_path = "cv-corpus-6.1-2020-12-11/ro/clips/"

def clean_sentence(sent):
    sent = sent.lower()
    # replace non-alpha characters with space
    sent = "".join(ch if ch.isalpha() else " " for ch in sent)
    # remove repeated spaces
    sent = " ".join(sent.split())
    return sent

targets = []
preds = []

for i, row in tqdm(cv_test.iterrows(), total=cv_test.shape[0]):
    row["sentence"] = clean_sentence(row["sentence"])
    speech_array, sampling_rate = torchaudio.load(clips_path + row["path"])
    resampler = torchaudio.transforms.Resample(sampling_rate, 16_000)
    row["speech"] = resampler(speech_array).squeeze().numpy()

    inputs = processor(row["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

    with torch.no_grad():
        logits = model(inputs.input_values.to("cuda"), attention_mask=inputs.attention_mask.to("cuda")).logits

    pred_ids = torch.argmax(logits, dim=-1)

    targets.append(row["sentence"])
    preds.append(processor.batch_decode(pred_ids)[0])

print("WER: {:2f}".format(100 * wer.compute(predictions=preds, references=targets)))
```

**Test Result**: 24.84 %  


## Training

The Common Voice `train` and `validation` datasets were used for training.

