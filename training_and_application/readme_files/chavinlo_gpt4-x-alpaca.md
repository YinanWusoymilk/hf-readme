# GPT4 x Alpaca

As a base model we used: https://huggingface.co/chavinlo/alpaca-13b

Finetuned on GPT4's responses, for 3 epochs.

NO LORA

Please do note that the configurations files maybe messed up, this is because of the trainer I used. I WILL NOT EDIT THEM because there are repos hat automatically fix this, changing it might break it. Generally you just need to change anything that's under the name of "LLaMa" to "Llama" NOTE THE UPPER AND LOWER CASE!!!!
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_chavinlo__gpt4-x-alpaca)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 46.78   |
| ARC (25-shot)         | 52.82          |
| HellaSwag (10-shot)   | 79.59    |
| MMLU (5-shot)         | 48.19         |
| TruthfulQA (0-shot)   | 48.88   |
| Winogrande (5-shot)   | 70.17   |
| GSM8K (5-shot)        | 2.81        |
| DROP (3-shot)         | 24.99         |
