---
license: apache-2.0
datasets:
- PipableAI/pip-txt-to-sql-spider-bird-dataset
language:
- en
metrics:
- accuracy
tags:
- sql
- code
- text2sql
- instruction_tuned
- basemodel
- jax
- pytorch
- text-generation-inference
library_name: transformers
pipeline_tag: text-generation
widget:
- text: >-
    <schema>CREATE TABLE system(JobID: String,GID: String, UID: String,
    Start:Time(yyyy/mm/dd), End: Time,ElapsedRaw: Time, CPUTimeRAW: Time,NCPUS:
    Number,NNodes: Number, NodeList: List,  State:String, Timelimit:
    Time);</schema><question>Get UID and job id for Jobs that started on Jan 20
    , 2023 ended on feb 14 2023 and has job id 20</question><sql>
  example_title: example
---
# pipSQL-1.3b

[pipableAi](https://www.linkedin.com/company/pipable.ai/about/)

[colab_notebook](https://colab.research.google.com/drive/1insSxvc3jjAXe0zmdIjmbG3ttb5mpRgQ?usp=sharing)

## What have we built?
A 1.3 bn SQL model that outperforms most SQL expert models and chatgpt on popular benchmarks.
This is a distilled model built on the deepseek base model.
Please refer to https://huggingface.co/PipableAI/pip-library-etl-1.3b for our state of the art model.
## How we built it?

We used softmax cross entropy and a modified form of policy grad along with Q loss, optimized in an EM set up.
Loss behaviour in the set up mentioned above - 

![image/png](https://cdn-uploads.huggingface.co/production/uploads/658d8095a2a6a6e0da8bb8a6/I80Ru1r4thoYrLagIWALa.png)

## Benchmarking :
For benchmarking purposes we are using Semantic Evaluation for Text-to-SQL with 
Distilled Test Suites, an officially accepted evaluation framework for Spider, SParC, and CoSQL which was proposed by a research team of Yale and Berkeley. 
The benchmark contains 2200 test data points
Here is the link to run the evaluation:


[Test Suite SQL Eval](https://github.com/taoyds/test-suite-sql-eval)

|model|easy|medium|hard|extra|
|-----|----|------|----|-----|
|sqlcoder-7b-2|72.0|58.0|40.6|37.3|
|pipSQL-1.3b|78.5|57.5|42.1|28.3|
|pipSQL-7b|63.0|40.0|30.2|25.0|
|sqlcoder-7b|60.6|48.2|28.3|20.4|
|gpt-3.5|58.8|44.7|31.0|28.4|

We have also benchmarked it on defog eval.
It contains 200 test data points handpicked by defog team.
Here is the link to it:


[Defog SQL-Eval](https://github.com/defog-ai/sql-eval)
These are the results -

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64d32c6b921678fdc9de3302/fFeLSEYBNpQk_JWjFsF5M.png)

## License
The model is open source under apache 2.0. License

## Usage

### Installation

```bash
pip install transformers
```

### Prompt
```python
prompt = f"""<schema>{schema}</schema>
<question>{question}</question>
<sql>"""
```

### PyTorch
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda"
model = AutoModelForCausalLM.from_pretrained("PipableAI/pip-sql-1.3b")
tokenizer = AutoTokenizer.from_pretrained("PipableAI/pip-sql-1.3b")

inputs = tokenizer(text, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0], skip_special_tokens=True).split('<sql>')[1].split('</sql>')[0])
```

### Flax
```python
from transformers import FlaxAutoModelForCausalLM, AutoTokenizer
device = "cuda"
model = FlaxAutoModelForCausalLM.from_pretrained("PipableAI/pip-sql-1.3b",from_pt=True)
tokenizer = AutoTokenizer.from_pretrained("PipableAI/pip-sql-1.3b")

inputs = tokenizer(text, return_tensors="jax")
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0], skip_special_tokens=True).split('<sql>')[1].split('</sql>')[0])
```

## Examples

### Schema
```sql
CREATE TABLE Products (
  product_id number,
  parent_product_id number,
  product_name text,
  product_price number,
  product_color text,
  product_size text,
  product_description text);

CREATE TABLE Customers (
  customer_id number,
  gender_code text,
  customer_first_name text,
  customer_middle_initial text,
  customer_last_name text,
  email_address text,
  login_name text,
  login_password text,
  phone_number text,
  address_line_1 text,
  town_city text,
  county text,
  country text);

CREATE TABLE Customer_Payment_Methods (
  customer_id number,
  payment_method_code text);

CREATE TABLE Invoices (
  invoice_number number,
  invoice_status_code text,
  invoice_date time);

CREATE TABLE Orders (
  order_id number,
  customer_id number,
  order_status_code text,
  date_order_placed time);

CREATE TABLE Order_Items (
  order_item_id number,
  product_id number,
  order_id number,
  order_item_status_code text);

CREATE TABLE Shipments (
  shipment_id number,
  order_id number,
  invoice_number number,
  shipment_tracking_number text,
  shipment_date time);

CREATE TABLE Shipment_Items (
  shipment_id number,
  order_item_id number);
```

### Questions
What are the email address, town and county of the customers who are of the least common gender?
```sql
SELECT email_address ,  town_city ,  county FROM customers GROUP BY gender_code ORDER BY count(*) ASC LIMIT 1
```

What are the product price and the product size of the products whose price is above average?
```sql
SELECT product_price ,  product_size FROM products WHERE product_price  > (SELECT avg(product_price) FROM products)
```

Which customers did not make any orders? List the first name, middle initial and last name.
```sql
SELECT T1.customer_first_name ,  T1.customer_middle_initial ,  T1.customer_last_name FROM Customers AS T1 WHERE T1.customer_id NOT IN (SELECT T2.customer_id FROM Orders AS T2)
```

### Team
Avi Kothari, Pratham Gupta, Ritvik Aryan Kalra, Rohan Bhatial, Soham Acharya