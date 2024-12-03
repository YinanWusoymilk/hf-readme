---
license: apache-2.0
datasets:
- bigcode/the-stack-dedup
library_name: transformers
language:
- code
---

## CodeSage-Large

### Model description
CodeSage is a new family of open code embedding models with an encoder architecture that support a wide range of source code understanding tasks. It is introduced in the paper:

[Code Representation Learning At Scale by 
Dejiao Zhang*, Wasi Uddin Ahmad*, Ming Tan, Hantian Ding, Ramesh Nallapati, Dan Roth, Xiaofei Ma, Bing Xiang](https://arxiv.org/abs/2402.01935) (* indicates equal contribution).

### Pretraining data
This checkpoint is trained on the Stack data (https://huggingface.co/datasets/bigcode/the-stack-dedup). Supported languages (9 in total) are as follows: c, c-sharp, go, java, javascript, typescript, php, python, ruby.

### Training procedure
This checkpoint is first trained on code data via masked language modeling (MLM) and then on bimodal text-code pair data. Please refer to the paper for more details.

### How to use
This checkpoint consists of an encoder (1.3B model), which can be used to extract code embeddings of 2048 dimension. It can be easily loaded using the AutoModel functionality and employs the Starcoder tokenizer (https://arxiv.org/pdf/2305.06161.pdf).

```
from transformers import AutoModel, AutoTokenizer

checkpoint = "codesage/codesage-large"
device = "cuda"  # for GPU usage or "cpu" for CPU usage

# Note: CodeSage requires adding eos token at the end of
# each tokenized sequence to ensure good performance
tokenizer = AutoTokenizer.from_pretrained(checkpoint, trust_remote_code=True, add_eos_token=True)

model = AutoModel.from_pretrained(checkpoint, trust_remote_code=True).to(device)

inputs = tokenizer.encode("def print_hello_world():\tprint('Hello World!')", return_tensors="pt").to(device)
embedding = model(inputs)[0]
print(f'Dimension of the embedding: {embedding[0].size()}')
# Dimension of the embedding: torch.Size([14, 2048])
```

### BibTeX entry and citation info
```
@inproceedings{
    zhang2024codesage,
    title={CodeSage: Code Representation Learning At Scale},
    author={Dejiao Zhang* and Wasi Ahmad* and Ming Tan and Hantian Ding and Ramesh Nallapati and Dan Roth and Xiaofei Ma and Bing Xiang},
    booktitle={The Twelfth International Conference on Learning Representations},
    year={2024},
    url={https://openreview.net/forum?id=vfzRRjumpX}
}
```