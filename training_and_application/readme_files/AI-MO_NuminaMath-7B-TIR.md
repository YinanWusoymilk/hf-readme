---
base_model: deepseek-ai/deepseek-math-7b-base
tags:
- alignment-handbook
- generated_from_trainer
widget:
  - example_title: Math problem
    messages:
      - role: user
        content: >-
          For how many values of the constant $k$ will the polynomial
          $x^{2}+kx+36$ have two distinct integer roots?
    output:
      text: >-
        ### Solution: 
        
        1- For the polynomial \\( x^2 + kx + 36 \\) to have two
        distinct integer roots, let's denote these roots by \\( r_1 \\) and \\(
        r_2 \\).



        2- According to Vieta's formulas, the sum of the roots \\( r_1 + r_2 \\)
        is equal to \\(-k\\), and the product of the roots \\( r_1 \\cdot r_2
        \\) is equal to 36.



        3- To find the distinct integer pairs \\((r_1, r_2)\\) whose product is
        36, we need to determine all pairs of integers \\((r_1, r_2)\\) such
        that \\( r_1 \\cdot r_2 = 36 \\) and \\( r_1 \\neq r_2 \\).



        4- From the equation \\( r_1 + r_2 = -k \\), for each valid pair
        \\((r_1, r_2)\\), we can compute the corresponding value of \\( k \\).



        5- Finally, since we need the polynomial to have two distinct integer
        roots, we need to ensure that \\( r_1 \\) and \\( r_2 \\) are distinct.

        Let's start by finding all pairs \\((r_1, r_2)\\) such that \\( r_1
        \\cdot r_2 = 36 \\). We'll then determine the values of \\( k \\) and
        ensure the roots are distinct.

        ```python import itertools

        # Find all pairs (r1, r2) such that r1 * r2 = 36 product_36 = 36
        factor_pairs = []

        for i in range(1, product_36 + 1):
          if product_36 % i == 0:
            pair = (i, product_36 // i)
            if pair[0] != pair[1]: # Ensure distinct pairs
              factor_pairs.append(pair)
            
            # Calculate k for each pair and ensure distinct integer roots
            valid_k_values = set()
            for r1, r2 in factor_pairs:
              if r1 != r2:
                k = -(r1 + r2)
                valid_k_values.add(k)
                
            print((len(valid_k_values), sorted(valid_k_values)))
         ```
         
         ```output
         (4, [-37, -20, -15,-13])
         ```
         The distinct integer values of \\( k \\) that make the
        polynomial \\( x^2 + kx + 36 \\) have two distinct integer roots are
        \\(-37, -20, -15, \\text{and} -13\\).

        Therefore, the number of such values of \\( k \\) is:

        [ \\boxed{4} \\]

pipeline_tag: text-generation
model-index:
- name: NuminaMath-7B-TIR
  results: []
license: apache-2.0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

<img src="https://huggingface.co/AI-MO/NuminaMath-7B-TIR/resolve/main/thumbnail.png" alt="Numina Logo" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


# Model Card for NuminaMath 7B TIR

NuminaMath is a series of language models that are trained to solve math problems using tool-integrated reasoning (TIR). NuminaMath 7B TIR won the first progress prize of the [AI Math Olympiad (AIMO)](https://aimoprize.com), with a score of 29/50 on the public and private tests sets. 

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6200d0a443eb0913fa2df7cc/NyhBs_gzg40iwL995DO9L.png)

This model is a fine-tuned version of [deepseek-ai/deepseek-math-7b-base](https://huggingface.co/deepseek-ai/deepseek-math-7b-base) with two stages of supervised fine-tuning:

* **Stage 1:** fine-tune the base model on a large, diverse dataset of natural language math problems and solutions, where each solution is templated with Chain of Thought (CoT) to facilitate reasoning. 
* **Stage 2:** fine-tune the model from Stage 1 on a synthetic dataset of tool-integrated reasoning, where each math problem is decomposed into a sequence of rationales, Python programs, and their outputs. Here we followed [Microsoft’s ToRA paper](https://arxiv.org/abs/2309.17452) and prompted GPT-4 to produce solutions in the ToRA format with code execution feedback. Fine-tuning on this data produces a reasoning agent that can solve mathematical problems via a mix of natural language reasoning and use of the Python REPL to compute intermediate results.



## Model description

- **Model type:** A 7B parameter math LLM fine-tuned in two stages of supervised fine-tuning, first on a dataset with math problem-solution pairs and then on a synthetic dataset with examples of multi-step generations using tool-integrated reasoning.
- **Language(s) (NLP):** Primarily English
- **License:** Apache 2.0
- **Finetuned from model:** [deepseek-ai/deepseek-math-7b-base](https://huggingface.co/deepseek-ai/deepseek-math-7b-base)

## Model performance

| | | NuminaMath-7B-CoT | NuminaMath-7B-TIR | Qwen2-7B-Instruct | Llama3-8B-Instruct | DeepSeekMath-7B-Instruct | DeepSeekMath-7B-RL | DART-Math-7B-CoT |
| --- | --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **GSM8k** | 0-shot | 76.3% | 84.6% | 82.3% | 79.6% | 82.8% | **88.2%** | 86.6% |
| Grade school math | 
| **MATH** | 0-shot | 55.8% | **68.1%** | 49.6% | 30.0% | 46.8% | 51.7% | 53.6% |
| Math problem-solving |
| **AMC 2023** | 0-shot | 11/40 | **20/40** | 10/40 | 2/40 | 7/40 | 9/40 | 11/40 |
| Competition-level math | maj@64 | 18/40 | **31/40** | 13/40 | 9/40 | 13/40 | 14/40 | 16/40 |
| **AIME 2024** | 0-shot | 0/30 | **5/30** | 1/30 | 0/30 | 1/30 | 1/30 | 1/30 |
| Competition-level math | maj@64 | 1/30 | **10/30** | 4/30 | 2/30 | 1/30 | 1/30 | 1/30 |

*Table: Comparison of various 7B and 8B parameter language models on different math benchmarks. All scores except those for NuminaMath-7B-TIR are reported without tool-integrated reasoning.*

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** Coming soon!
- **Demo:** https://huggingface.co/spaces/AI-MO/math-olympiad-solver

## Intended uses & limitations

Here's how you can run the model using the `pipeline()` function from 🤗 Transformers:

```python
import re
import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="AI-MO/NuminaMath-7B-TIR", torch_dtype=torch.bfloat16, device_map="auto")

messages = [
    {"role": "user", "content": "For how many values of the constant $k$ will the polynomial $x^{2}+kx+36$ have two distinct integer roots?"},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

gen_config = {
    "max_new_tokens": 1024,
    "do_sample": False,
    "stop_strings": ["```output"], # Generate until Python code block is complete
    "tokenizer": pipe.tokenizer,
}

outputs = pipe(prompt, **gen_config)
text = outputs[0]["generated_text"]
print(text)

# WARNING: This code will execute the python code in the string. We show this for eductional purposes only.
# Please refer to our full pipeline for a safer way to execute code.
python_code = re.findall(r"```python(.*?)```", text, re.DOTALL)[0]
exec(python_code)
```

The above executes a single step of Python code - for more complex problems, you will want to run the logic for several steps to obtain the final solution.  

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

NuminaMath 7B TIR was created to solve problems in the narrow domain of competition-level mathematics. As a result, the model should not be used for general chat applications. With greedy decoding, we find the model is capable of solving problems at the level of [AMC 12](https://artofproblemsolving.com/wiki/index.php/2023_AMC_12A_Problems), but often struggles generate a valid solution on harder problems at the AIME and Math Olympiad level. The model also struggles to solve geometry problems, likely due to it's limited capacity and lack of other modalities like vision. 


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 32
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 4.0


### Framework versions

- Transformers 4.40.1
- Pytorch 2.3.1
- Datasets 2.18.0
- Tokenizers 0.19.1

## Citation

If you find NuminaMath 7B TIR is useful in your work, please cite it with:

```
@misc{numina_math_7b,
  author = {Edward Beeching and Shengyi Costa Huang and Albert Jiang and Jia Li and Benjamin Lipkin and Zihan Qina and Kashif Rasul and Ziju Shen and Roman Soletskyi and Lewis Tunstall},
  title = {NuminaMath 7B TIR},
  year = {2024},
  publisher = {Numina & Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\url{https://huggingface.co/AI-MO/NuminaMath-7B-TIR}}
}
```