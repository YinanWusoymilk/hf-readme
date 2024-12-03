---
license: other
license_name: public-domain
license_link: LICENSE
---

# Usage: Ranking articles for a given query

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ncbi/MedCPT-Cross-Encoder")
model = AutoModelForSequenceClassification.from_pretrained("ncbi/MedCPT-Cross-Encoder")

query = "diabetes treatment"

# 6 articles to be ranked for the input query
articles = [
	"Type 1 and 2 diabetes mellitus: A review on current treatment approach and gene therapy as potential intervention. Type 1 and type 2 diabetes mellitus is a serious and lifelong condition commonly characterised by abnormally elevated blood glucose levels due to a failure in insulin production or a decrease in insulin sensitivity and function. [...]",
	"Diabetes mellitus and its chronic complications. Diabetes mellitus is a major cause of morbidity and mortality, and it is a major risk factor for early onset of coronary heart disease. Complications of diabetes are retinopathy, nephropathy, and peripheral neuropathy. [...]",
	"Diagnosis and Management of Central Diabetes Insipidus in Adults. Central diabetes insipidus (CDI) is a clinical syndrome which results from loss or impaired function of vasopressinergic neurons in the hypothalamus/posterior pituitary, resulting in impaired synthesis and/or secretion of arginine vasopressin (AVP). [...]",
	"Adipsic diabetes insipidus. Adipsic diabetes insipidus (ADI) is a rare but devastating disorder of water balance with significant associated morbidity and mortality. Most patients develop the disease as a result of hypothalamic destruction from a variety of underlying etiologies. [...]",
	"Nephrogenic diabetes insipidus: a comprehensive overview. Nephrogenic diabetes insipidus (NDI) is characterized by the inability to concentrate urine that results in polyuria and polydipsia, despite having normal or elevated plasma concentrations of arginine vasopressin (AVP). [...]",
	"Impact of Salt Intake on the Pathogenesis and Treatment of Hypertension. Excessive dietary salt (sodium chloride) intake is associated with an increased risk for hypertension, which in turn is especially a major risk factor for stroke and other cardiovascular pathologies, but also kidney diseases. Besides, high salt intake or preference for salty food is discussed to be positive associated with stomach cancer, and according to recent studies probably also obesity risk. [...]"
]

# combine query article into pairs
pairs = [[query, article] for article in articles]

with torch.no_grad():
	encoded = tokenizer(
		pairs,
		truncation=True,
		padding=True,
		return_tensors="pt",
		max_length=512,
	)

	logits = model(**encoded).logits.squeeze(dim=1)
	
	print(logits)
```

The output will be
```bash
tensor([  6.9363,  -8.2063,  -8.7692, -12.3450, -10.4416, -15.8475])
```
Higher scores indicate higher relevance.

# Acknowledgments

This work was supported by the Intramural Research Programs of the National Institutes of Health, National Library of Medicine.

# Disclaimer

This tool shows the results of research conducted in the Computational Biology Branch, NCBI/NLM. The information produced on this website is not intended for direct diagnostic use or medical decision-making without review and oversight by a clinical professional. Individuals should not change their health behavior solely on the basis of information produced on this website. NIH does not independently verify the validity or utility of the information produced by this tool. If you have questions about the information produced on this website, please see a health care professional. More information about NCBI's disclaimer policy is available.

# Citation

If you find this repo helpful, please cite MedCPT by:
```bibtext
@article{jin2023medcpt,
  title={MedCPT: Contrastive Pre-trained Transformers with large-scale PubMed search logs for zero-shot biomedical information retrieval},
  author={Jin, Qiao and Kim, Won and Chen, Qingyu and Comeau, Donald C and Yeganova, Lana and Wilbur, W John and Lu, Zhiyong},
  journal={Bioinformatics},
  volume={39},
  number={11},
  pages={btad651},
  year={2023},
  publisher={Oxford University Press}
}
```