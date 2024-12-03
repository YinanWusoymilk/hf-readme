---
license: apache-2.0
---

This is WizardLM trained on top of tiiuae/falcon-40b, with a subset of the dataset - responses that contained alignment / moralizing were removed. The intent is to train a WizardLM that doesn't have alignment built-in, so that alignment (of any sort) can be added separately with for example with a RLHF LoRA.

Shout out to the open source AI/ML community, and everyone who helped me out.

Note:
An uncensored model has no guardrails.
You are responsible for anything you do with the model, just as you are responsible for anything you do with any dangerous object such as a knife, gun, lighter, or car. Publishing anything this model generates is the same as publishing it yourself. You are responsible for the content you publish, and you cannot blame the model any more than you can blame the knife, gun, lighter, or car for what you do with it.

Prompt format is WizardLM.

```
What is a falcon?  Can I keep one as a pet?
### Response:
```

Thank you [chirper.ai](https://chirper.ai) for sponsoring some of my compute!