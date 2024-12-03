---
license: apache-2.0
language:
- en
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: yujiepan/bert-base-uncased-sst2-int8-unstructured80
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE SST2
      type: glue
      config: sst2
      split: validation
      args: sst2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.91284
---

# bert-base-uncased-sst2-unstructured80-int8-ov

 * Model creator: [Google](https://huggingface.co/google-bert)
 * Original model: [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased)

## Description

This model conducts unstructured magnitude pruning, quantization and distillation at the same time on [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) when finetuning on the GLUE SST2 dataset.
It achieves the following results on the evaluation set:
- Torch accuracy: **0.9128**
- OpenVINO IR accuracy: **0.9128**
- Sparsity in transformer block linear layers: **0.80**

The model was converted to the [OpenVINO™ IR](https://docs.openvino.ai/2024/documentation/openvino-ir-format.html) (Intermediate Representation) format with weights compressed to INT8 by [NNCF](https://github.com/openvinotoolkit/nncf).

## Compatibility

The provided OpenVINO™ IR model is compatible with:

* OpenVINO version 2024.3.0 and higher
* Optimum Intel 1.19.0 and higher

## Optimization Parameters

Optimization was performed using `nncf` with the following `nncf_config.json` file:

```
[
    {
        "algorithm": "quantization",
        "preset": "mixed",
        "overflow_fix": "disable",
        "initializer": {
            "range": {
                "num_init_samples": 300,
                "type": "mean_min_max"
            },
            "batchnorm_adaptation": {
                "num_bn_adaptation_samples": 0
            }
        },
        "scope_overrides": {
            "activations": {
                "{re}.*matmul_0": {
                    "mode": "symmetric"
                }
            }
        },
        "ignored_scopes": [
            "{re}.*Embeddings.*",
            "{re}.*__add___[0-1]",
            "{re}.*layer_norm_0",
            "{re}.*matmul_1",
            "{re}.*__truediv__*"
        ]
    },
    {
        "algorithm": "magnitude_sparsity",
        "ignored_scopes": [
            "{re}.*NNCFEmbedding.*",
            "{re}.*LayerNorm.*",
            "{re}.*pooler.*",
            "{re}.*classifier.*"
        ],
        "sparsity_init": 0.0,
        "params": {
            "power": 3,
            "schedule": "polynomial",
            "sparsity_freeze_epoch": 10,
            "sparsity_target": 0.8,
            "sparsity_target_epoch": 9,
            "steps_per_epoch": 2105,
            "update_per_optimizer_step": true
        }
    }
]
```

For more information on optimization, check the [OpenVINO model optimization guide](https://docs.openvino.ai/2024/openvino-workflow/model-optimization.html).

## Running Model Training

1. Install required packages:

```
conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia
pip install optimum[openvino,nncf]
pip install datasets sentencepiece scipy scikit-learn protobuf evaluate
pip install wandb # optional
```

2. Run model training:

```
NNCFCFG=/path/to/nncf_config.json
python run_glue.py \
  --lr_scheduler_type cosine_with_restarts \
  --cosine_lr_scheduler_cycles 11 6 \
  --record_best_model_after_epoch 9 \
  --load_best_model_at_end True \
  --metric_for_best_model accuracy \
  --model_name_or_path textattack/bert-base-uncased-SST-2 \
  --teacher_model_or_path yoshitomo-matsubara/bert-large-uncased-sst2 \
  --distillation_temperature 2 \
  --task_name sst2 \
  --nncf_compression_config $NNCFCFG \
  --distillation_weight 0.95 \
  --output_dir /tmp/bert-base-uncased-sst2-int8-unstructured80 \
  --overwrite_output_dir \
  --run_name bert-base-uncased-sst2-int8-unstructured80 \
  --do_train \
  --do_eval \
  --max_seq_length 128 \
  --per_device_train_batch_size 32 \
  --per_device_eval_batch_size 32 \
  --learning_rate 5e-05 \
  --optim adamw_torch \
  --num_train_epochs 17 \
  --logging_steps 1 \
  --evaluation_strategy steps \
  --eval_steps 250 \
  --save_strategy steps \
  --save_steps 250 \
  --save_total_limit 1 \
  --fp16 \
  --seed 1
```

For more details, refer to the [training configuration and script](https://gist.github.com/yujiepan-work/5d7e513a47b353db89f6e1b512d7c080).

## Usage examples

* [OpenVINO notebooks](https://github.com/openvinotoolkit/openvino_notebooks):
  - [Accelerate Inference of Sparse Transformer Models with OpenVINO™ and 4th Gen Intel® Xeon® Scalable Processors](https://github.com/openvinotoolkit/openvino_notebooks/blob/latest/notebooks/sparsity-optimization/sparsity-optimization.ipynb)

## Limitations

Check the original model card for [limitations](https://huggingface.co/google-bert/bert-base-uncased).

## Legal information

The original model is distributed under [apache-2.0](https://choosealicense.com/licenses/apache-2.0/) license. More details can be found in [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) model card.

## Disclaimer

Intel is committed to respecting human rights and avoiding causing or contributing to adverse impacts on human rights. See [Intel’s Global Human Rights Principles](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/policy-human-rights.pdf). Intel’s products and software are intended only to be used in applications that do not cause or contribute to adverse impacts on human rights.