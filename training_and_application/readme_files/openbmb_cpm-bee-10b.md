---
language:
- en
- zh
pipeline_tag: text-generation
---

# CPM-Bee

**CPM-Bee** is a fully open-source, commercially-usable Chinese-English bilingual base model with a capacity of ten billion parameters. It is the second milestone achieved through the training process of [**CPM-live**](https://live.openbmb.org/).
Utilizing the Transformer auto-regressive architecture, CPM-Bee has been pre-trained on an extensive corpus of trillion-scale tokens, thereby possessing remarkable foundational capabilities.

## Model description

- **Open-source and Commercial Usable**：OpenBMB adheres to the spirit of open-source, aiming to make large-scale models accessible to everyone. CPM-Bee, as a foudation model, is fully open-source and available for commercial use, contributing to the advancement of the field of large-scale models.

- **Excellent Performance in Chinese and English**： : CPM-Bee's base model has undergone rigorous selection and balancing of pre-training data, resulting in outstanding performance in both Chinese and English. For detailed information regarding evaluation tasks and results, please refer to the assessment documentation.


- **Vast and High-quality Corpus**： CPM-Bee, as a base model, has been trained on an extensive corpus of over trillion tokens, making it one of the models with the highest volume of training data within the open-source community. Furthermore, we have implemented stringent selection, cleaning, and post-processing procedures on the pre-training corpus to ensure its quality.

- **Support for OpenBMB System**： The OpenBMB system provides a comprehensive ecosystem of tools and scripts for high-performance pre-training, adaptation, compression, deployment, and tool development. CPM-Bee, as a base model, is accompanied by all the necessary tool scripts, enabling developers to efficiently utilize and explore advanced functionalities.


- **Conversational and Tool Usage Capabilities**： Building upon OpenBMB's exploration in instruction-based fine-tuning and tool learning, we have performed fine-tuning on top of the CPM-Bee base model, resulting in an instance model with powerful conversational and tool usage capabilities. The API and beta testing for this model will be made available in the near future.

## Intended uses & limitations

You can use the raw model for many NLP tasks like text generation or fine-tune it to a downstream task.

### How to use

```python
>>> from transformers import AutoModelForCausalLM, AutoTokenizer
>>> tokenizer = AutoTokenizer.from_pretrained("openbmb/cpm-bee-10b", trust_remote_code=True)
>>> model = AutoModelForCausalLM.from_pretrained("openbmb/cpm-bee-10b", trust_remote_code=True).cuda()  # 
>>> result = model.generate({"input": "今天天气不错，", "<ans>": ""}, tokenizer)
>>> print(result)
[{'input': '今天天气不错，', '<ans>': '适合睡觉。'}]
```

If you wanna use multi GPUs to inference, you can use `accelerate` as follow:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from accelerate import dispatch_model
from accelerate.utils import get_balanced_memory, infer_auto_device_map

tokenizer = AutoTokenizer.from_pretrained("openbmb/cpm-bee-10b", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("openbmb/cpm-bee-10b", trust_remote_code=True).cuda()

max_memory = get_balanced_memory(
    model, 
    no_split_module_classes=["CpmBeeTransformerBlock"]
)
device_map = infer_auto_device_map(model, max_memory=max_memory, no_split_module_classes=["CpmBeeTransformerBlock"]) 
# make sure the data on the same device when projecting hidden states to logits.
device_map["cpmbee.encoder.output_layernorm"] = device_map["cpmbee.input_embedding"] = 0

model = dispatch_model(model, device_map=device_map)

res = model.generate(
    [
        {"input": "今天天气是真的", "<ans>": ""},
        {"input": "NGC 6231是一个位于天蝎座的疏散星团，天球座标为赤经16时54分，赤纬-41度48分，视觉观测大小约45角分，亮度约2.6视星等，距地球5900光年。NGC 6231年龄约为三百二十万年，是一个非常年轻的星团，星团内的最亮星是5等的天蝎座 ζ1星。用双筒望远镜或小型望远镜就能看到个别的行星。NGC 6231在1654年被意大利天文学家乔瓦尼·巴蒂斯特·霍迪尔纳（Giovanni Battista Hodierna）以Luminosae的名字首次纪录在星表中，但是未见记载于夏尔·梅西耶的天体列表和威廉·赫歇尔的深空天体目录。这个天体在1678年被爱德蒙·哈雷（I.7）、1745年被夏西亚科斯（Jean-Phillippe Loys de Cheseaux）（9）、1751年被尼可拉·路易·拉卡伊（II.13）分别再次独立发现。", "question": "NGC 6231的经纬度是多少？", "<ans>": ""}
    ],
    tokenizer,
    max_new_tokens=100
)
print(res)

```

We suggest to use `bmtrain` to finetune CPM-Bee. Also, you can use `accelerate` and `deepspeed` to finetune CPM-Bee. Here we will give a brief example of a training loop:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from accelerate import Accelerator
from torch.utils.data import Dataset, DataLoader

accelerator = Accelerator()

trainset = Dataset()  # Make sure trainset.__getitem__() can get data with correct format like {"input": "...", "<ans>": ""}
# for details, you can read https://github.com/OpenBMB/CPM-Bee/tree/main/tutorials/basic_task_finetune
train_loader = DataLoader(trainset, batch_size=1)

tokenizer = AutoTokenizer.from_pretrained("openbmb/cpm-bee-10b", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("openbmb/cpm-bee-10b", trust_remote_code=True).cuda()

optimizer = torch.optim.Adam(model.parameters())

model, optimizer, train_loader = accelerator.prepare(
    model, optimizer, train_loader
)

for iter, data in enumerate(train_loader):
    optimizer.zero_grad()

    # change the data to a trainable format
    input_encoded = tokenizer.prepare_for_finetune(data, max_length=512).to(model.device)

    outputs = model(**input_encoded)
    loss = outputs.loss
    accelerator.backward(loss)
    optimizer.step()
```
You should design your own parallel and mix_precision training strategy on the basis of it.