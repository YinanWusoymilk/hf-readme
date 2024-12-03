---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF/blob/main/LICENSE
language:
- en
base_model:
- Qwen/Qwen2.5-Coder-7B-Instruct
pipeline_tag: text-generation
library_name: transformers
tags:
- code
- codeqwen
- chat
- qwen
- qwen-coder
---


# Qwen2.5-Coder-7B-Instruct-GGUF

## Introduction

Qwen2.5-Coder is the latest series of Code-Specific Qwen large language models (formerly known as CodeQwen). For Qwen2.5-Coder, we release three base language models and instruction-tuned language models, 1.5, 7 and 32 (coming soon) billion parameters. Qwen2.5-Coder brings the following improvements upon CodeQwen1.5:

- Significantly improvements in **code generation**, **code reasoning** and **code fixing**. Base on the strong Qwen2.5, we scale up the training tokens into 5.5 trillion including source code, text-code grounding, Synthetic data, etc. 
- A more comprehensive foundation for real-world applications such as **Code Agents**. Not only enhancing coding capabilities but also maintaining its strengths in mathematics and general competencies.
- **Long-context Support** up to 128K tokens.

**This repo contains the instruction-tuned 7B Qwen2.5-Coder model in the GGUF FOrmat**, which has the following features:
- Type: Causal Language Models
- Training Stage: Pretraining & Post-training
- Architecture: transformers with RoPE, SwiGLU, RMSNorm, and Attention QKV bias
- Number of Parameters: 7.61B
- Number of Paramaters (Non-Embedding): 6.53B
- Number of Layers: 28
- Number of Attention Heads (GQA): 28 for Q and 4 for KV
- Context Length: Full 32,768 tokens
  - Note: Currently, only vLLM supports YARN for length extrapolating. If you want to process sequences up to 131,072 tokens, please refer to non-GGUF models.
- Quantization: q2_K, q3_K_M, q4_0, q4_K_M, q5_0, q5_K_M, q6_K, q8_0

For more details, please refer to our [blog](https://qwenlm.github.io/blog/qwen2.5-coder/), [GitHub](https://github.com/QwenLM/Qwen2.5-Coder), [Documentation](https://qwen.readthedocs.io/en/latest/), [Arxiv](https://arxiv.org/abs/2409.12186).

## Quickstart

Check out our [llama.cpp documentation](https://qwen.readthedocs.io/en/latest/run_locally/llama.cpp.html) for more usage guide.

We advise you to clone [`llama.cpp`](https://github.com/ggerganov/llama.cpp) and install it following the official guide. We follow the latest version of llama.cpp. 
In the following demonstration, we assume that you are running commands under the repository `llama.cpp`.

Since cloning the entire repo may be inefficient, you can manually download the GGUF file that you need or use `huggingface-cli`:
1. Install
   ```shell
   pip install -U huggingface_hub
   ```
2. Download:
   ```shell
   huggingface-cli download Qwen/Qwen2.5-Coder-7B-Instruct-GGUF --include "qwen2.5-coder-7b-instruct-q5_k_m*.gguf" --local-dir . --local-dir-use-symlinks False

   ```
   For large files, we split them into multiple segments due to the limitation of file upload. They share a prefix, with a suffix indicating its index. For examples, `qwen2.5-coder-7b-instruct-q5_k_m-00001-of-00002.gguf` and `qwen2.5-coder-7b-instruct-q5_k_m-00002-of-00002.gguf`. You need to download all of them.
3. (Optional) Merge:
   For split files, you need to merge them first with the command `llama-gguf-split` as shown below:
   ```bash
   # ./llama-gguf-split --merge <first-split-file-path> <merged-file-path>
   ./llama-gguf-split --merge qwen2.5-coder-7b-instruct-q5_k_m-00001-of-00002.gguf qwen2.5-coder-7b-instruct-q5_k_m.gguf
   ```

For users, to achieve chatbot-like experience, it is recommended to commence in the conversation mode:

```shell
./llama-cli -m <gguf-file-path> \
    -co -cnv -p "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." \
    -fa -ngl 80 -n 512
```


## Evaluation & Performance

Detailed evaluation results are reported in this [📑 blog](https://qwenlm.github.io/blog/qwen2.5-coder/).

For quantized models, the benchmark results against the original bfloat16 models can be found [here](https://qwen.readthedocs.io/en/latest/benchmark/quantization_benchmark.html)

For requirements on GPU memory and the respective throughput, see results [here](https://qwen.readthedocs.io/en/latest/benchmark/speed_benchmark.html).

## Citation

If you find our work helpful, feel free to give us a cite.

```
@article{hui2024qwen2,
  title={Qwen2. 5-Coder Technical Report},
  author={Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Jiajun and Yu, Bowen and Dang, Kai and others},
  journal={arXiv preprint arXiv:2409.12186},
  year={2024}
}
@article{qwen2,
      title={Qwen2 Technical Report}, 
      author={An Yang and Baosong Yang and Binyuan Hui and Bo Zheng and Bowen Yu and Chang Zhou and Chengpeng Li and Chengyuan Li and Dayiheng Liu and Fei Huang and Guanting Dong and Haoran Wei and Huan Lin and Jialong Tang and Jialin Wang and Jian Yang and Jianhong Tu and Jianwei Zhang and Jianxin Ma and Jin Xu and Jingren Zhou and Jinze Bai and Jinzheng He and Junyang Lin and Kai Dang and Keming Lu and Keqin Chen and Kexin Yang and Mei Li and Mingfeng Xue and Na Ni and Pei Zhang and Peng Wang and Ru Peng and Rui Men and Ruize Gao and Runji Lin and Shijie Wang and Shuai Bai and Sinan Tan and Tianhang Zhu and Tianhao Li and Tianyu Liu and Wenbin Ge and Xiaodong Deng and Xiaohuan Zhou and Xingzhang Ren and Xinyu Zhang and Xipin Wei and Xuancheng Ren and Yang Fan and Yang Yao and Yichang Zhang and Yu Wan and Yunfei Chu and Yuqiong Liu and Zeyu Cui and Zhenru Zhang and Zhihao Fan},
      journal={arXiv preprint arXiv:2407.10671},
      year={2024}
}
```
