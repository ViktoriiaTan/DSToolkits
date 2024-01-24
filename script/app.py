from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
from io import BytesIO
from module_io import load_modelh5  # Assuming you have the necessary functions in module_io

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get image data from the request
        image_data = request.get_data()
        image = Image.open(BytesIO(image_data))

        # Convert image to numpy array
        image_array = np.array(image)

        # Load the pre-trained model
        model = load_modelh5("model.h5")  # Update with your actual model loading function

        # Make prediction
        prediction = model.predict(np.expand_dims(image_array, axis=0))

        # Assuming prediction is a one-hot encoded vector, convert it to a label
        predicted_label = np.argmax(prediction)

        # Save image and prediction to the database (You need to implement this)
        # ...

        return jsonify({'prediction': int(predicted_label)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
