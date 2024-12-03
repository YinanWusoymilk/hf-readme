---
license: other
license_name: nvidia-open-model-license
license_link: https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf
library_name: nemo
language:
- en
inference: false
fine-tuning: false
tags:
- nvidia
- steerlm
- reward model
datasets:
- nvidia/HelpSteer2
---


## Nemotron-4-340B-Reward

[![Model architecture](https://img.shields.io/badge/Model%20Arch-Transformer%20Decoder-green)](#model-architecture)[![Model size](https://img.shields.io/badge/Params-340B-green)](#model-architecture)[![Language](https://img.shields.io/badge/Language-English-green)](#datasets)


### Model Overview

The Nemotron-4-340B-Reward is a multi-dimensional Reward Model that can be used as part of a synthetic data generation pipeline to create training data that helps researchers and developers build their own LLMs; Nemotron-4-340B-Reward consists of the Nemotron-4-340B-Base model and a linear layer that converts the final layer representation of the end-of-response token into five scalar values, each corresponding to a [HelpSteer2](https://arxiv.org/abs/2406.08673) attribute. 

Try it for free at [build.nvidia.com](https://build.nvidia.com/nvidia/nemotron-4-340b-reward) - comes with an OpenAI-compatible API interface!

It supports a context length of up to 4,096 tokens.

Given a conversation with multiple turns between user and assistant, it rates the following attributes (typically between 0 and 4) for every assistant turn.

1. **Helpfulness**: Overall helpfulness of the response to the prompt.
2. **Correctness**: Inclusion of all pertinent facts without errors. 
3. **Coherence**: Consistency and clarity of expression. 
4. **Complexity**: Intellectual depth required to write response (i.e. whether the response can be written by anyone with basic language competency or requires deep domain expertise).
5. **Verbosity**: Amount of detail included in the response, relative to what is asked for in the prompt.

Nonetheless, if you are only interested in using it as a conventional reward model that outputs a singular scalar, we recommend using the weights ```[0, 0, 0, 0, 0.3, 0.74, 0.46, 0.47, -0.33]``` to do elementwise multiplication with the predicted attributes (which outputs 9 float values in line with [Llama2-13B-SteerLM-RM](https://huggingface.co/nvidia/Llama2-13B-SteerLM-RM) but the first four are not trained or used)

Under the NVIDIA Open Model License, NVIDIA confirms: 

* Models are commercially usable. 
* You are free to create and distribute Derivative Models. 
* NVIDIA does not claim ownership to any outputs generated using the Models or Derivative Models.

### License: 

[NVIDIA Open Model License](https://developer.download.nvidia.com/licenses/nvidia-open-model-license-agreement-june-2024.pdf)

### Intended use

Nemotron-4 340B Reward Model is a pretrained Reward Model intended for use in English Synthetic Data Generation and English Reinforcement Learning from AI Feedback (RLAIF).

Nemotron-4 340B-Reward can be used in the alignment stage to align pretrained models to human preferences. It can also be used in cases like Reward-Model-as-a-Judge.

**Model Developer:** NVIDIA

**Model Input:** Text only  
**Input Format:**  String  

**Model Output:** Scalar Values (List of 9 Floats)  
**Output Format:**  Float  

**Model Dates:** Nemotron-4-340B-Reward was trained between December 2023 and May 2024

**Data Freshness:** The pretraining data has a cutoff of June 2023

### Required Hardware

BF16 Inference:
- 16x H100 (2x H100 Nodes)
- 16x A100 (2x A100 80GB Nodes)

### Usage:

You can use the model with [NeMo Aligner](https://github.com/NVIDIA/NeMo-Aligner) following [SteerLM training user guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/modelalignment/steerlm.html).

1. Spin up an inference server within the NeMo container (`docker pull nvcr.io/nvidia/nemo:24.01.framework`)

```
python /opt/NeMo-Aligner/examples/nlp/gpt/serve_reward_model.py \
      rm_model_file=Nemotron-4-340B-Reward \
      trainer.num_nodes=2 \
      trainer.devices=8 \
      ++model.tensor_model_parallel_size=8 \
      ++model.pipeline_model_parallel_size=2 \
      inference.micro_batch_size=2 \
      inference.port=1424
```

2. Annotate data files using the served reward model. As an example, this can be the Open Assistant train/val files. Then follow the next step to train a SteerLM model based on [SteerLM training user guide](https://docs.nvidia.com/nemo-framework/user-guide/latest/modelalignment/steerlm.html#step-5-train-the-attribute-conditioned-sft-model) .

Please note that this script rounds the predicted floats to the nearest int (between 0 and 4 inclusive), as it's meant for SteerLM training. 
For other use cases (e.g. reward bench measurement, response filtering/ranking), we recommend using the floats directly, which can be done by commenting out [two lines of code in NeMo-Aligner](https://github.com/NVIDIA/NeMo-Aligner/blob/main/examples/nlp/data/steerlm/attribute_annotate.py#L139-140)

```
python /opt/NeMo-Aligner/examples/nlp/data/steerlm/preprocess_openassistant_data.py --output_directory=data/oasst

python /opt/NeMo-Aligner/examples/nlp/data/steerlm/attribute_annotate.py \
      --input-file=data/oasst/train.jsonl \
      --output-file=data/oasst/train_labeled.jsonl \
      --port=1424
```

3. Alternatively, this can be any conversational data file (in .jsonl) in the following format, where each line looks like 

```
{
    "conversations": [
              {"value": <user_turn_1>, "from": "User", "label": None},
              {"value": <assistant_turn_1>, "from": "Assistant", "label": <formatted_label_1>},
              {"value": <user_turn_2>, "from": "User", "label": None},
              {"value": <assistant_turn_2>, "from": "Assistant", "label": <formatted_label_2>},
          ],
    "mask": "User"
}
```

Ideally, each ```<formatted_label_n>``` refers to the ground truth label for the assistant turn but if they are not available, we can also use ```helpfulness:4,correctness:4,coherence:4,complexity:2,verbosity:2``` (i.e. defaulting to moderate complexity and verbosity, adjust if needed. or simply ```helpfulness:-1```. It must not be ```None``` or an empty string.


### Model Architecture:

Nemotron-4-340B-Reward is extended from Nemotron-4-340B-Base with an additional linear layer. It was trained with a global batch-size of 128. 

**Architecture Type:** Transformer Decoder (auto-regressive language model)

### Intended use

Nemotron-4-340B-Reward is a pretrained Reward Model intended for use in English Synthetic Data Generation and English Reinforcement Learning from AI Feedback (RLAIF).

### Dataset & Training

Nemotron-4-340B-Reward was trained for 2 epochs using the NVIDIA [HelpSteer2](https://arxiv.org/abs/2406.08673) data. The HelpSteer2 dataset is a permissively licensed preference dataset (CC-by-4.0) with ten thousand English response pairs and can be found [here](https://huggingface.co/datasets/nvidia/HelpSteer2).

### Evaluation Results

#### Reward Bench Primary Dataset

Evaluated using RewardBench - as introduced in the paper [RewardBench: Evaluating Reward Models for Language Modeling](https://arxiv.org/abs/2403.13787).

| Overall | Chat | Chat-Hard | Safety | Reasoning |
| --------- | ------- | -------------- | --------- | -------------- |
|  92.0 | 95.8 | 87.1 | 91.5 | 93.7 | 


### Limitations

This model was trained using an English dataset, and as such its use is optimized for English language use cases. In order to extend this model to other language domains, fine-tuning will be required.

### Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse. For more detailed information on ethical considerations for this model, please see the Model Card++ Explainability, Bias, Safety & Security, and Privacy Subcards [here](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/nemotron-4-340b-reward). Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).   


### Citation

If you find this model useful, please cite the following works

```bibtex
@misc{wang2024helpsteer2,
      title={HelpSteer2: Open-source dataset for training top-performing reward models}, 
      author={Zhilin Wang and Yi Dong and Olivier Delalleau and Jiaqi Zeng and Gerald Shen and Daniel Egert and Jimmy J. Zhang and Makesh Narsimhan Sreedhar and Oleksii Kuchaiev},
      year={2024},
      eprint={2406.08673},
      archivePrefix={arXiv},
      primaryClass={id='cs.CL' full_name='Computation and Language' is_active=True alt_name='cmp-lg' in_archive='cs' is_general=False description='Covers natural language processing. Roughly includes material in ACM Subject Class I.2.7. Note that work on artificial languages (programming languages, logics, formal systems) that does not explicitly address natural-language issues broadly construed (natural-language processing, computational linguistics, speech, text retrieval, etc.) is not appropriate for this area.'}
}
```