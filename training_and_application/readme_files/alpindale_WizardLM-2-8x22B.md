---
license: apache-2.0
model-index:
- name: WizardLM-2-8x22B
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
      value: 52.72
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/WizardLM-2-8x22B
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
      value: 48.58
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/WizardLM-2-8x22B
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
      value: 22.28
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/WizardLM-2-8x22B
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
      value: 17.56
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/WizardLM-2-8x22B
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
      value: 14.54
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/WizardLM-2-8x22B
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
      value: 39.96
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=alpindale/WizardLM-2-8x22B
      name: Open LLM Leaderboard
---



<p style="font-size:20px;" align="center">
🏠 <a href="https://wizardlm.github.io/WizardLM2" target="_blank">WizardLM-2 Release Blog</a> </p>
<p align="center">
🤗 <a href="https://huggingface.co/collections/microsoft/wizardlm-2-661d403f71e6c8257dbd598a" target="_blank">HF Repo</a>  •🐱 <a href="https://github.com/victorsungo/WizardLM/tree/main/WizardLM-2" target="_blank">Github Repo</a>  • 🐦 <a href="https://twitter.com/WizardLM_AI" target="_blank">Twitter</a> • 📃 <a href="https://arxiv.org/abs/2304.12244" target="_blank">[WizardLM]</a>  • 📃 <a href="https://arxiv.org/abs/2306.08568" target="_blank">[WizardCoder]</a>   • 📃 <a href="https://arxiv.org/abs/2308.09583" target="_blank">[WizardMath]</a>  <br>
</p>
<p align="center">
    👋 Join our <a href="https://discord.gg/VZjjHtWrKs" target="_blank">Discord</a>
</p>

## See [here](https://huggingface.co/lucyknada/microsoft_WizardLM-2-7B) for the WizardLM-2-7B re-upload.

## News 🔥🔥🔥 [2024/04/15]

We introduce and opensource WizardLM-2, our next generation state-of-the-art large language models, 
which have improved performance on complex chat, multilingual, reasoning and agent. 
New family includes three cutting-edge models: WizardLM-2 8x22B, WizardLM-2 70B, and WizardLM-2 7B.

- WizardLM-2 8x22B is our most advanced model, demonstrates highly competitive performance compared to those leading proprietary works 
and consistently outperforms all the existing state-of-the-art opensource models.
- WizardLM-2 70B reaches top-tier reasoning capabilities and is the first choice in the same size. 
- WizardLM-2 7B is the fastest and achieves comparable performance with existing 10x larger opensource leading models.

For more  details of WizardLM-2 please read our [release blog post](https://web.archive.org/web/20240415221214/https://wizardlm.github.io/WizardLM2/) and  upcoming paper.


## Model Details

* **Model name**: WizardLM-2 8x22B
* **Developed by**: WizardLM@Microsoft AI
* **Model type**: Mixture of Experts (MoE)
* **Base model**: [mistral-community/Mixtral-8x22B-v0.1](https://huggingface.co/mistral-community/Mixtral-8x22B-v0.1)
* **Parameters**: 141B
* **Language(s)**: Multilingual
* **Blog**: [Introducing WizardLM-2](https://web.archive.org/web/20240415221214/https://wizardlm.github.io/WizardLM2/)
* **Repository**: [https://github.com/nlpxucan/WizardLM](https://github.com/nlpxucan/WizardLM)
* **Paper**: WizardLM-2 (Upcoming)
* **License**: Apache2.0


## Model Capacities


**MT-Bench**

We also adopt the automatic MT-Bench evaluation framework based on GPT-4 proposed by lmsys to assess the performance of models. 
The WizardLM-2 8x22B even demonstrates highly competitive performance compared to the most advanced proprietary models. 
Meanwhile, WizardLM-2 7B and WizardLM-2 70B are all the top-performing models among the other leading baselines at 7B to 70B model scales.

<p align="center" width="100%">
<a ><img src="https://web.archive.org/web/20240415175608im_/https://wizardlm.github.io/WizardLM2/static/images/mtbench.png" alt="MTBench" style="width: 96%; min-width: 300px; display: block; margin: auto;"></a>
</p>


**Human Preferences Evaluation**

We carefully collected a complex and challenging set consisting of real-world instructions, which includes main requirements of humanity, such as writing, coding, math, reasoning, agent, and multilingual. 
We report the win:loss rate without tie:

- WizardLM-2 8x22B is just slightly falling behind GPT-4-1106-preview, and significantly stronger than Command R Plus and GPT4-0314.
- WizardLM-2 70B is better than GPT4-0613, Mistral-Large, and Qwen1.5-72B-Chat.
- WizardLM-2 7B is comparable with Qwen1.5-32B-Chat, and surpasses Qwen1.5-14B-Chat and Starling-LM-7B-beta.

<p align="center" width="100%">
<a ><img src="https://web.archive.org/web/20240415163303im_/https://wizardlm.github.io/WizardLM2/static/images/winall.png" alt="Win" style="width: 96%; min-width: 300px; display: block; margin: auto;"></a>
</p>





## Method Overview
We built a **fully AI powered synthetic training system** to train WizardLM-2 models, please refer to our [blog](https://web.archive.org/web/20240415221214/https://wizardlm.github.io/WizardLM2/) for more details of this system.

<p align="center" width="100%">
<a ><img src="https://web.archive.org/web/20240415163303im_/https://wizardlm.github.io/WizardLM2/static/images/exp_1.png" alt="Method" style="width: 96%; min-width: 300px; display: block; margin: auto;"></a>
</p>





## Usage

❗<b>Note for model system prompts usage:</b>


<b>WizardLM-2</b>  adopts the prompt format from <b>Vicuna</b> and supports **multi-turn** conversation. The prompt should be as following:

```
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, 
detailed, and polite answers to the user's questions. USER: Hi ASSISTANT: Hello.</s>
USER: Who are you? ASSISTANT: I am WizardLM.</s>......
```

<b> Inference WizardLM-2 Demo Script</b>

We provide a WizardLM-2 inference demo [code](https://github.com/nlpxucan/WizardLM/tree/main/demo) on our github.





# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_alpindale__WizardLM-2-8x22B)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |32.61|
|IFEval (0-Shot)    |52.72|
|BBH (3-Shot)       |48.58|
|MATH Lvl 5 (4-Shot)|22.28|
|GPQA (0-shot)      |17.56|
|MuSR (0-shot)      |14.54|
|MMLU-PRO (5-shot)  |39.96|

