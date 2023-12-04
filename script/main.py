"""
The core module for organizing data loading, model creation,
training, and evaluation.
"""

from module_io import load_mnist, save_modelh5, load_modelh5
from data_prepar import preproc
from model_architect import create_model
from train import train_model
from eval_model import eval_model


def main():
    model_file = '../data/mnist_model.h5'
    # Load the data
    (x_train, y_train), (x_test, y_test) = load_mnist()

    # Preprocess the data
    ((x_train, y_train),
     (x_test, y_test),
     num_classes,
     input_shape) = preproc(x_train, y_train, x_test, y_test)

    # Create the model
    model = create_model(input_shape, num_classes)

    # Train the model
    train_model(model, x_train, y_train)

    # Save the model
    save_modelh5(model, model_file)

    # Load the model
    model = load_modelh5(model_file)

    # Evaluate the model
    test_loss, test_accuracy = eval_model(model, x_test, y_test)

    print(f"Test Loss: {test_loss}")
    print(f"Test Accuracy: {test_accuracy}")


if __name__ == "__main__":
    main()
