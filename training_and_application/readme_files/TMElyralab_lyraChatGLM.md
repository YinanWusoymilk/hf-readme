---
license: mit
language: en
tags:
- LLM
- ChatGLM6B
---
## Breakings!

**We know what you want, and here you go!**

- Newly released lyraChatGLM model, suitable for Ampere (A100/A10) as well as Volta (V100)
- lyraChatGLM has been further optimized, reaching **9000 tokens/s** on A100 and **3900 tokens/s** on V100, about **5.5x** faster than the up-to-date official version (2023/6/1).
- The memory usage was optimized too, now we can set batch_size up to **256** on A100!
- INT8 weight only PTQ is supported

**Note that the code was fully updated too, you need to use the new API, see `Uses` below**

If you like our work and consider to join us, feel free to drop a line to benbinwu@tencent.com.

P.S. Recently we have received a lot of inquiries on accelerating customized models. Actually, we **do not have plan** to release the convertion tool at this moment, nor do we think it would be possible to apply your customized models based on our current release.
****
## Model Card for lyraChatGLM

lyraChatGLM is currently the **fastest ChatGLM-6B** available. To the best of our knowledge, it is the **first accelerated version of ChatGLM-6B**.

The inference speed of lyraChatGLM has achieved **300x** acceleration upon the early original version. We are still working hard to further improve the performance.

Among its main features are (updated on 2023-06-20):
- weights: original ChatGLM-6B weights released by THUDM.
- device: Nvidia GPU with Amperer architecture or Volta architecture (A100, A10, V100...).
- batch_size: compiled with dynamic batch size, maximum depends on device. 
- We now support cuda version of both 11.X and 12.X
- lyraChatGLM has been further optimized, with faster model load speed from few minutes to less than 10s for non-int8 mode, and around 1 min for int8 mode!

## Speed
- orginal version(fixed batch infer): commit id 1d240ba
  
### test on A100 40G
1. The maximum batch size and maximum speed table for each version of the model.
|version|max_batch_size|max_speed|
|:-:|:-:|:-:|
|original|1|30 tokens/s|
|original(fxied batch infer)|192|1638.52 tokens/s|
|lyraChatGLM(current)|256|9082.60 tokens/s|
2. The speed table for the same batch size.
|version|1 batch_size|8 batch_size| 64 batch_size | 128 batch_size |
|:-:|:-:|:-:|:-:|:-:|
|original|30 tokens/s| - | - | - |
|original(fxied batch infer)|34.48 tokens/s|356.29 tokens/s|1638.52 tokens/s|1338.45 tokens/s|
|lyraChatGLM(current)|110.05 tokens/s|843.60 tokens/s|4926.92 tokens/s|7235.04 tokens/s|

### test on V100
1. The maximum batch size and maximum speed table for each version of the model.
|version|max_batch_size|max_speed|
|:-:|:-:|:-:|
|original|1|17.83 tokens/s|
|original(fxied batch infer)|128|992.20 tokens/s|
|lyraChatGLM(current)|192|3958.39 tokens/s|
2. The speed table for the same batch size.
|version|1 batch_size|8 batch_size| 64 batch_size | 128 batch_size |
|:-:|:-:|:-:|:-:|:-:|
|original|17.83 tokens/s| - | - | - |
|original(fxied batch infer)|17.83 tokens/s|228.95 tokens/s|889.7 tokens/s|922.20 tokens/s|
|lyraChatGLM(current)|59.33 tokens/s|514.15 tokens/s|2849.88 tokens/s|3958.39 tokens/s|

## Model Sources

- **Repository:** https://huggingface.co/THUDM/chatglm-6b

## Docker Environment Recommendation

- For Cuda 11.X: we recommend ```nvcr.io/nvidia/pytorch:22.12-py3```
- For Cuda 12.0: we recommend ```nvcr.io/nvidia/pytorch:23.02-py3```

```bash
docker pull nvcr.io/nvidia/pytorch:23.02-py3
docker run --rm -it --gpus all -v ./:/lyraChatGLM nvcr.io/nvidia/pytorch:23.02-py3

pip install -r requirements.txt
python demo.py
```

## Uses

```python
from lyraChatGLM import LyraChatGLM6B

model_path = "./models/1-gpu-fp16.bin"
tokenizer_path = "./models"
data_type = "fp16"
int8_mode = 0   # 1 for INT8 WEIGHT ONLY PTQ
max_output_length = 150
arch = "Ampere" # Ampere or Volta
cuda_version = 12

model = LyraChatGLM6B(model_path, tokenizer_path, data_type, int8_mode, arch, cuda_version)
prompt = "列出3个不同的机器学习算法，并说明它们的适用范围."
test_batch_size = 256

prompts = [prompt, ]

# If you want to get different output in same batch, you can set do_sample to True
output_texts = model.generate(prompts, output_length=max_output_length,top_k=30, top_p=0.85, temperature=0.35, repetition_penalty=1.2, do_sample=False)

print(output_texts)

```
## Demo output

### input
列出3个不同的机器学习算法，并说明它们的适用范围.

### output
以下是三个常见的机器学习算法及其适用范围:

1. 决策树(Decision Tree):决策树是一种基于分类和回归问题的朴素贝叶斯模型。它通过构建一系列逐步分裂的分支来预测结果。适用于那些具有简单特征、大量数据且数据集大小在可接受范围内的情况。

2. 随机森林(Random Forest):随机森林是一种集成学习算法,由多个决策树组成。它的优点是能够处理大规模数据和高维度的特征。适用于需要对多个变量进行建模的场景,例如医疗诊断、金融风险评估等。

3. 支持向量机(Support Vector Machine):支持向量机是一种监督学习方法,通常用于分类问题。它可以处理高维数据,并且具有较高的准确性。适用于需要对高维数据进行分类或回归的问题,例如图像识别、自然语言处理等。

## INT8 

**Int8 usage**: 

Our current version supports INT8 weight only PTQ. To enable this mode, simply modify the `int8_mode` to `1` in the demo.py file. 

**In this mode, gpu memory can be further reduced by about half and the speed can be doubled.** 

This solves the issue mentioned in https://github.com/THUDM/ChatGLM-6B/issues/1042. 

However, the speed gain is best achieved with a batch size of no more than 128. If you don't use A100 GPU, you can adjust the 
batch size to reduce it and get the benefits. We recommend a batch size of 64.This mode is very suitable for GPUs with 
limited VRAM or scenarios where it is difficult to use larger batch sizes in real-time services. 

It should be noted that although we have aligned the accuracy in our test cases, there may be slight differences 
in accuracy in some untested scenarios with int8. Please be aware of this.


## Citation
``` bibtex
@Misc{lyraChatGLM2023,
  author =       {Kangjian Wu, Zhengtao Wang, Yibo Lu, Bin Wu},
  title =        {lyraChatGLM: Accelerating ChatGLM to 9000+ tokens/s},
  howpublished = {\url{https://huggingface.co/TMElyralab/lyraChatGLM}},
  year =         {2023}
}
```

## Report bug
- start a discussion to report any bugs!--> https://huggingface.co/TMElyralab/lyraChatGLM/discussions
- report bug with a `[bug]` mark in the title.