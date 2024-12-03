---
license: cc-by-sa-4.0
library_name: transformers
pipeline_tag: text-generation
---

# Model Card for SQLCoder-70B-Alpha

A capable large language model for natural language to SQL generation. Outperforms all generalist models (including GPT-4) on text to SQL.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/603bbad3fd770a9997b57cb6/3BVMV2z6FTEEPF1hJ2qu1.png)


## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** [Defog, Inc](https://defog.ai)
- **Model type:** [Text to SQL]
- **License:** [CC-by-SA-4.0]
- **Finetuned from model:** [CodeLlama-70B]

### Model Sources [optional]
- [**HuggingFace:**](https://huggingface.co/defog/sqlcoder-70b-alpha)
- [**GitHub:**](https://github.com/defog-ai/sqlcoder)
- [**Demo:**](https://defog.ai/sqlcoder-demo/)

## Uses

This model is intended to be used by non-technical users to understand data inside their SQL databases. It is meant as an analytics tool, and not as a database admin tool.

This model has not been trained to reject malicious requests from users with write access to databases, and should only be used by users with read-only access.

## How to Get Started with the Model

Use the code [here](https://github.com/defog-ai/sqlcoder/blob/main/inference.py) to get started with the model.

## Evaluation

This model was evaluated on [SQL-Eval](https://github.com/defog-ai/sql-eval), a PostgreSQL based evaluation framework developed by Defog for testing and alignment of model capabilities.

You can read more about the methodology behind SQLEval [here](https://defog.ai/blog/open-sourcing-sqleval/).

### Results

We classified each generated question into one of 6 categories. The table displays the percentage of questions answered correctly by each model, broken down by category.
|               | date | group_by | order_by | ratio | join | where |
| ------------- | ---- | -------- | -------- | ----- | ---- | ----- |
| sqlcoder-70b  | 96   | 91.4     | 97.1     | 85.7  | 97.1 | 91.4  |
| sqlcoder-34b  | 80   | 94.3     | 85.7     | 77.1  | 85.7 | 80    |
| gpt-4         | 64   | 94.3     | 88.6     | 74.2  | 85.7 | 80    |
| sqlcoder2-15b | 76   | 80       | 77.1     | 60    | 77.1 | 77.1  |
| sqlcoder-7b   | 64   | 82.9     | 74.3     | 54.3  | 74.3 | 74.3  |
| gpt-3.5       | 68   | 77.1     | 74.2     | 34.3  | 65.7 | 71.4  |
| claude-2      | 52   | 71.4     | 74.3     | 57.1  | 65.7 | 62.9  |

## Using SQLCoder

## Model Card Authors

- [Rishabh Srivastava](https://twitter.com/rishdotblog)
- [Wendy Aw](https://www.linkedin.com/in/wendyaw/)
- [Wong Jing Ping](https://www.linkedin.com/in/jing-ping-wong/)

## Model Card Contact

Contact us on X at [@defogdata](https://twitter.com/defogdata), or on email at [founders@defog.ai](mailto:founders@defog.ai)