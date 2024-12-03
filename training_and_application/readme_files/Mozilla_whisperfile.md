---
license: apache-2.0
license_link: LICENSE
tags:
- llamafile
---

# OpenAI Whisper - llamafile

Whisperfile is a high-performance implementation of [OpenAI's
Whisper](https://github.com/openai/whisper) created by Mozilla Ocho as
part of the [llamafile](https://github.com/Mozilla-Ocho/llamafile)
project, based on the
[whisper.cpp](https://github.com/ggerganov/whisper.cpp) software written
by Georgi Gerganov, et al.

- Model creator: [OpenAI](https://huggingface.co/collections/openai/whisper-release-6501bba2cf999715fd953013)
- Original models: [openai/whisper-release](https://huggingface.co/collections/openai/whisper-release-6501bba2cf999715fd953013)
- Origin of quantized weights: [ggerganov/whisper.cpp](https://huggingface.co/ggerganov/whisper.cpp)

The model is packaged into executable weights, which we call
[whisperfiles](https://github.com/Mozilla-Ocho/llamafile/blob/0.8.13/whisper.cpp/doc/index.md).
This makes it easy to use the model on Linux, MacOS, Windows, FreeBSD,
OpenBSD, and NetBSD for AMD64 and ARM64.

## Quickstart

Running the following on a desktop OS will transcribe the speech of a
wav/mp3/ogg/flac file into text. The `-pc` flag enables confidence color
coding.

```
wget https://huggingface.co/Mozilla/whisperfile/resolve/main/whisper-tiny.en.llamafile
wget https://huggingface.co/Mozilla/whisperfile/resolve/main/raven_poe_64kb.mp3
chmod +x whisper-tiny.en.llamafile
./whisper-tiny.en.llamafile -f raven_poe_64kb.mp3 -pc
```

![screenshot](screenshot.png)

There's also an HTTP server available:

```
./whisper-tiny.en.llamafile
```

You can also read the man page:

```
./whisper-tiny.en.llamafile --help
```

Having **trouble?** See the ["Gotchas"
section](https://github.com/mozilla-ocho/llamafile/?tab=readme-ov-file#gotchas-and-troubleshooting)
of the llamafile README.

## GPU Acceleration

The following flags are available to enable GPU support:

- `--gpu nvidia`
- `--gpu metal`
- `--gpu amd`

The medium and large whisperfiles contain prebuilt dynamic shared
objects for Linux and Windows. If you download one of the other models,
then you'll need to install the CUDA or ROCm SDK and pass `--recompile`
to build a GGML CUDA module for your system.

On Windows, only the graphics card driver needs to be installed if you
own an NVIDIA GPU. On Windows, if you have an AMD GPU, you should
install the ROCm SDK v6.1 and then pass the flags `--recompile --gpu
amd` the first time you run your llamafile.

On NVIDIA GPUs, by default, the prebuilt tinyBLAS library is used to
perform matrix multiplications. This is open source software, but it
doesn't go as fast as closed source cuBLAS. If you have the CUDA SDK
installed on your system, then you can pass the `--recompile` flag to
build a GGML CUDA library just for your system that uses cuBLAS. This
ensures you get maximum performance.

For further information, please see the [llamafile
README](https://github.com/mozilla-ocho/llamafile/).

## Documentation

See the [whisperfile
documentation](https://github.com/Mozilla-Ocho/llamafile/blob/6287b60/whisper.cpp/doc/index.md)
for tutorials and further details.
