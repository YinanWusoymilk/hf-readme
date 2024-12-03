---
license: apache-2.0
language:
- en
tags:
  - pretrained
  - text-to-speech
library_name: metavoice
inference: false
---

MetaVoice-1B is a 1.2B parameter base model trained on 100K hours of speech for TTS (text-to-speech). It has been built with the following priorities:
* Emotional speech rhythm and tone in English. No hallucinations.
* Support for voice cloning with finetuning.
  * We have had success with as little as 1 minute training data for Indian speakers.
* Zero-shot cloning for American & British voices, with 30s reference audio.
* Support for long-form synthesis.

We’re releasing MetaVoice-1B under the Apache 2.0 license, *it can be used without restrictions*.

## Usage
See [Github](https://github.com/metavoiceio/metavoice-src) for the latest usage instructions.

## Finetuning

See [Github](https://github.com/metavoiceio/metavoice-src?tab=readme-ov-file#finetuning) for the latest finetuning instructions.

## Soon
- Long form / arbitrary length TTS
- Streaming

## Architecture
We predict EnCodec tokens from text, and speaker information. This is then diffused up to the waveform level, with post-processing applied to clean up the audio.

* We use a causal GPT to predict the first two hierarchies of EnCodec tokens. Text and audio are part of the LLM context. Speaker information is passed via conditioning at the token embedding layer. This speaker conditioning is obtained from a separately trained speaker verification network.
  - The two hierarchies are predicted in a "flattened interleaved" manner, we predict the first token of the first hierarchy, then the first token of the second hierarchy, then the second token of the first hierarchy, and so on.
  - We use condition-free sampling to boost the cloning capability of the model.
  - The text is tokenised using a custom trained BPE tokeniser with 512 tokens.
  - Note that we've skipped predicting semantic tokens as done in other works, as we found that this isn't strictly necessary.
* We use a non-causal (encoder-style) transformer to predict the rest of the 6 hierarchies from the first two hierarchies. This is a super small model (~10Mn parameters), and has extensive zero-shot generalisation to most speakers we've tried. Since it's non-causal, we're also able to predict all the timesteps in parallel.
* We use multi-band diffusion to generate waveforms from the EnCodec tokens. We noticed that the speech is clearer than using the original RVQ decoder or VOCOS. However, the diffusion at waveform level leaves some background artifacts which are quite unpleasant to the ear. We clean this up in the next step.
* We use DeepFilterNet to clear up the artifacts introduced by the multi-band diffusion. 

## Optimizations
The model supports: 
1. KV-caching via Flash Decoding 
2. Batching (including texts of different lengths)