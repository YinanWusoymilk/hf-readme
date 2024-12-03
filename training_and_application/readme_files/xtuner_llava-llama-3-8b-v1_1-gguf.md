---
datasets:
- Lin-Chen/ShareGPT4V
pipeline_tag: image-to-text
---

<div align="center">
  <img src="https://github.com/InternLM/lmdeploy/assets/36994684/0cf8d00f-e86b-40ba-9b54-dc8f1bc6c8d8" width="600"/>


[![Generic badge](https://img.shields.io/badge/GitHub-%20XTuner-black.svg)](https://github.com/InternLM/xtuner)


</div>

## Model

llava-llama-3-8b-v1_1 is a LLaVA model fine-tuned from [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) and [CLIP-ViT-Large-patch14-336](https://huggingface.co/openai/clip-vit-large-patch14-336) with [ShareGPT4V-PT](https://huggingface.co/datasets/Lin-Chen/ShareGPT4V) and [InternVL-SFT](https://github.com/OpenGVLab/InternVL/tree/main/internvl_chat#prepare-training-datasets) by [XTuner](https://github.com/InternLM/xtuner).

**Note: This model is in GGUF format.**

Resources:

- GitHub: [xtuner](https://github.com/InternLM/xtuner)
- HuggingFace LLaVA format model: [xtuner/llava-llama-3-8b-v1_1-transformers](https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-transformers)
- Official LLaVA format model: [xtuner/llava-llama-3-8b-v1_1-hf](https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-hf)
- XTuner LLaVA format model: [xtuner/llava-llama-3-8b-v1_1](https://huggingface.co/xtuner/llava-llama-3-8b-v1_1)


## Details

| Model                 | Visual      Encoder | Projector | Resolution |   Pretraining Strategy | Fine-tuning      Strategy |      Pretrain     Dataset |    Fine-tune     Dataset |
| :-------------------- | ------------------: | --------: | ---------: | ---------------------: | ------------------------: | ------------------------: | -----------------------: |
| LLaVA-v1.5-7B         |              CLIP-L |       MLP |        336 | Frozen LLM, Frozen ViT |      Full LLM, Frozen ViT |       LLaVA-PT     (558K) |     LLaVA-Mix     (665K) |
| LLaVA-Llama-3-8B      |              CLIP-L |       MLP |        336 | Frozen LLM, Frozen ViT |        Full LLM, LoRA ViT |       LLaVA-PT     (558K) |     LLaVA-Mix     (665K) |
| LLaVA-Llama-3-8B-v1.1 |              CLIP-L |       MLP |        336 | Frozen LLM, Frozen ViT |        Full LLM, LoRA ViT | ShareGPT4V-PT     (1246K) | InternVL-SFT     (1268K) |

## Results

<div  align="center">
<img src="https://github.com/InternLM/xtuner/assets/36994684/a157638c-3500-44ed-bfab-d8d8249f91bb" alt="Image" width=500" />
</div>

| Model                 | MMBench Test (EN) | MMBench Test (CN) | CCBench Dev | MMMU  Val | SEED-IMG | AI2D Test | ScienceQA Test | HallusionBench aAcc | POPE | GQA  | TextVQA |   MME    | MMStar |
| :-------------------- | :---------------: | :---------------: | :---------: | :-------: | :------: | :-------: | :------------: | :-----------------: | :--: | :--: | :-----: | :------: | :----: |
| LLaVA-v1.5-7B         |       66.5        |       59.0        |    27.5     |   35.3    |   60.5   |   54.8    |      70.4      |        44.9         | 85.9 | 62.0 |  58.2   | 1511/348 |  30.3  |
| LLaVA-Llama-3-8B      |       68.9        |       61.6        |    30.4     |   36.8    |   69.8   |   60.9    |      73.3      |        47.3         | 87.2 | 63.5 |  58.0   | 1506/295 |  38.2  |
| LLaVA-Llama-3-8B-v1.1 |       72.3        |       66.4        |    31.6     |   36.8    |   70.1   |   70.0    |      72.9      |        47.7         | 86.4 | 62.6 |  59.0   | 1469/349 |  45.1  |


## Quickstart

### Download models

```bash
# mmproj
wget https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-gguf/resolve/main/llava-llama-3-8b-v1_1-mmproj-f16.gguf

# fp16 llm
wget https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-gguf/resolve/main/llava-llama-3-8b-v1_1-f16.gguf

# int4 llm
wget https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-gguf/resolve/main/llava-llama-3-8b-v1_1-int4.gguf

# (optional) ollama fp16 modelfile
wget https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-gguf/resolve/main/OLLAMA_MODELFILE_F16

# (optional) ollama int4 modelfile
wget https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-gguf/resolve/main/OLLAMA_MODELFILE_INT4
```

### Chat by `ollama`

```bash
# fp16
ollama create llava-llama3-f16 -f ./OLLAMA_MODELFILE_F16
ollama run llava-llama3-f16 "xx.png Describe this image"

# int4
ollama create llava-llama3-int4 -f ./OLLAMA_MODELFILE_INT4
ollama run llava-llama3-int4 "xx.png Describe this image"
```

### Chat by `llama.cpp`

1. Build [llama.cpp](https://github.com/ggerganov/llama.cpp) ([docs](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage)) .
2. Build `./llava-cli` ([docs](https://github.com/ggerganov/llama.cpp/tree/master/examples/llava#usage)).

Note: llava-llama-3-8b-v1_1 uses the Llama-3-instruct chat template.

```bash
# fp16
./llava-cli -m ./llava-llama-3-8b-v1_1-f16.gguf --mmproj ./llava-llama-3-8b-v1_1-mmproj-f16.gguf --image YOUR_IMAGE.jpg -c 4096 -e -p "<|start_header_id|>user<|end_header_id|>\n\n<image>\nDescribe this image<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"

# int4
./llava-cli -m ./llava-llama-3-8b-v1_1-int4.gguf --mmproj ./llava-llama-3-8b-v1_1-mmproj-f16.gguf --image YOUR_IMAGE.jpg -c 4096 -e -p "<|start_header_id|>user<|end_header_id|>\n\n<image>\nDescribe this image<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
```

### Reproduce

Please refer to [docs](https://github.com/InternLM/xtuner/tree/main/xtuner/configs/llava/llama3_8b_instruct_clip_vit_large_p14_336#readme).

## Citation

```bibtex
@misc{2023xtuner,
    title={XTuner: A Toolkit for Efficiently Fine-tuning LLM},
    author={XTuner Contributors},
    howpublished = {\url{https://github.com/InternLM/xtuner}},
    year={2023}
}
```
