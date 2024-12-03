---
license: apache-2.0
---
This is a first version of recreating roneneldan/TinyStories-1M but using Llama architecture.

* Full training process is included in the notebook train.ipynb. Recreating it as simple as downloading 
TinyStoriesV2-GPT4-train.txt and TinyStoriesV2-GPT4-valid.txt in the same folder with the notebook and running
the cells. Validation content is not used by the script so you put anythin in 

* Backup directory has a script do_backup that I used to copy weights from remote machine to local.
Weight are generated too quickly, so by the time script copied weihgt N+1 

* This is extremely PoC version. Training truncates stories that are longer than context size and doesn't use
any sliding window to train story not from the start

* Training took approximately 9 hours (3 hours per epoch) on 40GB A100. ~30GB VRAM was used

* I use tokenizer from open_llama_3b. However I had troubles with it locally(https://github.com/openlm-research/open_llama/issues/69).
I had no troubles on the cloud machine with preninstalled libraries.

* Demo script is demo.py

* Validation script is provided: valid.py. use it like `python valid.py path/to/TinyStoriesV2-GPT4-valid.txt [optional-model-id-or-path]`:
After training I decided that it's not necessary to beat validation into chunks

* Also this version uses very stupid caching mechinsm to shuffle stories for training: it keeps cache of N recently loaded chunks
so if random shuffle asks for a story, it may use cache or load chunk. 
Training dataset is too small, so in next versions I will get rid of it.


from transformers import AutoModelForCausalLM, AutoTokenizer
