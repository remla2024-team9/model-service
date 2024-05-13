# Prediction Service API

This repository contains a Flask application designed to predict data based on a provided URL input. The application utilizes a pre-trained model and a tokenizer to process and predict data efficiently.

## Application Overview

The Flask application (`app.py`) serves as a prediction service. It accepts POST requests containing URLs, processes these URLs through a tokenization step, and then uses a loaded model to predict the outcome based on the tokenized data. The prediction result is then returned as a JSON response.

The application also includes a `downloader.py` module, which handles the downloading of the necessary model and tokenizer files from remote URLs, ensuring that all required resources are available locally for the Flask application to function correctly.

## Getting Started

### Prerequisites

Before setting up the application, ensure that Poetry is installed on your system for dependency management. If you do not have Poetry installed, follow the instructions in the [Poetry documentation](https://python-poetry.org/docs/) to install it.

### Installation

1. **Clone the Repository**

`git clone git@github.com:remla2024-team9/model-service.git`

- Change working directory to this repository

2. **Install Dependencies**
Run the following commands to install the necessary dependencies:

`poetry install`


3. **Activate the Virtual Environment**
To activate the Poetry-created virtual environment, use:

`poetry shell`


4. **Download Required Files**
Execute the `downloader.py` to download the necessary model and tokenizer:

`python src/downloader.py`


### Running the Application

After completing the setup, start the Flask application by running:

`python src/app.py`

The application will start running on `http://localhost:5000`. You can use tools like Postman or curl to send POST requests to `http://localhost:5000/predict` with a JSON body containing a URL for prediction.

## Usage Example

Here's an example of how to send a prediction request using `curl`:

```bash
curl -X POST http://localhost:5000/predict -H 'Content-Type: application/json' -d '{"url": "http://example.com"}'
