---
base_model:
- nothingiisreal/MN-12B-Celeste-V1.9
- intervitens/mini-magnum-12b-v1.1
library_name: transformers
tags:
- mergekit
- merge
license: cc-by-nc-nd-4.0
---
**UPD: this model series is succeeded by [EVA](https://huggingface.co/EVA-UNIT-01/EVA-Qwen2.5-14B-v0.1)**<br>
**Unprivated, to store for historical reasons** <br>
*There's not much point in those merges, Celeste 70B 0.1 pretty much melded Celeste's and Magnum's datasets anyway*<br>
*To be continued, but on a different base, under a different name, and actually trained this time, without shortcuts*<br><br>
# MN-12B-Starcannon-v2

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit). Turned out to be a bit more Magnum-esque, but still is very creative, and writing style is pretty nice, even if some slop words appear time to time. Might be a good fit for people wanting more variety than Magnum has, and more verbose prose than Celeste v1.9 has.
<br><br>
[Dynamic FP8](https://huggingface.co/aetherwiing/MN-12B-Starcannon-v2-fp8-dynamic) <br>
[Static GGUF (by Mradermacher)](https://huggingface.co/mradermacher/MN-12B-Starcannon-v2-GGUF) <br>
[EXL2 (by kingbri of RoyalLab)](https://huggingface.co/royallab/MN-12B-Starcannon-v2-exl2)
## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [nothingiisreal/MN-12B-Celeste-V1.9](https://huggingface.co/nothingiisreal/MN-12B-Celeste-V1.9) as a base.

### Merge fodder

The following models were included in the merge:
* [nothingiisreal/MN-12B-Celeste-V1.9](https://huggingface.co/nothingiisreal/MN-12B-Celeste-V1.9)
* [intervitens/mini-magnum-12b-v1.1](https://huggingface.co/intervitens/mini-magnum-12b-v1.1)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
    - model: intervitens/mini-magnum-12b-v1.1
      parameters:
        density: 0.3
        weight: 0.5
    - model: nothingiisreal/MN-12B-Celeste-V1.9
      parameters:
        density: 0.7
        weight: 0.5

merge_method: ties
base_model: nothingiisreal/MN-12B-Celeste-V1.9
parameters:
    normalize: true
    int8_mask: true
dtype: bfloat16

```