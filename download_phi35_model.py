#!/usr/bin/env python3
"""
Download Phi-3.5 Mini Instruct ONNX model from Hugging Face.
This script downloads the model files needed for ONNX Runtime GenAI.
"""

import os
import requests
import sys
from pathlib import Path
from tqdm import tqdm

# Model repository and files
MODEL_REPO = "lokinfey/Phi-3.5-mini-instruct-onnx-cpu"
BASE_URL = f"https://huggingface.co/{MODEL_REPO}/resolve/main"
MODEL_DIR = Path("models/phi3.5-onnx")

# Files to download
FILES_TO_DOWNLOAD = [
    "model.onnx",
    "tokenizer.json",
    "tokenizer_config.json",
    "special_tokens_map.json",
    "model.onnx.data",
    "config.json",
    "generation_config.json"  # May not exist, but try
]

def download_file(url: str, dest_path: Path, desc: str = "") -> bool:
    """Download a file with progress bar."""
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))

        with open(dest_path, 'wb') as file, tqdm(
            desc=desc,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                pbar.update(size)

        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def main():
    """Main download function."""
    print(f"Downloading Phi-3.5 Mini Instruct ONNX model to {MODEL_DIR}")

    # Create model directory
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    success_count = 0
    total_files = len(FILES_TO_DOWNLOAD)

    for filename in FILES_TO_DOWNLOAD:
        url = f"{BASE_URL}/{filename}"
        dest_path = MODEL_DIR / filename
        desc = f"Downloading {filename}"

        print(f"\nDownloading {filename}...")
        if download_file(url, dest_path, desc):
            print(f"✓ Successfully downloaded {filename}")
            success_count += 1
        else:
            print(f"✗ Failed to download {filename}")
            # Continue with other files

    print(f"\nDownload complete: {success_count}/{total_files} files downloaded successfully")

    # Check if we have the essential files
    essential_files = ["model.onnx", "tokenizer.json"]
    essential_present = all((MODEL_DIR / f).exists() for f in essential_files)

    if essential_present:
        print("✓ Essential model files are present. Model should be ready to use.")
        return True
    else:
        print("✗ Essential model files are missing. Model may not work properly.")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\nDownload interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)