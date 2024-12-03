---
license: cc-by-4.0
pipeline_tag: text-to-speech
---
Download [F5-TTS](https://huggingface.co/SWivid/F5-TTS/tree/main/F5TTS_Base) or [E2 TTS](https://huggingface.co/SWivid/F5-TTS/tree/main/E2TTS_Base) and place under ckpts/
```
ckpts/
    E2TTS_Base/
        model_1200000.pt
    F5TTS_Base/
        model_1200000.pt
```
Inference with .safetensors option
```
ckpts/
    E2TTS_Base/
        model_1200000.safetensors
    F5TTS_Base/
        model_1200000.safetensors
```
Github: https://github.com/SWivid/F5-TTS      
Paper: [F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching](https://huggingface.co/papers/2410.06885)
