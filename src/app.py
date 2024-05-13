from flask import Flask, request, jsonify
from remla2024_team9_lib_ml import tokenize_url  # Ensure the package is correctly named
from tensorflow.keras.models import load_model
app = Flask(__name__)

#model_url = "https://www.dropbox.com/scl/fi/5giiub4m0aq0gvvnst7d9/best_model.keras?rlkey=nmmwvz9dz7fqjxfo5ll71lfy1&st=ttqjdxc5&dl=0"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'url' in data:
        # Tokenize the URL
        model = load_model("models/best_model.keras") # Change to loading model from cloud
        tokenized_input = tokenize_url(data['url'])
        output = model.predict(tokenized_input)
        # Dummy response for now, replace with actual model prediction logic
        response = {"status": "received", "tokenized": output}
    else:
        response = {"error": "URL not provided"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
