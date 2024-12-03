---
tags:
- summarization
language:
- en
license: mit
model-index:
- name: facebook/bart-large-xsum
  results:
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      config: 3.0.0
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 25.2697
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 7.6638
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 17.1808
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 21.7933
      verified: true
    - name: loss
      type: loss
      value: 3.5042972564697266
      verified: true
    - name: gen_len
      type: gen_len
      value: 27.4462
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: xsum
      type: xsum
      config: default
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 45.4525
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 22.3455
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 37.2302
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 37.2323
      verified: true
    - name: loss
      type: loss
      value: 2.3128726482391357
      verified: true
    - name: gen_len
      type: gen_len
      value: 25.5435
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: samsum
      type: samsum
      config: samsum
      split: train
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 24.7852
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 5.2533
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 18.6792
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 20.629
      verified: true
    - name: loss
      type: loss
      value: 3.746837854385376
      verified: true
    - name: gen_len
      type: gen_len
      value: 23.1206
      verified: true
  - task:
      type: summarization
      name: Summarization
    dataset:
      name: samsum
      type: samsum
      config: samsum
      split: test
    metrics:
    - name: ROUGE-1
      type: rouge
      value: 24.9158
      verified: true
    - name: ROUGE-2
      type: rouge
      value: 5.5837
      verified: true
    - name: ROUGE-L
      type: rouge
      value: 18.8935
      verified: true
    - name: ROUGE-LSUM
      type: rouge
      value: 20.76
      verified: true
    - name: loss
      type: loss
      value: 3.775235891342163
      verified: true
    - name: gen_len
      type: gen_len
      value: 23.0928
      verified: true
---
### Bart model finetuned on xsum

docs: https://huggingface.co/transformers/model_doc/bart.html

finetuning: examples/seq2seq/ (as of Aug 20, 2020)

Metrics: ROUGE > 22 on xsum.

variants: search for distilbart

paper: https://arxiv.org/abs/1910.13461