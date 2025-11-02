# 🚀 TechGuide Bot - Advanced Conversational AI Platform

Complete setup guide for the ChatGPT-style programming language advisor.

## Architecture
```
┌─────────────────┐      WebSocket/HTTP     ┌──────────────────┐
│   Streamlit     │ ──────────────────────> │   FastAPI        │
│   Chat UI       │ <────────────────────── │   Server         │
│  (port 8501)    │        JSON/REST        │  (port 8000)     │
└─────────────────┘                         └──────────────────┘
                                                      │
                                                      │ Executes
                                                      ▼
                                            ┌──────────────────┐
                                            │  JAC Walkers     │
                                            │  (AI Logic)      │
                                            └──────────────────┘
```

## Features

✅ ChatGPT-style conversational interface
✅ Real-time AI-powered recommendations
✅ Personalized learning paths
✅ Career guidance
✅ Session management
✅ Chat history export
✅ Responsive design
✅ Modern gradient UI

## Quick Start

### 1. Install Dependencies
```bash
# Backend
pip install -r backend/requirements.txt

# Frontend
pip install -r frontend/requirements.txt
```

### 2. Start Backend
```bash
cd backend
uvicorn server:app --reload --port 8000
```

### 3. Start Frontend
```bash
cd frontend
streamlit run app.py
```

### 4. Access the App

- **Frontend**: http://localhost:8501
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## Usage

### Chat Interface

1. Open the Streamlit app
2. Type your interest in the chat input (e.g., "I want to build mobile apps")
3. Get instant AI-powered recommendations with:
   - Language recommendation
   - Detailed reasoning
   - Learning path timeline
   - Career opportunities
   - Curated resources

### Quick Actions

Use the sidebar buttons for instant recommendations:
- 🌐 Web Development
- 📊 Data Science
- 📱 Mobile Apps
- 🎮 Game Development

### Features

- **Smart Classification**: AI understands natural language
- **Learning Paths**: Step-by-step roadmap
- **Session Tracking**: Persistent conversations
- **Export Chat**: Download your conversation
- **Backend Status**: Real-time health monitoring

## API Endpoints

### POST /chat
```json
{
  "message": "I want to build websites",
  "session_id": "optional-uuid"
}
```

### POST /techguide
```json
{
  "choice": "1",
  "session_id": "optional-uuid"
}
```

### GET /history/{session_id}
Returns conversation history

### GET /health
Health check endpoint

## Customization

### Change Backend URL

In `frontend/app.py`:
```python
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
```

Or set environment variable:
```bash
export BACKEND_URL=http://your-backend-url:8000
```

### Modify Theme

Edit `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#0a0a0a"
```

## Troubleshooting

### Backend Not Connecting

1. Check if backend is running:
```bash
   curl http://localhost:8000/health
```

2. Check backend logs for errors

3. Verify CORS is enabled in FastAPI

### Chat Not Responding

1. Check backend status in sidebar (🔌 Backend Status)
2. Click "🔄 Check Status" button
3. Ensure network connectivity

## Production Deployment

### Docker
```bash
# Build and run with Docker Compose
docker-compose up -d
```

### Environment Variables
```bash
export BACKEND_URL=https://api.yourdomain.com
export LOG_LEVEL=INFO
```

## License

MIT License

## Support

For issues: https://github.com/yourusername/techguide-bot/issues