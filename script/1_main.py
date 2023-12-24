"""
The core module for organizing data loading, model creation,
training, and evaluation.
"""

from module_io import load_mnist, save_modelh5, load_modelh5
from data_prepar import preproc
from model_architect import create_model
from train import train_model
from eval_predict import eval_model, predict
import psycopg2


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

    # Make predictions
    predictions = predict(model, x_test)

    # Print the first ten predictions
    print("First ten predictions:", predictions[:10])
    
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(
        host="postrges",
        database="milestone_3",
        user="admin",
        password="secret"
    )
    cursor = conn.cursor()

    # Save the model to the "models" table
    with open(model_file, 'rb') as f:
            model_data = f.read()
            cursor.execute("INSERT INTO models (model_data) VALUES (%s) RETURNING id;", (psycopg2.Binary(model_data),))
            model_id = cursor.fetchone()[0]
            conn.commit()

        # Close the database connection
    conn.close()


if __name__ == "__main__":
    main()
