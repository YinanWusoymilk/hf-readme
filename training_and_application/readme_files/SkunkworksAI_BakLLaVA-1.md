---
datasets:
- SkunkworksAI/BakLLaVA-1-FT
language:
- en
license: apache-2.0
---

<p><h1> BakLLaVA-1 </h1></p>

Thank you to our compute sponsors Together Compute (www.together.ai).
In collaboration with **Ontocord** (www.ontocord.ai) and **LAION** (www.laion.ai).


![image/png](https://cdn-uploads.huggingface.co/production/uploads/64b7e345f92b20f7a38bf47a/V5lpOHWGGYJ2yPpEo_8i1.png)

BakLLaVA 1 is a Mistral 7B base augmented with the LLaVA 1.5 architecture. In this first version, we showcase that a Mistral 7B base outperforms Llama 2 13B on several benchmarks. 
You can run BakLLaVA-1 on our repo. We are currently updating it to make it easier for you to finetune and inference. (https://github.com/SkunkworksAI/BakLLaVA).


Note: BakLLaVA-1 is fully open-source but was trained on certain data that includes LLaVA's corpus which is not commercially permissive. We will fix this in the upcoming release.


BakLLaVA 2 is cooking with a significantly larger (commercially viable) dataset and a novel architecture that expands beyond the current LLaVA method. BakLLaVA-2 will do away with the restrictions of BakLLaVA-1.


# Evaluations


![image/png](https://cdn-uploads.huggingface.co/production/uploads/64b7e345f92b20f7a38bf47a/qdYubrBmF7ztAHgdfkkwG.png)

# Training dataset

- 558K filtered image-text pairs from LAION/CC/SBU, captioned by BLIP.
- 158K GPT-generated multimodal instruction-following data.
- 450K academic-task-oriented VQA data mixture.
- 40K ShareGPT data.
- Additional private data (permissive)



