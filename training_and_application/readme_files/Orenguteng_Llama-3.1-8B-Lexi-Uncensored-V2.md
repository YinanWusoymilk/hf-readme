---
license: llama3.1
model-index:
- name: Llama-3.1-8B-Lexi-Uncensored-V2
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
      value: 77.92
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2
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
      value: 29.69
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2
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
      value: 16.92
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2
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
      value: 4.36
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2
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
      value: 7.77
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2
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
      value: 30.9
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Orenguteng/Llama-3.1-8B-Lexi-Uncensored-V2
      name: Open LLM Leaderboard
library_name: transformers
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/644ad182f434a6a63b18eee6/7mnEJyioRzQaWz8xLM4KI.png)

VERSION 2 Update Notes:
---
- More compliant
- Smarter
- For best response, use this system prompt (feel free to expand upon it as you wish):

Think step by step with a logical reasoning and intellectual sense before you provide any response.

- For more uncensored and compliant response, you can expand the system message differently, or simply enter a dot "." as system message.

- IMPORTANT: Upon further investigation, the Q4 seems to have refusal issues sometimes. 
There seems to be some of the fine-tune loss happening due to the quantization. I will look into it for V3. 
Until then, I suggest you run F16 or Q8 if possible.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/644ad182f434a6a63b18eee6/zaHhRjsk3rvo_YewgXV2Z.png)

GENERAL INFO:
---

This model is based on Llama-3.1-8b-Instruct, and is governed by [META LLAMA 3.1 COMMUNITY LICENSE AGREEMENT](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE)

Lexi is uncensored, which makes the model compliant. You are advised to implement your own alignment layer before exposing the model as a service. It will be highly compliant with any requests, even unethical ones. 

You are responsible for any content you create using this model. Please use it responsibly.

Lexi is licensed according to Meta's Llama license. I grant permission for any use, including commercial, that falls within accordance with Meta's Llama-3.1 license.

IMPORTANT:
---
Use the same template as the official Llama 3.1 8B instruct.
System tokens must be present during inference, even if you set an empty system message. If you are unsure, just add a short system message as you wish.

FEEDBACK:
---
If you find any issues or have suggestions for improvements, feel free to leave a review and I will look into it for upcoming improvements and next version.


![image/png](https://cdn-uploads.huggingface.co/production/uploads/644ad182f434a6a63b18eee6/uqJv-R1LeJEfMxi1nmTH5.png)


# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Orenguteng__Llama-3.1-8B-Lexi-Uncensored-V2)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |27.93|
|IFEval (0-Shot)    |77.92|
|BBH (3-Shot)       |29.69|
|MATH Lvl 5 (4-Shot)|16.92|
|GPQA (0-shot)      | 4.36|
|MuSR (0-shot)      | 7.77|
|MMLU-PRO (5-shot)  |30.90|

