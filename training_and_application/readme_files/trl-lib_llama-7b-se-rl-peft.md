---
license: bigscience-openrail-m
language:
- en
inference: false
tags:
- trl
- transformers
- rlhf
datasets:
- lvwerra/stack-exchange-paired
---

![pull_figure](https://huggingface.co/datasets/trl-internal-testing/example-images/resolve/main/images/stack-llama.png)

# Llama-se-rl-peft
Adapter weights of a Reinforcement Learning fine-tuned model based on the LLaMA model (see [Meta's LLaMA release](https://ai.facebook.com/blog/large-language-model-llama-meta-ai) for the original LLaMA model). 
The model is designed to generate human-like responses to questions in Stack Exchange domains of programming, mathematics, physics, and more.
For more info check out the [blog post](https://huggingface.co/blog/stackllama) and [github example](https://github.com/lvwerra/trl/tree/main/examples/stack_llama/scripts).

## Model Details

### Model Description
**Developed by:** Hugging Face

**Model type:** An auto-regressive language model based on the transformer architecture, and fine-tuned with [Stack Exchange datasets](https://huggingface.co/datasets/lvwerra/stack-exchange-paired). 

**Languages:** Predominantly English, with additional data from languages with the following ISO codes: 

| bg | ca | cs | da | de | es | fr | hr | hu | it | nl | pl | pt | ro | ru | sl | sr | sv | uk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 


**License:** [bigscience-openrail-m](https://drive.google.com/file/d/16NqKiAkzyZ55NClubCIFup8pT2jnyVIo/view?usp=sharing)

**Finetuned from:** [LLaMA](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md)

### Model Sources
**Repository:**  [https://huggingface.co/trl-lib/llama-7b-se-rl-peft/tree/main](https://huggingface.co/trl-lib/llama-7b-se-rl-peft/tree/main)

**Base Model Repository:** [https://github.com/facebookresearch/llama](https://github.com/facebookresearch/llama)

**Demo:** [https://huggingface.co/spaces/trl-lib/stack-llama](https://huggingface.co/spaces/trl-lib/stack-llama)

## Uses

### Direct Use
- Long-form question-answering on topics of programming, mathematics, and physics
- Demonstrating a Large Language Model's ability to follow target behavior of generating answers to a question that would be highly rated on [Stack Exchange](https://stackexchange.com).

### Out of Scope Use
- Replacing human expertise


## Bias, Risks, and Limitations
- Inherits bias, risks, and limitations from the LLaMA model, as described in the [LLaMA Model Card Bias Evaluation](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md#quantitative-analysis) and [Ethical Considerations](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md#ethical-considerations). 
- Retains biases present in the Stack Exchange dataset. Per the [latest developer survey for Stack Overflow](https://survey.stackoverflow.co/2022/),
which constitutes a significant part of the StackExchange data,
most users who answered the survey identified themselves as [White or European, men, between 25 and 34 years old, and based in the US (with a significant part of responders from India).](https://survey.stackoverflow.co/2022/#developer-profile-demographics)
- May generate answers that are incorrect or misleading.
- May copy answers from the training data verbatim.
- May generate language that is hateful or promotes discrimination ([example](https://huggingface.co/trl-lib/llama-7b-se-rl-peft/discussions/7#64376083369f6f907f5bfe4c)).
- May generate language that is offensive to direct or indirect users or to people or groups mentioned.


### Recommendations
- Answers should be validated through the use of external sources.
- Disparities between the data contributors and the direct and indirect users of the technology should inform developers in assessing what constitutes an appropriate use case.
- Further research is needed to attribute model generations to sources in the training data, especially in cases where the model copies answers from the training data.  

## Training Details

### Training Data
Original datasets are described in [the LLaMA Model Card](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md#training-dataset).
Fine-tuning datasets for this model are based on [Stack Exchange Paired](https://huggingface.co/datasets/lvwerra/stack-exchange-paired), which consists of questions and answers from various domains in Stack Exchange, such as programming, mathematics, physics, and more. Specifically:

**Traditional Fine-tuning:** [https://huggingface.co/datasets/lvwerra/stack-exchange-paired/tree/main/data/finetune](https://huggingface.co/datasets/lvwerra/stack-exchange-paired/tree/main/data/finetune)

**RL Fine-tuning:** [https://huggingface.co/datasets/lvwerra/stack-exchange-paired/tree/main/data/rl](https://huggingface.co/datasets/lvwerra/stack-exchange-paired/tree/main/data/rl)

**Reward Model:** [https://huggingface.co/trl-lib/llama-7b-se-rm-peft](https://huggingface.co/trl-lib/llama-7b-se-rm-peft)

### Training Procedure
The model was first fine-tuned on the Stack Exchange question and answer pairs and then RL fine-tuned using a Stack Exchange Reward Model. 
It is trained to respond to prompts with the following template:

```
Question: <Query> 

Answer: <Response>
```


## Citation

**BibTeX:**
```
@misc {beeching2023stackllama,
	author       = { Edward Beeching and
                     Younes Belkada and
                     Kashif Rasul and
                     Lewis Tunstall and
                     Leandro von Werra and
                     Nazneen Rajani and
                     Nathan Lambert
                   },
	title        = { StackLLaMa: An RL Fine-tuned LLaMa Model for Stack Exchange Question and Answering },
	year         = 2023,
	url          = { https://huggingface.co/trl-lib/llama-7b-se-rl-peft },
	doi          = { 10.57967/hf/0513 },
	publisher    = { Hugging Face Blog }
}
```

## Model Card Authors
[Nathan Lambert](https://huggingface.co/natolambert), [Leandro von Werra](https://huggingface.co/lvwerra), [Edward Beeching](https://huggingface.co/edbeeching), [Kashif Rasul](https://huggingface.co/kashif), [Younes Belkada](https://huggingface.co/ybelkada), [Margaret Mitchell](https://huggingface.co/meg)