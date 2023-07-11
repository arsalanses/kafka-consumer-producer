# Base image
FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY consumer.py .

# Start Kafka consumer
CMD ["sh", "-c", "python consumer.py"]
