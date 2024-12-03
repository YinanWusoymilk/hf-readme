---
datasets:
- stingning/ultrachat
---
# UltraLM-13b

<!-- Provide a quick summary of what the model is/does. -->

This is UltraLM-13b delta weights, a chat language model trained upon [UltraChat](https://github.com/thunlp/UltraChat)


## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

The model is fine-tuned based on LLaMA-13b with a multi-turn chat-format template as below

```
User: instruction 1<eos_token>
Assistant: response 1<eos_token>
User: instruction 2<eos_token>
Assistant: response 2<eos_token>
...
```

- **License:** UltraLM is based on LLaMA and should be used under LLaMA's [model license](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md).
- **Finetuned from model:** LLaMA-13b
- **Finetuned on data:** [UltraChat](https://github.com/thunlp/UltraChat)

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** [UltraChat](https://github.com/thunlp/UltraChat)
- **Paper:** [arxiv](https://arxiv.org/abs/2305.14233)
- **Demo:** [More Information Needed]

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
To use this model, you need to [recover](https://github.com/thunlp/UltraChat/tree/main/UltraLM) the full model from the delta weights and perform inference following the template below:

```
[Optional]User: system prompt<eos_token>
User: user input<eos_token>
Assistant: 
```
