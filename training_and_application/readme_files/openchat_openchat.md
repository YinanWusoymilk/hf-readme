---
language:
- en
tags:
- llama
license: other
---

# OpenChat: Less is More for Open-source Models

OpenChat is a series of open-source language models fine-tuned on a diverse and high-quality dataset of multi-round conversations. With only ~6K GPT-4 conversations filtered from the ~90K ShareGPT conversations, OpenChat is designed to achieve high performance with limited data.

**Generic models:**

 - OpenChat: based on LLaMA-13B (2048 context length)
   - **🚀 105.7%** of ChatGPT score on Vicuna GPT-4 evaluation
   - **🔥 80.9%** Win-rate on AlpacaEval
   - **🤗 Only used 6K data for finetuning!!!**
 - OpenChat-8192: based on LLaMA-13B  (extended to 8192 context length)
   - **106.6%** of ChatGPT score on Vicuna GPT-4 evaluation
   - **79.5%** Win-rate on AlpacaEval

**Code models:**

 - OpenCoderPlus: based on StarCoderPlus (native 8192 context length)
   - **102.5%** of ChatGPT score on Vicuna GPT-4 evaluation
   - **78.7%** Win-rate on AlpacaEval

*Note:* Please load the pretrained models using *bfloat16*

## Code and Inference Server

We provide the full source code, including an inference server compatible with the "ChatCompletions" API, in the [OpenChat](https://github.com/imoneoi/openchat) GitHub repository.

## Web UI

OpenChat also includes a web UI for a better user experience. See the GitHub repository for instructions.

## Conversation Template

The conversation template **involves concatenating tokens**.

Besides base model vocabulary, an end-of-turn token `<|end_of_turn|>` is added, with id `eot_token_id`.

```python
# OpenChat
[bos_token_id] + tokenize("Human: ") + tokenize(user_question) + [eot_token_id] + tokenize("Assistant: ")
# OpenCoder
tokenize("User:") + tokenize(user_question) + [eot_token_id] + tokenize("Assistant:")
```

*Hint: In BPE, `tokenize(A) + tokenize(B)` does not always equals to `tokenize(A + B)`*

Following is the code for generating the conversation templates:

```python
@dataclass
class ModelConfig:
    # Prompt
    system: Optional[str]

    role_prefix: dict
    ai_role: str
    eot_token: str
    bos_token: Optional[str] = None

    # Get template
    def generate_conversation_template(self, tokenize_fn, tokenize_special_fn, message_list):
        tokens = []
        masks = []

        # begin of sentence (bos)
        if self.bos_token:
            t = tokenize_special_fn(self.bos_token)
            tokens.append(t)
            masks.append(False)

        # System
        if self.system:
            t = tokenize_fn(self.system) + [tokenize_special_fn(self.eot_token)]
            tokens.extend(t)
            masks.extend([False] * len(t))

        # Messages
        for idx, message in enumerate(message_list):
            # Prefix
            t = tokenize_fn(self.role_prefix[message["from"]])
            tokens.extend(t)
            masks.extend([False] * len(t))

            # Message
            if "value" in message:
                t = tokenize_fn(message["value"]) + [tokenize_special_fn(self.eot_token)]
                tokens.extend(t)
                masks.extend([message["from"] == self.ai_role] * len(t))
            else:
                assert idx == len(message_list) - 1, "Empty message for completion must be on the last."

        return tokens, masks


MODEL_CONFIG_MAP = {
    # OpenChat / OpenChat-8192
    "openchat": ModelConfig(
        # Prompt
        system=None,

        role_prefix={
            "human": "Human: ",
            "gpt": "Assistant: "
        },
        ai_role="gpt",
        eot_token="<|end_of_turn|>",
        bos_token="<s>",
    ),

    # OpenCoder / OpenCoderPlus
    "opencoder": ModelConfig(
        # Prompt
        system=None,

        role_prefix={
            "human": "User:",
            "gpt": "Assistant:"
        },
        ai_role="gpt",
        eot_token="<|end_of_turn|>",
        bos_token=None,
    )
}
```


## License
Our weight license is subject to their corresponding base model. For example, OpenChat and OpenChat-8192 are the same as the model [License](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md) of LLaMA for non-commercial use only, while OpenCoderPlus is under the [License](https://huggingface.co/blog/starcoder) of StarCoder. Furthermore, we should follow the [Privacy Practices](https://chrome.google.com/webstore/detail/sharegpt-share-your-chatg/daiacboceoaocpibfodeljbdfacokfjb) of ShareGPT. The [code](https://github.com/imoneoi/openchat) released on GitHub is under Apache License 2.0.


## Citation

```
@software{openllms23,
  title = {{OpenLLMs: Less is More for Open-source Models}},
  author = {Wang, Guan and Cheng, Sijie and Yu, Qiying and Liu, Changling},
  doi = {10.5281/zenodo.8105775},
  url = {https://github.com/imoneoi/openchat},
  version = {pre-release},
  year = {2023},
  month = {7},
}
```