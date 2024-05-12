FROM python:3.10-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the files necessary for Poetry
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of your application
COPY . /app

CMD ["poetry", "run", "start"]
