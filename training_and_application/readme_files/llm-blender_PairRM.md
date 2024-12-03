---
license: mit
datasets:
- openai/summarize_from_feedback
- openai/webgpt_comparisons
- Dahoas/synthetic-instruct-gptj-pairwise
- Anthropic/hh-rlhf
- lmsys/chatbot_arena_conversations
- openbmb/UltraFeedback
metrics:
- accuracy
tags:
- reward_model
- reward-model
- RLHF
- evaluation
- llm
- instruction
- reranking
language:
- en
pipeline_tag: text-generation
---

# Pairwise Reward Model for LLMs (PairRM) from LLM-Blender 


- Github: [https://github.com/yuchenlin/LLM-Blender](https://github.com/yuchenlin/LLM-Blender)
- Paper: [https://arxiv.org/abs/2306.02561](https://arxiv.org/abs/2306.02561)
- Space Demo: [https://huggingface.co/spaces/llm-blender/LLM-Blender](https://huggingface.co/spaces/llm-blender/LLM-Blender)


## News

- Check out our results on AlpacaEval leaderboard: [Twitter](https://x.com/billyuchenlin/status/1732198787354067380?s=20) [Leaderboard](https://tatsu-lab.github.io/alpaca_eval/) 

## Introduction 

Pairwise Reward Model (PairRM) takes an instruction and a **pair** of output candidates as the input, 
and output a score for each candidate to measure their **relative** quality. 
PairRM can be used to (re-)rank a list of candidate outputs and thus can be used an LLM evaluator to efficiently assess the quality of LLMs in local environment.
PairRM can also be used to enhance the decoding by `best-of-n sampling` (i.e., reranking N sampled outputs). 
Apart from that, one can also use PairRM to further align instruction-tuned LLMs with RLHF methods. 

Unlike the other RMs that encode and score each candidate respectively, 
PairRM takes a pair of candidates and compares them side-by-side to indentify the subtle differences between them.
Also, PairRM is based on [`microsoft/deberta-v3-large`](https://huggingface.co/microsoft/deberta-v3-large), and thus it is super efficient: **0.4B**.
We trained PairRM on a diverse collection of six human-preference datasets (see more [here](https://huggingface.co/llm-blender/PairRM#training-datasets)).

PairRM is part of the LLM-Blender project (ACL 2023). Please see our [paper](https://arxiv.org/abs/2306.02561) above to know more.


## Installation

- First install `llm-blender`
```bash
pip install git+https://github.com/yuchenlin/LLM-Blender.git
```

- Then load PairRM:
```python
import llm_blender
blender = llm_blender.Blender()
blender.loadranker("llm-blender/PairRM") # load PairRM
```


## Usage 

### Use Case 1: Comparing/Ranking output candidates given an instruction

- Ranking a list candidate responses

```python
inputs = ["hello, how are you!", "I love you!"]
candidates_texts = [["get out!", "hi! I am fine, thanks!", "bye!"], 
                    ["I love you too!", "I hate you!", "Thanks! You're a good guy!"]]
ranks = blender.rank(inputs, candidates_texts, return_scores=False, batch_size=1)
# ranks is a list of ranks
# ranks[i][j] represents the ranks of candidate-j for input-i
"""
ranks -->
array([[3, 1, 2], # it means "hi! I am fine, thanks!" ranks the 1st, "bye" ranks the 2nd, and "get out!" ranks the 3rd. 
       [1, 3, 2]], # it means "I love you too"! ranks the the 1st, and "I hate you!" ranks the 3rd.
       dtype=int32) 

"""
```

- Directly comparing two candidate responses
```python
inputs = ["hello!", "I love you!"]
candidates_A = ["hi!", "I hate you!"]
candidates_B = ["f**k off!", "I love you, too!"]
comparison_results = blender.compare(inputs, candidates_A, candidates_B)
# comparison_results is a list of bool, where comparison_results[i] denotes
       # whether candidates_A[i] is better than candidates_B[i] for inputs[i]
# Example: comparison_results[0]--> True 
```

<details><summary> Comparing two multi-turn conversations. </summary>

```python
conv1 = [
    {
        "content": "hello",
        "role": "USER"
    },
    {
        "content": "[assistant1‘s response 1]",
        "role": "ASSISTANT"
    },
    ...
]
conv2 = [
    {
        "content": "hello",
        "role": "USER"
    },
    {
        "content": "[assistant2's response 1]",
        "role": "ASSISTANT"
    },
    ...
]
comparison_results = blender.compare_conversations([conv1], [conv2])
# comparison_results is a list of bool, where each element denotes whether all the responses in conv1 together is better than that of conv2
```
</details>

          
### Use Case 2: Best-of-n Sampling (Decoding Enhancment)

**Best-of-n Sampling**, aka, rejection sampling, is a strategy to enhance the response quality by selecting the one that was ranked highest by the reward model 
(see more in [OpenAI WebGPT section 3.2](https://arxiv.org/pdf/2112.09332.pdf) and [OpenAI Blog](https://openai.com/research/measuring-goodharts-law)). 
Best-of-n sampling with PairRM is a very easy way to imporve your LLMs with only a few changes of your inference code: 

```python
# loading models 
import llm_blender
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta")
model = AutoModelForCausalLM.from_pretrained("HuggingFaceH4/zephyr-7b-beta", device_map="auto")
system_message = {"role": "system", "content": "You are a friendly chatbot."}

# formatting your inputs 
inputs = ["can you tell me a joke about OpenAI?"]
messages = [[system_message, {"role": "user", "content": _input}] for _input in inputs]
prompts = [tokenizer.apply_chat_template(m, tokenize=False, add_generation_prompt=True) for m in messages]

# Conventional generation method 
input_ids = tokenizer(prompts[0], return_tensors="pt").input_ids
sampled_outputs = model.generate(input_ids, do_sample=True, top_k=50, top_p=0.95, num_return_sequences=1)
print(tokenizer.decode(sampled_outputs[0][len(input_ids[0]):], skip_special_tokens=False))
# --> The output could be a bad case such as a very short one, e.g., `Sure` 

# PairRM for best-of-n sampling 
blender = llm_blender.Blender()
blender.loadranker("llm-blender/PairRM") # load ranker checkpoint
outputs = blender.best_of_n_generate(model, tokenizer, prompts, n=10)

print("### Prompt:\n", prompts[0])
print("### best-of-n generations:\n", outputs[0])
# --> The output will be much more stable and consistently better than single sampling, for example: 
""" 
Sure, here's a joke about OpenAI:

Why did OpenAI decide to hire a mime as their new AI researcher?

Because they wanted someone who could communicate complex ideas without making a sound!

(Note: This is a joke, not a reflection of OpenAI's actual hiring practices.)
"""
```

### Use case 3: RLHF 
PairRM has been trained on various high-quality and large-scale datasets with human preference annotations 
and shown great correlation with human preferences with an extremely small model size (0.4B), 
approching the performance of GPT-4. 
PairRM will better help the future alignment of LLMs in a more efficient and effective way.
With a `blender.compare()` function, you can apply PairRM to popular RLHF toolkits such as [trl](https://huggingface.co/docs/trl/index). 

**🔥 Check more details on our example jupyter notebook usage: [`blender_usage.ipynb`](https://github.com/yuchenlin/LLM-Blender/blob/main/blender_usage.ipynb)**


Learn more in our LLM-Blender Github [README.md](https://github.com/yuchenlin/LLM-Blender#rank-and-fusion)




## Statistics

### Context length
|  PairRanker type  | Source max length | Candidate max length | Total max length |
|:-----------------:|:-----------------:|----------------------|------------------|
| [pair-ranker](https://huggingface.co/llm-blender/pair-ranker)  (our previous version)             | 128               | 128                  | 384              |
| [PairRM](https://huggingface.co/llm-blender/pair-reward-model/) (This model) | 1224              | 412                  | 2048             |

### Training Datasets
- [openai/summarize_from_feedback](https://huggingface.co/datasets/openai/summarize_from_feedback)
- [openai/webgpt_comparisons](https://huggingface.co/datasets/openai/webgpt_comparisons)
- [Dahoas/synthetic-instruct-gptj-pairwise](https://huggingface.co/datasets/Dahoas/synthetic-instruct-gptj-pairwise)
- [Anthropic/hh-rlhf](https://huggingface.co/datasets/Anthropic/hh-rlhf)
- [lmsys/chatbot_arena_conversations](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations)
- [openbmb/UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback)

### Performance
PairRM has been trained on various high-quality and large-scale dataset with human preference annotations and exhibits great correlation with human preferences 
with an extremly small model size (0.4B), approching the performance of GPT-4.

We test the pairwise comparison on 
- [Auto-J pairwise testdata](https://github.com/GAIR-NLP/auto-j#pairwise-response-comparison)
- [HHH-alignment](https://huggingface.co/datasets/HuggingFaceH4/hhh_alignment)
- [MT-bench-human-judgements](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments)

All following results are reported as pairwise comparison accuracies (agreements).

#### Auto-J Pairwise test data performance

|         Model         |    Summ   |    Exam   |    Code   | Rewriting |   Crea W  |   Func W  |  Comm |    NLP   |  Overall  |
|:---------------------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:-----:|:--------:|:---------:|
| Closed -source Models |
|        ChatGPT        |    33.3   |    40.3   |    36.6   |    31.6   |    48.2   |    40.4   |  47.6 |   45.8   |    42.7   |
|       Claude -2       |    30.6   |    36.1   |    41.7   |    34.2   |    48.1   |    42.5   |  40.6 |   48.5   |    42.4   |
|         GPT -4        |    59.7   |    51.4   |    69.2   |    58.3   |    66.7   |    60.4   |  58.3 |   65.2   |    61.9   |
|  Open -source Models  |
|        SteamSHP       |    33.3   |    29.2   |    26.7   |    33.3   |    40.7   |    31.3   |  51.4 |   51.9   |    40.6   |
|        PandaLM        |    29.2   |    33.3   |    31.7   |    23.3   |    43.5   |    32.9   |  44.8 |   48.9   |    38.9   |
|   LLaMA -2-Chat -13B  |    20.8   |    27.8   |    19.2   |     20    |    31.5   |    27.5   |  35.8 |   31.8   |     29    |
|    Vicuna -13B-v1.5   |    30.6   |    23.6   |     35    |    28.3   |    36.1   |    37.5   |  45.5 |   39.8   |    37.3   |
|   WizardLM -13B-v1.2  |    22.2   |    20.8   |    32.5   |    19.2   |    28.7   |    25.4   |  29.2 |    33    |    27.8   |
|   LLAMA -2-chat -70B  |    34.7   |    33.3   |    36.7   |    35.8   |    51.4   |    54.2   |  47.2 |   47.7   |    45.9   |
|       AUTO -J (13b)       |    45.8   |    38.9   |  **59.2** |    47.5   |    54.6   |    57.1   |  **58**  |   57.6    |    54.8   |
|       UltraRM (13b)       |    56.94  |    43.06  |    55.0   |    53.33  | **67.13** | **64.17** |   56.25  |   59.85   |    **59.85**   |
|         **PairRM (0.4b)**       | **56.94** | **52.78** | 58.33 | **55.83** |   61.57   | 59.17 | 57.64 | **62.5** | 59.05 |

#### HHH-Alignment and MT-bench human judgements

|        Evaluator LM       | HHH ALIGNMENT |           |           |          |             | MT BENCH HUMAN JUDG . |
|:-------------------------:|:-------------:|:---------:|:---------:|:--------:|:-----------:|:---------------------:|
|                           |     Help .    |   Harm .  |   Hon .   |   Other  | Total Avg . |    Human Preference   |
|           RANDOM          |       50      |     50    |     50    |    50    |      50     |         34.26         |
|  STANFORDNLP REWARD MODEL |     69.49     |   60.34   |   52.46   |   51.16  |    58.82    |         44.79         |
|    ALMOST REWARD MODEL    |     74.58     |   67.24   |   78.69   |   86.05  |    76.02    |          49.9         |
|      LLAMA2 -CHAT 7B      |      66.1     |   81.03   |   70.49   |   74.42  |    72.85    |         51.78         |
|      LLAMA2 -CHAT 13B     |     74.58     |   87.93   |   55.74   |   79.07  |    73.76    |         52.34         |
|      LLAMA2 -CHAT 70B     |      66.1     |   **89.66**   |   67.21   |   74.42  |    74.21    |         53.67         |
| LLAMA2 -CHAT 13B+COARSE . |     68.74     |   68.97   |   65.57   |   67.44  |    67.42    |         46.89         |
|    GPT -3.5-TURBO -0613   |     76.27     |   87.93   |   67.21   |   86.05  |    78.73    |         57.12         |
|       PROMETHEUS 7B       |     69.49     |   84.48   |   78.69   |   90.7   |    80.09    |         55.14         |
|       PROMETHEUS 13B      |     81.36     |   82.76   |   75.41   |   76.74  |    79.19    |         57.72         |
|           UltraRM (13B)   |   **86.44**   |   79.31   | **81.97** |   88.37  |    83.71    |           56          |
|   **PairRM (0.4B)**       |     84.75     |   84.48   |   80.33   | **90.7** |  **84.62**  |         **59**        |
|        GPT -4-0613        |     91.53     |    93.1   |   85.25   |   83.72  |    88.69    |         63.87         |

**While PairRM is a extremely small model (0.4B) based on deberta, the pairwise comparison aggrement performance approches GPT-4's performance!**

Two reasons to attribute:
- Our PairRM specically designed model arch for pairwise comparison through bidirectional attention (See LLM-blender paper for more details)
- The high-quality and large-scale human preference annotation data it was train on (see training dataset list on this hugging face page)






## Citation & Credits 
If you are using PairRM in your research, please cite LLM-blender.
```bibtex
@inproceedings{llm-blender-2023,
    title = "LLM-Blender: Ensembling Large Language Models with Pairwise Comparison and Generative Fusion",
    author = "Jiang, Dongfu and Ren, Xiang and Lin, Bill Yuchen",
    booktitle = "Proceedings of the 61th Annual Meeting of the Association for Computational Linguistics (ACL 2023)",
    year = "2023"
}

```


