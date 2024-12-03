---
license: openrail
datasets:
- ChristophSchuhmann/LAION-5B-EN-Aesthetics-Subset_above_6
---

![banner-large.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1674039767068-62bd5f951e22ec84279820e8.jpeg)

Image Mixer is a model that lets you combine the concepts, styles, and compositions from multiple images (and text prompts too) and generate new images.

It was trained by [Justin Pinkney](https://www.justinpinkney.com) at [Lambda Labs](https://lambdalabs.com/).

## Training details

This model is a fine tuned version of [Stable Diffusion Image Variations](https://huggingface.co/lambdalabs/sd-image-variations-diffusers) 
it has been trained to accept multiple CLIP embedding concatenated along the sequence dimension (as opposed to 1 in the original model). 
During training up to 5 crops of the training images are taken and CLIP embeddings are extracted, these are concatenated and used as the conditioning for the model.
At inference time, CLIP embeddings from multiple images can be used to generate images which are influence by multiple inputs.

Training was done at 640x640 on a subset of LAION improved aesthetics, using 8xA100 from [Lambda GPU Cloud](https://cloud.lambdalabs.com).

_Note text captions were not used during training of the model, 
although input text embeddings works to some extent during inference, the model is primarily designed to accept image embeddings_

## Usage

The model is available on [huggingface spaces](https://huggingface.co/spaces/lambdalabs/image-mixer-demo) or to run locally do the following:

```bash
git clone https://github.com/justinpinkney/stable-diffusion.git
cd stable-diffusion
git checkout 1c8a598f312e54f614d1b9675db0e66382f7e23c
python -m venv .venv --prompt sd
. .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python scripts/gradio_image_mixer.py
```

Then navigate to the gradio demo link printed in the terminal.

For details on how to use the model outside the app refer to the [`run` function](https://github.com/justinpinkney/stable-diffusion/blob/c1963a36a4f8ce23784c8247fa1af0e34e02b766/scripts/gradio_image_mixer.py#L79) in `gradio_image_mixer.py` in the [original repo](https://github.com/justinpinkney/stable-diffusion#image-mixer)