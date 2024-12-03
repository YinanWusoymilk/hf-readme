---
license: llama2
inference:
  parameters:
    do_sample: false
    max_length: 200
base_model: meta-llama/Llama-2-7b
widget:
- text: "### Instruction:\nYour task is to generate valid duckdb SQL to answer the following question.\n\n### Input:\n\n### Question:\ncreate a new table called tmp from test.csv\n\n### Response (use duckdb shorthand if possible):"
  example_title: "read test.csv"
- text: "### Instruction:\nYour task is to generate valid duckdb SQL to answer the following question.\n\n### Input:\n\n### Question:\ncreate a new table called tmp from test.csv\n\n### Response (use duckdb shorthand if possible):"
  example_title: "get _amount columns"
- text: "### Instruction:\nYour task is to generate valid duckdb SQL to answer the following question, given a duckdb database schema.\n\n### Input:\nHere is the database schema that the SQL query will run on:\nCREATE TABLE rideshare (\n    hvfhs_license_num varchar,\n    dispatching_base_num varchar,\n    originating_base_num varchar,\n    request_datetime timestamp,\n    on_scene_datetime timestamp,\n    pickup_datetime timestamp,\n    dropoff_datetime timestamp,\n    trip_miles double,\n    trip_time bigint,\n\n);\n\n### Question:\nget longest trip in december 2022\n\n### Response (use duckdb shorthand if possible):"
  example_title: "taxi trips"
---

# DuckDB-NSQL-7B

## Model Description

NSQL is a family of autoregressive open-source large foundation models (FMs) designed specifically for SQL generation tasks.

In this repository we are introducing a new member of NSQL, DuckDB-NSQL. It's based on Meta's original [Llama-2 7B model](https://huggingface.co/meta-llama/Llama-2-7b) and further pre-trained on a dataset of general SQL queries and then fine-tuned on a dataset composed of DuckDB text-to-SQL pairs.

## Training Data

200k DuckDB text-to-SQL pairs, synthetically generated using [Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1), guided by the DuckDB v0.9.2 documentation. And text-to-SQL pairs from [NSText2SQL](https://huggingface.co/datasets/NumbersStation/NSText2SQL) that were transpiled to DuckDB SQL using [sqlglot](https://github.com/tobymao/sqlglot).

## Evaluation Data

We evaluate our models on a DuckDB-specific benchmark that contains 75 text-to-SQL pairs. The benchmark is available [here](https://github.com/NumbersStationAI/DuckDB-NSQL/).

## Training Procedure

DuckDB-NSQL was trained using cross-entropy loss to maximize the likelihood of sequential inputs. For finetuning on text-to-SQL pairs, we only compute the loss over the SQL portion of the pair. The model is trained using 80GB A100s, leveraging data and model parallelism. We fine-tuned for 10 epochs.

## Intended Use and Limitations

The model was designed for text-to-SQL generation tasks from given table schema and natural language prompts. The model works best with the prompt format defined below and outputs.
In contrast to existing text-to-SQL models, the SQL generation is not contrained to `SELECT` statements, but can generate any valid DuckDB SQL statement, including statements for official DuckDB extensions.

## How to Use

Example 1:

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("motherduckdb/DuckDB-NSQL-7B-v0.1")
model = AutoModelForCausalLM.from_pretrained("motherduckdb/DuckDB-NSQL-7B-v0.1", torch_dtype=torch.bfloat16)

text = """### Instruction:
Your task is to generate valid duckdb SQL to answer the following question.

### Input:

### Question:
create a new table called tmp from test.csv

### Response (use duckdb shorthand if possible):
"""

input_ids = tokenizer(text, return_tensors="pt").input_ids

generated_ids = model.generate(input_ids, max_length=500)
print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
```

Example 2:

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("motherduckdb/DuckDB-NSQL-7B-v0.1")
model = AutoModelForCausalLM.from_pretrained("motherduckdb/DuckDB-NSQL-7B-v0.1", torch_dtype=torch.bfloat16)

text = """### Instruction:
Your task is to generate valid duckdb SQL to answer the following question, given a duckdb database schema.

### Input:
Here is the database schema that the SQL query will run on:
CREATE TABLE taxi (
    VendorID bigint,
    tpep_pickup_datetime timestamp,
    tpep_dropoff_datetime timestamp,
    passenger_count double,
    trip_distance double,
    fare_amount double,
    extra double,
    tip_amount double,
    tolls_amount double,
    improvement_surcharge double,
    total_amount double,
);

### Question:
get all columns ending with _amount from taxi table

### Response (use duckdb shorthand if possible):"""

input_ids = tokenizer(text, return_tensors="pt").input_ids

generated_ids = model.generate(input_ids, max_length=500)
print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
```

Example 3:

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("motherduckdb/DuckDB-NSQL-7B-v0.1")
model = AutoModelForCausalLM.from_pretrained("motherduckdb/DuckDB-NSQL-7B-v0.1", torch_dtype=torch.bfloat16)

text = """### Instruction:
Your task is to generate valid duckdb SQL to answer the following question, given a duckdb database schema.

### Input:
Here is the database schema that the SQL query will run on:
CREATE TABLE rideshare (
    hvfhs_license_num varchar,
    dispatching_base_num varchar,
    originating_base_num varchar,
    request_datetime timestamp,
    on_scene_datetime timestamp,
    pickup_datetime timestamp,
    dropoff_datetime timestamp,
    trip_miles double,
    trip_time bigint,

);

### Question:
get longest trip in december 2022

### Response (use duckdb shorthand if possible):
"""

input_ids = tokenizer(text, return_tensors="pt").input_ids

generated_ids = model.generate(input_ids, max_length=500)
print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
```



For more information (e.g., run with your local database), please find examples in [this repository](https://github.com/NumbersStationAI/DuckDB-NSQL).