---
license: cc-by-nc-4.0
datasets:
- yahma/alpaca-cleaned
language:
- en
pipeline_tag: text-generation
tags:
- llama-2
- alpaca
---



# Model Card for Llama-2-7b-alpaca-cleaned

<!-- Provide a quick summary of what the model is/does. -->

This model checkpoint is the Llama-2-7b fine-tuned on [alpaca-cleaned dataset](https://huggingface.co/datasets/yahma/alpaca-cleaned) with the original Alpaca fine-tuning hyper-parameters.

## Model Details

### Model Description

This model checkpoint is the Llama-2-7b fine-tuned on [alpaca-cleaned dataset](https://huggingface.co/datasets/yahma/alpaca-cleaned) with the original Alpaca fine-tuning hyper-parameters. \
The original Alpaca model is fine-tuned on Llama with the alpaca dataset by researchers from Stanford University


- **Developed by:** NEU Human-centered AI Lab
- **Shared by [optional]:** NEU Human-centered AI Lab
- **Model type:** Text-generation
- **Language(s) (NLP):** English
- **License:** cc-by-nc-4.0 (comply with the alpaca-cleaned dataset)
- **Finetuned from model [optional]:** [Llama-2-7b](https://huggingface.co/meta-llama/Llama-2-7b)

### Model Sources 

<!-- Provide the basic links for the model. -->

- **Repository:** https://huggingface.co/meta-llama/Llama-2-7b


## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

The model is intended to be used for research purposes only in English, complying with [stanford_alpaca project](https://github.com/tatsu-lab/stanford_alpaca). \
The model has been fine-tuned on the [alpaca-cleaned dataset](https://huggingface.co/datasets/yahma/alpaca-cleaned) for assistant-like chat and general natural language generation tasks. \
The use of this model should also comply with the restrictions from [Llama-2-7b](https://huggingface.co/meta-llama/Llama-2-7b).


### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

The out-of-Scope use of this model should also comply with [stanford_alpaca project](https://github.com/tatsu-lab/stanford_alpaca) and [Llama-2-7b](https://huggingface.co/meta-llama/Llama-2-7b).

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

{{ bias_risks_limitations | default("[More Information Needed]", true)}}


## How to Get Started with the Model

Use the code below to get started with the model.
```
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("NEU-HAI/Llama-2-7b-alpaca-cleaned")
model = AutoModelForCausalLM.from_pretrained("NEU-HAI/Llama-2-7b-alpaca-cleaned")
```
## Training Details

### Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

We use the [alpaca-cleaned dataset](https://huggingface.co/datasets/yahma/alpaca-cleaned), which is the cleaned version of the original [alpaca dataset](https://huggingface.co/datasets/tatsu-lab/alpaca) created by researchers from Stanford University.

### Training Procedure 

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->
We follow the same training procedure and mostly same hyper-parameters to fine-tune the original Alpaca model on Llama. The procedure can be found in [stanford_alpaca project](https://github.com/tatsu-lab/stanford_alpaca).


#### Training Hyperparameters

```
--bf16 True \
--num_train_epochs 3 \
--per_device_train_batch_size 4 \
--per_device_eval_batch_size 4 \
--gradient_accumulation_steps 8 \
--evaluation_strategy "no" \
--save_strategy "steps" \
--save_steps 2000 \
--save_total_limit 1 \
--learning_rate 2e-5 \
--weight_decay 0. \
--warmup_ratio 0.03 \
--lr_scheduler_type "cosine" \
--logging_steps 1 \
--fsdp "full_shard auto_wrap" \
--fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
--tf32 True
```

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Data Card if possible. -->

N/A

#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

N/A

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

N/A

### Results

N/A

#### Summary

N/A



<!--
## Environmental Impact

Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** {{ hardware | default("[More Information Needed]", true)}}
- **Hours used:** {{ hours_used | default("[More Information Needed]", true)}}
- **Cloud Provider:** {{ cloud_provider | default("[More Information Needed]", true)}}
- **Compute Region:** {{ cloud_region | default("[More Information Needed]", true)}}
- **Carbon Emitted:** {{ co2_emitted | default("[More Information Needed]", true)}}
-->



## Citation 

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

Please cite the [stanford_alpaca project](https://github.com/tatsu-lab/stanford_alpaca)

```
@misc{alpaca,
  author = {Rohan Taori and Ishaan Gulrajani and Tianyi Zhang and Yann Dubois and Xuechen Li and Carlos Guestrin and Percy Liang and Tatsunori B. Hashimoto },
  title = {Stanford Alpaca: An Instruction-following LLaMA model},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/tatsu-lab/stanford_alpaca}},
}
```



## Model Card Authors 

Northeastern Human-centered AI Lab

## Model Card Contact




