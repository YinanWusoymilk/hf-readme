---
license: apache-2.0
datasets:
- tatsu-lab/alpaca
- sahil2801/CodeAlpaca-20k
language:
- zh
- en
library_name: transformers
tags:
- baichuan
- lora
pipeline_tag: text-generation
inference: false
---

A bilingual instruction-tuned LoRA model of https://huggingface.co/baichuan-inc/baichuan-7B

- Instruction-following datasets used: alpaca, alpaca-zh, codealpaca
- Training framework: https://github.com/hiyouga/LLaMA-Factory

Please follow the [baichuan-7B License](https://huggingface.co/baichuan-inc/baichuan-7B/resolve/main/baichuan-7B%20%E6%A8%A1%E5%9E%8B%E8%AE%B8%E5%8F%AF%E5%8D%8F%E8%AE%AE.pdf) to use this model.

Usage:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

tokenizer = AutoTokenizer.from_pretrained("hiyouga/baichuan-7b-sft", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("hiyouga/baichuan-7b-sft", trust_remote_code=True).cuda()
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

query = "晚上睡不着怎么办"
template = (
    "A chat between a curious user and an artificial intelligence assistant. "
    "The assistant gives helpful, detailed, and polite answers to the user's questions.\n"
    "Human: {}\nAssistant: "
)

inputs = tokenizer([template.format(query)], return_tensors="pt")
inputs = inputs.to("cuda")
generate_ids = model.generate(**inputs, max_new_tokens=256, streamer=streamer)
```

You could also alternatively launch a CLI demo by using the script in https://github.com/hiyouga/LLaMA-Factory

```bash
python src/cli_demo.py --template default --model_name_or_path hiyouga/baichuan-7b-sft
```

---

You could reproduce our results with the following scripts using [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory):

```bash
CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --model_name_or_path baichuan-inc/baichuan-7B \
    --do_train \
    --dataset alpaca_gpt4_en,alpaca_gpt4_zh,codealpaca \
    --template default \
    --finetuning_type lora \
    --lora_rank 16 \
    --lora_target all \
    --output_dir baichuan_lora \
    --overwrite_cache \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --gradient_accumulation_steps 8 \
    --preprocessing_num_workers 16 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 100 \
    --eval_steps 100 \
    --learning_rate 5e-5 \
    --max_grad_norm 0.5 \
    --num_train_epochs 2.0 \
    --val_size 0.01 \
    --evaluation_strategy steps \
    --load_best_model_at_end \
    --plot_loss \
    --fp16
```

Loss curve on training set:
![train](assets/training_loss.svg)

Loss curve on evaluation set:
![eval](assets/eval_loss.svg)
