import io
import numpy as np
from tensorflow import keras
from PIL import Image

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
    
    
def decode_image(image_data):
    """
    Decode an image from raw data.
    
    Args:
        image_data (bytes): Raw image data.

    Returns:
        numpy.array: Decoded and preprocessed image array.
    """
    # Open the image using PIL
    image = Image.open(io.BytesIO(image_data))

    # Resize the image to 28x28 (MNIST image size) and convert to grayscale
    image = image.resize((28, 28)).convert('L')

    # Convert the image to a NumPy array and normalize it
    image_array = np.array(image) / 255.0

    return image_array

