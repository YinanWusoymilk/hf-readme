---
license: apache-2.0
---
# WD 1.4 SwinV2 Tagger V2

Supports ratings, characters and general tags.

Trained using https://github.com/SmilingWolf/SW-CV-ModelZoo.  
TPUs used for training kindly provided by the [TRC program](https://sites.research.google/trc/about/).

## Dataset
Last image id: 5944504  
Trained on Danbooru images with IDs modulo 0000-0899.  
Validated on images with IDs modulo 0950-0999.  
Images with less than 10 general tags were filtered out.  
Tags with less than 600 images were filtered out.

## Validation results
`v2.0: P=R: threshold = 0.3771, F1 = 0.6854`

## What's new
Model v2.1/Dataset v2:  
Re-exported to work around an ONNXRuntime v1.17.1 bug.  
Bumped the minimum ONNXRuntime version to `>= 1.17.0`.  
Now `timm` compatible! Load it up and give it a spin using the canonical one-liner!  
Exported to `msgpack` for compatibility with the [JAX-CV](https://github.com/SmilingWolf/JAX-CV) codebase.  
The batch dimension of the ONNX model is not fixed to 1 anymore. Now you can go crazy with batch inference.  
No change to the trained weights themselves. There might be small prediction discrepancies across frameworks due to implementation details.  

Model v2.0/Dataset v2:  
Initial release.  

# Runtime deps
ONNX model requires `onnxruntime >= 1.17.0`

## Final words
Subject to change and updates.  
Downstream users are encouraged to use tagged releases rather than relying on the head of the repo.
