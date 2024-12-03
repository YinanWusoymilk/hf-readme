---
license: other
tags:
- alignment-handbook
- trl
- dpo
- generated_from_trainer
base_model: HuggingFaceH4/zephyr-7b-gemma-sft-v0.1
datasets:
- argilla/dpo-mix-7k
license_name: gemma-terms-of-use
license_link: https://ai.google.dev/gemma/terms
pipeline_tag: text-generation
model-index:
- name: zephyr-7b-gemma
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MT-Bench
      type: unknown
    metrics:
    - type: unknown
      value: 7.81
      name: score
    source:
      url: https://huggingface.co/spaces/lmsys/mt-bench
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: AI2 Reasoning Challenge (25-Shot)
      type: ai2_arc
      config: ARC-Challenge
      split: test
      args:
        num_few_shot: 25
    metrics:
    - type: acc_norm
      value: 58.45
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=HuggingFaceH4/zephyr-7b-gemma-v0.1
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: HellaSwag (10-Shot)
      type: hellaswag
      split: validation
      args:
        num_few_shot: 10
    metrics:
    - type: acc_norm
      value: 83.48
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=HuggingFaceH4/zephyr-7b-gemma-v0.1
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU (5-Shot)
      type: cais/mmlu
      config: all
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 60.68
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=HuggingFaceH4/zephyr-7b-gemma-v0.1
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: TruthfulQA (0-shot)
      type: truthful_qa
      config: multiple_choice
      split: validation
      args:
        num_few_shot: 0
    metrics:
    - type: mc2
      value: 52.07
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=HuggingFaceH4/zephyr-7b-gemma-v0.1
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: Winogrande (5-shot)
      type: winogrande
      config: winogrande_xl
      split: validation
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 74.19
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=HuggingFaceH4/zephyr-7b-gemma-v0.1
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GSM8k (5-shot)
      type: gsm8k
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 45.56
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=HuggingFaceH4/zephyr-7b-gemma-v0.1
      name: Open LLM Leaderboard
---

<img src="https://huggingface.co/HuggingFaceH4/zephyr-7b-gemma-v0.1/resolve/main/thumbnail.png" alt="Zephyr 7B Gemma Logo" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

# Model Card for Zephyr 7B Gemma

Zephyr is a series of language models that are trained to act as helpful assistants. Zephyr 7B Gemma is the third model in the series, and is a fine-tuned version of [`google/gemma-7b`](https://huggingface.co/google/gemma-7b) that was trained on on a mix of publicly available, synthetic datasets using Direct Preference Optimization (DPO). You can reproduce the training of this model via the recipe provided in the [Alignment Handbook](https://github.com/huggingface/alignment-handbook).

## Model description

- **Model type:** A 7B parameter GPT-like model fine-tuned on a mix of publicly available, synthetic datasets.
- **Language(s) (NLP):** Primarily English
- **License:** Gemma Terms of Use
- **Finetuned from model:** [google/gemma-7b](https://huggingface.co/google/gemma-7b)

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/huggingface/alignment-handbook
- **Demo:** https://huggingface.co/spaces/HuggingFaceH4/zephyr-7b-gemma-chat

## Performance

|                                 Model                                 |MT Bench⬇️|IFEval|
|-----------------------------------------------------------------------|------:|------:|
|[zephyr-7b-gemma-v0.1](https://huggingface.co/HuggingFaceH4/zephyr-7b-gemma-v0.1)|  7.81 |  28.76|
|[zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)  |  7.34 |  43.81|
|[google/gemma-7b-it](https://huggingface.co/google/gemma-7b-it)               |  6.38 |  38.01|



|                                 Model                                 |AGIEval|GPT4All|TruthfulQA|BigBench|Average ⬇️|
|-----------------------------------------------------------------------|------:|------:|---------:|-------:|------:|
|[zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)  |  37.52|  71.77|     55.26|   39.77|  51.08|
|[zephyr-7b-gemma-v0.1](https://huggingface.co/HuggingFaceH4/zephyr-7b-gemma-v0.1)|  34.22|  66.37|     52.19|   37.10|  47.47|
|[mlabonne/Gemmalpaca-7B](https://huggingface.co/mlabonne/Gemmalpaca-7B)|  21.6 |  40.87|     44.85 |   30.49|  34.45|
|[google/gemma-7b-it](https://huggingface.co/google/gemma-7b-it)        |  21.33|  40.84|     41.70|   30.25|  33.53|


<details><summary>Details of AGIEval, GPT4All, TruthfulQA, BigBench </summary>

### AGIEval
|             Task             |Version| Metric |Value|   |Stderr|
|------------------------------|------:|--------|----:|---|-----:|
|agieval_aqua_rat              |      0|acc     |21.65|±  |  2.59|
|                              |       |acc_norm|25.20|±  |  2.73|
|agieval_logiqa_en             |      0|acc     |34.72|±  |  1.87|
|                              |       |acc_norm|35.94|±  |  1.88|
|agieval_lsat_ar               |      0|acc     |19.57|±  |  2.62|
|                              |       |acc_norm|21.74|±  |  2.73|
|agieval_lsat_lr               |      0|acc     |30.59|±  |  2.04|
|                              |       |acc_norm|32.55|±  |  2.08|
|agieval_lsat_rc               |      0|acc     |49.07|±  |  3.05|
|                              |       |acc_norm|42.75|±  |  3.02|
|agieval_sat_en                |      0|acc     |54.85|±  |  3.48|
|                              |       |acc_norm|53.40|±  |  3.48|
|agieval_sat_en_without_passage|      0|acc     |37.38|±  |  3.38|
|                              |       |acc_norm|33.98|±  |  3.31|
|agieval_sat_math              |      0|acc     |30.91|±  |  3.12|
|                              |       |acc_norm|28.18|±  |  3.04|

Average: 34.22%

### GPT4All
|    Task     |Version| Metric |Value|   |Stderr|
|-------------|------:|--------|----:|---|-----:|
|arc_challenge|      0|acc     |49.15|±  |  1.46|
|             |       |acc_norm|52.47|±  |  1.46|
|arc_easy     |      0|acc     |77.44|±  |  0.86|
|             |       |acc_norm|74.75|±  |  0.89|
|boolq        |      1|acc     |79.69|±  |  0.70|
|hellaswag    |      0|acc     |60.59|±  |  0.49|
|             |       |acc_norm|78.00|±  |  0.41|
|openbookqa   |      0|acc     |29.20|±  |  2.04|
|             |       |acc_norm|37.80|±  |  2.17|
|piqa         |      0|acc     |76.82|±  |  0.98|
|             |       |acc_norm|77.80|±  |  0.97|
|winogrande   |      0|acc     |64.09|±  |  1.35|

Average: 66.37%

### TruthfulQA
|    Task     |Version|Metric|Value|   |Stderr|
|-------------|------:|------|----:|---|-----:|
|truthfulqa_mc|      1|mc1   |35.74|±  |  1.68|
|             |       |mc2   |52.19|±  |  1.59|

Average: 52.19%

### Bigbench
|                      Task                      |Version|       Metric        |Value|   |Stderr|
|------------------------------------------------|------:|---------------------|----:|---|-----:|
|bigbench_causal_judgement                       |      0|multiple_choice_grade|53.68|±  |  3.63|
|bigbench_date_understanding                     |      0|multiple_choice_grade|59.89|±  |  2.55|
|bigbench_disambiguation_qa                      |      0|multiple_choice_grade|30.23|±  |  2.86|
|bigbench_geometric_shapes                       |      0|multiple_choice_grade|11.42|±  |  1.68|
|                                                |       |exact_str_match      | 0.00|±  |  0.00|
|bigbench_logical_deduction_five_objects         |      0|multiple_choice_grade|28.40|±  |  2.02|
|bigbench_logical_deduction_seven_objects        |      0|multiple_choice_grade|19.14|±  |  1.49|
|bigbench_logical_deduction_three_objects        |      0|multiple_choice_grade|44.67|±  |  2.88|
|bigbench_movie_recommendation                   |      0|multiple_choice_grade|26.80|±  |  1.98|
|bigbench_navigate                               |      0|multiple_choice_grade|50.00|±  |  1.58|
|bigbench_reasoning_about_colored_objects        |      0|multiple_choice_grade|52.75|±  |  1.12|
|bigbench_ruin_names                             |      0|multiple_choice_grade|33.04|±  |  2.22|
|bigbench_salient_translation_error_detection    |      0|multiple_choice_grade|33.37|±  |  1.49|
|bigbench_snarks                                 |      0|multiple_choice_grade|48.62|±  |  3.73|
|bigbench_sports_understanding                   |      0|multiple_choice_grade|58.11|±  |  1.57|
|bigbench_temporal_sequences                     |      0|multiple_choice_grade|37.20|±  |  1.53|
|bigbench_tracking_shuffled_objects_five_objects |      0|multiple_choice_grade|20.08|±  |  1.13|
|bigbench_tracking_shuffled_objects_seven_objects|      0|multiple_choice_grade|15.77|±  |  0.87|
|bigbench_tracking_shuffled_objects_three_objects|      0|multiple_choice_grade|44.67|±  |  2.88|

Average: 37.1%

</details>


## Intended uses & limitations

The model was initially fine-tuned on the [DEITA 10K](https://huggingface.co/datasets/HuggingFaceH4/deita-10k-v0-sft)  dataset, which contains a diverse range of synthetic dialogues generated by ChatGPT. 
We then further aligned the model with [🤗 TRL's](https://github.com/huggingface/trl) `DPOTrainer` on the [argilla/dpo-mix-7k](https://huggingface.co/datasets/argilla/dpo-mix-7k) dataset, which contains 7k prompts and model completions that are ranked by GPT-4. As a result, the model can be used for chat and you can check out our [demo](https://huggingface.co/spaces/HuggingFaceH4/zephyr-chat) to test its capabilities. 

Here's how you can run the model using the `pipeline()` function from 🤗 Transformers:

```python
# pip install transformers>=4.38.2
# pip install accelerate

import torch
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="HuggingFaceH4/zephyr-7b-gemma-v0.1",
    device_map="auto",
    torch_dtype=torch.bfloat16,
)
messages = [
    {
        "role": "system",
        "content": "",  # Model not yet trained for follow this
    },
    {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
]
outputs = pipe(
    messages,
    max_new_tokens=128,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95,
    stop_sequence="<|im_end|>",
)
print(outputs[0]["generated_text"][-1]["content"])
# It is not possible for a human to eat a helicopter in one sitting, as a
# helicopter is a large and inedible machine. Helicopters are made of metal,
# plastic, and other materials that are not meant to be consumed by humans.
# Eating a helicopter would be extremely dangerous and would likely cause
# serious health problems, including choking, suffocation, and poisoning. It is
# important to only eat food that is safe and intended for human consumption.
```

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

Zephyr 7B Gemma has not been aligned to human preferences for safety within the RLHF phase or deployed with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). It is also unknown what the size and composition of the corpus was used to train the base model (`google/gemma-7b`), however it is likely to have included a mix of Web data and technical sources like books and code. See the [StarCoder2 model card](https://huggingface.co/bigcode/starcoder2-15b) for an example of this.


## Training and evaluation data


This model is a fine-tuned version of [HuggingFaceH4/zephyr-7b-gemma-sft-v0.1](https://huggingface.co/HuggingFaceH4/zephyr-7b-gemma-sft-v0.1) on the argilla/dpo-mix-7k dataset.

It achieves the following results on the evaluation set:
- Loss: 0.4695
- Rewards/chosen: -3.3746
- Rewards/rejected: -4.9715
- Rewards/accuracies: 0.7188
- Rewards/margins: 1.5970
- Logps/rejected: -459.4853
- Logps/chosen: -429.9115
- Logits/rejected: 86.4684
- Logits/chosen: 92.8200

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-07
- train_batch_size: 2
- eval_batch_size: 4
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.1923        | 1.9   | 100  | 0.4736          | -3.4575        | -4.9556          | 0.75               | 1.4980          | -459.1662      | -431.5707    | 86.3863         | 92.7360       |


### Framework versions

- Transformers 4.39.0.dev0
- Pytorch 2.1.2+cu121
- Datasets 2.14.6
- Tokenizers 0.15.1

## Citation Information

If you find this model useful in your work, please consider citing the Zephyr technical report:

```
@misc{tunstall2023zephyr,
      title={Zephyr: Direct Distillation of LM Alignment}, 
      author={Lewis Tunstall and Edward Beeching and Nathan Lambert and Nazneen Rajani and Kashif Rasul and Younes Belkada and Shengyi Huang and Leandro von Werra and Clémentine Fourrier and Nathan Habib and Nathan Sarrazin and Omar Sanseviero and Alexander M. Rush and Thomas Wolf},
      year={2023},
      eprint={2310.16944},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```

You may also wish to cite the creators of this model as well:

```
@misc{zephyr_7b_gemma,
  author = {Lewis Tunstall and Philipp Schmid},
  title = {Zephyr 7B Gemma},
  year = {2024},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\url{https://huggingface.co/HuggingFaceH4/zephyr-7b-gemma-v0.1}}
}
```

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_HuggingFaceH4__zephyr-7b-gemma-v0.1)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |62.41|
|AI2 Reasoning Challenge (25-Shot)|58.45|
|HellaSwag (10-Shot)              |83.48|
|MMLU (5-Shot)                    |60.68|
|TruthfulQA (0-shot)              |52.07|
|Winogrande (5-shot)              |74.19|
|GSM8k (5-shot)                   |45.56|

