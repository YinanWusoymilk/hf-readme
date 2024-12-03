---
license: mit
language:
- en
pipeline_tag: token-classification
---

 A finetuned model designed to recognize and classify Personally Identifiable Information (PII) within unstructured text data. This powerful model accurately identifies a wide range of PII categories, such as account names, credit card numbers, emails, phone numbers, and addresses. The model is specifically trained to detect various PII types, including but not limited to:

```
| Category               | Data                                                                                   |
|------------------------|----------------------------------------------------------------------------------------|
| Account-related information | Account name, account number, and transaction amounts                             |
| Banking details        | BIC, IBAN, and Bitcoin or Ethereum addresses                                           |
| Personal information   | Full name, first name, middle name, last name, gender, and date of birth               |
| Contact information    | Email, phone number, and street address (including building number, city, county, state, and zip code) |
| Job-related data       | Job title, job area, job descriptor, and job type                                      |
| Financial data         | Credit card number, issuer, CVV, and currency information (code, name, and symbol)     |
| Digital identifiers    | IP addresses (IPv4 and IPv6), MAC addresses, and user agents                           |
| Online presence        | URL, usernames, and passwords                                                          |
| Other sensitive data   | SSN, vehicle VIN and VRM, phone IMEI, and nearby GPS coordinates                       |
```


The PII Identifier Model ensures data privacy and compliance by effectively detecting and categorizing sensitive information within documents, emails, user-generated content, and more. Make your data processing safer and more secure with our state-of-the-art PII detection technology.

How to do Inference :

```
from transformers import pipeline
gen = pipeline("token-classification", "lakshyakh93/deberta_finetuned_pii", device=-1)

text = "My name is John and I live in California."
output = gen(text, aggregation_strategy="first")
```

For any more details reach out to lakshaya.khandelwal@gmail.com
