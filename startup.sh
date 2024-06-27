#!/bin/bash

gcloud auth activate-service-account --key-file=/app/gcloud_key.json

mkdir -p /app/models

gsutil cp $MODEL_URL /app/models/model.keras

gsutil cp gs://remla_group_9_model/tokenizer.pkl /app/models/tokenizer.pkl

echo "Models downloaded successfully."