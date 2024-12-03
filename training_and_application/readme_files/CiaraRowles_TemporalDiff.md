---
license: openrail
pipeline_tag: text-to-video
---

TemporalDiff is a finetune of the original AnimateDiff weights on a higher resolution dataset (512x512).

Testing so far indicates a higher level of video coherency than the original weights, i also adjusted the stride from 4 to 2 frames to improve how smooth the motion was.

Current limitations are that the labelling for my dataset was a bit off, so it has slightly reduced ability to interpret the prompt, i'll be releasing a new version that fixes that soon.

This should work the same as any the base model in terms of use, just drag and drop it into comfy ui or the animatediff repository and use as normal. 

This does not require any additional memory to run as the generations were 512x512 before, the training was just done at 256x256.