import requests
import time
from tensorflow.keras.datasets import mnist
import io
from PIL import Image

# Load MNIST dataset
(_, _), (x_test, _) = mnist.load_data()

# Select one sample image from the dataset
image_array = x_test[0]

# Convert the array to an image
image = Image.fromarray(image_array)
buffered = io.BytesIO()
image.save(buffered, format="JPEG")
img_str = buffered.getvalue()
# Save the image to file system
image_file_path = 'mnist_sample.jpg'
image.save(image_file_path, format="JPEG")

# The URL to your Flask app's /predict endpoint
url = 'http://flask_app:5000/predict'

# Function to make a POST request to the Flask app
def make_request(url, img_str):
    try:
        files = {'image': ('image.jpg', img_str, 'image/jpeg')}
        response = requests.post(url, files=files)
        if response.status_code == 200:
            print("Prediction:", response.json())
        else:
            print("Error:", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return False
    return True

# Retry parameters
max_retries = 5
wait_seconds = 5

# Retry loop
for i in range(max_retries):
    print(f"Attempt {i+1} to connect to Flask app")
    if make_request(url, img_str):
        break
    print(f"Waiting for {wait_seconds} seconds before retrying...")
    time.sleep(wait_seconds)

print("Script completed")

