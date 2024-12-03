---
license: llama3.1
base_model: meta-llama/Meta-Llama-3.1-8B-Instruct
pipeline_tag: text-generation
tags:
- text-generation-inference
---


> [!NOTE]
> This is a model that is assumed to perform well, but may require more testing and user feedback. Be aware, only models featured within the GUI of GPT4All, are curated and officially supported by Nomic. Use at your own risk.



# About

<!-- ### quantize_version: 3 -->
<!-- ### convert_type: hf -->

<!-- ### quantize_version: 3 -->
<!-- ### convert_type: hf -->

Model converted and quantized by: [3Simplex](https://huggingface.co/3Simplex).<br>
GPT4All v3.1.1 required.  

![image/png](https://cdn-uploads.huggingface.co/production/uploads/645e666bb5c9a8666d0d99c5/9T9q6k90ZGa5EJKeSMbru.png)


## Prompt Template

```
<|start_header_id|>system<|end_header_id|>

{system_prompt}<|eot_id|>
```

```
<|start_header_id|>user<|end_header_id|>

{user_input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{assistant_response}
```

## 128k Context Length
"llama.context_length": 131072