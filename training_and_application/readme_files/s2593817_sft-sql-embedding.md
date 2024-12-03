---
base_model: sentence-transformers/all-mpnet-base-v2
datasets: []
language: []
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:300000
- loss:CoSENTLoss
widget:
- source_sentence: SELECT DISTINCT count(alias3.col1) , alias1.col2 FROM table1 AS
    alias1 JOIN table2 AS alias2 ON alias1.col2 = alias2.col2 JOIN table3 AS alias3
    ON alias1.col1 = alias3.col1 WHERE alias2.col3 = str AND alias3.year = num GROUP
    BY alias1.col2
  sentences:
  - SELECT col1 , avg(col2) FROM table1 WHERE col3 LIKE str GROUP BY col1
  - SELECT col1 , col2 FROM table1 WHERE col3 LIKE str GROUP BY col1 ORDER BY count(*)
    DESC LIMIT num
  - SELECT col1 , avg(col2) FROM table1 GROUP BY col1 ORDER BY avg(col2)
- source_sentence: SELECT alias2.year FROM table1 AS alias1 JOIN table2 AS alias2
    ON alias1.col1 = alias2.col2 WHERE alias1.alias1 = str
  sentences:
  - SELECT alias1.col1 , alias2.col2 FROM table1 AS alias1 JOIN table2 AS alias2 ON
    alias1.col3 = alias2.col3
  - SELECT DISTINCT alias1.col1 FROM table1 AS alias1 JOIN table2 AS alias2 ON alias2.col2
    = alias1.col3 JOIN table3 AS alias3 ON alias2.col4 = alias3.col3 WHERE alias3.col5
    > num
  - SELECT col1 FROM table1 ORDER BY col2 LIMIT num
- source_sentence: SELECT DISTINCT count(alias2.col1) FROM table1 AS alias1 JOIN table2
    AS alias2 ON alias1.col2 = alias2.col2 WHERE alias1.col3 = str
  sentences:
  - SELECT alias3.col1 FROM table1 AS alias1 JOIN table2 AS alias2 ON alias1.col2
    = alias2.col2 JOIN table3 AS alias3 ON alias2.col3 = alias3.col3 WHERE alias1.col4
    = str AND alias1.col5 = str
  - SELECT count(DISTINCT col1) FROM table1 WHERE col1 NOT IN ( SELECT col2 FROM table2
    )
  - SELECT count(*) FROM table1 WHERE col1 = str AND col2 < num
- source_sentence: SELECT alias1.col1 FROM table1 AS alias1 JOIN table2 AS alias2
    ON alias1.col2 = alias2.col2 WHERE alias2.col3 LIKE str
  sentences:
  - SELECT col1 FROM table1 ORDER BY col2 DESC
  - SELECT col1 FROM table1 WHERE col2 NOT IN (SELECT col2 FROM table2)
  - SELECT alias1.col1 , alias1.col2 , alias1.col3 FROM table1 AS alias1 JOIN table2
    AS alias2 ON alias1.col4 = alias2.col5 ORDER BY alias2.col6 LIMIT num
- source_sentence: SELECT alias1.col1 FROM table1 AS alias1 JOIN table2 AS alias2
    ON alias1.col2 = alias2.col2 JOIN table3 AS alias3 ON alias2.col3 = alias3.col3
    WHERE alias3.col4 = str INTERSECT SELECT alias1.col1 FROM table1 AS alias1 JOIN
    table2 AS alias2 ON alias1.col2 = alias2.col2 JOIN table3 AS alias3 ON alias2.col3
    = alias3.col3 WHERE alias3.col4 = str
  sentences:
  - SELECT count(*) FROM table1
  - SELECT count(DISTINCT col1) FROM table1
  - SELECT count(col1) FROM table1 WHERE col2 = num
---

# SentenceTransformer based on sentence-transformers/all-mpnet-base-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) <!-- at revision 84f2bcc00d77236f9e89c8a360a00fb1139bf47d -->
- **Maximum Sequence Length:** 384 tokens
- **Output Dimensionality:** 768 tokens
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 384, 'do_lower_case': False}) with Transformer model: MPNetModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("s2593817/sft-sql-embedding")
# Run inference
sentences = [
    'SELECT alias1.col1 FROM table1 AS alias1 JOIN table2 AS alias2 ON alias1.col2 = alias2.col2 JOIN table3 AS alias3 ON alias2.col3 = alias3.col3 WHERE alias3.col4 = str INTERSECT SELECT alias1.col1 FROM table1 AS alias1 JOIN table2 AS alias2 ON alias1.col2 = alias2.col2 JOIN table3 AS alias3 ON alias2.col3 = alias3.col3 WHERE alias3.col4 = str',
    'SELECT count(col1) FROM table1 WHERE col2 = num',
    'SELECT count(DISTINCT col1) FROM table1',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset


* Size: 300,000 training samples
* Columns: <code>sentence1</code>, <code>sentence2</code>, and <code>score</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence1                                                                          | sentence2                                                                          | score                                                           |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:----------------------------------------------------------------|
  | type    | string                                                                             | string                                                                             | float                                                           |
  | details | <ul><li>min: 8 tokens</li><li>mean: 38.49 tokens</li><li>max: 189 tokens</li></ul> | <ul><li>min: 7 tokens</li><li>mean: 37.44 tokens</li><li>max: 153 tokens</li></ul> | <ul><li>min: 0.04</li><li>mean: 0.36</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence1                                                                                                                                                                                                                                                                                                                                    | sentence2                                                                                                                                                                                                 | score                            |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|
  | <code>SELECT DISTINCT count(DISTINCT alias4.col1) , alias3.col2 FROM table1 AS alias1 JOIN table2 AS alias2 ON alias1.col3 = alias2.col3 JOIN table3 AS alias3 ON alias3.col4 = alias1.col4 JOIN table4 AS alias4 ON alias3.col4 = alias4.col5 WHERE alias2.col6 = str GROUP BY alias3.col2 ORDER BY count(DISTINCT alias4.col1) DESC</code> | <code>SELECT count(*) FROM table1 WHERE col1 = str</code>                                                                                                                                                 | <code>0.14221014492753623</code> |
  | <code>SELECT DISTINCT count(alias2.col1) FROM table1 AS alias1 JOIN table2 AS alias2 ON alias1.col2 = alias2.col2 WHERE alias1.col3 = str</code>                                                                                                                                                                                             | <code>SELECT alias3.col1 FROM table1 AS alias1 JOIN table2 AS alias2 ON alias1.col2 = alias2.col2 JOIN table3 AS alias3 ON alias2.col3 = alias3.col3 WHERE alias1.col4 = str AND alias1.col5 = str</code> | <code>0.5468686868686868</code>  |
  | <code>SELECT count(*) FROM table1</code>                                                                                                                                                                                                                                                                                                     | <code>SELECT count(*) FROM table1 WHERE col1 LIKE str</code>                                                                                                                                              | <code>0.6269230769230769</code>  |
* Loss: [<code>CoSENTLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosentloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "pairwise_cos_sim"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 160
- `learning_rate`: 2e-05
- `num_train_epochs`: 8
- `warmup_ratio`: 0.2
- `fp16`: True
- `dataloader_num_workers`: 16
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 160
- `per_device_eval_batch_size`: 8
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 8
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.2
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: False
- `fp16`: True
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 16
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: False
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch  | Step  | Training Loss |
|:------:|:-----:|:-------------:|
| 0.0533 | 100   | 12.0379       |
| 0.1067 | 200   | 9.2042        |
| 0.16   | 300   | 8.6521        |
| 0.2133 | 400   | 8.5353        |
| 0.2667 | 500   | 8.4472        |
| 0.32   | 600   | 8.4105        |
| 0.3733 | 700   | 8.3927        |
| 0.4267 | 800   | 8.3553        |
| 0.48   | 900   | 8.3326        |
| 0.5333 | 1000  | 8.3168        |
| 0.5867 | 1100  | 8.2941        |
| 0.64   | 1200  | 6.0021        |
| 0.6933 | 1300  | 5.3802        |
| 0.7467 | 1400  | 5.3282        |
| 0.8    | 1500  | 5.2365        |
| 0.8533 | 1600  | 5.0198        |
| 0.9067 | 1700  | 4.899         |
| 0.96   | 1800  | 4.8887        |
| 1.0133 | 1900  | 4.7603        |
| 1.0667 | 2000  | 4.6292        |
| 1.12   | 2100  | 4.4811        |
| 1.1733 | 2200  | 4.2841        |
| 1.2267 | 2300  | 4.2251        |
| 1.28   | 2400  | 4.0261        |
| 1.3333 | 2500  | 3.8628        |
| 1.3867 | 2600  | 3.8404        |
| 1.44   | 2700  | 3.6471        |
| 1.4933 | 2800  | 3.6673        |
| 1.5467 | 2900  | 3.5626        |
| 1.6    | 3000  | 3.5391        |
| 1.6533 | 3100  | 3.5629        |
| 1.7067 | 3200  | 3.4787        |
| 1.76   | 3300  | 3.4401        |
| 1.8133 | 3400  | 3.491         |
| 1.8667 | 3500  | 3.3358        |
| 1.92   | 3600  | 3.3555        |
| 1.9733 | 3700  | 3.161         |
| 2.0267 | 3800  | 3.1708        |
| 2.08   | 3900  | 3.1678        |
| 2.1333 | 4000  | 3.1348        |
| 2.1867 | 4100  | 2.9159        |
| 2.24   | 4200  | 2.8359        |
| 2.2933 | 4300  | 2.8359        |
| 2.3467 | 4400  | 2.796         |
| 2.4    | 4500  | 2.8483        |
| 2.4533 | 4600  | 2.7774        |
| 2.5067 | 4700  | 2.7766        |
| 2.56   | 4800  | 2.7185        |
| 2.6133 | 4900  | 2.778         |
| 2.6667 | 5000  | 2.7114        |
| 2.72   | 5100  | 2.6623        |
| 2.7733 | 5200  | 2.5093        |
| 2.8267 | 5300  | 2.4835        |
| 2.88   | 5400  | 2.2851        |
| 2.9333 | 5500  | 2.1488        |
| 2.9867 | 5600  | 2.2175        |
| 3.04   | 5700  | 2.0813        |
| 3.0933 | 5800  | 2.1489        |
| 3.1467 | 5900  | 2.1337        |
| 3.2    | 6000  | 2.2258        |
| 3.2533 | 6100  | 2.1601        |
| 3.3067 | 6200  | 1.9266        |
| 3.36   | 6300  | 1.8427        |
| 3.4133 | 6400  | 1.8434        |
| 3.4667 | 6500  | 1.917         |
| 3.52   | 6600  | 1.8204        |
| 3.5733 | 6700  | 2.0209        |
| 3.6267 | 6800  | 1.7852        |
| 3.68   | 6900  | 1.9566        |
| 3.7333 | 7000  | 1.852         |
| 3.7867 | 7100  | 1.8562        |
| 3.84   | 7200  | 1.7595        |
| 3.8933 | 7300  | 1.4295        |
| 3.9467 | 7400  | 1.2669        |
| 4.0    | 7500  | 1.2029        |
| 4.0533 | 7600  | 1.3074        |
| 4.1067 | 7700  | 1.435         |
| 4.16   | 7800  | 1.5712        |
| 4.2133 | 7900  | 1.2366        |
| 4.2667 | 8000  | 1.526         |
| 4.32   | 8100  | 1.2565        |
| 4.3733 | 8200  | 1.4546        |
| 4.4267 | 8300  | 1.374         |
| 4.48   | 8400  | 1.3387        |
| 4.5333 | 8500  | 1.3776        |
| 4.5867 | 8600  | 1.3984        |
| 4.64   | 8700  | 1.3577        |
| 4.6933 | 8800  | 1.2393        |
| 4.7467 | 8900  | 1.4125        |
| 4.8    | 9000  | 1.6127        |
| 4.8533 | 9100  | 1.6897        |
| 4.9067 | 9200  | 1.1217        |
| 4.96   | 9300  | 1.406         |
| 5.0133 | 9400  | 1.4641        |
| 5.0667 | 9500  | 1.48          |
| 5.12   | 9600  | 1.3367        |
| 5.1733 | 9700  | 1.4681        |
| 5.2267 | 9800  | 1.4628        |
| 5.28   | 9900  | 1.32          |
| 5.3333 | 10000 | 1.448         |
| 5.3867 | 10100 | 1.2516        |
| 5.44   | 10200 | 1.4421        |
| 5.4933 | 10300 | 1.2542        |
| 5.5467 | 10400 | 1.4545        |
| 5.6    | 10500 | 1.1441        |
| 5.6533 | 10600 | 1.251         |
| 5.7067 | 10700 | 1.3396        |
| 5.76   | 10800 | 1.0305        |
| 5.8133 | 10900 | 1.0155        |
| 5.8667 | 11000 | 0.9871        |
| 5.92   | 11100 | 1.074         |
| 5.9733 | 11200 | 0.4534        |
| 6.0267 | 11300 | 0.1965        |
| 6.08   | 11400 | 0.1822        |
| 6.1333 | 11500 | 0.2101        |
| 6.1867 | 11600 | 0.2326        |
| 6.24   | 11700 | 0.4126        |
| 6.2933 | 11800 | 0.4871        |
| 6.3467 | 11900 | 0.2012        |
| 6.4    | 12000 | 0.2113        |
| 6.4533 | 12100 | 0.1788        |
| 6.5067 | 12200 | 0.2271        |
| 6.56   | 12300 | 0.1685        |
| 6.6133 | 12400 | 0.3347        |
| 6.6667 | 12500 | 0.123         |
| 6.72   | 12600 | 0.155         |
| 6.7733 | 12700 | 0.2476        |
| 6.8267 | 12800 | 0.1926        |
| 6.88   | 12900 | 0.1394        |
| 6.9333 | 13000 | 0.1683        |
| 6.9867 | 13100 | 0.2484        |
| 7.04   | 13200 | 0.1338        |
| 7.0933 | 13300 | 0.1568        |
| 7.1467 | 13400 | 0.1206        |
| 7.2    | 13500 | 0.1683        |
| 7.2533 | 13600 | 0.1831        |
| 7.3067 | 13700 | 0.3077        |
| 7.36   | 13800 | 0.3533        |
| 7.4133 | 13900 | 0.1165        |
| 7.4667 | 14000 | 0.2128        |
| 7.52   | 14100 | 0.236         |
| 7.5733 | 14200 | 0.3616        |
| 7.6267 | 14300 | 0.2989        |
| 7.68   | 14400 | 0.2416        |
| 7.7333 | 14500 | 0.2105        |
| 7.7867 | 14600 | 0.1575        |
| 7.84   | 14700 | 0.224         |
| 7.8933 | 14800 | 0.1593        |
| 7.9467 | 14900 | 0.1293        |
| 8.0    | 15000 | 0.0985        |

</details>

### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 3.0.1
- Transformers: 4.42.4
- PyTorch: 2.3.1+cu121
- Accelerate: 0.33.0
- Datasets: 2.20.0
- Tokenizers: 0.19.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### CoSENTLoss
```bibtex
@online{kexuefm-8847,
    title={CoSENT: A more efficient sentence vector scheme than Sentence-BERT},
    author={Su Jianlin},
    year={2022},
    month={Jan},
    url={https://kexue.fm/archives/8847},
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->