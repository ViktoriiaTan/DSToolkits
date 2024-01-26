"""
Module for evaluating and predicting using the trained NN model.
"""


import numpy as np

def eval_model(model, x_test, y_test):
    return model.evaluate(x_test, y_test, verbose=0)


def predict(model, x_data):
    return model.predict(x_data)
    
def get_prediction(model, image_array):

    # Preprocess the image for the model
    processed_image = image_array.reshape(28, 28, 1)  # Reshape and normalize
    processed_image = processed_image.astype("float32") / 255

    # Predict using the model
    prediction_array = model.predict(np.array([processed_image]))
    prediction = np.argmax(prediction_array, axis=1)[0]

    return prediction
