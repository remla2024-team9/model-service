from flask import Flask, request, jsonify
from remla2024_team9_lib_ml import tokenize_url  # Ensure the package is correctly named

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if 'url' in data:
        # Tokenize the URL
        tokenized_input = tokenize_url(data['url'])
        # Dummy response for now, replace with actual model prediction logic
        response = {"status": "received", "tokenized": tokenized_input}
    else:
        response = {"error": "URL not provided"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
