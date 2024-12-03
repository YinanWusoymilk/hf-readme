---
datasets:
- Lin-Chen/ShareGPT4V
pipeline_tag: image-text-to-text
library_name: xtuner
---

<div align="center">
  <img src="https://github.com/InternLM/lmdeploy/assets/36994684/0cf8d00f-e86b-40ba-9b54-dc8f1bc6c8d8" width="600"/>


[![Generic badge](https://img.shields.io/badge/GitHub-%20XTuner-black.svg)](https://github.com/InternLM/xtuner)


</div>

## Model

llava-llama-3-8b-v1_1 is a LLaVA model fine-tuned from [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) and [CLIP-ViT-Large-patch14-336](https://huggingface.co/openai/clip-vit-large-patch14-336) with [ShareGPT4V-PT](https://huggingface.co/datasets/Lin-Chen/ShareGPT4V) and [InternVL-SFT](https://github.com/OpenGVLab/InternVL/tree/main/internvl_chat#prepare-training-datasets) by [XTuner](https://github.com/InternLM/xtuner).


**Note: This model is in XTuner LLaVA format.**

Resources:

- GitHub: [xtuner](https://github.com/InternLM/xtuner)
- HuggingFace LLaVA format model: [xtuner/llava-llama-3-8b-v1_1-transformers](https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-transformers)
- Official LLaVA format model: [xtuner/llava-llama-3-8b-v1_1-hf](https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-hf)
- GGUF format model: [xtuner/llava-llama-3-8b-v1_1-gguf](https://huggingface.co/xtuner/llava-llama-3-8b-v1_1-gguf)

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

### Installation

```shell
pip install 'git+https://github.com/InternLM/xtuner.git#egg=xtuner[deepspeed]'
```

### Chat

```shell
xtuner chat xtuner/llava-llama-3-8b-v1_1 \
  --visual-encoder openai/clip-vit-large-patch14-336 \
  --llava xtuner/llava-llama-3-8b-v1_1 \
  --prompt-template llama3_chat \
  --image $IMAGE_PATH
```

### MMBench Evaluation

XTuner integrates the MMBench evaluation, and you can perform evaluations with the following command!

```bash
xtuner mmbench xtuner/llava-llama-3-8b-v1_1 \
  --visual-encoder openai/clip-vit-large-patch14-336 \
  --llava xtuner/llava-llama-3-8b-v1_1 \
  --prompt-template llama3_chat \
  --data-path $MMBENCH_DATA_PATH \
  --work-dir $RESULT_PATH
```

After the evaluation is completed, if it's a development set, it will directly print out the results; If it's a test set, you need to submit `mmbench_result.xlsx` to the official MMBench for final evaluation to obtain precision results!

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
