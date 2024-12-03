# Stanford Alpaca

This is a replica of Alpaca by Stanford' tatsu

Trained using the original instructions with a minor modification in FSDP mode

# Other versions:
13B: https://huggingface.co/chavinlo/alpaca-13b

13B -> GPT4 : https://huggingface.co/chavinlo/gpt4-x-alpaca

## Compute Used
Trained on 4xA100s for 6H
Donated by redmond.ai

NO LORA HAS BEEN USED, this is a natively-finetuned model, hence "alpaca-native"

If you are interested on more llama-based models, you can check out my profile or search for other models at https://huggingface.co/models?other=llama

This (MIGHT) be a quantized version of this model, but be careful: https://boards.4channel.org/g/thread/92173062#p92182396

CONFIGURATION (default except fsdp):

```shell
torchrun --nproc_per_node=4 --master_port=3045 train.py \
    --model_name_or_path /workspace/llama-7b-hf \
    --data_path ./alpaca_data.json \
    --bf16 True \
    --output_dir /workspace/output \
    --num_train_epochs 3 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 200 \
    --save_total_limit 1 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --fsdp "shard_grad_op auto_wrap" \
    --fsdp_transformer_layer_cls_to_wrap 'LLaMADecoderLayer' \
    --tf32 True --report_to="wandb"
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_chavinlo__alpaca-native)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 41.96   |
| ARC (25-shot)         | 52.3          |
| HellaSwag (10-shot)   | 77.09    |
| MMLU (5-shot)         | 41.6         |
| TruthfulQA (0-shot)   | 37.58   |
| Winogrande (5-shot)   | 69.46   |
| GSM8K (5-shot)        | 1.44        |
| DROP (3-shot)         | 14.23         |
