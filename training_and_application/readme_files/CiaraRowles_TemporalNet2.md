---
license: openrail
tags:
- controlnet
- stable-diffusion
- diffusers
base_model: runwayml/stable-diffusion-v1-5
---
Introducing TemporalNet2

TemporalNet was a ControlNet model designed to enhance the temporal consistency of generated outputs

TemporalNet 2 is an evolution on the concept, where the generated outputs are guided by both the last frame *and* an optical flow map between the frames, improving generation consistency.

This took some modification of the original controlnet code so you'll have to do some extra things. If you just want to run a gradio example or look at the modified controlnet code,
that's here: https://github.com/CiaraStrawberry/TemporalNet  Just drop the model from this directory into that model folder and make sure the gradio_temporalnet.py script points at the model.

To use with stable diffusion, you can either use it with TemporalKit by moving to the branch here after following steps 1 and 2: https://github.com/CiaraStrawberry/TemporalKit/tree/TemporalNet , or use it just by accessing the base api through the temporalvideo.py script: 

1) move your controlnet webui install to this branch: https://github.com/CiaraStrawberry/sd-webui-controlnet-TemporalNet-API

2) Add the model to your models folder in the ControlNet extension in Automatic1111's Web UI.

3) Check you have:

- A folder named "Input_Images" with the input frames
- A PNG file called "init.png" that is pre-stylized in your desired style
- The "temporalvideo.py" script

4) Customize the "temporalvideo.py" script according to your preferences, such as the image resolution, prompt, and control net settings.

5) Launch Automatic1111's Web UI with the --api setting enabled.

6) Execute the Python script.

*Please note that the "init.png" image will not significantly influence the style of the output video. Its primary purpose is to prevent a drastic change in aesthetics during the first few frames.*

Also, I highly recommend you use this in conjunction with the hed model, the settings are already in the script.

ToDo:

Write an Extension for the web ui.

Write a feature that automatically generates an "init.png" image if none is provided.

 ̶C̶h̶a̶n̶g̶e̶ ̶t̶h̶e̶ ̶e̶x̶t̶e̶n̶s̶i̶o̶n̶ ̶t̶o̶ ̶.̶s̶a̶f̶e̶t̶e̶n̶s̶o̶r̶s̶ ̶a̶n̶d̶ ̶i̶n̶v̶e̶s̶t̶i̶g̶a̶t̶e̶ ̶c̶o̶m̶p̶r̶e̶s̶s̶i̶o̶n̶.̶
