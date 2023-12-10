"""
Module for building a basic convolutional neural network.
"""

from tensorflow import keras
from tensorflow.keras import layers


def create_model(input_shape, num_classes):
    """
    Create a sequential model.

    Args:
        input_shape (tuple): Shape of the input data.
        num_classes (int): Number of classes.

    Returns:
        keras.Sequential: The created model.
    """
    model = keras.Sequential([
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ])
    return model
