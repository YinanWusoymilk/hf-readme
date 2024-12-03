---
license: apache-2.0
base_model: v2ray/Mixtral-8x22B-v0.1
inference: false
model_creator: MaziyarPanahi
model_name: Mixtral-8x22B-v0.1-GGUF
pipeline_tag: text-generation
quantized_by: MaziyarPanahi
tags:
- quantized
- 2-bit
- 3-bit
- 4-bit
- 5-bit
- 6-bit
- 8-bit
- 16-bit
- GGUF
- mixtral
- moe
language:
- fr
- en
- es
- it
- de
---

<img src="./mixtral-8x22b.jpeg" width="600" />

# Mixtral-8x22B-v0.1-GGUF

On April 10th, [@MistralAI](https://huggingface.co/mistralai) released a model named "Mixtral 8x22B," an 176B MoE via magnet link (torrent):

- 141B MoE with ~35B active
- Context length of 65k tokens
- The base model can be fine-tuned
- Requires ~260GB VRAM in fp16, 73GB in int4
- Licensed under Apache 2.0, according to their Discord
- Available on @huggingface (community)
- Utilizes a tokenizer similar to previous models

The GGUF and quantized models here are based on [v2ray/Mixtral-8x22B-v0.1](https://huggingface.co/v2ray/Mixtral-8x22B-v0.1) model

## How to download
You can download only the quants you need instead of cloning the entire repository as follows:

```
huggingface-cli download MaziyarPanahi/WizardLM-2-8x22B-GGUF --local-dir . --include '*Q2_K*gguf'
```

## Load sharded model

`llama_load_model_from_file` will detect the number of files and will load additional tensors from the rest of files.

```sh
llama.cpp/main -m Mixtral-8x22B-v0.1.Q2_K-00001-of-00005.gguf -p "Building a website can be done in 10 simple steps:\nStep 1:" -n 1024 -e
```

The output from `Q2_K` quantized model:

```
system_info: n_threads = 64 / 128 | AVX = 1 | AVX_VNNI = 0 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 1 | SSSE3 = 1 | VSX = 0 | MATMUL_INT8 = 0 |
sampling:
        repeat_last_n = 64, repeat_penalty = 1.000, frequency_penalty = 0.000, presence_penalty = 0.000
        top_k = 40, tfs_z = 1.000, top_p = 0.950, min_p = 0.050, typical_p = 1.000, temp = 0.800
        mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampling order:
CFG -> Penalties -> top_k -> tfs_z -> typical_p -> top_p -> min_p -> temperature
generate: n_ctx = 512, n_batch = 2048, n_predict = 1024, n_keep = 1


 Building a website can be done in 10 simple steps:
Step 1: Pick a domain name
The domain name is your address on the Internet. It’s what people type into the browser to get to your website. It’s important to pick a domain name that is easy to remember and relates to your business. For example, if you were a plumber, you could register a domain like fixitplumbing.com. You can check the availability of a domain name with the WHOIS lookup tool. If your domain is available, you can register it at a domain registrar like GoDaddy.com or Domain.com.
Step 2: Sign up for a web hosting account
Web hosting is the service that stores your website files and makes them available to people on the Internet. It’s important to pick a web hosting provider that is reliable and has good customer service. Some popular web hosting providers include Bluehost, Hostgator, and Dreamhost.
Step 3: Create a website template
A website template is a pre-designed website that you can use as a starting point for your own website. There are many free website templates available online. Once you’ve found a template you like, you can download it and start customizing it to fit your needs.
Step 4: Add your content
Once you’ve chosen a template, you’ll need to add your own content to it. This includes things like your company logo, contact information, and text about your business. You can also add photos and videos to make your website more engaging.
Step 5: Test your website
Before you make your website live, it’s important to test it out. This includes checking for broken links, typos, and making sure that all of your content is correct. You can also ask friends or family to test your website and give you feedback.
Step 6: Launch your website
Once you’re happy with your website, you can make it live on the Internet. This process is called “launching” your website. You’ll need to upload your website files to your web hosting account and then point your domain name to your hosting account. Once you’ve done this, your website will be available to people on the Internet.
Step 7: Promote your website
Just because you’ve built a website doesn’t mean people will automatically find it. You need to promote your website to get people to visit it. This includes things like search engine optimization (SEO) and social media marketing.
Step 8: Track your website’s progress
Once you’ve built your website, you need to track its progress. This includes things like traffic, search engine rankings, and conversion rates. By tracking your website’s progress, you can make sure that it’s working properly and that people are finding it.
Step 9: Keep your website up-to-date
Just because you’ve built your website doesn’t mean you’re done. You need to keep your website up-to-date by adding new content and fixing any errors that occur. By keeping your website up-to-date, you can make sure that it’s always available to people on the Internet.
Step 10: Repeat steps 1-10

Once you’ve built your website, you need to promote it so that people can find it. You can do this by adding your website to search engines, directories, and social media sites. You can also promote your website by word-of-mouth and by giving people your business card.

Once you’ve promoted your website, you need to keep track of how it’s doing. You can do this by using website analytics tools. These tools will help you see how many people are visiting your website, where they’re coming from, and what they’re doing on your site.

If you want to keep your website up-to-date, you need to add new content on a regular basis. You can do this by writing blog posts, creating infographics, or recording videos. You can also add new content by updating your website’s design and by adding new features.

By following these steps, you can build a website that’s available to people on the Internet. You can also keep your website
```

Since this appears to be a base model, it will keep on generating. 



## Credit

- [MistralAI](https://huggingface.co/mistralai) for opening the weights
- [v2ray](https://huggingface.co/v2ray/) for downloading, converting, and sharing it with the community [Mixtral-8x22B-v0.1](https://huggingface.co/v2ray/Mixtral-8x22B-v0.1)
- [philschmid](https://huggingface.co/philschmid) for the photo he shared on his Twitter

                                                                     ▄▄▄░░
                                                            ▄▄▄▄▄█████████░░░░
                                                ▄▄▄▄▄▄████████████████████░░░░░
                                             █████████████████████████████░░░░░
                        ▄▄▄▄▄▄█████░░░       █████████████████████████████░░░░░
             ▄▄▄▄▄██████████████████░░░░░░  ██████████████████████████████░░░░░
      ▄█████████████████████████████░░░░░░░░██████████████████████████████░░░░░
      ███████████████████████████████░░░░░░░██████████████████████████████░░░░░
      ███████████████████████████████░░░░░░░██████████████████████████████░░░░░
      ███████████████████████████████░░░░░░███████████████████████████████░░░░░
      ████████████████████████████████░░░░░███████████████████████████████░░░░░
      ████████████████████████████████░░░░████████████████████████████████░░░░░
      █████████████████████████████████░░░████████████████████████████████░░░░░
      █████████████████████████████████░░░████████████░███████████████████░░░░░
      ██████████████████████████████████░█████████████░███████████████████░░░░░
      ███████████████████░██████████████▄█████████████░███████████████████░░░░░
      ███████████████████░███████████████████████████░░███████████████████░░░░░
      ███████████████████░░██████████████████████████░░███████████████████░░░░░
      ███████████████████░░█████████████████████████░░░███████████████████░░░░░
      ███████████████████░░░████████████████████████░░░███████████████████░░░░░
      ███████████████████░░░████████████████████████░░░███████████████████░░░░░
      ███████████████████░░░░██████████████████████░░░░███████████████████░░░░░
      ███████████████████░░░░██████████████████████░░░░███████████████████░░░░░
      ███████████████████░░░░░█████████████████████░░░░███████████████████░░░░░
      ███████████████████░░░░░████████████████████░░░░░███████████████████░░░░░
      ███████████████████░░░░░░███████████████████░░░░░███████████████████░░░░░
      ███████████████████░░░░░░██████████████████░░░░░░███████████████████░░░░░
      ███████████████████░░░░░░░█████████████████░░░░░░███████████████████░░░░░
      ███████████████████░░░░░░░█████████████████░░░░░░███████████████████░░░░░
      ███████████████████░░░░░░░░███████████████░░░░░░░██████████░░░░░░░░░░░░░░
      ███████████████████░░░░░░░░███████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
      ███████████████████░░░░░░░░███████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
      ███████████████████░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
      ███████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
      ██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░░░
          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      ░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░░░░░░░
                   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                        ░░░░░░░░░░░░░░░░░
                           ░░░░░