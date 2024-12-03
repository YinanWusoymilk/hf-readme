---
language: en
license: apache-2.0
tags:
- transformers
- bart
- paraphrase
- seq2seq
datasets:
- quora
- paws
---
# BART Paraphrase Model (Large)
A large BART seq2seq (text2text generation) model fine-tuned on 3 paraphrase datasets.

## Model description
The BART model was proposed in [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/abs/1910.13461) by Lewis et al. (2019).

- Bart uses a standard seq2seq/machine translation architecture with a bidirectional encoder (like BERT) and a left-to-right decoder (like GPT).
- The pretraining task involves randomly shuffling the order of the original sentences and a novel in-filling scheme, where spans of text are replaced with a single mask token.
- BART is particularly effective when fine tuned for text generation. This model is fine-tuned on 3 paraphrase datasets (Quora, PAWS and MSR paraphrase corpus).

The original BART code is from this [repository](https://github.com/pytorch/fairseq/tree/master/examples/bart).

## Intended uses & limitations
You can use the pre-trained model for paraphrasing an input sentence.
### How to use
```python
import torch
from transformers import BartForConditionalGeneration, BartTokenizer

input_sentence = "They were there to enjoy us and they were there to pray for us."

model = BartForConditionalGeneration.from_pretrained('eugenesiow/bart-paraphrase')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
tokenizer = BartTokenizer.from_pretrained('eugenesiow/bart-paraphrase')
batch = tokenizer(input_sentence, return_tensors='pt')
generated_ids = model.generate(batch['input_ids'])
generated_sentence = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

print(generated_sentence)
```
### Output
```
['They were there to enjoy us and to pray for us.']
```
## Training data
The model was fine-tuned on a pretrained [`facebook/bart-large`](https://huggingface.co/facebook/bart-large), using the [Quora](https://huggingface.co/datasets/quora), [PAWS](https://huggingface.co/datasets/paws) and [MSR paraphrase corpus](https://www.microsoft.com/en-us/download/details.aspx?id=52398). 
## Training procedure

We follow the training procedure provided in the [simpletransformers](https://github.com/ThilinaRajapakse/simpletransformers) seq2seq [example](https://github.com/ThilinaRajapakse/simpletransformers/blob/master/examples/seq2seq/paraphrasing/train.py).

## BibTeX entry and citation info
```bibtex
@misc{lewis2019bart,
      title={BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension}, 
      author={Mike Lewis and Yinhan Liu and Naman Goyal and Marjan Ghazvininejad and Abdelrahman Mohamed and Omer Levy and Ves Stoyanov and Luke Zettlemoyer},
      year={2019},
      eprint={1910.13461},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```