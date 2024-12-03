---
license: mit
model-index:
- name: RYS-XLarge
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: IFEval (0-Shot)
      type: HuggingFaceH4/ifeval
      args:
        num_few_shot: 0
    metrics:
    - type: inst_level_strict_acc and prompt_level_strict_acc
      value: 79.96
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=dnhkng/RYS-XLarge
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: BBH (3-Shot)
      type: BBH
      args:
        num_few_shot: 3
    metrics:
    - type: acc_norm
      value: 58.77
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=dnhkng/RYS-XLarge
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MATH Lvl 5 (4-Shot)
      type: hendrycks/competition_math
      args:
        num_few_shot: 4
    metrics:
    - type: exact_match
      value: 38.97
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=dnhkng/RYS-XLarge
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GPQA (0-shot)
      type: Idavidrein/gpqa
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 17.9
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=dnhkng/RYS-XLarge
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MuSR (0-shot)
      type: TAUR-Lab/MuSR
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 23.72
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=dnhkng/RYS-XLarge
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU-PRO (5-shot)
      type: TIGER-Lab/MMLU-Pro
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 49.2
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=dnhkng/RYS-XLarge
      name: Open LLM Leaderboard
---

This is a new kind of model optimization. It is based on a new method for the analysis of the functional role of layers within the transformer stack, and on layer duplication (self-merging) to increase intelligence.

### No Weights were modified in this process!

### Model improvement with layer duplication:
|                 | Average | IFEval | BBH  | MATH Lvl 5 | GPQA | MUSR  | MMLU-PRO |
|-----------------|--------:|-------:|-----:|-----------:|-----:|------:|---------:|
| RYS Improvement |    2.61% |  -2.05% | 2.51% |       8.16% | 2.58% | 17.72% |     0.31% |


This model is based on MaziyarPanahi/calme-2.1-qwen2-72b, which in turn was tuned from Qwen2-72B. As this method is orthogonal to fine-tuning, the further finetune from MaziyarPanahi now has the top position:
https://huggingface.co/MaziyarPanahi/calme-2.4-rys-78b


A paper on the technique is currently being written. Currently, all four top models on the leaderboard are based on the RYS method.  Special thanks to my wife, for putting up with me coding in the basement for too many evenings and weekends for months!

This research was supported with hardware from the [appliedAI Institute](https://www.appliedai-institute.de/en/), whose goal is to generate and communicate high-quality knowledge about trustworthy AI.

## Quickstart

Here is a code snippet with `apply_chat_template` to show you how to load the tokenizer and model and how to generate content.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained(
    "dnhkng/RYS-XLarge",
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("dnhkng/RYS-XLarge")

prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_dnhkng__RYS-XLarge)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |44.75|
|IFEval (0-Shot)    |79.96|
|BBH (3-Shot)       |58.77|
|MATH Lvl 5 (4-Shot)|38.97|
|GPQA (0-shot)      |17.90|
|MuSR (0-shot)      |23.72|
|MMLU-PRO (5-shot)  |49.20|


___________________________________
## *ADVERTISING BREAK*

I’m on the hunt for new challenges and a chance to dive into some exciting research opportunities. Oh, and did I mention I just snagged a top spot on the Open LLM leaderboard? 🎉



#### Profile
Innovation enthusiast, AI strategist, and interdisciplinary-tech nerd – that's me! With over a decade of experience in research and project management, my professional journey has been largely shaped by my passion for artificial intelligence and its potential to transform various industries. With a solid background in artificial intelligence and machine learning, coupled with a knack for innovation and problem-solving (and a healthy dose of curiosity), I'm excited to bring my skills to a new team.

Originally from Australia, where I earned my degrees in Organic Chemistry and Biochemistry, I moved to Germany in 2004. My academic pursuit continued with a Ph.D. in Chemistry at the Max Planck Institute of Biochemistry. Today, I leverage my robust educational background and diverse industry experience to drive AI innovations in a wide range of applications. Hobbies? Lots: I've also built the world's most powerful espresso machine and am working to bring [GLaDOS to life](https://github.com/dnhkng/GlaDOS).


___________________________________
I'm based out of Munich, Germany, but I would be interested in working remotely for a team with more compute than my ~~2x 4090s~~ 4x H100s (thanks appliedAI!) 🚀

#### Reach out via [LinkedIn - Dr David Noel Ng](https://www.linkedin.com/in/dnhkng)
