"""
This module sets up a Flask application that predicts data based on a given model and tokenizer, 
and handles the downloading of data files from remote URLs.
"""


import pickle
from flask import Flask, request, jsonify
from keras.models import load_model
from remla2024_team9_lib_ml import tokenize_url

app = Flask(__name__)
# Load the model and tokenizer
model = load_model('models/model.keras')
with open('models/tokenizer.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

@app.route('/predict', methods=['POST'])
def predict():
    """Receives a URL via POST request and returns the prediction from the model."""
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
