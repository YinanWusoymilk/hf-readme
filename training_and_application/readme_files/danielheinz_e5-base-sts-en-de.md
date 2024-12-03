---
license: mit
datasets:
- deutsche-telekom/ger-backtrans-paraphrase
- paws-x
- stsb_multi_mt
language:
- de
model-index:
  - name: e5-base-sts-en-de
    results:
    - task:
        type: semantic textual similarity
      dataset:
        type: stsb_multi_mt
        name: stsb_multi_mt
      metrics:
        - type: spearmanr
          value: 0.904
---
**INFO**: The model is being continuously updated.

The model is a [multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base) model fine-tuned with the task of semantic textual similarity in mind.

## Model Training
The model has been fine-tuned on the German subsets of the following datasets:
- [German paraphrase corpus by Philip May](https://huggingface.co/datasets/deutsche-telekom/ger-backtrans-paraphrase)
- [paws-x](https://huggingface.co/datasets/paws-x)
- [stsb_multi_mt](https://huggingface.co/datasets/stsb_multi_mt)

The training procedure can be divided into two stages:
- training on paraphrase datasets with the Multiple Negatives Ranking Loss
- training on semantic textual similarity datasets using the Cosine Similarity Loss

# Results
The model achieves the following results:
- 0.920 on stsb's validation subset
- 0.904 on stsb's test subset