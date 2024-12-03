---
license: cc-by-sa-4.0
datasets:
- bigcode/the-stack-dedup
- sahil2801/CodeAlpaca-20k
- teknium/GPTeacher-CodeInstruct
model-base:
- replit/replit-code-v1-3b
tags:
- code
- instruct
- self instruct
language:
- code
programming_language: 
- Markdown
- Java
- JavaScript
- Python
- TypeScript
- PHP
- SQL
- JSX
- reStructuredText
- Rust
- C
- CSS
- Go
- C++
- HTML
- Vue
- Ruby
- Jupyter Notebook
- R
- Shell
---

Base Model: replit/replit-code-v1-3b

This is version 2 of the Replit Code Instruct fine tune model.

This model is fine tuned on both Sahil2801's CodeAlpaca & Teknium's GPTeacher Code-Instruct to give Replit's Code model instruct capabilities.

Try this model on it's HuggingFace demo Spaces: https://huggingface.co/spaces/teknium/Replit-v2-CodeInstruct-3B

Dataset links:
CodeAlpaca: https://huggingface.co/datasets/sahil2801/CodeAlpaca-20k
GPTeacher subset - Code Instruct: https://github.com/teknium1/GPTeacher

This model was trained on 2x a100 80gb for 1 hour on ~25,000 code instruction/response pairs in Alpaca format.

The first model was only trained on 512 sequence length, this model on 2000, giving it much greater access to training data knowledge.

Refer to the base models HuggingFace model card for some basic requirements to run: https://huggingface.co/replit/replit-code-v1-3b

This fine tune can be prompted like any alpaca fine tune:
```
### Instruction:
<prompt>

### Input:
<additional context>

### Response:
```

or  

```
### Instruction:
<prompt>

### Response:

```

This model seems to have issues with device="auto" in the model arguments (and requires the trust_remote_code=True, so you should maybe load it like I am here:  
```  
        self.tokenizer = AutoTokenizer.from_pretrained("./Replit-CodeInstruct/", trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(
            "./Replit-CodeInstruct",
            torch_dtype=torch.bfloat16,
            trust_remote_code=True
        )
        self.model.to('cuda')
```  


This model for me produced coherent outputs with the following sampler settings, but feel free to experiment:  
```  
max_new_tokens=128, do_sample=True, use_cache=True, temperature=0.2, top_p=0.9, eos_token_id= self.tokenizer.eos_token_id
```  

In the tokenizer decode arguments, it also needs these settings:  
```  
skip_special_tokens=True, clean_up_tokenization_space=False
```  

The following parameters were used with HuggingFace trainer to train the model with:  
```
--model_name_or_path replit/replit-code-v1-3b --data_path /root/stanford_alpaca/train.json --bf16 True --output_dir /root/stanford_alpaca/model_ckpts --num_train_epochs 3 --per_device_train_batch_size 4 --per_device_eval_batch_size 1 --gradient_accumulation_steps 8 --save_strategy steps --save_steps 200 --save_total_limit 3 --learning_rate 1e-5 --weight_decay 0. --warmup_ratio 0.03 --tf32 True --run_name Replit1
``` 