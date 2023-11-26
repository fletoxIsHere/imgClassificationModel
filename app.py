from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import cv2
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
import requests

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Load your pre-trained model
model = load_model('my_model.h5')  # Replace 'my_model.h5' with your model's filename

# Load or initialize your label encoder
label_encoder = LabelEncoder()
label_encoder.classes_ = np.load('classes.npy')  # Ensure 'classes.npy' is in the same directory

# Define the image processing and prediction function
def predict_image_from_url(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = np.frombuffer(response.content, dtype=np.uint8)
        img = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
        if img is not None:
            img = cv2.resize(img, (224, 224)) / 255.0
            prediction = model.predict(np.array([img]))
            return label_encoder.inverse_transform([np.argmax(prediction)])[0]
        else:
            return "Failed to decode image"
    else:
        return "Failed to download image"

# Define a route for the API to handle URL inputs
@app.route('/predict', methods=['POST'])
def predict_from_url():
    data = request.json
    if not data or 'url' not in data:
        return jsonify({'error': 'No URL provided'}), 400

    image_url = data['url']
    prediction = predict_image_from_url(image_url)

    return jsonify({'category': prediction})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Use debug=False in a production environment
