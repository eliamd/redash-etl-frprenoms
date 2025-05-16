#https://www.insee.fr/fr/statistiques/fichier/7633685/dpt2022_csv.zip

import pandas as pd
import os
import zipfile
import requests
from io import BytesIO
from pathlib import Path
# Load environment variables
DATA_DIR = Path('data/raw')

def download_and_extract_zip(url, extract_to):
    """
    Download a zip file from a URL and extract its contents to a specified directory.

    Parameters:
    url (str): The URL of the zip file to download.
    extract_to (str): The directory to extract the contents of the zip file to.
    """
    response = requests.get(url)
    with zipfile.ZipFile(BytesIO(response.content)) as z:
        z.extractall(extract_to)
        print(f"Extracted {len(z.namelist())} files to {extract_to}")
def extract_data():
    """
    Extracts data from a zip file and saves it to a specified directory.

    The function downloads a zip file from a given URL, extracts its contents,
    and saves the extracted files to a specified directory.
    """
    url = "https://www.insee.fr/fr/statistiques/fichier/7633685/dpt2022_csv.zip"
    extract_to = 'data/raw'

    # Create the directory if it doesn't exist
    os.makedirs(extract_to, exist_ok=True)

    # Download and extract the zip file
    download_and_extract_zip(url, extract_to)
    # List the files in the directory
    files = os.listdir(extract_to)
    print(f"Files in {extract_to}: {files}")
if __name__ == "__main__":
    extract_data()
    # Check if the data directory exists
    if DATA_DIR.exists():
        print(f"Data directory exists: {DATA_DIR}")
    else:
        print(f"Data directory does not exist: {DATA_DIR}")

