from flask import Flask, request, jsonify, render_template, url_for
from werkzeug.utils import secure_filename
from eval_predict import get_prediction
from database import save_to_db, init_db
from data_prepar import decode_image
from keras.models import load_model
import numpy as np
import psycopg2 
import os


# Initialize the Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Load trained model
model = load_model('../data/model.h5')

# Database initialization
init_db()

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' in request.files:
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            image_data = open(file_path, 'rb').read()
        
        image_array = decode_image(image_data)
        
        prediction = get_prediction(model, np.array(image_array))
        print('predict done')
        prediction = int(prediction)
        save_to_db(image_data, prediction) ## Save image data and prediction to the database
        print('saved ok')
        
        # Check if the request wants a JSON response
        if request.accept_mimetypes.best == 'application/json':
            return jsonify({'prediction': prediction})
        else:
            return render_template('result.html', prediction=prediction, image_path=file_path)
    else:
        response = jsonify({'error': 'No image provided'})
        response.status_code = 400
        return response
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
