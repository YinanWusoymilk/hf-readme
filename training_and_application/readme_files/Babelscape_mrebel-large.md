---
language:
- ar
- ca
- de
- el
- en
- es
- fr
- hi
- it
- ja
- ko
- nl
- pl
- pt
- ru
- sv
- vi
- zh
widget:
- text: >-
    Els Red Hot Chili Peppers es van formar a Los Angeles per Kiedis, Flea, el
    guitarrista Hillel Slovak i el bateria Jack Irons.
  example_title: Catalan
inference:
  parameters:
    decoder_start_token_id: 250058
    src_lang: ca_XX
    tgt_lang: <triplet>
tags:
- seq2seq
- relation-extraction
license: cc-by-nc-sa-4.0
pipeline_tag: translation
datasets:
- Babelscape/SREDFM
---
# RED<sup>FM</sup>: a Filtered and Multilingual Relation Extraction Dataset

This is a multilingual version of [REBEL](https://huggingface.co/Babelscape/rebel-large). It can be used as a standalone multulingual Relation Extraction system, or as a pretrained system to be tuned on multilingual Relation Extraction datasets.

mREBEL is introduced in the ACL 2023 paper [RED^{FM}: a Filtered and Multilingual Relation Extraction Dataset](https://arxiv.org/abs/2306.09802). We present a new multilingual Relation Extraction dataset and train a multilingual version of REBEL which reframed Relation Extraction as a seq2seq task. The paper can be found [here](https://arxiv.org/abs/2306.09802). If you use the code or model, please reference this work in your paper:

    @inproceedings{huguet-cabot-et-al-2023-redfm-dataset,
        title = "RED$^{\rm FM}$: a Filtered and Multilingual Relation Extraction Dataset",
        author = "Huguet Cabot, Pere-Llu{\'\i}s  and Tedeschi, Simone and Ngonga Ngomo, Axel-Cyrille and
          Navigli, Roberto",
        booktitle = "Proc. of the 61st Annual Meeting of the Association for Computational Linguistics: ACL 2023",
        month = jul,
        year = "2023",
        address = "Toronto, Canada",
        publisher = "Association for Computational Linguistics",
        url = "https://arxiv.org/abs/2306.09802",
    }

The original repository for the paper can be found [here](https://github.com/Babelscape/rebel#REDFM)

Be aware that the inference widget at the right does not output special tokens, which are necessary to distinguish the subject, object and relation types. For a demo of mREBEL and its pre-training dataset check the [Spaces demo](https://huggingface.co/spaces/Babelscape/mrebel-demo).

## Pipeline usage

```python
from transformers import pipeline

triplet_extractor = pipeline('translation_xx_to_yy', model='Babelscape/mrebel-large', tokenizer='Babelscape/mrebel-large')
# We need to use the tokenizer manually since we need special tokens.
extracted_text = triplet_extractor.tokenizer.batch_decode([triplet_extractor("The Red Hot Chili Peppers were formed in Los Angeles by Kiedis, Flea, guitarist Hillel Slovak and drummer Jack Irons.", decoder_start_token_id=250058, src_lang="en_XX", tgt_lang="<triplet>", return_tensors=True, return_text=False)[0]["translation_token_ids"]]) # change en_XX for the language of the source.
print(extracted_text[0])
# Function to parse the generated text and extract the triplets
def extract_triplets_typed(text):
    triplets = []
    relation = ''
    text = text.strip()
    current = 'x'
    subject, relation, object_, object_type, subject_type = '','','','',''

    for token in text.replace("<s>", "").replace("<pad>", "").replace("</s>", "").replace("tp_XX", "").replace("__en__", "").split():
        if token == "<triplet>" or token == "<relation>":
            current = 't'
            if relation != '':
                triplets.append({'head': subject.strip(), 'head_type': subject_type, 'type': relation.strip(),'tail': object_.strip(), 'tail_type': object_type})
                relation = ''
            subject = ''
        elif token.startswith("<") and token.endswith(">"):
            if current == 't' or current == 'o':
                current = 's'
                if relation != '':
                    triplets.append({'head': subject.strip(), 'head_type': subject_type, 'type': relation.strip(),'tail': object_.strip(), 'tail_type': object_type})
                object_ = ''
                subject_type = token[1:-1]
            else:
                current = 'o'
                object_type = token[1:-1]
                relation = ''
        else:
            if current == 't':
                subject += ' ' + token
            elif current == 's':
                object_ += ' ' + token
            elif current == 'o':
                relation += ' ' + token
    if subject != '' and relation != '' and object_ != '' and object_type != '' and subject_type != '':
        triplets.append({'head': subject.strip(), 'head_type': subject_type, 'type': relation.strip(),'tail': object_.strip(), 'tail_type': object_type})
    return triplets
extracted_triplets = extract_triplets_typed(extracted_text[0])
print(extracted_triplets)
```

## Model and Tokenizer using transformers

```python
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def extract_triplets_typed(text):
    triplets = []
    relation = ''
    text = text.strip()
    current = 'x'
    subject, relation, object_, object_type, subject_type = '','','','',''

    for token in text.replace("<s>", "").replace("<pad>", "").replace("</s>", "").replace("tp_XX", "").replace("__en__", "").split():
        if token == "<triplet>" or token == "<relation>":
            current = 't'
            if relation != '':
                triplets.append({'head': subject.strip(), 'head_type': subject_type, 'type': relation.strip(),'tail': object_.strip(), 'tail_type': object_type})
                relation = ''
            subject = ''
        elif token.startswith("<") and token.endswith(">"):
            if current == 't' or current == 'o':
                current = 's'
                if relation != '':
                    triplets.append({'head': subject.strip(), 'head_type': subject_type, 'type': relation.strip(),'tail': object_.strip(), 'tail_type': object_type})
                object_ = ''
                subject_type = token[1:-1]
            else:
                current = 'o'
                object_type = token[1:-1]
                relation = ''
        else:
            if current == 't':
                subject += ' ' + token
            elif current == 's':
                object_ += ' ' + token
            elif current == 'o':
                relation += ' ' + token
    if subject != '' and relation != '' and object_ != '' and object_type != '' and subject_type != '':
        triplets.append({'head': subject.strip(), 'head_type': subject_type, 'type': relation.strip(),'tail': object_.strip(), 'tail_type': object_type})
    return triplets

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Babelscape/mrebel-large", src_lang="en_XX", tgt_lang="tp_XX") 
# Here we set English ("en_XX") as source language. To change the source language swap the first token of the input for your desired language or change to supported language. For catalan ("ca_XX") or greek ("el_EL") (not included in mBART pretraining) you need a workaround:
# tokenizer._src_lang = "ca_XX"
# tokenizer.cur_lang_code_id = tokenizer.convert_tokens_to_ids("ca_XX")
# tokenizer.set_src_lang_special_tokens("ca_XX")
model = AutoModelForSeq2SeqLM.from_pretrained("Babelscape/mrebel-large")
gen_kwargs = {
    "max_length": 256,
    "length_penalty": 0,
    "num_beams": 3,
    "num_return_sequences": 3,
    "forced_bos_token_id": None,
}

# Text to extract triplets from
text = 'The Red Hot Chili Peppers were formed in Los Angeles by Kiedis, Flea, guitarist Hillel Slovak and drummer Jack Irons.'

# Tokenizer text
model_inputs = tokenizer(text, max_length=256, padding=True, truncation=True, return_tensors = 'pt')

# Generate
generated_tokens = model.generate(
    model_inputs["input_ids"].to(model.device),
    attention_mask=model_inputs["attention_mask"].to(model.device),
    decoder_start_token_id = tokenizer.convert_tokens_to_ids("tp_XX"),
    **gen_kwargs,
)

# Extract text
decoded_preds = tokenizer.batch_decode(generated_tokens, skip_special_tokens=False)

# Extract triplets
for idx, sentence in enumerate(decoded_preds):
    print(f'Prediction triplets sentence {idx}')
    print(extract_triplets_typed(sentence))
```

## License

This model is licensed under the CC BY-SA 4.0 license. The text of the license can be found [here](https://creativecommons.org/licenses/by-nc-sa/4.0/).