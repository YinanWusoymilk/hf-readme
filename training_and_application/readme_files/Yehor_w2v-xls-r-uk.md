---
base_model: facebook/wav2vec2-xls-r-300m
language: 
  - uk
license: "apache-2.0"
tags:
- automatic-speech-recognition
datasets:
- mozilla-foundation/common_voice_10_0
metrics:
  - wer
model-index:
  - name: w2v-xls-r-uk
    results:
      - task:
          name: Automatic Speech Recognition
          type: automatic-speech-recognition
        dataset:
          name: common_voice_10_0
          type: common_voice_10_0
          config: uk
          split: test
          args: uk
        metrics:
          - name: Wer
            type: wer
            value: 0.0463
---

🚨🚨🚨 **ATTENTION!** 🚨🚨🚨

**Use an updated model**: https://huggingface.co/Yehor/w2v-bert-uk-v2.1

---

## Community

- Discord: https://discord.gg/yVAjkBgmt4
- Speech Recognition: https://t.me/speech_recognition_uk
- Speech Synthesis: https://t.me/speech_synthesis_uk

## Overview

This model has apostrophes and hyphens.

The language model is trained on the texts of the Common Voice dataset, which is used during training.

Metrics:

| Dataset | CER | WER |
|-|-|-|
| CV7 (no LM) |  0.0432 | 0.2288 |
| CV7 (with LM) | 0.0169 | 0.0706 |
| CV10 (no LM) | 0.0412 | 0.2206 |
| CV10 (with LM) | 0.0118 | 0.0463 |
