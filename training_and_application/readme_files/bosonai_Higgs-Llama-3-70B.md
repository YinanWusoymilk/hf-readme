---
license: other
base_model: meta-llama/Meta-Llama-3-70B
---
# Higgs-Llama-3-70B

Higgs-Llama-3-70B is post-trained from [meta-llama/Meta-Llama-3-70B](https://huggingface.co/meta-llama/Meta-Llama-3-70B), specially tuned for role-playing while being competitive in general-domain instruction-following and reasoning.

We perform supervised fine-tuning with our in-house instruction-following and chat datasets. Afterwards, we construct preference pairs with a semi-automated pipeline that relies on both human-labelers and our private LLMs.
We conduct iterative preference optimization to align the model. During alignment, we adopted a special strategy to align the model’s behavior with the system message.
Compared with other instruct models, Higgs models follow their roles more closely.

See our [release blog](https://boson.ai/higgs-opensource/).

## Evaluation

All benchmarks lead to eventual overfitting, including those for LLMs. Training on data, particularly beneficial for benchmarks typically does not improve (or even worsen) role-playing performance. We worked to exclude benchmark data, including their training examples, from our fine-tuning data.

We highlight our results on two new and challenging benchmarks: [MMLU-Pro](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro) and [Arena-Hard](https://github.com/lm-sys/arena-hard-auto). MMLU-Pro extends the popular MMLU benchmark. We believe that it suffers from less overfitting by other released models as well, as it was released only recently (it was released after our models finished training).

### MMLU-Pro

<table class="col-12 col-md-6" width="100px">
  <tr>
    <td><b>Model</b></td>
    <td><b>MMLU-Pro</b></td>
  </tr>
  <tr>
    <td>GPT-4o</td>
    <td>72.6</td>
  </tr>
  <tr>
    <td>Gemini-1.5-Pro</td>
    <td>69.0</td>
  </tr>
  <tr>
    <td>Claude-3-Opus</td>
    <td>68.5</td>
  </tr>
  <tr>
    <td>GPT-4-Turbo</td>
    <td>63.7</td>
  </tr>
  <tr style="font-weight: bold">
    <td>Higgs-Llama-3-70B</td>
    <td>63.2</td>
  </tr>
  <tr>
    <td>Gemini-1.5-Flash</td>
    <td>59.1</td>
  </tr>
  <tr>
    <td>Claude-3-Sonnet</td>
    <td>56.8</td>
  </tr>
  <tr>
    <td>Llama-3-70B-Instruct</td>
    <td>56.2</td>
  </tr>
</table>


### Arena-Hard

<table class="col-12 col-md-6">
  <tr>
    <td><b>Model</b></td>
    <td><b>Arena-Hard</b></td>
  </tr>
  <tr>
    <td>GPT-4o</td>
    <td>79.5</td>
  </tr>
  <tr>
    <td>Gemini-1.5-Pro</td>
    <td>72.0</td>
  </tr>
  <tr>
    <td>Claude-3-Opus</td>
    <td>60.4</td>
  </tr>
  <tr style="font-weight: bold">
    <td>Higgs-Llama-3-70B</td>
    <td>49.6</td>
  </tr>
  <tr>
    <td>Gemini-1.5-Flash</td>
    <td>49.6</td>
  </tr>
  <tr>
    <td>Claude-3-Sonnet</td>
    <td>46.8</td>
  </tr>
  <tr>
    <td>Claude-3-Haiku</td>
    <td>41.5</td>
  </tr>
  <tr>
    <td>Llama-3-70B-Instruct</td>
    <td>41.1</td>
  </tr>
  <tr>
    <td>GPT-4-0613</td>
    <td>37.9</td>
  </tr>
  <tr>
    <td>Mistral-Large</td>
    <td>37.7</td>
  </tr>
</table>

## Overall Results

In the following, we compare our model's performance with `gpt-4o` and `Llama-3-70B-Instruct` on [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro), [Arena-Hard](https://github.com/lm-sys/arena-hard-auto/tree/main), [AlpacaEval 2.0 LC](https://github.com/tatsu-lab/alpaca_eval), MMLU, GPQA and DROP. For MMLU, GPQA and DROP, we adopt [openai/simple-evals](https://github.com/openai/simple-evals) for evaluation. For the other benchmarks, we evaluate via the official implementation.

<div style="overflow: auto">
  <table>
    <tr>
      <th></th>
      <td><b>MMLU-Pro</td>
      <td><b>Arena-Hard</td>
      <td><b>AlpacaEval <br> 2.0 LC</b></td>
      <td><b>MMLU</b></td>
      <td><b>GPQA</b></td>
      <td><b>DROP <br> (F1,3-shot)</b></td>
    </tr>
    <tr>
      <td>GPT-4o</td>
      <td>72.6</td>
      <td>79.5*</td>
      <td>57.5</td>
      <td>87.2</td>
      <td>49.9</td>
      <td>83.7</td>
    </tr>
    <tr style="font-weight: bold">
      <td>Higgs-Llama-3-70B</td>
      <td>63.2</td>
      <td>49.6</td>
      <td>38.6</td>
      <td>80.8</td>
      <td>42.1</td>
      <td>81.6</td>
    </tr>
    <tr>
      <td>Llama-3-70B-Instruct*</td>
      <td>56.2</td>
      <td>41.1</td>
      <td>34.4</td>
      <td>80.2</td>
      <td>41.3</td>
      <td>81.4</td>
    </tr>
  </table>
</div>

<small>*For Llama-3-70B-Instruct, the MMLU-Pro number is copied from the [MMLU-Pro leaderboard](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro); the Arena-Hard numbers are copied from the [leaderboard updated on 5/21](https://github.com/lm-sys/arena-hard-auto/tree/main?tab=readme-ov-file#full-leaderboard-updated-0521) while we run gpt-4o ourselves; and the MMLU/GPQA/DROP are copied from [simple-evals](https://github.com/openai/simple-evals).</small>


## How to use

We use the same prompting format as in Meta-Llama-3-70B-Instruct.

### Use with transformers

See the snippet below for usage with Transformers:

```python
import transformers
import torch

model_id = "bosonai/Higgs-Llama-3-70B"

pipeline = transformers.pipeline(
  "text-generation",
  model=model_id,
  model_kwargs={"torch_dtype": torch.bfloat16},
  device_map="auto",
)

messages = [
  {"role": "system", "content": "You are an AI assistant that speaks in the style of Sheldon Cooper. You are arguing with the user and is trying to prove the opposite of what the user said."},
  {"role": "user", "content": "The earth is round."},
]

prompt = pipeline.tokenizer.apply_chat_template(
  messages,
  tokenize=False,
  add_generation_prompt=True
)

outputs = pipeline(
  prompt,
  max_new_tokens=256,
  eos_token_id=[
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>"),
    pipeline.tokenizer.eos_token_id,
  ],
  do_sample=True,
  temperature=1.0,
  top_p=0.95,
)
print(outputs[0]["generated_text"][len(prompt):])
```

## License
[Our license](https://huggingface.co/bosonai/Higgs-Llama-3-70B/blob/main/LICENSE) is based on Meta's LLama 3 Community License.