"""Utility functions for general use."""
import os
import tarfile
import zipfile
from ctypes import ArgumentError

import kaggle
import requests


class HttpDownloader:
    """Implements download from GitHub"""

    def download(self, url: str, dest: str, extract: bool = False, headers=None):

        # Guard statement:
        if not dest or not url:
            raise ArgumentError("url and dest parameters are required.")

        if not os.path.exists(dest):
            os.mkdir(dest)

        file_name = os.path.basename(url)
        with requests.get(url, stream=True, headers=headers) as r:
            r.raise_for_status()
            with open(os.path.join(dest, file_name), "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        # Guard statment: If extraction not required, done
        if not extract:
            return

        if file_name.endswith(".zip"):
            with zipfile.ZipFile(os.path.join(dest, file_name)) as zfile:
                zfile.extractall(dest)
        else:
            with tarfile.open(os.path.join(dest, file_name)) as tfile:
                tfile.extractall(dest)


class KaggleDownloader:
    """Implements download of datasets from Kaggle urls"""

    def download(
        self, url: str, dest: str, extract: bool = False, headers=None, **kwargs
    ):
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(path=dest, dataset=url, unzip=extract)


def download_data_file(url: str, dest: str, **kwargs):
    # Default Downloader:
    clz = kwargs.get("clz", HttpDownloader)
    print(f"Using {clz.__name__} to download {url} to {dest}")
    clz().download(url=url, dest=dest, **kwargs)
