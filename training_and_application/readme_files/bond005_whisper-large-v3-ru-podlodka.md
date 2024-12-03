---
license: apache-2.0
widget:
- example_title: Нейронные сети - это хорошо!
  src: >-
    https://huggingface.co/bond005/whisper-large-v3-ru-podlodka/resolve/main/test_sound_ru.flac
- example_title: >-
    К сожалению, система распознавания речи не всегда стабильна, особенно в
    шумных условиях.
  src: >-
    https://huggingface.co/bond005/whisper-large-v3-ru-podlodka/resolve/main/test_sound_with_noise.wav
- example_title: >-
    Мимо театра мальчик ходил довольно часто — белое, со взбитыми сливками,
    здание-торт.
  src: >-
    https://huggingface.co/bond005/whisper-large-v3-ru-podlodka/resolve/main/anna_matveeva_test.wav
datasets:
- bond005/taiga_speech_v2
- bond005/podlodka_speech
- bond005/rulibrispeech
language:
- ru
pipeline_tag: automatic-speech-recognition
metrics:
- wer
model-index:
- name: Whisper Large V3 Russian Podlodka by Ivan Bondarenko
  results:
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Podlodka.io
      type: bond005/podlodka_speech
      args: ru
    metrics:
    - name: WER (with punctuation and capital letters)
      type: wer
      value: 20.910
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Podlodka.io
      type: bond005/podlodka_speech
      args: ru
    metrics:
    - name: WER (without punctuation)
      type: wer
      value: 10.987
  - task:
      name: Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Russian Librispeech
      type: bond005/rulibrispeech
      args: ru
    metrics:
    - name: WER (without punctuation)
      type: wer
      value: 9.795
---