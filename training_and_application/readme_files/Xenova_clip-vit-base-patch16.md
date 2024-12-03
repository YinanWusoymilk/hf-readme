---
base_model: openai/clip-vit-base-patch16
library_name: transformers.js
---

https://huggingface.co/openai/clip-vit-base-patch16 with ONNX weights to be compatible with Transformers.js.

## Usage (Transformers.js)

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@xenova/transformers) using:
```bash
npm i @xenova/transformers
```

**Example:** Perform zero-shot image classification with the `pipeline` API.
```js
const classifier = await pipeline('zero-shot-image-classification', 'Xenova/clip-vit-base-patch16');
const url = 'https://huggingface.co/datasets/Xenova/transformers.js-docs/resolve/main/tiger.jpg';
const output = await classifier(url, ['tiger', 'horse', 'dog']);
// [
//   { score: 0.9993917942047119, label: 'tiger' },
//   { score: 0.0003519294841680676, label: 'horse' },
//   { score: 0.0002562698791734874, label: 'dog' }
// ]
```

**Example:** Perform zero-shot image classification with `CLIPModel`.

```js
import { AutoTokenizer, AutoProcessor, CLIPModel, RawImage } from '@xenova/transformers';

// Load tokenizer, processor, and model
const tokenizer = await AutoTokenizer.from_pretrained('Xenova/clip-vit-base-patch16');
const processor = await AutoProcessor.from_pretrained('Xenova/clip-vit-base-patch16');
const model = await CLIPModel.from_pretrained('Xenova/clip-vit-base-patch16');

// Run tokenization
const texts = ['a photo of a car', 'a photo of a football match'];
const text_inputs = tokenizer(texts, { padding: true, truncation: true });

// Read image and run processor
const image = await RawImage.read('https://huggingface.co/datasets/Xenova/transformers.js-docs/resolve/main/football-match.jpg');
const image_inputs = await processor(image);

// Run model with both text and pixel inputs
const output = await model({ ...text_inputs, ...image_inputs });
// {
//   logits_per_image: Tensor {
//     dims: [ 1, 2 ],
//     data: Float32Array(2) [ 18.579734802246094, 24.31830596923828 ],
//   },
//   logits_per_text: Tensor {
//     dims: [ 2, 1 ],
//     data: Float32Array(2) [ 18.579734802246094, 24.31830596923828 ],
//   },
//   text_embeds: Tensor {
//     dims: [ 2, 512 ],
//     data: Float32Array(1024) [ ... ],
//   },
//   image_embeds: Tensor {
//     dims: [ 1, 512 ],
//     data: Float32Array(512) [ ... ],
//   }
// }
```

**Example:** Compute text embeddings with `CLIPTextModelWithProjection`.
```js
import { AutoTokenizer, CLIPTextModelWithProjection } from '@xenova/transformers';

// Load tokenizer and text model
const tokenizer = await AutoTokenizer.from_pretrained('Xenova/clip-vit-base-patch16');
const text_model = await CLIPTextModelWithProjection.from_pretrained('Xenova/clip-vit-base-patch16');

// Run tokenization
const texts = ['a photo of a car', 'a photo of a football match'];
const text_inputs = tokenizer(texts, { padding: true, truncation: true });

// Compute embeddings
const { text_embeds } = await text_model(text_inputs);
// Tensor {
//   dims: [ 2, 512 ],
//   type: 'float32',
//   data: Float32Array(1024) [ ... ],
//   size: 1024
// }
```

**Example:** Compute vision embeddings with `CLIPVisionModelWithProjection`.
```js
import { AutoProcessor, CLIPVisionModelWithProjection, RawImage } from '@xenova/transformers';

// Load processor and vision model
const processor = await AutoProcessor.from_pretrained('Xenova/clip-vit-base-patch16');
const vision_model = await CLIPVisionModelWithProjection.from_pretrained('Xenova/clip-vit-base-patch16');

// Read image and run processor
const image = await RawImage.read('https://huggingface.co/datasets/Xenova/transformers.js-docs/resolve/main/football-match.jpg');
const image_inputs = await processor(image);

// Compute embeddings
const { image_embeds } = await vision_model(image_inputs);
// Tensor {
//   dims: [ 1, 512 ],
//   type: 'float32',
//   data: Float32Array(512) [ ... ],
//   size: 512
// }
```

---

Note: Having a separate repo for ONNX weights is intended to be a temporary solution until WebML gains more traction. If you would like to make your models web-ready, we recommend converting to ONNX using [🤗 Optimum](https://huggingface.co/docs/optimum/index) and structuring your repo like this one (with ONNX weights located in a subfolder named `onnx`).