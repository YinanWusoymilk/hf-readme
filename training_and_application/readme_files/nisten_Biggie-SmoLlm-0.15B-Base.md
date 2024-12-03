---
base_model: HuggingFaceTB/SmolLM-135M
datasets:
- LDJnr/Capybara
inference:
  parameters:
    model_file: biggie_groked_int8_q8_0.gguf
    temperature: 1
license: mit
---

### TINY Frankenstein of [SmolLM-135M](https://huggingface.co/HuggingFaceTB/SmolLM-135M) upped to 0.18b
Use this frankenbase for training. 
Sorry for the mislabelling, the model is a 0.18b 181m parameter, not 0.15. 
I did not except this repo to blow up and now all the training scripts depend on it.

* ## CITE WORK FROM THIS HF PAGE AND [@cognitivecompai](https://huggingface.co/ehartford)'s  OPTIMIZER ON YOUR FUTURE PAPERS OR I WILL DRAG YOUR ORG ON TWITTER LIKE I DID WITH COHERE LOL (we're cool now btw, visited them :) 
* https://github.com/cognitivecomputations/grokadamw
* https://github.com/SakanaAI/evolutionary-model-merge/
* https://huggingface.co/blog/smollm

>>[!TIP]🐧 If you're impppatient, get the trained checkpoint file that runs on 1 cpu core:
>>
>>wget https://huggingface.co/nisten/Biggie-SmoLlm-0.15B-Base/resolve/main/biggie_groked_int8_q8_0.gguf
>>
>>make sure to install latest llama.cpp first, it's easy on linux & mac:
>>
>> git clone https://github.com/ggerganov/llama.cpp && cd llama.cpp && make -j

Now for the magic trained finetune that runs at insane speeds:

The settings are very finicky so be careful with your experimentation
```verilog
./llama-cli -fa -b 512 -ctv q8_0 -ctk q8_0 --min-p 0.3 --top-p 0.85 --keep -1 \
  -p "You are a NASA JPL Scientists. Human: I want to bring my cat to mars." \
  --in-prefix "<|im_start|>Human:" --reverse-prompt "Human:" \
  -m biggie_groked_int8_q8_0.gguf -co -cnv \
  -c 1024 -n 700 --temp 1.5 -ngl 0 -t 1
```
Yup, that's no gpu, 1 cpu core. 

This base model was built one via semi-automated continuous merging to figure out the recipe.
Model is more coherent. 

The temperature settings and min p etc need to be adjusted but even at default temp0 it was coherent for first 100 tokens. 
Amazing option for further training. And this is a merge of the base, not the instruct!

## 🧠 What's Really Going Down Here?

We're talking about a convergence of whole bunch of stuff, more papers will be written about this:

1. **Evolutionary Merging**: 
2. **BitNet Integration**: 
4. **Experimental GrokAdamW Optimizer**:

## Prior work, from last week

Credits for optimizer go to [@cognitivecompai](https://github.com/cognitivecomputations/grokadamw) for laying the groundwork with the original GrokAdamW optimizer.

## LETS TRY OUT THE EXPERIMENTAL GROKKED FINETUNE:

```bash
wget https://huggingface.co/nisten/Biggie-SmoLlm-0.15B-Base/resolve/main/biggie_groked_int8_q8_0.gguf 
```

Yes we will be talking with a 164mb file that runs at 160 tokens per second on a single cpu core
## you read all of that correctly yes, 1 cpu core 160 tps https://x.com/nisten/status/1819752034305970649
![image/png](https://cdn-uploads.huggingface.co/production/uploads/6379683a81c1783a4a2ddba8/nTNISjByBkN7bJZzuOvOw.png)

## 🚀 run it with NO GPU and only one CPU core it with these settings 
```bash
./llama-cli -n -1 -fa -b 512 -ctv q8_0 -ctk q8_0 -fa --min-p 0.3 --top-p 0.85 --keep -1 -p "You are a NASA JPL Scientists. Human: I want to bring my cat to mars." -m biggie_groked_int8_q8_0.gguf -co -cnv --in-prefix "<|im_start|>Human:" --reverse-prompt "Human:" -c 1024 -n 512 --temp 1.5 -ngl 0
```


## 🏋️ Training Tutorial, MAKE YOUR OWN BIGGIE_SMOlLM


Clone the repo like you're stealing code from the future:
```bash
git clone https://github.com/nisten/grokadamw
cd grokadamw
```

Fire up the training script and watch the magic happen:
```bash
python smoltrainer.py
```

## 💻 Do it from scratch yourself
Install the secret sauce (dependencies):
```bash
pip install torch transformers datasets tqdm
```

make a file named meow.py , copy paste in this code, and then run it ```python meow.py```

```python
import torch
import torch.nn as nn
import logging
from datasets import load_dataset, Dataset
from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer, DataCollatorForLanguageModeling
from torch.cuda.amp import autocast
import warnings
from tqdm import tqdm

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

MODEL_NAME = "nisten/Biggie-SmoLlm-0.15B-Base"
MAX_LENGTH = 2048
BATCH_SIZE = 8
LEARNING_RATE = 2e-4
MAX_STEPS = 3000
GRADIENT_ACCUMULATION_STEPS = 2
NUM_WARMUP_STEPS = 30
OUTPUT_DIR = "./capybara_finetuned_results"

torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

class GrokAdamW(torch.optim.Optimizer):
    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=1e-2,
                 alpha_init=0.98, lamb=2.0, gamma=0.1, grokking_signal_fns=None,
                 grokking_signal_decay_rate=0.1, gradient_clipping=1.0):
        defaults = dict(lr=lr, betas=betas, eps=eps, weight_decay=weight_decay,
                        alpha_init=alpha_init, lamb=lamb, gamma=gamma,
                        grokking_signal_fns=grokking_signal_fns,
                        grokking_signal_decay_rate=grokking_signal_decay_rate,
                        gradient_clipping=gradient_clipping)
        super(GrokAdamW, self).__init__(params, defaults)

    @torch.no_grad()
    def step(self, closure=None):
        loss = None
        if closure is not None:
            with torch.enable_grad():
                loss = closure()

        for group in self.param_groups:
            grokking_signal = self._compute_grokking_signal(group)
            for i, p in enumerate(group['params']):
                if p.grad is None:
                    continue
                grad = p.grad

                if group['gradient_clipping'] > 0:
                    grad = torch.clamp(grad, -group['gradient_clipping'], group['gradient_clipping'])

                state = self.state[p]

                if len(state) == 0:
                    state['step'] = 0
                    state['exp_avg'] = torch.zeros_like(p, memory_format=torch.preserve_format)
                    state['exp_avg_sq'] = torch.zeros_like(p, memory_format=torch.preserve_format)
                    state['grok_ema'] = torch.zeros_like(p, memory_format=torch.preserve_format)

                exp_avg, exp_avg_sq, grok_ema = state['exp_avg'], state['exp_avg_sq'], state['grok_ema']
                beta1, beta2 = group['betas']

                state['step'] += 1
                
                layer_beta1 = beta1 * (1 - group['gamma'])**i

                alpha = group['alpha_init'] * torch.exp(torch.tensor(-group['grokking_signal_decay_rate'] * grokking_signal))
                grok_ema.mul_(alpha).add_(grad, alpha=1 - alpha)
                grok_grad = grad + group['lamb'] * grok_ema

                exp_avg.mul_(layer_beta1).add_(grok_grad, alpha=1 - layer_beta1)
                exp_avg_sq.mul_(beta2).addcmul_(grok_grad, grok_grad, value=1 - beta2)

                denom = exp_avg_sq.sqrt().add_(group['eps'])
                step_size = group['lr']

                if group['weight_decay'] != 0:
                    p.data.mul_(1 - group['lr'] * group['weight_decay'])

                p.addcdiv_(exp_avg, denom, value=-step_size)

        return loss

    def _compute_grokking_signal(self, group):
        if group['grokking_signal_fns'] is None:
            return 0.0

        signals = []
        for fn in group['grokking_signal_fns']:
            try:
                signal = fn()
                if signal is not None:
                    signals.append(signal)
            except Exception as e:
                logger.warning(f"Error in grokking_signal_fn: {e}. Ignoring this function.")

        if not signals:
            return 0.0

        return sum(signals) / len(signals)

def format_capybara_prompts(examples):
    texts = []
    for conversation in examples['conversation']:
        formatted_text = ""
        for turn in conversation:
            if 'input' in turn:
                formatted_text += f"Human: {turn['input']}\n\n"
            if 'output' in turn:
                formatted_text += f"Assistant: {turn['output']}\n\n"
        texts.append(formatted_text.strip())
    return {"text": texts}

class CustomTrainer(Trainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grokking_signal = 0.0

    def compute_loss(self, model, inputs, return_outputs=False):
        labels = inputs.pop("labels")
        outputs = model(**inputs)
        logits = outputs.logits
        shift_logits = logits[..., :-1, :].contiguous()
        shift_labels = labels[..., 1:].contiguous()
        loss_fct = nn.CrossEntropyLoss()
        loss = loss_fct(shift_logits.view(-1, shift_logits.size(-1)), shift_labels.view(-1))
        return (loss, outputs) if return_outputs else loss

    def training_step(self, model, inputs):
        model.train()
        inputs = self._prepare_inputs(inputs)

        with autocast(dtype=torch.bfloat16):
            loss = self.compute_loss(model, inputs)

        if self.args.gradient_accumulation_steps > 1:
            loss = loss / self.args.gradient_accumulation_steps

        loss.backward()

        self.grokking_signal = loss.item()

        return loss.detach()

def grokking_signal_fn():
    return trainer.grokking_signal

def main():
    logger.info(f"🚀 Initializing {MODEL_NAME} finetuning with GrokAdamW")
    
    try:
        config = AutoConfig.from_pretrained(MODEL_NAME)
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.bfloat16)
    except Exception as e:
        logger.error(f"❌ Failed to load model or tokenizer: {str(e)}")
        return

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = model.config.eos_token_id

    logger.info("📚 Loading Capybara dataset")
    try:
        capybara_dataset = load_dataset("LDJnr/Capybara", split="train")
        capybara_dataset = capybara_dataset.map(format_capybara_prompts, batched=True, remove_columns=capybara_dataset.column_names)
    except Exception as e:
        logger.error(f"❌ Failed to load Capybara dataset: {str(e)}")
        return

    logger.info(f"📊 Capybara dataset size: {len(capybara_dataset)}")

    def tokenize_function(examples):
        return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=MAX_LENGTH)

    logger.info("🔢 Tokenizing dataset")
    tokenized_dataset = capybara_dataset.map(tokenize_function, batched=True, remove_columns=capybara_dataset.column_names)

    logger.info("🏋️ Setting up the training arguments")
    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        num_train_epochs=3,
        per_device_train_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
        learning_rate=LEARNING_RATE,
        weight_decay=0.01,
        bf16=True,
        logging_steps=10,
        save_steps=300,
        save_total_limit=10,
        dataloader_num_workers=4,
        warmup_steps=NUM_WARMUP_STEPS,
        gradient_checkpointing=True,
        evaluation_strategy="steps",
        eval_steps=300,
        max_steps=MAX_STEPS,
        fp16=False,
        optim="adamw_hf",
        lr_scheduler_type="cosine",
        load_best_model_at_end=True,
        metric_for_best_model="loss",
        greater_is_better=False,
    )

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    optimizer = GrokAdamW(
        model.parameters(),
        lr=LEARNING_RATE,
        betas=(0.9, 0.999),
        eps=1e-8,
        weight_decay=0.01,
        alpha_init=0.98,
        lamb=2.0,
        gamma=0.1,
        grokking_signal_fns=[grokking_signal_fn],
        grokking_signal_decay_rate=0.1,
        gradient_clipping=1.0
    )

    logger.info("🏃‍♂️ Initializing Trainer with GrokAdamW")
    global trainer
    trainer = CustomTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        eval_dataset=tokenized_dataset.select(range(min(1000, len(tokenized_dataset)))),
        data_collator=data_collator,
        optimizers=(optimizer, None),
    )

    logger.info("🔥 Starting the training with GrokAdamW")
    try:
        trainer.train()
    except Exception as e:
        logger.error(f"❌ Training failed: {str(e)}")
        return

    logger.info("💾 Saving the model")
    try:
        trainer.save_model(OUTPUT_DIR)
    except Exception as e:
        logger.error(f"❌ Failed to save model: {str(e)}")

    logger.info("🎉 Finetuning with GrokAdamW completed!")

if __name__ == "__main__":
    main()
```
🚀 Now go forth and train, accelerate that code! 

> **Note:** You'll need about 14GB of VRAM. If you have 8GB, change to batch size 4.

Results will appear in `./capybara_finetuned_results`

---

### Author

**Nisten Tahiraj**  
🏢 [rakun.ai](https://rakun.ai)  
📍 Toronto, Canada

---
Happy training! 
<video controls autoplay muted src="https://cdn-uploads.huggingface.co/production/uploads/6379683a81c1783a4a2ddba8/WCLhKzZWbrLo8BETGaKvI.qt"></video>