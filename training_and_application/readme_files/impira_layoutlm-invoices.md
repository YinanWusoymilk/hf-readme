---
language: en
license: cc-by-nc-sa-4.0
pipeline_tag: document-question-answering
tags:
 - layoutlm
 - document-question-answering
 - pdf
 - invoices
widget:
- text: "What is the invoice number?"
  src: "https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/invoice.png"
- text: "What is the purchase amount?"
  src: "https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/contract.jpeg"
---

# LayoutLM for Invoices

This is a fine-tuned version of the multi-modal [LayoutLM](https://aka.ms/layoutlm) model for the task of question answering on invoices and other documents. It has been fine-tuned on a proprietary dataset of
invoices as well as both [SQuAD2.0](https://huggingface.co/datasets/squad_v2) and [DocVQA](https://www.docvqa.org/) for general comprehension.

## Non-consecutive tokens

Unlike other QA models, which can only extract consecutive tokens (because they predict the start and end of a sequence), this model can predict longer-range, non-consecutive sequences with an additional
classifier head. For example, QA models often encounter this failure mode:

### Before

![Broken Address](./before.png)


### After

However this model is able to predict non-consecutive tokens and therefore the address correctly:

![Two-line Address](./after.png)

## Getting started with the model

The best way to use this model is via [DocQuery](https://github.com/impira/docquery).

## About us

This model was created by the team at [Impira](https://www.impira.com/).
