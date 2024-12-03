---
language:
- en
---

<div align='center'>
<h1>Generative Multimodal Models are In-Context Learners</h1h1>
<h3><a href="">Generative Multimodal Models are In-Context Learners</a></h3>

[Quan Sun](https://github.com/Quan-Sun)<sup>1*</sup>, [Yufeng Cui](https://scholar.google.com/citations?hl=en&user=5Ydha2EAAAAJ)<sup>1*</sup>, [Xiaosong Zhang](https://zhangxiaosong18.github.io)<sup>1*</sup>, [Fan Zhang](https://scholar.google.com/citations?user=VsJ39HMAAAAJ)<sup>1*</sup>, [Qiying Yu](https://yqy2001.github.io)<sup>2,1*</sup>, [Zhengxiong Luo](https://greatlog.github.io)<sup>1</sup>, [Yueze Wang]()<sup>1</sup>, [Yongming Rao](https://raoyongming.github.io)<sup>1</sup>,<br>[Jingjing Liu](https://air.tsinghua.edu.cn/en/info/1046/1194.htm)<sup>2</sup>, [Tiejun Huang](https://scholar.google.com/citations?user=knvEK4AAAAAJ&hl=en)<sup>1,3</sup>, [Xinlong Wang](https://www.xloong.wang/)<sup>1†</sup>
	
<sup>1</sup> [BAAI](https://www.baai.ac.cn/english.html), <sup>2</sup> [THU](https://air.tsinghua.edu.cn), <sup>3</sup> [PKU](https://english.pku.edu.cn/) <br><sup>*</sup> equal contribution   <sup>†</sup> project lead

|  [Paper](https://arxiv.org/abs/2312.13286) | [🤗HF Demo](https://huggingface.co/spaces/BAAI/Emu2) | [Demo](https://emu.ssi.plus) | [Project Page](https://baaivision.github.io/emu2/) | [Github](https://github.com/baaivision/Emu)

</div>

The human ability to easily solve multimodal tasks in context (i.e., with only a few demonstrations or simple instructions), is what current multimodal systems have largely struggled to imitate. 
In this work, we demonstrate that the task-agnostic in-context learning capabilities of large multimodal models can be significantly enhanced by effective scaling-up. 
We introduce **Emu2**, a generative multimodal model with 37 billion parameters, trained on large-scale multimodal sequences with a unified autoregressive objective.
**Emu2** exhibits strong multimodal in-context learning abilities, even emerging to solve tasks that require on-the-fly reasoning, such as visual prompting and object-grounded generation.
The model sets a new record on multiple multimodal understanding tasks in few-shot settings.
When instruction-tuned to follow specific instructions, **Emu2** further achieves new state-of-the-art on challenging tasks such as question answering benchmarks for large multimodal models and open-ended subject-driven generation.
These achievements demonstrate that **Emu2** can serve as a base model and general-purpose interface for a wide range of multimodal tasks. 
Code and models are publicly available to facilitate future research.

## Model Weights

| Model name         | Weight                                                  |
| ------------------ | ------------------------------------------------------- |
| **Emu2** | [🤗 HF link](https://huggingface.co/BAAI/Emu2) |
| **Emu2-Chat** | [🤗 HF link](https://huggingface.co/BAAI/Emu2-Chat) |
| **Emu2-Gen** | [🤗 HF link](https://huggingface.co/BAAI/Emu2-Gen) |


## Inference (Huggingface Version)

#### Single GPU

```python
from PIL import Image
import requests
import torch 
from transformers import AutoModelForCausalLM, AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("BAAI/Emu2")

model = AutoModelForCausalLM.from_pretrained(
    "BAAI/Emu2",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    trust_remote_code=True).to('cuda').eval()


# `[<IMG_PLH>]` is the image placeholder which will be replaced by image embeddings. 
# the number of `[<IMG_PLH>]` should be equal to the number of input images

query = '[<IMG_PLH>]Describe the image in details:' 
image = Image.open(requests.get('https://github.com/baaivision/Emu/Emu2/examples/blue_black_1_top_left.jpg?raw=true',stream=True).raw).convert('RGB')


inputs = model.build_input_ids(
    text=[query],
    tokenizer=tokenizer,
    image=[image]
)

with torch.no_grad():
     outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        image=inputs["image"].to(torch.bfloat16),
        max_new_tokens=64,
        length_penalty=-1)

output_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)
```

Interleaved image and text

```python
from PIL import Image
import requests
import torch 
from transformers import AutoModelForCausalLM, AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("BAAI/Emu2")

model = AutoModelForCausalLM.from_pretrained(
    "BAAI/Emu2",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    trust_remote_code=True).to('cuda').eval()

# `[<IMG_PLH>]` is the image placeholder which will be replaced by image embeddings. 
# the number of `[<IMG_PLH>]` should be equal to the number of input images

query = "[<IMG_PLH>][red, white, 3, bottom left].[<IMG_PLH>][yellow, white, 2, top left].[<IMG_PLH>][green, black, 4, bottom right][<IMG_PLH>]"

images = [
    Image.open(requests.get('https://github.com/baaivision/Emu/Emu2/examples/red_white_3_bottom_left.jpg?raw=true',stream=True).raw).convert('RGB'),
    Image.open(requests.get('https://github.com/baaivision/Emu/Emu2/examples/yellow_white_2_top_right.jpg?raw=true',stream=True).raw).convert('RGB'),
    Image.open(requests.get('https://github.com/baaivision/Emu/Emu2/examples/green_black_4_bottom_right.jpg?raw=true',stream=True).raw).convert('RGB'),
    Image.open(requests.get('https://github.com/baaivision/Emu/Emu2/examples/blue_black_1_top_left.jpg?raw=true',stream=True).raw).convert('RGB'),
]

inputs = model.build_input_ids(
    text=[query],
    tokenizer=tokenizer,
    image=images

)

with torch.no_grad():
     outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        image=inputs["image"].to(torch.bfloat16),
        max_new_tokens=64,
        length_penalty=-1)

output_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)
```

#### Multi GPU


```python
from PIL import Image 
import requests
import torch 
from transformers import AutoModelForCausalLM, AutoTokenizer
from accelerate import init_empty_weights, infer_auto_device_map, load_checkpoint_and_dispatch

tokenizer = AutoTokenizer.from_pretrained("BAAI/Emu2")

with init_empty_weights():
     model = AutoModelForCausalLM.from_pretrained(
        "BAAI/Emu2",
        torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
        trust_remote_code=True)  

device_map = infer_auto_device_map(model, max_memory={0:'38GiB',1:'38GiB',}, no_split_module_classes=['Block','LlamaDecoderLayer'])  
# input and output logits should be on same device
device_map["model.decoder.lm.lm_head"] = 0

model = load_checkpoint_and_dispatch(
    model, 
    'local/path/to/hf/version/Emu2/model',
    device_map=device_map).eval()

# `[<IMG_PLH>]` is the image placeholder which will be replaced by image embeddings. 
# the number of `[<IMG_PLH>]` should be equal to the number of input images

query = '[<IMG_PLH>]Describe the image in details:' 
image = Image.open(requests.get('https://github.com/baaivision/Emu/Emu2/examples/blue_black_1_top_left.jpg?raw=true',stream=True).raw).convert('RGB')

inputs = model.build_input_ids(
    text=[query],
    tokenizer=tokenizer,
    image=[image]

)

with torch.no_grad():
     outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        image=inputs["image"].to(torch.bfloat16),
        max_new_tokens=64,
        length_penalty=-1)

output_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)
```

Interleaved image and text

```python
from PIL import Image 
import requests
import torch 
from transformers import AutoModelForCausalLM, AutoTokenizer
from accelerate import init_empty_weights, infer_auto_device_map, load_checkpoint_and_dispatch

tokenizer = AutoTokenizer.from_pretrained("BAAI/Emu2")

with init_empty_weights():
     model = AutoModelForCausalLM.from_pretrained(
        "BAAI/Emu2",
        torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
        trust_remote_code=True)  

device_map = infer_auto_device_map(model, max_memory={0:'38GiB',1:'38GiB',}, no_split_module_classes=['Block','LlamaDecoderLayer'])  
# input and output logits should be on same device
device_map["model.decoder.lm.lm_head"] = 0

model = load_checkpoint_and_dispatch(
    model, 
    'local/path/to/hf/version/Emu2/model',
    device_map=device_map).eval()

# `[<IMG_PLH>]` is the image placeholder which will be replaced by image embeddings. 
# the number of `[<IMG_PLH>]` should be equal to the number of input images
query = "[<IMG_PLH>][red, white, 3, bottom left].[<IMG_PLH>][yellow, white, 2, top left].[<IMG_PLH>][green, black, 4, bottom right][<IMG_PLH>]"

images = [
    Image.open(requests.get('https://github.com/baaivision/Emu/Emu2/examples/red_white_3_bottom_left.jpg?raw=true',stream=True).raw).convert('RGB'),
    Image.open(requests.get('https://github.com/baaivision/Emu/Emu2/examples/yellow_white_2_top_right.jpg?raw=true',stream=True).raw).convert('RGB'),
    Image.open(requests.get('https://github.com/baaivision/Emu/Emu2/examples/green_black_4_bottom_right.jpg?raw=true',stream=True).raw).convert('RGB'),
    Image.open(requests.get('https://github.com/baaivision/Emu/Emu2/examples/blue_black_1_top_left.jpg?raw=true',stream=True).raw).convert('RGB'),
]

inputs = model.build_input_ids(
    text=[query],
    tokenizer=tokenizer,
    image=images

)

with torch.no_grad():
     outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        image=inputs["image"].to(torch.bfloat16),
        max_new_tokens=64,
        length_penalty=-1)

output_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)
```

#### Quantization

Check quantization guidance at [transformers](https://huggingface.co/docs/transformers/v4.28.0/main_classes/quantization)


```python
from PIL import Image 
import requests
import torch 
from transformers import AutoModelForCausalLM, AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("BAAI/Emu2")

model = AutoModelForCausalLM.from_pretrained(
    "BAAI/Emu2",
    load_in_4bit=True,
    trust_remote_code=True, 
    bnb_4bit_compute_dtype=torch.float16).eval()

query = '[<IMG_PLH>]Describe the image in details:' 
image = Image.open(requests.get('https://github.com/baaivision/Emu/Emu2/examples/blue_black_1_top_left.jpg?raw=true',stream=True).raw).convert('RGB')

inputs = model.build_input_ids(
    text=[query],
    tokenizer=tokenizer,
    image=[image]

)

with torch.no_grad():
     outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        image=inputs["image"].to(torch.float16), # should be torch.float16
        max_new_tokens=64,
        length_penalty=-1)

output_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)
```

## Citation

If you find Emu2 useful for your research and applications, please consider starring this repository and citing:

```
@article{Emu2,
    title={Generative Multimodal Models are In-Context Learners}, 
    author={Quan Sun and Yufeng Cui and Xiaosong Zhang and Fan Zhang and Qiying Yu and Zhengxiong Luo and Yueze Wang and Yongming Rao and Jingjing Liu and Tiejun Huang and Xinlong Wang},
    publisher={arXiv preprint arXiv:2312.13286},
    year={2023},
}
```