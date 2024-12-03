---
license: other
license_name: tongyi-qianwen-research
license_link: >-
  https://huggingface.co/Qwen/CodeQwen1.5-7B/blob/main/LICENSE
language:
- en
pipeline_tag: text-generation
tags:
- pretrained
---

# CodeQwen1.5-7B


## Introduction

CodeQwen1.5 is the Code-Specific version of Qwen1.5. It is a transformer-based decoder-only language model pretrained on a large amount of data of codes. 

* Strong code generation capabilities and competitve performance across a series of benchmarks;
* Supporting long context understanding and generation with the context length of 64K tokens;
* Supporting 92 coding languages
* Excellent performance in text-to-SQL, bug fix, etc.


For more details, please refer to our [blog post](https://qwenlm.github.io/blog/codeqwen1.5/) and [GitHub repo](https://github.com/QwenLM/Qwen1.5).


## Model Details
CodeQwen1.5 is based on Qwen1.5, a language model series including decoder language models of different model sizes. It is trained on 3 trillion tokens of data of codes, and it includes group query attention (GQA) for efficient inference.


## Requirements
The code of Qwen1.5 has been in the latest Hugging face transformers and we advise you to install `transformers>=4.37.0`, or you might encounter the following error:
```
KeyError: 'qwen2'.
```


## Usage

For the base language model, we do not advise you to use it for chat. You can use it for finetuning, and you can also use it for code infilling, code generation, etc., but please be careful about your stopping criteria.


## Citation

If you find our work helpful, feel free to give us a cite.

```
@article{qwen,
  title={Qwen Technical Report},
  author={Jinze Bai and Shuai Bai and Yunfei Chu and Zeyu Cui and Kai Dang and Xiaodong Deng and Yang Fan and Wenbin Ge and Yu Han and Fei Huang and Binyuan Hui and Luo Ji and Mei Li and Junyang Lin and Runji Lin and Dayiheng Liu and Gao Liu and Chengqiang Lu and Keming Lu and Jianxin Ma and Rui Men and Xingzhang Ren and Xuancheng Ren and Chuanqi Tan and Sinan Tan and Jianhong Tu and Peng Wang and Shijie Wang and Wei Wang and Shengguang Wu and Benfeng Xu and Jin Xu and An Yang and Hao Yang and Jian Yang and Shusheng Yang and Yang Yao and Bowen Yu and Hongyi Yuan and Zheng Yuan and Jianwei Zhang and Xingxuan Zhang and Yichang Zhang and Zhenru Zhang and Chang Zhou and Jingren Zhou and Xiaohuan Zhou and Tianhang Zhu},
  journal={arXiv preprint arXiv:2309.16609},
  year={2023}
}
```
