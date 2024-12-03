---
language:
- ru
license: apache-2.0
---

# FRED-T5 1.7B (Full-scale Russian Enhanced Denoisers T5) 
The model architecture design, pretraining, and evaluation are documented in our preprint: [**A Family of Pretrained Transformer Language Models for Russian**](https://arxiv.org/abs/2309.10931).


The model was trained by [SberDevices](https://sberdevices.ru/).  

Architecture based on T5. 

It has 24 layers and 1536 hidden size. More details in config.json.

The model trained on a mixture of 7 denoisers like UL2 with several differences (https://arxiv.org/abs/2205.05131).

It was trained on Russian language corpus (300GB).   The dataset is the same as for ruT5 models. 

Bbpe tokenizer. 50257 + special tokens 107. Prefix tokens: '\<LM\>', '\<SC1>',.. '\<SC6>'

First half of the time model trained on the small part of all dataset (1%,3GB) and without prefixes in each task.

For RSG, we trained as described in the T5 paper. First, we trained multitask for all tasks. Then we took the best checkpoint for the task and trained it further.
RSG submit here https://russiansuperglue.com/login/submit_info/1936

Total training time was around 45 days on 112 A100 GPUs.


## Usage (HuggingFace Models Repository)

```python
import torch
from transformers import GPT2Tokenizer, T5ForConditionalGeneration 
tokenizer = GPT2Tokenizer.from_pretrained('ai-forever/FRED-T5-1.7B',eos_token='</s>')
model = T5ForConditionalGeneration.from_pretrained('ai-forever/FRED-T5-1.7B')
device='cuda'
model.to(device)

#Prefix <LM>
lm_text='<LM>Принялся Кутузов рассказывать свою историю как он сюда попал. Началось'
input_ids=torch.tensor([tokenizer.encode(lm_text)]).to(device)
outputs=model.generate(input_ids,eos_token_id=tokenizer.eos_token_id,early_stopping=True)
print(tokenizer.decode(outputs[0][1:]))

# print result: с того, что он был в армии, служил в артиллерии</s>.

#Prefix <SC1>
lm_text='<SC1>Принялся Кутузов рассказывать свою историю <extra_id_0>. Началось с того, что он был в армии, служил в артиллерии.'
input_ids=torch.tensor([tokenizer.encode(lm_text)]).to(device)
outputs=model.generate(input_ids,eos_token_id=tokenizer.eos_token_id,early_stopping=True)
print(tokenizer.decode(outputs[0][1:]))

#print result: '<extra_id_0>, как он воевал</s>'

# Prefix <SC5> 
lm_text='<SC5>Принялся Кутузов рассказывать свою историю <extra_id_0>. Началось с того, что он был в армии, служил в артиллерии.'
input_ids=torch.tensor([tokenizer.encode(lm_text)]).to(device)
outputs=model.generate(input_ids,eos_token_id=tokenizer.eos_token_id,early_stopping=True)
tokenizer.decode(outputs[0][1:])

#print result: '<extra_id_0>, как он стал генералом</s>'

```
# Authors
+ NLP core team RnD [Telegram channel](https://t.me/nlpcoreteam):
  + Dmitry Zmitrovich 
  + Andrei Kalmykov 
  + Vitaly Kadulin 
  + Mikhail Novikov
  + Alexey Khoroshilov
 
[Salute AI Community](https://t.me/SaluteTechGroup).  


# Cite us
```
@misc{zmitrovich2023family,
      title={A Family of Pretrained Transformer Language Models for Russian}, 
      author={Dmitry Zmitrovich and Alexander Abramov and Andrey Kalmykov and Maria Tikhonova and Ekaterina Taktasheva and Danil Astafurov and Mark Baushenko and Artem Snegirev and Tatiana Shavrina and Sergey Markov and Vladislav Mikhailov and Alena Fenogenova},
      year={2023},
      eprint={2309.10931},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```