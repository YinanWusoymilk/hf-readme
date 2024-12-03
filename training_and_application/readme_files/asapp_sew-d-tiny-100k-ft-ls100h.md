---
language: en
datasets:
- librispeech_asr
tags:
- audio
- speech
- automatic-speech-recognition
- hf-asr-leaderboard
license: apache-2.0
widget:
- example_title: Librispeech sample 1
  src: https://cdn-media.huggingface.co/speech_samples/sample1.flac
- example_title: Librispeech sample 2
  src: https://cdn-media.huggingface.co/speech_samples/sample2.flac
model-index:
- name: sew-d-tiny-100k-ft-ls100h
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: LibriSpeech (clean)
      type: librispeech_asr
      config: clean
      split: test
      args: 
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 10.47
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: LibriSpeech (other)
      type: librispeech_asr
      config: other
      split: test
      args: 
        language: en
    metrics:
    - name: Test WER
      type: wer
      value: 22.73
---

# SEW-D-tiny

[SEW-D by ASAPP Research](https://github.com/asappresearch/sew)

The base model pretrained on 16kHz sampled speech audio. When using the model make sure that your speech input is also sampled at 16Khz. Note that this model should be fine-tuned on a downstream task, like Automatic Speech Recognition, Speaker Identification, Intent Classification, Emotion Recognition, etc...

Paper: [Performance-Efficiency Trade-offs in Unsupervised Pre-training for Speech Recognition](https://arxiv.org/abs/2109.06870)

Authors: Felix Wu, Kwangyoun Kim, Jing Pan, Kyu Han, Kilian Q. Weinberger, Yoav Artzi

**Abstract**
This paper is a study of performance-efficiency trade-offs in pre-trained models for automatic speech recognition (ASR). We focus on wav2vec 2.0, and formalize several architecture designs that influence both the model performance and its efficiency. Putting together all our observations, we introduce SEW (Squeezed and Efficient Wav2vec), a pre-trained model architecture with significant improvements along both performance and efficiency dimensions across a variety of training setups. For example, under the 100h-960h semi-supervised setup on LibriSpeech, SEW achieves a 1.9x inference speedup compared to wav2vec 2.0, with a 13.5% relative reduction in word error rate. With a similar inference time, SEW reduces word error rate by 25-50% across different model sizes.

The original model can be found under https://github.com/asappresearch/sew#model-checkpoints .

# Usage
To transcribe audio files the model can be used as a standalone acoustic model as follows:
```python
from transformers import Wav2Vec2Processor, SEWDForCTC
from datasets import load_dataset
import soundfile as sf
import torch
 
# load the model and preprocessor
processor = Wav2Vec2Processor.from_pretrained("asapp/sew-d-tiny-100k-ft-ls100h")
model = SEWDForCTC.from_pretrained("asapp/sew-d-tiny-100k-ft-ls100h")

# load the dummy dataset with speech samples
ds = load_dataset("patrickvonplaten/librispeech_asr_dummy", "clean", split="validation")
 
# preprocess
input_values = processor(ds[0]["audio"]["array"], return_tensors="pt").input_values  # Batch size 1

# retrieve logits
logits = model(input_values).logits
 
# take argmax and decode
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)
 ```

 ## Evaluation
 
 This code snippet shows how to evaluate **asapp/sew-d-tiny-100k-ft-ls100h** on LibriSpeech's "clean" and "other" test data.
 
```python
from datasets import load_dataset
from transformers import SEWDForCTC, Wav2Vec2Processor
import torch
from jiwer import wer

librispeech_eval = load_dataset("librispeech_asr", "clean", split="test")

model = SEWDForCTC.from_pretrained("asapp/sew-d-tiny-100k-ft-ls100h").to("cuda")
processor = Wav2Vec2Processor.from_pretrained("asapp/sew-d-tiny-100k-ft-ls100h")

def map_to_pred(batch):
    input_values = processor(batch["audio"][0]["array"], sampling_rate=16000, 
                             return_tensors="pt", padding="longest").input_values
    with torch.no_grad():
        logits = model(input_values.to("cuda")).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    batch["transcription"] = transcription
    return batch

result = librispeech_eval.map(map_to_pred, batched=True, batch_size=1, remove_columns=["audio"])

print("WER:", wer(result["text"], result["transcription"]))
```

*Result (WER)*:

| "clean" | "other" |
| --- | --- |
| 10.47 | 22.73 |
