import psycopg2
import numpy as np
from tensorflow.keras.datasets import mnist
from PIL import Image
import io

# Function to convert image to binary data
def img_to_binary(image):
    img_byte_arr = io.BytesIO()
    Image.fromarray(image).save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="student",
    password="123456"
)
cur = conn.cursor()

# Create a table for storing images
cur.execute("""
    CREATE TABLE IF NOT EXISTS mnist_images (
        id SERIAL PRIMARY KEY,
        digit_image BYTEA NOT NULL
    )
""")
conn.commit()

# Load MNIST dataset
(x_train, _), (_, _) = mnist.load_data()

# Select one sample image from the dataset
sample_image = x_train[0]

# Convert the image to binary
binary_image = img_to_binary(sample_image)

# Insert the image into the database
cur.execute("INSERT INTO mnist_images (digit_image) VALUES (%s)", (binary_image,))
conn.commit()

# Fetch the image back
cur.execute("SELECT digit_image FROM mnist_images WHERE id = 1")
image_data = cur.fetchone()[0]

# Convert binary data to image
retrieved_image = Image.open(io.BytesIO(image_data))

# Display the image
retrieved_image.show()

# Close the connection
cur.close()
conn.close()
