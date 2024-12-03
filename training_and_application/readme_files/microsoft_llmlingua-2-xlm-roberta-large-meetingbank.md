---
license: mit
---

# LLMLingua-2-Bert-base-Multilingual-Cased-MeetingBank

This model was introduced in the paper [**LLMLingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression** (Pan et al, 2024)](https://arxiv.org/abs/2403.12968). It is a [XLM-RoBERTa (large-sized model)](https://huggingface.co/FacebookAI/xlm-roberta-large) finetuned to perform token classification for task agnostic prompt compression. The probability $p_{preserve}$ of each token $x_i$ is used as the metric for compression. This model is trained on [an extractive text compression dataset(will public)]() constructed with the methodology proposed in the [**LLMLingua-2**](https://arxiv.org/abs/2403.12968), using training examples from [MeetingBank (Hu et al, 2023)](https://meetingbank.github.io/) as the seed data.

For more details, please check the home page of [LLMLingua-2](https://llmlingua.com/llmlingua2.html) and [LLMLingua Series](https://llmlingua.com/).

## Usage
```python
from llmlingua import PromptCompressor

compressor = PromptCompressor(
    model_name="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",
    use_llmlingua2=True
)

original_prompt = """John: So, um, I've been thinking about the project, you know, and I believe we need to, uh, make some changes. I mean, we want the project to succeed, right? So, like, I think we should consider maybe revising the timeline.
Sarah: I totally agree, John. I mean, we have to be realistic, you know. The timeline is, like, too tight. You know what I mean? We should definitely extend it.
"""
results = compressor.compress_prompt_llmlingua2(
    original_prompt,
    rate=0.6,
    force_tokens=['\n', '.', '!', '?', ','],
    chunk_end_tokens=['.', '\n'],
    return_word_label=True,
    drop_consecutive=True
)

print(results.keys())
print(f"Compressed prompt: {results['compressed_prompt']}")
print(f"Original tokens: {results['origin_tokens']}")
print(f"Compressed tokens: {results['compressed_tokens']}")
print(f"Compression rate: {results['rate']}")

# get the annotated results over the original prompt
word_sep = "\t\t|\t\t"
label_sep = " "
lines = results["fn_labeled_original_prompt"].split(word_sep)
annotated_results = []
for line in lines:
    word, label = line.split(label_sep)
    annotated_results.append((word, '+') if label == '1' else (word, '-')) # list of tuples: (word, label)
print("Annotated results:")
for word, label in annotated_results[:10]:
    print(f"{word} {label}")
```

## Citation
```
@article{wu2024llmlingua2,
    title = "{LLML}ingua-2: Data Distillation for Efficient and Faithful Task-Agnostic Prompt Compression",
    author = "Zhuoshi Pan and Qianhui Wu and Huiqiang Jiang and Menglin Xia and Xufang Luo and Jue Zhang and Qingwei Lin and Victor Ruhle and Yuqing Yang and Chin-Yew Lin and H. Vicky Zhao and Lili Qiu and Dongmei Zhang",
    url = "https://arxiv.org/abs/2403.12968",
    journal = "ArXiv preprint",
    volume = "abs/2403.12968",
    year = "2024",
}
```