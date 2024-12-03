# Image Captioning App

## Overview

This application generates descriptive captions for images using advanced ML models. It processes single images or entire directories, leveraging CLIP and LLM models for accurate and contextual captions. It has NSFW captioning support with natural language. This is just an extension of the original author's efforts to improve performance. Their repo is located here: https://huggingface.co/spaces/fancyfeast/joy-caption-pre-alpha.

## Features

- Single image and batch processing
- Multiple directory support
- Custom output directory
- Adjustable batch size
- Progress tracking

## Usage

| Command | Description |
|---------|-------------|
| `python app.py image.jpg` | Process a single image |
| `python app.py /path/to/directory` | Process all images in a directory |
| `python app.py /path/to/dir1 /path/to/dir2` | Process multiple directories |
| `python app.py /path/to/dir --output /path/to/output` | Specify output directory |
| `python app.py /path/to/dir --bs 8` | Set batch size (default: 4) |

## Technical Details

- **Models**: CLIP (vision), LLM (language), custom ImageAdapter
- **Optimization**: CUDA-enabled GPU support
- **Error Handling**: Skips problematic images in batch processing

## Requirements

- Python 3.x
- PyTorch
- Transformers library
- CUDA-capable GPU (recommended)

## Installation

Windows

```bash
git clone https://huggingface.co/Wi-zz/joy-caption-pre-alpha
cd joy-caption-pre-alpha
python -m venv venv
.\venv\Scripts\activate
# Change as per https://pytorch.org/get-started/locally/
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

Linux

```bash
git clone https://huggingface.co/Wi-zz/joy-caption-pre-alpha
cd joy-caption-pre-alpha
python3 -m venv venv
source venv/bin/activate
pip3 install torch torchvision torchaudio
pip3 install -r requirements.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).