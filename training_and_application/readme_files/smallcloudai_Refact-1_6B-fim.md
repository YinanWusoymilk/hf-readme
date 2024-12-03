---
pipeline_tag: text-generation
inference: true
widget:
- text: 'def print_hello_world():'
  example_title: Hello world
  group: Python
license: bigscience-openrail-m
pretrain-datasets:
- books
- arxiv
- c4
- falcon-refinedweb
- wiki
- github-issues
- stack_markdown
- self-made dataset of permissive github code
datasets:
- bigcode/the-stack-dedup
- rombodawg/2XUNCENSORED_MegaCodeTraining188k
- bigcode/commitpackft
metrics:
- code_eval
library_name: transformers
tags:
- code
model-index:
- name: Refact-1.6B
  results:
  - task:
      type: text-generation
    dataset:
      type: openai_humaneval
      name: HumanEval
    metrics:
    - name: pass@1 (T=0.01)
      type: pass@1
      value: 32.0
      verified: false
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 31.5
      verified: false
    - name: pass@10 (T=0.8)
      type: pass@10
      value: 53.0
      verified: false
    - name: pass@100 (T=0.8)
      type: pass@100
      value: 76.9
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalSynthesize Python
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 35.8
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalSynthesize JavaScript
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 31.6
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalSynthesize Java
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 29.1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalSynthesize Go
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: -1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalSynthesize C++
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 26.3
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalSynthesize Rust
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: -1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalSynthesize Average
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: -1
      verified: false




      
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixTests Python
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 18.38
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixTests JavaScript
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 12.28
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixTests Java
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 15.12
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixTests Go
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: -1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixTests C++
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 13.17
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixTests Rust
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 2.8
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixTests Average
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: -1
      verified: false





      
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixDocs Python
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 26.92
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixDocs JavaScript
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 26.85
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixDocs Java
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 30.76
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixDocs Go
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: -1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixDocs C++
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 25.94
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixDocs Rust
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 8.44
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalFixDocs Average
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: -1
      verified: false



     
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalExplain Python
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 26.46
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalExplain JavaScript
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 17.86
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalExplain Java
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 20.94
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalExplain Go
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: -1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalExplain C++
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 18.78
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalExplain Rust
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: -1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: bigcode/humanevalpack
      name: HumanEvalExplain Average
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: -1
      verified: false


  - task:
      type: text-generation
    dataset:
      type: mbpp
      name: MBPP
    metrics:
    - name: pass@1 (T=0.01)
      type: pass@1
      value: 31.15
      verified: false
  - task:
      type: text-generation
    dataset:
      type: ds1000
      name: DS-1000 (Overall Completion)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 10.1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (C++)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 21.61
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (C#)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 13.91
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (D)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 9.5
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Go)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 53.57
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Java)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 21.58
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Julia)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 13.75
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (JavaScript)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 26.88
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Lua)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 15.26
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (PHP)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 23.04
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Perl)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 12.1
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Python)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 29.6
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (R)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 13.77
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Ruby)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 12.68
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Racket)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 4.29
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Rust)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 19.54
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Scala)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 18.33
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Bash)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 5.7
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (Swift)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 17.68
      verified: false
  - task:
      type: text-generation
    dataset:
      type: nuprl/MultiPL-E
      name: MultiPL-HumanEval (TypeScript)
    metrics:
    - name: pass@1 (T=0.2)
      type: pass@1
      value: 25
      verified: false

language:
- en
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/643a9dd0c5f633a7fa7e804a/HkB0QYV0BbmB3ktMugbZy.png)


# Refact-1.6B

Finally, the model we started training with our [blog post](https://refact.ai/blog/2023/applying-recent-innovations-to-train-model/) is ready 🎉

After fine-tuning on generated data, it beats Replit 3b, Stability Code 3b and many other models. It almost beats
StarCoder ten times the size!


Model                 | Size          | HumanEval pass@1   | HumanEval pass@10  |
----------------------|---------------|--------------------|--------------------|
DeciCoder-1b          |   1b          |  19.1%             |                    |
<b>Refact-1.6-fim</b> | <b>1.6b</b>   |  <b>32.0%</b>      | <b>53.0%</b>       |
StableCode            |   3b          |  20.2%             | 33.8%              |
ReplitCode v1         |   3b          |  21.9%             |                    |
CodeGen2.5-multi      |   7b          |  28.4%             | 47.5%              |
CodeLlama             |   7b          |  33.5%             | 59.6%              |
StarCoder             |  15b          |  33.6%             |                    |

Likely, it's the best model for practical use in your IDE for code completion because it's smart and fast!
You can start using it right now by downloading the
[Refact plugin](https://refact.ai/). You can host the model yourself, too, using the
[open source docker container](https://github.com/smallcloudai/refact).

And it's multi-language (see MultiPL-HumanEval and other metrics below) and it works as a chat (see the section below).

# It Works As a Chat

The primary application of this model is code completion (infill) in multiple programming languages.
But it works as a chat quite well.

HumanEval results using instruction following (chat) format, against models specialized for chat only:

Model                  | Size   | pass@1   | pass@10  |
-----------------------|--------|----------|----------|
<b>Refact-1.6-fim</b>  | 1.6b   |  38.4%   | 55.6%    |
StableCode-instruct    |   3b   |  26.9%   | 36.2%    |
OctoGeeX               |   6b   |  44.7%   |          |
CodeLlama-instruct     |   7b   |  34.8%   | 64.3%    |
CodeGen2.5-instruct    |   7b   |  36.2%   | 60.87    |
CodeLlama-instruct     |  13b   |  42.7%   | 71.6%    |
StarChat-β             |  15b   |  33.5%   |          |
OctoCoder              |  15b   |  46.2%   |          |


# Example

Fill-in-the-middle uses special tokens to identify the prefix/middle/suffix part of the input and output:

```python
# pip install -q transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "smallcloudai/Refact-1_6B-fim"
device = "cuda" # for GPU usage or "cpu" for CPU usage

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True).to(device)

prompt = '<fim_prefix>def print_hello_world():\n    """<fim_suffix>\n    print("Hello world!")<fim_middle>'

inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
outputs = model.generate(inputs, max_length=100, temperature=0.2)
print("-"*80)
print(tokenizer.decode(outputs[0]))
```

# Chat Format

The same model works as chat (experimental).

```python
prompt_template = "<empty_output>SYSTEM {system}\n" \
                  "<empty_output>USER {query}\n" \
                  "<empty_output>ASSISTANT"
prompt = prompt_template.format(system="You are a programming assistant",
                                query="How do I sort a list in Python?")
```

# Architecture

As described in more detail in the blog post, we used:

- [ALiBi](https://arxiv.org/abs/2108.12409) based attention
- [LayerNorm](https://arxiv.org/abs/1607.06450v1) instead of [RMSNorm](https://arxiv.org/pdf/1910.07467.pdf)
- [Multi Query Attention](https://arxiv.org/abs/1911.02150)

We also used LiON, flash attention, early dropout. It's not that innovative that you can't run it, in fact you can -- see an example below.


# Pretraining

For the base model, we used our own dataset that contains code with permissive licenses only, and open text datasets.
Filtering is the key to success of this model:

- We only used text in English
- Only topics related to computer science
- Applied heavy deduplication

The text to code proportion was 50:50, model trained for 1.2T tokens. 

We don't release the base model, because its Fill-in-the-Middle (FIM) capability likes to repeat itself too much, so
its practical use is limited. But if you still want it, write us a message on Discord.


# Finetuning

We tested our hypothesis that chat data should boost base model performance in FIM and
regular left-to-right code completion. We found that just 15% of open
[code](https://huggingface.co/datasets/bigcode/commitpackft)
[instruction-following](https://huggingface.co/datasets/rombodawg/2XUNCENSORED_MegaCodeTraining188k) datasets,
that we filtered for quality, improves almost all metrics.

Additionally, to improve FIM, we observed common failure modes, and prepared a synthetic dataset based on
[The Stack dedup v1.1](https://huggingface.co/datasets/bigcode/the-stack-dedup) to address them.

There is a distribution shift between typical code on the internet, and the code you write in your IDE.
The former is likely finished, so the model tries to come up with a suggestion that makes the code complete.
You are likely to have half-written code as you work on it, there is no single addition that can repair it
fully.

In practice, model needs to have a tendency to stop after a couple of lines are added, and sometimes don't write
anything at all. We found that just giving it empty completions, single line completions, multiline
completions that end with a smaller text indent or at least a newline -- makes it much more usable. This data
was used as the rest 85% of the finetune dataset.

The final model is the result of several attempts to make it work as good as possible for code completion,
and to perform well on a wide range of metrics. The best attempt took 40B tokens.


# Limitations and Bias

The Refact-1.6B model was trained on text in English. But it has seen a lot more languages in
code comments. Its performance on non-English languages is lower, for sure.


# Model Stats

- **Architecture:** LLAMA-like model with multi-query attention
- **Objectives** Fill-in-the-Middle, Chat
- **Tokens context:** 4096
- **Pretraining tokens:** 1.2T
- **Finetuning tokens:** 40B
- **Precision:** bfloat16
- **GPUs** 64 NVidia A5000
- **Training time** 28 days


# License

The model is licensed under the BigScience OpenRAIL-M v1 license agreement


# Citation

If you are using this model, please give a link to this page.