# textgen

A fork of [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) with additional features and improvements.

## Features

- Web UI for running large language models
- Support for multiple model backends (llama.cpp, ExLlamaV2, transformers, etc.)
- API endpoints compatible with OpenAI format
- Extensions system for additional functionality
- Portable releases for Windows, Linux, and macOS

## Installation

### One-click installers

Download the latest release from the [Releases](../../releases) page and run the installer for your platform.

### Manual installation

```bash
# Clone the repository
git clone https://github.com/your-org/textgen
cd textgen

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python server.py
```

Then open your browser at `http://localhost:7860`.

### Common flags

| Flag | Description |
|------|-------------|
| `--model MODEL` | Name of the model to load at startup |
| `--listen` | Listen on all network interfaces |
| `--api` | Enable the API server |
| `--port PORT` | Port to run the web UI on (default: 7860) |
| `--cpu` | Use CPU for inference |
| `--gpu-memory VRAM` | GPU memory in GiB to allocate |
| `--load-in-4bit` | Load the model in 4-bit precision |
| `--load-in-8bit` | Load the model in 8-bit precision |

For a full list of flags, run:

```bash
python server.py --help
```

## Models

Place your models in the `models/` directory. Supported formats:

- GGUF (llama.cpp)
- GPTQ
- AWQ
- EXL2 (ExLlamaV2)
- HuggingFace (safetensors / pytorch)

## API

When started with `--api`, the server exposes OpenAI-compatible endpoints at `http://localhost:5000`.

See the [API documentation](docs/API.md) for details.

## Extensions

Extensions live in the `extensions/` directory. Enable them with:

```bash
python server.py --extensions extension_name
```

## Contributing

Pull requests are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting.

## License

AGPL-3.0. See [LICENSE](LICENSE) for details.
