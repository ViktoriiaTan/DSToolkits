"""
Module for evaluating and predicting using the trained NN model.
"""


def eval_model(model, x_test, y_test):
    return model.evaluate(x_test, y_test, verbose=0)


def predict(model, x_data):
    return model.predict(x_data)
