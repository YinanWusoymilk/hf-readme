---
license: apache-2.0
datasets:
- berkeley-nest/Nectar
language:
- en
library_name: transformers
tags:
- reward model
- RLHF
- RLAIF
---
# Starling-RM-7B-alpha

<!-- Provide a quick summary of what the model is/does. -->

Starling-RM-7B-alpha is a reward model trained from [Llama2-7B-Chat](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf). Following the method of training reward model in [the instructGPT paper](https://arxiv.org/abs/2203.02155), we remove the last layer of Llama2-7B Chat, 
and concatenate a linear layer that outputs scalar for any pair of input prompt and response. We train the reward model with preference dataset [berkeley-nest/Nectar](https://huggingface.co/datasets/berkeley-nest/Nectar), 
with the K-wise maximum likelihood estimator proposed in [this paper](https://arxiv.org/abs/2301.11270). The reward model outputs a scalar for any given prompt and response. A response that is more helpful and 
less harmful will get the highest reward score. Note that since the preference dataset [berkeley-nest/Nectar](https://huggingface.co/datasets/berkeley-nest/Nectar) is based on GPT-4 preference, the reward model is likely to be biased
towards GPT-4's own preference, including longer responses and certain response format. 

For more detailed discussions, please check out our [blog post](https://starling.cs.berkeley.edu), and stay tuned for our upcoming code and paper!


- **Developed by:** Banghua Zhu * , Evan Frick * , Tianhao Wu * , Hanlin Zhu and Jiantao Jiao.
- **Model type:** Reward Model for RLHF
- **License:** Apache-2.0 license under the condition that the model is not used to compete with OpenAI
- **Finetuned from model:** [Llama2-7B-Chat](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)


### Model Sources

<!-- Provide the basic links for the model. -->

- **Blog:** https://starling.cs.berkeley.edu/
- **Paper:** Coming soon!
- **Code:** Coming soon!

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
Please use the following code for inference with the reward model.

```
import os
import torch
from torch import nn
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import snapshot_download

## Define the reward model function class

class GPTRewardModel(nn.Module):
    def __init__(self, model_path):
        super().__init__()
        model = AutoModelForCausalLM.from_pretrained(model_path)
        self.config = model.config
        self.config.n_embd = self.config.hidden_size if hasattr(self.config, "hidden_size") else self.config.n_embd
        self.model = model
        self.transformer = model.model
        self.v_head = nn.Linear(self.config.n_embd, 1, bias=False)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.tokenizer.pad_token = self.tokenizer.unk_token
        self.PAD_ID = self.tokenizer(self.tokenizer.pad_token)["input_ids"][0]

    def get_device(self):
        return self.model.device

    def forward(
        self,
        input_ids=None,
        past_key_values=None,
        attention_mask=None,
        position_ids=None,
    ):
        """
        input_ids, attention_mask: torch.Size([bs, seq_len])
        return: scores: List[bs]
        """
        bs = input_ids.shape[0]
        transformer_outputs = self.transformer(
            input_ids,
            past_key_values=past_key_values,
            attention_mask=attention_mask,
            position_ids=position_ids,
        )
        hidden_states = transformer_outputs[0]
        scores = []
        rewards = self.v_head(hidden_states).squeeze(-1)
        for i in range(bs):
            c_inds = (input_ids[i] == self.PAD_ID).nonzero()
            c_ind = c_inds[0].item() if len(c_inds) > 0 else input_ids.shape[1]
            scores.append(rewards[i, c_ind - 1])
        return scores

## Load the model and tokenizer

reward_model = GPTRewardModel("meta-llama/Llama-2-7b-chat-hf")
reward_tokenizer = reward_model.tokenizer
reward_tokenizer.truncation_side = "left"

directory = snapshot_download("berkeley-nest/Starling-RM-7B-alpha")
for fpath in os.listdir(directory):
    if fpath.endswith(".pt") or fpath.endswith("model.bin"):
        checkpoint = os.path.join(directory, fpath)
        break
   
reward_model.load_state_dict(torch.load(checkpoint), strict=False)
reward_model.eval().requires_grad_(False)


## Define the reward function

def get_reward(samples):
    """samples: List[str]"""
    input_ids = []
    attention_masks = []
    encodings_dict = reward_tokenizer(
        samples,
        truncation=True,
        max_length=2048,
        padding="max_length",
        return_tensors="pt",
    ).to(reward_device)
    input_ids = encodings_dict["input_ids"]
    attention_masks = encodings_dict["attention_mask"]
    mbs = reward_batch_size
    out = []
    for i in range(math.ceil(len(samples) / mbs)):
        rewards = reward_model(input_ids=input_ids[i * mbs : (i + 1) * mbs], attention_mask=attention_masks[i * mbs : (i + 1) * mbs])
        out.extend(rewards)
    return torch.hstack(out)

## Inference over test prompts with llama2 chat template

test_sample = ["<s>[INST] Hello? </s> [/INST] Hi, how can I help you?</s>"] 
reward_for_test_sample = get_reward(test_sample)
print(reward_for_test_sample)
```



## License
The dataset, model and online demo is a research preview intended for non-commercial use only, subject to the data distillation [License](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md) of LLaMA, [Terms of Use](https://openai.com/policies/terms-of-use) of the data generated by OpenAI, and [Privacy Practices](https://chrome.google.com/webstore/detail/sharegpt-share-your-chatg/daiacboceoaocpibfodeljbdfacokfjb) of ShareGPT. Please contact us if you find any potential violation.


## Acknowledgment
We would like to thank Wei-Lin Chiang from Berkeley for detailed feedback of the blog and the projects. We would like to thank the [LMSYS Organization](https://lmsys.org/) for their support of [lmsys-chat-1M](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) dataset, evaluation and online demo. We would like to thank the open source community for their efforts in providing the datasets and base models we used to develope the project, including but not limited to Anthropic, Llama, Mistral, Hugging Face H4, LMSYS, OpenChat, OpenBMB, Flan and ShareGPT.

## Citation
```
@misc{starling2023,
    title = {Starling-7B: Improving LLM Helpfulness & Harmlessness with RLAIF},
    url = {},
    author = {Zhu, Banghua and Frick, Evan and Wu, Tianhao and Zhu, Hanlin and Jiao, Jiantao},
    month = {November},
    year = {2023}
}
```