---
license: other
license_name: msrla
license_link: https://huggingface.co/microsoft/rad-dino/blob/main/LICENSE
library_name: transformers
---

# Model card for RAD-DINO

<!-- Provide a quick summary of what the model is/does. -->

## Model description

<!-- Provide a longer summary of what this model is. -->

RAD-DINO is a vision transformer model trained to encode chest X-rays using the self-supervised learning method [DINOv2](https://openreview.net/forum?id=a68SUt6zFt).

RAD-DINO is described in detail in [RAD-DINO: Exploring Scalable Medical Image Encoders Beyond Text Supervision (F. Pérez-García, H. Sharma, S. Bond-Taylor, et al., 2024)](https://arxiv.org/abs/2401.10815).

- **Developed by:** Microsoft Health Futures
- **Model type:** Vision transformer
- **License:** [MSRLA](./LICENSE)
- **Finetuned from model:** [`dinov2-base`](https://huggingface.co/facebook/dinov2-base)

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

RAD-DINO is shared for research purposes only.
It is **not meant to be used for clinical practice**.

<!-- ### Downstream use -->

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

The model is a vision backbone that can be plugged to other models for downstream tasks.
Some potential uses are:

- Image classification, with a classifier trained on top of the `CLS` token
- Image segmentation, with a decoder trained using the patch tokens
- Clustering, using the image embeddings directly
- Image retrieval, using nearest neighbors of the CLS token
- Report generation, with a language model to decode text

Fine-tuning RAD-DINO is typically not necessary to obtain good performance in downstream tasks.

<!-- ### Out-of-scope use -->

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

## Biases, risks, and limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

RAD-DINO was trained with data from three countries, therefore it might be biased towards population in the training data.
Underlying biases of the training datasets may not be well characterized.

## Getting started

Let us first write an auxiliary function to download a chest X-ray.

```python
>>> import requests
>>> from PIL import Image
>>> def download_sample_image() -> Image.Image:
...     """Download chest X-ray with CC license."""
...     base_url = "https://upload.wikimedia.org/wikipedia/commons"
...     image_url = f"{base_url}/2/20/Chest_X-ray_in_influenza_and_Haemophilus_influenzae.jpg"
...     headers = {"User-Agent": "RAD-DINO"}
...     response = requests.get(image_url, headers=headers, stream=True)
...     return Image.open(response.raw)
...
```

Now let us download the model and encode an image.

```python
>>> import torch
>>> from transformers import AutoModel
>>> from transformers import AutoImageProcessor
>>>
>>> # Download the model
>>> repo = "microsoft/rad-dino"
>>> model = AutoModel.from_pretrained(repo)
>>>
>>> # The processor takes a PIL image, performs resizing, center-cropping, and
>>> # intensity normalization using stats from MIMIC-CXR, and returns a
>>> # dictionary with a PyTorch tensor ready for the encoder
>>> processor = AutoImageProcessor.from_pretrained(repo)
>>>
>>> # Download and preprocess a chest X-ray
>>> image = download_sample_image()
>>> image.size  # (width, height)
(2765, 2505)
>>> inputs = processor(images=image, return_tensors="pt")
>>>
>>> # Encode the image!
>>> with torch.inference_mode():
>>>     outputs = model(**inputs)
>>>
>>> # Look at the CLS embeddings
>>> cls_embeddings = outputs.pooler_output
>>> cls_embeddings.shape  # (batch_size, num_channels)
torch.Size([1, 768])
```

If we are interested in the feature maps, we can reshape the patch embeddings into a grid.
We will use [`einops`](https://einops.rocks/) (install with `pip install einops`) for this.

```python
>>> def reshape_patch_embeddings(flat_tokens: torch.Tensor) -> torch.Tensor:
...     """Reshape flat list of patch tokens into a nice grid."""
...     from einops import rearrange
...     image_size = processor.crop_size["height"]
...     patch_size = model.config.patch_size
...     embeddings_size = image_size // patch_size
...     patches_grid = rearrange(flat_tokens, "b (h w) c -> b c h w", h=embeddings_size)
...     return patches_grid
...
>>> flat_patch_embeddings = outputs.last_hidden_state[:, 1:]  # first token is CLS
>>> reshaped_patch_embeddings = reshape_patch_embeddings(flat_patch_embeddings)
>>> reshaped_patch_embeddings.shape  # (batch_size, num_channels, height, width)
torch.Size([1, 768, 37, 37])
```

## Training details

### Training data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

We used images from five public, deidentified chest X-ray datasets to train this checkpoint of RAD-DINO.

| Dataset   | Num. images |
| --------- | ----------: |
| [MIMIC-CXR](https://www.nature.com/articles/s41597-019-0322-0) | 368 960 |
| [CheXpert](https://ojs.aaai.org/index.php/AAAI/article/view/3834) | 223 648 |
| [NIH-CXR](https://openaccess.thecvf.com/content_cvpr_2017/html/Wang_ChestX-ray8_Hospital-Scale_Chest_CVPR_2017_paper.html) | 112 120 |
| [PadChest](https://www.sciencedirect.com/science/article/abs/pii/S1361841520301614) | 136 787 |
| [BRAX](https://www.nature.com/articles/s41597-022-01608-8) | 41 260 |
| **TOTAL** | 882 775 |

Images in the validation and test sets used to train [MAIRA](https://arxiv.org/abs/2311.13668) were excluded from the training set of RAD-DINO.
The list of image files used for training is available at [`./training_images.csv`](./training_images.csv).

Note this checkpoint is different from the one in the paper, where some private data was used (and fewer GPUs).
The checkpoint shared here is trained for 35 000 iterations (the total number of iterations in the run was 100 000, but we selected this checkpoint using linear probing on the validation sets of the evaluation datasets described in the paper).
We used 16 nodes with 4 A100 GPUs each, and a batch size of 40 images per GPU.

### Training procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

We refer to the [manuscript](https://arxiv.org/abs/2401.10815) for a detailed description of the training procedure.

#### Preprocessing

All DICOM files were resized using B-spline interpolation so that their shorter size was 518, min-max scaled to [0, 255], and stored as PNG files.

#### Training hyperparameters

- **Training regime:** fp16 using PyTorch-FSDP mixed-precision.

<!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

Our evaluation is best described in the [manuscript](https://arxiv.org/abs/2401.10815).

<!-- ### Testing data, factors & metrics

#### Testing Data

[More Information Needed]

#### Factors

[More Information Needed]

#### Metrics

[More Information Needed]

### Results

[More Information Needed]

#### Summary -->

## Environmental impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

<!-- Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700). -->

<!-- Hardware type: A100 PCIe -->
<!-- Hours: 1d 16h = 40h -->
<!-- Cloud provider: Azure -->
<!-- Region: Italy North -->

- **Hardware type:** NVIDIA A100 GPUs
- **Hours used:** 40 hours/GPU × 16 nodes × 4 GPUs/node = 2560 GPU-hours
- **Cloud provider:** Azure
- **Compute region:** West US 2
- **Carbon emitted:** 222 kg CO₂ eq.

### Compute infrastructure

RAD-DINO was trained on [Azure Machine Learning](https://azure.microsoft.com/en-us/products/machine-learning).

#### Hardware

We used 16 `Standard_NC96ads_A100_v4` nodes with four NVIDIA A100 (80 GB) GPUs each.

#### Software

We leveraged the code in [DINOv2](https://openreview.net/forum?id=a68SUt6zFt) for training.
We used [SimpleITK](https://simpleitk.org/) and [Pydicom](https://pydicom.github.io/) for processing of DICOM files.

## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```bibtex
@misc{perezgarcia2024raddino,
      title={{RAD-DINO}: Exploring Scalable Medical Image Encoders Beyond Text Supervision},
      author={Fernando Pérez-García and Harshita Sharma and Sam Bond-Taylor and Kenza Bouzid and Valentina Salvatelli and Maximilian Ilse and Shruthi Bannur and Daniel C. Castro and Anton Schwaighofer and Matthew P. Lungren and Maria Wetscherek and Noel Codella and Stephanie L. Hyland and Javier Alvarez-Valle and Ozan Oktay},
      year={2024},
      eprint={2401.10815},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

**APA:**

> Pérez-García, F., Sharma, H., Bond-Taylor, S., Bouzid, K., Salvatelli, V., Ilse, M., Bannur, S., Castro, D.C., Schwaighofer, A., Lungren, M.P., Wetscherek, M.T., Codella, N., Hyland, S.L., Alvarez-Valle, J., & Oktay, O. (2024). *RAD-DINO: Exploring Scalable Medical Image Encoders Beyond Text Supervision*. ArXiv, abs/2401.10815.

## Model card contact

Fernando Pérez-García ([`fperezgarcia@microsoft.com`](mailto:fperezgarcia@microsoft.com)).
