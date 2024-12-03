---
license: mit
---

# stories15M_MOE

This model is [ModelCloud/tinyllama-15M-stories](https://huggingface.co/ModelCloud/tinyllama-15M-stories) repeated 4 times to make 4 experts.

The model is used for testing, not intended to be used in production (unless your product is some kind of bedtime story teller)

Weight of router is initialized randomly

## shakespeare LoRA adapter

A LoRA adapter trained on first 100 paragraphs of shakespeare can be found inside `moe_shakespeare15M`

With input: `Look in thy glass`
- Original model generates: `Look in thy glass was a little girl. She was only three years old and she was three years old. She was`
- LoRA adapter generates: `Look in thy glass in love of the eye: That's when when the eye see thy on the sun'`
