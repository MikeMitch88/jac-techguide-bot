# Use an official Python image
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your backend code
COPY . .

# Expose port 10000 for Render
EXPOSE 10000

# Start the app
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "10000"]
