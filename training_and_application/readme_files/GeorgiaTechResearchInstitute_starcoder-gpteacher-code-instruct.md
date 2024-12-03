---
license: bigcode-openrail-m
datasets:
- bigcode/the-stack-dedup
- teknium1/GPTeacher-codegen
library_name: transformers
pipeline_tag: text-generation
tags:
- Code-Gen
---
# StarCoder GPTeacher-Codegen Fine-Tuned

<!-- Provide a quick summary of what the model is/does. -->

This model is [`bigcode/starcoder`](https://huggingface.co/bigcode/starcoder) fine-tuned on the [`teknium1/GPTeacher`](https://github.com/teknium1/GPTeacher) codegen dataset (GPT-4 code instruction fine-tuning).

## Model Details

The base StarCoder models are 15.5B parameter models trained on 80+ programming languages from [The Stack (v1.2)](https://huggingface.co/datasets/bigcode/the-stack), with opt-out requests excluded. The model uses [Multi Query Attention](https://arxiv.org/abs/1911.02150), [a context window of 8192 tokens](https://arxiv.org/abs/2205.14135),  and was trained using the [Fill-in-the-Middle objective](https://arxiv.org/abs/2207.14255) on 1 trillion tokens. 

- **Repository:** [bigcode/Megatron-LM](https://github.com/bigcode-project/Megatron-LM)
- **Project Website:** [bigcode-project.org](https://www.bigcode-project.org)
- **Paper:** [💫StarCoder: May the source be with you!](https://drive.google.com/file/d/1cN-b9GnWtHzQRoE7M7gAEyivY0kl4BYs/view)
- **Point of Contact:** [contact@bigcode-project.org](mailto:contact@bigcode-project.org)
- **Languages:** 80+ Programming languages

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
### Intended use

The base model was trained on GitHub code and then fine-tuned to follow instructions. Prompts such as "Write a function that computes the square root." should work reasonably well. The original repo recommeds using the [Tech Assistant prompt](https://huggingface.co/datasets/bigcode/ta-prompt) to few-shot prompt it into behaving as a technical assistant. This fine-tuned model uses the [Alpaca prompts](https://github.com/tatsu-lab/stanford_alpaca/blob/main/train.py).

### Generation
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "GeorgiaTechResearchInstitute/starcoder-gpteacher-code-instruct"
device = "cuda"

input_prompt = ("Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.\n\n"
                "### Instruction:\n"
                "{instruction}\n\n"
                "### Input:\n"
                "{input}\n\n"
                "### Response:")

prompt = "Please explain the following program."
extra_input = "send(to, from, count)
              register short *to, *from;
              register count;
              {
                register n = (count + 7) / 8;
                switch (count % 8) {
                case 0: do { *to = *from++;
                case 7:      *to = *from++;
                case 6:      *to = *from++;
                case 5:      *to = *from++;
                case 4:      *to = *from++;
                case 3:      *to = *from++;
                case 2:      *to = *from++;
                case 1:      *to = *from++;
                  } while (--n > 0);
                }
              }"
prompt = input_prompt.format_map({"instruction": prompt, "input": extra_input})
                  
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint, trust_remote_code=True, torch_dtype=torch.float16).to(device)

inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
```

<details>
  <summary> Example Outputs </summary>
  
*__Full Prompt:__*
```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.
### Instruction:
What does this program do and how does it work?
### Input:
send(to, from, count)
register short *to, *from;
register count;
{
    register n = (count + 7) / 8;
    switch (count % 8) {
        case 0: *to = *from++;
        case 7: *to = *from++;
        case 6: *to = *from++;
        case 5: *to = *from++;
        case 4: *to = *from++;
        case 3: *to = *from++;
        case 2: *to = *from++;
        case 1: *to = *from++;
    }
    while (--n > 0) {
        *to = *from++;
        *to = *from++;
        *to = *from++;
        *to = *from++;
        *to = *from++;
        *to = *from++;
        *to = *from++;
        *to = *from++;
    }
}
### Response:
```

*__Response:__*
```
This program is designed to efficiently copy bytes from one memory location to another. It copies 'count' bytes from the location pointed to by 'from' to the location pointed to by 'to', and works correctly regardless of address alignment. The function 'foo' is a wrapper function that initializes the 'to' and 'from' pointers, checks for proper memory bounds, and performs byte alignment if necessary.

To use this program, you must declare two pointer variables, 'to' and 'from', and then call the 'foo' function with the following parameters:

foo(to, from, count)
```

</details>

### Attribution & Other Requirements

The pretraining dataset of the model was filtered for permissive licenses only. Nevertheless, the model can generate source code verbatim from the dataset. The code's license might require attribution and/or other specific requirements that must be respected. The BigCode project provides a [search index](https://huggingface.co/spaces/bigcode/starcoder-search) that let's you search through the pretraining data to identify where generated code came from and apply the proper attribution to your code.

# Limitations

The model has been trained on source code from 80+ programming languages. The predominant language in source is English although other languages are also present. As such the model is capable of generating code snippets provided some context but the generated code is not guaranteed to work as intended. It can be inefficient, contain bugs or exploits. See [the original paper](https://drive.google.com/file/d/1cN-b9GnWtHzQRoE7M7gAEyivY0kl4BYs/view) for an in-depth discussion of the model limitations.
The fine-tuning process makes the model more responsive to direct user input, however this is an early attempt at instruction fine-tuning starcoder models and the results may not be representative of the model's full potential.

# Training

## Model

- **Architecture:** GPT-2 model with multi-query attention and Fill-in-the-Middle objective
- **Pretraining steps:** 250k
- **Pretraining tokens:** 1 trillion
- **Precision:** bfloat16
- **Fine-Tuning Instruct-Response Pairs:** 4.5k
- **Fine-Tuning Context Length:** 1024
- **Fine-Tuning Epochs:** 3
- **Fine-Tuning LR:** 2e-5
- **Fine-Tuning Optimizations:** FSDP

## Hardware

- **GPUs:** 8 Tesla A100
- **Training time:** 5 hours

# License
The model is licensed under the BigCode OpenRAIL-M v1 license agreement. You can find the full agreement [here](https://huggingface.co/spaces/bigcode/bigcode-model-license-agreement). This model was also fine-tuned using outputs from OpenAI's GPT-4, and as such it is additionally subject to [OpenAI's terms of service.](https://openai.com/policies/terms-of-use)

## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->
The base model HF repo can be found [here.](https://huggingface.co/bigcode/starcoder)
```
@article{li2023starcoder,
      title={StarCoder: may the source be with you!}, 
      author={Raymond Li and Loubna Ben Allal and Yangtian Zi and Niklas Muennighoff and Denis Kocetkov and Chenghao Mou and Marc Marone and Christopher Akiki and Jia Li and Jenny Chim and Qian Liu and Evgenii Zheltonozhskii and Terry Yue Zhuo and Thomas Wang and Olivier Dehaene and Mishig Davaadorj and Joel Lamy-Poirier and João Monteiro and Oleh Shliazhko and Nicolas Gontier and Nicholas Meade and Armel Zebaze and Ming-Ho Yee and Logesh Kumar Umapathi and Jian Zhu and Benjamin Lipkin and Muhtasham Oblokulov and Zhiruo Wang and Rudra Murthy and Jason Stillerman and Siva Sankalp Patel and Dmitry Abulkhanov and Marco Zocca and Manan Dey and Zhihan Zhang and Nour Fahmy and Urvashi Bhattacharyya and Wenhao Yu and Swayam Singh and Sasha Luccioni and Paulo Villegas and Maxim Kunakov and Fedor Zhdanov and Manuel Romero and Tony Lee and Nadav Timor and Jennifer Ding and Claire Schlesinger and Hailey Schoelkopf and Jan Ebert and Tri Dao and Mayank Mishra and Alex Gu and Jennifer Robinson and Carolyn Jane Anderson and Brendan Dolan-Gavitt and Danish Contractor and Siva Reddy and Daniel Fried and Dzmitry Bahdanau and Yacine Jernite and Carlos Muñoz Ferrandis and Sean Hughes and Thomas Wolf and Arjun Guha and Leandro von Werra and Harm de Vries},
      year={2023},
      eprint={2305.06161},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_GeorgiaTechResearchInstitute__starcoder-gpteacher-code-instruct)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 32.57   |
| ARC (25-shot)         | 32.68          |
| HellaSwag (10-shot)   | 47.6    |
| MMLU (5-shot)         | 28.63         |
| TruthfulQA (0-shot)   | 40.41   |
| Winogrande (5-shot)   | 55.56   |
| GSM8K (5-shot)        | 0.0        |
| DROP (3-shot)         | 23.11         |
