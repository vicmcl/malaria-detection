import shutil
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path


def main():

    # Define constants
    DATASET = "iarunava/cell-images-for-detecting-malaria"
    DATA_PATH = Path('../data/')

    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Download the dataset
    api.dataset_download_files(DATASET, path=DATA_PATH, unzip=True)

    # Remove the nested copy of the directory
    nested_dir = DATA_PATH / 'cell_images' / 'cell_images'
    if nested_dir.exists():
        shutil.rmtree(nested_dir)

if __name__ == '__main__':
    main()