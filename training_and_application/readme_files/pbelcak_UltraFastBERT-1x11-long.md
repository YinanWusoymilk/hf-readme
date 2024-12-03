---
license: mit
datasets:
- EleutherAI/pile
language:
- en
metrics:
- glue
---

# UltraFastBERT-1x11-long

This is the final model described in "Exponentially Faster Language Modelling".
The model has been pretrained just like crammedBERT but with fast feedforward networks (FFF) in place of the traditional feedforward layers.
To use this model, you need the code from the repo at https://github.com/pbelcak/UltraFastBERT.

You can find the paper here: https://arxiv.org/abs/2311.10770, and the abstract below:

> Language models only really need to use an exponential fraction of their neurons for individual inferences. 
> As proof, we present UltraFastBERT, a BERT variant that uses 0.3% of its neurons during inference while performing on par with similar BERT models. UltraFastBERT selectively engages just 12 out of 4095 neurons for each layer inference. This is achieved by replacing feedforward networks with fast feedforward networks (FFFs).
> While no truly efficient implementation currently exists to unlock the full acceleration potential of conditional neural execution, we provide high-level CPU code achieving 78x speedup over the optimized baseline feedforward implementation, and a PyTorch implementation delivering 40x speedup over the equivalent batched feedforward inference. We publish our training code, benchmarking setup, and model weights.


## Intended uses & limitations

This is the raw pretraining checkpoint. You can use this to fine-tune on a downstream task like GLUE as discussed in the paper. This model is provided only as sanity check for research purposes, it is untested and unfit for deployment.

### How to get started

1. Create a new Python/conda environment, or simply use one that does not have any previous version of the original `cramming` project installed. If, by accident, you use the original cramming repository code instead of the one provided in the `/training` folder of this project, you will be warned by `transformers` that there are some extra weights (FFF weight) and that some weights are missing (the FF weights expected by the original `crammedBERT`).
2. `cd ./training`
3. `pip install .`
4. Create `minimal_example.py`
5. Paste the code below

```python
import cramming
from transformers import AutoModelForMaskedLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("pbelcak/UltraFastBERT-1x11-long")
model = AutoModelForMaskedLM.from_pretrained("pbelcak/UltraFastBERT-1x11-long")

text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

6. Run `python minimal_example.py`.


### Limitations and bias

The training data used for this model was further filtered and sorted beyond the normal Pile. These modifications were not tested for unintended consequences.

## Training data, Training procedure, Preprocessing, Pretraining

These are discussed in the paper. You can find the final configurations for each in this repository.

## Evaluation results

When fine-tuned on downstream tasks, this model achieves the following results:

Glue test results:

| Task | MNLI-(m-mm) | QQP  | QNLI | SST-2 | STS-B | MRPC | RTE  | Average |
|:----:|:-----------:|:----:|:----:|:-----:|:-----:|:----:|:----:|:-------:|
| Score|  81.3       | 87.6 | 89.7 | 89.9  | 86.4  | 87.5 | 60.7 | 83.0    |

These numbers are the median over 5 trials on "GLUE-sane" using the GLUE-dev set. With this variant of GLUE, finetuning cannot be longer than 5 epochs on each task, and hyperparameters have to be chosen equal for all tasks.

### BibTeX entry and citation info

```bibtex
@article{belcak2023exponential,
  title = {Exponentially {{Faster}} {{Language}} {{Modelling}}},
  author = {Belcak, Peter and Wattenhofer, Roger},
  year = {2023},
  month = nov,
  eprint = {2311.10770},
  eprinttype = {arxiv},
  primaryclass = {cs},
  publisher = {{arXiv}},
  url = {https://arxiv.org/pdf/2311.10770},
  urldate = {2023-11-21},
  archiveprefix = {arXiv},
  keywords = {Computer Science - Computation and Language,Computer Science - Machine Learning},
  journal = {arxiv:2311.10770[cs]}
}
```