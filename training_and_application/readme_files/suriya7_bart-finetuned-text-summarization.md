---
license: mit
pipeline_tag: summarization
widget:
- text: >-
    Now, there is no doubt that one of the most important aspects of any Pixel
    phone is its camera. And there might be good news for all camera lovers.
    Rumours have suggested that the Pixel 9 could come with a telephoto lens,
    improving its photography capabilities even further. Google will likely
    continue to focus on using AI to enhance its camera performance, in order to
    make sure that Pixel phones remain top contenders in the world of mobile
    photography.
- text: >-
    The Samastha Kerala Sunni Students Federation (SKSSF) has also expressed
    concern over holding the election on Friday. In a statement issued in
    Kozhikode on Saturday, SKSSF state secretariat asked the EC to postpone the
    election to another day. It said conducting elections on Friday will cause
    inconvenience to people from the Muslim community deputed on poll duty or as
    booth agents of political parties to participate in Friday juma prayers.
    Meanwhile, the Wisdom Islamic Organisation has asked the state government to
    officially demand the EC to hold the elections in Kerala and Tamil Nadu on
    some other day, citing inconvenience of believers. State president P N Abdul
    Latheef Madani said all secular forces should put pressure on the poll panel
    to change the date of elections.
datasets:
- EdinburghNLP/xsum
language:
- en
---

# BART Large CNN Text Summarization Model

This model is based on the Facebook BART (Bidirectional and Auto-Regressive Transformers) architecture, specifically the large variant fine-tuned for text summarization tasks. BART is a sequence-to-sequence model introduced by Facebook AI, capable of handling various natural language processing tasks, including summarization.

## Model Details:

- **Architecture**: BART Large CNN
- **Pre-trained model**: BART Large
- **Fine-tuned for**: Text Summarization
- **Fine-tuning dataset**: [xsum](https://huggingface.co/datasets/EdinburghNLP/xsum)

## Usage:

### Installation:

You can install the necessary libraries using pip:
```bash
pip install transformers
```
### Inferecnce
provided a simple snippet of how to use this model for the task of paragraph summarization in PyTorch.
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("suriya7/bart-finetuned-text-summarization")
model = AutoModelForSeq2SeqLM.from_pretrained("suriya7/bart-finetuned-text-summarization")

def generate_summary(text):
    inputs = tokenizer([text], max_length=1024, return_tensors='pt', truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_new_tokens=100, do_sample=False)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

text_to_summarize = """Now, there is no doubt that one of the most important aspects of any Pixel phone is its camera.
And there might be good news for all camera lovers. Rumours have suggested that the Pixel 9 could come with a telephoto lens,
improving its photography capabilities even further. Google will likely continue to focus on using AI to enhance its camera performance,
in order to make sure that Pixel phones remain top contenders in the world of mobile photography."""
summary = generate_summary(text_to_summarize)
print(summary)
```

```
Google is rumoured to be about to unveil its next-generation Pixel smartphone,
the Google Pixel 9,which is expected to come with a telephoto lens and an artificial intelligence (AI)
system to improve its camera capabilities, as well as improve the quality of its images.
```

### Training Parameters
```python
num_train_epochs=1,
warmup_steps = 500,
per_device_train_batch_size=4,
per_device_eval_batch_size=4,
weight_decay = 0.01,
gradient_accumulation_steps=16
```