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

llava-phi-3-mini is a LLaVA model fine-tuned from [microsoft/Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) and [CLIP-ViT-Large-patch14-336](https://huggingface.co/openai/clip-vit-large-patch14-336) with [ShareGPT4V-PT](https://huggingface.co/datasets/Lin-Chen/ShareGPT4V) and [InternVL-SFT](https://github.com/OpenGVLab/InternVL/tree/main/internvl_chat#prepare-training-datasets) by [XTuner](https://github.com/InternLM/xtuner).

**Note: This model is in GGUF format.**

Resources:

- GitHub: [xtuner](https://github.com/InternLM/xtuner)
- Official LLaVA format model: [xtuner/llava-phi-3-mini](https://huggingface.co/xtuner/llava-phi-3-mini)
- HuggingFace LLaVA format model: [xtuner/llava-phi-3-mini-hf](https://huggingface.co/xtuner/llava-phi-3-mini-hf)
- XTuner LLaVA format model: [xtuner/llava-phi-3-mini-xtuner](https://huggingface.co/xtuner/llava-phi-3-mini-xtuner)


## Details

| Model                 | Visual      Encoder | Projector | Resolution |   Pretraining Strategy | Fine-tuning      Strategy |      Pretrain     Dataset |    Fine-tune     Dataset | Pretrain Epoch | Fine-tune Epoch |
| :-------------------- | ------------------: | --------: | ---------: | ---------------------: | ------------------------: | ------------------------: | -----------------------: | -------------- | --------------- |
| LLaVA-v1.5-7B         |              CLIP-L |       MLP |        336 | Frozen LLM, Frozen ViT |      Full LLM, Frozen ViT |       LLaVA-PT     (558K) |     LLaVA-Mix     (665K) | 1              | 1               |
| LLaVA-Llama-3-8B      |              CLIP-L |       MLP |        336 | Frozen LLM, Frozen ViT |        Full LLM, LoRA ViT |       LLaVA-PT     (558K) |     LLaVA-Mix     (665K) | 1              | 1               |
| LLaVA-Llama-3-8B-v1.1 |              CLIP-L |       MLP |        336 | Frozen LLM, Frozen ViT |        Full LLM, LoRA ViT | ShareGPT4V-PT     (1246K) | InternVL-SFT     (1268K) | 1              | 1               |
| **LLaVA-Phi-3-mini**  |              CLIP-L |       MLP |        336 | Frozen LLM, Frozen ViT |        Full LLM, Full ViT | ShareGPT4V-PT     (1246K) | InternVL-SFT     (1268K) | 1              | 2               |

## Results

<div  align="center">
<img src="https://github.com/InternLM/xtuner/assets/36994684/78524f65-260d-4ae3-a687-03fc5a19dcbb" alt="Image" width=500" />
</div>

| Model                 | MMBench Test (EN) | MMMU  Val | SEED-IMG | AI2D Test | ScienceQA Test | HallusionBench aAcc | POPE | GQA  | TextVQA |   MME    | MMStar |
| :-------------------- | :---------------: | :-------: | :------: | :-------: | :------------: | :-----------------: | :--: | :--: | :-----: | :------: | :----: |
| LLaVA-v1.5-7B         |       66.5        |   35.3    |   60.5   |   54.8    |      70.4      |        44.9         | 85.9 | 62.0 |  58.2   | 1511/348 |  30.3  |
| LLaVA-Llama-3-8B      |       68.9        |   36.8    |   69.8   |   60.9    |      73.3      |        47.3         | 87.2 | 63.5 |  58.0   | 1506/295 |  38.2  |
| LLaVA-Llama-3-8B-v1.1 |       72.3        |   37.1    |   70.1   |   70.0    |      72.9      |        47.7         | 86.4 | 62.6 |  59.0   | 1469/349 |  45.1  |
| **LLaVA-Phi-3-mini**  |       69.2        |   41.4    |   70.0   |   69.3    |      73.7      |        49.8         | 87.3 | 61.5 |  57.8   | 1477/313 |  43.7  |


## Quickstart

### Download models

```bash
# mmproj
wget https://huggingface.co/xtuner/llava-phi-3-mini-gguf/resolve/main/llava-phi-3-mini-mmproj-f16.gguf

# fp16 llm
wget https://huggingface.co/xtuner/llava-phi-3-mini-gguf/resolve/main/llava-phi-3-mini-f16.gguf

# int4 llm
wget https://huggingface.co/xtuner/llava-phi-3-mini-gguf/resolve/main/llava-phi-3-mini-int4.gguf

# (optional) ollama fp16 modelfile
wget https://huggingface.co/xtuner/llava-phi-3-mini-gguf/resolve/main/OLLAMA_MODELFILE_F16

# (optional) ollama int4 modelfile
wget https://huggingface.co/xtuner/llava-phi-3-mini-gguf/resolve/main/OLLAMA_MODELFILE_INT4
```

### Chat by `ollama`

Note: llava-phi-3-mini uses the `Phi-3-instruct` chat template.

```bash
# fp16
ollama create llava-phi3-f16 -f ./OLLAMA_MODELFILE_F16
ollama run llava-phi3-f16 "xx.png Describe this image"

# int4
ollama create llava-phi3-int4 -f ./OLLAMA_MODELFILE_INT4
ollama run llava-phi3-int4 "xx.png Describe this image"
```

### Chat by `./llava-cli`

1. Build [llama.cpp](https://github.com/ggerganov/llama.cpp) ([docs](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage)) .
2. Build `./llava-cli` ([docs](https://github.com/ggerganov/llama.cpp/tree/master/examples/llava#usage)).

Note: llava-phi-3-mini uses the `Phi-3-instruct` chat template.

```bash
# fp16
./llava-cli -m ./llava-phi-3-mini-f16.gguf --mmproj ./llava-phi-3-mini-mmproj-f16.gguf --image YOUR_IMAGE.jpg -c 4096

# int4
./llava-cli -m ./llava-phi-3-mini-int4.gguf --mmproj ./llava-phi-3-mini-mmproj-f16.gguf --image YOUR_IMAGE.jpg -c 4096
```

### Reproduce

Please refer to [docs](https://github.com/InternLM/xtuner/tree/main/xtuner/configs/llava/phi3_mini_4k_instruct_clip_vit_large_p14_336#readme).

## Citation

```bibtex
@misc{2023xtuner,
    title={XTuner: A Toolkit for Efficiently Fine-tuning LLM},
    author={XTuner Contributors},
    howpublished = {\url{https://github.com/InternLM/xtuner}},
    year={2023}
}
```
