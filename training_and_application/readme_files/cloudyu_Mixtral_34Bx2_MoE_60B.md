---
license: apache-2.0
tags:
- yi
- moe
model-index:
- name: Mixtral_34Bx2_MoE_60B
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
      value: 45.38
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cloudyu/Mixtral_34Bx2_MoE_60B
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
      value: 41.21
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cloudyu/Mixtral_34Bx2_MoE_60B
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
      value: 6.57
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cloudyu/Mixtral_34Bx2_MoE_60B
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
      value: 11.74
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cloudyu/Mixtral_34Bx2_MoE_60B
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
      value: 17.78
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cloudyu/Mixtral_34Bx2_MoE_60B
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
      value: 41.85
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=cloudyu/Mixtral_34Bx2_MoE_60B
      name: Open LLM Leaderboard
---

# Mixtral  MOE  2x34B

* [One of Best Model reviewed by reddit community](https://www.reddit.com/r/LocalLLaMA/comments/1916896/llm_comparisontest_confirm_leaderboard_big_news/)
* [Another review by reddit community](https://www.reddit.com/r/LocalLLaMA/comments/191mvlp/i_have_tried_mixtral_34bx2_moe_also_named_yi/)

Highest score Model ranked by Open LLM Leaderboard (2024-01-10)
* [Average Score 76.66](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

This is my first English & Chinese MoE Model based on
* [jondurbin/bagel-dpo-34b-v0.2]
* [SUSTech/SUS-Chat-34B]


# [New Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_cloudyu__Mixtral_34Bx2_MoE_60B)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |27.42|
|IFEval (0-Shot)    |45.38|
|BBH (3-Shot)       |41.21|
|MATH Lvl 5 (4-Shot)| 6.57|
|GPQA (0-shot)      |11.74|
|MuSR (0-shot)      |17.78|
|MMLU-PRO (5-shot)  |41.85|

# [Old New Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_cloudyu__Mixtral_34Bx2_MoE_60B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |76.66|
|AI2 Reasoning Challenge (25-Shot)|71.33|
|HellaSwag (10-Shot)              |85.25|
|MMLU (5-Shot)                    |77.34|
|TruthfulQA (0-shot)              |66.59|
|Winogrande (5-shot)              |84.85|
|GSM8k (5-shot)                   |74.60|

gpu code example

```
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import math

## v2 models
model_path = "cloudyu/Mixtral_34Bx2_MoE_60B"

tokenizer = AutoTokenizer.from_pretrained(model_path, use_default_system_prompt=False)
model = AutoModelForCausalLM.from_pretrained(
    model_path, torch_dtype=torch.float32, device_map='auto',local_files_only=False, load_in_4bit=True
)
print(model)
prompt = input("please input prompt:")
while len(prompt) > 0:
  input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("cuda")

  generation_output = model.generate(
    input_ids=input_ids, max_new_tokens=500,repetition_penalty=1.2
  )
  print(tokenizer.decode(generation_output[0]))
  prompt = input("please input prompt:")
```

CPU example

```
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import math

## v2 models
model_path = "cloudyu/Mixtral_34Bx2_MoE_60B"

tokenizer = AutoTokenizer.from_pretrained(model_path, use_default_system_prompt=False)
model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.bfloat16, device_map='cpu'
)
print(model)
prompt = input("please input prompt:")
while len(prompt) > 0:
  input_ids = tokenizer(prompt, return_tensors="pt").input_ids

  generation_output = model.generate(
    input_ids=input_ids, max_new_tokens=500,repetition_penalty=1.2
  )
  print(tokenizer.decode(generation_output[0]))
  prompt = input("please input prompt:")

```

Output Examples:
```
please input prompt:write a story about yosemite
write a story about yosemite national park
Yosemite National Park is located in the Sierra Nevada Mountains of California, USA. It was established on October 1st, 1890 and covers an area of approximately 747,956 acres (302,687 hectares). The park boasts some of America's most iconic natural wonders such as Yosemite Valley, Half Dome, El Capitan, Bridalveil Fall, Tuolumne Meadows, Glacier Point, Mariposa Grove, and many more breathtaking landscapes that attract millions of visitors each year.

The history of Yosemite dates back to over seven million years ago when glaciers carved out its stunning granite cliffs and valleys. Native American tribes like Miwok and Paiute have lived here for thousands of years before European explorers arrived during the mid-nineteenth century. In fact, it was John Muir - one of America’s greatest conservationists who helped establish this region as a protected wilderness area by advocating for its preservation through his writings and activism.

Today, Yosemite offers various recreational activities including hiking, rock climbing, camping, fishing, horseback riding, wildlife watching, photography, and winter sports like skiing and snowshoeing. Visitors can also enjoy ranger programs, guided tours, educational exhibits at visitor centers, or simply take time to appreciate nature while strolling along scenic trails surrounded by towering sequoia trees, cascading waterfalls, and crystal clear lakes.

In addition to preserving these awe-inspiring vistas, Yosemite plays a crucial role in protecting numerous plant and animal species found within its boundaries. Some notable inhabitants include black bears, mountain lions, mule deer, coyotes, bobcats, golden eagles, peregrine falcons, bighorn sheep, and several types of fish native to the Merced River which runs through the heart of the valley.

As we continue our journey into the future, let us remember the importance of safeguarding places like Yosemite so they may remain pristine sanctuaries where both humans and animals alike can thrive together amidst unspoiled beauty.</s>
please input prompt:李开复是谁？
李开复是谁？
他是一个在人工智能领域有着卓越贡献的科学家，也是一位成功的企业家。他的名字与谷歌、微软等科技巨头紧密相连，他是创新工场的创始人之一，更是无数创业者心中的偶像和导师。然而，除了这些耀眼的光环之外，李开复还有着怎样的故事呢？让我们一起来揭秘这位传奇人物的人生历程吧！</s>
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_cloudyu__Mixtral_34Bx2_MoE_60B)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |27.42|
|IFEval (0-Shot)    |45.38|
|BBH (3-Shot)       |41.21|
|MATH Lvl 5 (4-Shot)| 6.57|
|GPQA (0-shot)      |11.74|
|MuSR (0-shot)      |17.78|
|MMLU-PRO (5-shot)  |41.85|

