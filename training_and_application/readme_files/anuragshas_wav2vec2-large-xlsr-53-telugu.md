---
language: te
datasets:
- openslr
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: Anurag Singh XLSR Wav2Vec2 Large 53 Telugu
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: OpenSLR te
      type: openslr
      args: te
    metrics:
       - name: Test WER
         type: wer
         value: 44.98
---
# Wav2Vec2-Large-XLSR-53-Telugu
Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on Telugu using the [OpenSLR SLR66](http://openslr.org/66/) dataset.
When using this model, make sure that your speech input is sampled at 16kHz.
## Usage
The model can be used directly (without a language model) as follows:
```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import pandas as pd
# Evaluation notebook contains the procedure to download the data
df = pd.read_csv("/content/te/test.tsv", sep="\t")
df["path"] = "/content/te/clips/" + df["path"]
test_dataset = Dataset.from_pandas(df)
processor = Wav2Vec2Processor.from_pretrained("anuragshas/wav2vec2-large-xlsr-53-telugu")
model = Wav2Vec2ForCTC.from_pretrained("anuragshas/wav2vec2-large-xlsr-53-telugu") 
resampler = torchaudio.transforms.Resample(48_000, 16_000)
# Preprocessing the datasets.
# We need to read the aduio files as arrays
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
```python
import torch
import torchaudio
from datasets import Dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re
from sklearn.model_selection import train_test_split
import pandas as pd
# Evaluation notebook contains the procedure to download the data
df = pd.read_csv("/content/te/test.tsv", sep="\t")
df["path"] = "/content/te/clips/" + df["path"]
test_dataset = Dataset.from_pandas(df)
wer = load_metric("wer")
processor = Wav2Vec2Processor.from_pretrained("anuragshas/wav2vec2-large-xlsr-53-telugu")
model = Wav2Vec2ForCTC.from_pretrained("anuragshas/wav2vec2-large-xlsr-53-telugu") 
model.to("cuda")
chars_to_ignore_regex = '[\,\?\.\!\-\_\;\:\"\“\%\‘\”\।\’\'\&]'
resampler = torchaudio.transforms.Resample(48_000, 16_000)
def normalizer(text):
    # Use your custom normalizer
    text = text.replace("\\n","\n")
    text = ' '.join(text.split())
    text = re.sub(r'''([a-z]+)''','',text,flags=re.IGNORECASE)
    text = re.sub(r'''%'''," శాతం ", text)
    text = re.sub(r'''(/|-|_)'''," ", text)
    text = re.sub("ై","ై", text)
    text = text.strip()
    return text
def speech_file_to_array_fn(batch):
    batch["sentence"] = normalizer(batch["sentence"])
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()+ " "
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = resampler(speech_array).squeeze().numpy()
    return batch
test_dataset = test_dataset.map(speech_file_to_array_fn)
# Preprocessing the datasets.
# We need to read the aduio files as arrays
def evaluate(batch):
    inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)
    with torch.no_grad():
        logits = model(inputs.input_values.to("cuda"), attention_mask=inputs.attention_mask.to("cuda")).logits
    pred_ids = torch.argmax(logits, dim=-1)
    batch["pred_strings"] = processor.batch_decode(pred_ids)
    return batch
result = test_dataset.map(evaluate, batched=True, batch_size=8)
print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))
```

**Test Result**: 44.98%
## Training
70% of the OpenSLR Telugu dataset was used for training.

Train Split of annotations is [here](https://www.dropbox.com/s/xqc0wtour7f9h4c/train.tsv)

Test Split of annotations is [here](https://www.dropbox.com/s/qw1uy63oj4qdiu4/test.tsv)

Training Data Preparation notebook can be found [here](https://colab.research.google.com/drive/1_VR1QtY9qoiabyXBdJcOI29-xIKGdIzU?usp=sharing)

Training notebook can be found[here](https://colab.research.google.com/drive/14N-j4m0Ng_oktPEBN5wiUhDDbyrKYt8I?usp=sharing)

Evaluation notebook is [here](https://colab.research.google.com/drive/1SLEvbTWBwecIRTNqpQ0fFTqmr1-7MnSI?usp=sharing)