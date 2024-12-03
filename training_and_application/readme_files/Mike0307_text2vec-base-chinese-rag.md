---
license: apache-2.0
pipeline_tag: sentence-similarity
metrics:
- spearmanr
---

## Overview
This model is primarily designed for language understanding between Chinese texts.<br>
It utilizes the **CoSENT** training framework for the purpose of the **Retrieval-Augmented Generation(RAG)** task.

## Download the model

```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("Mike0307/text2vec-base-chinese-rag")
model = AutoModel.from_pretrained("Mike0307/text2vec-base-chinese-rag")
```

## Example of similarity comparison
```python
import torch
def mean_pooling(model_output, attention_mask):
  token_embeddings = model_output[0]
  input_mask_expanded = (
    attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
  )
  return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(
    input_mask_expanded.sum(1), min=1e-9
  )

sentences =  [
  "福井舞所屬哪家唱片公司？",
  "23歲時出道、血型A型的福井舞是出身於京都的日本女創作歌手，所屬唱片公司為J-more。2004年，與WADAGAKI、SHINO組合地下音樂隊Poplar，發表了兩張專輯，天照和夢死物語。在2006年時退出，2007年10月加入了Avex獨立發展。"
]

encode_output = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt", max_length=512)
model_output = model(**encode_output)
embeddings = mean_pooling(model_output, encode_output['attention_mask'])

torch.cosine_similarity(embeddings[0], embeddings[1], dim=0)
# tensor(0.7002)

```

## Example of Langchain RAG

RAG with Langchain: https://python.langchain.com/v0.1/docs/use_cases/question_answering/
![image/png](https://cdn-uploads.huggingface.co/production/uploads/6414866f1cbd604c9217c7d0/RrBoHJINfrSWtCNkePs7g.png)

Install the langchain packages

```bash
pip install --upgrade --quiet  langchain langchain-community
```

### 1. Use this embedding model to build a retiever

Download HuggingFace model through langchain_community

```python
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
model_name = "Mike0307/text2vec-base-chinese-rag"
embeddings = HuggingFaceEmbeddings(model_name=model_name)
```

An example of retriever with Meta FAISS vectorstore

```python
from langchain.schema import Document
from langchain_community.vectorstores.faiss import FAISS
documents = [
    Document(page_content="埃及聖䴉（學名：Threskiornis aethiopicus），又名埃及聖朱鷺、埃及聖鷺、聖䴉，是撒哈拉以南非洲、伊拉克東南部及以往埃及的一種朱鷺。牠們在埃及備受尊敬，經常被製成木乃伊當做托特的象徵。牠們也被引入到法國、義大利、西班牙及美國。現在，在臺灣西部濱海地區也可看到牠們。"),
    Document(page_content="隨著科技的不斷發展和革新，人工智能已經成為了眾多企業和機構的重點關注對象。機器學習、自然語言處理、深度神經網絡等技術的應用，已經開始推動著人工智能產業的快速發展。從目前的發展情況來看，人工智能不僅可以提高工作效率，降低人力成本，還可以促進產業升級，改善生活品質。"),
    Document(page_content="Apache Hadoop是一款支持數據密集型分佈式應用程序並以Apache 2.0許可協議發佈的開源軟體框架。它支持在商品硬件構建的大型集群上運行的應用程序。Hadoop是根據谷歌公司發表的MapReduce和Google檔案系統的論文自行實作而成。"),
    Document(page_content="23歲時出道、血型A型的福井舞是出身於京都的日本女創作歌手，所屬唱片公司為J-more。2004年，與WADAGAKI、SHINO組合地下音樂隊Poplar，發表了兩張專輯，天照和夢死物語。在2006年時退出，2007年10月加入了Avex獨立發展。"),
    Document(page_content="協和橋（Pont de la Concorde）是法國巴黎一座跨越塞納河的拱橋，介於協和廣場的堤道（quai des Tuileries）（右岸）和奧賽堤道（quai d'Orsay）（左岸）之間。它在過去曾稱為路易十六橋（pont Louis XVI）、革命橋（pont de la Révolution）、協和橋，波旁復辟時期（1814年）複稱路易十六橋，1830年再度恢復協和橋名稱，直至今日。"),
    Document(page_content="中華民國空氣汙染指標（Pollutant Standards Index，PSI）是空氣汙染情況的一項指標，由中華民國行政院環境保護署於1993年擴充測站後推出，目標乃藉由本測站系統監控全臺灣所有的空氣品質並加以通報改善。空氣汙染指標為依據監測資料將當日空氣中懸浮微粒(PM10)、二氧化硫(SO)、二氧化氮(NO)、一氧化碳 (CO) 及臭氧 (O) 等5種空氣汙染物濃度數值"),
    Document(page_content="滾石國際音樂股份有限公司 Rock Records Co., Ltd.  曾用名 滾石雜誌社 滾石有聲出版社 公司類型 股份有限公司 統一編號 22012304 成立 1976年，滾石雜誌社 1980年，滾石有聲出版社 1986年1月28日（公司登記日期）（38年113天） 創辦人 段鍾沂、段鍾潭 代表人物 段鍾沂、段鍾潭 "),
]
db = FAISS.from_documents(documents, embeddings)
retriever = db.as_retriever(search_kwargs = {"k" : 1})
retriever.invoke("福井舞所屬哪家唱片公司？")
# [Document(page_content='23歲時出道、血型A型的福井舞是出身於京都的日本女創作歌手，所屬唱片公司為J-more。2004年，與WADAGAKI、SHINO組合地下音樂隊Poplar，發表了兩張專輯，天照和夢死物語。在2006年時退出，2007年10月加入了Avex獨立發展。')]
```

### 2. Use HuggingFace LLM as customized Langchain LLM

Sometimes, we don’t want to rely on the OpenAI API. Here are some tips to empower the use of HuggingFace models.
First, download the HuggingFace LLM via the bellow code. Check [this repo](https://huggingface.co/Mike0307/Phi-3-mini-4k-instruct-chinese-lora) if you encounter any problems.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

llm_id = "Mike0307/Phi-3-mini-4k-instruct-chinese-lora"
model = AutoModelForCausalLM.from_pretrained(
    llm_id, 
    device_map="mps", # Change mps if not MacOS
    torch_dtype=torch.float32,  # try float16 for M1 chip
    trust_remote_code=True,
    attn_implementation="eager", # without flash_attn
)
tokenizer = AutoTokenizer.from_pretrained(llm_id)
```

Secondly, construct a valid langchain LLM class via the downloaded HuggingFace model.

```python
import re
from pydantic import Field
from typing import Any, List, Optional
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM

class CustomLLM(LLM):
    model : Any = Field(..., description="The huggingface llm model.")
    tokenizer : Any = Field(..., description="The huggingface llm tokenizer.")
    def __init__(self, model, tokenizer):
        super().__init__(model = model, tokenizer = tokenizer)
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,**kwargs: Any,) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(**inputs, temperature = 0.0, max_length = 500, do_sample = False)
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=False)
        return self.output_parser(generated_text)
    
    @property
    def _llm_type(self) -> str:
        return "custom"
    
    def output_parser(output):
        pattern = "<\|assistant\|>(.*?)<\|endoftext\|>"
        match = re.search(pattern, output, re.DOTALL)
        if match:
            return match.group(1).strip()
        return output.strip()

```

### 3. Make a simple RAG chain

Use `promt`, `llm`, `retriever` to build a simple RAG chain and try inference.

```python
import langchain
langchain.debug = True # Check the chain process and validate the retrieved documents

prompt = PromptTemplate.from_template(template="<|user|>{documents}\n{question} <|end|>\n<|assistant|>")
llm = CustomLLM(model, tokenizer)
rag = {
    "question" : RunnablePassthrough(),
    "documents" : retriever
} | prompt | llm

## example of inference
query = "埃及聖䴉是什麼？"
rag.invoke(query)
## '埃及聖䴉是一種埃及的朱鷺，它在埃及備受尊敬，經常被製成木乃伊當做托特的象徵。它也被引入到法國、義大利、西班牙及美國。現在，在臺灣西部濱海地區也可看到埃及聖䴉。'

```


