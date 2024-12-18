---
license: mit
pipeline_tag: feature-extraction
tags:
- bark
- tts
- hubert
- text-to-speech
datasets:
- GitMylo/bark-semantic-training
---
# Bark-voice-cloning
Bark-voice-cloning is a model which processes the outputs from a HuBERT model, and turns them into semantic tokens compatible with bark text to speech.

This can be used for many things, including speech transfer and voice cloning.

[code repo](https://github.com/gitmylo/bark-voice-cloning-HuBERT-quantizer)
[audio webui](https://github.com/gitmylo/audio-webui)

# The models in this repo
* [quantifier_hubert_base_ls960.pth](https://huggingface.co/GitMylo/bark-voice-cloning/blob/main/quantifier_hubert_base_ls960.pth) (the model trained on literature for 4 epochs)
* [quantifier_hubert_base_ls960_14.pth](https://huggingface.co/GitMylo/bark-voice-cloning/blob/main/quantifier_hubert_base_ls960_14.pth) (the model trained on literature for 10 more epochs, based on the previous)
* [quantifier_V1_hubert_base_ls960_23.pth](https://huggingface.co/GitMylo/bark-voice-cloning/blob/main/quantifier_V1_hubert_base_ls960_23.pth) (a larger model, trained for more epochs on the same dataset)

(Please use the model manager from the [code repo](https://github.com/gitmylo/bark-voice-cloning-HuBERT-quantizer) for easy downloading of models)

# Voice cloning
Voice cloning is creating a new voice for text-to-speech.

Process:
1. Load your wav audio file into your pytorch application
2. For the fine prompt extract [discrete representations](https://github.com/facebookresearch/encodec#extracting-discrete-representations). (These are used by bark to know about the voice), **make sure to `.squeeze()` the resulting codes.**
3. For the coarse prompt do `fine_prompt[:2, :]`, to get the coarse prompt from a fine prompt.
4. For the semantics, load a HuBERT model without Kmeans (I personally use the [audiolm-pytorch](https://github.com/lucidrains/audiolm-pytorch) implementation's hubertwithkmeans, but i edited it to skip kmeans.)
5. Next, to get the actual semantic tokens, run the tokens through this model. Your output will be compatible with bark.
6. Save these files in an npz with `numpy.savez(semantic_prompt=semantics, fine_prompt=fine, coarse_prompt=coarse)`. This is your speaker file containing your cloned voice.

# Voice masking
Voice masking is replacing a voice in an audio clip for speech-to-speech.

## Random
Replacing a voice in an audio clip with a voice generated by bark.

process:
1. Extract semantics from the audio clip using HuBERT and this model
2. Run `semantic_to_waveform` from `bark.api` with the extracted semantics
3. The previous step returns the generated audio.

## Transfer
Replacing a voice with a voice from another audio clip.

process:
1. Create a speaker file using the steps under the voice cloning section
2. Extract the semantics from the clip with the text you want spoken
3. Run `semantics_to_waveform` from `bark.api` with the extracted semantics, and the speaker prompt that you created on step 1.
4. The previous step returns the generated audio.

# Disclaimer
I am not responsible for any misuse of this model. I do not agree with cloning people's voices without permission. Please make sure it is appropriate to clone someone's voice before doing so.