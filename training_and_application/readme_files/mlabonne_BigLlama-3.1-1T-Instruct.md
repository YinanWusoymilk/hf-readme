---
base_model:
- meta-llama/Meta-Llama-3.1-681B-Instruct
library_name: transformers
tags:
- mergekit
- merge
---

# 🦙✨ BigLlama-3.1-1T-Instruct

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/ywomdgvQYP9cpr-PH1nf7.png)

<center>🦙⛰️ <i><a href="https://huggingface.co/mlabonne/BigLlama-3.1-681B-Instruct">mlabonne/BigLlama-3.1-681B-Instruct</a></i></center>

This is an experimental self-merge using [meta-llama/Meta-Llama-3.1-405B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct) and created with [mergekit](https://github.com/cg123/mergekit).

This is the direct successor of [Meta-Llama-3-120B-Instruct](https://huggingface.co/mlabonne/Meta-Llama-3-120B-Instruct), a self-merge of Llama 3 70B that produced a decent 120B model for tasks like creative writing.

I tweaked the range of duplicated layers to hopefully make a sensible model. Use it at your own risk!

## 🔍 Applications

I recommend using this model for creative writing with the Llama 3 chat template.

## ⚡ Quantization

TBD.

## 🏆 Evaluation

TBD.

## 🧩 Configuration

This model was merged using the passthrough merge method. The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - layer_range: [0, 105]
    model: mlabonne/BigLlama-3.1-681B-Instruct
- sources:
  - layer_range: [52, 157]
    model: mlabonne/BigLlama-3.1-681B-Instruct
- sources:
  - layer_range: [104, 209]
    model: mlabonne/BigLlama-3.1-681B-Instruct
merge_method: passthrough
dtype: bfloat16
```

Here is the code I've used to generate the config and calculate the number of layers/parameters after passthrough:

```python
def generate_yaml_config(range_size, total_layers, nb_parameters):
    new_size = total_layers + total_layers - range_size
    new_param = (nb_parameters / total_layers) * new_size
    print(f"New size = {new_size} layers")
    print(f"New parameters = {new_param:.2f}B")
    yaml_str = "slices:\n"

    for i in range(0, round(total_layers - range_size + 1), range_size // 2):
        start = i
        end = min(start + range_size, total_layers)
        yaml_str += f"- sources:\n"
        yaml_str += f"  - layer_range: [{start}, {end}]\n"
        yaml_str += f"    model: meta-llama/Meta-Llama-3.1-405B-Instruct\n"

    yaml_str += "merge_method: passthrough\n"
    yaml_str += "dtype: bfloat16\n"

    print(yaml_str)

    return new_size, new_param

# Example usage
new_size, new_param = generate_yaml_config(42, 126, 410)
new_size, new_param = generate_yaml_config(105, new_size, new_param)
```