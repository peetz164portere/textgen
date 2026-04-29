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

> **Personal note:** I usually launch with `python server.py --api --listen --load-in-4bit` on my local machine. Works well for most GGUF models under 13B.
>
> For my RTX 3060 (12GB VRAM), adding `--gpu-memory 10` keeps things stable and leaves headroom for the OS. Without it I'd occasionally get OOM crashes mid-generation.
>
> Also found that adding `--n-gpu-layers 35` gives a nice speed boost for 7B GGUF models on this card — offloads most layers to GPU without blowing the VRAM budget.
>
> **My go-to launch command for daily use:**
> ```bash
> python server.py --api --listen --load-in-4bit --gpu-memory 10 --n-gpu-layers 35 --port 7860
> ```
> Saved this as `start.sh` in the repo root so I don't have to remember it every time.
>
> **Update:** Bumped `--n-gpu-layers` to 40 after some testing — stable on 7B and most Q4 13B models. Also switched to `--port 7861` to avoid conflicts with another local service I'm running on 7860.
>
> **Update 2:** Tried `--n-gpu-layers 43` on the Q4_K_M 13B Mistral fine-tune I've been using lately — fits fine and noticeably faster. Keeping that as my new default for 13B models. For 7B I still use 40, no real benefit going higher.
>
> **Update 3:** Switched from `--load-in-4bit` to just relying on the GGUF quantization directly — cleaner and one less thing that can go wrong. New daily command:
> ```bash
> python server.py --api --listen --gpu-memory 10 --n-gpu-layers 43 --port 7861
> ```
> Updated `start.sh` accordingly.
>
> **Update 4:** Added `--extensions sd_api_pictures` to the daily command since I've been experimenting with the image gen integration. Also worth noting — if the server hangs on startup, killing and restarting usually fixes it; seems to be a known issue with the llama.cpp backend on Windows.
> ```bash
> python server.py --api --listen --gpu-memory 10 --n-gpu-layers 43 --port 7861 --extensions sd_api_pictures
> ```
