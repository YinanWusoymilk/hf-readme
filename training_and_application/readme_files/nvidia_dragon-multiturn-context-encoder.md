---
language:
- en
tag:
- dragon
- retriever
- conversation
- multi-turn
- conversational query
license:
- other
---

## Model Description
We introduce Dragon-multiturn, a retriever specifically designed for the conversational QA scenario. It can handle conversational query which combine dialogue history with the current query. It is built on top of the [Dragon](https://huggingface.co/facebook/dragon-plus-query-encoder) retriever. The details of Dragon-multiturn can be found in [here](https://arxiv.org/pdf/2401.10225). **Please note that Dragon-multiturn is a dual encoder consisting of a query encoder and a context encoder. This repository is only for the context encoder of Dragon-multiturn for getting the context embeddings, and you also need the query encoder to get query embeddings, which can be found [here](https://huggingface.co/nvidia/dragon-multiturn-query-encoder). Both query encoder and context encoder share the same tokenizer.**

## Other Resources
[Llama3-ChatQA-1.5-8B](https://huggingface.co/nvidia/Llama3-ChatQA-1.5-8B) &ensp; [Llama3-ChatQA-1.5-70B](https://huggingface.co/nvidia/Llama3-ChatQA-1.5-70B) &ensp; [Evaluation Data](https://huggingface.co/datasets/nvidia/ChatRAG-Bench) &ensp; [Training Data](https://huggingface.co/datasets/nvidia/ChatQA-Training-Data) &ensp; [Website](https://chatqa-project.github.io/) &ensp; [Paper](https://arxiv.org/pdf/2401.10225)

## Benchmark Results
<style type="text/css">
.tg  {border:none;border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;
  padding:10px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;font-weight:normal;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:center}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:center}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky" rowspan="2"></th>
    <th class="tg-c3ow" colspan="2">Average</th>
    <th class="tg-c3ow" colspan="2">Doc2Dial</th>
    <th class="tg-c3ow" colspan="2">QuAC</th>
    <th class="tg-c3ow" colspan="2">QReCC</th>
    <th class="tg-c3ow" colspan="2">TopiOCQA</th>
    <th class="tg-c3ow" colspan="2">INSCIT</th>
  </tr>
  <tr>
    <th class="tg-c3ow">top-1</th>
    <th class="tg-c3ow">top-5</th>
    <th class="tg-c3ow">top-1</th>
    <th class="tg-c3ow">top-5</th>
    <th class="tg-c3ow">top-1</th>
    <th class="tg-c3ow">top-5</th>
    <th class="tg-c3ow">top-1</th>
    <th class="tg-c3ow">top-5</th>
    <th class="tg-c3ow">top-5*</th>
    <th class="tg-c3ow">top-20*</th>
    <th class="tg-c3ow">top-5*</th>
    <th class="tg-c3ow">top-20*</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Dragon</td>
    <td class="tg-c3ow">46.3</td>
    <td class="tg-c3ow">73.1</td>
    <td class="tg-c3ow">43.3</td>
    <td class="tg-c3ow">75.6</td>
    <td class="tg-c3ow">56.8</td>
    <td class="tg-c3ow">82.9</td>
    <td class="tg-c3ow">46.2</td>
    <td class="tg-c3ow">82.0</td>
    <td class="tg-c3ow">57.7</td>
    <td class="tg-c3ow">78.8</td>
    <td class="tg-c3ow">27.5</td>
    <td class="tg-c3ow">46.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">Dragon-multiturn</td>
    <td class="tg-c3ow">53.0</td>
    <td class="tg-c3ow">81.2</td>
    <td class="tg-c3ow">48.6</td>
    <td class="tg-c3ow">83.5</td>
    <td class="tg-c3ow">54.8</td>
    <td class="tg-c3ow">83.2</td>
    <td class="tg-c3ow">49.6</td>
    <td class="tg-c3ow">86.7</td>
    <td class="tg-c3ow">64.5</td>
    <td class="tg-c3ow">85.2</td>
    <td class="tg-c3ow">47.4</td>
    <td class="tg-c3ow">67.1</td>
  </tr>
</tbody>
</table>
Retrieval results across five multi-turn QA datasets (Doc2Dial, QuAC, QReCC, TopiOCQA, INSCIT) with the average top-1 and top-5 recall scores. *Since the average context length in TopiOCQA and INSCIT is smaller than in other datasets, we report top-5 and top-20 to roughly match the context lengths of top-1 and top-5, respectively, in those datasets.


## How to use
```python
import torch
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained('nvidia/dragon-multiturn-query-encoder')
query_encoder = AutoModel.from_pretrained('nvidia/dragon-multiturn-query-encoder')
context_encoder = AutoModel.from_pretrained('nvidia/dragon-multiturn-context-encoder')

query = [
    {"role": "user", "content": "I need help planning my Social Security benefits for my survivors."},
    {"role": "agent", "content": "Are you currently planning for your future?"},
    {"role": "user", "content": "Yes, I am."}
]
contexts = [
    "Benefits Planner: Survivors | Planning For Your Survivors \nAs you plan for the future , you'll want to think about what your family would need if you should die now. Social Security can help your family if you have earned enough Social Security credits through your work. You can earn up to four credits each year. In 2019 , for example , you earn one credit for each $1,360 of wages or self - employment income. When you have earned $5,440 , you have earned your four credits for the year. The number of credits needed to provide benefits for your survivors depends on your age when you die. No one needs more than 40 credits 10 years of work to be eligible for any Social Security benefit. But , the younger a person is , the fewer credits they must have for family members to receive survivors benefits. Benefits can be paid to your children and your spouse who is caring for the children even if you don't have the required number of credits. They can get benefits if you have credit for one and one - half years of work 6 credits in the three years just before your death.  For Your Widow Or Widower \nThere are about five million widows and widowers receiving monthly Social Security benefits based on their deceased spouse's earnings record.",
    "Benefits Planner: Retirement \nOther Things to Consider \nWhat Is The Best Age To Start Your Benefits? The answer is that there is no one \" best age \" for everyone and, ultimately, it is your choice. You should make an informed decision about when to apply for benefits based on your individual and family circumstances. Your monthly benefit amount can differ substantially based on the age when you start receiving benefits. If you decide to start benefits : before your full retirement age , your benefit will be smaller but you will receive it for a longer period of time. at your full retirement age or later , you will receive a larger monthly benefit for a shorter period of time. The amount you receive when you first get benefits sets the base for the amount you will receive for the rest of your life. You may want to consider the following when you make that decision : If you plan to continue working , there are limits on how much you can earn each year between age 62 and full retirement age and still get all your benefits. Depending on the amount of your benefit and your earnings for the year , you may have to give up some of your benefits."
]

## convert query into a format as follows:
## user: {user}\nagent: {agent}\nuser: {user}
formatted_query = '\n'.join([turn['role'] + ": " + turn['content'] for turn in query]).strip()

## get query and context embeddings
query_input = tokenizer(formatted_query, return_tensors='pt')
ctx_input = tokenizer(contexts, padding=True, truncation=True, max_length=512, return_tensors='pt')
query_emb = query_encoder(**query_input).last_hidden_state[:, 0, :] # (1, emb_dim)
ctx_emb = context_encoder(**ctx_input).last_hidden_state[:, 0, :] # (num_ctx, emb_dim)

## Compute similarity scores using dot product
similarities = query_emb.matmul(ctx_emb.transpose(0, 1)) # (1, num_ctx)

## rank the similarity (from highest to lowest)
ranked_results = torch.argsort(similarities, dim=-1, descending=True) # (1, num_ctx)
```

## Evaluations on Multi-Turn QA Retrieval Benchmark
**(UPDATE!!)** We evaluate multi-turn QA retrieval on five datasets: Doc2Dial, QuAC, QReCC, TopiOCQA, and INSCIT, which can be found in the [ChatRAG Bench](https://huggingface.co/datasets/nvidia/ChatRAG-Bench). The evaluation scripts can be found [here](https://huggingface.co/nvidia/dragon-multiturn-query-encoder/tree/main/evaluation).


## License
Dragon-multiturn is built on top of [Dragon](https://arxiv.org/abs/2302.07452). We refer users to the original license of the Dragon model. Dragon-multiturn is also subject to the [Terms of Use](https://openai.com/policies/terms-of-use).

## Correspondence to
Zihan Liu (zihanl@nvidia.com), Wei Ping (wping@nvidia.com)

## Citation
<pre>
@article{liu2024chatqa,
  title={ChatQA: Surpassing GPT-4 on Conversational QA and RAG},
  author={Liu, Zihan and Ping, Wei and Roy, Rajarshi and Xu, Peng and Lee, Chankyu and Shoeybi, Mohammad and Catanzaro, Bryan},
  journal={arXiv preprint arXiv:2401.10225},
  year={2024}}
</pre>
