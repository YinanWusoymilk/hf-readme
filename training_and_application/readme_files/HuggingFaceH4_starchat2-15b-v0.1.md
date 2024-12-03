---
base_model: HuggingFaceH4/starchat2-15b-sft-v0.1
tags:
- alignment-handbook
- generated_from_trainer
datasets:
- HuggingFaceH4/ultrafeedback_binarized
- HuggingFaceH4/orca_dpo_pairs
model-index:
- name: starchat2-15b-v0.1
  results: []
---

<img src="https://huggingface.co/HuggingFaceH4/starchat2-15b-v0.1/resolve/main/model_logo.png" alt="StarChat2 15B Logo" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

# Model Card for StarChat2 15B

StarChat is a series of language models that are trained to act as helpful coding assistants. StarChat2 is the latest model in the series, and is a fine-tuned version of [StarCoder2](https://huggingface.co/bigcode/starcoder2-15b) that was trained with SFT and DPO on a mix of synthetic datasets.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Model type:** A 16B parameter GPT-like model fine-tuned on a mix of publicly available, synthetic datasets.
- **Language(s) (NLP):** Primarily English and 600+ programming languages.
- **License:** BigCode Open RAIL-M v1
- **Finetuned from model:** [bigcode/starcoder2-15b](https://huggingface.co/bigcode/starcoder2-15b)

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/huggingface/alignment-handbook
- **Demo:** https://huggingface.co/spaces/HuggingFaceH4/starchat2-playground

## Performance

StarChat2 15B was trained to balance chat and programming capabilities. It achieves strong performance on chat benchmarks like [MT Bench](https://huggingface.co/spaces/lmsys/mt-bench) and [IFEval](https://arxiv.org/abs/2311.07911), as well as the canonical HumanEval benchmark for Python code completion. The scores reported below were obtained using the [LightEval](https://github.com/huggingface/lighteval) evaluation suite (commit `988959cb905df4baa050f82b4d499d46e8b537f2`) and each prompt has been formatted with the model's corresponding chat template to simulate real-world usage. This is why some scores may differ from those reported in technical reports or on the Open LLM Leaderboard. 

| Model                                                                                           | MT Bench | IFEval | HumanEval |
|-------------------------------------------------------------------------------------------------|---------:|-------:|----------:|
| [starchat2-15b-v0.1](https://huggingface.co/HuggingFaceH4/starchat2-15b-v0.1)                   |     7.66 |  35.12 |     71.34 |
| [deepseek-coder-6.7b-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct) |     4.17 |  14.23 |     80.48 |
| [CodeLlama-13b-Instruct-hf](https://huggingface.co/codellama/CodeLlama-13b-Instruct-hf)         |     6.80 |  43.44 |     50.60 |


## Intended uses & limitations

The model was fine-tuned on a blend of chat, code, math, and reasoning datasets. As a result, the model can be used for chat and you can check out our [demo](https://huggingface.co/spaces/HuggingFaceH4/starchat2-playground) to test its coding capabilities. 

Here's how you can run the model using the `pipeline()` function from 🤗 Transformers:

```python
# pip install 'transformers @ git+https://github.com/huggingface/transformers.git@831bc25d8fdb85768402f772cf65cc3d7872b211'
# pip install accelerate

import torch
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="HuggingFaceH4/starchat2-15b-v0.1",
    device_map="auto",
    torch_dtype=torch.bfloat16,
)
messages = [
    {
        "role": "system",
        "content": "You are StarChat2, an expert programming assistant",
    },
    {"role": "user", "content": "Write a simple website in HTML. When a user clicks the button, it shows a random Chuck Norris joke."},
]
outputs = pipe(
    messages,
    max_new_tokens=512,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95,
    stop_sequence="<|im_end|>",
)
print(outputs[0]["generated_text"][-1]["content"])
```

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

StarChat2 15B has not been aligned to human preferences with techniques like RLHF or deployed with in-the-loop filtering of responses like ChatGPT, so the model can produce problematic outputs (especially when prompted to do so). 
Models trained primarily on code data will also have a more skewed demographic bias commensurate with the demographics of the GitHub community, for more on this see the [StarCoder2 dataset](https://huggingface.co/datasets/bigcode/the-stack-v2)

Since the base model was pretrained on a large corpus of code, it may produce code snippets that are syntactically valid but semantically incorrect. 
For example, it may produce code that does not compile or that produces incorrect results.  
It may also produce code that is vulnerable to security exploits.  
We have observed the model also has a tendency to produce false URLs which should be carefully inspected before clicking.

StarChat2 15B was fine-tuned from the base model [StarCoder2](https://huggingface.co/bigcode/starcoder2-15b), please refer to its model card's [Limitations Section](https://huggingface.co/bigcode/starcoder2-15b#limitations) for relevant information. 
In particular, the model was evaluated on some categories of gender biases, propensity for toxicity, and risk of suggesting code completions with known security flaws; these evaluations are reported in its [technical report](https://huggingface.co/papers/2402.19173).


## Training details

This model is a fine-tuned version of [starchat2-15b-sft-v0.1](https://huggingface.co/HuggingFaceH4/starchat2-15b-sft-v0.1) on the HuggingFaceH4/ultrafeedback_binarized and the HuggingFaceH4/orca_dpo_pairs datasets. Check out the recipe in the [Alignment Handbook](https://github.com/huggingface/alignment-handbook) for more details.

It achieves the following results on the evaluation set:
- Loss: 0.4347
- Rewards/chosen: -0.9461
- Rewards/rejected: -2.7745
- Rewards/accuracies: 0.7658
- Rewards/margins: 1.8284
- Logps/rejected: -322.1934
- Logps/chosen: -316.1898
- Logits/rejected: -2.3817
- Logits/chosen: -2.3005

## Training procedure

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
| 0.717         | 0.17  | 100  | 0.6006          | -0.0924        | -0.2899          | 0.6329             | 0.1975          | -272.5022      | -299.1165    | -2.5313         | -2.4191       |
| 0.6273        | 0.35  | 200  | 0.5160          | -0.3994        | -0.9461          | 0.6930             | 0.5467          | -285.6261      | -305.2568    | -2.5281         | -2.4278       |
| 0.5538        | 0.52  | 300  | 0.4781          | -0.6589        | -1.5892          | 0.7247             | 0.9302          | -298.4870      | -310.4470    | -2.4996         | -2.4110       |
| 0.5056        | 0.7   | 400  | 0.4594          | -0.8283        | -2.1332          | 0.7437             | 1.3050          | -309.3687      | -313.8344    | -2.4472         | -2.3644       |
| 0.4983        | 0.87  | 500  | 0.4512          | -0.7758        | -2.2806          | 0.7468             | 1.5049          | -312.3167      | -312.7843    | -2.4223         | -2.3404       |
| 0.4662        | 1.04  | 600  | 0.4431          | -0.7839        | -2.4016          | 0.7658             | 1.6177          | -314.7355      | -312.9465    | -2.4049         | -2.3215       |
| 0.4411        | 1.22  | 700  | 0.4415          | -1.0090        | -2.7582          | 0.7690             | 1.7492          | -321.8679      | -317.4481    | -2.3840         | -2.3016       |
| 0.471         | 1.39  | 800  | 0.4368          | -0.9617        | -2.7445          | 0.7690             | 1.7828          | -321.5930      | -316.5019    | -2.3809         | -2.2991       |
| 0.4485        | 1.57  | 900  | 0.4351          | -0.9490        | -2.7594          | 0.7722             | 1.8103          | -321.8916      | -316.2497    | -2.3815         | -2.3004       |
| 0.4411        | 1.74  | 1000 | 0.4348          | -0.9293        | -2.7469          | 0.7658             | 1.8176          | -321.6409      | -315.8547    | -2.3823         | -2.3011       |
| 0.4499        | 1.92  | 1100 | 0.4348          | -0.9482        | -2.7767          | 0.7658             | 1.8285          | -322.2369      | -316.2320    | -2.3828         | -2.3012       |


### Framework versions

- Transformers 4.39.0.dev0
- Pytorch 2.1.2+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
