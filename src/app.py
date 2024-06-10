"""
This module sets up a Flask application that predicts data based on a given model and tokenizer, 
and handles the downloading of data files from remote URLs.
"""
import pickle

from flask import Flask, request, jsonify
from keras.models import load_model
from remla2024_team9_lib_ml import tokenize_url
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

model = load_model('../models/model.keras')

# Load the model and tokenizer
tokenizer = pickle.load(open('../models/tokenizer.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'url' in data:
        tokenized_input = tokenize_url(tokenizer, data['url'])
        prediction = model.predict(tokenized_input)
        response = {"prediction": prediction.tolist()}
    else:
        response = {"error": "URL not provided"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
