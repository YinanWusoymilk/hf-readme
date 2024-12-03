---
language: ml
datasets:
- Indic TTS Malayalam Speech Corpus
- Openslr Malayalam Speech Corpus
- SMC Malayalam Speech Corpus
- IIIT-H Indic Speech Databases
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- speech
- xlsr-fine-tuning-week
license: apache-2.0
model-index:
- name: Malayalam XLSR Wav2Vec2 Large 53
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Test split of combined dataset using all datasets mentioned above
      type: custom
      args: ml
    metrics:
       - name: Test WER
         type: wer
         value: 28.43
---

# Wav2Vec2-Large-XLSR-53-ml

Fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on ml (Malayalam) using the [Indic TTS Malayalam Speech Corpus (via Kaggle)](https://www.kaggle.com/kavyamanohar/indic-tts-malayalam-speech-corpus), [Openslr Malayalam Speech Corpus](http://openslr.org/63/), [SMC Malayalam Speech Corpus](https://blog.smc.org.in/malayalam-speech-corpus/) and [IIIT-H Indic Speech Databases](http://speech.iiit.ac.in/index.php/research-svl/69.html). The notebooks used to train model are available [here](https://github.com/gauthamsuresh09/wav2vec2-large-xlsr-53-malayalam/). When using this model, make sure that your speech input is sampled at 16kHz.

## Usage

The model can be used directly (without a language model) as follows:

```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

test_dataset = <load-test-split-of-combined-dataset> # Details on loading this dataset in the evaluation section

processor = Wav2Vec2Processor.from_pretrained("gvs/wav2vec2-large-xlsr-malayalam")
model = Wav2Vec2ForCTC.from_pretrained("gvs/wav2vec2-large-xlsr-malayalam")

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
print("Reference:", test_dataset["sentence"])
```


## Evaluation

The model can be evaluated as follows on the test data of combined custom dataset. For more details on dataset preparation, check the notebooks mentioned at the end of this file.


```python
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re
from datasets import load_dataset, load_metric
from pathlib import Path

# The custom dataset needs to be created using notebook mentioned at the end of this file
data_dir = Path('<path-to-custom-dataset>')

dataset_folders = {
    'iiit': 'iiit_mal_abi',
    'openslr': 'openslr',
    'indic-tts': 'indic-tts-ml',
    'msc-reviewed': 'msc-reviewed-speech-v1.0+20200825',
}

# Set directories for datasets
openslr_male_dir = data_dir / dataset_folders['openslr'] / 'male'
openslr_female_dir = data_dir / dataset_folders['openslr'] / 'female'
iiit_dir = data_dir / dataset_folders['iiit']
indic_tts_male_dir = data_dir / dataset_folders['indic-tts'] / 'male'
indic_tts_female_dir = data_dir / dataset_folders['indic-tts'] / 'female'
msc_reviewed_dir = data_dir / dataset_folders['msc-reviewed']

# Load the datasets
openslr_male = load_dataset("json", data_files=[f"{str(openslr_male_dir.absolute())}/sample_{i}.json" for i in range(2023)], split="train")
openslr_female = load_dataset("json", data_files=[f"{str(openslr_female_dir.absolute())}/sample_{i}.json" for i in range(2103)], split="train")
iiit = load_dataset("json", data_files=[f"{str(iiit_dir.absolute())}/sample_{i}.json" for i in range(1000)], split="train")
indic_tts_male = load_dataset("json", data_files=[f"{str(indic_tts_male_dir.absolute())}/sample_{i}.json" for i in range(5649)], split="train")
indic_tts_female = load_dataset("json", data_files=[f"{str(indic_tts_female_dir.absolute())}/sample_{i}.json" for i in range(2950)], split="train")
msc_reviewed = load_dataset("json", data_files=[f"{str(msc_reviewed_dir.absolute())}/sample_{i}.json" for i in range(1541)], split="train")

# Create test split as 20%, set random seed as well.
test_size = 0.2
random_seed=1
openslr_male_splits = openslr_male.train_test_split(test_size=test_size, seed=random_seed)
openslr_female_splits = openslr_female.train_test_split(test_size=test_size, seed=random_seed)
iiit_splits = iiit.train_test_split(test_size=test_size, seed=random_seed)
indic_tts_male_splits = indic_tts_male.train_test_split(test_size=test_size, seed=random_seed)
indic_tts_female_splits = indic_tts_female.train_test_split(test_size=test_size, seed=random_seed)
msc_reviewed_splits = msc_reviewed.train_test_split(test_size=test_size, seed=random_seed)

# Get combined test dataset
split_list = [openslr_male_splits, openslr_female_splits, indic_tts_male_splits, indic_tts_female_splits, msc_reviewed_splits, iiit_splits]
test_dataset = datasets.concatenate_datasets([split['test'] for split in split_list)

wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("gvs/wav2vec2-large-xlsr-malayalam") 
model = Wav2Vec2ForCTC.from_pretrained("gvs/wav2vec2-large-xlsr-malayalam")
model.to("cuda")

resamplers = {
    48000: torchaudio.transforms.Resample(48_000, 16_000),
}

chars_to_ignore_regex = '[\\\\,\\\\?\\\\.\\\\!\\\\-\\\\;\\\\:\\\\"\\\\“\\\\%\\\\‘\\\\”\\\\�Utrnle\\\\_]'
unicode_ignore_regex = r'[\\\\u200e]'

# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"])
    batch["sentence"] = re.sub(unicode_ignore_regex, '', batch["sentence"])
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    # Resample if its not in 16kHz
    if sampling_rate != 16000:
        batch["speech"] = resamplers[sampling_rate](speech_array).squeeze().numpy()
    else:
        batch["speech"] = speech_array.squeeze().numpy()
    # If more than one dimension is present, pick first one
    if batch["speech"].ndim > 1:
        batch["speech"] = batch["speech"][0]
    return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)

# Preprocessing the datasets.
# We need to read the audio files as arrays
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

**Test Result (WER)**: 28.43 %  


## Training

A combined dataset was created using [Indic TTS Malayalam Speech Corpus (via Kaggle)](https://www.kaggle.com/kavyamanohar/indic-tts-malayalam-speech-corpus), [Openslr Malayalam Speech Corpus](http://openslr.org/63/), [SMC Malayalam Speech Corpus](https://blog.smc.org.in/malayalam-speech-corpus/) and [IIIT-H Indic Speech Databases](http://speech.iiit.ac.in/index.php/research-svl/69.html). The datasets were downloaded and was converted to HF Dataset format using [this notebook](https://github.com/gauthamsuresh09/wav2vec2-large-xlsr-53-malayalam/blob/main/make_hf_dataset.ipynb)

The notebook used for training and evaluation can be found [here](https://github.com/gauthamsuresh09/wav2vec2-large-xlsr-53-malayalam/blob/main/fine-tune-xlsr-wav2vec2-on-malayalam-asr-with-transformers_v2.ipynb)