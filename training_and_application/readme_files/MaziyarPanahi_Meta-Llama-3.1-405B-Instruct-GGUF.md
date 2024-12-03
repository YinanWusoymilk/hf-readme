---
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
tags:
- quantized
- 2-bit
- 3-bit
- GGUF
- text-generation
- text-generation
model_name: Meta-Llama-3.1-405B-Instruct-GGUF
base_model: meta-llama/Meta-Llama-3.1-405B-Instruct
inference: false
model_creator: meta-llama
pipeline_tag: text-generation
quantized_by: MaziyarPanahi
license: llama3.1
---
# [MaziyarPanahi/Meta-Llama-3.1-405B-Instruct-GGUF](https://huggingface.co/MaziyarPanahi/Meta-Llama-3.1-405B-Instruct-GGUF)
- Model creator: [meta-llama](https://huggingface.co/meta-llama)
- Original model: [meta-llama/Meta-Llama-3.1-405B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct)

## Description
[MaziyarPanahi/Meta-Llama-3.1-405B-Instruct-GGUF](https://huggingface.co/MaziyarPanahi/Meta-Llama-3.1-405B-Instruct-GGUF) contains GGUF format model files for [meta-llama/Meta-Llama-3.1-405B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct).

## Sample

> llama.cpp/llama-cli -m Meta-Llama-3.1-405B-Instruct.Q2_K.gguf-00001-of-00009.gguf -p "write 10 sentences ending with the word apple." -n 1024 -t 40

```
system_info: n_threads = 40 / 80 | AVX = 1 | AVX_VNNI = 0 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | AVX512_BF16 = 0 | FMA = 1 | NEON = 0 | SVE = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 1 | SSSE3 = 1 | VSX = 0 | MATMUL_INT8 = 0 | LLAMAFILE = 1 |
sampling:
        repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000
        top_k = 40, tfs_z = 1.000, top_p = 0.950, min_p = 0.050, typical_p = 1.000, temp = 0.800
        mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampling order:
CFG -> Penalties -> top_k -> tfs_z -> typical_p -> top_p -> min_p -> temperature
generate: n_ctx = 131072, n_batch = 2048, n_predict = 1024, n_keep = 1


write 10 sentences ending with the word apple.
1. I love to eat a crunchy, juicy apple.
2. The teacher gave the student a shiny, red apple.
3. The farmer plucked a ripe, delicious apple.
4. My favorite snack is a sweet, tasty apple.
5. The child picked a fresh, green apple.
6. The cafeteria served a healthy, sliced apple.
7. The vendor sold a crisp, autumn apple.
8. The artist painted a still life with a golden apple.
9. The baby took a big bite of a soft, mealy apple.
10. The family enjoyed a basket of fresh, orchard apple. [end of text]

llama_print_timings:        load time = 1068588.13 ms
llama_print_timings:      sample time =    2262.60 ms /   136 runs   (   16.64 ms per token,    60.11 tokens per second)
llama_print_timings: prompt eval time =  339484.02 ms /    11 tokens (30862.18 ms per token,     0.03 tokens per second)
llama_print_timings:        eval time = 33458013.45 ms /   135 runs   (247837.14 ms per token,     0.00 tokens per second)
llama_print_timings:       total time = 33800561.08 ms /   146 tokens
Log end
```

### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.

Here is an incomplete list of clients and libraries that are known to support GGUF:

* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for GGUF. Offers a CLI and a server option.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration. Linux available, in beta as of 27/11/2023.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [GPT4All](https://gpt4all.io/index.html), a free and open source local running GUI, supporting Windows, Linux and macOS with full GPU accel.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server. Note, as of time of writing (November 27th 2023), ctransformers has not been updated in a long time and does not support many recent models.

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.