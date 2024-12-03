---
language:
- en
license: apache-2.0
model-index:
- name: test_dataset_Codellama-3-8B
  results:
  - task:
      type: text-generation
    dataset:
      name: HumanEval
      type: openai_humaneval
    metrics:
    - type: pass@1
      value: 0.630
      name: pass@1
      verified: false
---
## Please note this model is a test, the full finetuned version can be found here: https://huggingface.co/rombodawg/Llama-3-8B-Instruct-Coder
_______________________________________________________
## GOOGLE COLAB IS A SCAM DO NOT USE THE PAID VERSION
## THEY WILL DISCONNECT YOUR RUNTIME BEFORE EVEN 24 HOURS
https://github.com/googlecolab/colabtools/issues/3451
_________________________________________________________________________________________

## PLEASE INSTEAD USE TENSORDOCK ITS CHEAPER AND DOESNT DISCONNECT YOU
tensordock.com
_________________________________________________________________________________________
__________________________________________________________________________________________________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________
_________________________________________________________________________________________
This is unsloth/llama-3-8b-Instruct trained on the Replete-AI/code-test-dataset using the code bellow with unsloth and google colab with under 15gb of vram. This training was complete in about 40 minutes total.

__________________________________________________________________________
Colab doc if you dont want to copy the code by hand:
- https://colab.research.google.com/drive/1bX4BsjLcdNJnoAf7lGXmWOgaY8yekg8p?usp=sharing
__________________________________________________________________________
Copy from my announcement in my discord:
```
If anyone wants to train their own llama-3-8b model for free on any dataset
 that has around 1,500 lines of data or less you can now do it easily by using
 the code I provided in the model card for my test model in this repo and
 google colab. The training for this model uses (Unsloth + Qlora + Galore) to
 achieve the ability for training under such low vram. 
```

For anyone that is new to coding and training Ai, all your really have to edit is

1. (max_seq_length = 8192) To match the max tokens of the dataset or model you are using
2. (model_name = "unsloth/llama-3-8b-Instruct",) Change what model you are finetuning, this setup is specifically for llama-3-8b
3. (alpaca_prompt =) Change the prompt format, this one is setup to meet llama-3-8b-instruct format, but match it to your specifications. 
4. (dataset = load_dataset("Replete-AI/code-test-dataset", split = "train")) What dataset you are using from huggingface
5. (model.push_to_hub_merged("rombodawg/test_dataset_Codellama-3-8B", tokenizer, save_method = "merged_16bit", token = ""))
6. For the above you need to change "rombodawg" to your Hugginface name, "test_dataset_Codellama-3-8B" to the model name you want saved as, and in token = "" you need to put your huggingface write token so the model can be saved.  


```Python
%%capture
import torch
major_version, minor_version = torch.cuda.get_device_capability()
# Must install separately since Colab has torch 2.2.1, which breaks packages
!pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"

if major_version >= 8:
    # Use this for new GPUs like Ampere, Hopper GPUs (RTX 30xx, RTX 40xx, A100, H100, L40)
    !pip install --no-deps packaging ninja einops flash-attn xformers trl peft accelerate bitsandbytes
else:
    # Use this for older GPUs (V100, Tesla T4, RTX 20xx)
    !pip install --no-deps xformers trl peft accelerate bitsandbytes
pass
```

```Python
!pip install galore_torch
```

```Python
from unsloth import FastLanguageModel
import torch
max_seq_length = 8192 # Choose any! We auto support RoPE Scaling internally!
dtype = None # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
load_in_4bit = True # Use 4bit quantization to reduce memory usage. Can be False.

# 4bit pre quantized models we support for 4x faster downloading + no OOMs.
fourbit_models = [
    "unsloth/mistral-7b-bnb-4bit",
    "unsloth/mistral-7b-instruct-v0.2-bnb-4bit",
    "unsloth/llama-2-7b-bnb-4bit",
    "unsloth/gemma-7b-bnb-4bit",
    "unsloth/gemma-7b-it-bnb-4bit", # Instruct version of Gemma 7b
    "unsloth/gemma-2b-bnb-4bit",
    "unsloth/gemma-2b-it-bnb-4bit", # Instruct version of Gemma 2b
    "unsloth/llama-3-8b-bnb-4bit", # [NEW] 15 Trillion token Llama-3
] # More models at https://huggingface.co/unsloth

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/llama-3-8b-Instruct",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
    # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
)
```

```Python
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context
    random_state = 3407,
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)
```

```Python

alpaca_prompt = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Below is an instruction that describes a task, Write a response that appropriately completes the request.<|eot_id|><|start_header_id|>user<|end_header_id|>

{}<|eot_id|><|start_header_id|>assistant<|end_header_id|>{}"""

EOS_TOKEN = tokenizer.eos_token # Must add EOS_TOKEN
def formatting_prompts_func(examples):
    inputs       = examples["human"]
    outputs      = examples["assistant"]
    texts = []
    for input, output in zip(inputs, outputs):
        # Must add EOS_TOKEN, otherwise your generation will go on forever!
        text = alpaca_prompt.format(input, output) + EOS_TOKEN
        texts.append(text)
    return { "text" : texts, }
pass

from datasets import load_dataset
dataset = load_dataset("Replete-AI/code-test-dataset", split = "train")
dataset = dataset.map(formatting_prompts_func, batched = True,)
```

```Python
from trl import SFTTrainer
from transformers import TrainingArguments
from galore_torch import GaLoreAdamW8bit
import torch.nn as nn
galore_params = []
target_modules_list = ["attn", "mlp"]
for module_name, module in model.named_modules():
    if not isinstance(module, nn.Linear):
        continue

    if not any(target_key in module_name for target_key in target_modules_list):
        continue

    print('mod ', module_name)
    galore_params.append(module.weight)
id_galore_params = [id(p) for p in galore_params]
regular_params = [p for p in model.parameters() if id(p) not in id_galore_params]


param_groups = [{'params': regular_params},
                {'params': galore_params, 'rank': 64, 'update_proj_gap': 200, 'scale': 0.25, 'proj_type': 'std'}]

optimizer = GaLoreAdamW8bit(param_groups, lr=2e-5)

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    optimizers=(optimizer, None),
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = True, # Can make training 5x faster for short sequences.
    args = TrainingArguments(
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        learning_rate = 2e-4,
        fp16 = not torch.cuda.is_bf16_supported(),
        bf16 = torch.cuda.is_bf16_supported(),
        logging_steps = 1,
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
    ),
)
```



```Python
trainer_stats = trainer.train()
model.save_pretrained_merged("model", tokenizer, save_method = "merged_16bit",)
model.push_to_hub_merged("rombodawg/test_dataset_Codellama-3-8B", tokenizer, save_method = "merged_16bit", token = "")
```

