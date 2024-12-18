---
language: es

widget:
- text: "La inteligencia artificial en lationoamérica se ha desarrollado "
license: apache-2.0
datasets: 
- wikipedia
---
La descripción en Español se encuentra después de la descripción en Inglés.

# (English) GPT2-small-spanish: a Language Model for Spanish text generation (and more NLP tasks...)
GPT2-small-spanish is a state-of-the-art language model for Spanish based on the GPT-2 small model. 

It was trained on Spanish Wikipedia using **Transfer Learning and Fine-tuning techniques**. The training took around 70 hours with four GPU NVIDIA GTX 1080-Ti with 11GB of DDR5 and with around 3GB of (processed) training data. 

It was fine-tuned from the [English pre-trained GPT-2 small](https://huggingface.co/gpt2) using the Hugging Face libraries (Transformers and Tokenizers) wrapped into the [fastai v2](https://dev.fast.ai/) Deep Learning framework. All the fine-tuning fastai v2 techniques were used.

The training is purely based on the [GPorTuguese-2](https://huggingface.co/pierreguillou/gpt2-small-portuguese) model developed by Pierre Guillou. The training details are in this article: "[Faster than training from scratch — Fine-tuning the English GPT-2 in any language with Hugging Face and fastai v2 (practical case with Portuguese)](https://medium.com/@pierre_guillou/faster-than-training-from-scratch-fine-tuning-the-english-gpt-2-in-any-language-with-hugging-f2ec05c98787)".

This preliminary version is now available on Hugging Face.

## Limitations and bias

(Copied from original GPorTuguese-2 model)The training data used for this model come from Spanish Wikipedia. We know it contains a lot of unfiltered content from the internet, which is far from neutral. As the openAI team themselves point out in their model card:

> Because large-scale language models like GPT-2 do not distinguish fact from fiction, we don’t support use-cases that require the generated text to be true. Additionally, language models like GPT-2 reflect the biases inherent to the systems they were trained on, so we do not recommend that they be deployed into systems that interact with humans > unless the deployers first carry out a study of biases relevant to the intended use-case. We found no statistically significant difference in gender, race, and religious bias probes between 774M and 1.5B, implying all versions of GPT-2 should be approached with similar levels of caution around use cases that are sensitive to biases around human attributes.

## Authors

The model was trained and evaluated by [Josué Obregon](https://www.linkedin.com/in/josue-obregon/) and [Berny Carrera](https://www.linkedin.com/in/bernycarrera/), founders of [Datificate](https://datificate.com), a space for learning Machine Learning in Spanish.
The training was possible thanks to the computing power of several GPUs (GPU NVIDIA GTX1080-Ti) of the [IAI Lab](http://iai.khu.ac.kr/) (Kyung Hee University) from which Josué is attached as a Postdoctoral Researcher in Industrial Artificial Intelligence.

As stated before, this work is mainly based in the work of [Pierre GUILLOU](https://www.linkedin.com/in/pierreguillou/).


# (Español) GPT2-small-spanish: un modelo de lenguaje para generación de texto en Español (y algunas otras tareas de NLP...)

GPT2-small-spanish es un modelo de lenguaje de vanguardia en Español basado en el modelo pequeño GPT-2. 

Fué entrenado con la Wikipedia en Español usando **técnicas de Aprendizaje por Transferencia y afinación de modelos**. El entrenamiento del modelo tomó alrededor 70 horas con cuatro GPUs NVIDIA GTX 1080-Ti con 11GB de DDR5 y con aproximadamente 3GB de datos de entrenamiento preprocesados. 

Fue afinado del modelo en Inglés [English pre-trained GPT-2 small](https://huggingface.co/gpt2) utilizando las librerías de Hugging Face  (Transformers y Tokenizers) integradas con el framework de Deep Learning [fastai v2](https://dev.fast.ai/). Se usaron técnicas de afinamiento fino de fastai v2.

El entrenamiento está enteramente basado en el modelo en Portugués [GPorTuguese-2](https://huggingface.co/pierreguillou/gpt2-small-portuguese) desarrollado por Pierre Guillou. Los detalles del entrenamiento se encuentran en este articulo: "[Faster than training from scratch — Fine-tuning the English GPT-2 in any language with Hugging Face and fastai v2 (practical case with Portuguese)](https://medium.com/@pierre_guillou/faster-than-training-from-scratch-fine-tuning-the-english-gpt-2-in-any-language-with-hugging-f2ec05c98787)".

La versión preliminar del modelo se encuentra en Hugging Face.

## Limitaciones y sesgos

(Copiado del modelo original GPorTuguese-2 model)Los datos de entrenamiento provienen de la Wikipedia en Español. Se sabe que contiene bastante contenido no filtrado del internet, lo cual está lejos de ser neutral. Esto es señalado por el equipo desarrollador de openAI en su propia tarjeta de modelo:

> Because large-scale language models like GPT-2 do not distinguish fact from fiction, we don’t support use-cases that require the generated text to be true. Additionally, language models like GPT-2 reflect the biases inherent to the systems they were trained on, so we do not recommend that they be deployed into systems that interact with humans > unless the deployers first carry out a study of biases relevant to the intended use-case. We found no statistically significant difference in gender, race, and religious bias probes between 774M and 1.5B, implying all versions of GPT-2 should be approached with similar levels of caution around use cases that are sensitive to biases around human attributes.

## Autores

El modelo fue entreando y evaluado por [Josué Obregon](https://www.linkedin.com/in/josue-obregon/) y [Berny Carrera](https://www.linkedin.com/in/bernycarrera/), fundadores de [Datificate](https://datificate.com), un espacio para aprender Machine Learning en Español.

El entrenamiento fue posible gracias al poder computacional de varias GPUs (GPU NVIDIA GTX1080-Ti) del Laboratorio de Inteligencia Artificial Industrial [IAI Lab](http://iai.khu.ac.kr/) (Universidad de Kyung Hee) al cual Josué pertenece como investigador postdoctoral en Inteligencia Artificial Industrial.

Como fue mencionado anteriormente, este trabajo está basado en el trabajo de [Pierre GUILLOU](https://www.linkedin.com/in/pierreguillou/).

