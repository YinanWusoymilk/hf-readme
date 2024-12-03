---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
- bert-base-uncased
- text-classification
- fp32 
datasets:
- glue
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-mrpc
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: GLUE MRPC
      type: glue
      args: mrpc
    metrics:
    - type: accuracy
      value: 0.8602941176470589
      name: Accuracy
    - type: f1
      value: 0.9042016806722689
      name: F1
  - task:
      type: natural-language-inference
      name: Natural Language Inference
    dataset:
      name: glue
      type: glue
      config: mrpc
      split: validation
    metrics:
    - type: accuracy
      value: 0.8602941176470589
      name: Accuracy
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZWMzOWFiNmZjY2ZjMzYzYjk2YjA2ZTc0NjBmYmRlMWM4YWQwMzczYmU0NjcxNjU4YWNhMGMxMjQxNmEwNzM3NSIsInZlcnNpb24iOjF9.5c8Um2j-oDEviTR2S_mlrjQU2Z5zEIgoEldxU6NpIGkM22WhGRMmuCUlkPEpy1q2-HsA4Lz16SAF2bXOXZMqBw
    - type: precision
      value: 0.8512658227848101
      name: Precision
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiNzA0MjM4OGYyYmNhYTU3OTBmNzE3YzViNzQyZTk2NmJiODE2NGJkZGVlMTYxZGQzOWE1YTRkZjZmNjI5ODljNyIsInZlcnNpb24iOjF9.mzDbq7IbSFWnlR6jV-KwuNhOrqnuZVVQX38UzQVClox6O1DRmxAFuo3wmSYBEEaydGipdDN1FAkLXDyZP4LFBg
    - type: recall
      value: 0.96415770609319
      name: Recall
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMDMxMzUyZDVhNGM0ZTk3NjUxYTVlYmRjYjMxZTY3NjEzZmU5YzA5NTRmZTM3YTU1MjE3MzBmYjA1NzhkNjJlYSIsInZlcnNpb24iOjF9.WxpDTp5ANy97jjbzn4BOeQc5A5JJsyK2NQDv651v7J8AHrt_Srvy5lVia_gyWgqt4bI-ZpPPmBCCCP9MdOhdBw
    - type: auc
      value: 0.8985718651885194
      name: AUC
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiMWE3ZDc1ZWMwY2RmZmM4ZjQyY2RiMGJjMzFmNmNjNzVmMzE4Y2FlMzJjNzk0MTI3YjdkMTY5ZDg3ZGZjMGFkNSIsInZlcnNpb24iOjF9.PiS1glSDlAM9r7Pvu0FdTCdx45Dr_IDe7TRuZD8QhJzKw__H-Lil5bkBW-FsoN6hKQe80-qtuhLhvLwlZPORCA
    - type: f1
      value: 0.9042016806722689
      name: F1
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiY2FiOTY2MDI1ZDcyYjE3OGVjOGJjOTc3NGRiODgwNzQxNTEzOGM4YTJhMDE0NjRlNjg1ODk0YzM5YTY0NTQxYSIsInZlcnNpb24iOjF9.gz3szT-MroNcsPhMznhg0kwgWsIa1gfJi8vrhcFMD0PK6djlvZIVKoAS2QE-1cgqPMph7AJXTLifQuPgPBQLDA
    - type: loss
      value: 0.6978028416633606
      name: loss
      verified: true
      verifyToken: eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJoYXNoIjoiZDZjODM1NGYyZWMyNDQxOTg0ODkxODgyODcxMzRlZTVjMTc5YjU3MDJmMGMzYzczZDU1Y2NjNTYwYjM2MDEzZiIsInZlcnNpb24iOjF9.eNSy3R0flowu2c4OEAv9rayTQI4YluNN-AuXKzBJM6KPASzuVOD6vTElHMptXiJWc-2tfHJw6CdvyAQSEGTaBg
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-mrpc

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the **GLUE MRPC dataset**. The GLUE MRPC dataset, from The [Microsoft Research Paraphrase Corpus (Dolan & Brockett, 2005)](https://www.tensorflow.org/datasets/catalog/glue) is a corpus of sentence pairs automatically extracted from online news sources, with human annotations for whether the sentences in the pair are semantically equivalent.

It is a pretrained model on English language using a masked language modeling (MLM) objective. It was introduced in this paper [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805). 
This model, bert-base-uncased-mrpc, is uncased: it does not make a difference between **"english"** and **"English"**. Masked language modeling predicts a masked token in a sequence, and the model can attend to tokens bidirectionally. This means the model has full access to the tokens on the left and right. Masked language modeling is great for tasks that require a good contextual understanding of an entire sequence. BERT is an example of a masked language model. For this model, you don’t need labels (also known as an unsupervised task) because the next word (MLM) is the label
BERT base model (uncased)

It provides:
 - Masked language modeling (MLM): taking a sentence, the model randomly masks 15% of the words in the input then run the entire masked sentence through the model and has to predict the masked words. This is different from traditional recurrent neural networks (RNNs) that usually see the words one after the other, or from autoregressive models like GPT which internally masks the future tokens. It allows the model to learn a bidirectional representation of the sentence.
 - Next sentence prediction (NSP): the models concatenates two masked sentences as inputs during pretraining. Sometimes they correspond to sentences that were next to each other in the original text, sometimes not. The model then has to predict if the two sentences were following each other or not.

# Results
It achieves the following results on the evaluation set:
- Loss: 0.6978
- Accuracy: 0.8603
- F1: 0.9042
- Combined Score: 0.8822

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu102
- Datasets 1.14.0
- Tokenizers 0.11.6

# To use:
```python
from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained('Intel/bert-base-uncased-mrpc')
model = BertModel.from_pretrained("Intel/bert-base-uncased-mrpc")
text = "The inspector analyzed the soundness in the building."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
# print BaseModelOutputWithPoolingAndCrossAttentions and  pooler_output

# Print tokens * ids in of inmput string below
print('Tokenized Text: ', tokenizer.tokenize(text), '\n')
print('Token IDs: ', tokenizer.convert_tokens_to_ids(tokenizer.tokenize(text)))

#Print tokens in text
encoded_input['input_ids'][0]
tokenizer.convert_ids_to_tokens(encoded_input['input_ids'][0])
```
# Output similar to:
```python
BaseModelOutputWithPoolingAndCrossAttentions(last_hidden_state=tensor([[[ 0.0219,  0.1258, -0.8529,  ...,  0.6416,  0.6275,  0.5583],
         [ 0.3125, -0.1921, -0.9895,  ...,  0.6069,  1.8431, -0.5939],
         [ 0.6147, -0.6098, -0.3517,  ..., -0.1145,  1.1748, -0.7104],
         ...,
         [ 0.8959, -0.2324, -0.6311,  ...,  0.2424,  0.1025,  0.2101],
         [ 0.2484, -0.3004, -0.9474,  ...,  1.0401,  0.5493, -0.4170],
         [ 0.8206,  0.2023, -0.7929,  ...,  0.7073,  0.0779, -0.2781]]],
       grad_fn=<NativeLayerNormBackward0>), pooler_output=tensor([[-0.7867,  0.1878, -0.8186,  0.8494,  0.4263,  0.5157,  0.9564,  0.1514,
         -0.9176, -0.9994,  0.2962,  0.2891, -0.3301,  0.8786,  0.9234, -0.7643,
          0.2487, -0.5245, -0.0649, -0.6722,  0.8550,  1.0000, -0.7785,  0.5322,
          0.6056,  0.4622,  0.2838,  0.5501,  0.6981,  0.2597, -0.7896, -0.1189,
```

# Related work on QuantizationAwareTraining
An Int8 Quantized version of this model can be found [link](https://huggingface.co/Intel/bert-base-uncased-mrpc-int8-qat-inc)

This is an INT8 PyTorch model quantized with huggingface/optimum-intel through the usage of Intel® Neural Compressor.

# Ethical Considerations and Limitations
bert-base-uncased-mrpc can produce factually incorrect output, and should not be relied on to produce factually accurate information. Because of the limitations of the pretrained model and the finetuning datasets, it is possible that this model could generate lewd, biased or otherwise offensive outputs.

Therefore, before deploying any applications of bert-base-uncased-mrpc, developers should perform safety testing.

# Caveats and Recommendations
Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model.

Here are a couple of useful links to learn more about Intel's AI software:

- Intel Neural Compressor [link](https://github.com/intel/neural-compressor)
- Intel Extension for Transformers [link](https://github.com/intel/intel-extension-for-transformers)

# Disclaimer
The license on this model does not constitute legal advice. We are not responsible for the actions of third parties who use this model. Please cosult an attorney before using this model for commercial purposes.

# BibTeX entry and citation info
```bibtex
@article{DBLP:journals/corr/abs-1810-04805,
  author    = {Jacob Devlin and
               Ming{-}Wei Chang and
               Kenton Lee and
               Kristina Toutanova},
  title     = {{BERT:} Pre-training of Deep Bidirectional Transformers for Language
               Understanding},
  journal   = {CoRR},
  volume    = {abs/1810.04805},
  year      = {2018},
  url       = {http://arxiv.org/abs/1810.04805},
  archivePrefix = {arXiv},
  eprint    = {1810.04805},
  timestamp = {Tue, 30 Oct 2018 20:39:56 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1810-04805.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}