---
license: llama3
---
# Llama-3-8B-SFR-Iterative-DPO-R

## Introduction
We release a state-of-the-art instruct model of its class, **Llama-3-8B-SFR-Iterative-DPO-R**.
On all three widely-used instruct model benchmarks: **Alpaca-Eval-V2**, **MT-Bench**, **Chat-Arena-Hard**, our model outperforms all models of similar size (e.g., LLaMA-3-8B-it), most large open-sourced models (e.g., Mixtral-8x7B-it),
and strong proprietary models (e.g., GPT-3.5-turbo-0613). The model is trained with open-sourced datasets without any additional human-/GPT4-labeling.

## Model Releases
- [SFT model](https://huggingface.co/Salesforce/SFR-SFT-LLaMA-3-8B-R)
- [Reward model](https://huggingface.co/Salesforce/SFR-RM-LLaMA-3-8B-R)
- [RLHF model](https://huggingface.co/Salesforce/SFR-Iterative-DPO-LLaMA-3-8B-R)


## Training methods
We have developed a simple and efficient online RLHF recipe for LLM instruct training. Our recipe is DPO-based and thus much cheaper and simpler to train and tune compared to PPO-based approaches.
Unlike widely-used offline DPO, the online component of our approach effectively mitigates distribution shifts during policy optimization.
For a detailed exposition, please refer to our accompanying technical report.


## Chat Benchmarks

| **Model**               | **Size** | **Method**        | **LC Alpaca-Eval-V2** | **MT-Bench** | **Chat-Arena-Hard** |
|-------------------------|----------|-------------------|-----------------------|--------------|---------------------|
| **Small Open-Sourced Models**           |          |                   |                       |              |                     |
| Gemma-7B-it             | 7B       | SFT               | 10.4                  | 6.38         | 7.5                 |
| Zephyr-7B-beta          | 7B       | Vanilla DPO       | 13.1                  | 7.34         | -                   |
| Mistral-7B-v0.2-it      | 7B       | SFT               | 17.1                  | 7.51         | 12.6                |
| Open-Chat-0106          | 7B       | SFT               | 15.6                  | 7.8          | -                   |
| Starling-7B-beta        | 7B       | PPO               | 25.8                  | 8.12         | 23.0                |
| LLaMA-3-8B-it           | 8B       | RS+DPO+PPO        | 22.9                  | 8.16         | 20.6                |
| **Ours**                |          |                   |                       |              |                     |
| Ours (SFT baseline)     | 8B       | SFT               | 10.2                  | 7.69         | 5.6                 |
| Ours (DPO baseline)     | 8B       | Vanilla DPO       | 22.5                  | 8.17         | 22.4                |
| Ours (Online RLHF)      | 8B       | Iterative DPO     | **31.3**              | **8.46**     | **29.1**            |
| **Large Open-Sourced Models**       |          |                   |                       |              |                     |
| Vicuna-33b-v1.3         | 33B      | SFT               | 17.6                  | 7.12         | 8.6                 |
| Yi-34B-Chat             | 34B      | SFT               | 27.2                  | -            | 23.1                |
| Mixtral-8x7B-it         | 45B*     | SFT               | 23.7                  | 8.30         | 23.4                |
| Tulu-2-DPO-70B          | 70B      | Vanilla DPO       | 21.2                  | 7.89         | 15.0                |
| LLaMA-3-70B-it          | 70B      | RS+DPO+PPO        | 34.4                  | 8.95         | 41.1                |
| Mixtral-8x22B-it        | 141B*    | SFT               | 30.9                  | 8.66         | 36.4                |
| **Proprietary Models**  |       |                   |                       |              |                     |
| GPT-3.5-turbo-1106      | -        | -                 | 19.3                  | 8.35         | 18.9                |
| GPT-3.5-turbo-0613      | -        | -                 | 22.7                  | 8.39         | 24.8                |
| GPT-4-0613              | -        | -                 | 30.2                  | 9.18         | 37.9                |
| Claude-3-Opus           | -        | -                 | 40.5                  | 9.00         | 60.4                |
| GPT-4 Turbo (04/09)     | -        | -                 | 55.0                  | -            | 82.6                |


## Academic Benchmarks

| **Model**                  | **Size** | **Method**      | **GSM-8K** | **MMLU** | **HumanEval** | **TruthfulQA** | **ARC** | **MBPP** |
|----------------------------|----------|-----------------|------------|----------|---------------|----------------|---------|----------|
| LLaMA-3-8B-it              | 8B       | RS+DPO+PPO      | 79.6       | 66.0     | 61.6          | 43.9           | 59.5    | 61.1     |
| Ours (SFT baseline)        | 8B       | SFT             | 74.2       | 64.7     | 65.2          | 53.4           | 61.4    | 62.3     |
| Ours (DPO baseline)        | 8B       | Vanilla DPO     | 79.8       | 64.5     | 63.4          | 61.8           | 65.2    | 60.3     |
| Ours (Iterative RLHF)      | 8B       | Iterative DPO   | 80.7       | 65.3     | 64.6          | 60.4           | 64.3    | 60.8     |


## Usage
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" 

model = AutoModelForCausalLM.from_pretrained("Salesforce/Llama-3-8B-SFR-Iterative-DPO-R")
tokenizer = AutoTokenizer.from_pretrained("Salesforce/Llama-3-8B-SFR-Iterative-DPO-R")

messages = [
    {"role": "user", "content": "I'm trying to teach myself to have nicer handwriting. Can you help?"},
]

model_inputs = tokenizer.apply_chat_template(messages, return_tensors="pt")

model_inputs = model_inputs.to(device)
model.to(device)

output_tokens = model.generate(model_inputs, max_new_tokens=1024, do_sample=True)
model_outputs = tokenizer.batch_decode(output_tokens)
print(model_outputs[0])
```


## Limitations
Llama-3-8B-SFR-Iterative-DPO-R is a research model developed as part of our RLHF initiative at Salesforce. 
While safety and ethical considerations are integral to our alignment process, 
there remains the possibility that the model could generate offensive or unethical content, particularly under adversarial conditions. 
We are committed to continuous improvement in our models to minimize such risks and encourage responsible usage.

## Citation
Please cite our papers if you find our models are useful.

```bibtex
@misc{dong2024rlhf,
      title={RLHF Workflow: From Reward Modeling to Online RLHF}, 
      author={Hanze Dong* and Wei Xiong* and Bo Pang* and Haoxiang Wang* and Han Zhao and Yingbo Zhou and Nan Jiang and Doyen Sahoo and Caiming Xiong and Tong Zhang},
      year={2024},
      eprint={2405.07863},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
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