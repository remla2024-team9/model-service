# Prediction Service API

This repository contains a Flask application designed to predict data based on a provided URL input. The application utilizes a pre-trained model and a tokenizer to process and predict data efficiently.

## Application Overview

The Flask application (`app.py`) serves as a prediction service. It accepts POST requests containing URLs, processes these URLs through a tokenization step, and then uses a loaded model to predict the outcome based on the tokenized data. The prediction result is then returned as a JSON response.

## Getting Started

## Running with Docker

To run the application in a Docker container, the image is publicly available and can be easily pulled and run with Docker without needing to manage dependencies manually.

### Pulling the Docker Image

You can pull the latest version of the Docker image directly from GitHub Container Registry by using the following command:

```bash
`docker pull ghcr.io/remla2024-team9/model-service:latest`


### Running the Docker Image

Once you have the image, you can run it locally on your machine. If the application inside the Docker container runs on port 5000, you need to map this port to a port on your local machine. Here’s how you can run the application using Docker:

`docker run -p 5000:5000 ghcr.io/remla2024-team9/model-service:latest`

This command starts the container and maps port 5000 of the container to port 5000 on your host, making the application accessible through your local machine at http://localhost:5000.

