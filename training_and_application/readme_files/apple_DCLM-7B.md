---
license: apple-ascl
---



<img src="https://cdn-uploads.huggingface.co/production/uploads/63118add64939fabc0108b28/BB42g4V8HTxb5dR4tcy8A.png" alt="DCLM Logo" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


# Model Card for DCLM-Baseline-7B

DCLM-Baseline-7B is a 7 billion parameter language model trained on the DCLM-Baseline dataset, which was curated as part of the DataComp for Language Models (DCLM) benchmark. This model is designed to showcase the effectiveness of systematic data curation techniques for improving language model performance.

## Model Details

| Size | Training Tokens | Layers | Hidden Size | Attention Heads | Context Length |
|------|-----------------|--------|-------------|-----------------|----------------|
| 7B   | 2.5T            | 32     | 4096        | 32              | 2048           |


### Model Description

- **Developed by:** DataComp for Language Models (DCLM) Team
- **Model type:** Decoder-only Transformer language model
- **Language(s):** English (primarily)
- **License:** Apple Sample Code License
- **Contact:** contact@datacomp.ai
- **Date:** June 2024

### Model Sources

- **Repository:** https://github.com/mlfoundations/dclm
- **Dataset:** https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0
- **Paper:** [DataComp-LM: In search of the next generation of training sets for language models](https://arxiv.org/abs/2406.11794)


## Using Model

First install open_lm

```bash
pip install git+https://github.com/mlfoundations/open_lm.git
```

Then:
```python
from open_lm.hf import *
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("apple/DCLM-Baseline-7B")
model = AutoModelForCausalLM.from_pretrained("apple/DCLM-Baseline-7B")

inputs = tokenizer(["Machine learning is"], return_tensors="pt")
gen_kwargs = {"max_new_tokens": 50, "top_p": 0.8, "temperature": 0.8, "do_sample": True, "repetition_penalty": 1.1}
output = model.generate(inputs['input_ids'], **gen_kwargs)
output = tokenizer.decode(output[0].tolist(), skip_special_tokens=True)
print(output)
```






### Training Details

The model was trained using the following setup:

- **Architecture:** Decoder-only Transformer 
- **Framework:** PyTorch with OpenLM
- **Optimizer:** AdamW
- **Learning Rate:** 2e-3 (peak)
- **Weight Decay:** 0.05
- **Batch Size:** 2048 sequences
- **Sequence Length:** 2048 tokens
- **Total Training Tokens:** 2.5T
- **Hardware:** Trained on H100 GPUs

For more detailed training information, please refer to Section 3.4 and Appendix F of the DCLM paper.
To ensure our trained model is broadly useful, including for math and coding tasks, we combine our 3.8T [DCLM-BASELINE](https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0)  with the [StarCoder](https://huggingface.co/datasets/bigcode/starcoderdata)  and [ProofPile2](https://huggingface.co/datasets/EleutherAI/proof-pile-2) data to arrive at a 4.1T token dataset.

## Evaluation

Here are the evaluation results for DCLM-Baseline-7B on various tasks (using [llm-foundry](https://github.com/mosaicml/llm-foundry) eval suite)

| Task | Score |
|------|-------|
| MMLU (zero-shot) | 0.5766 |
| MMLU (few-shot) | 0.6372 |
| HellaSwag (zero-shot) | 0.7987 |
| HellaSwag | 0.8043 |
| Jeopardy | 0.4745 |
| TriviaQA | 0.5270 |
| GSM8K (CoT) | 0.0250 |
| AGI Eval SAT Math (CoT) | 0.0136 |
| AQuA (CoT) | 0.0490 |
| SVAMP (CoT) | 0.4900 |
| BigBench QA Wikidata | 0.7120 |
| ARC Easy | 0.8220 |
| ARC Challenge | 0.5990 |
| BigBench Misconceptions | 0.6986 |
| COPA | 0.8500 |
| SIQA | 0.8291 |
| CommonsenseQA | 0.8018 |
| PIQA | 0.8128 |
| OpenBookQA | 0.4540 |
| BigBench Novel Concepts | 0.7188 |
| BigBench Strange Stories | 0.7586 |
| BigBench Strategy QA | 0.6173 |
| LAMBADA | 0.8220 |
| Winograd | 0.8828 |
| Winogrande | 0.7269 |
| BigBench Conlang Translation | 0.0244 |
| BigBench Language Identification | 0.5219 |
| BigBench Conceptual Combinations | 0.6990 |
| BigBench Elementary Math QA | 0.3431 |
| BigBench Dyck Languages | 0.4930 |
| AGI Eval LSAT AR | 0.2435 |
| BigBench CS Algorithms | 0.6121 |
| BigBench Logical Deduction | 0.3620 |
| BigBench Operators | 0.4857 |
| BigBench Repeat Copy Logic | 0.4063 |
| Simple Arithmetic (no spaces) | 0.2940 |
| Simple Arithmetic (with spaces) | 0.3110 |
| MathQA | 0.3098 |
| LogiQA | 0.4132 |
| PubMedQA | 0.7060 |
| SQuAD | 0.5856 |
| AGI Eval LSAT RC | 0.6716 |
| AGI Eval LSAT LR | 0.5392 |
| CoQA | 0.4074 |
| BigBench Understanding Fables | 0.6825 |
| BoolQ | 0.8343 |
| AGI Eval SAT EN | 0.7670 |
| Winogender MC (Female) | 0.6000 |
| Winogender MC (Male) | 0.5500 |
| Enterprise PII Classification | 0.7676 |
| BBQ | 0.6912 |
| GPQA Main | 0.2612 |
| GPQA Diamond | 0.2475 |

Note: All scores are presented as decimal values between 0 and 1, representing the proportion of correct answers or the model's performance on each task.


## Comparison 


Below are comparisions of this model with other models in the 7B regime.

| Model         | Params | Tokens | Open dataset? | CORE     | MMLU     | EXTENDED |
|---------------|--------|--------|---------------|----------|----------|----------|
| **Open weights, closed datasets** |        |        |               |          |          |          |
| Llama2        | 7B     | 2T     | ❌             | 49.2     | 45.8     | 34.1     |
| DeepSeek      | 7B     | 2T     | ❌             | 50.7     | 48.5     | 35.3     |
| Mistral-0.3   | 7B     | ?      | ❌             | 57.0     | 62.7     | 45.1     |
| QWEN-2        | 7B     | ?      | ❌            | 57.5     | **71.9** | 50.5     |
| Llama3        | 8B     | 15T    | ❌             | 57.6     | 66.2     | 46.3     |
| Gemma         | 8B     | 6T     | ❌             | 57.8     | 64.3     | 44.6     |
| Phi-3         | 7B     | ?      | ❌             | **61.0** | 69.9     | **57.9** |
| **Open weights, open datasets** |        |        |               |          |          |          |
| Falcon        | 7B     | 1T     | ✅              | 44.1     | 27.4     | 25.1     |
| OLMo-1.7      | 7B     | 2.1T   | ✅              | 47.0     | 54.0     | 34.2     |
| MAP-Neo       | 7B     | 4.5T   | ✅              | **50.2** | **57.1** | **40.4** |
| **DCLM-7B** | 7B     | 2.5T   | ✅              | **56.1** | **63.7** | **43.6** |



## Limitations and Biases

While DCLM-Baseline-7B demonstrates strong performance across a range of tasks, it's important to note:

1. The model may exhibit biases present in its training data, which is derived from web crawl data.
2. It has not undergone specific alignment or safety fine-tuning, so outputs should be used with caution.
3. Performance on tasks not included in the evaluation suite may vary.
4. The model's knowledge is limited to its training data cutoff date.

## Ethical Considerations

Users should be aware that this model, like all large language models, can potentially generate harmful or biased content. It should not be used for making decisions about individuals or in sensitive applications without appropriate safeguards and human oversight.

## Citation

If you use this model in your research, please cite:

```
@article{Li2024DataCompLM,
  title={DataComp-LM: In search of the next generation of training sets for language models},
  author={Jeffrey Li and Alex Fang and Georgios Smyrnis and Maor Ivgi and Matt Jordan and Samir Gadre and Hritik Bansal and Etash Guha and Sedrick Keh and Kushal Arora and [... full author list]},
  journal={arXiv preprint arXiv:2406.11794},
  year={2024}
}
```
