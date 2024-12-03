---
license: mit
---
**[ALMA-R](https://arxiv.org/abs/2401.08417)** builds upon [ALMA models](https://arxiv.org/abs/2309.11674), with further LoRA fine-tuning with our proposed **Contrastive Preference Optimization (CPO)** as opposed to the Supervised Fine-tuning used in ALMA. CPO fine-tuning requires our [triplet preference data](https://huggingface.co/datasets/haoranxu/ALMA-R-Preference) for preference learning. ALMA-R now can matches or even exceeds GPT-4 or WMT winners!
```
@misc{xu2024contrastive,
      title={Contrastive Preference Optimization: Pushing the Boundaries of LLM Performance in Machine Translation}, 
      author={Haoran Xu and Amr Sharaf and Yunmo Chen and Weiting Tan and Lingfeng Shen and Benjamin Van Durme and Kenton Murray and Young Jin Kim},
      year={2024},
      eprint={2401.08417},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
```
@misc{xu2023paradigm,
      title={A Paradigm Shift in Machine Translation: Boosting Translation Performance of Large Language Models}, 
      author={Haoran Xu and Young Jin Kim and Amr Sharaf and Hany Hassan Awadalla},
      year={2023},
      eprint={2309.11674},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
# Download ALMA(-R) Models and Dataset 🚀

We release six translation models presented in the paper:
- ALMA-7B
- ALMA-7B-LoRA
- **ALMA-7B-R (NEW!)**: Further LoRA fine-tuning upon ALMA-7B-LoRA with contrastive preference optimization.
- ALMA-13B
- ALMA-13B-LoRA
- **ALMA-13B-R (NEW!)**: Further LoRA fine-tuning upon ALMA-13B-LoRA with contrastive preference optimization (BEST MODEL!). 
  
Model checkpoints are released at huggingface:
|     Models    | Base Model Link | LoRA Link |
|:-------------:|:---------------:|:---------:|
|    ALMA-7B    |        [haoranxu/ALMA-7B](https://huggingface.co/haoranxu/ALMA-7B)        |     -     |
|  ALMA-7B-LoRA |        [haoranxu/ALMA-7B-Pretrain](https://huggingface.co/haoranxu/ALMA-7B-Pretrain)        |     [haoranxu/ALMA-7B-Pretrain-LoRA](https://huggingface.co/haoranxu/ALMA-7B-Pretrain-LoRA)     |
|  **ALMA-7B-R (NEW!)** |        [haoranxu/ALMA-7B-R (LoRA merged)](https://huggingface.co/haoranxu/ALMA-7B-R)        |     -    |
|    ALMA-13B   |        [haoranxu/ALMA-13B](https://huggingface.co/haoranxu/ALMA-13B)        |     -     |
| ALMA-13B-LoRA |        [haoranxu/ALMA-13B-Pretrain](https://huggingface.co/haoranxu/ALMA-13B-Pretrain)        |     [haoranxu/ALMA-13B-Pretrain-LoRA](https://huggingface.co/haoranxu/ALMA-13B-Pretrain-LoRA)     |
| **ALMA-13B-R (NEW!)** |        [haoranxu/ALMA-13B-R (LoRA merged)](https://huggingface.co/haoranxu/ALMA-13B-R)        |    -   |

**Note that `ALMA-7B-Pretrain` and `ALMA-13B-Pretrain` are NOT translation models. They only experience stage 1 monolingual fine-tuning (20B tokens for the 7B model and 12B tokens for the 13B model), and should be utilized in conjunction with their LoRA models.** 

Datasets used by ALMA and ALMA-R are also released at huggingface now (NEW!)
|     Datasets    | Train / Validation| Test |
|:-------------:|:---------------:|:---------:|
|    Human-Written Parallel Data (ALMA)    |        [train and validation](https://huggingface.co/datasets/haoranxu/ALMA-Human-Parallel)        |     [WMT'22](https://huggingface.co/datasets/haoranxu/WMT22-Test)    |
|  Triplet Preference Data |        [train](https://huggingface.co/datasets/haoranxu/ALMA-R-Preference)        |   [WMT'22](https://huggingface.co/datasets/haoranxu/WMT22-Test) and [WMT'23](https://huggingface.co/datasets/haoranxu/WMT23-Test)   |


A quick start to use our best system (ALMA-13B-R) for translation. An example of translating "我爱机器翻译。" into English:
```
import torch
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer

# Load base model and LoRA weights
model = AutoModelForCausalLM.from_pretrained("haoranxu/ALMA-13B-R", torch_dtype=torch.float16, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("haoranxu/ALMA-13B-R", padding_side='left')

# Add the source sentence into the prompt template
prompt="Translate this from Chinese to English:\nChinese: 我爱机器翻译。\nEnglish:"
input_ids = tokenizer(prompt, return_tensors="pt", padding=True, max_length=40, truncation=True).input_ids.cuda()

# Translation
with torch.no_grad():
    generated_ids = model.generate(input_ids=input_ids, num_beams=5, max_new_tokens=20, do_sample=True, temperature=0.6, top_p=0.9)
outputs = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
print(outputs)
```

Please find more details in our [GitHub repository](https://github.com/fe1ixxu/ALMA)