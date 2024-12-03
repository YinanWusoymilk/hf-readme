---
license: mit
datasets:
- kaiokendev/SuperCOT-dataset
- neulab/conala
- yahma/alpaca-cleaned
- QingyiSi/Alpaca-CoT
---

### SuperCOT LoRA
SuperCOT is a LoRA trained with the aim of making LLaMa follow prompts for Langchain better, by infusing chain-of-thought datasets, code explanations and instructions, snippets, logical deductions and Alpaca GPT-4 prompts.
It uses a mixture of the following datasets:

[https://huggingface.co/datasets/QingyiSi/Alpaca-CoT](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT)
- Chain of thought QED
- Chain of thought Aqua
- CodeAlpaca

[https://huggingface.co/datasets/neulab/conala](https://huggingface.co/datasets/neulab/conala)
- Code snippets

[https://huggingface.co/datasets/yahma/alpaca-cleaned](https://huggingface.co/datasets/yahma/alpaca-cleaned)
- Alpaca GPT4

### Merged Models
#### 30B
- GGML 30B 4-bit: [https://huggingface.co/gozfarb/llama-30b-supercot-ggml](https://huggingface.co/gozfarb/llama-30b-supercot-ggml)
- GGML 30B Q4_3: [https://huggingface.co/camelids/llama-33b-supercot-ggml-q4_3](https://huggingface.co/camelids/llama-33b-supercot-ggml-q4_3)
- GGML 30B Q5_1: [https://huggingface.co/camelids/llama-33b-supercot-ggml-q5_1](https://huggingface.co/camelids/llama-33b-supercot-ggml-q5_1)
- 30B (unquantized): [https://huggingface.co/ausboss/llama-30b-supercot](https://huggingface.co/ausboss/llama-30b-supercot)
- 30B 4-bit 128g CUDA: [https://huggingface.co/tsumeone/llama-30b-supercot-4bit-128g-cuda](https://huggingface.co/tsumeone/llama-30b-supercot-4bit-128g-cuda)
- 30B 4-bit 128g TRITON: N/A
- 30B 4-bit CUDA (no groupsize, better VRAM): [https://huggingface.co/tsumeone/llama-30b-supercot-4bit-cuda](https://huggingface.co/tsumeone/llama-30b-supercot-4bit-cuda)
- 30B 3-bit 128g CUDA: [https://huggingface.co/tsumeone/llama-30b-supercot-3bit-128g-cuda](https://huggingface.co/tsumeone/llama-30b-supercot-3bit-128g-cuda)

#### 13B
- GGML 13B 4-bit: [https://huggingface.co/gozfarb/llama-13b-supercot-ggml](https://huggingface.co/gozfarb/llama-13b-supercot-ggml)
- GGML 13B Q4_3: [https://huggingface.co/camelids/llama-13b-supercot-ggml-q4_3](https://huggingface.co/camelids/llama-13b-supercot-ggml-q4_3)
- GGML 13B Q5_1: [https://huggingface.co/camelids/llama-13b-supercot-ggml-q5_1](https://huggingface.co/camelids/llama-13b-supercot-ggml-q5_1)
- GGML 13B Q8_0: [https://huggingface.co/camelids/llama-13b-supercot-ggml-q8_0](https://huggingface.co/camelids/llama-13b-supercot-ggml-q8_0)
- 13B (unquantized): [https://huggingface.co/ausboss/llama-13b-supercot](https://huggingface.co/ausboss/llama-13b-supercot)
- 13B 4-bit 128g CUDA: [https://huggingface.co/ausboss/llama-13b-supercot-4bit-128g](https://huggingface.co/ausboss/llama-13b-supercot-4bit-128g)
- 13B 4-bit 128g TRITON: [https://huggingface.co/TheYuriLover/llama-13b-SuperCOT-4bit-TRITON](https://huggingface.co/TheYuriLover/llama-13b-SuperCOT-4bit-TRITON)
- 13B 4-bit CUDA (no groupsize, better VRAM): N/A

(Thanks to all the awesome anons with supercomputers)

### Compatibility
This LoRA is compatible with any 7B, 13B or 30B 4-bit quantized LLaMa model, including ggml quantized converted bins

### Prompting
You should prompt the LoRA the same way you would prompt Alpaca or Alpacino:

```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
<instruction>

### Input:
<any additional context. Remove this if it's not neccesary>

### Response:
<make sure to leave a single new-line here for optimal results>
```

Remember that with lower parameter sizes, the structure of the prompt becomes more important. The same prompt worded differently can give wildly different answers. Consider using the following suggestion suffixes to improve output quality:

- "Think through this step by step"
- "Let's think about this logically"
- "Explain your reasoning"
- "Provide details to support your answer"
- "Compare and contrast your answer with alternatives"

### Coming Soon
- Tweet fix for 13B and 7B - lower model sizes seem to be extremely sensitive to hashtags at the end of training data responses, especially at longer cutoffs

### Citations
Alpaca COT datasets
```
@misc{alpaca-cot,
  author = {Qingyi Si, Zheng Lin },
  school = {Institute of Information Engineering, Chinese Academy of Sciences, Beijing, China},
  title = {Alpaca-CoT: An Instruction Fine-Tuning Platform with Instruction Data Collection and Unified Large Language Models Interface},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/PhoebusSi/alpaca-CoT}},
}
```
Stanford Alpaca
```
@misc{alpaca,
  author = {Rohan Taori and Ishaan Gulrajani and Tianyi Zhang and Yann Dubois and Xuechen Li and Carlos Guestrin and Percy Liang and Tatsunori B. Hashimoto },
  title = {Stanford Alpaca: An Instruction-following LLaMA model},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/tatsu-lab/stanford_alpaca}},
}
```
Google FLAN
```
@inproceedings{weifinetuned,
  title={Finetuned Language Models are Zero-Shot Learners},
  author={Wei, Jason and Bosma, Maarten and Zhao, Vincent and Guu, Kelvin and Yu, Adams Wei and Lester, Brian and Du, Nan and Dai, Andrew M and Le, Quoc V},
  booktitle={International Conference on Learning Representations}
}
```