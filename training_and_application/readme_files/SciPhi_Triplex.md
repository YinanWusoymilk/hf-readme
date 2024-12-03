---
license: cc-by-nc-sa-4.0

---

# Triplex: a SOTA LLM for knowledge graph construction.

Knowledge graphs, like Microsoft's Graph RAG, enhance RAG methods but are expensive to build. Triplex offers a 98% cost reduction for knowledge graph creation, outperforming GPT-4 at 1/60th the cost and enabling local graph building with SciPhi's R2R.

Triplex is a finetuned version of Phi3-3.8B for creating knowledge graphs from unstructured data developed by [SciPhi.AI](https://www.sciphi.ai). It works by extracting triplets - simple statements consisting of a subject, predicate, and object - from text or other data sources. 

![image/png](https://cdn-uploads.huggingface.co/production/uploads/668d8d7a2413acbd544530d1/kcUC5FDEoziMSEcjVHQ3-.png)

## Benchmark

![image/png](https://cdn-uploads.huggingface.co/production/uploads/668d8d7a2413acbd544530d1/xsZ2UPZE5mnTFvgAsQwtl.png)

## Usage:


- **Blog:** [https://www.sciphi.ai/blog/triplex](https://www.sciphi.ai/blog/triplex)
- **Demo:** [kg.sciphi.ai](https://kg.sciphi.ai)
- **Cookbook:** [https://r2r-docs.sciphi.ai/cookbooks/knowledge-graph](https://r2r-docs.sciphi.ai/cookbooks/knowledge-graph)
- **Python:**

```python
import json
from transformers import AutoModelForCausalLM, AutoTokenizer

def triplextract(model, tokenizer, text, entity_types, predicates):

    input_format = """Perform Named Entity Recognition (NER) and extract knowledge graph triplets from the text. NER identifies named entities of given entity types, and triple extraction identifies relationships between entities using specified predicates.
      
        **Entity Types:**
        {entity_types}
        
        **Predicates:**
        {predicates}
        
        **Text:**
        {text}
        """

    message = input_format.format(
                entity_types = json.dumps({"entity_types": entity_types}),
                predicates = json.dumps({"predicates": predicates}),
                text = text)

    messages = [{'role': 'user', 'content': message}]
    input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt = True, return_tensors="pt").to("cuda")
    output = tokenizer.decode(model.generate(input_ids=input_ids, max_length=2048)[0], skip_special_tokens=True)
    return output

model = AutoModelForCausalLM.from_pretrained("sciphi/triplex", trust_remote_code=True).to('cuda').eval()
tokenizer = AutoTokenizer.from_pretrained("sciphi/triplex", trust_remote_code=True)

entity_types = [ "LOCATION", "POSITION", "DATE", "CITY", "COUNTRY", "NUMBER" ]
predicates = [ "POPULATION", "AREA" ]
text = """
San Francisco,[24] officially the City and County of San Francisco, is a commercial, financial, and cultural center in Northern California. 

With a population of 808,437 residents as of 2022, San Francisco is the fourth most populous city in the U.S. state of California behind Los Angeles, San Diego, and San Jose.
"""

prediction = triplextract(model, tokenizer, text, entity_types, predicates)
print(prediction)


```

## Commercial usage
We want Triplex to be as widely accessible as possible, but we also need to keep commercial concerns in mind as we are still an early stage organization. Research and personal usage is fine, but we are placing some restrictions on commercial usage.

The weights for the models are licensed cc-by-nc-sa-4.0, but we will waive them for any organization with under $5M USD in gross revenue in the most recent 12-month period. If you want to remove the GPL license requirements (dual-license) and/or use the weights commercially over the revenue limit, please reach out to our team at founders@sciphi.ai.

## Citation

```
@misc{pimpalgaonkar2024triplex,
author = {Pimpalgaonkar, Shreyas and Tremelling, Nolan and Colegrove, Owen},
title = {Triplex: a SOTA LLM for knowledge graph construction},
year = {2024},
url = {https://huggingface.co/sciphi/triplex}
}
```
