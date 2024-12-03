---
library_name: transformers.js
tags: 
- transformers
---

## Usage (Transformers.js)

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@xenova/transformers) using:
```bash
npm i @xenova/transformers
```

You can then use the model to generate text like this:

```js
import { pipeline } from "@xenova/transformers";

// Create a text-generation pipeline
const generator = await pipeline('text-generation', 'Xenova/llama2.c-stories15M');

const text = 'Once upon a time,';
const output = await generator(text);
console.log(output);
// [{ generated_text: "Once upon a time, there was a little girl named Lily. She loved to play outside in" }]

const output2 = await generator(text, { max_new_tokens: 50 });
console.log(output2);
// [{ generated_text: "Once upon a time, there was a little girl named Lily. She loved to play outside in the sunshine. One day, she saw a big, dark cloud in the sky. She knew it was going to rain soon.\nLily ran inside her house" }]
```
