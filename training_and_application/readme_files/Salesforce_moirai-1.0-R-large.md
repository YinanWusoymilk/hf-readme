---
license: cc-by-nc-4.0
pipeline_tag: time-series-forecasting
tags:
  - time series
  - forecasting
  - pretrained models
  - foundation models
  - time series foundation models
  - time-series
---

# Moirai-1.0-R-Large

Moirai, the Masked Encoder-based Universal Time Series Forecasting Transformer is a Large Time Series Model pre-trained on [LOTSA data](https://huggingface.co/datasets/Salesforce/lotsa_data).
For more details on the Moirai architecture, training, and results, please refer to the [paper](https://arxiv.org/abs/2402.02592).

<p align="center">
  <img src="figures/architecture.png" width="100%">
  <br />
  <span>
    Fig. 1: Overall architecture of Moirai. Visualized is a 3-variate time series, where variates 0 and 1 are target variables (i.e. to be forecasted, and variate 2 is a dynamic covariate (values in forecast horizon known). Based on a patch size of 64, each variate is patchified into 3 tokens. The patch embeddings along with sequence and variate id are fed into the Transformer. The shaded patches represent the forecast horizon to be forecasted, whose corresponding output representations are mapped into the mixture distribution parameters.
  </span>
</p>

## Usage

To perform inference with Moirai, install the uni2ts library from our [GitHub repo](https://github.com/SalesforceAIResearch/uni2ts).

1. Clone repository:
```shell
git clone https://github.com/SalesforceAIResearch/uni2ts.git
cd uni2ts
```

2) Create virtual environment:
```shell
virtualenv venv
. venv/bin/activate
```

3) Build from source:
```shell
pip install -e '.[notebook]'
```

4) Create a `.env` file:
```shell
touch .env
```

A simple example to get started:

```python
import torch
import matplotlib.pyplot as plt
import pandas as pd
from gluonts.dataset.pandas import PandasDataset
from gluonts.dataset.split import split

from uni2ts.eval_util.plot import plot_single
from uni2ts.model.moirai import MoiraiForecast, MoiraiModule


SIZE = "small"  # model size: choose from {'small', 'base', 'large'}
PDT = 20  # prediction length: any positive integer
CTX = 200  # context length: any positive integer
PSZ = "auto"  # patch size: choose from {"auto", 8, 16, 32, 64, 128}
BSZ = 32  # batch size: any positive integer
TEST = 100  # test set length: any positive integer

# Read data into pandas DataFrame
url = (
    "https://gist.githubusercontent.com/rsnirwan/c8c8654a98350fadd229b00167174ec4"
    "/raw/a42101c7786d4bc7695228a0f2c8cea41340e18f/ts_wide.csv"
)
df = pd.read_csv(url, index_col=0, parse_dates=True)

# Convert into GluonTS dataset
ds = PandasDataset(dict(df))

# Split into train/test set
train, test_template = split(
    ds, offset=-TEST
)  # assign last TEST time steps as test set

# Construct rolling window evaluation
test_data = test_template.generate_instances(
    prediction_length=PDT,  # number of time steps for each prediction
    windows=TEST // PDT,  # number of windows in rolling window evaluation
    distance=PDT,  # number of time steps between each window - distance=PDT for non-overlapping windows
)

# Prepare pre-trained model by downloading model weights from huggingface hub
model = MoiraiForecast(
    module=MoiraiModule.from_pretrained(f"Salesforce/moirai-1.0-R-{SIZE}"),
    prediction_length=PDT,
    context_length=CTX,
    patch_size=PSZ,
    num_samples=100,
    target_dim=1,
    feat_dynamic_real_dim=ds.num_feat_dynamic_real,
    past_feat_dynamic_real_dim=ds.num_past_feat_dynamic_real,
)

predictor = model.create_predictor(batch_size=BSZ)
forecasts = predictor.predict(test_data.input)

input_it = iter(test_data.input)
label_it = iter(test_data.label)
forecast_it = iter(forecasts)

inp = next(input_it)
label = next(label_it)
forecast = next(forecast_it)

plot_single(
    inp, 
    label, 
    forecast, 
    context_length=200,
    name="pred",
    show_label=True,
)
plt.show()
```

## The Moirai Family

| # Model | # Parameters |
| :---: | :---: |
| [Moirai-1.0-R-Small](https://huggingface.co/Salesforce/moirai-1.0-R-small) | 14m |
| [Moirai-1.0-R-Base](https://huggingface.co/Salesforce/moirai-1.0-R-base) | 91m |
| [Moirai-1.0-R-Large](https://huggingface.co/Salesforce/moirai-1.0-R-large) | 311m |

## Citation

If you're using Uni2TS in your research or applications, please cite it using this BibTeX:

```markdown
@article{woo2024unified,
  title={Unified Training of Universal Time Series Forecasting Transformers},
  author={Woo, Gerald and Liu, Chenghao and Kumar, Akshat and Xiong, Caiming and Savarese, Silvio and Sahoo, Doyen},
  journal={arXiv preprint arXiv:2402.02592},
  year={2024}
}
```