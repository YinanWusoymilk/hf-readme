---
license: mit
datasets:
- bigbio/chemdner
- ncbi_disease
- jnlpba
- bigbio/n2c2_2018_track2
- bigbio/bc5cdr
widget:
- text: Drug<SEP>He was given aspirin and paracetamol.
language:
- en
metrics:
- precision
- recall
- f1
pipeline_tag: token-classification
tags:
- token-classification
- biology
- medical
- zero-shot
- few-shot
library_name: transformers
---
# Zero and few shot NER for biomedical texts

## Model description

This model was created during the research collaboration between Bayer Pharma and Serbian Institute for Artificial Intelligence Research and Development. 
The model is trained on about 25+ biomedical NER classes and can perform also zero-shot inference and can be further fine-tuned for new classes with just few examples (few-shot learning). 
For more details about our methods please see the paper named ["A transformer-based method for zero and few-shot biomedical named entity recognition"](https://arxiv.org/abs/2305.04928). The model corresponds to BioBERT-based mode, trained with 1 in the first segment (check paper for more details).

Model takes as input two strings. String1 is NER label that is being searched in second string. String1 must be phrase for entity. String2 is short text where String1 is searched for semantically.
model outputs list of zeros and ones corresponding to the occurance of Named Entity and corresponing to the tokens(tokens given by transformer tokenizer) of the Sring2.

## Example of usage
```python
from transformers import AutoTokenizer
from transformers import BertForTokenClassification

modelname = 'ProdicusII/ZeroShotBioNER'  # modelpath
tokenizer = AutoTokenizer.from_pretrained(modelname)  ## loading the tokenizer of that model
string1 = 'Drug'
string2 = 'No recent antibiotics or other nephrotoxins, and no symptoms of UTI with benign UA.'
encodings = tokenizer(string1, string2, is_split_into_words=False,
                      padding=True, truncation=True, add_special_tokens=True, return_offsets_mapping=False,
                      max_length=512, return_tensors='pt')

model0 = BertForTokenClassification.from_pretrained(modelname, num_labels=2)
prediction_logits = model0(**encodings)
print(prediction_logits)
```

## Example of fine-tuning with few-shot learning

In order to fine-tune model to the new entity using few shots, the dataset needs to be transformed to torch.utils.data.Dataset, containing BERT tokens and set of 0s and 1s (1 is where the class is positive and should be predicted as the member of given NER class). After the dataset is created, the following can be done (for more details, please have a look at the code at GitHub - https://github.com/br-ai-ns-institute/Zero-ShotNER): 

```python
 training_args = TrainingArguments(
        output_dir=os.path.join('Results', class_unseen, str(j)+'Shot'),  # folder for results
        num_train_epochs=10,                                              # number of epochs
        per_device_train_batch_size=16,                                   # batch size per device during training
        per_device_eval_batch_size=16,                                    # batch size for evaluation
        weight_decay=0.01,                                                # strength of weight decay
        logging_dir=os.path.join('Logs', class_unseen, str(j)+'Shot'),    # folder for logs
        save_strategy='epoch',
        evaluation_strategy='epoch',
        load_best_model_at_end=True,
    )
    
model0 = BertForTokenClassification.from_pretrained(model_path, num_labels=2)
trainer = Trainer(
    model=model0,                # pretrained model
    args=training_args,          # training artguments
    train_dataset=dataset,       # Object of class torch.utils.data.Dataset for training
    eval_dataset=dataset_valid   # Object of class torch.utils.data.Dataset for vaLidation
    )
start_time = time.time()
trainer.train()
total_time = time.time()-start_time
model0_path = os.path.join('Results', class_unseen, str(j)+'Shot', 'Model')
os.makedirs(model0_path, exist_ok=True)
trainer.save_model(model0_path)
```

## Available classes

The following datasets and entities were used for training and therefore they can be used as label in the first segment (as a first string). Note that multiword string have been merged.


* NCBI
  * Specific Disease 
  * Composite Mention 
  * Modifier 
  * Disease Class
* BIORED
  * Sequence Variant 
  * Gene Or Gene Product 
  * Disease Or Phenotypic Feature 
  * Chemical Entity 
  * Cell Line 
  * Organism Taxon 
* CDR
  * Disease 
  * Chemical
* CHEMDNER
  * Chemical
  * Chemical Family
* JNLPBA
  * Protein
  * DNA 
  * Cell Type 
  * Cell Line 
  * RNA 
* n2c2
  * Drug
  * Frequency 
  * Strength
  * Dosage
  * Form
  * Reason
  * Route
  * ADE 
  * Duration

On top of this, one can use the model in zero-shot regime with other classes, and also fine-tune it with few examples of other classes. 



## Code availibility

Code used for training and testing the model is available at https://github.com/br-ai-ns-institute/Zero-ShotNER 

## Citation

If you use this model, or are inspired by it, please cite in your paper the following paper: 

Košprdić M.,Prodanović N., Ljajić A., Bašaragin B., Milošević N., 2023. A transformer-based method for zero and few-shot biomedical named entity recognition. arXiv preprint arXiv:2305.04928. https://arxiv.org/abs/2305.04928

or in bibtex:
```
@misc{kosprdic2023transformerbased,
      title={A transformer-based method for zero and few-shot biomedical named entity recognition}, 
      author={Miloš Košprdić and Nikola Prodanović and Adela Ljajić and Bojana Bašaragin and Nikola Milošević},
      year={2023},
      eprint={2305.04928},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```