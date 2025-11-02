# TechGuide Bot API Documentation

## Overview
FastAPI-enabled JAC backend service for programming language recommendations.

## Architecture
- **JAC Layer**: Core business logic (nodes, walkers, graph)
- **FastAPI Layer**: HTTP wrapper exposing REST endpoints
- **Python Helpers**: Optional classification utilities

## Quick Start

### Prerequisites
- Python 3.10+
- JAC installed (`pip install jaclang`)
- Virtual environment (recommended)

### Installation
```bash
# Create virtual environment
python -m venv .env
source .env/bin/activate  # Linux/Mac
# .env\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Verify JAC installation
jac --version
```

### Running the Service

**Method 1: Direct FastAPI**
```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

**Method 2: Python script**
```bash
python server.py
```

**Method 3: Docker**
```bash
docker build -t techguide-api .
docker run -p 8000:8000 techguide-api
```

### Verify Installation
```bash
curl http://localhost:8000/health
```

## API Endpoints

### 1. Health Check
**GET** `/health`

Response:
```json
{
  "status": "healthy",
  "service": "TechGuide Bot API",
  "version": "2.0",
  "timestamp": "2025-11-02T10:30:00"
}
```

### 2. Get Recommendation
**POST** `/techguide`

Request:
```json
{
  "choice": "2",
  "session_id": "optional-session-id"
}
```

Response (Success):
```json
{
  "status": "ok",
  "language": "Python",
  "reason": "Python is ideal for data science with libraries like Pandas, NumPy, and TensorFlow",
  "resources": [
    "Python.org tutorials",
    "DataCamp",
    "Kaggle Learn"
  ],
  "metadata": {
    "difficulty": "Beginner",
    "estimated_time": "4-6 months",
    "session_id": "abc-123"
  }
}
```

Response (Error):
```json
{
  "status": "error",
  "message": "Invalid or missing choice. Please send choice 1-4."
}
```

### 3. Classify Free Text
**POST** `/classify`

Request:
```json
{
  "text": "I want to build mobile apps"
}
```

Response:
```json
{
  "status": "ok",
  "language": "Swift/Kotlin",
  "reason": "Swift (iOS) and Kotlin (Android) are the best choices for mobile app development",
  "resources": [...],
  "classification": {
    "input_text": "I want to build mobile apps",
    "classified_choice": "3",
    "confidence": 0.8,
    "scores": {"1": 0, "2": 0, "3": 4, "4": 0}
  }
}
```

## Testing with cURL
```bash
# Health check
curl http://localhost:8000/health

# Get recommendation
curl -X POST http://localhost:8000/techguide \
  -H "Content-Type: application/json" \
  -d '{"choice": "3"}'

# Classify text
curl -X POST http://localhost:8000/classify \
  -H "Content-Type: application/json" \
  -d '{"text": "I love analyzing data and building ML models"}'

# Invalid choice
curl -X POST http://localhost:8000/techguide \
  -H "Content-Type: application/json" \
  -d '{"choice": "9"}'
```

## Testing with Python
```python
import requests

# Get recommendation
response = requests.post(
    "http://localhost:8000/techguide",
    json={"choice": "1"}
)
print(response.json())

# Classify text
response = requests.post(
    "http://localhost:8000/classify",
    json={"text": "I want to make games"}
)
print(response.json())
```

## Interactive API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure
```
jac-techguide-bot/
├── jac_modules/
│   ├── nodes.jac           # Node definitions
│   ├── walkers.jac         # Walker logic
│   └── main_api.jac        # API entry point
├── server.py               # FastAPI server
├── classifier.py           # Python helper
├── requirements.txt
├── Dockerfile
└── README_API.md
```

## Production Deployment

### Environment Variables
```bash
export HOST=0.0.0.0
export PORT=8000
export LOG_LEVEL=INFO
```

### Docker Compose
```yaml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - LOG_LEVEL=INFO
    restart: unless-stopped
```

### Monitoring
- Logs: `tail -f /var/log/techguide-api.log`
- Metrics: Access `/health` endpoint

## Troubleshooting

### JAC Not Found
```bash
pip install --upgrade jaclang
jac --version
```

### Port Already in Use
```bash
lsof -i :8000
kill -9 <PID>
```

### Import Errors
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

## License
MIT License

## Support
For issues, contact: support@techguide.com