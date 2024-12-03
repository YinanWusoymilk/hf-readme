---
license: llama3
license_name: llama3
license_link: LICENSE
library_name: transformers
---
# Llama-3-70B-Instruct-abliterated Model Card

This is meta-llama/Llama-3-70B-Instruct with orthogonalized bfloat16 safetensor weights, generated with the methodology that was described in the preview paper/blog post: '[Refusal in LLMs is mediated by a single direction](https://www.alignmentforum.org/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction)' which I encourage you to read to understand more.

TL;DR: this model has had certain weights manipulated to "inhibit" the model's ability to express refusal. It is not in anyway _guaranteed_ that it won't refuse you, understand your request, it may still lecture you about ethics/safety, etc. It is tuned in all other respects the same as the original 70B instruct model was, just with the strongest refusal direction orthogonalized out.

## Quants
[GGUF Quants available here](https://huggingface.co/failspy/llama-3-70B-Instruct-abliterated-GGUF)

## For the people who like tinkering or looking to save bandwidth
In the repo, I've included `refusal_dir.pth`
If you have Llama-3-70B-Instruct model downloaded already, you can use the ortho cookbook to apply it to your downloaded model, which will make it the same as what you'd download from here.

## Quirkiness awareness notice

This model may come with interesting quirks, as I obviously haven't extensively tested it, and the methodology being so new. I encourage you to play with the model, and post any quirks you notice in the community tab, as that'll help us further understand what this orthogonalization has in the way of side effects. The code I used to generate it (and my published 'Kappa-3' model which is just Phi-3 with the same methodology applied) is available in a Python notebook in this repo. Specifically, the [ortho_cookbook.ipynb](https://huggingface.co/failspy/llama-3-70B-Instruct-abliterated/blob/main/ortho_cookbook.ipynb). 

If you manage to develop further improvements, please share! This is really the most primitive way to use ablation, but there are other possibilities that I believe are as-yet unexplored.