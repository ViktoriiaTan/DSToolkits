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
import numpy as np
import pickle


def init_db(cursor):
    # Create tables if they don't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS input_data (
            id SERIAL PRIMARY KEY,
            image_data BYTEA
        );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id SERIAL PRIMARY KEY,
            input_data_id INTEGER REFERENCES input_data(id),
            prediction_result TEXT
        );
    """)
    

def main():
    model_file = '../data/mnist_model.h5'
    # Database connection
    conn = psycopg2.connect(
        host="postgres",
        database="milestone_3",
        user="admin",
        password="secret"
    )
    cursor = conn.cursor()

    # Initialize database
    init_db(cursor)
    
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
    train_model(model, x_train, y_train)

    # Save the model
    print("Saving model...")
    save_modelh5(model, model_file)

    # Load the model
    print("Loading model...")
    model = load_modelh5(model_file)

    # Evaluate the model
    print("Evaluating model...")
    test_loss, test_accuracy = eval_model(model, x_test, y_test)

    print(f"Test Loss: {test_loss}")
    print(f"Test Accuracy: {test_accuracy}")
    
    # Serialize and save a sample to the database
    sample_data = pickle.dumps(x_test[0])
    cursor.execute("INSERT INTO input_data (image_data) VALUES (%s) RETURNING id;", (psycopg2.Binary(sample_data),))
    sample_id = cursor.fetchone()[0]
    conn.commit()

    # Load and deserialize the sample
    cursor.execute("SELECT image_data FROM input_data WHERE id = %s;", (sample_id,))
    loaded_sample_data = cursor.fetchone()[0]
    loaded_sample = pickle.loads(loaded_sample_data)
    
    # Make predictions
    print("Making predictions...")
    prediction = predict(model, np.array([loaded_sample]))
    print("Prediction:", prediction)

    # Save the prediction result
    cursor.execute("INSERT INTO predictions (input_data_id, prediction_result) VALUES (%s, %s);", (sample_id, str(prediction)))
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
