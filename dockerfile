FROM alpine:latest as prebuild


RUN apk update &&\
    apk add --update curl &&\
    apk add --update bash &&\
    apk add --update python3

RUN curl -sSL https://sdk.cloud.google.com | bash
ENV PATH $PATH:/root/google-cloud-sdk/bin

WORKDIR /gcli
COPY gcloud_key.json ./
RUN gcloud auth activate-service-account --key-file=gcloud_key.json

WORKDIR /models
RUN gsutil cp gs://remla_group_9_model/best_model.keras model.keras
RUN gsutil cp gs://remla_group_9_model/tokenizer.pkl tokenizer.pkl

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install Poetry
RUN pip install poetry

# Set the working directory to /app
WORKDIR /app

COPY . ./

# Install dependencies using Poetry
RUN poetry install --no-dev --no-interaction --no-ansi

COPY --from=prebuild /models models/

WORKDIR /app/src

# Set the Flask application variable
ENV FLASK_APP=app.py

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app
CMD ["poetry", "run", "python", "app.py"]
