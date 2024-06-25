"""
This module sets up a Flask application that predicts data based on a given model and tokenizer, 
and handles the downloading of data files from remote URLs.
"""
import os
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

MODEL_CHANGE_COUNT = Counter("model_service_model_type_change_count", "Number of times the model was changed")

#model_type=1 => normal model, model_type=2 => best_model
model_type = os.environ.get("MODEL_TYPE", "1")

model1 = load_model('../models/model.keras')
model2 = load_model("../models/best_model.keras")

model = model1 if (model_type == "1") else model2

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


@app.route("/change", methods=['POST'])
def change():
    global model, model_type

    if (model_type == "1"):
        model = model2
        model_type = "2"
    
    elif (model_type == "2"):
        model = model1
        model_type = "1"

    else:
        return jsonify({"error": "Invalid Internal State"}), 500

    MODEL_CHANGE_COUNT.inc()

    return jsonify({"current": model_type}), 200

@app.route('/metrics')
def metrics():
    return generate_latest(), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

