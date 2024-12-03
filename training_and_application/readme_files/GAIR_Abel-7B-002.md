We released **Abel-7B-002**, resulting in a stronger (35% improvement on GSM8K, 126% improvement on MATH) and more generalized model, achieving the best performance among all 7B models (80.44 on GSM8K, 29.46 on MATH)

| Model | GSM8k  | MATH |MathQA | SVAMP |SCQ5K-EN | ARC-E|ARC-C|HellaSwag|MMLU |
|-----------|------------|----------|--------------|-----------|----------------|---------|----------|---------------|----------|
|Abel-7B-002 |	**80.44** | **29.46**	| **69.78**	|77.67	|**55.95**	|77.67	|**55.05**	|77.72	|61.19	|
|Abel-7B-001 |59.74	|13	|1.21	|57.67	|9.3	|53.32	|38.97	|63.51|40.59	|
|MetaMath-Mistral-7B|77.7	|28.2	|33.94	|**79.33**	|37.6|	**78.48**	|51.93	|76.44|	61.93|
|Qwen-7b|47.84	|9.34	|27.44	|53	|40.05	|74.97	|53.05	|**86.85**|57.98	|
|Mistral-7b|37.83	|9.06	|25.73	|63	|39.6	|76.83	|53.22|	76.31|**64.05**	|
|Yi-6b| 32.6	|5.78	|26.98	|55.67	|35.5	|73.66	|49.53	|68.97|64.02	|
|LLaMA2-7b|12.96	|2.78	|11.52	|44	|28.24	|71.12	|46.61	|71.32|46.7	|

Please cite the repo if the model/code/conclusion in this repo are helpful to you.
```
@misc{abel,
  author = {Chern, Ethan and Zou, Haoyang and Li, Xuefeng and Hu, Jiewen and Feng, Kehua and Li, Junlong and Liu, Pengfei},
  title = {Generative AI for Math: Abel},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/GAIR-NLP/abel}},
}
```