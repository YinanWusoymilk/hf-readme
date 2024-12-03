---
license: apache-2.0
---

![An eagle soaring above a transformer robot](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bbd31a7-21b4-4ff6-b43f-8735d1decf25_2048x1652.png)

> **! Important Note !**
>
> The following is the full RWKV-5 Eagle 7B model weights, which can be used with our various inference libraries
> [Download link here](https://huggingface.co/RWKV/v5-Eagle-7B/resolve/main/RWKV-v5-Eagle-World-7B-v2-20240128-ctx4096.pth?download=true)
>
> For HF compatible implementation, [refer to here](https://huggingface.co/RWKV/HF_v5-Eagle-7B)
>
> This is not an instruct tune model! (soon...)

- [HF Demo](https://huggingface.co/spaces/BlinkDL/RWKV-Gradio-2)
- [Our wiki](https://wiki.rwkv.com)
- [HF compatible weights](https://huggingface.co/RWKV/HF_v5-Eagle-7B)

# Eagle 7B - in short

Eagle 7B is a 7.52B parameter model that:

- Built on the RWKV-v5 architecture
  (a linear transformer with 10-100x+ lower inference cost)
- Ranks as the world’s greenest 7B model (per token)
- Trained on 1.1 Trillion Tokens across 100+ languages
  (70% English, 15% multi lang, 15% code)
- Outperforms all 7B class models in multi-lingual benchmarks
- Approaches Falcon (1.5T), LLaMA2 (2T), Mistral (>2T?) level of performance in English evals
- Trade blows with MPT-7B (1T) in English evals
- All while being an “Attention-Free Transformer”
- Is a foundation model, with a very small instruct tune - further fine-tuning is required for various use cases!

Find out more at our model announcement: https://blog.rwkv.com/p/eagle-7b-soaring-past-transformers

Or our wiki: https://wiki.rwkv.com