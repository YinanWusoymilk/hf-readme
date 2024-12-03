---
language: 
- pt
tags:
- generated_from_trainer
datasets:
- lener_br
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: checkpoints
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: lener_br
      type: lener_br
    metrics:
    - name: F1
      type: f1
      value: 0.8926146010186757
    - name: Precision
      type: precision
      value: 0.8810222036028488
    - name: Recall
      type: recall
      value: 0.9045161290322581
    - name: Accuracy
      type: accuracy
      value: 0.9759397808828684
    - name: Loss
      type: loss
      value: 0.18803243339061737
widget:
- text: "Ao Instituto Médico Legal da jurisdição do acidente ou da residência cumpre fornecer, no prazo de 90 dias, laudo à vítima (art. 5, § 5, Lei n. 6.194/74  de 19 de dezembro de 1974), função técnica que pode ser suprida por prova pericial realizada por ordem do juízo da causa, ou por prova técnica realizada no âmbito administrativo que se mostre coerente com os demais elementos de prova constante dos autos."
- text: "Acrescento que não há de se falar em violação do artigo 114, § 3º, da Constituição Federal, posto que referido dispositivo revela-se impertinente, tratando da possibilidade de ajuizamento de dissídio coletivo pelo Ministério Público do Trabalho nos casos de greve em atividade essencial."
- text: "Dispõe sobre o estágio de estudantes; altera a redação do art. 428 da Consolidação das Leis do Trabalho – CLT, aprovada pelo Decreto-Lei no 5.452, de 1o de maio de 1943, e a Lei no 9.394, de 20 de dezembro de 1996; revoga as Leis nos 6.494, de 7 de dezembro de 1977, e 8.859, de 23 de março de 1994, o parágrafo único do art. 82 da Lei no 9.394, de 20 de dezembro de 1996, e o art. 6o da Medida Provisória  no 2.164-41, de 24 de agosto de 2001; e dá outras providências."
---

## (BERT base) NER model in the legal domain in Portuguese (LeNER-Br)

**ner-bert-base-portuguese-cased-lenerbr** is a NER model (token classification) in the legal domain in Portuguese that was finetuned on 20/12/2021 in Google Colab from the model [pierreguillou/bert-base-cased-pt-lenerbr](https://huggingface.co/pierreguillou/bert-base-cased-pt-lenerbr) on the dataset [LeNER_br](https://huggingface.co/datasets/lener_br) by using a NER objective.

Due to the small size of BERTimbau base and finetuning dataset, the model overfitted before to reach the end of training. Here are the overall final metrics on the validation dataset (*note: see the paragraph "Validation metrics by Named Entity" to get detailed metrics*):
  - **f1**: 0.8926146010186757
  - **precision**: 0.8810222036028488
  - **recall**: 0.9045161290322581
  - **accuracy**: 0.9759397808828684
  - **loss**: 0.18803243339061737
  
Check as well the [large version of this model](https://huggingface.co/pierreguillou/ner-bert-large-cased-pt-lenerbr) with a f1 of 0.908.

**Note**: the model [pierreguillou/bert-base-cased-pt-lenerbr](https://huggingface.co/pierreguillou/bert-base-cased-pt-lenerbr) is a language model that was created through the finetuning of the model [BERTimbau base](https://huggingface.co/neuralmind/bert-base-portuguese-cased) on the dataset [LeNER-Br language modeling](https://huggingface.co/datasets/pierreguillou/lener_br_finetuning_language_model) by using a MASK objective. This first specialization of the language model before finetuning on the NER task improved a bit the model quality. To prove it, here are the results of the NER model finetuned from the model [BERTimbau base](https://huggingface.co/neuralmind/bert-base-portuguese-cased) (a non-specialized language model):
  - **f1**: 0.8716487228203504
  - **precision**: 0.8559286898839138
  - **recall**: 0.8879569892473118
  - **accuracy**: 0.9755893153732458
  - **loss**: 0.1133928969502449
  
## Blog post

[NLP | Modelos e Web App para Reconhecimento de Entidade Nomeada (NER) no domínio jurídico brasileiro](https://medium.com/@pierre_guillou/nlp-modelos-e-web-app-para-reconhecimento-de-entidade-nomeada-ner-no-dom%C3%ADnio-jur%C3%ADdico-b658db55edfb) (29/12/2021)
  
## Widget & App

You can test this model into the widget of this page.

Use as well the [NER App](https://huggingface.co/spaces/pierreguillou/ner-bert-pt-lenerbr) that allows comparing the 2 BERT models (base and large) fitted in the NER task with the legal LeNER-Br dataset.

## Using the model for inference in production
````
# install pytorch: check https://pytorch.org/
# !pip install transformers 
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

# parameters
model_name = "pierreguillou/ner-bert-base-cased-pt-lenerbr"
model = AutoModelForTokenClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

input_text = "Acrescento que não há de se falar em violação do artigo 114, § 3º, da Constituição Federal, posto que referido dispositivo revela-se impertinente, tratando da possibilidade de ajuizamento de dissídio coletivo pelo Ministério Público do Trabalho nos casos de greve em atividade essencial."

# tokenization
inputs = tokenizer(input_text, max_length=512, truncation=True, return_tensors="pt")
tokens = inputs.tokens()

# get predictions
outputs = model(**inputs).logits
predictions = torch.argmax(outputs, dim=2)

# print predictions
for token, prediction in zip(tokens, predictions[0].numpy()):
    print((token, model.config.id2label[prediction]))
````
You can use pipeline, too. However, it seems to have an issue regarding to the max_length of the input sequence.
````
!pip install transformers
import transformers
from transformers import pipeline

model_name = "pierreguillou/ner-bert-base-cased-pt-lenerbr"

ner = pipeline(
    "ner",
    model=model_name
) 

ner(input_text)
````
## Training procedure

### Notebook

The notebook of finetuning ([HuggingFace_Notebook_token_classification_NER_LeNER_Br.ipynb](https://github.com/piegu/language-models/blob/master/HuggingFace_Notebook_token_classification_NER_LeNER_Br.ipynb)) is in github.

### Hyperparameters

#### batch, learning rate...
- per_device_batch_size = 2
- gradient_accumulation_steps = 2
- learning_rate = 2e-5
- num_train_epochs = 10
- weight_decay = 0.01
- optimizer = AdamW
- betas = (0.9,0.999)
- epsilon = 1e-08
- lr_scheduler_type = linear
- seed = 7

#### save model & load best model
- save_total_limit = 2
- logging_steps = 300
- eval_steps = logging_steps
- evaluation_strategy = 'steps'
- logging_strategy = 'steps'
- save_strategy = 'steps'
- save_steps = logging_steps
- load_best_model_at_end = True
- fp16 = True

#### get best model through a metric
- metric_for_best_model = 'eval_f1'
- greater_is_better = True

### Training results

````
Num examples = 7828
Num Epochs = 10
Instantaneous batch size per device = 2
Total train batch size (w. parallel, distributed & accumulation) = 4
Gradient Accumulation steps = 2
Total optimization steps = 19570

Step	Training Loss Validation Loss      Precision     Recall  	 F1      	Accuracy
300	  0.127600	  0.178613	        0.722909	  0.741720	 0.732194	0.948802
600	  0.088200	  0.136965	        0.733636	  0.867742	 0.795074	0.963079
900	  0.078000	  0.128858	        0.791912	  0.838065	 0.814335	0.965243
1200 	0.077800      0.126345	        0.815400	  0.865376	 0.839645	0.967849
1500 	0.074100      0.148207	        0.779274	  0.895914	 0.833533	0.960184
1800 	0.059500      0.116634	        0.830829	  0.868172	 0.849090	0.969342
2100 	0.044500      0.208459	        0.887150	  0.816559	 0.850392	0.960535
2400 	0.029400      0.136352	        0.867821	  0.851398	 0.859531	0.970271
2700 	0.025000      0.165837	        0.814881	  0.878495	 0.845493	0.961235
3000 	0.038400      0.120629	        0.811719	  0.893763	 0.850768	0.971506
3300 	0.026200      0.175094	        0.823435	  0.882581	 0.851983	0.962957
3600 	0.025600      0.178438	        0.881095	  0.886022	 0.883551	0.963689
3900 	0.041000      0.134648	        0.789035	  0.916129	 0.847846	0.967681
4200 	0.026700      0.130178	        0.821275	  0.903226	 0.860303	0.972313
4500 	0.018500      0.139294	        0.844016	  0.875054	 0.859255	0.971140
4800 	0.020800      0.197811	        0.892504	  0.873118	 0.882705	0.965883
5100 	0.019300      0.161239	        0.848746	  0.888172	 0.868012	0.967849
5400 	0.024000      0.139131	        0.837507	  0.913333	 0.873778	0.970591
5700 	0.018400      0.157223	        0.899754	  0.864731	 0.881895	0.970210
6000 	0.023500      0.137022	        0.883018	  0.873333	 0.878149	0.973243
6300 	0.009300      0.181448	        0.840490	  0.900860	 0.869628	0.968290
6600 	0.019200      0.173125	        0.821316	  0.896559	 0.857290	0.966736
6900 	0.016100      0.143160	        0.789938	  0.904946	 0.843540	0.968245
7200 	0.017000      0.145755	        0.823274	  0.897634	 0.858848	0.969037
7500 	0.012100      0.159342	        0.825694	  0.883226	 0.853491	0.967468
7800 	0.013800      0.194886            0.861237	  0.859570	 0.860403	0.964771
8100 	0.008000      0.140271	        0.829914	  0.896129	 0.861752	0.971567
8400 	0.010300      0.143318	        0.826844	  0.908817	 0.865895	0.973578
8700 	0.015000      0.143392	        0.847336	  0.889247	 0.867786	0.973365
9000 	0.006000      0.143512	        0.847795	  0.905591	 0.875741	0.972892
9300 	0.011800      0.138747	        0.827133	  0.894194	 0.859357	0.971673
9600 	0.008500      0.159490	        0.837030	  0.909032	 0.871546	0.970028
9900 	0.010700      0.159249	        0.846692	  0.910968	 0.877655	0.970546
10200	0.008100	  0.170069  	      0.848288	  0.900645	 0.873683	0.969113
10500	0.004800	  0.183795	        0.860317	  0.899355	 0.879403	0.969570
10800	0.010700	  0.157024	        0.837838	  0.906667	 0.870894	0.971094
11100	0.003800	  0.164286	        0.845312	  0.880215	 0.862410	0.970744
11400	0.009700	  0.204025	        0.884294	  0.887527	 0.885907	0.968854
11700	0.008900	  0.162819	        0.829415	  0.887742	 0.857588	0.970530
12000	0.006400	  0.164296	        0.852666	  0.901075	 0.876202	0.971414
12300	0.007100	  0.143367	        0.852959	  0.895699	 0.873807	0.973669
12600	0.015800	  0.153383	        0.859224	  0.900430	 0.879345	0.972679
12900	0.006600	  0.173447	        0.869954	  0.899140	 0.884306	0.970927
13200	0.006800	  0.163234  	      0.856849	  0.897204	 0.876563	0.971795
13500	0.003200	  0.167164	        0.850867	  0.907957	 0.878485	0.971231
13800	0.003600	  0.148950  	      0.867801	  0.910538	 0.888656	0.976961
14100	0.003500	  0.155691  	      0.847621	  0.907957	 0.876752	0.974127
14400	0.003300	  0.157672	        0.846553	  0.911183	 0.877680	0.974584
14700	0.002500	  0.169965	        0.847804	  0.917634	 0.881338	0.973045
15000	0.003400	  0.177099  	      0.842199	  0.912473	 0.875929	0.971155
15300	0.006000	  0.164151  	      0.848928	  0.911183	 0.878954	0.973258
15600	0.002400	  0.174305	        0.847437	  0.906667	 0.876052	0.971765
15900	0.004100	  0.174561  	      0.852929	  0.907957	 0.879583	0.972907
16200	0.002600	  0.172626	        0.843263	  0.907097	 0.874016	0.972100
16500	0.002100	  0.185302	        0.841108	  0.907312	 0.872957	0.970485
16800	0.002900	  0.175638	        0.840557	  0.909247	 0.873554	0.971704
17100	0.001600	  0.178750	        0.857056	  0.906452	 0.881062	0.971765
17400	0.003900	  0.188910	        0.853619	  0.907957	 0.879950	0.970835
17700	0.002700	  0.180822	        0.864699	  0.907097	 0.885390	0.972283
18000	0.001300	  0.179974	        0.868150	  0.906237	 0.886785	0.973060

18300	0.000800	  0.188032	        0.881022	  0.904516	 0.892615	0.972572

18600	0.002700	  0.183266	        0.868601	  0.901290	 0.884644	0.972298
18900	0.001600	  0.180301	        0.862041	  0.903011	 0.882050	0.972344
19200	0.002300	  0.183432	        0.855370	  0.904301	 0.879155	0.971109
19500	0.001800	  0.183381	        0.854501	  0.904301	 0.878696	0.971186
````

### Validation metrics by Named Entity
````
Num examples = 1177

{'JURISPRUDENCIA': {'f1': 0.7016574585635359,
  'number': 657,
  'precision': 0.6422250316055625,
  'recall': 0.7732115677321156},
 'LEGISLACAO': {'f1': 0.8839681133746677,
  'number': 571,
  'precision': 0.8942652329749103,
  'recall': 0.8739054290718039},
 'LOCAL': {'f1': 0.8253968253968254,
  'number': 194,
  'precision': 0.7368421052631579,
  'recall': 0.9381443298969072},
 'ORGANIZACAO': {'f1': 0.8934049079754601,
  'number': 1340,
  'precision': 0.918769716088328,
  'recall': 0.8694029850746269},
 'PESSOA': {'f1': 0.982653539615565,
  'number': 1072,
  'precision': 0.9877474081055608,
  'recall': 0.9776119402985075},
 'TEMPO': {'f1': 0.9657657657657657,
  'number': 816,
  'precision': 0.9469964664310954,
  'recall': 0.9852941176470589},
 'overall_accuracy': 0.9725722644643211,
 'overall_f1': 0.8926146010186757,
 'overall_precision': 0.8810222036028488,
 'overall_recall': 0.9045161290322581}
 ````