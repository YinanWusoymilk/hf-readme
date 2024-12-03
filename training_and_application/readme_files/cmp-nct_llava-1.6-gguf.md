---
license: apache-2.0
pipeline_tag: image-text-to-text
---
Update: PR is merged, llama.cpp now natively supports these models  
Important: Verify that processing a simple question with any image at least uses 1200 tokens of prompt processing, that shows that the new PR is in use.
If your prompt is just 576 + a few tokens, you are using llava-1.5 code (or projector) and this is incompatible with llava-1.6

**note** Keep in mind the different fine tunes as described in the llama.cpp llava readme, it's essential to use the non defaults for non vicuna models


The mmproj files are the embedded ViT's that came with llava-1.6, I've not compared them but given the previous releases from the team I'd be surprised if the ViT has not been fine tuned this time.
If that's the case, using another ViT can cause issues.  
You need to use the mmproj of the right model but you can mix quantizations.  

Original models: https://github.com/haotian-liu/LLaVA