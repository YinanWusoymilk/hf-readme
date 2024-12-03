---
license: apache-2.0
---
# notdiamond-0001

notdiamond-0001 automatically determines whether to send queries to GPT-3.5 or GPT-4, depending on which model is best-suited for your task. We've trained notdiamond-0001 on hundreds of thousands of data points from robust, cross-domain evaluation benchmarks.

This router is free to use under the Apache 2.0 license. You can also access a much more powerful router from our [API](https://notdiamond.readme.io/reference/api-introduction) which supports many more models.

The notdiamond-0001 router model is a classifier and will return a label for either GPT-3.5 or GPT-4. You determine which version of each model you want to use and make the calls client-side with your own keys.

To use notdiamond-0001, format your queries using the following prompt with your query appended at the end
``` python
    query = "Can you write a function that counts from 1 to 10?"

    formatted_prompt = f"""Determine whether the following query should be sent to GPT-3.5 or GPT-4.
        Query:
        {query}"""
```


You can then determine the model to call as follows
``` python
    import torch
    from transformers import AutoTokenizer, AutoModelForSequenceClassification

    id2label = {0: 'gpt-3.5', 1: 'gpt-4'}
    tokenizer = AutoTokenizer.from_pretrained("notdiamond/notdiamond-0001")
    model = AutoModelForSequenceClassification.from_pretrained("notdiamond/notdiamond-0001")

    inputs = tokenizer(formatted_prompt, truncation=True, max_length=512, return_tensors="pt")
    logits = model(**inputs).logits
    model_id = logits.argmax().item()
    model_to_call = id2label[model_id]
```
For more details on how you can integrate this into your techstack and use notdiamond-0001 to improve quality while reducing latency and cost, check out our [documentation](https://notdiamond.readme.io/docs/).