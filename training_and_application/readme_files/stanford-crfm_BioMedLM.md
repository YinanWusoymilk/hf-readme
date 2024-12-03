---
license: bigscience-bloom-rail-1.0
datasets:
- pubmed
widget: 
- text: 'Photosynthesis is'
---

# Model Card for BioMedLM 2.7B

Note: This model was previously known as PubMedGPT 2.7B, but we have changed it due to a request from the NIH which holds the trademark for "PubMed".

Paper: [BioMedLM: A 2.7B Parameter Language Model Trained On Biomedical Text](https://arxiv.org/abs/2403.18421)

BioMedLM 2.7B is new language model trained exclusively on biomedical abstracts and papers from [The Pile](https://pile.eleuther.ai/). This GPT-style model can achieve strong results on a variety of biomedical NLP tasks, including a new state of the art performance of 50.3% accuracy on the MedQA biomedical question answering task.

As an autoregressive language model, BioMedLM 2.7B is also capable of natural language generation. However, we have only begun to explore the generation capabilities and limitations of this model, and we emphasize that this model’s generation capabilities are for research purposes only and not suitable for production. In releasing this model, we hope to advance both the development of biomedical NLP applications and best practices for responsibly training and utilizing domain-specific language models; issues of reliability, truthfulness, and explainability are top of mind for us.

This model was a joint collaboration of [Stanford CRFM](https://crfm.stanford.edu/) and [MosaicML](https://www.mosaicml.com/).

#  Table of Contents

- [Model Card for BioMedLM 2.7B](#model-card-for--model_id-)
- [Table of Contents](#table-of-contents)
- [Model Details](#model-details)
  - [Model Description](#model-description)
- [Uses](#uses)
  - [Downstream Use](#downstream-use)
  - [Out-of-Scope Use](#out-of-scope-use)
- [Bias, Risks, and Limitations](#bias-risks-and-limitations)
  - [Recommendations](#recommendations)
- [Training Details](#training-details)
  - [Training Data](#training-data)
  - [Training Procedure](#training-procedure)
    - [Preprocessing](#preprocessing)
- [Environmental Impact](#environmental-impact)
- [Technical Specifications](#technical-specifications)
  - [Model Architecture and Objective](#model-architecture-and-objective)
  - [Compute Infrastructure](#compute-infrastructure)

# Model Details

## Model Description

<!-- Provide a longer summary of what this model is/does. -->
BioMedLM 2.7B is new language model trained exclusively on biomedical abstracts and papers from [The Pile](https://pile.eleuther.ai/). This GPT-style model can achieve strong results on a variety of biomedical NLP tasks, including a new state of the art performance of 50.3% accuracy on the MedQA biomedical question answering task.

As an autoregressive language model, BioMedLM 2.7B is also capable of natural language generation. However, we have only begun to explore the generation capabilities and limitations of this model, and we emphasize that this model’s generation capabilities are for research purposes only and not suitable for production. In releasing this model, we hope to advance both the development of biomedical NLP applications and best practices for responsibly training and utilizing domain-specific language models; issues of reliability, truthfulness, and explainability are top of mind for us.

This model was a joint collaboration of [Stanford CRFM](https://crfm.stanford.edu/) and [MosaicML](https://www.mosaicml.com/).


- **Developed by:** Stanford CRFM, MosaicML
- **Shared by:** Stanford CRFM
- **Model type:** Language model
- **Language(s) (NLP):** en
- **License:**  [bigscience-bloom-rail-1.0](https://huggingface.co/spaces/bigscience/license)

# Uses

This model is licensed under the terms of [BigScience Open RAIL-M license](https://huggingface.co/spaces/bigscience/license) used for [BLOOM](https://huggingface.co/bigscience/bloom-1b1). Please note that, among other restrictions, this license forbids use of the model (or derivatives thereof)
"To provide medical advice and medical results interpretation." If you are concerned that your use case would follow under the "letter" of this restriction, but not the "spirit," you can contact us to discuss.

## Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
<!-- If the user enters content, print that. If not, but they enter a task in the list, use that. If neither, say "more info needed." -->
It is possible to use this model to generate text, which is useful for experimentation and understanding its capabilities. It should not be directly used for production or work that may directly impact people.

## Downstream Use

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->
The main way we have used this model is finetuning for downstream question answering tasks, and we recommend using this model that way.
 
## Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
We do not recommend using this model for natural language generation in a production environment, finetuned or otherwise.

# Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
Significant research has explored bias and fairness issues with language models (see, e.g., [Sheng et al. (2021)](https://aclanthology.org/2021.acl-long.330.pdf)). Predictions generated by the model may include disturbing and harmful stereotypes across protected classes; identity characteristics; and sensitive, social, and occupational groups.

## Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->
While this model is capable of generating natural language text, we have only begun to explore this capability and its limitations. Understanding these limitations is especially important in a domain like medicine. Therefore, **we strongly recommend against using this model in production for natural language generation.**

# Training Details

## Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

This model was trained on the Pubmed Abstracts and Full Text from [The Pile](https://pile.eleuther.ai/). 

## Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

The model was trained on [MosaicML Cloud](https://www.mosaicml.com/cloud), a platform designed for large workloads like LLMs. Using the [Composer](https://github.com/mosaicml/composer) training library and [PyTorch FSDP](https://pytorch.org/docs/stable/fsdp.html), it was easy to enable multi-node training across 128 A100-40GB GPUs, and the total run was completed in ~6.25 days. The model was trained with batch size=1024 and sequence length=1024 for 300B tokens using Decoupled AdamW with the following settings:

|  |  |
| --- | ------ |
| lr  | 1.6e-4 |
| eps | 1e-8       |
| betas | \[0.9, 0.95\]      |
| weight decay    |  1.6e-5      |

The training process was very smooth and did not suffer from any divergences.

As we were preparing the training run, we were unsure of the benefits of training out to 300B tokens for language model perplexity and downstream task performance. While most models of this scale (e.g. GPT Neo 2.7B) are trained to 300-400B tokens, the datasets those models use are vastly larger than PubMed. For instance, The Pile is 8x the size of its PubMed subcorpora.
  
Fortunately, we did continue to see steady perplexity improvements on the validation and training sets for the entirety of training, and preliminary experiments showed improved downstream task performance as we trained out to the full 300B tokens. Our takeaway from this was that it was indeed worth it to train for the full 300B tokens, even though this represented dramatically more passes through the data than comparable models.

### Preprocessing

The model uses a custom tokenizer trained on the PubMed Abstracts. When building domain specific models we have found it important to use a tokenizer trained on in-domain text to maximize performance on downstream tasks. A key benefit is that common biomedical terms are represented as entire tokens. 

For instance, all of these following terms are tokenized into single tokens by the biomedical tokenizer and multiple tokens by the standard GPT-2 tokenizer:
  
|   |   |
| --- | --- |
| chromatography |   chrom/atography |
| cytotoxicity |   cyt/ot/oxicity |
| Immunohistochemistry |   Immun/oh/ist/ochemistry |
| photosynthesis |   photos/ynthesis |
| probiotic |   prob/iotic |

This allows the model to encode information about these concepts in their individual token representations rather than spread out across subword tokens like “oh” shared with many other terms.

# Technical Specifications

## Model Architecture and Objective

BioMedLM 2.7B is a standard GPT-2 implementation (trained with Flash Attention) with the following hyperparameters:

|             |       |
| ----------- | ----- |
| hidden size | 2560  |
| heads       | 20    |
| layers      | 32    |
| vocab size  | 28896 |
| sequence length| 1024      |

## Compute Infrastructure

The model was trained on [MosaicML Cloud](https://www.mosaicml.com/cloud), a platform designed for large workloads like LLMs. Using the [Composer](https://github.com/mosaicml/composer) training library and [PyTorch FSDP](https://pytorch.org/docs/stable/fsdp.html), it was easy to enable multi-node training across 128 A100-40GB GPUs, and the total run was completed in ~6.25 days.
