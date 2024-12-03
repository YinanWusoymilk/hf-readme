---
license: apache-2.0
datasets:
- multi_nli
language:
- en
pipeline_tag: text-classification
---

# DeBERTa-v3 (large) fine-tuned to Multi-NLI (MNLI)  
This model is for Textual Entailment (aka NLI), i.e., predict whether `textA` is supported by `textB`. More specifically, it's a 2-way classification where the relationship between `textA` and `textB` can be **entail, neutral, contradict**.  

- Input: (`textA`, `textB`)
- Output: prob(entail), prob(contradict)

Note that during training, all 3 labels (entail, neural, contradict) were used. But for this model, the neural output head has been removed.

## Model Details
- Base model: [deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large)
- Training data: [MNLI](https://huggingface.co/datasets/multi_nli)
- Training details: num_epochs = 3, batch_size = 16, `textA=hypothesis`, `textB=premise`

## Example

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("potsawee/deberta-v3-large-mnli")
model = AutoModelForSequenceClassification.from_pretrained("potsawee/deberta-v3-large-mnli")

textA = "Kyle Walker has a personal issue"
textB = "Kyle Walker will remain Manchester City captain following reports about his private life, says boss Pep Guardiola."

inputs = tokenizer.batch_encode_plus(
    batch_text_or_text_pairs=[(textA, textB)],
    add_special_tokens=True, return_tensors="pt",
)
logits = model(**inputs).logits # neutral is already removed
probs = torch.softmax(logits, dim=-1)[0]
# probs = [0.7080, 0.2920], meaning that prob(entail) = 0.708, prob(contradict) = 0.292
```

## Citation

```bibtex
@article{manakul2023selfcheckgpt,
  title={Selfcheckgpt: Zero-resource black-box hallucination detection for generative large language models},
  author={Manakul, Potsawee and Liusie, Adian and Gales, Mark JF},
  journal={arXiv preprint arXiv:2303.08896},
  year={2023}
}
```