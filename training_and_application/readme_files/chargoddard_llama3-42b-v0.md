---
license: llama3
datasets:
- JeanKaddour/minipile
language:
- en
tags:
- axolotl
- mergekit
- llama
---
> 🚨 THIS IS A BASE MODEL 🚨
> 
> This model is pruned from the base Llama 3 70B, which has no instruction tuning and randomly initialized special tokens.
> 
> Using this with the Llama 3 instruction format is injecting random noise into latent space and will give you deranged results. (It's pretty funny actually.)
> Treat this as the untrained foundation model this is and use appropriate prompts.


Meta's Llama 3 70B pruned to 42B parameters using the methodology described in [The Unreasonable Ineffectiveness of the Deeper Layers](https://arxiv.org/abs/2403.17887). Post-pruning trained using QLoRA for ~100M tokens from [JeanKaddour/minipile](https://huggingface.co/datasets/JeanKaddour/minipile).

Layers to prune selected using [PruneMe](https://github.com/arcee-ai/PruneMe).

Still evaluating, don't get too excited! Might be incredibly dumb. Check out these numbers though:

|      Groups      |Version|Filter|n-shot|Metric|Value |   |Stderr|
|------------------|-------|------|-----:|------|-----:|---|-----:|
|mmlu              |N/A    |none  |     0|acc   |0.7669|±  |0.0034|
| - humanities     |N/A    |none  |     5|acc   |0.7296|±  |0.0062|
| - other          |N/A    |none  |     5|acc   |0.8101|±  |0.0067|
| - social_sciences|N/A    |none  |     5|acc   |0.8668|±  |0.0060|
| - stem           |N/A    |none  |     5|acc   |0.6825|±  |0.0079|
|winogrande|      1|none  |     5|acc   |0.8027|±  |0.0112|
|hellaswag|      1|none  |    10|acc_norm|0.8025|±  |0.0040|


[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)