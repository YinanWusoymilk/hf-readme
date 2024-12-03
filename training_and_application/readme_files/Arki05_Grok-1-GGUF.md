---
license: apache-2.0
---
# Grok-1 GGUF Quantizations

This repository contains unofficial GGUF Quantizations of Grok-1, compatible with `llama.cpp` as of [PR- Add grok-1 support #6204](https://github.com/ggerganov/llama.cpp/pull/6204).

## Updates

#### Native Split Support in llama.cpp
- The splits have been updated to utilize the improvements from [PR: llama_model_loader: support multiple split/shard GGUFs](https://github.com/ggerganov/llama.cpp/pull/6187). As a result, manual merging with `gguf-split` is no longer required.

  With this, there is no need to merge the split files before use. Just download all splits and run llama.cpp with the first split like you would previously. It'll detect the other splits and load them as well.

#### Direct Split Download from huggingface using llama.cpp
- Thanks to a new PR [common: llama_load_model_from_url split support  #6192](https://github.com/ggerganov/llama.cpp/pull/6192) from phymbert it's now possible load model splits from url.

  That means this downloads and runs the model:

```
server \
    --hf-repo Arki05/Grok-1-GGUF \
    --hf-file grok-1-IQ3_XS-split-00001-of-00009.gguf \
    --model models/grok-1-IQ3_XS-split-00001-of-00009.gguf \
    -ngl 999
```

And that is very cool (@phymbert)


## Available Quantizations

The following Quantizations are currently available for download:

| Quant    | Split Files | Size     |
|----------|-------------|----------|
| `Q2_K`   | [1-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q2_K-split-00001-of-00009.gguf), [2-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q2_K-split-00002-of-00009.gguf), [3-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q2_K-split-00003-of-00009.gguf), [4-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q2_K-split-00004-of-00009.gguf), [5-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q2_K-split-00005-of-00009.gguf), [6-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q2_K-split-00006-of-00009.gguf), [7-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q2_K-split-00007-of-00009.gguf), [8-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q2_K-split-00008-of-00009.gguf), [9-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q2_K-split-00009-of-00009.gguf) | 112.4 GB |
| `IQ3_XS` | [1-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-IQ3_XS-split-00001-of-00009.gguf), [2-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-IQ3_XS-split-00002-of-00009.gguf), [3-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-IQ3_XS-split-00003-of-00009.gguf), [4-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-IQ3_XS-split-00004-of-00009.gguf), [5-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-IQ3_XS-split-00005-of-00009.gguf), [6-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-IQ3_XS-split-00006-of-00009.gguf), [7-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-IQ3_XS-split-00007-of-00009.gguf), [8-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-IQ3_XS-split-00008-of-00009.gguf), [9-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-IQ3_XS-split-00009-of-00009.gguf) | 125.4 GB |
| `Q4_K`   | [1-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q4_K-split-00001-of-00009.gguf), [2-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q4_K-split-00002-of-00009.gguf), [3-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q4_K-split-00003-of-00009.gguf), [4-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q4_K-split-00004-of-00009.gguf), [5-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q4_K-split-00005-of-00009.gguf), [6-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q4_K-split-00006-of-00009.gguf), [7-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q4_K-split-00007-of-00009.gguf), [8-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q4_K-split-00008-of-00009.gguf), [9-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q4_K-split-00009-of-00009.gguf) | 186.0 GB |
| `Q6_K`   | [1-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q6_K-split-00001-of-00009.gguf), [2-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q6_K-split-00002-of-00009.gguf), [3-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q6_K-split-00003-of-00009.gguf), [4-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q6_K-split-00004-of-00009.gguf), [5-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q6_K-split-00005-of-00009.gguf), [6-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q6_K-split-00006-of-00009.gguf), [7-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q6_K-split-00007-of-00009.gguf), [8-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q6_K-split-00008-of-00009.gguf), [9-of-9](https://huggingface.co/Arki05/Grok-1-GGUF/resolve/main/grok-1-Q6_K-split-00009-of-00009.gguf) | 259.8 GB |

I would recommend the `IQ3_XS` version for now.

*More Quantizations will be uploaded soon. All current Quants are created without any importance matrix.*