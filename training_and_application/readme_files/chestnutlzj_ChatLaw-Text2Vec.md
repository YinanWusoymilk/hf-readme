---
license: apache-2.0
language:
- zh
pipeline_tag: sentence-similarity
---

# Law Text2Vec

本模型用于法律相关文本的相似度计算。可用于制作向量数据库等。

# Dataset

本模型利用936727条全国案例库数据集训练，数据集样本如下：


| sentence1 | sentence2 | score |
| --------  | --------  | --------  |
|股权转让合同的双方就转让对价未达成合意，导致已签订的股权转让协议不具有可履行性的，应认定该转让协议不成立。|有限责任公司的股东会决议确认了有关股东之间股权转让的相关事宜，但对转让价款规定不明确，当事人不能达成补充协议的，讼争股东之间的股权转让合同是否成立？|1|
|租赁房屋消防要求不达标，能否导致合同目的不能实现，合同是否当然无效的问题。|原审认为，二被告作为承租人租赁的是一般房屋，双方对租赁物了解，标的物是符合合同要求的。租赁房屋存在与相邻建筑防火间距不足，疏散通道的宽度不够的问题。该标的物的相邻建筑防火间距和疏散通道宽度均达不到国家标准。承租人取得租赁房屋后从事宾馆经营，提升了消防要求，但阻隔合同目的实现不是必然的，不支持合同无效。 再审认为，该租赁房屋在建成后，一直作为服务性经营场所，本案提及的消防问题，程度不一的存在。但未发现以前有行政管理部门禁止其经营的记录。本次公安消防的通知是整改，并不是禁止经营。公安部2012年颁布的《建设工程消防监督管理规定》强制消防要求达标的范围，是指在50米以下的建筑物。也就是该房屋作为租赁物建立合同关系，不违反国家的强制性规定。参照最高人民法院[2003]民一他字第11号函复《关于未经消防验收合格而订立的房屋租赁合同如何认定其效力》的相关意见，认定双方签订的租赁合同成立并有效。|1|


# Examples

> 请问夫妻之间共同财产如何定义？

1. 最高人民法院关于适用《婚姻法》若干问题的解释（三）(2011-08-09): 第五条 夫妻一方个人财产在婚后产生的收益，除孳息和自然增值外，应认定为夫妻共同财产。
2. 最高人民法院关于适用《婚姻法》若干问题的解释（二）的补充规定(2017-02-28): 第十九条 由一方婚前承租、婚后用共同财产购买的房屋，房屋权属证书登记在一方名下的，应当认定为夫妻共同财产。
3. 最高人民法院关于适用《婚姻法》若干问题的解释（二）的补充规定(2017-02-28): 第二十二条 当事人结婚前，父母为双方购置房屋出资的，该出资应当认定为对自己子女的个人赠与，但父母明确表示赠与双方的除外。当事人结婚后，父母为双方购置房屋出资的，该出资应当认定为对夫妻双方的赠与，但父母明确表示赠与一方的除外。

> 请问民间借贷的利息有什么限制

1. 合同法(1999-03-15): 第二百零六条 借款人应当按照约定的期限返还借款。对借款期限没有约定或者约定不明确，依照本法第六十一条的规定仍不能确定的，借款人可以随时返还；贷款人可以催告借款人在合理期限内返还。
2. 合同法(1999-03-15): 第二百零五条 借款人应当按照约定的期限支付利息。对支付利息的期限没有约定或者约定不明确，依照本法第六十一条的规定仍不能确定，借款期间不满一年的，应当在返还借款时一并支付；借款期间一年以上的，应当在每届满一年时支付，剩余期间不满一年的，应当在返还借款时一并支付。
3. 最高人民法院关于审理民间借贷案件适用法律若干问题的规定(2020-08-19): 第二十六条 出借人请求借款人按照合同约定利率支付利息的，人民法院应予支持，但是双方约定的利率超过合同成立时一年期贷款市场报价利率四倍的除外。前款所称“一年期贷款市场报价利率”，是指中国人民银行授权全国银行间同业拆借中心自2019年8月20日起每月发布的一年期贷款市场报价利率。

# Usage

```python
from sentence_transformers import SentenceTransformer,  LoggingHandler, losses, models, util
from sentence_transformers.util import cos_sim


model_path = "your_model_path"
model = SentenceTransformer(model_path).cuda()

sentence1 = "合同法(1999-03-15): 第二百零六条 借款人应当按照约定的期限返还借款。对借款期限没有约定或者约定不明确，依照本法第六十一条的规定仍不能确定的，借款人可以随时返还；贷款人可以催告借款人在合理期限内返还。"

sentence2 = "请问如果借款没还怎么办。"

encoded_sentence1 = model.encode(sentence1)

encoded_sentence2 = model.encode(sentence2)

print(cos_sim(encoded_sentence1, encoded_sentence2))

# tensor([[0.9960]])
```

欢迎引用我们:

```
@misc{cui2023chatlaw,
      title={ChatLaw: Open-Source Legal Large Language Model with Integrated External Knowledge Bases}, 
      author={Jiaxi Cui and Zongjian Li and Yang Yan and Bohua Chen and Li Yuan},
      year={2023},
      eprint={2306.16092},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
@misc{ChatLaw,
  author={Jiaxi Cui and Zongjian Li and Yang Yan and Bohua Chen and Li Yuan},
  title={ChatLaw},
  year={2023},
  publisher={GitHub},
  journal={GitHub repository},
  howpublished={\url{https://github.com/PKU-YuanGroup/ChatLaw}},
}
```



