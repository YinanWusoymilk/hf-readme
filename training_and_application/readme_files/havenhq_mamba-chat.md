---
license: apache-2.0
---

Mamba-Chat is the first chat language model based on a state-space model architecture, not a transformer.

The model is a fine-tune of Albert Gu's and Tri Dao's model [Mamba-2.8B](https://github.com/state-spaces/mamba) from their paper *Mamba: Linear-Time Sequence Modeling with Selective State Spaces*.

Check our our [Github repository](https://github.com/havenhq/mamba-chat/tree/main) for training and inference code.

The prompt format is the zephyr format:

```
<|user|> {user_message}
<|assistant|> {assistant_message}
<|user|> {user_message}
<|assistant|> {assistant_message}
```