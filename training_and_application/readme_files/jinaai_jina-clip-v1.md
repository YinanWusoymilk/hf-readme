---
tags:
- feature-extraction
- sentence-similarity
- mteb
- clip
- vision
- transformers.js
language: en
inference: false
license: apache-2.0
library_name: transformers
---

<br><br>

<p align="center">
<img src="https://aeiljuispo.cloudimg.io/v7/https://cdn-uploads.huggingface.co/production/uploads/603763514de52ff951d89793/AFoybzd5lpBQXEBrQHuTt.png?w=200&h=200&f=face" alt="Finetuner logo: Finetuner helps you to create experiments in order to improve embeddings on search tasks. It accompanies you to deliver the last mile of performance-tuning for neural search applications." width="150px">
</p>


<p align="center">
<b>The embedding set trained by <a href="https://jina.ai/"><b>Jina AI</b></a>.</b>
</p>

<p align="center">
<b>Jina CLIP: your CLIP model is also your text retriever!</b>
</p>


## Intended Usage & Model Info

`jina-clip-v1` is a state-of-the-art English **multimodal (text-image) embedding model**.

Traditional text embedding models, such as [jina-embeddings-v2-base-en](https://huggingface.co/jinaai/jina-embeddings-v2-base-en), excel in text-to-text retrieval but incapable of cross-modal tasks. Models like [openai/clip-vit-base-patch32](https://huggingface.co/openai/clip-vit-base-patch32) effectively align image and text embeddings but are not optimized for text-to-text retrieval due to their training methodologies and context limitations.

`jina-clip-v1` bridges this gap by offering robust performance in both domains.
Its text component matches the retrieval efficiency of `jina-embeddings-v2-base-en`, while its overall architecture sets a new benchmark for cross-modal retrieval.
This dual capability makes it an excellent tool for multimodal retrieval-augmented generation (MuRAG) applications, enabling seamless text-to-text and text-to-image searches within a single model.


## Data & Parameters

[Check out our paper](https://arxiv.org/abs/2405.20204)

## Usage

1. The easiest way to starting using jina-clip-v1-en is to use Jina AI's [Embeddings API](https://jina.ai/embeddings/).
2. Alternatively, you can use Jina CLIP directly via transformers/sentence-transformers package.

```python
!pip install transformers einops timm pillow
from transformers import AutoModel

# Initialize the model
model = AutoModel.from_pretrained('jinaai/jina-clip-v1', trust_remote_code=True)

# New meaningful sentences
sentences = ['A blue cat', 'A red cat']

# Public image URLs
image_urls = [
    'https://i.pinimg.com/600x315/21/48/7e/21487e8e0970dd366dafaed6ab25d8d8.jpg',
    'https://i.pinimg.com/736x/c9/f2/3e/c9f23e212529f13f19bad5602d84b78b.jpg'
]

# Encode text and images
text_embeddings = model.encode_text(sentences)
image_embeddings = model.encode_image(image_urls)  # also accepts PIL.image, local filenames, dataURI

# Compute similarities
print(text_embeddings[0] @ text_embeddings[1].T) # text embedding similarity
print(text_embeddings[0] @ image_embeddings[0].T) # text-image cross-modal similarity
print(text_embeddings[0] @ image_embeddings[1].T) # text-image cross-modal similarity
print(text_embeddings[1] @ image_embeddings[0].T) # text-image cross-modal similarity
print(text_embeddings[1] @ image_embeddings[1].T)# text-image cross-modal similarity
```

or sentence-transformers:

```python
# !pip install -U sentence-transformers 
from sentence_transformers import SentenceTransformer

# Initialize the model
model = SentenceTransformer('jinaai/jina-clip-v1', trust_remote_code=True)

# New meaningful sentences
sentences = ['A blue cat', 'A red cat']

# Public image URLs
image_urls = [
    'https://i.pinimg.com/600x315/21/48/7e/21487e8e0970dd366dafaed6ab25d8d8.jpg',
    'https://i.pinimg.com/736x/c9/f2/3e/c9f23e212529f13f19bad5602d84b78b.jpg'
]

text_embeddings = model.encode(sentences)
image_embeddings = model.encode(image_urls)
```

3. JavaScript developers can use Jina CLIP via the [Transformers.js](https://huggingface.co/docs/transformers.js) library. Note that to use this model, you need to install Transformers.js [v3](https://github.com/xenova/transformers.js/tree/v3) from source using `npm install xenova/transformers.js#v3`.

```js
import { AutoTokenizer, CLIPTextModelWithProjection, AutoProcessor, CLIPVisionModelWithProjection, RawImage, cos_sim } from '@xenova/transformers';

// Load tokenizer and text model
const tokenizer = await AutoTokenizer.from_pretrained('jinaai/jina-clip-v1');
const text_model = await CLIPTextModelWithProjection.from_pretrained('jinaai/jina-clip-v1');

// Load processor and vision model
const processor = await AutoProcessor.from_pretrained('Xenova/clip-vit-base-patch32');
const vision_model = await CLIPVisionModelWithProjection.from_pretrained('jinaai/jina-clip-v1');

// Run tokenization
const texts = ['A blue cat', 'A red cat'];
const text_inputs = tokenizer(texts, { padding: true, truncation: true });

// Compute text embeddings
const { text_embeds } = await text_model(text_inputs);

// Read images and run processor
const urls = [
    'https://i.pinimg.com/600x315/21/48/7e/21487e8e0970dd366dafaed6ab25d8d8.jpg',
    'https://i.pinimg.com/736x/c9/f2/3e/c9f23e212529f13f19bad5602d84b78b.jpg'
];
const image = await Promise.all(urls.map(url => RawImage.read(url)));
const image_inputs = await processor(image);

// Compute vision embeddings
const { image_embeds } = await vision_model(image_inputs);

//  Compute similarities
console.log(cos_sim(text_embeds[0].data, text_embeds[1].data)) // text embedding similarity
console.log(cos_sim(text_embeds[0].data, image_embeds[0].data)) // text-image cross-modal similarity
console.log(cos_sim(text_embeds[0].data, image_embeds[1].data)) // text-image cross-modal similarity
console.log(cos_sim(text_embeds[1].data, image_embeds[0].data)) // text-image cross-modal similarity
console.log(cos_sim(text_embeds[1].data, image_embeds[1].data)) // text-image cross-modal similarity
```

## Performance

### Text-Image Retrieval

| Name             | Flickr Image Retr. R@1 | Flickr Image Retr. R@5 | Flickr Text Retr. R@1 | Flickr Text Retr. R@5 |
|------------------|-------------------------|-------------------------|-----------------------|-----------------------|
| ViT-B-32         | 0.597                   | 0.8398                  | 0.781                 | 0.938                 |
| ViT-B-16         | 0.6216                  | 0.8572                  | 0.822                 | 0.966                 |
| jina-clip        | 0.6748                  | 0.8902                  | 0.811                 | 0.965                 |


| Name             | MSCOCO Image Retr. R@1  | MSCOCO Image Retr. R@5 | MSCOCO Text Retr. R@1 | MSCOCO Text Retr. R@5 |
|------------------|-------------------------|-------------------------|-----------------------|-----------------------|
| ViT-B-32         | 0.342                   | 0.6001                  | 0.5234                | 0.7634                |
| ViT-B-16         | 0.3309                  | 0.5842                  | 0.5242                | 0.767                 |
| jina-clip        | 0.4111                  | 0.6644                  | 0.5544                | 0.7904                |

### Text-Text Retrieval

| Name                  | STS12  | STS15  | STS17  | STS13  | STS14  | STS16  | STS22  | STSBenchmark | SummEval |
|-----------------------|--------|--------|--------|--------|--------|--------|--------|--------------|----------|
| jina-embeddings-v2    | 0.7427 | 0.8755 | 0.8888 | 0.833  | 0.7917 | 0.836  | 0.6346 | 0.8404       | 0.3056   |
| jina-clip             | 0.7352 | 0.8746 | 0.8976 | 0.8323 | 0.7868 | 0.8377 | 0.6583 | 0.8493       | 0.3048   |


| Name               | ArguAna | FiQA2018 | NFCorpus | Quora | SCIDOCS | SciFact | TRECCOVID |
|--------------------|---------|----------|----------|-------|---------|---------|-----------|
| jina-embeddings-v2 | 0.4418  | 0.4158   | 0.3245   | 0.882 | 0.1986  | 0.6668  | 0.6591    |
| jina-clip          | 0.4933  | 0.3827   | 0.3352   | 0.8789| 0.2024  | 0.6734  | 0.7161    |

## Contact

Join our [Discord community](https://discord.jina.ai) and chat with other community members about ideas.

## Citation

If you find `jina-clip-v1` useful in your research, please cite the following paper:

```bibtex
@misc{2405.20204,
    Author = {Andreas Koukounas and Georgios Mastrapas and Michael Günther and Bo Wang and Scott Martens and Isabelle Mohr and Saba Sturua and Mohammad Kalim Akram and Joan Fontanals Martínez and Saahil Ognawala and Susana Guzman and Maximilian Werk and Nan Wang and Han Xiao},
    Title = {Jina CLIP: Your CLIP Model Is Also Your Text Retriever},
    Year = {2024},
    Eprint = {arXiv:2405.20204},
}
```

## FAQ

### I encounter this problem, what should I do?

```
ValueError: The model class you are passing has a `config_class` attribute that is not consistent with the config class you passed (model has <class 'transformers_modules.jinaai.jina-clip-implementation.7f069e2d54d609ef1ad2eb578c7bf07b5a51de41.configuration_clip.JinaCLIPConfig'> and you passed <class 'transformers_modules.jinaai.jina-clip-implementation.7f069e2d54d609ef1ad2eb578c7bf07b5a51de41.configuration_cli.JinaCLIPConfig'>. Fix one of those so they match!
```

There was a bug in Transformers library between 4.40.x to 4.41.1. You can update transformers to >4.41.2 or <=4.40.0

### Given one query, how can I merge its text-text and text-image cosine similarity?

Our emperical study shows that text-text cosine similarity is normally larger than text-image cosine similarity!
If you want to merge two scores, we recommended 2 ways:

1. weighted average of text-text sim and text-image sim:

```python
combined_scores = sim(text, text) + lambda * sim(text, image)  # optimal lambda depends on your dataset, but in general lambda=2 can be a good choice.
```

2. apply z-score normalization before merging scores:

```python
# pseudo code
query_document_mean = np.mean(cos_sim_text_texts)
query_document_std = np.std(cos_sim_text_texts)
text_image_mean = np.mean(cos_sim_text_images)
text_image_std = np.std(cos_sim_text_images)

query_document_sim_normalized = (cos_sim_query_documents - query_document_mean) / query_document_std
text_image_sim_normalized = (cos_sim_text_images - text_image_mean) / text_image_std
```