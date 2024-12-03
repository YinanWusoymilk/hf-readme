---
license: other
license_name: nvidia-open-model-license
license_link: https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf
library_name: nemo
inference: false
fine-tuning: false
tags:
- nvidia
---
## Nemotron-4-340B-Base

[![Model architecture](https://img.shields.io/badge/Model%20Arch-Transformer%20Decoder-green)](#model-architecture)[![Model size](https://img.shields.io/badge/Params-340B-green)](#model-architecture)[![Language](https://img.shields.io/badge/Language-Multilingual-green)](#datasets)



### Model Overview:

Nemotron-4-340B-Base is a large language model (LLM) that can be used as part of a synthetic data generation pipeline to create training data that helps researchers and developers build their own LLMs. This model has 340 billion parameters, and supports a context length of 4,096 tokens. It is pre-trained for a total of 9 trillion tokens, consisting of a diverse assortment of English-based texts, 50+ natural languages and 40+ coding languages.  After an initial pre-training phase of 8 trillion tokens, continuous pre-training of 1 trillion tokens was performed on top of the pre-trained model in order to improve model quality. During continuous pre-training, we altered the data composition by using a different distribution than the one seen at the beginning of training.

Under the NVIDIA Open Model License, NVIDIA confirms: 
- Models are commercially usable. 
- You are free to create and distribute Derivative Models. 
- NVIDIA does not claim ownership to any outputs generated using the Models or Derivative Models


### License: 

[NVIDIA Open Model License](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf)

### Intended use

Nemotron-4-340B-Base is a completion model intended for use in over 50+ natural and 40+ coding languages. It is compatible with [NVIDIA NeMo Framework](https://docs.nvidia.com/nemo-framework/index.html). For best performance on a given task, users are encouraged to customize the model using the NeMo Framework suite of customization tools including Parameter-Efficient Fine-Tuning (P-tuning, Adapters, LoRA, and more), and Model Alignment (SFT, SteerLM, RLHF, and more) using [NeMo-Aligner](https://github.com/NVIDIA/NeMo-Aligner). Refer to the [documentation](https://docs.nvidia.com/nemo-framework/user-guide/latest/llms/nemotron/index.html) for examples.

**Model Developer:** NVIDIA

**Model Dates:** Nemotron-4-340B-Base was trained between December 2023 and May 2024.

### Required Hardware

BF16 Inference:
- 8x H200 (1x H200 node)
- 16x H100 (2x H100 nodes)
- 16x A100 80GB (2x A100 80GB nodes)

### Model Architecture:

Nemotron-4-340B-Base is trained with a global batch-size of 2304, a sequence length of 4096 tokens, uses Grouped-Query Attention (GQA), and Rotary Position Embeddings (RoPE).

**Architecture Type:** Transformer Decoder (auto-regressive language model)

**Network Architecture:**
Nemotron-4

### Usage

Deployment and inference with Nemotron-4-340B-Base can be done in three steps using NeMo Framework:

1. Create a Python script to interact with the deployed model.
2. Create a Bash script to start the inference server.
3. Schedule a Slurm job to distribute the model across 2 nodes and associate them with the inference server.

The first task is for the Python Script.

1. Define the Python script ``call_server.py``

```python
import requests
import json
headers = {"Content-Type": "application/json"}
def text_generation(data, ip='localhost', port=None):
    resp = requests.put(f'http://{ip}:{port}/generate', data=json.dumps(data), headers=headers)
    return resp.json()
def get_generation(prompt, greedy, add_BOS, token_to_gen, min_tokens, temp, top_p, top_k, repetition, batch=False):
    data = {
        "sentences": [prompt] if not batch else prompt,
        "tokens_to_generate": int(token_to_gen),
        "temperature": temp,
        "add_BOS": add_BOS,
        "top_k": top_k,
        "top_p": top_p,
        "greedy": greedy,
        "all_probs": False,
        "repetition_penalty": repetition,
        "min_tokens_to_generate": int(min_tokens),
        "end_strings": ["<|endoftext|>", "<extra_id_1>", "\x11", "<extra_id_1>User"],
    }
    sentences = text_generation(data, port=1424)['sentences']
    return sentences[0] if not batch else sentences
PROMPT_TEMPLATE = "{prompt}"
question = "Write a poem on NVIDIA in the style of Shakespeare"
prompt = PROMPT_TEMPLATE.format(prompt=question)
print(prompt)
response = get_generation(prompt, greedy=True, add_BOS=False, token_to_gen=1024, min_tokens=1, temp=1.0, top_p=1.0, top_k=0, repetition=1.0, batch=False)
response = response[len(prompt):]
print(response)
```


2. Given this Python script, create a Bash script which spins up the inference server within the [NeMo container](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/nemo) (```docker pull nvcr.io/nvidia/nemo:24.05```) and calls the Python script ``call_server.py``. The Bash script ``nemo_inference.sh`` is as follows:


```bash
NEMO_FILE=$1
WEB_PORT=1424
depends_on () {
    HOST=$1
    PORT=$2
    STATUS=$(curl -X PUT http://$HOST:$PORT >/dev/null 2>/dev/null; echo $?)
    while [ $STATUS -ne 0 ]
    do
         echo "waiting for server ($HOST:$PORT) to be up"
         sleep 10
         STATUS=$(curl -X PUT http://$HOST:$PORT >/dev/null 2>/dev/null; echo $?)
    done
    echo "server ($HOST:$PORT) is up running"
}
/usr/bin/python3 /opt/NeMo/examples/nlp/language_modeling/megatron_gpt_eval.py \
        gpt_model_file=$NEMO_FILE \
        pipeline_model_parallel_split_rank=0 \
        server=True tensor_model_parallel_size=8 \
        trainer.precision=bf16 pipeline_model_parallel_size=2 \
        trainer.devices=8 \
        trainer.num_nodes=2 \
        web_server=False \
        port=${WEB_PORT} &
    SERVER_PID=$!
    readonly local_rank="${LOCAL_RANK:=${SLURM_LOCALID:=${OMPI_COMM_WORLD_LOCAL_RANK:-}}}"
    if [ $SLURM_NODEID -eq 0 ] && [ $local_rank -eq 0 ]; then
        depends_on "0.0.0.0" ${WEB_PORT}
        echo "start get json"
        sleep 5
        echo "SLURM_NODEID: $SLURM_NODEID"
        echo "local_rank: $local_rank"
        /usr/bin/python3 /scripts/call_server.py
        echo "clean up dameons: $$"
        kill -9 $SERVER_PID
        pkill python
    fi
    wait
```


3. Launch ``nemo_inference.sh`` with a Slurm script defined like below, which starts a 2-node job for model inference.

```bash
#!/bin/bash
#SBATCH -A SLURM-ACCOUNT
#SBATCH -p SLURM-PARITION
#SBATCH -N 2
#SBATCH -J generation      
#SBATCH --ntasks-per-node=8   
#SBATCH --gpus-per-node=8
set -x
RESULTS=<PATH_TO_YOUR_SCRIPTS_FOLDER>
OUTFILE="${RESULTS}/slurm-%j-%n.out"
ERRFILE="${RESULTS}/error-%j-%n.out"
MODEL=<PATH_TO>/Nemotron-4-340B-Base
CONTAINER="nvcr.io/nvidia/nemo:24.05"
MOUNTS="--container-mounts=<PATH_TO_YOUR_SCRIPTS_FOLDER>:/scripts,MODEL:/model"
read -r -d '' cmd <<EOF
bash /scripts/nemo_inference.sh /model
EOF
srun -o $OUTFILE -e $ERRFILE --container-image="$CONTAINER" $MOUNTS bash -c "${cmd}"
```


### Dataset & Training

The training corpus for Nemotron-4-340B-Base consists of English and multilingual text, as well as code. Our sources cover a variety of document types such as: webpages, dialogue, articles, and other written materials. The corpus spans domains including legal, math, science, finance, and more. In our continued training set, we introduce a small portion of question-answering, and alignment style data to improve model performance.

**Data Freshness:** The pretraining data has a cutoff of June 2023.

### Evaluation Results

#### Overview

*5-shot performance.* Language Understanding evaluated using Massive Multitask Language Understanding:
| Average |
| :------------- |
| 81.1 |

*Zero-shot performance.* Evaluated using select datasets from the LM Evaluation Harness with additions:
| HellaSwag | Winogrande | BBH| ARC-Challenge |
| :------------- | :------------- | :------------- | :------------- |
| 90.53 | 89.50 | 85.44  | 94.28 |

*Chain of Thought (CoT)*. Multilingual capabilities evaluated using Multilingual Grade School Math:

| ES Exact Match (%) | JA Exact Match (%) | TH Exact Match (%) |
| :------------- | :------------- | :------------- |
| 68.8 | 69.6 | 68.4 |

*Code generation performance*. Evaluated using HumanEval:
| p@1, 0-Shot |
| :------------- |
| 57.3 |

### Limitations

The model was trained on data that contains toxic language, unsafe content, and societal biases originally crawled from the internet. Therefore, the model may amplify those biases and return toxic responses especially when prompted with toxic prompts. The model may generate answers that may be inaccurate, omit key information, or include irrelevant or redundant text producing socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive.

### Ethical Considerations

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards [here.](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/nemotron-4-340b-base).  Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/). 