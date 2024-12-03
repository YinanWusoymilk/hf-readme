---
license: cc-by-4.0
datasets:
- pythainlp/thainer-corpus-v2
language:
- th
metrics:
- f1
widget:
- text: "ฉันชื่อ นางสาวมะลิวา บุญสระดี อาศัยอยู่ที่อำเภอนางรอง จังหวัดบุรีรัมย์ อายุ 23 ปี เพิ่งเรียนจบจาก มหาวิทยาลัยขอนแก่น และนี่คือข้อมูลปลอม ชื่อคนไม่มีอยู่จริง"
---

This is a Named Entity Recognition model that trained with [Thai NER v2.0 Corpus](https://huggingface.co/datasets/pythainlp/thainer-corpus-v2)

Training script and split data: [https://zenodo.org/record/7761354](https://zenodo.org/record/7761354)

The model was trained by [WangchanBERTa base model](https://huggingface.co/airesearch/wangchanberta-base-att-spm-uncased).

Validation from the Validation set
- Precision: 0.830336794125095
- Recall: 0.873701039168665
- F1: 0.8514671513892494
- Accuracy: 0.9736483416628805

Test from the Test set
- Precision: 0.8199168093956447
- Recall: 0.8781446540880503
- F1: 0.8480323927622422
- Accuracy: 0.9724346779516247

Download: [HuggingFace Hub](https://huggingface.co/datasets/pythainlp/thainer-corpus-v2)

Read more: [Thai NER v2.0](https://pythainlp.github.io/Thai-NER/version/2)

## Inference

Huggingface doesn't support inference token classification for Thai and It will give wrong tag. You must using this code.

```python
from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification
from pythainlp.tokenize import word_tokenize # pip install pythainlp
import torch

name="pythainlp/thainer-corpus-v2-base-model"
tokenizer = AutoTokenizer.from_pretrained(name)
model = AutoModelForTokenClassification.from_pretrained(name)

sentence="ฉันชื่อ นางสาวมะลิวา บุญสระดี อาศัยอยู่ที่อำเภอนางรอง จังหวัดบุรีรัมย์ อายุ 23 ปี เพิ่งเรียนจบจาก มหาวิทยาลัยขอนแก่น และนี่คือข้อมูลปลอมชื่อคนไม่มีอยู่จริง อายุ 23 ปี"
cut=word_tokenize(sentence.replace(" ", "<_>"))
inputs=tokenizer(cut,is_split_into_words=True,return_tensors="pt")

ids = inputs["input_ids"]
mask = inputs["attention_mask"]
# forward pass
outputs = model(ids, attention_mask=mask)
logits = outputs[0]

predictions = torch.argmax(logits, dim=2)
predicted_token_class = [model.config.id2label[t.item()] for t in predictions[0]]

def fix_span_error(words,ner):
    _ner = []
    _ner=ner
    _new_tag=[]
    for i,j in zip(words,_ner):
        #print(i,j)
        i=tokenizer.decode(i)
        if i.isspace() and j.startswith("B-"):
            j="O"
        if i=='' or i=='<s>' or i=='</s>':
            continue
        if i=="<_>":
            i=" "
        _new_tag.append((i,j))
    return _new_tag

ner_tag=fix_span_error(inputs['input_ids'][0],predicted_token_class)
print(ner_tag)
```
output:
```python
[('ฉัน', 'O'),
 ('ชื่อ', 'O'),
 (' ', 'O'),
 ('นางสาว', 'B-PERSON'),
 ('มะลิ', 'I-PERSON'),
 ('วา', 'I-PERSON'),
 (' ', 'I-PERSON'),
 ('บุญ', 'I-PERSON'),
 ('สระ', 'I-PERSON'),
 ('ดี', 'I-PERSON'),
 (' ', 'O'),
 ('อาศัย', 'O'),
 ('อยู่', 'O'),
 ('ที่', 'O'),
 ('อําเภอ', 'B-LOCATION'),
 ('นาง', 'I-LOCATION'),
 ('รอง', 'I-LOCATION'),
 (' ', 'O'),
 ('จังหวัด', 'B-LOCATION'),
 ('บุรีรัมย์', 'I-LOCATION'),
 (' ', 'O'),
 ('อายุ', 'O'),
 (' ', 'O'),
 ('23', 'B-AGO'),
 (' ', 'I-AGO'),
 ('ปี', 'I-AGO'),
 (' ', 'O'),
 ('เพิ่ง', 'O'),
 ('เรียนจบ', 'O'),
 ('จาก', 'O'),
 (' ', 'O'),
 ('มหาวิทยาลั', 'B-ORGANIZATION'),
 ('ยขอนแก่น', 'I-ORGANIZATION'),
 (' ', 'O'),
 ('และ', 'O'),
 ('นี่', 'O'),
 ('คือ', 'O'),
 ('ข้อมูล', 'O'),
 ('ปลอม', 'O'),
 ('ชื่อ', 'O'),
 ('คน', 'O'),
 ('ไม่', 'O'),
 ('มี', 'O'),
 ('อยู่', 'O'),
 ('จริง', 'O'),
 (' ', 'O'),
 ('อายุ', 'O'),
 (' ', 'O'),
 ('23', 'B-AGO'),
 (' ', 'O'),
 ('ปี', 'I-AGO')]
```

## Cite

> Wannaphong Phatthiyaphaibun. (2022). Thai NER 2.0 (2.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7761354

or BibTeX

```
@dataset{wannaphong_phatthiyaphaibun_2022_7761354,
  author       = {Wannaphong Phatthiyaphaibun},
  title        = {Thai NER 2.0},
  month        = sep,
  year         = 2022,
  publisher    = {Zenodo},
  version      = {2.0},
  doi          = {10.5281/zenodo.7761354},
  url          = {https://doi.org/10.5281/zenodo.7761354}
}
```