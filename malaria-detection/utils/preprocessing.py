from pathlib import Path
from PIL import Image
from sklearn.model_selection import train_test_split
import numpy as np

ROOT = Path('../../')
DATA_PATH = ROOT / 'data' / 'cell_images'
uninfected_path = DATA_PATH / "Uninfected"
parasitized_path = DATA_PATH / "Parasitized"


def resize_images(filepath, size = (64, 64)):
    img = Image.open(filepath).resize(size)
    return img


def normalize_images(images):
    return np.array([np.array(x) / 255 for x in images]).astype("float32")


def add_images(path, label, x, y):
    for filepath in path.iterdir():
        if filepath.name.endswith("png"):
            x.append(resize_images(filepath))
            y.append(label)
    return x, y


def preprocess_data():

    x, y = [], []
    x, y = add_images(uninfected_path, 0, x, y)
    x, y = add_images(parasitized_path, 1, x, y)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )

    x_train = normalize_images(x_train)
    x_test = normalize_images(x_test)

    return x_train, x_test, y_train, y_test