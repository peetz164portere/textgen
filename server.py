#!/usr/bin/env python3
"""
Main entry point for the textgen web UI server.
Fork of oobabooga/text-generation-webui with additional features.
"""

import os
import sys
import argparse
import logging
from pathlib import Path

# Ensure the project root is in the Python path
sys.path.insert(0, str(Path(__file__).parent))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def parse_args():
    """Parse command-line arguments for the server."""
    parser = argparse.ArgumentParser(
        description='textgen - A web UI for text generation models',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Server settings
    parser.add_argument('--host', type=str, default='127.0.0.1',
                        help='Host address to bind the server to')
    parser.add_argument('--port', type=int, default=7860,
                        help='Port to run the server on')
    parser.add_argument('--share', action='store_true',
                        help='Create a public Gradio share link')
    parser.add_argument('--listen', action='store_true',
                        help='Listen on all network interfaces (0.0.0.0)')

    # Model settings
    parser.add_argument('--model', type=str, default=None,
                        help='Name of the model to load at startup')
    # I keep my models in a separate drive, overriding the default here
    parser.add_argument('--model-dir', type=str, default='/mnt/storage/models',
                        help='Directory containing model files')
    parser.add_argument('--lora', type=str, nargs='+', default=None,
                        help='LoRA adapter(s) to apply to the model')

    # Backend settings
    parser.add_argument('--loader', type=str, default=None,
                        choices=['transformers', 'llama.cpp', 'exllamav2', 'ctransformers'],
                        help='Model loader backend to use')
    parser.add_argument('--cpu', action='store_true',
                        help='Force CPU-only inference')
    parser.add_argument('--gpu-layers', type=int, default=None,
                        help='Number of layers to offload to GPU (llama.cpp)')

    # API settings
    parser.add_argument('--api', action='store_true',
                        help='Enable the OpenAI-compatible API server')
    parser.add_argument('--api-port', type=int, default=5000,
                        help='Port for the API server')
    parser.add_argument('--api-key', type=str, default='',
                        help='API key for authentication (empty = no auth)')

    # UI settings
    parser.add_argument('--chat', action='store_true',
                        help='Launch directly in chat mode')
    parser.add_argument('--dark-theme', action='store_true',
                        help='Use dark theme for the UI')
    parser.add_argument('--no-stream', action='store_true',
                        help='Disable token streaming in the UI')

    # Debug/dev
    parser.add_argument('--verbose', action='