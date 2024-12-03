# BERT with Flash-Attention
### Installing dependencies
To run the model on GPU, you need to install Flash Attention. 
You may either install from pypi (which may not work with fused-dense), or from source.
To install from source, clone the GitHub repository:
```console
git clone git@github.com:Dao-AILab/flash-attention.git
```
The code provided here should work with commit `43950dd`.
Change to the cloned repo and install:
```console
cd flash-attention && python setup.py install
```
This will compile the flash-attention kernel, which will take some time.

If you would like to use fused MLPs (e.g. to use activation checkpointing),
you may install fused-dense also from source:
```console
cd csrc/fused_dense_lib && python setup.py install
```


### Configuration
The config adds some new parameters:
- `use_flash_attn`: If `True`, always use flash attention. If `None`, use flash attention when GPU is available. If `False`, never use flash attention (works on CPU).
- `window_size`: Size (left and right) of the local attention window. If `(-1, -1)`, use global attention
- `dense_seq_output`: If true, we only need to pass the hidden states for the masked out token (around 15%) to the classifier heads. I set this to true for pretraining.
- `fused_mlp`: Whether to use fused-dense. Useful to reduce VRAM in combination with activation checkpointing
- `mlp_checkpoint_lvl`: One of `{0, 1, 2}`. Increasing this increases the amount of activation checkpointing within the MLP. Keep this at 0 for pretraining and use gradient accumulation instead. For embedding training, increase this as much as needed.
- `last_layer_subset`: If true, we only need the compute the last layer for a subset of tokens. I left this to false.
- `use_qk_norm`: Whether or not to use QK-normalization
- `num_loras`: Number of LoRAs to use when initializing a `BertLoRA` model. Has no effect on other models.

