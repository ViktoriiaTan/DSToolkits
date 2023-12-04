"""
Module for handling input and output operations, including data loading,
as well as saving and loading models.
"""

from tensorflow import keras
import numpy as np


def load_mnist():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    x_train = x_train.astype("float32") / 255
    x_test = x_test.astype("float32") / 255

    x_train = np.expand_dims(x_train, -1)
    x_test = np.expand_dims(x_test, -1)

    return (x_train, y_train), (x_test, y_test)


def save_modelh5(model, filename):
    model.save(filename)


def load_modelh5(filename):
    return keras.models.load_model(filename)
