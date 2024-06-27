# Use an official Python runtime as a parent image
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    curl \
    bash 

RUN curl -sSL https://sdk.cloud.google.com | bash
ENV PATH $PATH:/root/google-cloud-sdk/bin

# Install Poetry
RUN pip install poetry

# Set the working directory to /app
WORKDIR /app

COPY . ./

RUN chmod +x startup.sh

# Install dependencies using Poetry
RUN poetry install --no-dev --no-interaction --no-ansi

WORKDIR /app/src

# Set the Flask application variable
ENV FLASK_APP=app.py

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app
CMD ["/bin/bash", "-c", "/app/startup.sh && poetry run python app.py"]
