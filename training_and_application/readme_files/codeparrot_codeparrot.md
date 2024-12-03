---
language: code
tags:
- code
- gpt2
- generation
datasets:
- codeparrot/codeparrot-clean-train
widget:
- text: "from transformer import"
  example_title: "Transformers"
- text: "def print_hello_world():\n\t"
  example_title: "Hello World!"
- text: "def get_file_size(filepath):"
  example_title: "File size"
- text: "import numpy as"
  example_title: "Numpy"
model-index:
- name: codeparrot
  results:
  - task: 
      name: Code Generation
      type: code-generation
    dataset:
      name: "HumanEval" 
      type: openai_humaneval
    metrics:
       - name: pass@1
         type: code_eval
         value: 3.99
       - name: pass@10
         type: code_eval
         value: 8.69
       - name: pass@100
         type: code_eval
         value: 17.88
---


# CodeParrot 🦜

CodeParrot 🦜 is a GPT-2 model (1.5B parameters) trained to generate Python code. After the initial training and release of v1.0 we trained the model some more and released v1.1 (see below for details).

## Usage

You can load the CodeParrot model and tokenizer directly in `transformers`:

```Python
from transformers import AutoTokenizer, AutoModelWithLMHead
  
tokenizer = AutoTokenizer.from_pretrained("codeparrot/codeparrot")
model = AutoModelWithLMHead.from_pretrained("codeparrot/codeparrot")

inputs = tokenizer("def hello_world():", return_tensors="pt")
outputs = model(**inputs)
```

or with a `pipeline`:

```Python
from transformers import pipeline

pipe = pipeline("text-generation", model="codeparrot/codeparrot")
outputs = pipe("def hello_world():")
```

## Training

The model was trained on the cleaned [CodeParrot 🦜 dataset](https://huggingface.co/datasets/codeparrot/codeparrot-clean) in two steps. After the initial training (v1.0) the model was trained for another 30k steps resulting in v1.1 and you find the settings in the following table:

|Config| v1.0| v1.1|
|------|------------------|--------------------|
|Batch size| 512 | 512 |
|Context size| 1024 | 1024 |
|Training steps| 50'000| 30'000
|Gradient accumulation| 16| 16 |
|Gradient checkpointing| True| True |
|Learning rate| 2e-4 | 5e-5 |
|Weight decay | 0.1 | 0.1 |
|Warmup steps| 750 | 750 |
|Schedule| Cosine | Cosine |

The training was executed on 16 x A100 (40GB) GPUs. This setting amounts to roughly 26 + 15 billion tokens.

## Performance

We evaluated the model on OpenAI's [HumanEval](https://huggingface.co/datasets/openai_humaneval) benchmark which consists of programming challenges:

| Metric | v1.0 | v1.1 |
|--------|-----|-----|
|pass@1 | 3.58% | 3.99% |
|pass@10 | 8.03% | 8.69% |
|pass@100 | 14.96% | 17.88% |

The [pass@k metric](https://huggingface.co/metrics/code_eval) tells the probability that at least one out of k generations passes the tests. 

## Resources

- Dataset: [full](https://huggingface.co/datasets/codeparrot/codeparrot-clean), [train](https://huggingface.co/datasets/codeparrot/codeparrot-clean-train), [valid](https://huggingface.co/datasets/codeparrot/codeparrot-clean-valid)
- Code: [repository](https://github.com/huggingface/transformers/tree/master/examples/research_projects/codeparrot)
- Spaces: [generation](), [highlighting]()