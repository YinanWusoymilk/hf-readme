---
language: en
datasets:
- wikisql
widget:
- text: "question: get people name with age equal 25 table: id, name, age"
---
There are an upgraded version that support multiple tables and support "<" sign using Flan-T5 as a based model [here](https://huggingface.co/juierror/flan-t5-text2sql-with-schema-v2).

# How to use
```python
from typing import List
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("juierror/text-to-sql-with-table-schema")
model = AutoModelForSeq2SeqLM.from_pretrained("juierror/text-to-sql-with-table-schema")

def prepare_input(question: str, table: List[str]):
    table_prefix = "table:"
    question_prefix = "question:"
    join_table = ",".join(table)
    inputs = f"{question_prefix} {question} {table_prefix} {join_table}"
    input_ids = tokenizer(inputs, max_length=700, return_tensors="pt").input_ids
    return input_ids

def inference(question: str, table: List[str]) -> str:
    input_data = prepare_input(question=question, table=table)
    input_data = input_data.to(model.device)
    outputs = model.generate(inputs=input_data, num_beams=10, top_k=10, max_length=700)
    result = tokenizer.decode(token_ids=outputs[0], skip_special_tokens=True)
    return result

print(inference(question="get people name with age equal 25", table=["id", "name", "age"]))
```