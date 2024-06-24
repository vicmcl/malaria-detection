from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from pathlib import Path

def checkpoint(fname, patience = 5):
    weights_path = Path('../weights')
    callbacks = [
        EarlyStopping(patience = patience),    # Stop the training after 20 iterations without improvement
        ModelCheckpoint(                        # Save the weights giving the best results in a file
            filepath = weights_path / fname,
            monitor = "val_loss",
            save_best_only = True,
        )
    ]

    return callbacks