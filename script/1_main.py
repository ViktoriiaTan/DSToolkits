"""
The core module for organizing data loading, model creation,
training, and evaluation.
"""
import numpy as np
import wandb
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
    
    # Retrieve and log the Git commit hash
    git_commit_hash = os.getenv('GIT_COMMIT_HASH', 'N/A')
    wandb.config.update({"git_commit_hash": git_commit_hash})
    
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

    # Train the model
    print("Training model...")
    
    # Train the model and log the metric
    history = train_model(model,
    x_train, y_train,
    epochs=10,
    batch_size=128,
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
    
    # Convert predictions to label indices
    preds = np.argmax(y_pred, axis=1)
    y_true = np.argmax(y_test, axis=1)
    
    # Calculate F1 Score
    f1 = f1_score(y_true, preds, average='weighted')

    # Log the F1 score to Weights & Biases
    wandb.log({'f1_score': f1})
    
    # Log the confusion matrix
    wandb.log({"conf_mat": wandb.plot.confusion_matrix(probs=None,
                                                   y_true=y_true, 
                                                   preds=preds,
                                                   class_names=[str(i) for i in range(10)])})
    
    # Convert predictions to single column
    if y_pred.ndim > 1 and y_pred.shape[1] > 1:
        # Convert one-hot encoded predictions to class indices
        y_pred = np.argmax(y_pred, axis=1).reshape(-1, 1)
        
    # Create a W&B artifact for predictions
    predictions_artifact = wandb.Artifact('predictions', type='predictions')
    
    # Add the predictions to the artifact
    predictions_table = wandb.Table(data=y_pred, columns=["Predictions"])
    predictions_artifact.add(predictions_table, "prediction_results")
    
    # Log the artifact to W&B
    wandb.log_artifact(predictions_artifact)
    
if __name__ == "__main__":
    main()
