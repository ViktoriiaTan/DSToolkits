"""
Module for evaluating the trained neural network model.
"""


def eval_model(model, x_test, y_test):
    return model.evaluate(x_test, y_test, verbose=0)
