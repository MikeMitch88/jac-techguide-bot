
# 🤖 TechGuide Bot - AI-Powered Programming Language Advisor

[![JAC](https://img.shields.io/badge/JAC-0.5+-blue.svg)](https://jaclang.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29-red.svg)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

> An intelligent conversational chatbot that helps beginners discover the perfect programming language based on their interests and career goals. Built with JAC, FastAPI, Streamlit, and powered by Google Gemini AI.

![TechGuide Bot Demo](https://via.placeholder.com/800x400/667eea/ffffff?text=TechGuide+Bot+Demo)

---

## ✨ Features

- 🧠 **AI-Powered Reasoning** - Uses Google Gemini to understand complex user queries
- 💬 **ChatGPT-Style Interface** - Modern, conversational UI built with Streamlit
- 🎯 **12+ Technology Categories** - Covers web, mobile, data science, game dev, DevOps, and more
- 🗺️ **Personalized Learning Paths** - Get 3-4 phase roadmaps with timelines
- 💼 **Career Guidance** - Realistic job market insights and career paths
- 📚 **Curated Resources** - Hand-picked tutorials, docs, and learning platforms
- ⚡ **Real-Time API** - RESTful backend with FastAPI
- 🔄 **Session Management** - Maintains conversation context
- 🎨 **Beautiful UI** - Modern gradient design with smooth animations

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- pip
- Virtual environment (recommended)

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/jac-techguide-bot.git
cd jac-techguide-bot

# 2. Create virtual environment
python -m venv .env
source .env/bin/activate  # Linux/Mac
# .env\Scripts\activate   # Windows

# 3. Install backend dependencies
cd backend
pip install -r requirements.txt

# 4. Install frontend dependencies
cd ../frontend
pip install -r requirements.txt
```

### Running the Application

**Terminal 1 - Start Backend:**
```bash
cd backend
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Start Frontend:**
```bash
cd frontend
streamlit run app.py
```

**Access the app:**
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## 🏗️ Architecture
```
┌──────────────┐      HTTP/REST      ┌──────────────┐      Python      ┌──────────────┐
│  Streamlit   │ ──────────────────> │   FastAPI    │ ──────────────> │  JAC Engine  │
│   Frontend   │ <────────────────── │   Backend    │ <────────────── │   (Logic)    │
│  (port 8501) │      JSON           │  (port 8000) │                 └──────────────┘
└──────────────┘                     └──────┬───────┘
                                            │ API Call
                                            ▼
                                     ┌──────────────┐
                                     │  Gemini AI   │
                                     │  (Reasoning) │
                                     └──────────────┘
```

### Tech Stack

- **Core Logic**: JAC (Jac Programming Language)
- **Backend**: FastAPI + Python
- **Frontend**: Streamlit
- **AI**: Google Gemini 2.0 Flash
- **Deployment**: Docker (optional)

---

## 📁 Project Structure
```
jac-techguide-bot/
├── backend/
│   ├── jac_modules/
│   │   ├── nodes.jac          # Node definitions
│   │   ├── walkers.jac        # Walker logic
│   │   └── main_api.jac       # API entry point
│   ├── server.py              # FastAPI application
│   ├── ai_helper.py           # Gemini AI integration
│   └── requirements.txt       # Python dependencies
├── frontend/
│   ├── app.py                 # Streamlit UI
│   └── requirements.txt       # Frontend dependencies
├── .streamlit/
│   └── config.toml            # Streamlit theme
├── main.jac                   # Original CLI version
├── TOOLKIT.md                 # Complete documentation
├── README.md                  # This file
└── .gitignore
```

---

## 💡 Usage Examples

### Simple Query
```
User: "I want to build websites"
Bot: Recommends JavaScript with React/Node.js ecosystem
```

### Complex Query
```
User: "I'm 30 and want to transition into tech within 6 months. What should I learn?"
Bot: Provides personalized career-focused recommendation considering age, timeline, and job market
```

### Comparison Query
```
User: "Compare Python vs JavaScript for backend development"
Bot: Gives honest pros/cons with use case recommendations
```

### Career Question
```
User: "What programming language pays the most in 2025?"
Bot: Provides salary insights and market demand analysis
```

---

## 🎯 Supported Technologies

### Languages & Frameworks
1. **JavaScript** - Web development (React, Vue, Angular, Node.js)
2. **Python** - Data science, ML, AI, backend
3. **Swift/Kotlin** - Native mobile (iOS/Android)
4. **C#/C++** - Game development (Unity/Unreal)
5. **Go** - Cloud, microservices, DevOps
6. **Rust** - Systems programming, performance
7. **TypeScript** - Type-safe web development
8. **SQL/Databases** - Data engineering
9. **Java** - Enterprise backend, Android
10. **Ruby/Rails** - Rapid web development
11. **PHP/Laravel** - Web development, WordPress
12. **Cybersecurity** - Ethical hacking, pentesting

---

## 🔧 Configuration

### API Keys

Create `backend/.env`:
```env
GEMINI_API_KEY=your-gemini-api-key-here
AI_MODEL=models/gemini-2.0-flash
```

Get your API key: https://aistudio.google.com/app/apikey

### Backend URL

In `frontend/app.py`, update if needed:
```python
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
```

---

## 🧪 Testing

### Test Backend
```bash
# Health check
curl http://localhost:8000/health

# Get recommendation
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "I want to build mobile apps"}'
```

### Test AI Helper
```bash
cd backend
python ai_helper.py
```

---

## 🐳 Docker Deployment (Optional)
```bash
# Build
docker build -t techguide-bot .

# Run
docker run -p 8000:8000 -p 8501:8501 techguide-bot
```

---

## 📊 API Endpoints

### `GET /health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "service": "TechGuide Bot API",
  "version": "3.0.0",
  "ai_enabled": true
}
```

### `POST /chat`
Main chat endpoint

**Request:**
```json
{
  "message": "I want to learn data science",
  "session_id": "optional-uuid"
}
```

**Response:**
```json
{
  "status": "ok",
  "response": "For data science, I recommend Python...",
  "ai_powered": true,
  "session_id": "abc-123"
}
```

### `POST /techguide`
Direct recommendation endpoint

**Request:**
```json
{
  "choice": "2",
  "session_id": "optional-uuid"
}
```

**Response:**
```json
{
  "status": "ok",
  "language": "Python",
  "reason": "Python is ideal for data science...",
  "resources": ["Python.org", "DataCamp", ...],
  "metadata": {
    "difficulty": "Beginner",
    "estimated_time": "4-6 months",
    "learning_path": [...],
    "career_paths": [...]
  }
}
```

### `GET /history/{session_id}`
Get conversation history

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **JAC Team** - For creating an amazing language
- **Moringa School** - For the capstone project structure
- **Google Gemini** - For AI capabilities
- **FastAPI & Streamlit** - For excellent frameworks

---

## 📧 Contact

**Author:** [Your Name]  
**Email:** your.email@example.com  
**GitHub:** [@yourusername](https://github.com/yourusername)  
**LinkedIn:** [Your LinkedIn](https://linkedin.com/in/yourprofile)

---

## 🌟 Show Your Support

If this project helped you, please give it a ⭐️!

---

## 📸 Screenshots

### Chat Interface
![Chat Interface](https://via.placeholder.com/800x400/667eea/ffffff?text=Chat+Interface)

### Recommendation Display
![Recommendation](https://via.placeholder.com/800x400/764ba2/ffffff?text=Recommendation+Display)

### Learning Path
![Learning Path](https://via.placeholder.com/800x400/1e3a5f/ffffff?text=Learning+Path+Timeline)

---

## 🗺️ Roadmap

- [x] Core chatbot functionality
- [x] AI-powered reasoning
- [x] 12+ technology categories
- [x] Learning paths
- [x] REST API
- [x] Modern UI
- [ ] User authentication
- [ ] Save conversation history to database
- [ ] Voice input/output
- [ ] Mobile app
- [ ] Multi-language support
- [ ] Analytics dashboard

---

## 📚 Documentation

- [Complete Toolkit Documentation](TOOLKIT.md)
- [API Documentation](http://localhost:8000/docs) (when running)
- [JAC Language Guide](https://docs.jaclang.org)

---

**Built with ❤️ using JAC, FastAPI, Streamlit, and AI**

*Making programming language selection intelligent and accessible for everyone.*
