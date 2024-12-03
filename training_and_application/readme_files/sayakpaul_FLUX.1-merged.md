---
language:
- en
library_name: diffusers
license: other
license_name: flux-1-dev-non-commercial-license
license_link: LICENSE.md
base_model:
  - black-forest-labs/FLUX.1-dev
  - black-forest-labs/FLUX.1-schnell
base_model_relation: merge
---
# FLUX.1-merged

This repository provides the merged params for [`black-forest-labs/FLUX.1-dev`](https://huggingface.co/black-forest-labs/FLUX.1-dev)
and [`black-forest-labs/FLUX.1-schnell`](https://huggingface.co/black-forest-labs/FLUX.1-schnell). Please be aware of the licenses of both
the models before using the params commercially. 

<table>
    <thead>
        <tr>
            <th>Dev (50 steps)</th>
            <th>Dev (4 steps)</th>
            <th>Dev + Schnell (4 steps)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <img src="./assets/flux.png" alt="Dev 50 Steps">
            </td>
            <td>
                <img src="./assets/flux_4.png" alt="Dev 4 Steps">
            </td>
            <td>
                <img src="./assets/merged_flux.png" alt="Dev + Schnell 4 Steps">
            </td>
        </tr>
    </tbody>
</table>

## Sub-memory-efficient merging code

```python
from diffusers import FluxTransformer2DModel
from huggingface_hub import snapshot_download
from accelerate import init_empty_weights
from diffusers.models.model_loading_utils import load_model_dict_into_meta
import safetensors.torch
import glob
import torch


with init_empty_weights():
    config = FluxTransformer2DModel.load_config("black-forest-labs/FLUX.1-dev", subfolder="transformer")
    model = FluxTransformer2DModel.from_config(config)

dev_ckpt = snapshot_download(repo_id="black-forest-labs/FLUX.1-dev", allow_patterns="transformer/*")
schnell_ckpt = snapshot_download(repo_id="black-forest-labs/FLUX.1-schnell", allow_patterns="transformer/*")

dev_shards = sorted(glob.glob(f"{dev_ckpt}/transformer/*.safetensors"))
schnell_shards = sorted(glob.glob(f"{schnell_ckpt}/transformer/*.safetensors"))

merged_state_dict = {}
guidance_state_dict = {}

for i in range(len((dev_shards))):
    state_dict_dev_temp = safetensors.torch.load_file(dev_shards[i])
    state_dict_schnell_temp = safetensors.torch.load_file(schnell_shards[i])

    keys = list(state_dict_dev_temp.keys())
    for k in keys:
        if "guidance" not in k:
            merged_state_dict[k] = (state_dict_dev_temp.pop(k) + state_dict_schnell_temp.pop(k)) / 2
        else:
            guidance_state_dict[k] = state_dict_dev_temp.pop(k)

    if len(state_dict_dev_temp) > 0:
        raise ValueError(f"There should not be any residue but got: {list(state_dict_dev_temp.keys())}.")
    if len(state_dict_schnell_temp) > 0:
        raise ValueError(f"There should not be any residue but got: {list(state_dict_dev_temp.keys())}.")

merged_state_dict.update(guidance_state_dict)
load_model_dict_into_meta(model, merged_state_dict)

model.to(torch.bfloat16).save_pretrained("merged-flux")
```

## Inference code

```python
from diffusers import FluxPipeline
import torch

pipeline = FluxPipeline.from_pretrained(
    "sayakpaul/FLUX.1-merged", torch_dtype=torch.bfloat16
).to("cuda")
image = pipeline(
    prompt="a tiny astronaut hatching from an egg on the moon",
    guidance_scale=3.5,
    num_inference_steps=4,
    height=880,
    width=1184,
    max_sequence_length=512,
    generator=torch.manual_seed(0),
).images[0]
image.save("merged_flux.png")
```

## Documentation

* https://huggingface.co/docs/diffusers/main/en/api/pipelines/flux
* https://huggingface.co/docs/diffusers/main/en/api/models/flux_transformer