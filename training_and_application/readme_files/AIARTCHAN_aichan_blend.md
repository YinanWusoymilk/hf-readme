---
license: other
tags:
- stable-diffusion
- aiartchan
---

Mixed stable diffusion models from the ai image channel and elsewhere. Feel free to download.


## file download code example

```python
# urlretrieve, no progressbar
from urllib.request import urlretrieve
from huggingface_hub import hf_hub_url

repo_id = "AIARTCHAN/aichan_blend"
filename = "AbyssOrangeMix2_nsfw-pruned.safetensors"
url = hf_hub_url(repo_id, filename)
urlretrieve(url, filename)
```

```python
# with tqdm, urllib
import shutil
from urllib.request import urlopen
from huggingface_hub import hf_hub_url
from tqdm import tqdm

repo_id = "AIARTCHAN/aichan_blend"
filename = "AbyssOrangeMix2_nsfw-pruned.safetensors"
url = hf_hub_url(repo_id, filename)

with urlopen(url) as resp:
    total = int(resp.headers.get("Content-Length", 0))
    with tqdm.wrapattr(
        resp, "read", total=total, desc="Download..."
    ) as src:
        with open(filename, "wb") as dst:
            shutil.copyfileobj(src, dst)
```

```python
# with tqdm, requests
import shutil
import requests
from huggingface_hub import hf_hub_url
from tqdm import tqdm

repo_id = "AIARTCHAN/aichan_blend"
filename = "AbyssOrangeMix2_nsfw-pruned.safetensors"
url = hf_hub_url(repo_id, filename)

resp = requests.get(url, stream=True)
total = int(resp.headers.get("Content-Length", 0))
with tqdm.wrapattr(
    resp.raw, "read", total=total, desc="Download..."
) as src:
    with open(filename, "wb") as dst:
        shutil.copyfileobj(src, dst)
```