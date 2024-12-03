---
license: apache-2.0
pipeline_tag: text-generation
widget:
- text: 1.1.1.21<sep><start>
inference:
  parameters:
    top_k: 9
    repetition_penalty: 1.2
tags:
- biology
---
# **ZymCTRL**

ZymCTRL (Enzyme Control) ([ see preprint ](https://www.biorxiv.org/content/10.1101/2024.05.03.592223v1)) 
is a conditional language model for the generation of artificial functional enzymes. 
It was trained on the UniProt database of sequences containing (Enzyme Commission) EC annotations, comprising over 37 M sequences. 
Given a user-defined Enzymatic Commission (EC) number, the model generates protein sequences that fulfil that catalytic reaction. 
The generated sequences are ordered, globular, and distant to natural ones, while their intended catalytic properties match those defined by users.

If you don't know the EC number of your protein of interest, have a look for example here: https://www.brenda-enzymes.org/ecexplorer.php?browser=1

See below for information about the model, how to generate sequences, and how to save and rank them by perplexity.

## **Model description**
ZymCTRL is based on the [CTRL Transformer](https://arxiv.org/abs/1909.05858) architecture (which in turn is very similar to ChatGPT) and contains 36 layers
with a model dimensionality of 1280, totaling 738 million parameters. 

ZymCTRL is a decoder-only transformer model pre-trained on the Uniprot subset of enzyme sequences, totalling 37M sequences.
(version July 2022). The pre-training was done on the raw sequences without FASTA headers,
with the EC classes prepended to each sequence. The databases will be uploaded soon.

ZymCTRL was trained with an autoregressive objective, i.e., the model learns to predict
the next token given a sequence context. Because the first tokens on each sequence encode the EC numbers,
the model learns the dependencies among EC classes and their corresponding sequences and is able to _speak_ the enzyme language.

There are stark differences in the number of members among EC classes, and for this reason, we also tokenized the EC numbers.
In this manner, EC numbers '2.7.1.1' and '2.7.1.2' share the first three tokens (six, including separators), and hence the model can infer that
there are relationships between the two classes.

The figure below summarizes the process of training:

![plot](./github1.png)

 
## **How to use ZymCTRL**
ZymCTRL can be used with the HuggingFace transformer python package.
Detailed installation instructions can be found here: https://huggingface.co/docs/transformers/installation

Since ZymCTRL has been trained on the classical language model objective on enzyme sequences with their EC annotation,
it particularly excels at generating enzyme sequences given a user-defined EC class, such as alcohol dehydrogenases ('1.1.1.2').

The model can generate in two ways: in a zero-shot fashion, i.e., directly generating from the checkpoint weights, or after fine-tuning. 
Fine-tuning allows augmenting the specific EC datasets that were used during training, for example, 
if you have a curated internal dataset or a set of ancestrally-reconstructed sequences. This is entirely optional. One advantage of 
running the model in zero-shot is that it doesn't require any further training.


### **Example 1: Generating nitrilases (EC 3.5.5.1)**  

The script below will be used for the generation of any EC class in a zero-shot fashion, 
here we showcase the generation of novel nitrilases.

To run this script, you should download ZymCTRL to a local folder in your workstation. 
Then replace the placeholders in the script with your actual folder path.

You can run it directly in the command line (once you have hugging face installed), 
with the following command: `python generate.py`

The script will write each sequence in a fasta file in the folder you specify. In the fasta header,
it will store the sequence's computed perplexity value. Perplexity is a measure of the model's confidence
in that generation, with lower values being better. The sequences are ordered by perplexity before writing them out,
so those that finish in *_0.fasta and *_1.fasta will be the best ones per batch. 

**Given that generation runs so fast, we recommend generating hundreds or thousands and then only picking the best 5% or less. 
With the script below, that would mean picking only those that finish in '_0.fasta'. Good perplexity values for this model so be below 1.75-1.5.** 

```
import torch
from transformers import GPT2LMHeadModel, AutoTokenizer
import os
from tqdm import tqdm
import math

def remove_characters(sequence, char_list):
    "This function removes special tokens used during training."
    columns = sequence.split('<sep>')
    seq = columns[1]
    for char in char_list:
        seq = seq.replace(char, '')
    return seq

def calculatePerplexity(input_ids,model,tokenizer):
    "This function computes perplexities for the generated sequences"
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
    loss, logits = outputs[:2]
    return math.exp(loss)
        
def main(label, model,special_tokens,device,tokenizer):
    # Generating sequences
    input_ids = tokenizer.encode(label,return_tensors='pt').to(device)
    outputs = model.generate(
        input_ids, 
    	top_k=9, #tbd
        repetition_penalty=1.2,
        max_length=1024,
        eos_token_id=1,
        pad_token_id=0,
   	    do_sample=True,
   	    num_return_sequences=20) # Depending non your GPU, you'll be able to generate fewer or more sequences. This runs in an A40.
    
    # Check sequence sanity, ensure sequences are not-truncated.
    # The model will truncate sequences longer than the specified max_length (1024 above). We want to avoid those sequences.
    new_outputs = [ output for output in outputs if output[-1] == 0]
    if not new_outputs:
        print("not enough sequences with short lengths!!")

    # Compute perplexity for every generated sequence in the batch
    ppls = [(tokenizer.decode(output), calculatePerplexity(output, model, tokenizer)) for output in new_outputs ]

    # Sort the batch by perplexity, the lower the better
    ppls.sort(key=lambda i:i[1]) # duplicated sequences?

    # Final dictionary with the results
    sequences={}
    sequences[label] = [(remove_characters(x[0], special_tokens), x[1]) for x in ppls]

    return sequences

if __name__=='__main__':
    device = torch.device("cuda") # Replace with 'cpu' if you don't have a GPU - but it will be slow
    print('Reading pretrained model and tokenizer')
    tokenizer = AutoTokenizer.from_pretrained('/path/to/zymCTRL/') # change to ZymCTRL location
    model = GPT2LMHeadModel.from_pretrained('/path/to/zymCTRL').to(device) # change to ZymCTRL location
    special_tokens = ['<start>', '<end>', '<|endoftext|>','<pad>',' ', '<sep>']

    # change to the appropriate EC classes
    labels=['3.5.5.1'] # nitrilases. You can put as many labels as you want.

    for label in tqdm(labels):
        # We'll run 100 batches per label. 20 sequences will be generated per batch.
        for i in range(0,100): 
            sequences = main(label, model, special_tokens, device, tokenizer)
            for key,value in sequences.items():
                for index, val in enumerate(value):
                    # Sequences will be saved with the name of the label followed by the batch index,
                    # and the order of the sequence in that batch.           
                    fn = open(f"/path/to/folder/{label}_{i}_{index}.fasta", "w")
                    fn.write(f'>{label}_{i}_{index}\t{val[1]}\n{val[0]}')
                    fn.close()
```
 

## **Example 2: Fine-tuning on a set of user-defined sequences**  

This alternative to the zero-shot generation allows updating ZymCTRL's weights to new sequences.

This strategy is not strictly necessary, in fact, we have observed good generations even for EC classes where there are 
only 1-2 representatives in Nature. But you might have an internal set of sequences that you'd like to incorporate into the model.
For example, internal datasets after protein engineering efforts, 
ancestrally-reconstructed sets, or after searching against metagenomics databases. In these cases, it is advisable to fine-tune ZymCTRL,
as it will learn new properties from your dataset and potentially improve the generation quality 
(especially for poorly populated EC classes).

To fine-tune ZymCTRL, you can use the script below to process your sequences. The only requisite is to start with an input file,
'sequences.fasta' which contains all the sequences in a fasta format. Please follow the format below. There should not be new lines '\n' or 
any separator between sequences. In the script, change the variable ec_label to the specific EC class you'd like to fine-tune.
The script will produce a file called {ec_label}_processed.txt and a folder with the training and validation datasets (split 10%)
```
>Sequence1
MMMMYMPLKVCD..
>Sequence2
MQWMXMYMPLKVCD..
>Sequence3
MPLKVCWMXMYMPLD..
```
We recommend using at least 200 sequences to obtain the best results. But we've seen it working with fewer sequences, so if you don't have
that many, give it still a go.


```
import random
from transformers import AutoTokenizer

from datasets import load_dataset
import transformers
from transformers.testing_utils import CaptureLogger

## DEFINE THESE VARIABLES
tokenizer = AutoTokenizer.from_pretrained('AI4PD/ZymCTRL')
ec_label = '1.1.1.1' # CHANGE TO YOUR LABEL
validation_split_percentage = 10 # change if you want
sequence_file = 'sequence.fasta'


#Load sequences, Read source file
with open(sequence_file, 'r') as fn: #! CHANGE TO SEQUENCES.FASTA
    data = fn.readlines()
    fn.close()

# Put sequences into dictionary
sequences={}
for line in data:
    if '>' in line:
        name = line.strip()
        sequences[name] = []  #! CHANGE TO corre
        continue
    sequences[name].append(line.strip())

#Pass sequences to list and shuffle their order randomly
sequences_list = [(key,value[0]) for key,value in sequences.items()]
random.shuffle(sequences_list)

#the objective is to get here strings, that when tokenized, would span a length of 1024.
#for each sequence group its length and untokenized string
print("procesing dataset")
processed_dataset = []
for i in sequences_list:
    # length of the control code
    sequence = i[1].strip()
    separator = '<sep>'
    control_code_length = len(tokenizer(ec_label+separator)['input_ids'])
    available_space = 1021 - control_code_length # It is not 1024 because '<|endoftext|>', and start and end

    # Option 1: the sequence is larger than the available space (3-4% of sequences)
    if len(sequence) > available_space:
        total_length = control_code_length + len(sequence[:available_space]) + 1
        seq = f"{ec_label}{separator}{sequence[:available_space]}<|endoftext|>"
        processed_dataset.append((total_length, seq))

    # Option 2 & 3: The sequence fits in the block_size space with or without padding
    else:
        total_length = control_code_length + len(sequence) + 3
        # in this case the sequence does not fit with the start/end tokens
        seq = f"{ec_label}{separator}<start>{sequence}<end><|endoftext|>"
        processed_dataset.append((total_length, seq))

# Group sequences
def grouper(iterable):
    prev = None
    group = ''
    total_sum = 0
    for item in iterable:
        if prev is None or item[0] + total_sum < 1025:
            group += item[1]
            total_sum += item[0]
        else:
            total_sum = item[0]
            yield group
            group = item[1]
        prev = item
    if group:
        total_sum = 0
        yield group

print("grouping processed dataset")
grouped_dataset=dict(enumerate(grouper(processed_dataset),1))

# Write file out for the tokenizer to read
fn = open(f"{ec_label}_processed.txt",'w')
for key,value in grouped_dataset.items():
    padding_len = 1024 - len(tokenizer(value)['input_ids'])
    padding = "<pad>"*padding_len
    fn.write(value+padding)
    fn.write
    fn.write("\n")
fn.close()

##TOKENIZE
# adapted from the trainer file
data_files = {}
dataset_args = {}

data_files["train"] = f"{ec_label}_processed.txt"
extension = "text"
tok_logger = transformers.utils.logging.get_logger("transformers.tokenization_utils_base")

raw_datasets = load_dataset(extension, data_files=data_files, cache_dir='.', **dataset_args)

raw_datasets["train"] = load_dataset(extension,
                data_files=data_files,
                split=f"train[{validation_split_percentage}%:]",
                cache_dir='.',
                **dataset_args,)

raw_datasets["validation"] = load_dataset(extension,
                                          data_files=data_files,
                                          split=f"train[:{validation_split_percentage}%]",
                                          cache_dir='.',
                                          **dataset_args,)

def tokenize_function(examples):
    with CaptureLogger(tok_logger) as cl:
        output = tokenizer(examples["text"])
    # clm input could be much much longer than block_size
    if "Token indices sequence length is longer than the" in cl.out:
        tok_logger.warning(
            "^^^^^^^^^^^^^^^^ Please ignore the warning above - this long input will be chunked into smaller bits before being passed to the model."
        )
    return output

tokenized_datasets = raw_datasets.map(
    tokenize_function,
    batched=True,
    num_proc=32,
    remove_columns=['text'],
    load_from_cache_file = False,
    desc="Running tokenizer on dataset",
)

block_size = 1024
def group_texts(examples):
    # Concatenate all texts.
    concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
    total_length = len(concatenated_examples[list(examples.keys())[0]])
    # We drop the small remainder, we could add padding if the model supported it instead of this drop,
    # you can customize this part to your needs.
    if total_length >= block_size:
        total_length = (total_length // block_size) * block_size
    # Split by chunks of max_len.
    result = {
        k: [t[i : i + block_size] for i in range(0, total_length, block_size)]
        for k, t in concatenated_examples.items()
    }
    result["labels"] = result["input_ids"].copy()
    return result

lm_datasets = tokenized_datasets.map(
    group_texts,
    batched=True,
    num_proc=124,
    load_from_cache_file=False,
    desc=f"Grouping texts in chunks of {block_size}",
)

train_dataset = lm_datasets["train"]
eval_dataset = lm_datasets["validation"]

train_dataset.save_to_disk('./dataset/train2')
eval_dataset.save_to_disk('./dataset/eval2')


```
The processed datasets will be inside the folder dataset/, called train2 and eval2.
You could also put the two previous scripts into a single one and run it in one go (that is what we do).

Now you are ready to fine-tune the model. 
To do that, you can take the trainer file that we provide in this repository (5.run_clm-post.py), or use the trainer from Hugging Face. 
The command below shows an example at an specific learning rate, 
but you could try with other hyperparameters to obtain the best training and evaluation losses.

```
python 5.run_clm-post.py --tokenizer_name AI4PD/ZymCTRL
 --do_train --do_eval --output_dir output --evaluation_strategy steps --eval_steps 10
 --logging_steps 5 --save_steps 500 --num_train_epochs 28 --per_device_train_batch_size 1
 --per_device_eval_batch_size 4 --cache_dir '.' --save_total_limit 2 --learning_rate  0.8e-04
 --dataloader_drop_last True --model_name_or_path AI4PD/ZymCTRL
```
In any case, the original HuggingFace script run_clm.py can be found here: 
https://github.com/huggingface/transformers/blob/master/examples/pytorch/language-modeling/run_clm.py


### **Training specs**
The model was trained on 48 NVIDIA A100 GPUs for eight epochs, 
using a block size of 1024 and a total batch size of 768. 
The optimizer used was Adam (beta1 = 0.9, beta2 = 0.999) 
with a learning rate of 0.8e-04.

### **Contact**

We are the AI for Protein Design group at the Centre for Genomic Regulation (https://www.aiproteindesign.com/).
For any questions post an issue in this repository so that other people can benefit from the feedback, and I'll get back to you shortly.
We are always open for collaborations, send an email to noelia [dot] ferruz [at] crg [dot] eu.