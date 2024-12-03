---
license: openrail
language:
- pt
---

# Cabrita: portuguese instructLLaMA

## Usage

Check the Github repo with code: https://github.com/22-hours/cabrita

```python
from peft import PeftModel
from transformers import LLaMATokenizer, LLaMAForCausalLM, GenerationConfig

tokenizer = LLaMATokenizer.from_pretrained("decapoda-research/llama-7b-hf")
model = LLaMAForCausalLM.from_pretrained(
    "decapoda-research/llama-7b-hf",
    load_in_8bit=True,
    device_map="auto",
)
model = PeftModel.from_pretrained(model, "22h/cabrita-lora-v0-1")
```


## Data

We translated the [alpaca_data.json](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json) to portuguese using ChatGPT. Even if this translation was not the best, the tradeoff between costs and results were. We paid around US$ 8.00 to translate the full dataset to portuguese.
If you want to know more about how the dataset was built go to: [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca).

## Finetuning

To finetuned the LLaMA model we used the code available on [Alpaca Lora](https://github.com/tloen/alpaca-lora), which provides code to finetune the LLaMA model using PEFT from Hugging Face. With this, we could run our finetuning step using 1 A100 at Colab on top of LLaMA-7B. We trained during 4 hours and we found the results pretty incredible with just that much time. The notebook we used is avaible [here](notebooks/train_lora.ipynb).

## Example outputs

Stanford Alpaca:
```
Instruction: Invente uma desculpa criativa pra dizer que não preciso ir à festa.
Response: Eu preciso se concentrar em trabalho importante para mim, por isso eu não posso ir à festa.
```

Cabrita:
```
Instrução: Invente uma desculpa criativa pra dizer que não preciso ir à festa.
Resposta: "Eu preciso ficar em casa para cuidar dos meus animais de estimação."
```


Stanford Alpaca:
```
Instruction: Como posso começar a carreira como cientista de dados? Escreva na forma de lista.
Response:
1. Comece por se especializar em um campo específico, como big data, computação, bioinformática ou estatística.
2. Obtivere um diploma em um programa de graduação relacionado a ciência de dados, como informática, matemática ou estatística.
3. Aquisite experiência prática através de internships ou projetos em empresas ou instituições.
4. Ameize sua resumo e currículo com resultados relevantes e experiência em trabalho relacionado.
5. Leia artigos, livros e atualizações sobre ciência de dados.
6. Crie um portfólio com projetos e experimentos que tenha realizado.
7. Receba um certificado de qualificação em alguma área de ciência de dados.
8. Tente obter contato com profissionais da área para conversar sobre oportunidades de emprego.
9. Acesse redes sociais, como LinkedIn, para encontrar empregos e conexões.
10. Continui sua formação atualizando-se com tecnologias e ferramentas de ciência de dados.
```

Cabrita:
```
Instrução: Como posso começar a carreira como cientista de dados? Escreva na forma de lista.
Resposta: 
1. Obtenha um mestrado em ciência de dados ou engenharia de dados.
2. Encontre um emprego como cientista de dados ou engenheiro de dados.
3. Conheça as principais ferramentas de análise de dados, como Python, R e SQL.
4. Conheça as principais técnicas de análise de dados, como regressão linear, regressão logística e análise de clustering.
5. Conheça as principais abordagens de análise de dados, como análise exploratória, análise de associação e análise de regressão.
6. Conheça as principais ferramentas de visualização de dados, como Tableau, QlikView e Power BI.
7. Conheça as principais abordagens de análise de dados, como análise de associação, análise de regressão e análise exploratória.
```

You can test it using the eval notebook [here](https://colab.research.google.com/github/22-hours/cabrita/blob/main/notebooks/cabrita-lora.ipynb).

## References

> If I have seen further it is by standing on the sholders [sic] of Giants.
> -- <cite>Isaac Newton</cite>
We started this section with this citation because everything we did was only possible due to the strong community and works that other people and groups did. For our work, we rely mainly in the works developed by: [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/), [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca), [Alpaca Lora](https://github.com/tloen/alpaca-lora), [ChatGPT](https://openai.com/blog/chatgpt) and [Hugging Face](https://huggingface.co/). So, thank you all for the great work and open this to the world!

## Hardware Requirements

For training we have used an A100 in Google Colab. For eval, you can use a T4.