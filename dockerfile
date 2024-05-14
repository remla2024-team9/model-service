# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the files necessary for Poetry
COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the entire src directory into the container at /app/src
COPY src/ /app/src

# Ensure the models directory exists
RUN mkdir -p /app/src/models

# Set the working directory to /app/src for running the Python scripts
WORKDIR /app/src

# Run the downloader to set up the models and tokenizer
RUN poetry run python downloader.py

# Set the Flask application variable
ENV FLASK_APP=app.py

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app
CMD ["poetry", "run", "python", "app.py"]
