---
language: 
- en
thumbnail:
tags:
- convAI
- conversational
- facebook
license: apache-2.0
datasets:
- blended_skill_talk
metrics:
- perplexity
---

## Model description

+ Paper: [Recipes for building an open-domain chatbot]( https://arxiv.org/abs/2004.13637)
+ [Original PARLAI Code](https://parl.ai/projects/recipes/)


### Abstract


Building open-domain chatbots is a challenging area for machine learning research. While prior work has shown that scaling neural models in the number of parameters and the size of the data they are trained on gives improved results, we show that other ingredients are important for a high-performing chatbot. Good conversation requires a number of skills that an expert conversationalist blends in a seamless way: providing engaging talking points and listening to their partners, both asking and answering questions, and displaying knowledge, empathy and personality appropriately, depending on the situation. We show that large scale models can learn these skills when given appropriate training data and choice of generation strategy. We build variants of these recipes with 90M, 2.7B and 9.4B parameter neural models, and make our models and code publicly available. Human evaluations show our best models are superior to existing approaches in multi-turn dialogue in terms of engagingness and humanness measurements. We then discuss the limitations of this work by analyzing failure cases of our models.
