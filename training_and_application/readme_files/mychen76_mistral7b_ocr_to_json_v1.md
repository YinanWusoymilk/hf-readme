---
thumbnail: "url to a thumbnail used in social sharing"
tags:
- tag1
- tag2
license: apache-2.0
datasets:
- dataset1
- dataset2
metrics:
- metric1
- metric2
---

Model Architecture:

The mychen76/mistral7b_ocr_to_json_v1 (LLM) is a finetuned for convert OCR text to Json object task. this experimental model is based on Mistral-7B-v0.1 which outperforms Llama 2 13B on all benchmarks tested.

Motivation:

Currently, OCR engines are well tested on image detection and text recognition. LLM models are well trained for text processing and generation. Hence, leveraging outputs from OCR engines could save LLM training times for image-to-text use cases such as invoice or receipt image to JSON object conversion tasks.

Model Usage:

Take an invoice or receipt image, perform OCR on the image to get text boxes, and feed the outputs into LLM models to generate a well-formed receipt JSON object.

```
### Instruction:
You are POS receipt data expert, parse, detect, recognize and convert following receipt OCR image result into structure receipt data object. 
Don't make up value not in the Input. Output must be a well-formed JSON object.```json

### Input:
[[[[184.0, 42.0], [278.0, 45.0], [278.0, 62.0], [183.0, 59.0]], ('BAJA FRESH', 0.9551795721054077)], [[[242.0, 113.0], [379.0, 118.0], [378.0, 136.0], [242.0, 131.0]], ('GENERAL MANAGER:', 0.9462024569511414)], [[[240.0, 133.0], [300.0, 135.0], [300.0, 153.0], [240.0, 151.0]], ('NORMAN', 0.9913229942321777)], [[[143.0, 166.0], [234.0, 171.0], [233.0, 192.0], [142.0, 187.0]], ('176 Rosa C', 0.9229503870010376)], [[[130.0, 207.0], [206.0, 210.0], [205.0, 231.0], [129.0, 228.0]], ('Chk 7545', 0.9349349141120911)], [[[283.0, 215.0], [431.0, 221.0], [431.0, 239.0], [282.0, 233.0]], ("Dec26'0707:26PM", 0.9290117025375366)], [[[440.0, 221.0], [489.0, 221.0], [489.0, 239.0], [440.0, 239.0]], ('Gst0', 0.9164432883262634)], [[[164.0, 252.0], [308.0, 256.0], [308.0, 276.0], [164.0, 272.0]], ('TAKE OUT', 0.9367803335189819)], [[[145.0, 274.0], [256.0, 278.0], [255.0, 296.0], [144.0, 292.0]], ('1 BAJA STEAK', 0.9167789816856384)], [[[423.0, 282.0], [465.0, 282.0], [465.0, 304.0], [423.0, 304.0]], ('6.95', 0.9965073466300964)], [[[180.0, 296.0], [292.0, 299.0], [292.0, 319.0], [179.0, 316.0]], ('NO GUACAMOLE', 0.9631438255310059)], [[[179.0, 317.0], [319.0, 322.0], [318.0, 343.0], [178.0, 338.0]], ('ENCHILADO STYLE', 0.9704310894012451)], [[[423.0, 325.0], [467.0, 325.0], [467.0, 347.0], [423.0, 347.0]], ('1.49', 0.988395631313324)], [[[159.0, 339.0], [201.0, 341.0], [200.0, 360.0], [158.0, 358.0]], ('CASH', 0.9982023239135742)], [[[417.0, 348.0], [466.0, 348.0], [466.0, 367.0], [417.0, 367.0]], ('20.00', 0.9921982884407043)], [[[156.0, 380.0], [200.0, 382.0], [198.0, 404.0], [155.0, 402.0]], ('FOOD', 0.9906187057495117)], [[[426.0, 390.0], [468.0, 390.0], [468.0, 409.0], [426.0, 409.0]], ('8.44', 0.9963030219078064)], [[[154.0, 402.0], [190.0, 405.0], [188.0, 427.0], [152.0, 424.0]], ('TAX', 0.9963871836662292)], [[[427.0, 413.0], [468.0, 413.0], [468.0, 432.0], [427.0, 432.0]], ('0.61', 0.9934712648391724)], [[[153.0, 427.0], [224.0, 429.0], [224.0, 450.0], [153.0, 448.0]], ('PAYMENT', 0.9948703646659851)], [[[428.0, 436.0], [470.0, 436.0], [470.0, 455.0], [428.0, 455.0]], ('9.05', 0.9961490631103516)], [[[152.0, 450.0], [251.0, 453.0], [250.0, 475.0], [152.0, 472.0]], ('Change Due', 0.9556287527084351)], [[[420.0, 458.0], [471.0, 458.0], [471.0, 480.0], [420.0, 480.0]], ('10.95', 0.997236430644989)], [[[209.0, 498.0], [382.0, 503.0], [381.0, 524.0], [208.0, 519.0]], ('$2.000FF', 0.9757758378982544)], [[[169.0, 522.0], [422.0, 528.0], [421.0, 548.0], [169.0, 542.0]], ('NEXT PURCHASE', 0.962527871131897)], [[[167.0, 546.0], [365.0, 552.0], [365.0, 570.0], [167.0, 564.0]], ('CALL800 705 5754or', 0.926964521408081)], [[[146.0, 570.0], [416.0, 577.0], [415.0, 597.0], [146.0, 590.0]], ('Go www.mshare.net/bajafresh', 0.9759786128997803)], [[[147.0, 594.0], [356.0, 601.0], [356.0, 621.0], [146.0, 614.0]], ('Take our brief survey', 0.9390400648117065)], [[[143.0, 620.0], [410.0, 626.0], [409.0, 647.0], [143.0, 641.0]], ('When Prompted, Enter Store', 0.9385656118392944)], [[[142.0, 646.0], [408.0, 653.0], [407.0, 673.0], [142.0, 666.0]], ('Write down redemption code', 0.9536812901496887)], [[[141.0, 672.0], [409.0, 679.0], [408.0, 699.0], [141.0, 692.0]], ('Use this receipt as coupon', 0.9658807516098022)], [[[138.0, 697.0], [448.0, 701.0], [448.0, 725.0], [138.0, 721.0]], ('Discount on purchases of $5.00', 0.9624248743057251)], [[[139.0, 726.0], [466.0, 729.0], [466.0, 750.0], [139.0, 747.0]], ('or more,Offer expires in 30 day', 0.9263916611671448)], [[[137.0, 750.0], [459.0, 755.0], [459.0, 778.0], [137.0, 773.0]], ('Good at participating locations', 0.963909924030304)]]

### Output:
```
```json
{
  "receipt": {
    "store": "BAJA FRESH",
    "manager": "GENERAL MANAGER: NORMAN",
    "address": "176 Rosa C",
    "check": "Chk 7545",
    "date": "Dec26'0707:26PM",
    "tax": "Gst0",
    "total": "20.00",
    "payment": "CASH",
    "change": "0.61",
    "discount": "Discount on purchases of $5.00 or more,Offer expires in 30 day",
    "coupon": "Use this receipt as coupon",
    "survey": "Take our brief survey",
    "redemption": "Write down redemption code",
    "prompt": "When Prompted, Enter Store Write down redemption code Use this receipt as coupon",
    "items": [
      {
        "name": "1 BAJA STEAK",
        "price": "6.95",
        "modifiers": [
          "NO GUACAMOLE",
          "ENCHILADO STYLE"
        ]
      },
      {
        "name": "TAKE OUT",
        "price": "1.49"
      }
    ]
  }
}
```

# Looking for Model with ChatML format?
see link here: https://huggingface.co/mychen76/mistral_ocr2json_v3_chatml

# looking for receipt image to Json vision model
see link here: https://huggingface.co/mychen76/paligemma-receipt-json-3b-mix-448-v2b


# Load model directly
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("mychen76/mistral7b_ocr_to_json_v1")
model = AutoModelForCausalLM.from_pretrained("mychen76/mistral7b_ocr_to_json_v1")

prompt=f"""### Instruction:
You are POS receipt data expert, parse, detect, recognize and convert following receipt OCR image result into structure receipt data object. 
Don't make up value not in the Input. Output must be a well-formed JSON object.```json

### Input:
{receipt_boxes}

### Output:
"""
with torch.inference_mode():
    inputs = tokenizer(prompt,return_tensors="pt",truncation=True).to(device)
    outputs = model.generate(**inputs, max_new_tokens=512) 
    result_text = tokenizer.batch_decode(outputs)[0]
    print(result_text)
```

## Get OCR Image boxes
```python
from paddleocr import PaddleOCR, draw_ocr
from ast import literal_eval
import json

paddleocr = PaddleOCR(lang="en",ocr_version="PP-OCRv4",show_log = False,use_gpu=True)

def paddle_scan(paddleocr,img_path_or_nparray):
    result = paddleocr.ocr(img_path_or_nparray,cls=True)
    result = result[0]
    boxes = [line[0] for line in result]       #boundign box 
    txts = [line[1][0] for line in result]     #raw text
    scores = [line[1][1] for line in result]   # scores
    return  txts, result

# perform ocr scan
receipt_texts, receipt_boxes = paddle_scan(paddleocr,receipt_image_array)
print(50*"--","\ntext only:\n",receipt_texts)
print(50*"--","\nocr boxes:\n",receipt_boxes)

```

# Load model in 4bits
```python

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, BitsAndBytesConfig

# quantization_config = BitsAndBytesConfig(llm_int8_enable_fp32_cpu_offload=True)
bnb_config = BitsAndBytesConfig(
    llm_int8_enable_fp32_cpu_offload=True,
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)
# control model memory allocation between devices for low GPU resource (0,cpu)
device_map = {
    "transformer.word_embeddings": 0,
    "transformer.word_embeddings_layernorm": 0,
    "lm_head": 0,
    "transformer.h": 0,
    "transformer.ln_f": 0,
    "model.embed_tokens": 0,
    "model.layers":0,
    "model.norm":0    
}
device = "cuda" if torch.cuda.is_available() else "cpu"

# model use for inference
model_id="mychen76/mistral7b_ocr_to_json_v1"
model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    trust_remote_code=True,  
    torch_dtype=torch.float16,
    quantization_config=bnb_config,
    device_map=device_map)
# tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
```

Dataset use for finetuning:  

mychen76/invoices-and-receipts_ocr_v1


## Usage Notebooks

#### English Receipts
model_id="mychen76/mistral7b_ocr_to_json_v1"
https://github.com/minyang-chen/LLM_convert_receipt_image-to-json_or_xml/blob/main/Convert_Receipt_Image-to-Json_using_OCR_to_JSON_v1-English.ipynb

model_id: mychen76/mistral_ocr2json_v3_chatml
https://github.com/minyang-chen/LLM_convert_receipt_image-to-json_or_xml/blob/main/Convert_Receipt_Image-to-Json_using_OCR_to_JSON_v2_ChatML.ipynb


#### German Receipts
model_id="mychen76/mistral7b_ocr_to_json_v1"

Test01
https://github.com/minyang-chen/LLM_convert_receipt_image-to-json_or_xml/blob/main/Convert_Receipt_Image-to-Json_using_OCR_to_JSON_v1-German-Test1-passed.ipynb

Test02
https://github.com/minyang-chen/LLM_convert_receipt_image-to-json_or_xml/blob/main/Convert_Receipt_Image-to-Json_using_OCR_to_JSON_v1-German-Test2-failed.ipynb

Test03
https://github.com/minyang-chen/LLM_convert_receipt_image-to-json_or_xml/blob/main/Convert_Receipt_Image-to-Json_using_OCR_to_JSON_v1-German-Test3-okay.ipynb

