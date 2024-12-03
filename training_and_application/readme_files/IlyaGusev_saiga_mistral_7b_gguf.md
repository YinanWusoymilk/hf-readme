---
datasets:
- IlyaGusev/ru_turbo_saiga
- IlyaGusev/ru_sharegpt_cleaned
- IlyaGusev/oasst1_ru_main_branch
- IlyaGusev/ru_turbo_alpaca_evol_instruct
- lksy/ru_instruct_gpt4
language:
- ru
inference: false
pipeline_tag: text-generation
license: apache-2.0
---

Llama.cpp compatible versions of an original [7B model](https://huggingface.co/IlyaGusev/saiga_mistral_7b_lora).

Download one of the versions, for example `model-q4_K.gguf`.
```
wget https://huggingface.co/IlyaGusev/saiga_mistral_7b_gguf/resolve/main/model-q4_K.gguf
```

Download [interact_mistral_llamacpp.py](https://raw.githubusercontent.com/IlyaGusev/rulm/master/self_instruct/src/interact_mistral_llamacpp.py)
```
wget https://raw.githubusercontent.com/IlyaGusev/rulm/master/self_instruct/src/interact_mistral_llamacpp.py
```

How to run:
```
pip install llama-cpp-python fire

python3 interact_mistral_llamacpp.py model-q4_K.gguf
```

System requirements:
* 10GB RAM for q8_0 and less for smaller quantizations
