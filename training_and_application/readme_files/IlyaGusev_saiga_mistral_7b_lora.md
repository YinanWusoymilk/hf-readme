---
datasets:
- IlyaGusev/ru_turbo_saiga
- IlyaGusev/ru_sharegpt_cleaned
- IlyaGusev/oasst1_ru_main_branch
- IlyaGusev/gpt_roleplay_realm
- lksy/ru_instruct_gpt4
language:
- ru
pipeline_tag: conversational
license: cc-by-4.0
---

# Saiga/Mistral 7B, Russian Mistral-based chatbot

Based on [Mistral OpenOrca](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca).

This is an adapter-only version.

Merged version: [link](https://huggingface.co/IlyaGusev/saiga_mistral_7b_merged)

Llama.cpp version: [link](https://huggingface.co/IlyaGusev/saiga_mistral_7b_gguf)

Colab: [link](https://colab.research.google.com/drive/1C7TTwYDbfEmkHrbgHNIHS-udoWIEQTUo)

Training code: [link](https://github.com/IlyaGusev/rulm/tree/master/self_instruct).

```python
import torch
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

MODEL_NAME = "IlyaGusev/saiga_mistral_7b"
DEFAULT_MESSAGE_TEMPLATE = "<s>{role}\n{content}</s>"
DEFAULT_RESPONSE_TEMPLATE = "<s>bot\n"
DEFAULT_SYSTEM_PROMPT = "Ты — Сайга, русскоязычный автоматический ассистент. Ты разговариваешь с людьми и помогаешь им."

class Conversation:
    def __init__(
        self,
        message_template=DEFAULT_MESSAGE_TEMPLATE,
        system_prompt=DEFAULT_SYSTEM_PROMPT,
        response_template=DEFAULT_RESPONSE_TEMPLATE
    ):
        self.message_template = message_template
        self.response_template = response_template
        self.messages = [{
            "role": "system",
            "content": system_prompt
        }]

    def add_user_message(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })

    def add_bot_message(self, message):
        self.messages.append({
            "role": "bot",
            "content": message
        })

    def get_prompt(self, tokenizer):
        final_text = ""
        for message in self.messages:
            message_text = self.message_template.format(**message)
            final_text += message_text
        final_text += DEFAULT_RESPONSE_TEMPLATE
        return final_text.strip()


def generate(model, tokenizer, prompt, generation_config):
    data = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
    data = {k: v.to(model.device) for k, v in data.items()}
    output_ids = model.generate(
        **data,
        generation_config=generation_config
    )[0]
    output_ids = output_ids[len(data["input_ids"][0]):]
    output = tokenizer.decode(output_ids, skip_special_tokens=True)
    return output.strip()

config = PeftConfig.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    config.base_model_name_or_path,
    load_in_8bit=True,
    torch_dtype=torch.float16,
    device_map="auto"
)
model = PeftModel.from_pretrained(
    model,
    MODEL_NAME,
    torch_dtype=torch.float16
)
model.eval()

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=False)
generation_config = GenerationConfig.from_pretrained(MODEL_NAME)
print(generation_config)

inputs = ["Почему трава зеленая?", "Сочини длинный рассказ, обязательно упоминая следующие объекты. Дано: Таня, мяч"]
for inp in inputs:
    conversation = Conversation()
    conversation.add_user_message(inp)
    prompt = conversation.get_prompt(tokenizer)

    output = generate(model, tokenizer, prompt, generation_config)
    print(inp)
    print(output)
    print()
    print("==============================")
    print()
```

Examples:
```
User: Почему трава зеленая? 
Saiga: Зеленый цвет у растений обусловлен наличием в них хлорофилла - пигмента, который принимает участие в процессе фотосинтеза.
Фотосинтез - это процесс, благодаря которому растения получают энергию из света и углекислого газа (CO2), превращая их в органические соединения, такие как сахара и жиры.
Хлорофилл поглощает световые волны, которые имеют длину 430-450 нм (синий цвет) и 670-680 нм (красный цвет).
Эти волны поглощаются и передаются другим молекулам, что вызывает ощущение зеленого цвета.
```

```
User: Сочини длинный рассказ, обязательно упоминая следующие объекты. Дано: Таня, мяч
Saiga: Таня была маленькой девочкой, которая любила играть в футбол. Она жила в небольшом городке, где все знали друг друга и всегда были готовы помо
чь. У Тани был единственный мяч, который она называла "Мячик". Он был старым, но для Тани он был самым ценным предметом в мире.
Однажды, когда Таня играла в футбол со своими друзьями, Мячик пропал. Все они начали поиск, но ничего не могли найти. Таня была очень грустна, ведь без своего Мячика она не может играть в свою любимую игру.
В это время в городе проходил фестиваль, и все жители собрались на площади. Таня решила попросить помощи у всех присутствующих. Она рассказала историю о своем Мячике и просила помощи в его поиске. Вся толпа сочувствовала Тане и обещала помочь.
На следующий день, когда фестиваль закончился, Таня получила звонок от одного из жителей города. Он сказал, что нашел её Мячик и хотел бы вернуть ему. Таня была рада и с радостью отправилась к нему.
Когда она пришла к дому, где находился Мячик, она увидела, что он был в хорошем состоянии. Мячик был чистым и блестящим, как новый. Таня была очень рада и с большим счастьем приняла свой Мячик обратно.
Таня и ее друзья продолжали играть в футбол, и каждый раз, когда они играли, они помнили о том, как Мячик вернулся к ней. Именно благодаря этому, они стали лучшими друзьями и всегда поддерживали друг друга в трудных ситуациях.
И так, Таня и ее Мячик стали легендарными в городе, и их история передавалась из поколения в поколение. И вот так, Мячик стал символом дружбы и верности, и все, кто знал эту историю, понимали, что Таня и ее Мячик - одно целое.
```

v1:
- dataset code revision d0d123dd221e10bb2a3383bcb1c6e4efe1b4a28a
- wandb [link](https://wandb.ai/ilyagusev/rulm_self_instruct/runs/ip1qmm9p)
- 5 datasets: ru_turbo_saiga, ru_sharegpt_cleaned, oasst1_ru_main_branch, gpt_roleplay_realm, ru_instruct_gpt4
- Datasets merging script: [create_short_chat_set.py](https://github.com/IlyaGusev/rulm/blob/d0d123dd221e10bb2a3383bcb1c6e4efe1b4a28a/self_instruct/src/data_processing/create_short_chat_set.py)
- saiga_mistral_7b vs saiga2_13b: 243-31-141
