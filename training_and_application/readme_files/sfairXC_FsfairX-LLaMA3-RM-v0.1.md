---
license: cc-by-nc-4.0
---

This reward function can be used for RLHF, including PPO, iterative SFT, iterative DPO.

The license is derived from `PKU-Alignment/PKU-SafeRLHF-30K`.

## Training
The base model is `meta-llama/Meta-Llama-3-8B-Instruct`.

We use the training script at `https://github.com/WeiXiongUST/RLHF-Reward-Modeling`.


## Uses

```python
  from transformers import AutoTokenizer, pipeline
  rm_tokenizer = AutoTokenizer.from_pretrained("sfairXC/FsfairX-LLaMA3-RM-v0.1")
  device = 0 # accelerator.device
  rm_pipe = pipeline(
      "sentiment-analysis",
      model="sfairXC/FsfairX-LLaMA3-RM-v0.1",
      #device="auto",
      device=device,
      tokenizer=rm_tokenizer,
      model_kwargs={"torch_dtype": torch.bfloat16}
  )

  pipe_kwargs = {
      "return_all_scores": True,
      "function_to_apply": "none",
      "batch_size": 1
  }

  chat = [
   {"role": "user", "content": "Hello, how are you?"},
   {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
   {"role": "user", "content": "I'd like to show off how chat templating works!"},
  ]

  test_texts = [tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=False).replace(tokenizer.bos_token, "")]
  pipe_outputs = rm_pipe(test_texts, **pipe_kwargs)
  rewards = [output[0]["score"] for output in pipe_outputs]
```


## Results


This Reward model is the SOTA open-source RM (Apr 20, 2024) on Reward-Bench.

| Metric       | Score  |
|--------------|--------|
| Chat         | 99.44  |
| Chat Hard    | 65.13  |
| Safety       | 88.76  |
| Reasoning    | 88.3   |



## References
The repo was part of the iterative rejection sampling fine-tuning and iterative DPO. If you find the content of this repo useful in your work, please consider cite it as follows:

```bibtex
@article{dong2023raft,
  title={Raft: Reward ranked finetuning for generative foundation model alignment},
  author={Dong, Hanze and Xiong, Wei and Goyal, Deepanshu and Pan, Rui and Diao, Shizhe and Zhang, Jipeng and Shum, Kashun and Zhang, Tong},
  journal={arXiv preprint arXiv:2304.06767},
  year={2023}
}

@misc{xiong2024iterative,
      title={Iterative Preference Learning from Human Feedback: Bridging Theory and Practice for RLHF under KL-Constraint}, 
      author={Wei Xiong and Hanze Dong and Chenlu Ye and Ziqi Wang and Han Zhong and Heng Ji and Nan Jiang and Tong Zhang},
      year={2024},
      eprint={2312.11456},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```