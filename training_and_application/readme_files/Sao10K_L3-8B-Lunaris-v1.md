---
license: llama3
language:
- en
---

A generalist / roleplaying model merge based on Llama 3. Models are selected from my personal experience while using them.

I personally think this is an improvement over Stheno v3.2, considering the other models helped balance out its creativity and at the same time improving its logic.

Settings:
```
Instruct // Context Template: Llama-3-Instruct
Temperature: 1.4
min_p: 0.1
```

---

Merging seems to be a black box magic though? In my personal experience merging multiple models from different datasets / data works better than combining them all in one.

*Values chosen are from long-running personal experimentation since Llama-2 Merging Era. I have tweaked them to fit this recipe.*

Mergekit Config 
```
models:
  - model: meta-llama/Meta-Llama-3-8B-Instruct
  - model: crestf411/L3-8B-sunfall-v0.1 # Another RP Model trained on... stuff
    parameters:
      density: 0.4
      weight: 0.25
  - model: Hastagaras/Jamet-8B-L3-MK1 - # Another RP / Storytelling Model
    parameters:
      density: 0.5
      weight: 0.3
  - model: maldv/badger-iota-llama-3-8b #Megamerge - Helps with General Knowledge
    parameters:
      density: 0.6
      weight: 0.35
  - model: Sao10K/Stheno-3.2-Beta # This is Stheno v3.2's Initial Name
    parameters:
      density: 0.7
      weight: 0.4
merge_method: ties
base_model: meta-llama/Meta-Llama-3-8B-Instruct
parameters:
  int8_mask: true
  rescale: true
  normalize: false
dtype: bfloat16
```