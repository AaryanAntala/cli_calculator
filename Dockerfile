# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy application files
COPY app.py .
COPY test_calculator.py .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the calculator in interactive mode by default
CMD ["python", "app.py"]
