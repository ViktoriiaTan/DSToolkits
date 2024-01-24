from flask import Flask, request, jsonify
import numpy as np
from PIL import Image
from io import BytesIO
from module_io import load_modelh5, save_to_database  

app = Flask(__name__)


# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:secret@postgres/milestone_3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)


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

        # Save image and prediction to the database 
        save_to_database(image_array, predicted_label)

        return jsonify({'prediction': int(predicted_label)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
