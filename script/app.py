from flask import Flask, request, jsonify
from eval_predict import get_prediction
from database import save_to_db, init_db
from data_prepar import decode_image
from keras.models import load_model
import numpy as np
import psycopg2 

# Initialize the Flask app
app = Flask(__name__)

# Load trained model
model = load_model('../data/model.h5')

# Database initialization
init_db()

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' in request.files:
        image_data = request.files['image'].read()
        
        image_array = decode_image(image_data)
        
        prediction = get_prediction(model, np.array(image_array))
        
        save_to_db(image_data, prediction) ## Save image data and prediction to the database
        
        return jsonify({'prediction': int(prediction)})
    else:
        return jsonify({'error': 'No image provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
