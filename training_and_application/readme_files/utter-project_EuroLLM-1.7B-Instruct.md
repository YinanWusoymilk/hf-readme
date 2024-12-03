---
license: apache-2.0
language:
- en
- de
- es
- fr
- it
- pt
- pl
- nl
- tr
- sv
- cs
- el
- hu
- ro
- fi
- uk
- sl
- sk
- da
- lt
- lv
- et
- bg
- 'no'
- ca
- hr
- ga
- mt
- gl
- zh
- ru
- ko
- ja
- ar
- hi
base_model:
- utter-project/EuroLLM-1.7B
---

## *Model updated on September 24*





# Model Card for EuroLLM-1.7B-Instruct



This is the model card for the first instruction tuned model of the EuroLLM series: EuroLLM-1.7B-Instruct. You can also check the pre-trained version: [EuroLLM-1.7B](https://huggingface.co/utter-project/EuroLLM-1.7B).

- **Developed by:** Unbabel, Instituto Superior Técnico, University of Edinburgh, Aveni, University of Paris-Saclay, University of Amsterdam, Naver Labs, Sorbonne Université.
- **Funded by:** European Union.
- **Model type:** A 1.7B parameter instruction tuned multilingual transfomer LLM.
- **Language(s) (NLP):** Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hungarian, Irish, Italian, Latvian, Lithuanian, Maltese, Polish, Portuguese, Romanian, Slovak, Slovenian, Spanish, Swedish, Arabic, Catalan, Chinese, Galician, Hindi, Japanese, Korean, Norwegian, Russian, Turkish, and Ukrainian. 
- **License:** Apache License 2.0.

## Model Details

The EuroLLM project has the goal of creating a suite of LLMs capable of understanding and generating text in all European Union languages as well as some additional relevant languages.
EuroLLM-1.7B is a 1.7B parameter model trained on 4 trillion tokens divided across the considered languages and several data sources: Web data, parallel data (en-xx and xx-en), and high-quality datasets.
EuroLLM-1.7B-Instruct was further instruction tuned on EuroBlocks, an instruction tuning dataset with focus on general instruction-following and machine translation.



### Model Description

EuroLLM uses a standard, dense Transformer architecture:
- We use grouped query attention (GQA) with 8 key-value heads, since it has been shown to increase speed at inference time while maintaining downstream performance.
- We perform pre-layer normalization, since it improves the training stability, and use the RMSNorm, which is faster.
- We use the SwiGLU activation function, since it has been shown to lead to good results on downstream tasks.
- We use rotary positional embeddings (RoPE) in every layer, since these have been shown to lead to good performances while allowing the extension of the context length.

For pre-training, we use 256 Nvidia H100 GPUs of the Marenostrum 5 supercomputer, training the model with a constant batch size of 3,072 sequences, which corresponds to approximately 12 million tokens, using the Adam optimizer, and BF16 precision.
Here is a summary of the model hyper-parameters:
|                                      |                      |
|--------------------------------------|----------------------|
| Sequence Length                      | 4,096                |
| Number of Layers                     | 24                   |
| Embedding Size                       | 2,048                |
| FFN Hidden Size                      | 5,632                |
| Number of Heads                      | 16                   |
| Number of KV Heads (GQA)             | 8                    |
| Activation Function                  | SwiGLU               |
| Position Encodings                   | RoPE (\Theta=10,000) |
| Layer Norm                           | RMSNorm              |
| Tied Embeddings                      | No                   |
| Embedding Parameters                 | 0.262B               |
| LM Head Parameters                   | 0.262B               |
| Non-embedding Parameters             | 1.133B               |
| Total Parameters                     | 1.657B               |

## Run the model
    
    from transformers import AutoModelForCausalLM, AutoTokenizer
    
    model_id = "utter-project/EuroLLM-1.7B-Instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    
    text = '<|im_start|>system\n<|im_end|>\n<|im_start|>user\nTranslate the following English source text to Portuguese:\nEnglish: I am a language model for european languages. \nPortuguese: <|im_end|>\n<|im_start|>assistant\n'
    
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=20)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))



## Results

### Machine Translation

We evaluate EuroLLM-1.7B-Instruct on several machine translation benchmarks: FLORES-200, WMT-23, and WMT-24 comparing it with [Gemma-2B](https://huggingface.co/google/gemma-2b) and [Gemma-7B](https://huggingface.co/google/gemma-7b) (also instruction tuned on EuroBlocks).
The results show that EuroLLM-1.7B is substantially better than Gemma-2B in Machine Translation and competitive with Gemma-7B.


#### Flores-200
| Model                          | AVG  | AVG en-xx | AVG xx-en | en-ar | en-bg | en-ca | en-cs | en-da | en-de | en-el | en-es-latam | en-et | en-fi | en-fr | en-ga | en-gl | en-hi | en-hr | en-hu | en-it | en-ja | en-ko | en-lt | en-lv | en-mt | en-nl | en-no | en-pl | en-pt-br | en-ro | en-ru | en-sk | en-sl | en-sv | en-tr | en-uk | en-zh-cn | ar-en | bg-en | ca-en | cs-en | da-en | de-en | el-en | es-latam-en | et-en | fi-en | fr-en | ga-en | gl-en | hi-en | hr-en | hu-en | it-en | ja-en | ko-en | lt-en | lv-en | mt-en | nl-en | no-en | pl-en | pt-br-en | ro-en | ru-en | sk-en | sl-en | sv-en | tr-en | uk-en | zh-cn-en |
|--------------------------------|------|-----------|-----------|-------|-------|-------|-------|-------|-------|-------|--------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|----------|-------|-------|-------|-------|-------|-------|-------|----------|-------|-------|-------|-------|-------|-------|-------|--------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|----------|-------|-------|-------|-------|-------|-------|-------|----------|
| EuroLLM-1.7B-Instruct     |86.89 |	86.53 |	87.25 | 85.17 | 89.42 | 84.72 | 89.13 | 89.47 | 86.90 | 87.60 | 86.29       | 88.95 | 89.40 | 87.69 | 74.89 | 86.41 | 76.92 | 84.79 | 86.78 | 88.17 | 89.76 | 87.70 | 87.27 | 87.62 | 67.84 | 87.10 | 90.00 | 88.18 | 89.29    | 89.49 | 88.32 | 88.18 | 86.85 | 90.00 | 87.31 | 87.89 | 86.60    | 86.34 | 87.45 | 87.57 | 87.95 | 89.72 | 88.80 | 87.00 | 86.77         | 88.34 | 89.09 | 88.95 | 82.69 | 87.80 | 88.37 | 86.71 | 87.20 | 87.81 | 86.79 | 86.79 | 85.62 | 86.48 | 81.10 | 86.97 | 90.25    | 85.75 | 89.20 | 88.88 | 86.00 | 87.38 | 86.76 | 89.61 | 87.94    |
| Gemma-2B-EuroBlocks       | 81.59 |	78.97 |	84.21 | 76.68 | 82.73 | 83.14 | 81.63 | 84.63 | 83.15 | 79.42 | 84.05       | 72.58 | 79.73 | 84.97 | 40.50 | 82.13 | 67.79 | 80.53 | 78.36 | 84.90 | 87.43 | 82.98 | 72.29 | 68.68 | 58.55 | 83.13 | 86.15 | 82.78 | 86.79    | 83.14 | 84.61 | 78.18 | 75.37 | 80.89 | 78.38 | 84.38 | 84.35    | 83.88 | 85.77 | 86.85 | 86.31 | 88.24 | 88.12 | 84.79 | 84.90         | 82.51 | 86.32 | 88.29 | 54.78 | 86.53 | 85.83 | 85.41 | 85.18 | 86.77 | 85.78 | 84.99 | 81.65 | 81.78 | 67.27 | 85.92 | 89.07    | 84.14 | 88.07 | 87.17 | 85.23 | 85.09 | 83.95 | 87.57 | 84.77    |
| Gemma-7B-EuroBlocks       |85.27 |	83.90 |	86.64 | 86.38 | 87.87 | 85.74 | 84.25 | 85.69       | 81.49 | 85.52 | 86.93 | 62.83 | 84.96 | 75.34 | 84.93 | 83.91 | 86.92 | 88.19 | 86.11 | 81.73 | 80.55 | 66.85 | 85.31 | 89.36 | 85.87 | 88.62    | 88.06 | 86.67 | 84.79 | 82.71 | 86.45 | 85.19 | 86.67 | 85.77    | 86.36 | 87.21 | 88.09 | 87.17 | 89.40 | 88.26 | 86.74 | 86.73         | 87.25 | 88.87 | 88.81 | 72.45 | 87.62 | 87.86 | 87.08 | 87.01 | 87.58 | 86.92 | 86.70 | 85.10 | 85.74 | 77.81 | 86.83 | 90.40    | 85.41 | 89.04 | 88.77 | 86.13 | 86.67 | 86.32 | 89.27 | 87.92    |


#### WMT-23
| Model                          | AVG  | AVG en-xx | AVG xx-en | AVG xx-xx | en-de | en-cs | en-uk | en-ru | en-zh-cn | de-en | uk-en | ru-en | zh-cn-en | cs-uk |
|--------------------------------|------|-----------|-----------|-----------|-------|-------|-------|-------|----------|-------|-------|-------|----------|-------|
| EuroLLM-1.7B-Instruct   | 82.91     | 83.20     | 81.77     | 86.82     | 81.56     | 85.23     | 81.30     | 82.47     | 83.61     | 85.03      | 84.06      | 85.25      | 81.31      | 78.83      | 79.42      | 86.82      |
| Gemma-2B-EuroBlocks       | 79.96     | 79.01     | 80.86     | 81.15     | 76.82     | 76.05     | 77.92     | 78.98     | 81.58     | 82.73      | 82.71      | 83.99      | 80.35      | 78.27      | 78.99      | 81.15      |
| Gemma-7B-EuroBlocks       | 82.76     | 82.26     | 82.70     | 85.98     | 81.37     | 82.42     | 81.54     | 82.18     | 82.90     | 83.17      | 84.29      | 85.70      | 82.46      | 79.73      | 81.33      | 85.98      |



#### WMT-24
| Model | AVG | AVG en-xx | AVG xx-xx | en-de | en-es-latam | en-cs | en-ru | en-uk | en-ja | en-zh-cn | en-hi | cs-uk | ja-zh-cn |
|---------|------|------|-------|----|---|-------|-------|--------|--------|-------|-------|-------|-----|
| EuroLLM-1.7B-Instruct|79.32     | 79.32     | 79.34     | 79.42     | 80.67     | 80.55     | 78.65     | 80.12     | 82.96     | 80.60      | 71.59      | 83.48      | 75.20      |
|Gemma-2B-EuroBlocks| 74.72     | 74.41     | 75.97     | 74.93     | 78.81     | 70.54     | 74.90     | 75.84     | 79.48     | 78.06      | 62.70      | 79.87      | 72.07      |
|Gemma-7B-EuroBlocks| 78.67     | 78.34     | 80.00     | 78.88     | 80.47     | 78.55     | 78.55     | 80.12     | 80.55     | 78.90      | 70.71      | 84.33      | 75.66      |


### General Benchmarks
We also compare EuroLLM-1.7B with [TinyLlama-v1.1](https://huggingface.co/TinyLlama/TinyLlama_v1.1) and [Gemma-2B](https://huggingface.co/google/gemma-2b) on 3 general benchmarks: Arc Challenge and Hellaswag.
For the non-english languages we use the [Okapi](https://aclanthology.org/2023.emnlp-demo.28.pdf) datasets.
Results show that EuroLLM-1.7B is superior to TinyLlama-v1.1 and similar to Gemma-2B on Hellaswag but worse on Arc Challenge. This can be due to the lower number of parameters of EuroLLM-1.7B (1.133B non-embedding parameters against 1.981B).

#### Arc Challenge
| Model              | Average | English | German | Spanish | French | Italian | Portuguese | Chinese | Russian | Dutch | Arabic | Swedish | Hindi  | Hungarian | Romanian | Ukrainian | Danish | Catalan |
|--------------------|---------|---------|--------|---------|--------|---------|------------|---------|---------|-------|--------|---------|--------|-----------|----------|-----------|--------|---------|
| EuroLLM-1.7B | 0.3496    | 0.4061    | 0.3464    | 0.3684    | 0.3627    | 0.3738    | 0.3855    | 0.3521    | 0.3208    | 0.3507     | 0.3045     | 0.3605     | 0.2928     | 0.3271     | 0.3488     | 0.3516     | 0.3513     | 0.3396     |
| TinyLlama-v1.1       | 0.2650    | 0.3712  | 0.2524  | 0.2795  | 0.2883  | 0.2652  | 0.2906  | 0.2410  | 0.2669   | 0.2404   | 0.2310   | 0.2687   | 0.2354   | 0.2449   | 0.2476   | 0.2524   | 0.2494   | 0.2796   |
| Gemma-2B             | 0.3617    | 0.4846  | 0.3755  | 0.3940  | 0.4080  | 0.3687  | 0.3872  | 0.3726  | 0.3456   | 0.3328   | 0.3122   | 0.3519   | 0.2851   | 0.3039   | 0.3590   | 0.3601   | 0.3565   | 0.3516   |


#### Hellaswag
| Model              | Average | English | German | Spanish | French | Italian | Portuguese | Russian | Dutch  | Arabic | Swedish | Hindi  | Hungarian | Romanian | Ukrainian | Danish | Catalan |
|--------------------|---------|---------|--------|---------|--------|---------|------------|---------|--------|--------|---------|--------|-----------|----------|-----------|--------|---------|
| EuroLLM-1.7B | 0.4744  | 0.4760    | 0.6057    | 0.4793    | 0.5337    | 0.5298    | 0.5085    | 0.5224    | 0.4654    | 0.4949    | 0.4104     | 0.4800     | 0.3655     | 0.4097     | 0.4606     | 0.436      | 0.4702     | 0.4445     |
| TinyLlama-v1.1       |0.3674   | 0.6248  | 0.3650  | 0.4137  | 0.4010  | 0.3780  | 0.3892  | 0.3494  | 0.3588   | 0.2880   | 0.3561   | 0.2841   | 0.3073   | 0.3267   | 0.3349   | 0.3408   | 0.3613   |
| Gemma-2B             |0.4666  | 0.7165  | 0.4756  | 0.5414  | 0.5180  | 0.4841  | 0.5081  | 0.4664  | 0.4655   | 0.3868   | 0.4383   | 0.3413   | 0.3710   | 0.4316   | 0.4291   | 0.4471   | 0.4448   |


## Bias, Risks, and Limitations

EuroLLM-1.7B-Instruct has not been aligned to human preferences, so the model may generate problematic outputs (e.g., hallucinations, harmful content, or false statements).

## Paper

Paper: [EuroLLM: Multilingual Language Models for Europe](https://huggingface.co/papers/2409.16235)