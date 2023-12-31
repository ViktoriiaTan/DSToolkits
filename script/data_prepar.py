"""
Module for preprocessing the MNIST dataset, including data scaling,
reshaping  and conversion of class vectors to binary matrices.
"""

import numpy as np
from tensorflow import keras


def preproc(x_train, y_train, x_test, y_test):
    """
    Preprocess the MNIST dataset.
    Args:
        x_train (numpy.array): Training data.
        y_train (numpy.array): Training labels.
        x_test (numpy.array): Test data.
        y_test (numpy.array): Test labels.

    Returns:
    Tuple of numpy arrays: (x_train, y_train), (x_test, y_test),
    num_classes, input_shape
    """
    num_classes = 10
    input_shape = (28, 28, 1)

    # Scale images to the [0, 1] range
    x_train = x_train.astype("float32") / 255
    x_test = x_test.astype("float32") / 255

    # Ensure images have shape (28, 28, 1)
    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)

    # Convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    return (x_train, y_train), (x_test, y_test), num_classes, input_shape
