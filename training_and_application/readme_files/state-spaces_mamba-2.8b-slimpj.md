---
license: apache-2.0
---
Mamba-2.8b-slimpj is a model using the [Mamba](https://arxiv.org/abs/2312.00752) architecture, with 2.8B parameters, trained for 600B tokens on the SlimPajama dataset. 

Model code: https://github.com/state-spaces/mamba/tree/main

To load the model, follow the installation instruction in the code repo, and then:
```
from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel
model = MambaLMHeadModel.from_pretrained("state-spaces/mamba-2.8b-slimpj")
```