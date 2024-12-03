---
license: apache-2.0
tags:
- text2text-generation
pipeline_tag: text2text-generation
language:
- zh
- en
widget:
- text: |-
    Human: 使用python写一个二分查找的代码
    Assistant: 
  example_title: code zh
- text: >-
    Human: Classify the sentiment of the following sentence into Positive,
    Neutral, or Negative: 

    Super excited about teaching Stanford’s first course on Large Language
    Models! Check the syllabus out here

    Assistant: 
  example_title: sentiment en
- text: |-
    Human: 今天天气怎么样，把这句话翻译成英语
    Assistant: 
  example_title: translation zh-en
- text: |-
    Human: 怎么让自己精力充沛，列5点建议
    Assistant: 
  example_title: brainstorming zh
- text: |-
    Human: 请以『春天的北京』为题写一首诗歌
    Assistant: 
  example_title: generation zh
- text: |-
    Human: 明天就假期结束了，有点抗拒上班，应该怎么办？
    Assistant: 
  example_title: brainstorming zh
- text: |-
    Human: 父母都姓吴，取一些男宝宝和女宝宝的名字
    Assistant: 
  example_title: brainstorming zh
- text: |-
    Human: 推荐几本金庸的武侠小说
    Assistant: 
  example_title: brainstorming zh
---

# Model Card for Model ID

## Welcome
If you find this model helpful, please *like* this model and star us on https://github.com/LianjiaTech/BELLE !

## Model description
BELLE is based on Bloomz-7b1-mt and finetuned with 2M Chinese data combined with 50,000 pieces of English data from the open source Stanford-Alpaca, resulting in good Chinese instruction understanding and response generation capabilities. 

The code of Chinese data generation and other detailed information can be found in our Github project repository: https://github.com/LianjiaTech/BELLE.

We trained models using datasets of different sizes (200,000, 600,000, 1,000,000, and 2,000,000 samples) for instruction learning, and we obtained different model versions as shown below:
| Datasize| 200,000 | 600,000 | 1,000,000 | 2,000,000 |
| ----- | ----- | ----- | ----- | ----- |
| Finetuned Model | [BELLE-7B-0.2M](https://huggingface.co/BelleGroup/BELLE-7B-0.2M) | [BELLE-7B-0.6M](https://huggingface.co/BelleGroup/BELLE-7B-0.6M) | [BELLE-7B-1M](https://huggingface.co/BelleGroup/BELLE-7B-1M) | [BELLE-7B-2M](https://huggingface.co/BelleGroup/BELLE-7B-2M) |

## Training hyper-parameters
| Parameter | Value |
| ------ | ------ |
| Batch size | 64 |
| Learning rate | 3e-6 |
| Epochs | 3 |
|Weight_decay | 0.001 |
|Warmup_rate | 0.1 |
|LR_scheduler | linear |

## Use model
Please note that the input should be formatted as follows in both **training** and **inference**.
``` python
Human: {input} \n\nAssistant:
``` 

BELLE can be easily loaded with AutoModelForCausalLM.
``` python
from transformers import AutoTokenizer, AutoModelForCausalLM
import sys

model_path = "./" # You can modify the path for storing the local model
model =  AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
print("Human:")
line = input()
while line:
        inputs = 'Human: ' + line.strip() + '\n\nAssistant:'
        input_ids = tokenizer(inputs, return_tensors="pt").input_ids
        outputs = model.generate(input_ids, max_new_tokens=200, do_sample = True, top_k = 30, top_p = 0.85, temperature = 0.35, repetition_penalty=1.2)
        rets = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        print("Assistant:\n" + rets[0].strip().replace(inputs, ""))
        print("\n------------------------------------------------\nHuman:")
        line = input()

```

The above example did not utilize the context from previous turns of the conversation. If you want to perform multi-turn dialogue understanding, you can concatenate the previous turns of the conversation in the format of Human:{input}\n\nAssistant:{output} and input it to the generate function

## Limitations
There still exists a few issues in the model trained on current base model and data:

1. The model might generate factual errors when asked to follow instructions related to facts.

2. Occasionally generates harmful responses since the model still struggles to identify potential harmful instructions.

3. Needs improvements on reasoning and coding.

Since the model still has its limitations, we require developers only use the open-sourced code, data, model and any other artifacts generated via this project for research purposes. Commercial use and other potential harmful use cases are not allowed.

## Some use cases

| Human | Assitant |
| ----- | ------ |
| 帮忙写一篇散文诗，主题为扎根，终有一天，我们会变成参天大树| 在人生路途中，我们每个人都会经历各种各样的挑战和困难。但是，这些困难并不是让我们停滞不前的原因，而是让我们成长、进步的机会。只有通过不断地努力扎根，才能最终成为参天大树。<br/><br/>首先，扎根需要我们拥有坚定的信念和目标。没有目标和信仰的人，很难有前进的动力。因此，我们需要明确自己的理想和追求，并为之付出行动的努力。只有在不断努力的过程中，我们才能够逐渐扎下根基，形成强大的内心力量。<br/><br/>其次，扎根需要我们具备勤奋的精神。成功不是靠天赋，而是要靠勤奋和毅力。只有持之以恒地学习、实践和积累经验，我们才能逐步提高自己的能力和水平。而这种精神也是我们在面对各种困难时所需要的，因为只有坚持不懈地努力，才能克服一切困难，走向成功的道路。<br/><br/>最后，扎根需要我们有勇气去接受失败。生活中难免会遇到挫折和失败，但我们不能因此而气馁或放弃。相反，我们应该从失败中吸取教训，总结经验教训，并不断调整自己的方向和方法。只有勇于尝试和创新，我们才能真正扎下深厚的根基，实现自己的人生价值。<br/><br/>总之，扎根是一个漫长而又充满挑战的过程，它需要我们不断地努力和探索。只有通过不断的扎实根基，我们才能在未来的路上越走越稳健，越来越接近我们的梦想。 |
| 请生成一个房产经纪人和客户的对话 | 经纪人：你好！我是XX房地产中介公司的经纪人。您想了解哪些信息？<br/>客户：我正在寻找一栋公寓，可以让我住得舒适又安全。<br/>经纪人：在我们公司里有很多这样的房源。我可以给您介绍几个适合您的选择。<br/>客户：好的，请告诉我一些细节。<br/>经纪人：这栋公寓位于市中心，步行距离内有许多商店和餐馆，交通也十分便利。此外，它配备有现代化的设施和安全系统，以确保您的居住体验更加安全和舒适。<br/>客户：听起来很不错。我想看看照片和视频。<br/>经纪人：当然，这是该地区的几个房源，您可以从中选择最合适的一栋公寓。<br/>客户：好的，我会考虑一下。<br/>经纪人：非常感谢您的咨询，如果您有任何其他问题或需要帮助，随时联系我。 |
| Classify the sentiment of the following sentence into Positive, Neutral, or Negative: <br/>Super excited about teaching Stanford’s first course on Large Language Models! Check the syllabus out here | Positive |
| 列出3个不同的机器学习算法，并说明它们的适用范围。 | 1. 支持向量机（SVM）-适用于分类和回归问题，特别适用于处理非线性数据集。<br/>2. 决策树（Decision Tree） -适用于分类、回归和聚类等问题，可以很好地理解和可视化。<br/>3. 随机森林（Random Forest）-适用于分类和回归问题，能够有效地处理高维数据和特征选择困难的问题。 |
| 周杰伦哪年出生的 | 周杰伦出生于1979年1月18日。 |
| 女性应该什么时候结婚？ | 这取决于个人的意愿和情况。一些女性可能希望早些结婚，而另一些则可能更喜欢晚些结婚。此外，女性的教育水平、职业发展等因素也会影响她们的决定。 |
| 帮我写一个周报，主题包含：chatgpt，客服 | 尊敬的领导和同事们：<br/><br/>本周我们团队的主要工作是使用Chatgpt（聊天机器人平台）来提升客户服务质量。以下是我对这个主题的简要报告：<br/><br/>1. 使用ChatgPT进行在线聊天<br/>在过去的一周里，我们的团队使用了Chatgpt来进行在线聊天。 chatgpt能够提供更加智能化的回答，使得客户可以更快地得到他们需要的帮助。此外，它还可以根据客户的需求自动推荐相关的产品和服务。这大大提高了我们服务的效率和质量。<br/><br/>2. 优化客服流程<br/>在上一周中，我们的团队对客服流程进行了一些改进。我们发现，如果客户遇到的问题比较复杂或者需要更多的支持，那么他们的满意度会降低。因此，我们在客服平台上添加了一些新的功能，例如自助问答、知识库等，这些功能可以帮助客户更好地解决问题和获取更多信息。<br/><br/>3. 加强培训和支持<br/>为了进一步提高我们的客服水平，我们的团队正在加强员工的培训和支持。我们会定期组织内部培训和外部学习机会，以便员工不断更新自己的技能和知识。同时，我们也加强了与客户之间的沟通，了解他们的需求和反馈，以更好地满足客户的要求。<br/><br/>总的来说，本周的重点工作是使用Chatgpt来改善客户服务体验，并且优化了客服流程。我们还将继续加强员工的培训和支持，以提高整个团队的服务能力和水平。感谢大家的关注和支持！ |
| “下好一盘围棋需要强大的计算能力。”把这句话翻译成英文 | To play well in a game of Go requires strong computing ability. |

## Citation

Please cite us when using our code, data or model.

```
@misc{BELLE,
  author = {Yunjie Ji, Yong Deng, Yan Gong, Yiping Peng, Qiang Niu, Baochang Ma, Xiangang Li},
  title = {BELLE: Bloom-Enhanced Large Language model Engine },
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/LianjiaTech/BELLE}},
}
```

Cite the original BLOOM, Stanford Alpaca and Self-Instruct papers as well!

***

## 欢迎
如果您觉得此模型对您有帮助，请like此模型并在https://github.com/LianjiaTech/BELLE 项目中star我们！

## 模型描述
BELLE模型以Bloomz-7b1-mt为基础，在 2.0M 条中文数据上，结合Stanford-Alpaca开源的5万条英文数据上训练，取得了较好的中文instruction理解以及response生成能力。

中文数据生成代码及其他详细信息，位于我们的Github项目仓库: https://github.com/LianjiaTech/BELLE

我们采取了不同大小规模（20万、60万、100万和200万样本）的指令学习的数据集训练模型，我们得到不同的模型版本如下所示:
| Datasize| 200,000 | 600,000 | 1,000,000 | 2,000,000 | 
| ----- | ----- | ----- | ----- | ----- |
| Finetuned Model | [BELLE-7B-0.2M](https://huggingface.co/BelleGroup/BELLE-7B-0.2M) | [BELLE-7B-0.6M](https://huggingface.co/BelleGroup/BELLE-7B-0.6M) | [BELLE-7B-1M](https://huggingface.co/BelleGroup/BELLE-7B-1M) | [BELLE-7B-2M](https://huggingface.co/BelleGroup/BELLE-7B-2M)

## 模型训练超参数
| 参数 | 值 |
| ------ | ------ |
| Batch size | 64 |
| Learning rate | 3e-6 |
| Epochs | 3 |
|Weight_decay | 0.001 |
|Warmup_rate | 0.1 |
|LR_scheduler | linear |

## 使用模型
请注意，在训练和推理时，模型的输入应该处理成如下形式：
``` python
Human: {input} \n\nAssistant:
``` 

通过AutoModelForCausalLM即可直接载入模型并使用。

``` python
from transformers import AutoTokenizer, AutoModelForCausalLM
import sys

model_path = "./" # You can modify the path for storing the local model
model =  AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
print("Human:")
line = input()
while line:
        inputs = 'Human: ' + line.strip() + '\n\nAssistant:'
        input_ids = tokenizer(inputs, return_tensors="pt").input_ids
        outputs = model.generate(input_ids, max_new_tokens=200, do_sample = True, top_k = 30, top_p = 0.85, temperature = 0.35, repetition_penalty=1.2)
        rets = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        print("Assistant:\n" + rets[0].strip().replace(inputs, ""))
        print("\n------------------------------------------------\nHuman:")
        line = input()

```

上面样例没有利用对话上文，如果你想做多轮对话理解，可以将对话上文按照Human:{input}\n\nAssistant:{output} 方式拼接起来输入给generate函数

## 局限性和使用限制
基于当前数据和基础模型训练得到的SFT模型，在效果上仍存在以下问题：

1. 在涉及事实性的指令上可能会产生违背事实的错误回答。

2. 对于具备危害性的指令无法很好的鉴别，由此会产生危害性言论。

3. 在一些涉及推理、代码等场景下模型的能力仍有待提高。

基于以上模型局限性，我们要求开发者仅将我们开源的代码、数据、模型及后续用此项目生成的衍生物用于研究目的，不得用于商业，以及其他会对社会带来危害的用途。

## 一些示例

| Human | Assitant |
| ----- | ------ |
| 帮忙写一篇散文诗，主题为扎根，终有一天，我们会变成参天大树| 在人生路途中，我们每个人都会经历各种各样的挑战和困难。但是，这些困难并不是让我们停滞不前的原因，而是让我们成长、进步的机会。只有通过不断地努力扎根，才能最终成为参天大树。<br/><br/>首先，扎根需要我们拥有坚定的信念和目标。没有目标和信仰的人，很难有前进的动力。因此，我们需要明确自己的理想和追求，并为之付出行动的努力。只有在不断努力的过程中，我们才能够逐渐扎下根基，形成强大的内心力量。<br/><br/>其次，扎根需要我们具备勤奋的精神。成功不是靠天赋，而是要靠勤奋和毅力。只有持之以恒地学习、实践和积累经验，我们才能逐步提高自己的能力和水平。而这种精神也是我们在面对各种困难时所需要的，因为只有坚持不懈地努力，才能克服一切困难，走向成功的道路。<br/><br/>最后，扎根需要我们有勇气去接受失败。生活中难免会遇到挫折和失败，但我们不能因此而气馁或放弃。相反，我们应该从失败中吸取教训，总结经验教训，并不断调整自己的方向和方法。只有勇于尝试和创新，我们才能真正扎下深厚的根基，实现自己的人生价值。<br/><br/>总之，扎根是一个漫长而又充满挑战的过程，它需要我们不断地努力和探索。只有通过不断的扎实根基，我们才能在未来的路上越走越稳健，越来越接近我们的梦想。 |
| 请生成一个房产经纪人和客户的对话 | 经纪人：你好！我是XX房地产中介公司的经纪人。您想了解哪些信息？<br/>客户：我正在寻找一栋公寓，可以让我住得舒适又安全。<br/>经纪人：在我们公司里有很多这样的房源。我可以给您介绍几个适合您的选择。<br/>客户：好的，请告诉我一些细节。<br/>经纪人：这栋公寓位于市中心，步行距离内有许多商店和餐馆，交通也十分便利。此外，它配备有现代化的设施和安全系统，以确保您的居住体验更加安全和舒适。<br/>客户：听起来很不错。我想看看照片和视频。<br/>经纪人：当然，这是该地区的几个房源，您可以从中选择最合适的一栋公寓。<br/>客户：好的，我会考虑一下。<br/>经纪人：非常感谢您的咨询，如果您有任何其他问题或需要帮助，随时联系我。 |
| Classify the sentiment of the following sentence into Positive, Neutral, or Negative: <br/>Super excited about teaching Stanford’s first course on Large Language Models! Check the syllabus out here | Positive |
| 列出3个不同的机器学习算法，并说明它们的适用范围。 | 1. 支持向量机（SVM）-适用于分类和回归问题，特别适用于处理非线性数据集。<br/>2. 决策树（Decision Tree） -适用于分类、回归和聚类等问题，可以很好地理解和可视化。<br/>3. 随机森林（Random Forest）-适用于分类和回归问题，能够有效地处理高维数据和特征选择困难的问题。 |
| 周杰伦哪年出生的 | 周杰伦出生于1979年1月18日。 |
| 女性应该什么时候结婚？ | 这取决于个人的意愿和情况。一些女性可能希望早些结婚，而另一些则可能更喜欢晚些结婚。此外，女性的教育水平、职业发展等因素也会影响她们的决定。 |
| 帮我写一个周报，主题包含：chatgpt，客服 | 尊敬的领导和同事们：<br/><br/>本周我们团队的主要工作是使用Chatgpt（聊天机器人平台）来提升客户服务质量。以下是我对这个主题的简要报告：<br/><br/>1. 使用ChatgPT进行在线聊天<br/>在过去的一周里，我们的团队使用了Chatgpt来进行在线聊天。 chatgpt能够提供更加智能化的回答，使得客户可以更快地得到他们需要的帮助。此外，它还可以根据客户的需求自动推荐相关的产品和服务。这大大提高了我们服务的效率和质量。<br/><br/>2. 优化客服流程<br/>在上一周中，我们的团队对客服流程进行了一些改进。我们发现，如果客户遇到的问题比较复杂或者需要更多的支持，那么他们的满意度会降低。因此，我们在客服平台上添加了一些新的功能，例如自助问答、知识库等，这些功能可以帮助客户更好地解决问题和获取更多信息。<br/><br/>3. 加强培训和支持<br/>为了进一步提高我们的客服水平，我们的团队正在加强员工的培训和支持。我们会定期组织内部培训和外部学习机会，以便员工不断更新自己的技能和知识。同时，我们也加强了与客户之间的沟通，了解他们的需求和反馈，以更好地满足客户的要求。<br/><br/>总的来说，本周的重点工作是使用Chatgpt来改善客户服务体验，并且优化了客服流程。我们还将继续加强员工的培训和支持，以提高整个团队的服务能力和水平。感谢大家的关注和支持！ |
| “下好一盘围棋需要强大的计算能力。”把这句话翻译成英文 | To play well in a game of Go requires strong computing ability. |

## 引用
如果使用本项目的代码、数据或模型，请引用本项目。
```
@misc{BELLE,
  author = {Yunjie Ji, Yong Deng, Yan Gong, Yiping Peng, Qiang Niu, Baochang Ma, Xiangang Li},
  title = {BELLE: Bloom-Enhanced Large Language model Engine },
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/LianjiaTech/BELLE}},
}
```
也请同时引用原始的BLOOM论文、Stanford Alpaca和Self-Instruct论文。