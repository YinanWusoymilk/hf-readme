---
language:
- en
tags:
- summarization
datasets:
- xsum
metrics:
- rouge
widget:
- text: National Commercial Bank (NCB), Saudi Arabia’s largest lender by assets, agreed
    to buy rival Samba Financial Group for $15 billion in the biggest banking takeover
    this year.NCB will pay 28.45 riyals ($7.58) for each Samba share, according to
    a statement on Sunday, valuing it at about 55.7 billion riyals. NCB will offer
    0.739 new shares for each Samba share, at the lower end of the 0.736-0.787 ratio
    the banks set when they signed an initial framework agreement in June.The offer
    is a 3.5% premium to Samba’s Oct. 8 closing price of 27.50 riyals and about 24%
    higher than the level the shares traded at before the talks were made public.
    Bloomberg News first reported the merger discussions.The new bank will have total
    assets of more than $220 billion, creating the Gulf region’s third-largest lender.
    The entity’s $46 billion market capitalization nearly matches that of Qatar National
    Bank QPSC, which is still the Middle East’s biggest lender with about $268 billion
    of assets.
model-index:
- name: human-centered-summarization/financial-summarization-pegasus
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: xsum
      type: xsum
      config: default
      split: test
    metrics:
    - type: rouge
      value: 35.2055
      name: ROUGE-1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMTA5OTZkY2YxMDU1YzE3NGJlMmE1OTg1NjlmNzcxOTg4YzY2OThlOTlkNGFhMGFjZWY4YjdiMjU5NDdmMWYzNSIsInZlcnNpb24iOjF9.ufBRoV2JoX4UlEfAUOYq7F3tZougwngdpKlnaC37tYXJU3omsR5hTsWM69hSdYO-k0cKUbAWCAMzjmoGwIaPAw
    - type: rouge
      value: 16.5689
      name: ROUGE-2
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOWQwMmM2NjJjNzM1N2Y3NjZmMmE5NzNlNjRjNjEwNzNhNjcyZTRiMGRlODY3NWUyMGQ0YzZmMGFhODYzOTRmOSIsInZlcnNpb24iOjF9.AZZkbaYBZG6rw6-QHYjRlSl-p0gBT2EtJxwjIP7QYH5XIQjeoiQsTnDPIq25dSMDbmQLSZnpHC104ZctX0f_Dg
    - type: rouge
      value: 30.1285
      name: ROUGE-L
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiOTRjYThlMTllZjI4MGFiMDZhZTVkYmRjMTNhZDUzNTQ0OWQyNDQxMmQ5ODJiMmJiNGI3OTAzYjhiMzc2MTI4NCIsInZlcnNpb24iOjF9.zTHd3F4ZlgS-azl-ZVjOckcTrtrJmDOGWVaC3qQsvvn2UW9TnseNkmo7KBc3DJU7_NmlxWZArl1BdSetED0NCg
    - type: rouge
      value: 30.1706
      name: ROUGE-LSUM
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZGMzZGFjNzVkYWI0NTJkMmZjZDQ0YjhiYjIxN2VkNmJjMTgwZTk1NjFlOGU2NjNjM2VjYTNlYTBhNTQ5MGZkNSIsInZlcnNpb24iOjF9.xQ2LoI3PwlEiXo1OT2o4Pq9o2thYCd9lSCKCWlLmZdxI5GxdsjcASBKmHKopzUcwCGBPR7zF95MHSAPyszOODA
    - type: loss
      value: 2.7092134952545166
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMzQzODE0NDc5YTYzYjJlMWU2YTVjOGRjN2JmYWVkOWNkNTRlMTZlOWIyN2NiODJkMDljMjI3YzZmYzM3N2JjYSIsInZlcnNpb24iOjF9.Vv_pdeFuRMoKK3cPr5P6n7D6_18ChJX-2qcT0y4is3XX3mS98fk3U1AYEuy9nBHOwYR3o0U8WBgQ-Ya_FqefBg
    - type: gen_len
      value: 15.1414
      name: gen_len
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiYjk5OTk3NWRiNjZlZmQzMmYwOTU2MmQwOWE1MDNlNTg3YWVkOTgwOTc2ZTQ0MTBiZjliOWMyZTYwMDI2MDUzYiIsInZlcnNpb24iOjF9.Zvj84JzIhM50rWTQ2GrEeOU7HrS8KsILH-8ApTcSWSI6kVnucY0MyW2ODxvRAa_zHeCygFW6Q13TFGrT5kLNAA
---

### PEGASUS for Financial Summarization 

This model was fine-tuned on a novel financial news dataset, which consists of 2K articles from [Bloomberg](https://www.bloomberg.com/europe), on topics such as stock, markets, currencies, rate and cryptocurrencies. 

It is based on the [PEGASUS](https://huggingface.co/transformers/model_doc/pegasus.html) model and in particular PEGASUS fine-tuned on the Extreme Summarization (XSum) dataset: [google/pegasus-xsum model](https://huggingface.co/google/pegasus-xsum). PEGASUS was originally proposed by Jingqing Zhang, Yao Zhao, Mohammad Saleh and Peter J. Liu in [PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization](https://arxiv.org/pdf/1912.08777.pdf). 

*Note: This model serves as a base version. For an even more advanced model with significantly enhanced performance, please check out our [advanced version](https://rapidapi.com/medoid-ai-medoid-ai-default/api/financial-summarization-advanced) on Rapid API. The advanced model offers more than a 16% increase in ROUGE scores (similarity to a human-generated summary) compared to our base model. Moreover, our advanced model also offers several convenient plans tailored to different use cases and workloads, ensuring a seamless experience for both personal and enterprise access.*

### How to use 
We provide a simple snippet of how to use this model for the task of financial summarization in PyTorch.

```Python
from transformers import PegasusTokenizer, PegasusForConditionalGeneration, TFPegasusForConditionalGeneration

# Let's load the model and the tokenizer 
model_name = "human-centered-summarization/financial-summarization-pegasus"
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name) # If you want to use the Tensorflow model 
                                                                    # just replace with TFPegasusForConditionalGeneration


# Some text to summarize here
text_to_summarize = "National Commercial Bank (NCB), Saudi Arabia’s largest lender by assets, agreed to buy rival Samba Financial Group for $15 billion in the biggest banking takeover this year.NCB will pay 28.45 riyals ($7.58) for each Samba share, according to a statement on Sunday, valuing it at about 55.7 billion riyals. NCB will offer 0.739 new shares for each Samba share, at the lower end of the 0.736-0.787 ratio the banks set when they signed an initial framework agreement in June.The offer is a 3.5% premium to Samba’s Oct. 8 closing price of 27.50 riyals and about 24% higher than the level the shares traded at before the talks were made public. Bloomberg News first reported the merger discussions.The new bank will have total assets of more than $220 billion, creating the Gulf region’s third-largest lender. The entity’s $46 billion market capitalization nearly matches that of Qatar National Bank QPSC, which is still the Middle East’s biggest lender with about $268 billion of assets."

# Tokenize our text
# If you want to run the code in Tensorflow, please remember to return the particular tensors as simply as using return_tensors = 'tf'
input_ids = tokenizer(text_to_summarize, return_tensors="pt").input_ids

# Generate the output (Here, we use beam search but you can also use any other strategy you like)
output = model.generate(
    input_ids, 
    max_length=32, 
    num_beams=5, 
    early_stopping=True
)

# Finally, we can print the generated summary
print(tokenizer.decode(output[0], skip_special_tokens=True))
# Generated Output: Saudi bank to pay a 3.5% premium to Samba share price. Gulf region’s third-largest lender will have total assets of $220 billion
```

## Evaluation Results
The results before and after the fine-tuning on our dataset are shown below:


| Fine-tuning |  R-1  |  R-2  |  R-L   |  R-S  |
|:-----------:|:-----:|:-----:|:------:|:-----:|
| Yes         | 23.55 |  6.99 | 18.14  | 21.36 | 
| No          | 13.8  |  2.4  | 10.63  | 12.03 |


## Citation

You can find more details about this work in the following workshop paper. If you use our model in your research, please consider citing our paper:

> T. Passali, A. Gidiotis, E. Chatzikyriakidis and G. Tsoumakas. 2021. 
> Towards Human-Centered Summarization: A Case Study on Financial News.
> In Proceedings of the First Workshop on Bridging Human-Computer Interaction and Natural Language Processing(pp. 21–27). Association for Computational Linguistics.

BibTeX entry:

```
@inproceedings{passali-etal-2021-towards,
    title = "Towards Human-Centered Summarization: A Case Study on Financial News",
    author = "Passali, Tatiana  and Gidiotis, Alexios  and Chatzikyriakidis, Efstathios  and Tsoumakas, Grigorios",
    booktitle = "Proceedings of the First Workshop on Bridging Human{--}Computer Interaction and Natural Language Processing",
    month = apr,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2021.hcinlp-1.4",
    pages = "21--27",
}
```

## Support

Contact us at [info@medoid.ai](mailto:info@medoid.ai) if you are interested in a more sophisticated version of the model, trained on more articles and adapted to your needs!

More information about Medoid AI: 
- Website: [https://www.medoid.ai](https://www.medoid.ai)
- LinkedIn: [https://www.linkedin.com/company/medoid-ai/](https://www.linkedin.com/company/medoid-ai/)


