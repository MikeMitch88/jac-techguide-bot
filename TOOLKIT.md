# TechGuide Bot - Beginner's Toolkit with JAC

**Moringa AI Capstone Project**  
**Author:** [Your Name]  
**Date:** November 2, 2025  
**Technology:** JAC (Jac Programming Language)

---

## 📋 Table of Contents

1. [Title & Objective](#title--objective)
2. [Quick Summary of JAC](#quick-summary-of-jac)
3. [System Requirements](#system-requirements)
4. [Installation & Setup](#installation--setup)
5. [Minimal Working Example](#minimal-working-example)
6. [AI Prompt Journal](#ai-prompt-journal)
7. [Common Issues & Fixes](#common-issues--fixes)
8. [Architecture Overview](#architecture-overview)
9. [References & Resources](#references--resources)

---

## 1. Title & Objective

### Project Title
**TechGuide Bot: AI-Powered Programming Language Advisor**

### Technology Chosen
**JAC (Jac Programming Language)** - A modern, data-spatial programming language designed for AI applications.

### Why JAC?
- Unique paradigm combining OOP with graph-based data structures
- Built-in support for AI/ML workflows
- Perfect for building conversational agents and recommendation systems
- Growing ecosystem with strong community support

### End Goal
Build an intelligent chatbot that:
- Recommends programming languages based on user interests
- Provides personalized learning paths with AI reasoning
- Offers career guidance and resources
- Serves as a REST API backend (FastAPI) with modern web UI (Streamlit)

---

## 2. Quick Summary of JAC

### What is JAC?

JAC is a revolutionary programming language that introduces **Data-Spatial Programming (DSP)**. Unlike traditional languages, JAC allows you to:

- **Navigate through data like physical spaces** using walkers
- **Define nodes** that represent data locations or entities
- **Connect nodes with edges** to model relationships
- **Create walkers** that traverse the graph and execute logic

### Real-World Use Cases

1. **Conversational AI**: Build chatbots with state machines represented as nodes
2. **Recommendation Systems**: Model user preferences and content as graphs
3. **Data Pipelines**: Process data by traversing through transformation nodes
4. **Social Networks**: Naturally represent connections between users

### Example: Traditional vs JAC Approach

**Traditional (Python):**
```python
user = {"name": "Alice", "interests": ["web", "mobile"]}
recommendation = recommend_language(user["interests"])
```

**JAC (Data-Spatial):**
```jac
node User {
    has interests: list = [];
}

walker Recommender {
    can suggest with User entry {
        # Navigate and process
    }
}
```

The JAC approach naturally models the problem domain as interconnected data.

---

## 3. System Requirements

### Operating System
- **Linux** (Ubuntu 24.04 - tested)
- macOS 12+ (compatible)
- Windows 10+ with WSL2 (compatible)

### Software Requirements
- **Python**: 3.10 or higher
- **pip**: Latest version
- **Virtual Environment**: venv or conda
- **Git**: For version control
- **Text Editor**: VS Code, nano, or vim

### Hardware Requirements
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 2GB free space
- **Processor**: Any modern CPU
- **Internet**: Required for API calls and package installation

### Python Packages
```txt
jaclang>=0.5.0
fastapi==0.104.1
uvicorn[standard]==0.24.0
streamlit==1.29.0
google-generativeai>=0.3.0
pydantic==2.5.0
requests==2.31.0
```

---

## 4. Installation & Setup

### Step 1: Set Up Virtual Environment
```bash
# Create project directory
mkdir jac-techguide-bot
cd jac-techguide-bot

# Create virtual environment
python -m venv .env
source .env/bin/activate  # Linux/Mac
# .env\Scripts\activate    # Windows

# Upgrade pip
pip install --upgrade pip
```

### Step 2: Install JAC
```bash
# Install JacLang
pip install jaclang

# Verify installation
jac --version
```

**Expected output:**
```
Jac version: 0.5.x
```

### Step 3: Install Backend Dependencies
```bash
# Create requirements file
cat > backend/requirements.txt << 'EOL'
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
jaclang>=0.5.0
google-generativeai>=0.3.0
setuptools>=65.0.0
python-dotenv==1.0.0
protobuf==4.25.5
EOL

# Install
pip install -r backend/requirements.txt
```

### Step 4: Install Frontend Dependencies
```bash
# Create requirements file
cat > frontend/requirements.txt << 'EOL'
streamlit==1.29.0
requests==2.31.0
EOL

# Install
pip install -r frontend/requirements.txt
```

### Step 5: Configure API Keys
```bash
# Create .env file (optional - keys are in code)
cat > backend/.env << 'EOL'
GEMINI_API_KEY=your-key-here
AI_MODEL=models/gemini-2.0-flash
EOL
```

---

## 5. Minimal Working Example

### Basic JAC Hello World

**File: `hello.jac`**
```jac
# Simple JAC program demonstrating core concepts

node GreetingNode {
    has message: str = "Hello from JAC!";
    
    can greet with entry {
        print(self.message);
    }
}

walker HelloWalker {
    can start with `root entry {
        greeting = GreetingNode();
        root ++> greeting;
        visit [-->];
    }
}

with entry {
    root spawn HelloWalker();
}
```

**Run it:**
```bash
jac run hello.jac
```

**Expected output:**
```
Hello from JAC!
```

### Simple Recommendation System (Core Concept)

**File: `simple_recommend.jac`**
```jac
node InterestNode {
    has name: str = "";
    has recommendation: str = "";
}

walker RecommendWalker {
    has user_interest: str = "web";
    
    can recommend with `root entry {
        if self.user_interest == "web" {
            print("Recommendation: JavaScript");
        } elif self.user_interest == "data" {
            print("Recommendation: Python");
        }
    }
}

with entry {
    root spawn RecommendWalker(user_interest="web");
}
```

**Run it:**
```bash
jac run simple_recommend.jac
```

---

## 6. AI Prompt Journal

### Prompt 1: Understanding JAC Basics
**Prompt:**
```
Explain the core concepts of JAC programming language: What are walkers, 
nodes, and edges? How do they work together? Provide a simple analogy for beginners.
```

**AI Response Summary:**
- Nodes = Buildings (data locations)
- Edges = Roads (connections)
- Walkers = Travelers (agents that navigate and process)

**Evaluation:** ✅ Excellent - Helped understand the fundamental paradigm shift from traditional programming.

---

### Prompt 2: Chatbot Architecture
**Prompt:**
```
How would I structure a conversational chatbot in JAC using walkers and nodes? 
Describe the flow where nodes represent conversation states.
```

**AI Response Summary:**
- Create nodes for each conversation state (Welcome, Ask, Recommend, etc.)
- Use walker to navigate between states based on user input
- Store context in walker properties

**Evaluation:** ✅ Very helpful - Provided clear mental model for implementation.

---

### Prompt 3: JAC Syntax Basics
**Prompt:**
```
Show me the basic syntax for defining a node and a walker in JAC. 
Include a simple example with code comments.
```

**AI Response Summary:**
- Node definition: `node NodeName { has property: type; }`
- Walker definition: `walker WalkerName { can method with node entry {} }`
- Entry point: `with entry { }`

**Evaluation:** ✅ Perfect - Had working code examples I could test immediately.

---

### Prompt 4: Building the Chatbot
**Prompt:**
```
Help me create a conversational chatbot in JAC that recommends programming 
languages based on user interests. Use nodes for states and walker for navigation.
```

**AI Response Summary:**
- Provided complete architecture with multiple nodes
- Showed how to pass data between walker and nodes
- Included error handling patterns

**Evaluation:** ✅ Excellent - Accelerated development significantly.

---

### Prompt 5: FastAPI Integration
**Prompt:**
```
How do I integrate a JAC backend with FastAPI to expose REST endpoints? 
Show me how to call JAC code from Python.
```

**AI Response Summary:**
- Use subprocess to call `jac run`
- Alternative: Import JAC modules directly with `jac_import`
- Return JSON responses from walkers using `report`

**Evaluation:** ✅ Good - Led to working API integration.

---

### Prompt 6: Debugging JAC Syntax
**Prompt:**
```
I'm getting 'Missing COLON' error in JAC when using 'for i, option in enumerate()'. 
What's the correct for loop syntax in JAC?
```

**AI Response Summary:**
- JAC doesn't support tuple unpacking in for loops like Python
- Use `for idx in range(len(list))` instead
- Access elements with `list[idx]`

**Evaluation:** ✅ Critical - Solved blocking syntax error.

---

### Prompt 7: AI Enhancement with Gemini
**Prompt:**
```
How do I integrate Google Gemini API with my JAC chatbot to provide 
AI-powered responses? Show me the Python integration code.
```

**AI Response Summary:**
- Use `google-generativeai` library
- Configure with API key
- Use `GenerativeModel` class with proper model name
- Handle responses and errors

**Evaluation:** ✅ Excellent - Enabled intelligent reasoning in chatbot.

---

### Key Learning: How AI Improved Productivity

**Before AI:**
- Trial and error with syntax
- Reading through extensive documentation
- Debugging without context

**With AI:**
- Rapid prototyping with examples
- Context-aware error solutions
- Architecture suggestions
- **Estimated time saved: 60-70%**

---

## 7. Common Issues & Fixes

### Issue #1: JAC For Loop Syntax Error

**Error Message:**
```
Error: Missing COLON at line 22
for i, option in enumerate(self.options, 1)
```

**Cause:**  
JAC doesn't support Python-style tuple unpacking in for loops.

**Solution:**
```jac
# ❌ Wrong (Python style)
for i, option in enumerate(self.options, 1) {
    print(f"{i}. {option}");
}

# ✅ Correct (JAC style)
for idx in range(len(self.options)) {
    print(f"{idx + 1}. {self.options[idx]}");
}
```

---

### Issue #2: Module Import Errors

**Error Message:**
```
ModuleNotFoundError: No module named 'jaclang'
```

**Cause:**  
JAC not installed or wrong virtual environment active.

**Solution:**
```bash
# Verify you're in virtual environment
which python  # Should show .env/bin/python

# Reinstall JAC
pip install --upgrade jaclang

# Verify
jac --version
```

---

### Issue #3: FastAPI CORS Errors

**Error Message:**
```
Access to fetch blocked by CORS policy
```

**Cause:**  
Frontend (Streamlit) can't access backend due to CORS restrictions.

**Solution:**
```python
# In server.py
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

### Issue #4: Gemini API Model Not Found

**Error Message:**
```
404 models/gemini-pro is not found for API version v1beta
```

**Cause:**  
Using outdated model name. Google updated their model names.

**Solution:**
```python
# ❌ Old model name
model = genai.GenerativeModel('gemini-pro')

# ✅ Current model names
model = genai.GenerativeModel('models/gemini-2.0-flash')
# or
model = genai.GenerativeModel('models/gemini-2.5-flash')
```

**To find available models:**
```python
import google.generativeai as genai
for m in genai.list_models():
    print(m.name)
```

---

### Issue #5: Protobuf Version Conflicts

**Error Message:**
```
ERROR: streamlit requires protobuf<5, but you have protobuf 5.29.5
```

**Cause:**  
Dependency conflict between Streamlit and Google AI packages.

**Solution:**
```bash
# Downgrade protobuf to compatible version
pip install protobuf==4.25.5

# Or update Streamlit
pip install --upgrade streamlit
```

---

### Issue #6: Backend Not Responding

**Symptom:**  
Streamlit shows "Cannot connect to backend"

**Troubleshooting Steps:**
```bash
# 1. Check if backend is running
curl http://localhost:8000/health

# 2. Check backend logs for errors
# Look in terminal where uvicorn is running

# 3. Verify correct URL in frontend
# In frontend/app.py, check BACKEND_URL

# 4. Restart both services
# Terminal 1: uvicorn server:app --reload
# Terminal 2: streamlit run frontend/app.py
```

---

## 8. Architecture Overview

### System Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                        USER BROWSER                         │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP/WebSocket
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                   STREAMLIT FRONTEND                        │
│                   (port 8501)                               │
│  • Chat Interface                                           │
│  • Session Management                                       │
│  • UI Rendering                                             │
└────────────────────┬────────────────────────────────────────┘
                     │ REST API (JSON)
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    FASTAPI BACKEND                          │
│                    (port 8000)                              │
│  • HTTP Routing                                             │
│  • Session Storage                                          │
│  • Error Handling                                           │
└────────┬───────────────────────────────┬────────────────────┘
         │                               │
         │ Python calls                  │ API calls
         ▼                               ▼
┌─────────────────────┐      ┌──────────────────────────────┐
│   JAC ENGINE        │      │   GOOGLE GEMINI AI           │
│                     │      │   (models/gemini-2.0-flash)  │
│  • Walkers          │      │                              │
│  • Nodes            │      │  • Natural Language          │
│  • Graph Logic      │      │  • Classification            │
│  • Recommendations  │      │  • Reasoning                 │
└─────────────────────┘      └──────────────────────────────┘
```

### Data Flow

1. **User Input** → Streamlit captures message
2. **HTTP Request** → POST to `/chat` endpoint
3. **Backend Processing** → FastAPI receives request
4. **AI Classification** → Gemini analyzes intent
5. **JAC Logic** → Walker processes recommendation
6. **Response Generation** → Structured JSON created
7. **Frontend Display** → Streamlit renders result

---

### Project Structure
```
jac-techguide-bot/
├── backend/
│   ├── jac_modules/          # JAC source code
│   │   ├── nodes.jac         # Node definitions
│   │   ├── walkers.jac       # Walker logic
│   │   └── main_api.jac      # API entry point
│   ├── server.py             # FastAPI application
│   ├── ai_helper.py          # Gemini AI integration
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # API keys (gitignored)
├── frontend/
│   ├── app.py                # Streamlit UI
│   ├── requirements.txt      # Frontend dependencies
│   └── config.py             # Configuration
├── .streamlit/
│   └── config.toml           # Streamlit theme
├── main.jac                  # Original CLI version
├── TOOLKIT.md                # This document
├── README.md                 # Project README
└── .gitignore                # Git ignore rules
```

---

## 9. References & Resources

### Official Documentation

1. **JAC Language**
   - Official Docs: https://docs.jaclang.org
   - GitHub: https://github.com/Jaseci-Labs/jaclang
   - Examples: https://github.com/Jaseci-Labs/jaclang/tree/main/examples

2. **FastAPI**
   - Docs: https://fastapi.tiangolo.com
   - Tutorial: https://fastapi.tiangolo.com/tutorial/

3. **Streamlit**
   - Docs: https://docs.streamlit.io
   - Gallery: https://streamlit.io/gallery

4. **Google Gemini API**
   - Docs: https://ai.google.dev/docs
   - Python SDK: https://github.com/google/generative-ai-python

### Tutorials & Learning Resources

1. **JAC Programming**
   - Jaseci YouTube Channel
   - JAC Discord Community
   - Medium articles on Data-Spatial Programming

2. **Building Chatbots**
   - "Conversational AI with JAC" - Jaseci Blog
   - FastAPI + Streamlit Integration Guides

3. **API Integration**
   - Google AI Studio: https://aistudio.google.com
   - REST API Best Practices

### Community & Support

- **JAC Discord**: https://discord.gg/jaseci
- **Stack Overflow**: Tag `jaclang`
- **GitHub Discussions**: Jaseci-Labs/jaclang

### Videos & Courses

1. Introduction to JAC - Jaseci Official
2. Building AI Apps with FastAPI
3. Streamlit for Data Apps

---

## 🎓 Lessons Learned

### Technical Skills Gained

1. ✅ **JAC Programming**
   - Data-spatial programming paradigm
   - Walker-node architecture
   - Graph-based data modeling

2. ✅ **API Development**
   - RESTful API design with FastAPI
   - CORS and middleware configuration
   - Session management

3. ✅ **AI Integration**
   - Google Gemini API usage
   - Prompt engineering
   - Error handling for AI services

4. ✅ **Frontend Development**
   - Streamlit component architecture
   - Real-time chat interfaces
   - State management

5. ✅ **DevOps Basics**
   - Virtual environments
   - Dependency management
   - Multi-service coordination

### Soft Skills Developed

- **Problem Solving**: Debugging complex integration issues
- **Research**: Finding solutions with AI and documentation
- **Project Management**: Breaking down requirements into tasks
- **Communication**: Writing clear documentation

### What Worked Well

- Using AI (ChatGPT/Claude) to accelerate learning
- Iterative development with frequent testing
- Modular architecture (separation of concerns)
- Version control with Git

### What Could Be Improved

- Earlier focus on error handling
- More comprehensive testing
- Better logging and monitoring
- Performance optimization

---

## 🚀 Future Enhancements

### Planned Features

1. **Multi-language Support**
   - i18n for global users
   - Detect user language automatically

2. **User Accounts**
   - Save progress and history
   - Personalized recommendations over time

3. **Advanced AI Features**
   - Voice input/output
   - Image-based recommendations
   - Multi-turn conversations with context

4. **Analytics Dashboard**
   - Track popular technologies
   - User engagement metrics
   - A/B testing for recommendations

5. **Mobile App**
   - React Native wrapper
   - Push notifications for new resources

---

## ✅ Conclusion

This project successfully demonstrates:

- ✅ Learning a new technology (JAC) using AI assistance
- ✅ Building a functional, deployable application
- ✅ Integrating multiple technologies (JAC, FastAPI, Streamlit, Gemini AI)
- ✅ Creating comprehensive documentation
- ✅ Solving real-world problems (helping people choose programming languages)

**TechGuide Bot** showcases how modern AI tools can accelerate learning and development while building something genuinely useful for the developer community.

---

**Project Status:** ✅ Complete and Production-Ready  
**Submission Date:** November 2, 2025  
**Total Development Time:** 5 days  
**Lines of Code:** ~2,500+  
**Technologies Mastered:** 5 (JAC, FastAPI, Streamlit, Gemini AI, Python)

---

*Built with ❤️ using JAC, FastAPI, Streamlit, and AI*