---
license: other
language:
- tr
library_name: transformers
pipeline_tag: text2text-generation
inference: false
datasets:
- vngrs-ai/vngrs-web-corpus
---

<!--    
inference:
  parameters:
      temperature: 10
      repetition_penalty: 10
      top_p: 0.5

temperature: 0.7
    repetition_penalty: 100
    top_p: 0.9
-->

# Model Card for TURNA

<!-- Provide a quick summary of what the model is/does. -->

TURNA is a Turkish language model based on the UL2 framework which is suitable for both understanding and generation tasks.

Evaluations across three generation and five understanding tasks in Turkish show that TURNA outperforms several multilingual models and competes with monolingual Turkish models in understanding tasks.

The model is shared with the public to be used solely for non-commercial academic research purposes.

## Model Details

- 36 encoder and decoder layers
- 16 attention heads
- Token embeddings are 1024 dimensional
- The multi-layer perceptron layers have 2816 hidden dimensions and employ Gated GeLu activations
- The parameters of the input and classification layers are not shared
- 1.1B parameters
- used a unigram subword tokenizer trained on 10GB of text that consists of random subsets of OSCAR, OPUS, and Wikipedia
- Vocabulary size: 32000 tokens + 128 special tokens

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Bogazici University Computer Engineering Department TABILAB (special thanks to VNGRS-AI for sharing their tokenizer)
- **Funded by:** We thank the Google TPU Research Cloud program for providing us with credits to pretrain our model on TPU v3-8 machines. We are grateful to TETAM and BOUN CMPE for providing access to the GPU cluster used in fine-tuning and evaluation experiments.
<!-- - **Shared by [optional]:** [More Information Needed] -->
- **Model type:** Transformer-based encoder-decoder
- **Language(s) (NLP):** Turkish
- **License:** The model is shared with the public to be used solely for non-commercial academic research purposes.

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** [Training code](https://github.com/boun-tabi-LMG/turna), [Finetuning library](https://github.com/boun-tabi-LMG/turkish-lm-tuner)
- **Paper:** [Arxiv paper](https://arxiv.org/abs/2401.14373)

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

This model can be used for research purposes. You give some text and this model tries to predict the next words.

### Downstream Use

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

This model can be finetuned using [our library](https://github.com/boun-tabi-LMG/turkish-lm-tuner) to solve your custom task involving Turkish language.

This model can be further trained to behave more helpful, less harmful and better for dialog use cases.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

Any commercial or malicious activity.

## Bias, Risks, and Limitations

We refer to the Flan-T5's [official model card](https://arxiv.org/pdf/2210.11416.pdf):

> Language models, including Flan-T5, can potentially be used for language generation in a harmful way, according to Rae et al. (2021). Flan-T5 should not be used directly in any application, without a prior assessment of safety and fairness concerns specific to the application.

### Ethical considerations and risks

> ... (ed. The model) is fine-tuned on a large corpus of text data that was not filtered for explicit content or assessed for existing biases. As a result the model itself is potentially vulnerable to generating equivalently inappropriate content or replicating inherent biases in the underlying data.

### Known Limitations

> ... (ed. The model) has not been tested in real world applications.

### Sensitive Use:

> ... (ed. The model) should not be applied for any unacceptable use cases, e.g., generation of abusive speech.


## How to Get Started with the Model

You can find the technical guidance at our library's Github [page](https://github.com/boun-tabi-LMG/turkish-lm-tuner).

## Training Details

- The pretraining was performed with Mixture-of-Denoisers (MoD)
- This version of the model is trained for 1740000 steps
- Batch size: 48
- Input and output lengths: 512
- Effectively exposed to 42.7B tokens

Refer to the paper for more information.


## Evaluation

We didn't yet evaluate the model for biases in any way.

However, we performed finetuning for several understanding and generation tasks:

- Paraphrasing: TAT and OST ([source](https://aclanthology.org/2022.icnlsp-1.14.pdf))
- Summarization and news title generation: [TRNews](https://dl.acm.org/doi/10.1007/s10579-021-09568-y) and [MLSUM](https://arxiv.org/pdf/2004.14900v1.pdf)
- Named Entity Recognition: [WikiANN](https://www.aclweb.org/anthology/P19-1015) and [MilliyetNER](https://doi.org/10.1017/S135132490200284X)
- Part of Speech tagging: Two Universal Dependencies Turkish Treebanks, [IMST](https://universaldependencies.org/treebanks/tr_imst/index.html), [BOUN](https://universaldependencies.org/treebanks/tr_boun/index.html).
- Semantic Textual Similarity: [STSb-tr](https://doi.org/10.18653/v1/2021.gem-1.3)
- Natural language inference: [NLI-TR](https://doi.org/10.18653/v1/2020.emnlp-main.662)
- Text classification: [Product reviews](https://huggingface.co/datasets/turkish_product_reviews), [TTC4900](https://doi.org/10.5505/pajes.2018.15931), and [Tweet sentiments](https://ieeexplore.ieee.org/document/8554037)

Refer to the paper for more information.

## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** TPU v3-8
- **Hours used:** About 400 hours
- **Cloud Provider:** Google Cloud
- **Compute Region:** europe-west4-a
- **Carbon Emitted:** 64.52 kg CO2_2

## Technical Specifications

Refer to the paper for more information.

## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

Coming soon!

**APA:**

Coming soon!

## Model Card Authors

Paper authors.

## Model Card Contact

Onur Güngör

<!--datasets:
- batubayk/TR-News
- mlsum
- mrbesher/tr-paraphrase-opensubtitles2018
- mrbesher/tr-paraphrase-tatoeba
- figenfikri/stsb_tr
- nli_tr
- ttc4900
- turkish_product_reviews-->