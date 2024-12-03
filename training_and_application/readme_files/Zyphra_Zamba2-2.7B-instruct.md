---
license: apache-2.0
datasets:
- HuggingFaceH4/ultrachat_200k
- BAAI/Infinity-Instruct
- HuggingFaceH4/ultrafeedback_binarized
- Intel/orca_dpo_pairs
- argilla/OpenHermesPreferences
base_model:
- Zyphra/Zamba2-2.7B
library_name: transformers
---
# Model Card for Zamba2-2.7B-Instruct

Zamba2-2.7B-Instruct is obtained from [Zamba2-2.7B](https://huggingface.co/Zyphra/Zamba2-2.7B) by fine-tuning on instruction-following and chat datasets. Specifically:

1. SFT of the base [Zamba2-2.7B](https://huggingface.co/Zyphra/Zamba2-2.7B) model on [ultrachat_200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) and [Infinity-Instruct](https://huggingface.co/datasets/BAAI/Infinity-Instruct)
2. DPO of the SFT checkpoint on [ultrafeedback_binarized](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized), [orca_dpo_pairs](https://huggingface.co/datasets/Intel/orca_dpo_pairs), and [OpenHermesPreferences](https://huggingface.co/datasets/argilla/OpenHermesPreferences)

Zamba2-2.7B-Instruct is a hybrid model composed of state-space ([Mamba2](https://github.com/state-spaces/mamba)) and transformer blocks.

## Quick start

### Prerequisites

To download Zamba2-2.7B-instruct, clone Zyphra's fork of transformers:
1. `git clone https://github.com/Zyphra/transformers_zamba2.git`
2. `cd transformers_zamba2`
3. Install the repository: `pip install -e .`
4. `pip install accelerate`


### Inference

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Instantiate model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Zyphra/Zamba2-2.7B-instruct")
model = AutoModelForCausalLM.from_pretrained("Zyphra/Zamba2-2.7B-instruct", device_map="cuda", torch_dtype=torch.bfloat16)

# Format the input as a chat template
user_turn_1 = "In one season a flower blooms three times. In one year, there is one blooming season. How many times do two flowers bloom in two years? Please include your logic."
assistant_turn_1 = "In one season, a flower blooms three times. In one year, there is one blooming season. Therefore, in two years, there are two blooming seasons. Since each flower blooms three times in one season, in two blooming seasons, each flower will bloom six times. Since there are two flowers, the total number of times they will bloom in two years is 12."
user_turn_2 = "How many times do the two flowers blossom in three years?"
sample = [{'role': 'user', 'content': user_turn_1}, {'role': 'assistant', 'content': assistant_turn_1}, {'role': 'user', 'content': user_turn_2}]
chat_sample = tokenizer.apply_chat_template(sample, tokenize=False)

# Tokenize input and generate output
input_ids = tokenizer(chat_sample, return_tensors='pt', add_special_tokens=False).to("cuda")
outputs = model.generate(**input_ids, max_new_tokens=150, return_dict_in_generate=False, output_scores=False, use_cache=True, num_beams=1, do_sample=False)
print((tokenizer.decode(outputs[0])))
```

## Performance

Zamba2-2.7B-Instruct punches dramatically above its weight, achieving extremely strong instruction-following benchmark scores, significantly outperforming Gemma2-2B-Instruct of the same size and outperforming Mistral-7B-Instruct in most metrics.

<center>
<img src="https://cdn-uploads.huggingface.co/production/uploads/65bc13717c6ad1994b6619e9/QnudHrMeMx_NuRc2evwRG.png" width="900"/>
</center>


| Model                     | Size | Aggregate MT-Bench | IFEval   |
|:---------------------------:|:-----:|:------------------:|:---------:|
| **Zamba2-2.7B-Instruct**  | 2.7B | **72.40**| **48.02**|
| Mistral-7B-Instruct       |    7B|     66.4 |     45.3 |
| Gemma2-2B-Instruct        | 2.7B |    51.69 |    42.20 |
| H2O-Danube-4B-Chat        |    4B|    52.57 |    37.96 |
| StableLM-Zephyr-3B        |    3B|    66.43 |    38.27 |


Moreover, due to its unique hybrid SSM architecture, Zamba2-2.7B-Instruct achieves extremely low inference latency and rapid generation with a significantly smaller memory footprint than comparable transformer-based models. 

<center>
<img src="https://cdn-uploads.huggingface.co/production/uploads/65bc13717c6ad1994b6619e9/WKTcYkhDgJCHyze4TDpLa.png" width="700" alt="Zamba performance">
</center>


Time to First Token (TTFT)             |  Output Generation
:-------------------------:|:-------------------------:
![](https://cdn-uploads.huggingface.co/production/uploads/65bc13717c6ad1994b6619e9/BmE8X6tDNVw5OJcbZt8sZ.png)  |  ![](https://cdn-uploads.huggingface.co/production/uploads/65bc13717c6ad1994b6619e9/wECc9cItK1FW1MOMGSLrp.png)


<center>
<img src="https://cdn-uploads.huggingface.co/production/uploads/65bc13717c6ad1994b6619e9/nhoss41xlzfEBZzcQXI6z.png" width="700" alt="Zamba inference and memory cost">
</center>

Zamba2-2.7B-Instruct's high performance, strong instruction-following and reasoning capabilities, and small inference compute and memory footprint renders it an ideal generalist model for on-device applications.

## Model Details

Zamba2-2.7B-Instruct utilizes and extends our original Zamba hybrid SSM-attention architecture. The core Zamba architecture consists of a backbone of Mamba2 layers interleaved with one or more shared attention layers (one shared attention in Zamba1, two in Zamba2). This attention has shared weights to minimize the parameter cost of the model. We find that concatenating the original model embeddings to the input to this attention block improves performance, likely due to better maintenance of information across depth. The Zamba2 architecture also applies LoRA projection matrices to the shared MLP to gain some additional expressivity in each block and allow each shared block to specialize slightly to its own unique position while keeping the additional parameter overhead small. 

<center>
<img src="https://cdn-uploads.huggingface.co/production/uploads/65c05e75c084467acab2f84a/XrEIEBxd0fqIgh3LyArAV.png" width="300" alt="Zamba architecture">
</center>



Note: this is a temporary HuggingFace implementation of Zamba2-2.7B. It may not yet be fully compatible with all frameworks and tools intended to interface with HuggingFace models.

A standalone Pytorch implementation of Zamba2-2.7B may be found [here](https://github.com/Zyphra/Zamba2).