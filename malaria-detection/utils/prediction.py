import numpy as np

def prediction(model, x_test, y_test):

    # Apply the model to the test dataset to get new predictions
    y_pred = model.predict(x_test)
    
    # Get the index of the 1 in the predicted labels and true labels
    y_pred_arg = np.argmax(y_pred, axis=1)
    y_test_arg = np.argmax(y_test, axis=1)

    return y_test_arg, y_pred_arg