---
license: apache-2.0
datasets:
- Skylion007/openwebtext
- JeanKaddour/minipile
language:
- en
pipeline_tag: text-generation
inference:
  parameters:
    do_sample: True
    temperature: 0.5
    top_p: 0.5
    top_k: 50
    max_new_tokens: 250
    repetition_penalty: 1.176
---
A pre-trained language model, based on the Mistral 7B model, has been scaled down to approximately 248 million parameters. This model has been trained on 7,488,000 examples. This model isn't intended for direct use but for fine-tuning on a downstream task.
This model should have a context length of around 32,768 tokens. Safe serialization has been removed due to issues saving model weights.

During evaluation on InstructMix, this model achieved an average perplexity score of 6.3. More epochs are planned for this model on different datasets.
# [Open LLM Leaderboard Evaluation Results (outdated)](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Locutusque__TinyMistral-248m)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 24.18   |
| ARC (25-shot)         | 20.82          |
| HellaSwag (10-shot)   | 26.98    |
| MMLU (5-shot)         | 23.11         |
| TruthfulQA (0-shot)   | 46.89   |
| Winogrande (5-shot)   | 50.75   |
| GSM8K (5-shot)        | 0.0        |
| DROP (3-shot)         | 0.74         |


The purpose of this model is to prove that trillion-scale datasets are not needed to pretrain a language model. As a result of needing small datasets, this model was pretrained on a single GPU (Titan V).