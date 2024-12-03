---
license: apache-2.0
datasets:
- snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset
pipeline_tag: text-generation
---

Read our release blog here: [Snorkel AI Blog](https://snorkel.ai/new-benchmark-results-demonstrate-value-of-snorkel-ai-approach-to-llm-alignment/)

You can try our models on the [Together AI](https://api.together.xyz/playground/chat/snorkelai/Snorkel-Mistral-PairRM-DPO) playground: https://api.together.xyz/playground/chat/snorkelai/Snorkel-Mistral-PairRM-DPO.
This model is optimized for chat purposes. Have fun!


Our model is also available through [Together AI API](https://www.together.ai/solutions#what-we-offer) with the following model API string: `snorkelai/Snorkel-Mistral-PairRM-DPO`.
Special thanks to the [Together AI](https://www.together.ai/) team for adding our model to their endpoints.

We also provide an HF inference endpoint for everyone to test the model.
It may initially take a few minutes to activate, but will eventually operate at the standard speed of HF's 7B model text inference endpoint.
The speed of inference depends on HF endpoint performance and is not related to Snorkel offerings.
This endpoint is designed for initial trials, not for ongoing production use.

```
import requests

API_URL = "https://t1q6ks6fusyg1qq7.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
	"Accept" : "application/json",
	"Content-Type": "application/json" 
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
	"inputs": "[INST] Recommend me some Hollywood movies [/INST]",
	"parameters": {}
})
```

### Dataset:
Training dataset: [snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset](https://huggingface.co/datasets/snorkelai/Snorkel-Mistral-PairRM-DPO-Dataset)

We utilize ONLY the prompts from [UltraFeedback](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized); **no external LLM responses used**.

### Methodology:
  1. Generate five response variations for each prompt from a subset of 20,000 using the LLM - to start, we used [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2).
  2. Apply [PairRM](https://huggingface.co/llm-blender/PairRM) for response reranking.
  3. Update the LLM by applying Direct Preference Optimization (DPO) on the top (chosen) and bottom (rejected) responses.
  4. Use this LLM as the base model for the next iteration, repeating three times in total.
 
This overview provides a high-level summary of our approach. 
We plan to release more detailed results and findings in the coming weeks on the [Snorkel blog.](https://snorkel.ai/blog/)

The prompt format follows the Mistral model:

```[INST] {prompt} [/INST]```

### Training recipe:
- The provided data is formatted to be compatible with the Hugging Face's [Zephyr recipe](https://github.com/huggingface/alignment-handbook/tree/main/recipes/zephyr-7b-beta).
We executed the n_th DPO iteration using the "train/test_iteration_{n}".

### Key Premises:
- **Specialization Requirement**: For most enterprise use cases, using LLMs "off-the-shelf" falls short of production quality, necessitating additional fine-tuning and alignment.
- **Ease of Model Building**: Creating ranking/scoring/classification models is simpler than developing high-quality, manually annotated datasets for long-form responses.
- **Alignment Recipe**: Using smaller but specialized teacher models (reward models) can incrementally align LLMs towards specific axes.

### Applications:
Unlike our customers, who have very specific use cases to align LLMs to,
the AlpacaEval 2.0 leaderboard measures the ability of LLMS to follow user instructions.
With this demonstration, we focus on the general approach to alignment. 
Thus, we use a general-purpose reward model - the performant [PairRM model](https://huggingface.co/llm-blender/PairRM).
We use the [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) model as our base LLM.

For interest in building your **specialized internal reward models
that reflect your enterprises' needs**, please contact the Snorkel AI team or consider attending our
[**Enterprise LLM Summit: Building GenAI with Your Data on January 25, 2024**](https://snorkel.ai/event/enterprise-llm-summit/)
to learn more about "Programmatically scaling human preferences and alignment in GenAI".

### Result:
On [**Alpaca-Eval 2.0**](https://tatsu-lab.github.io/alpaca_eval/):
- The base model: [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) scored **14.72**.

After applying the above methodology:
- This model scored **30.22** - ranked 3rd and the highest for an open-source base model at the time of publication.
- When post-processing the model outputs with PairRM-best-of-16, which involved generating 16 responses and selecting the highest-scoring response by PairRM, we scored **34.86** - ranked 2nd.
The best model on the leaderboard is "gpt-4-turbo", which is also the judge of optimal responses.

We recognize that the Alpaca-Eval 2.0 benchmark does not entirely capture the full range of capabilities and performances of LLMs.
However, in our current work, where the goal is to align with general "human preferences," Alpaca-Eval 2.0 serves as a suitable and representative benchmark.
Moving forward, we anticipate further contributions from the community regarding new alignment axes, and conduct evaluations using other appropriate benchmarks.

The Alpaca-Eval 2.0 evaluator, "gpt-4-turbo," exhibits a bias towards longer responses. 
This tendency might also be present in our chosen reward model, resulting in our model producing lengthier responses after DPO iterations,
which can be among the factors to our higher ranks on the leaderboard.
Future work could include measures to control response length and other relevant metrics.

### Limitations:
The model is a quick demonstration that the LLMs can be programmatically aligned using smaller specialized reward models. 
It does not have any moderation mechanisms. 
We look forward to continuing to engage with the research community and our customers exploring optimal methods for getting models to respect guardrails, 
allowing for deployment in environments requiring moderated outputs.

### Contemporary Work and Acknowledgements:
- The Mistral AI Team for developing and releasing the advanced Mistral-7B-Instruct-v0.2 model.
- The author of the [Direct Preference Optimization paper](https://arxiv.org/abs/2305.18290) for the innovative approach
- The author of the [Pairwise Reward Model for LLMs paper](https://arxiv.org/abs/2306.02561) for the powerful general-purpose reward model
- The HuggingFace team for the DPO implementation under [The Alignment Handbook](https://github.com/huggingface/alignment-handbook)
- We would also like to acknowledge contemporary work published independently on arXiv on 2024-01-18 by Meta & NYU (Yuan, et al) in a paper called [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020), 
which proposes a similar general approach for creating alignment pairs from a larger set of candidate responses, but using the LLM as the reward model.
While this may work for general-purpose models, our experience has shown that task-specific reward models guided by SMEs are necessary for most 
enterprise applications of LLMs for specific use cases, which is why we focus on the use of external reward models.
- Also, we would like to acknowledge another concurrent work that has a similar approach but focuses more on the theoretical aspect of the iterative DPO process: [Iterative Preference Learning from Human Feedback: Bridging Theory and
Practice for RLHF under KL-Constraint](https://arxiv.org/pdf/2312.11456.pdf) on 2024-01-28 (Xiong, et al).

### GGUF version
Snorkel-Mistral-PairRM-DPO GGUF model version: from [andrew-cartwheel](https://huggingface.co/andrew-cartwheel/snorkel-mistral-pairRM-DPO-q8_0.gguf) or [brittlewis12](https://huggingface.co/brittlewis12/Snorkel-Mistral-PairRM-DPO-GGUF).
ExllamaV2 quants model version: from [bartowski](https://huggingface.co/bartowski/Snorkel-Mistral-PairRM-DPO-exl2). 
Thanks to the mentioned community members for providing the GGUF model versions.

### The Snorkel AI Team
Hoang Tran, Chris Glaze, Braden Hancock

If you found this work useful, feel free to cite [our work](https://huggingface.co/snorkelai/Snorkel-Mistral-PairRM-DPO/):
```
@techreport{viethoangtranduong,
  author = {Tran, Hoang and Glaze, Chris, and Hancock, Braden},
  title = {Iterative DPO Alignment},
  institution = {Snorkel AI},
  year = {2023},
}
```