---
license: apache-2.0
library_name: generic
tags:
  - text2text-generation
  - punctuation
  - sentence-boundary-detection
  - truecasing
  - true-casing
language:
  - af
  - am
  - ar
  - bg
  - bn
  - de
  - el
  - en
  - es
  - et
  - fa
  - fi
  - fr
  - gu
  - hi
  - hr
  - hu
  - id
  - is
  - it
  - ja
  - kk
  - kn
  - ko
  - ky
  - lt
  - lv
  - mk
  - ml
  - mr
  - nl
  - or
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - rw
  - so
  - sr
  - sw
  - ta
  - te
  - tr
  - uk
  - zh
widget:
  - text: "hola amigo cómo estás es un día lluvioso hoy"
  - text: "please rsvp for the party asap preferably before 8 pm tonight"
  - text: "este modelo fue entrenado en un gpu a100 en realidad no se que dice esta frase lo traduje con nmt"
  - text: "此模型向文本添加标点符号它支持47种语言并在a100gpu上接受过训练它可以在每种语言上运行而无需每种语言的特殊路径"
  - text: "यह मॉडल 47 भाषाओं में विराम चिह्न जोड़ता है यह भाषा विशिष्ट पथ के बिना काम करता है यह प्रत्येक भाषा के लिए विशेष पथों के बिना प्रत्येक भाषा पर कार्य कर सकता है"
---

# Model Overview
This is an `xlm-roberta` fine-tuned to restore punctuation, true-case (capitalize), 
and detect sentence boundaries (full stops) in 47 languages.

# Usage

If you want to just play with the model, the widget on this page will suffice. To use the model offline,
the following snippets show how to use the model both with a wrapper (that I wrote, available from `PyPI`)
and manual usuage (using the ONNX and SentencePiece models in this repo).

## Usage via `punctuators` package


<details>

  <summary>Click to see usage with wrappers</summary>

The easiest way to use this model is to install [punctuators](https://github.com/1-800-BAD-CODE/punctuators):

```bash
$ pip install punctuators
```

But this is just an ONNX and SentencePiece model, so you may run it as you wish.

The input to the `punctuators` API is a list (batch) of strings. 
Each string will be punctuated, true-cased, and segmented on predicted full stops.
The output will therefore be a list of list of strings: one list of segmented sentences per input text.
To disable full stops, use `m.infer(texts, apply_sbd=False)`. 
The output will then be a list of strings: one punctuated, true-cased string per input text.

<details open>

  <summary>Example Usage</summary>
  
```python

from typing import List

from punctuators.models import PunctCapSegModelONNX

m: PunctCapSegModelONNX = PunctCapSegModelONNX.from_pretrained(
    "1-800-BAD-CODE/xlm-roberta_punctuation_fullstop_truecase"
)

input_texts: List[str] = [
    "hola mundo cómo estás estamos bajo el sol y hace mucho calor santa coloma abre los huertos urbanos a las escuelas de la ciudad",
    "hello friend how's it going it's snowing outside right now in connecticut a large storm is moving in",
    "未來疫苗將有望覆蓋3歲以上全年齡段美國與北約軍隊已全部撤離還有鐵路公路在內的各項基建的來源都將枯竭",
    "በባለፈው ሳምንት ኢትዮጵያ ከሶማሊያ 3 ሺህ ወታደሮቿንም እንዳስወጣች የሶማሊያው ዳልሳን ሬድዮ ዘግቦ ነበር ጸጥታ ሃይሉና ህዝቡ ተቀናጅቶ በመስራቱ በመዲናዋ ላይ የታቀደው የጥፋት ሴራ ከሽፏል",
    "こんにちは友人" "調子はどう" "今日は雨の日でしたね" "乾いた状態を保つために一日中室内で過ごしました",
    "hallo freund wie geht's es war heute ein regnerischer tag nicht wahr ich verbrachte den tag drinnen um trocken zu bleiben",
    "हैलो दोस्त ये कैसा चल रहा है आज बारिश का दिन था न मैंने सूखा रहने के लिए दिन घर के अंदर बिताया",
    "كيف تجري الامور كان يومًا ممطرًا اليوم أليس كذلك قضيت اليوم في الداخل لأظل جافًا",
]

results: List[List[str]] = m.infer(
    texts=input_texts, apply_sbd=True,
)
for input_text, output_texts in zip(input_texts, results):
    print(f"Input: {input_text}")
    print(f"Outputs:")
    for text in output_texts:
        print(f"\t{text}")
    print()

```

</details>


<details open>

  <summary>Expected output</summary>

```text
Input: hola mundo cómo estás estamos bajo el sol y hace mucho calor santa coloma abre los huertos urbanos a las escuelas de la ciudad
Outputs:
	Hola mundo, ¿cómo estás?
	Estamos bajo el sol y hace mucho calor.
	Santa Coloma abre los huertos urbanos a las escuelas de la ciudad.

Input: hello friend how's it going it's snowing outside right now in connecticut a large storm is moving in
Outputs:
	Hello friend, how's it going?
	It's snowing outside right now.
	In Connecticut, a large storm is moving in.

Input: 未來疫苗將有望覆蓋3歲以上全年齡段美國與北約軍隊已全部撤離還有鐵路公路在內的各項基建的來源都將枯竭
Outputs:
	未來，疫苗將有望覆蓋3歲以上全年齡段。
	美國與北約軍隊已全部撤離。
	還有，鐵路，公路在內的各項基建的來源都將枯竭。

Input: በባለፈው ሳምንት ኢትዮጵያ ከሶማሊያ 3 ሺህ ወታደሮቿንም እንዳስወጣች የሶማሊያው ዳልሳን ሬድዮ ዘግቦ ነበር ጸጥታ ሃይሉና ህዝቡ ተቀናጅቶ በመስራቱ በመዲናዋ ላይ የታቀደው የጥፋት ሴራ ከሽፏል
Outputs:
	በባለፈው ሳምንት ኢትዮጵያ ከሶማሊያ 3 ሺህ ወታደሮቿንም እንዳስወጣች የሶማሊያው ዳልሳን ሬድዮ ዘግቦ ነበር።
	ጸጥታ ሃይሉና ህዝቡ ተቀናጅቶ በመስራቱ በመዲናዋ ላይ የታቀደው የጥፋት ሴራ ከሽፏል።

Input: こんにちは友人調子はどう今日は雨の日でしたね乾いた状態を保つために一日中室内で過ごしました
Outputs:
	こんにちは、友人、調子はどう？
	今日は雨の日でしたね。
	乾いた状態を保つために、一日中、室内で過ごしました。

Input: hallo freund wie geht's es war heute ein regnerischer tag nicht wahr ich verbrachte den tag drinnen um trocken zu bleiben
Outputs:
	Hallo Freund, wie geht's?
	Es war heute ein regnerischer Tag, nicht wahr?
	Ich verbrachte den Tag drinnen, um trocken zu bleiben.

Input: हैलो दोस्त ये कैसा चल रहा है आज बारिश का दिन था न मैंने सूखा रहने के लिए दिन घर के अंदर बिताया
Outputs:
	हैलो दोस्त, ये कैसा चल रहा है?
	आज बारिश का दिन था न, मैंने सूखा रहने के लिए दिन घर के अंदर बिताया।

Input: كيف تجري الامور كان يومًا ممطرًا اليوم أليس كذلك قضيت اليوم في الداخل لأظل جافًا
Outputs:
	كيف تجري الامور؟
	كان يومًا ممطرًا اليوم، أليس كذلك؟
	قضيت اليوم في الداخل لأظل جافًا.

```

</details>

</details>

## Manual Usage
If you want to use the ONNX and SP models without wrappers, see the following example.

<details>

  <summary>Click to see manual usage</summary>


```python
from typing import List

import numpy as np
import onnxruntime as ort
from huggingface_hub import hf_hub_download
from omegaconf import OmegaConf
from sentencepiece import SentencePieceProcessor

# Download the models from HF hub. Note: to clean up, you can find these files in your HF cache directory
spe_path = hf_hub_download(repo_id="1-800-BAD-CODE/xlm-roberta_punctuation_fullstop_truecase", filename="sp.model")
onnx_path = hf_hub_download(repo_id="1-800-BAD-CODE/xlm-roberta_punctuation_fullstop_truecase", filename="model.onnx")
config_path = hf_hub_download(
    repo_id="1-800-BAD-CODE/xlm-roberta_punctuation_fullstop_truecase", filename="config.yaml"
)

# Load the SP model
tokenizer: SentencePieceProcessor = SentencePieceProcessor(spe_path)  # noqa
# Load the ONNX graph
ort_session: ort.InferenceSession = ort.InferenceSession(onnx_path)
# Load the model config with labels, etc.
config = OmegaConf.load(config_path)
# Potential classification labels before each subtoken
pre_labels: List[str] = config.pre_labels
# Potential classification labels after each subtoken
post_labels: List[str] = config.post_labels
# Special class that means "predict nothing"
null_token = config.get("null_token", "<NULL>")
# Special class that means "all chars in this subtoken end with a period", e.g., "am" -> "a.m."
acronym_token = config.get("acronym_token", "<ACRONYM>")
# Not used in this example, but if your sequence exceed this value, you need to fold it over multiple inputs
max_len = config.max_length
# For reference only, graph has no language-specific behavior
languages: List[str] = config.languages

# Encode some input text, adding BOS + EOS
input_text = "hola mundo cómo estás estamos bajo el sol y hace mucho calor santa coloma abre los huertos urbanos a las escuelas de la ciudad"
input_ids = [tokenizer.bos_id()] + tokenizer.EncodeAsIds(input_text) + [tokenizer.eos_id()]

# Create a numpy array with shape [B, T], as the graph expects as input.
# Note that we do not pass lengths to the graph; if you are using a batch, padding should be tokenizer.pad_id() and the
# graph's attention mechanisms will ignore pad_id() without requiring explicit sequence lengths.
input_ids_arr: np.array = np.array([input_ids])

# Run the graph, get outputs for all analytics
pre_preds, post_preds, cap_preds, sbd_preds = ort_session.run(None, {"input_ids": input_ids_arr})
# Squeeze off the batch dimensions and convert to lists
pre_preds = pre_preds[0].tolist()
post_preds = post_preds[0].tolist()
cap_preds = cap_preds[0].tolist()
sbd_preds = sbd_preds[0].tolist()

# Segmented sentences
output_texts: List[str] = []
# Current sentence, which is built until we hit a sentence boundary prediction
current_chars: List[str] = []
# Iterate over the outputs, ignoring the first (BOS) and final (EOS) predictions and tokens
for token_idx in range(1, len(input_ids) - 1):
    token = tokenizer.IdToPiece(input_ids[token_idx])
    # Simple SP decoding
    if token.startswith("▁") and current_chars:
        current_chars.append(" ")
    # Token-level predictions
    pre_label = pre_labels[pre_preds[token_idx]]
    post_label = post_labels[post_preds[token_idx]]
    # If we predict "pre-punct", insert it before this token
    if pre_label != null_token:
        current_chars.append(pre_label)
    # Iterate over each char. Skip SP's space token,
    char_start = 1 if token.startswith("▁") else 0
    for token_char_idx, char in enumerate(token[char_start:], start=char_start):
        # If this char should be capitalized, apply upper case
        if cap_preds[token_idx][token_char_idx]:
            char = char.upper()
        # Append char
        current_chars.append(char)
        # if this is an acronym, add a period after every char (p.m., a.m., etc.)
        if post_label == acronym_token:
            current_chars.append(".")
    # Maybe this subtoken ends with punctuation
    if post_label != null_token and post_label != acronym_token:
        current_chars.append(post_label)

    # If this token is a sentence boundary, finalize the current sentence and reset
    if sbd_preds[token_idx]:
        output_texts.append("".join(current_chars))
        current_chars.clear()

# Maybe push final sentence, if the final token was not classified as a sentence boundary
if current_chars:
    output_texts.append("".join(current_chars))

# Pretty print
print(f"Input: {input_text}")
print("Outputs:")
for text in output_texts:
    print(f"\t{text}")

```

Expected output:

```text
Input: hola mundo cómo estás estamos bajo el sol y hace mucho calor santa coloma abre los huertos urbanos a las escuelas de la ciudad
Outputs:
	Hola mundo, ¿cómo estás?
	Estamos bajo el sol y hace mucho calor.
	Santa Coloma abre los huertos urbanos a las escuelas de la ciudad.
```

</details>

&nbsp;


# Model Architecture

This model implements the following graph, which allows punctuation, true-casing, and fullstop prediction 
in every language without language-specific behavior: 

![graph.png](https://cdn-uploads.huggingface.co/production/uploads/62d34c813eebd640a4f97587/WJ8aWIM4A--xzYu8FR4ht.png)

<details>

  <summary>Click to see graph explanations</summary>
  
We start by tokenizing the text and encoding it with XLM-Roberta, which is the pre-trained portion of this graph.

Then we predict punctuation before and after every subtoken. 
Predicting before each token allows for Spanish inverted question marks.
Predicting after every token allows for all other punctuation, including punctuation within continuous-script 
languages and acronyms.

We use embeddings to represent the predicted punctuation tokens to inform the sentence boundary head of the
punctuation that'll be inserted into the text. This allows proper full stop prediction, since certain punctuation
tokens (periods, questions marks, etc.) are strongly correlated with sentence boundaries.

We then shift full stop predictions to the right by one, to inform the true-casing head of where the beginning
of each new sentence is. This is important since true-casing is strongly correlated to sentence boundaries.

For true-casing, we predict `N` predictions per subtoken, where `N` is the number of characters in the subtoken.
In practice, `N` is the maximum subtoken length and extra predictions are ignored. Essentially, true-casing is
modeled as a multi-label problem. This allows for upper-casing arbitrary characters, e.g., "NATO", "MacDonald", "mRNA", etc.

Applying all these predictions to the input text, we can punctuate, true-case, and split sentences in any language.

</details>

## Tokenizer

<details>

  <summary>Click to see how the XLM-Roberta tokenizer was un-hacked</summary>
  
Instead of the hacky wrapper used by FairSeq and strangely ported (not fixed) by HuggingFace, the `xlm-roberta` SentencePiece model was adjusted to correctly encode
the text. Per HF's comments,

```python
# Original fairseq vocab and spm vocab must be "aligned":
# Vocab    |    0    |    1    |   2    |    3    |  4  |  5  |  6  |   7   |   8   |  9
# -------- | ------- | ------- | ------ | ------- | --- | --- | --- | ----- | ----- | ----
# fairseq  | '<s>'   | '<pad>' | '</s>' | '<unk>' | ',' | '.' | '▁' | 's'   | '▁de' | '-'
# spm      | '<unk>' | '<s>'   | '</s>' | ','     | '.' | '▁' | 's' | '▁de' | '-'   | '▁a'
```

The SP model was un-hacked with the following snippet 
(SentencePiece experts, let me know if there is a problem here):

```python
from sentencepiece import SentencePieceProcessor
from sentencepiece.sentencepiece_model_pb2 import ModelProto

m = ModelProto()
m.ParseFromString(open("/path/to/xlmroberta/sentencepiece.bpe.model", "rb").read())

pieces = list(m.pieces)
pieces = (
    [
        ModelProto.SentencePiece(piece="<s>", type=ModelProto.SentencePiece.Type.CONTROL),
        ModelProto.SentencePiece(piece="<pad>", type=ModelProto.SentencePiece.Type.CONTROL),
        ModelProto.SentencePiece(piece="</s>", type=ModelProto.SentencePiece.Type.CONTROL),
        ModelProto.SentencePiece(piece="<unk>", type=ModelProto.SentencePiece.Type.UNKNOWN),
    ]
    + pieces[3:]
    + [ModelProto.SentencePiece(piece="<mask>", type=ModelProto.SentencePiece.Type.USER_DEFINED)]
)
del m.pieces[:]
m.pieces.extend(pieces)

with open("/path/to/new/sp.model", "wb") as f:
    f.write(m.SerializeToString())
```

Now we can use just the SP model without a wrapper.

</details>

## Post-Punctuation Tokens
This model predicts the following set of punctuation tokens after each subtoken:

| Token  | Description | Relevant Languages |
| ---: | :---------- | :----------- |
| \<NULL\>    | No punctuation | All |
| \<ACRONYM\>    | Every character in this subword is followed by a period | Primarily English, some European |
| .    | Latin full stop | Many |
| ,    | Latin comma | Many |
| ?    | Latin question mark | Many |
| ？    | Full-width question mark | Chinese, Japanese |
| ，    | Full-width comma | Chinese, Japanese |
| 。    | Full-width full stop | Chinese, Japanese |
| 、    | Ideographic comma | Chinese, Japanese |
| ・    | Middle dot | Japanese |
| ।    | Danda | Hindi, Bengali, Oriya |
| ؟    | Arabic question mark | Arabic |
| ;    | Greek question mark | Greek |
| ።    | Ethiopic full stop | Amharic |
| ፣    | Ethiopic comma | Amharic |
| ፧    | Ethiopic question mark | Amharic |


## Pre-Punctuation Tokens
This model predicts the following set of punctuation tokens before each subword:

| Token  | Description | Relevant Languages |
| ---: | :---------- | :----------- |
| \<NULL\>    | No punctuation | All |
| ¿    | Inverted question mark | Spanish |



# Training Details
This model was trained in the NeMo framework on an A100 for approximately 7 hours.
You may view the `tensorboard` log on [tensorboard.dev](https://tensorboard.dev/experiment/xxnULI1aTeK37vUDL4ejiw/#scalars).

This model was trained with News Crawl data from WMT.
1M lines of text for each language was used, except for a few low-resource languages which may have used less.
Languages were chosen based on whether the News Crawl corpus contained enough reliable-quality data as judged by the author.

# Limitations

This model was trained on news data, and may not perform well on conversational or informal data.

This model is unlikely to be of production quality. 
It was trained with "only" 1M lines per language, and the dev sets may have been noisy due to the nature of web-scraped news data.

This model over-predicts Spanish question marks, especially the inverted question mark `¿` (see metrics below). 
Since `¿` is a rare token, especially in the context of a 47-language model, Spanish questions were over-sampled 
by selecting more of these sentences from additional training data that was not used. However, this seems to have 
"over-corrected" the problem and a lot of Spanish question marks are predicted.

The model may also over-predict commas.

If you find any general limitations not mentioned here, let me know so all limitations can be addressed in the 
next fine-tuning.

# Evaluation
In these metrics, keep in mind that
1. The data is noisy
2. Sentence boundaries and true-casing are conditioned on predicted punctuation, which is the most difficult task and sometimes incorrect.
   When conditioning on reference punctuation, true-casing and SBD is practically 100% for most languages.
4. Punctuation can be subjective. E.g.,
   
   `Hola mundo, ¿cómo estás?`
   
   or

   `Hola mundo. ¿Cómo estás?`

   When the sentences are longer and more practical, these ambiguities abound and affect all 3 analytics.

## Test Data and Example Generation
Each test example was generated using the following procedure:

1. Concatenate 11 random sentences (1 + 10 for each sentence in the test set)
2. Lower-case the concatenated sentence
3. Remove all punctuation

Targets are generated as we lower-case letters and remove punctuation.

The data is a held-out portion of News Crawl, which has been deduplicated. 
3,000 lines of data per language was used, generating 3,000 unique examples of 11 sentences each.
We generate 3,000 examples, where example `i` begins with sentence `i` and is followed by 10 random
sentences selected from the 3,000 sentence test set.

For measuring true-casing and sentence boundary detection, reference punctuation tokens were used for 
conditioning (see graph above). If we use predicted punctuation instead, then incorrect punctuation will
result in true-casing and SBD targets not aligning correctly and these metrics will be artificially low.

## Selected Language Evaluation Reports
For now, metrics for a few selected languages are shown below. 
Given the amount of work required to collect and pretty-print metrics in 47 languages, I'll add more eventually.

Expand any of the following tabs to see metrics for that language.


<details>
  <summary>English</summary>
  
```text
punct_post test report: 
    label                                                precision    recall       f1           support   
    <NULL> (label_id: 0)                                    99.25      98.43      98.84     564908
    <ACRONYM> (label_id: 1)                                 63.14      84.67      72.33        613
    . (label_id: 2)                                         90.97      93.91      92.42      32040
    , (label_id: 3)                                         73.95      84.32      78.79      24271
    ? (label_id: 4)                                         79.05      81.94      80.47       1041
    ？ (label_id: 5)                                          0.00       0.00       0.00          0
    ， (label_id: 6)                                          0.00       0.00       0.00          0
    。 (label_id: 7)                                          0.00       0.00       0.00          0
    、 (label_id: 8)                                          0.00       0.00       0.00          0
    ・ (label_id: 9)                                          0.00       0.00       0.00          0
    । (label_id: 10)                                         0.00       0.00       0.00          0
    ؟ (label_id: 11)                                         0.00       0.00       0.00          0
    ، (label_id: 12)                                         0.00       0.00       0.00          0
    ; (label_id: 13)                                         0.00       0.00       0.00          0
    ። (label_id: 14)                                         0.00       0.00       0.00          0
    ፣ (label_id: 15)                                         0.00       0.00       0.00          0
    ፧ (label_id: 16)                                         0.00       0.00       0.00          0
    -------------------
    micro avg                                               97.60      97.60      97.60     622873
    macro avg                                               81.27      88.65      84.57     622873
    weighted avg                                            97.77      97.60      97.67     622873
```

```
cap test report: 
    label                                                precision    recall       f1           support   
    LOWER (label_id: 0)                                     99.72      99.85      99.78    2134956
    UPPER (label_id: 1)                                     96.33      93.52      94.91      91996
    -------------------
    micro avg                                               99.59      99.59      99.59    2226952
    macro avg                                               98.03      96.68      97.34    2226952
    weighted avg                                            99.58      99.59      99.58    2226952
```

```
seg test report: 
    label                                                precision    recall       f1           support   
    NOSTOP (label_id: 0)                                    99.99      99.98      99.99     591540
    FULLSTOP (label_id: 1)                                  99.61      99.89      99.75      34333
    -------------------
    micro avg                                               99.97      99.97      99.97     625873
    macro avg                                               99.80      99.93      99.87     625873
    weighted avg                                            99.97      99.97      99.97     625873
```

</details>



<details>
  <summary>Spanish</summary>
  
```text
  punct_pre test report: 
    label                                                precision    recall       f1           support   
    <NULL> (label_id: 0)                                    99.94      99.89      99.92     636941
    ¿ (label_id: 1)                                         56.73      71.35      63.20       1288
    -------------------
    micro avg                                               99.83      99.83      99.83     638229
    macro avg                                               78.34      85.62      81.56     638229
    weighted avg                                            99.85      99.83      99.84     638229
```

```
punct_post test report: 
    label                                                precision    recall       f1           support   
    <NULL> (label_id: 0)                                    99.19      98.41      98.80     578271
    <ACRONYM> (label_id: 1)                                 30.10      56.36      39.24         55
    . (label_id: 2)                                         91.92      93.12      92.52      30856
    , (label_id: 3)                                         72.98      82.44      77.42      27761
    ? (label_id: 4)                                         52.77      71.85      60.85       1286
    ？ (label_id: 5)                                          0.00       0.00       0.00          0
    ， (label_id: 6)                                          0.00       0.00       0.00          0
    。 (label_id: 7)                                          0.00       0.00       0.00          0
    、 (label_id: 8)                                          0.00       0.00       0.00          0
    ・ (label_id: 9)                                          0.00       0.00       0.00          0
    । (label_id: 10)                                         0.00       0.00       0.00          0
    ؟ (label_id: 11)                                         0.00       0.00       0.00          0
    ، (label_id: 12)                                         0.00       0.00       0.00          0
    ; (label_id: 13)                                         0.00       0.00       0.00          0
    ። (label_id: 14)                                         0.00       0.00       0.00          0
    ፣ (label_id: 15)                                         0.00       0.00       0.00          0
    ፧ (label_id: 16)                                         0.00       0.00       0.00          0
    -------------------
    micro avg                                               97.40      97.40      97.40     638229
    macro avg                                               69.39      80.44      73.77     638229
    weighted avg                                            97.60      97.40      97.48     638229
```

```
cap test report: 
    label                                                precision    recall       f1           support   
    LOWER (label_id: 0)                                     99.82      99.86      99.84    2324724
    UPPER (label_id: 1)                                     95.92      94.70      95.30      79266
    -------------------
    micro avg                                               99.69      99.69      99.69    2403990
    macro avg                                               97.87      97.28      97.57    2403990
    weighted avg                                            99.69      99.69      99.69    2403990
```

```
seg test report: 
    label                                                precision    recall       f1           support   
    NOSTOP (label_id: 0)                                    99.99      99.96      99.98     607057
    FULLSTOP (label_id: 1)                                  99.31      99.88      99.60      34172
    -------------------
    micro avg                                               99.96      99.96      99.96     641229
    macro avg                                               99.65      99.92      99.79     641229
    weighted avg                                            99.96      99.96      99.96     641229
```

</details>


<details>
  <summary>Amharic</summary>
  
```text
punct_post test report: 
    label                                                precision    recall       f1           support   
    <NULL> (label_id: 0)                                    99.83      99.28      99.56     729664
    <ACRONYM> (label_id: 1)                                  0.00       0.00       0.00          0
    . (label_id: 2)                                          0.00       0.00       0.00          0
    , (label_id: 3)                                          0.00       0.00       0.00          0
    ? (label_id: 4)                                          0.00       0.00       0.00          0
    ？ (label_id: 5)                                          0.00       0.00       0.00          0
    ， (label_id: 6)                                          0.00       0.00       0.00          0
    。 (label_id: 7)                                          0.00       0.00       0.00          0
    、 (label_id: 8)                                          0.00       0.00       0.00          0
    ・ (label_id: 9)                                          0.00       0.00       0.00          0
    । (label_id: 10)                                         0.00       0.00       0.00          0
    ؟ (label_id: 11)                                         0.00       0.00       0.00          0
    ، (label_id: 12)                                         0.00       0.00       0.00          0
    ; (label_id: 13)                                         0.00       0.00       0.00          0
    ። (label_id: 14)                                        91.27      97.90      94.47      25341
    ፣ (label_id: 15)                                        61.93      82.11      70.60       5818
    ፧ (label_id: 16)                                        67.41      81.73      73.89       1177
    -------------------
    micro avg                                               99.08      99.08      99.08     762000
    macro avg                                               80.11      90.26      84.63     762000
    weighted avg                                            99.21      99.08      99.13     762000
```

```
cap test report: 
    label                                                precision    recall       f1           support   
    LOWER (label_id: 0)                                     98.40      98.03      98.21       1064
    UPPER (label_id: 1)                                     71.23      75.36      73.24         69
    -------------------
    micro avg                                               96.65      96.65      96.65       1133
    macro avg                                               84.81      86.69      85.73       1133
    weighted avg                                            96.74      96.65      96.69       1133
```

```
seg test report: 
    label                                                precision    recall       f1           support   
    NOSTOP (label_id: 0)                                    99.99      99.85      99.92     743158
    FULLSTOP (label_id: 1)                                  95.20      99.62      97.36      21842
    -------------------
    micro avg                                               99.85      99.85      99.85     765000
    macro avg                                               97.59      99.74      98.64     765000
    weighted avg                                            99.85      99.85      99.85     765000
```

</details>


<details>
  <summary>Chinese</summary>

```text
punct_post test report: 
    label                                                precision    recall       f1           support   
    <NULL> (label_id: 0)                                    99.53      97.31      98.41     435611
    <ACRONYM> (label_id: 1)                                  0.00       0.00       0.00          0
    . (label_id: 2)                                          0.00       0.00       0.00          0
    , (label_id: 3)                                          0.00       0.00       0.00          0
    ? (label_id: 4)                                          0.00       0.00       0.00          0
    ？ (label_id: 5)                                         81.85      87.31      84.49       1513
    ， (label_id: 6)                                         74.08      93.67      82.73      35921
    。 (label_id: 7)                                         96.51      96.93      96.72      32097
    、 (label_id: 8)                                          0.00       0.00       0.00          0
    ・ (label_id: 9)                                          0.00       0.00       0.00          0
    । (label_id: 10)                                         0.00       0.00       0.00          0
    ؟ (label_id: 11)                                         0.00       0.00       0.00          0
    ، (label_id: 12)                                         0.00       0.00       0.00          0
    ; (label_id: 13)                                         0.00       0.00       0.00          0
    ። (label_id: 14)                                         0.00       0.00       0.00          0
    ፣ (label_id: 15)                                         0.00       0.00       0.00          0
    ፧ (label_id: 16)                                         0.00       0.00       0.00          0
    -------------------
    micro avg                                               97.00      97.00      97.00     505142
    macro avg                                               87.99      93.81      90.59     505142
    weighted avg                                            97.48      97.00      97.15     505142
```

```
cap test report: 
    label                                                precision    recall       f1           support   
    LOWER (label_id: 0)                                     94.89      94.98      94.94       2951
    UPPER (label_id: 1)                                     81.34      81.03      81.18        796
    -------------------
    micro avg                                               92.02      92.02      92.02       3747
    macro avg                                               88.11      88.01      88.06       3747
    weighted avg                                            92.01      92.02      92.01       3747
```

```
seg test report: 
    label                                                precision    recall       f1           support   
    NOSTOP (label_id: 0)                                    99.99      99.97      99.98     473642
    FULLSTOP (label_id: 1)                                  99.55      99.90      99.72      34500
    -------------------
    micro avg                                               99.96      99.96      99.96     508142
    macro avg                                               99.77      99.93      99.85     508142
    weighted avg                                            99.96      99.96      99.96     508142
```
  
</details>


<details>
  <summary>Japanese</summary>

```text
punct_post test report: 
    label                                                precision    recall       f1           support   
    <NULL> (label_id: 0)                                    99.34      95.90      97.59     406341
    <ACRONYM> (label_id: 1)                                  0.00       0.00       0.00          0
    . (label_id: 2)                                          0.00       0.00       0.00          0
    , (label_id: 3)                                          0.00       0.00       0.00          0
    ? (label_id: 4)                                          0.00       0.00       0.00          0
    ？ (label_id: 5)                                         70.55      73.56      72.02       1456
    ， (label_id: 6)                                          0.00       0.00       0.00          0
    。 (label_id: 7)                                         94.38      96.95      95.65      32537
    、 (label_id: 8)                                         54.28      87.62      67.03      18610
    ・ (label_id: 9)                                         28.18      71.64      40.45       1100
    । (label_id: 10)                                         0.00       0.00       0.00          0
    ؟ (label_id: 11)                                         0.00       0.00       0.00          0
    ، (label_id: 12)                                         0.00       0.00       0.00          0
    ; (label_id: 13)                                         0.00       0.00       0.00          0
    ። (label_id: 14)                                         0.00       0.00       0.00          0
    ፣ (label_id: 15)                                         0.00       0.00       0.00          0
    ፧ (label_id: 16)                                         0.00       0.00       0.00          0
    -------------------
    micro avg                                               95.51      95.51      95.51     460044
    macro avg                                               69.35      85.13      74.55     460044
    weighted avg                                            96.91      95.51      96.00     460044
```

```
cap test report: 
    label                                                precision    recall       f1           support   
    LOWER (label_id: 0)                                     92.33      94.03      93.18       4174
    UPPER (label_id: 1)                                     83.51      79.46      81.43       1587
    -------------------
    micro avg                                               90.02      90.02      90.02       5761
    macro avg                                               87.92      86.75      87.30       5761
    weighted avg                                            89.90      90.02      89.94       5761
```

```
seg test report: 
    label                                                precision    recall       f1           support   
    NOSTOP (label_id: 0)                                    99.99      99.92      99.96     428544
    FULLSTOP (label_id: 1)                                  99.07      99.87      99.47      34500
    -------------------
    micro avg                                               99.92      99.92      99.92     463044
    macro avg                                               99.53      99.90      99.71     463044
    weighted avg                                            99.92      99.92      99.92     463044
```

</details>


<details>
  <summary>Hindi</summary>
  
```text
punct_post test report: 
    label                                                precision    recall       f1           support   
    <NULL> (label_id: 0)                                    99.75      99.44      99.59     560358
    <ACRONYM> (label_id: 1)                                  0.00       0.00       0.00          0
    . (label_id: 2)                                          0.00       0.00       0.00          0
    , (label_id: 3)                                         69.55      78.48      73.75       8084
    ? (label_id: 4)                                         63.30      87.07      73.31        317
    ？ (label_id: 5)                                          0.00       0.00       0.00          0
    ， (label_id: 6)                                          0.00       0.00       0.00          0
    。 (label_id: 7)                                          0.00       0.00       0.00          0
    、 (label_id: 8)                                          0.00       0.00       0.00          0
    ・ (label_id: 9)                                          0.00       0.00       0.00          0
    । (label_id: 10)                                        96.92      98.66      97.78      32118
    ؟ (label_id: 11)                                         0.00       0.00       0.00          0
    ، (label_id: 12)                                         0.00       0.00       0.00          0
    ; (label_id: 13)                                         0.00       0.00       0.00          0
    ። (label_id: 14)                                         0.00       0.00       0.00          0
    ፣ (label_id: 15)                                         0.00       0.00       0.00          0
    ፧ (label_id: 16)                                         0.00       0.00       0.00          0
    -------------------
    micro avg                                               99.11      99.11      99.11     600877
    macro avg                                               82.38      90.91      86.11     600877
    weighted avg                                            99.17      99.11      99.13     600877
```

```
cap test report: 
    label                                                precision    recall       f1           support   
    LOWER (label_id: 0)                                     97.19      96.72      96.95       2466
    UPPER (label_id: 1)                                     89.14      90.60      89.86        734
    -------------------
    micro avg                                               95.31      95.31      95.31       3200
    macro avg                                               93.17      93.66      93.41       3200
    weighted avg                                            95.34      95.31      95.33       3200
```

```
seg test report: 
    label                                                precision    recall       f1           support   
    NOSTOP (label_id: 0)                                   100.00      99.99      99.99     569472
    FULLSTOP (label_id: 1)                                  99.82      99.99      99.91      34405
    -------------------
    micro avg                                               99.99      99.99      99.99     603877
    macro avg                                               99.91      99.99      99.95     603877
    weighted avg                                            99.99      99.99      99.99     603877
```
  
</details>


<details>
  <summary>Arabic</summary>

```text
punct_post test report: 
    label                                                precision    recall       f1           support   
    <NULL> (label_id: 0)                                    99.30      96.94      98.10     688043
    <ACRONYM> (label_id: 1)                                 93.33      77.78      84.85         18
    . (label_id: 2)                                         93.31      93.78      93.54      28175
    , (label_id: 3)                                          0.00       0.00       0.00          0
    ? (label_id: 4)                                          0.00       0.00       0.00          0
    ？ (label_id: 5)                                          0.00       0.00       0.00          0
    ， (label_id: 6)                                          0.00       0.00       0.00          0
    。 (label_id: 7)                                          0.00       0.00       0.00          0
    、 (label_id: 8)                                          0.00       0.00       0.00          0
    ・ (label_id: 9)                                          0.00       0.00       0.00          0
    । (label_id: 10)                                         0.00       0.00       0.00          0
    ؟ (label_id: 11)                                        65.93      82.79      73.40        860
    ، (label_id: 12)                                        44.89      79.20      57.30      20941
    ; (label_id: 13)                                         0.00       0.00       0.00          0
    ። (label_id: 14)                                         0.00       0.00       0.00          0
    ፣ (label_id: 15)                                         0.00       0.00       0.00          0
    ፧ (label_id: 16)                                         0.00       0.00       0.00          0
    -------------------
    micro avg                                               96.29      96.29      96.29     738037
    macro avg                                               79.35      86.10      81.44     738037
    weighted avg                                            97.49      96.29      96.74     738037
```

```
cap test report: 
    label                                                precision    recall       f1           support   
    LOWER (label_id: 0)                                     97.10      99.49      98.28       4137
    UPPER (label_id: 1)                                     98.71      92.89      95.71       1729
    -------------------
    micro avg                                               97.55      97.55      97.55       5866
    macro avg                                               97.90      96.19      96.99       5866
    weighted avg                                            97.57      97.55      97.52       5866
```

```
seg test report: 
    label                                                precision    recall       f1           support   
    NOSTOP (label_id: 0)                                    99.99      99.97      99.98     710456
    FULLSTOP (label_id: 1)                                  99.39      99.85      99.62      30581
    -------------------
    micro avg                                               99.97      99.97      99.97     741037
    macro avg                                               99.69      99.91      99.80     741037
    weighted avg                                            99.97      99.97      99.97     741037
```
  
</details>

&nbsp;

# Extra Stuff

## Acronyms, abbreviations, and bi-capitalized words

This section briefly demonstrates the models behavior when presented with the following:

1. Acronyms: "NATO"
2. Fake acronyms: "NHTG" in place of "NATO"
3. Ambigous term which could be an acronym or proper noun: "Tuny"
3. Bi-capitalized words: "McDavid"
4. Intialisms: "p.m."

<details open>

  <summary>Acronyms, etc. inputs</summary>
  
```python
from typing import List

from punctuators.models import PunctCapSegModelONNX

m: PunctCapSegModelONNX = PunctCapSegModelONNX.from_pretrained(
    "1-800-BAD-CODE/xlm-roberta_punctuation_fullstop_truecase"
)

input_texts = [
    "the us is a nato member as a nato member the country enjoys security guarantees notably article 5",
    "the us is a nhtg member as a nhtg member the country enjoys security guarantees notably article 5",
    "the us is a tuny member as a tuny member the country enjoys security guarantees notably article 5",
    "connor andrew mcdavid is a canadian professional ice hockey centre and captain of the edmonton oilers of the national hockey league the oilers selected him first overall in the 2015 nhl entry draft mcdavid spent his childhood playing ice hockey against older children",
    "please rsvp for the party asap preferably before 8 pm tonight",
]

results: List[List[str]] = m.infer(
    texts=input_texts, apply_sbd=True,
)
for input_text, output_texts in zip(input_texts, results):
    print(f"Input: {input_text}")
    print(f"Outputs:")
    for text in output_texts:
        print(f"\t{text}")
    print()

```

</details>


<details open>

  <summary>Expected output</summary>
  
```text
Input: the us is a nato member as a nato member the country enjoys security guarantees notably article 5
Outputs:
	The U.S. is a NATO member.
	As a NATO member, the country enjoys security guarantees, notably Article 5.

Input: the us is a nhtg member as a nhtg member the country enjoys security guarantees notably article 5
Outputs:
	The U.S. is a NHTG member.
	As a NHTG member, the country enjoys security guarantees, notably Article 5.

Input: the us is a tuny member as a tuny member the country enjoys security guarantees notably article 5
Outputs:
	The U.S. is a Tuny member.
	As a Tuny member, the country enjoys security guarantees, notably Article 5.

Input: connor andrew mcdavid is a canadian professional ice hockey centre and captain of the edmonton oilers of the national hockey league the oilers selected him first overall in the 2015 nhl entry draft mcdavid spent his childhood playing ice hockey against older children
Outputs:
	Connor Andrew McDavid is a Canadian professional ice hockey centre and captain of the Edmonton Oilers of the National Hockey League.
	The Oilers selected him first overall in the 2015 NHL entry draft.
	McDavid spent his childhood playing ice hockey against older children.

Input: please rsvp for the party asap preferably before 8 pm tonight
Outputs:
	Please RSVP for the party ASAP, preferably before 8 p.m. tonight.
```

</details> 
