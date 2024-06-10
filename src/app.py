"""
This module sets up a Flask application that predicts data based on a given model and tokenizer, 
and handles the downloading of data files from remote URLs.
"""
import time
import pickle
from flask import Flask, request, jsonify
from keras.models import load_model
from remla2024_team9_lib_ml import tokenize_url
from flask_cors import CORS
from prometheus_client import Counter, Gauge, Summary, generate_latest

app = Flask(__name__)
CORS(app)

# Metrics
PREDICTION_COUNT = Counter('model_service_prediction_count', 'Total number of predictions')
IN_PROGRESS_PREDICTIONS = Gauge('model_service_in_progress_predictions', 'Number of in-progress predictions')
PREDICTION_LATENCY = Summary('model_service_prediction_latency_seconds', 'Prediction latency in seconds')

model = load_model('../models/model.keras')

# Load the model and tokenizer
tokenizer = pickle.load(open('../models/tokenizer.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'url' in data:
        with IN_PROGRESS_PREDICTIONS.track_inprogress():
            start_time = time.time()
            tokenized_input = tokenize_url(tokenizer, data['url'])
            prediction = model.predict(tokenized_input)
            PREDICTION_COUNT.inc()
            PREDICTION_LATENCY.observe(time.time() - start_time)
            response = {"prediction": prediction.tolist()}
    else:
        response = {"error": "URL not provided"}
    return jsonify(response)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

