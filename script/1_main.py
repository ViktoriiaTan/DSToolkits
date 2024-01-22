"""
The core module for organizing data loading, model creation,
training, and evaluation.
"""
import numpy as np
import pickle
import wandb
import os
from wandb.keras import WandbCallback
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from module_io import load_mnist, save_modelh5, load_modelh5
from data_prepar import preproc
from model_architect import create_model
from train import train_model
from eval_predict import eval_model, predict


def main():
    # Initialize Weights & Biases
    wandb.init(project="mnist_digit_classification", entity="tantsuraviktoria")
    
    model_file = '../data/mnist_model.h5'
    
    # Load the data
    print("Loading data...")
    (x_train, y_train), (x_test, y_test) = load_mnist()

    # Preprocess the data
    print("Preprocessing data...")
    ((x_train, y_train),
     (x_test, y_test),
     num_classes,
     input_shape) = preproc(x_train, y_train, x_test, y_test)

    # Create the model
    print("Creating model...")
    model = create_model(input_shape, num_classes)

    # Compile the model with accuracy as a metric
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    print("Training model...")
    
    # Train the model and log the metric
    history = model.fit(
    x_train, y_train,
    validation_data=(x_test, y_test),
    epochs=10,
    callbacks=[WandbCallback()]
    )

    # Save the model
    model.save("model.h5")
    
    # Upload the model to Weights & Biases
    wandb.save("model.h5")

    # Load the model
    print("Loading model...")
    model = load_modelh5("model.h5")
    
    # Evaluate the model
    print("Evaluating model...")
    test_loss, test_accuracy = eval_model(model, x_test, y_test)
    
    # Make predictions
    y_pred = model.predict(x_test)
    
    # Convert predictions to label indices if they're in a one-hot encoded format
    preds = np.argmax(y_pred, axis=1)
    y_true = np.argmax(y_test, axis=1)
    
    # Calculate F1 Score
    f1 = f1_score(y_true, preds, average='weighted')

    # Log the F1 score to Weights & Biases
    wandb.log({'f1_score': f1})
    
    
if __name__ == "__main__":
    main()
