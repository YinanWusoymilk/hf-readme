---
language:
- tr
- en
pipeline_tag: text-generation
license: apache-2.0
---
<img src="https://huggingface.co/Trendyol/Trendyol-LLM-7b-chat-v0.1/resolve/main/llama-tr-image.jpeg"
alt="drawing" width="400"/>
# **Trendyol LLM**
Trendyol LLM is a generative model that is based on LLaMa2 7B model. This is the repository for the chat model.

## Model Details

**Model Developers** Trendyol

**Variations** base and chat variations.

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture** Trendyol LLM is an auto-regressive language model (based on LLaMa2 7b) that uses an optimized transformer architecture. The chat version is fine-tuned on 180K instruction sets with the following trainables by using LoRA:

- **lr**=1e-4
- **lora_rank**=64
- **lora_alpha**=128
- **lora_trainable**=q_proj,v_proj,k_proj,o_proj,gate_proj,down_proj,up_proj
- **modules_to_save**=embed_tokens,lm_head
- **lora_dropout**=0.05
- **fp16**=True
- **max_seq_length**=1024

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/peft/lora_diagram.png"
alt="drawing" width="600"/>

## Usage

```python
from transformers import AutoModelForCausalLM, LlamaTokenizer, pipeline

model_id = "Trendyol/Trendyol-LLM-7b-chat-v0.1"
tokenizer = LlamaTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, 
                                             device_map='auto', 
                                             load_in_8bit=True)

sampling_params = dict(do_sample=True, temperature=0.3, top_k=50, top_p=0.9)

pipe = pipeline("text-generation", 
                model=model, 
                tokenizer=tokenizer,
                device_map="auto",
                max_new_tokens=1024, 
                return_full_text=True,
                repetition_penalty=1.1
               )

DEFAULT_SYSTEM_PROMPT = "Sen yardımcı bir asistansın ve sana verilen talimatlar doğrultusunda en iyi cevabı üretmeye çalışacaksın.\n"

TEMPLATE = (
    "[INST] <<SYS>>\n"
    "{system_prompt}\n"
    "<</SYS>>\n\n"
    "{instruction} [/INST]"
)

def generate_prompt(instruction, system_prompt=DEFAULT_SYSTEM_PROMPT):
    return TEMPLATE.format_map({'instruction': instruction,'system_prompt': system_prompt})

def generate_output(user_query, sys_prompt=DEFAULT_SYSTEM_PROMPT):
    prompt = generate_prompt(user_query, sys_prompt)
    outputs = pipe(prompt,
               **sampling_params
              )
    return outputs[0]["generated_text"].split("[/INST]")[-1]

user_query = "Türkiye'de kaç il var?"
response = generate_output(user_query)
print(response)
```

with chat template:
```python
pipe = pipeline("conversational", 
                model=model, 
                tokenizer=tokenizer,
                device_map="auto",
                max_new_tokens=1024,
                repetition_penalty=1.1
               )

messages = [
    {
        "role": "system",
        "content": "Sen yardımsever bir chatbotsun. Sana verilen diyalog akışına dikkat ederek diyaloğu devam ettir.",
    },
    {"role": "user", "content": "Türkiye'de kaç il var?"}
]

outputs = pipe(messages, **sampling_params)
print(outputs)
```


## Limitations, Risks, Bias, and Ethical Considerations

### Limitations and Known Biases

- **Primary Function and Application:** Trendyol LLM, an autoregressive language model, is primarily designed to predict the next token in a text string. While often used for various applications, it is important to note that it has not undergone extensive real-world application testing. Its effectiveness and reliability across diverse scenarios remain largely unverified.

- **Language Comprehension and Generation:** The model is primarily trained in standard English and Turkish. Its performance in understanding and generating slang, informal language, or other languages may be limited, leading to potential errors or misinterpretations.

- **Generation of False Information:** Users should be aware that Trendyol LLM may produce inaccurate or misleading information. Outputs should be considered as starting points or suggestions rather than definitive answers.

### Risks and Ethical Considerations

- **Potential for Harmful Use:** There is a risk that Trendyol LLM could be used to generate offensive or harmful language. We strongly discourage its use for any such purposes and emphasize the need for application-specific safety and fairness evaluations before deployment.

- **Unintended Content and Bias:** The model was trained on a large corpus of text data, which was not explicitly checked for offensive content or existing biases. Consequently, it may inadvertently produce content that reflects these biases or inaccuracies.

- **Toxicity:** Despite efforts to select appropriate training data, the model is capable of generating harmful content, especially when prompted explicitly. We encourage the open-source community to engage in developing strategies to minimize such risks.

### Recommendations for Safe and Ethical Usage

- **Human Oversight:** We recommend incorporating a human curation layer or using filters to manage and improve the quality of outputs, especially in public-facing applications. This approach can help mitigate the risk of generating objectionable content unexpectedly.

- **Application-Specific Testing:** Developers intending to use Trendyol LLM should conduct thorough safety testing and optimization tailored to their specific applications. This is crucial, as the model’s responses can be unpredictable and may occasionally be biased, inaccurate, or offensive.

- **Responsible Development and Deployment:** It is the responsibility of developers and users of Trendyol LLM to ensure its ethical and safe application. We urge users to be mindful of the model's limitations and to employ appropriate safeguards to prevent misuse or harmful consequences.