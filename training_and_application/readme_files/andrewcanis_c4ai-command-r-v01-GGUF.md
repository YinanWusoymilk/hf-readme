---
license: cc-by-nc-4.0
---

# Command-R 35B v1.0 - GGUF
- Model creator: [CohereForAI](https://huggingface.co/CohereForAI)
- Original model: [Command-R 35B v1.0](https://huggingface.co/CohereForAI/c4ai-command-r-v01)

<!-- description start -->
## Description

This repo contains llama.cpp GGUF format model files for
[Command-R 35B v1.0](https://huggingface.co/CohereForAI/c4ai-command-r-v01).

<!-- compatibility_gguf start -->
## Compatibility

These quantised GGUF files are compatible with llama.cpp from Mar 16, 2024 onwards,
starting from release [b2440](https://github.com/ggerganov/llama.cpp/releases/tag/b2440)

## F16 files are split and require joining

**Note:** Hugging face does not support uploading files larger than 50GB so
I uploaded the GGUF as 2 split files.

To join the files, run the following:

Linux and macOS:
```
cat c4ai-command-r-v01-f16.gguf-split-* > c4ai-command-r-v01-f16.gguf
```
Then you can remove the split files to save space:
```
rm c4ai-command-r-v01-f16.gguf-split-*
```
Windows command line:
```
COPY /B c4ai-command-r-v01-f16.gguf-split-a + c4ai-command-r-v01-f16.gguf-split-b c4ai-command-r-v01-f16.gguf
```

Then you can remove the split files to save space:
```
del c4ai-command-r-v01-f16.gguf-split-a c4ai-command-r-v01-f16.gguf-split-b
```

You can optionally confirm the checksum of merged c4ai-command-r-v01-f16.gguf
with the md5sum file:
```
md5sum -c md5sum
```
