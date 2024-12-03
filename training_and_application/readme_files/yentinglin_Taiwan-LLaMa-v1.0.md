---
license: llama2
datasets:
- yentinglin/zh_TW_c4
- yentinglin/traditional_mandarin_instructions
language:
- zh
widget:
 - text: "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. USER: 你好，請問你可以幫我寫一封推薦信嗎？ ASSISTANT:"
library_name: transformers
pipeline_tag: text-generation
extra_gated_heading: Acknowledge license to accept the repository.
extra_gated_prompt: Please contact the author for access.
extra_gated_button_content: Acknowledge license 同意以上內容
extra_gated_fields:
  Name: text
  Mail: text
  Organization: text
  Country: text
  Any utilization of the Taiwan LLM repository mandates the explicit acknowledgment and attribution to the original author: checkbox
---
<img src="https://cdn-uploads.huggingface.co/production/uploads/5df9c78eda6d0311fd3d541f/CmusIT5OlSXvFrbTJ7l-C.png" alt="Taiwan LLM Logo" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

# 🌟 Checkout [Taiwan-LLM Demo Chat-UI](http://www.twllm.com) 🌟

# Model Card for Taiwan LLM 13B v1.0 chat

Taiwan LLM is an advanced language model tailored for Traditional Chinese, focusing on the linguistic and cultural contexts of Taiwan. 
Developed from a large base model, it's enriched with diverse Taiwanese textual sources and refined through Supervised Fine-Tuning. 
This model excels in language understanding and generation, aligning closely with Taiwan's cultural nuances. 
It demonstrates improved performance on various benchmarks like TC-Eval, showcasing its contextual comprehension and cultural relevance. 
For detailed insights into Taiwan LLM's development and features, refer to our [technical report](https://github.com/MiuLab/Taiwan-LLaMa/blob/main/twllm_paper.pdf).


## Model description

- **Model type:** A 13B parameter GPT-like model fine-tuned on a mix of publicly available, synthetic datasets.
- **Language(s) (NLP):** Primarily Traditional Chinese (zh-tw)
- **Finetuned from model:** [yentinglin/Taiwan-LLaMa-v1.0-base](https://huggingface.co/yentinglin/Taiwan-LLaMa-v1.0-base)

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/MiuLab/Taiwan-LLaMa
- **Demo:** https://twllm.com/

## Performance


![image/png](https://cdn-uploads.huggingface.co/production/uploads/5df9c78eda6d0311fd3d541f/HTwIzw6RDha2-PhuWqSuI.png)

## Intended uses

Here's how you can run the model using the `pipeline()` function from 🤗 Transformers:

```python
# pip install transformers>=4.34
# pip install accelerate

import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="yentinglin/Taiwan-LLaMa-v1.0", torch_dtype=torch.bfloat16, device_map="auto")

# We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {
        "role": "system",
        "content": "你是一個人工智慧助理",
    },
    {"role": "user", "content": "東北季風如何影響台灣氣候？"},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```

### Training hyperparameters

![image/png](https://cdn-uploads.huggingface.co/production/uploads/5df9c78eda6d0311fd3d541f/MdvHwdUvH-c926qyRAw7K.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/5df9c78eda6d0311fd3d541f/kKpkvxDzOEyiAoTqmzRYO.png)


![image/png](https://cdn-uploads.huggingface.co/production/uploads/5df9c78eda6d0311fd3d541f/FsnlJ_fkRxf7fn5RKZnjE.png)

The following hyperparameters were used during training:
- learning_rate: 5e-05
- distributed_type: multi-GPU
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 5.0

## Citation

If you find Taiwan LLM is useful in your work, please cite it with:

```
@misc{lin2023taiwan,
      title={Taiwan LLM: Bridging the Linguistic Divide with a Culturally Aligned Language Model}, 
      author={Yen-Ting Lin and Yun-Nung Chen},
      year={2023},
      eprint={2311.17487},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
