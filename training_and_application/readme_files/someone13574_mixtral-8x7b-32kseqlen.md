### NOTICE: Mistral has uploaded the model to their HuggingFace organization. Please prefer it instead. [Link](https://huggingface.co/mistralai/Mixtral-8x7B-v0.1)

Upload of the model released here: https://twitter.com/MistralAI/status/1733150512395038967

The model is split into 11 8gb files because of file size limits and it was easier to handle. You need to concatenate them together after downloading. The final hash of the model should match the one in the RELEASE file.

To recombine: `cat consolidated.00.pth-split0 consolidated.00.pth-split1 consolidated.00.pth-split2 consolidated.00.pth-split3 consolidated.00.pth-split4 consolidated.00.pth-split5 consolidated.00.pth-split6 consolidated.00.pth-split7 consolidated.00.pth-split8 consolidated.00.pth-split9 consolidated.00.pth-split10 > consolidated.00.pth`