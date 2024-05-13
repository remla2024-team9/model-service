"""
This module handles the downloading of the model and tokenizer from remote URLs.
"""

import os
import requests

# Constants for URL downloads
URL_MODEL = "https://www.dropbox.com/scl/fi/uzfys196rsd0axqx3o3om/model.keras"
"?rlkey=obet9rdk3x6kfkfnmghvft33h&st=bur0qvl7&dl=0"
URL_TOKENIZER = "https://www.dropbox.com/scl/fi/agkgy9nnwrs5kclnvz9ld/tokenizer.pkl"
"?rlkey=dczufz4fv7d0dyg6hlz3mjqyg&st=wy13pwe7&dl=0"

def download_file(url, local_filename):
    """Downloads a file from a URL and saves it locally."""
    if not os.path.exists(local_filename):
        print(f"Downloading {local_filename}...")
        with requests.get(url, stream=True, timeout=30) as response:
            response.raise_for_status()
            os.makedirs(os.path.dirname(local_filename), exist_ok=True)
            with open(local_filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        print(f"Downloaded the file: {local_filename}")
    else:
        print(f"File already exists: {local_filename}")

def setup_models():
    """Set up the dataset by downloading and saving necessary files (if they don't already exist)"""
    files = {
        "model.keras": URL_MODEL,
        "tokenizer.pkl": URL_TOKENIZER
    }
    extract_path = "models/"

    # Download each file if not already downloaded
    for file_name, url in files.items():
        if not os.path.exists(os.path.join(extract_path, file_name)):
            local_path = os.path.join(extract_path, file_name)
            download_file(url, local_path)

if __name__ == "__main__":
    setup_models()