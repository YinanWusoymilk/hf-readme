---
license: apache-2.0
metrics:
- cer
---
## Welcome
If you find this model helpful, please *like* this model and star us on https://github.com/LianjiaTech/BELLE  and https://github.com/shuaijiang/Whisper-Finetune

# Belle-whisper-large-v3-zh
Fine tune whisper-large-v3 to enhance Chinese speech recognition capabilities, 
Belle-whisper-large-v3-zh demonstrates a **24-65%** relative improvement in performance on Chinese ASR benchmarks, including AISHELL1, AISHELL2, WENETSPEECH, and HKUST.


## Usage
```python

from transformers import pipeline

transcriber = pipeline(
  "automatic-speech-recognition", 
  model="BELLE-2/Belle-whisper-large-v3-zh"
)

transcriber.model.config.forced_decoder_ids = (
  transcriber.tokenizer.get_decoder_prompt_ids(
    language="zh", 
    task="transcribe"
  )
)

transcription = transcriber("my_audio.wav") 

```

## Fine-tuning
|       Model      |  (Re)Sample Rate   |                      Train Datasets         | Fine-tuning (full or peft) | 
|:----------------:|:-------:|:----------------------------------------------------------:|:-----------:|
| Belle-whisper-large-v3-zh | 16KHz | [AISHELL-1](https://openslr.magicdatatech.com/resources/33/) [AISHELL-2](https://www.aishelltech.com/aishell_2) [WenetSpeech](https://wenet.org.cn/WenetSpeech/) [HKUST](https://catalog.ldc.upenn.edu/LDC2005S15)  |   [full fine-tuning](https://github.com/shuaijiang/Whisper-Finetune)   |    

If you want to fine-thuning the model on your datasets, please reference to the [github repo](https://github.com/shuaijiang/Whisper-Finetune)

    
## CER(%) ↓ 
|      Model       |  Language Tag   | aishell_1_test(↓) |aishell_2_test(↓)| wenetspeech_net(↓) | wenetspeech_meeting(↓) | HKUST_dev(↓)|   
|:----------------:|:-------:|:-----------:|:-----------:|:--------:|:-----------:|:-------:|
| whisper-large-v3 | Chinese |  8.085 | 5.475  |  11.72   |  20.15 | 28.597 |
| Belle-whisper-large-v2-zh | Chinese |   2.549    | 3.746  |   8.503    | 14.598 | 16.289 |
| Belle-whisper-large-v3-zh | Chinese |   2.781    | 3.786  |   8.865    | **11.246** | 16.440 |

It is worth mentioning that compared to Belle-whisper-large-v2-zh, Belle-whisper-large-v3-zh has a significant improvement in complex acoustic scenes(such as wenetspeech_meeting).

## Citation

Please cite our paper and github when using our code, data or model.

```
@misc{BELLE,
  author = {BELLEGroup},
  title = {BELLE: Be Everyone's Large Language model Engine},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/LianjiaTech/BELLE}},
}
```