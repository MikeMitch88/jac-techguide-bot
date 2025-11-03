
"""
Enhanced FastAPI Server with Chat Endpoints
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import logging
from datetime import datetime
import uuid
import os
import json
from collections import defaultdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Try to import AI helper
try:
    from ai_helper import ai_helper
    AI_AVAILABLE = ai_helper.is_enabled()
    logger.info(f"✅ AI Helper available: {AI_AVAILABLE}")
except Exception as e:
    AI_AVAILABLE = False
    logger.warning(f"⚠️ AI Helper not available: {e}")

# Initialize FastAPI app
app = FastAPI(
    title="TechGuide Bot API - Advanced",
    description="AI-powered conversational programming language advisor",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory session storage
sessions = defaultdict(lambda: {
    "created_at": datetime.now().isoformat(),
    "messages": [],
    "recommendations": []
})

# Request/Response Models
class ChatRequest(BaseModel):
    message: str = Field(..., description="User message")
    session_id: Optional[str] = Field(None, description="Session ID")

class TechGuideRequest(BaseModel):
    choice: Optional[str] = Field(None, description="Choice number (1-4)")
    message: Optional[str] = Field(None, description="Free text describing interest")
    session_id: Optional[str] = Field(None, description="Session ID")

class EnhancedBackend:
    """Enhanced backend with 10+ technology categories"""
    
    INTEREST_MAP = {
        "1": {
            "lang": "JavaScript",
            "reason": "JavaScript powers the modern web. Master it to build interactive frontends with React/Vue/Angular and scalable backends with Node.js. It's versatile, beginner-friendly, and has the largest developer community.",
            "difficulty": "Beginner",
            "time": "3-4 months",
            "learning_path": [
                {"phase": "Fundamentals", "duration": "4 weeks", "topics": ["Variables, Functions, DOM", "ES6+ features", "Async/Promises", "Fetch API"]},
                {"phase": "Frontend Frameworks", "duration": "6 weeks", "topics": ["React ecosystem", "State management (Redux/Context)", "Component architecture", "Routing & Forms"]},
                {"phase": "Backend & Full-Stack", "duration": "6 weeks", "topics": ["Node.js & Express", "REST APIs", "Database integration", "Authentication"]},
                {"phase": "Real Projects", "duration": "4 weeks", "topics": ["E-commerce site", "Social media clone", "Real-time chat app", "Deploy to Vercel/Heroku"]}
            ],
            "career_paths": ["Frontend Developer", "Full-Stack Developer", "React Developer", "Node.js Backend Engineer", "JavaScript Architect"]
        },
        "2": {
            "lang": "Python",
            "reason": "Python dominates data science, AI/ML, automation, and backend development. Its simple syntax makes it perfect for beginners, while its powerful libraries (NumPy, Pandas, TensorFlow, Django) make it a professional powerhouse.",
            "difficulty": "Beginner",
            "time": "4-6 months",
            "learning_path": [
                {"phase": "Core Python", "duration": "3 weeks", "topics": ["Syntax, Data structures", "OOP, Functions", "File I/O, Error handling", "Modules & packages"]},
                {"phase": "Data Science Stack", "duration": "8 weeks", "topics": ["NumPy & Pandas", "Matplotlib & Seaborn", "SQL & databases", "Statistical analysis"]},
                {"phase": "Machine Learning", "duration": "8 weeks", "topics": ["Scikit-learn fundamentals", "Supervised/Unsupervised learning", "Model evaluation", "TensorFlow/PyTorch intro"]},
                {"phase": "Applied Projects", "duration": "5 weeks", "topics": ["Kaggle competitions", "Predictive analytics", "NLP project", "Computer vision basics"]}
            ],
            "career_paths": ["Data Scientist", "ML Engineer", "AI Researcher", "Python Backend Developer", "Data Analyst", "Automation Engineer"]
        },
        "3": {
            "lang": "Swift/Kotlin",
            "reason": "Swift (iOS) and Kotlin (Android) are the official languages for native mobile development. Build blazing-fast, beautiful apps that leverage platform-specific features. High demand, great salaries, and direct access to billions of users.",
            "difficulty": "Intermediate",
            "time": "6-9 months",
            "learning_path": [
                {"phase": "Language Mastery", "duration": "6 weeks", "topics": ["Swift/Kotlin syntax", "OOP & protocols", "Memory management", "Concurrency basics"]},
                {"phase": "Platform Development", "duration": "8 weeks", "topics": ["UIKit/SwiftUI or Jetpack Compose", "Navigation & lifecycle", "Networking & APIs", "Local data persistence"]},
                {"phase": "Advanced Features", "duration": "6 weeks", "topics": ["Push notifications", "Core Data/Room", "Camera & media", "App architecture (MVVM/MVI)"]},
                {"phase": "Ship Apps", "duration": "8 weeks", "topics": ["3-5 portfolio apps", "App Store optimization", "TestFlight/Play Console", "User feedback iteration"]}
            ],
            "career_paths": ["iOS Developer", "Android Developer", "Mobile Architect", "Cross-Platform Developer", "Mobile Team Lead"]
        },
        "4": {
            "lang": "C#/C++",
            "reason": "Game dev powerhouses! C# with Unity dominates indie and mobile games with its accessibility. C++ with Unreal Engine powers AAA titles with cutting-edge graphics. Both offer creative careers in a $200B+ industry.",
            "difficulty": "Intermediate",
            "time": "6-12 months",
            "learning_path": [
                {"phase": "Language & Math", "duration": "8 weeks", "topics": ["C#/C++ fundamentals", "OOP concepts", "Vectors & matrices", "Physics basics"]},
                {"phase": "Engine Fundamentals", "duration": "10 weeks", "topics": ["Unity/Unreal interface", "GameObject systems", "Physics engines", "Lighting & materials"]},
                {"phase": "Game Mechanics", "duration": "10 weeks", "topics": ["Player controllers", "AI & pathfinding", "Animation systems", "UI/UX for games"]},
                {"phase": "Complete Games", "duration": "12 weeks", "topics": ["2D platformer", "3D action game", "Multiplayer basics", "Polish & publish"]}
            ],
            "career_paths": ["Game Developer", "Unity Engineer", "Unreal Developer", "Gameplay Programmer", "Technical Artist", "Engine Programmer"]
        },
        "5": {
            "lang": "Go (Golang)",
            "reason": "Go is Google's language for building fast, concurrent, cloud-native systems. Perfect for microservices, APIs, DevOps tools, and distributed systems. Simple syntax, powerful concurrency, and blazing performance make it ideal for backend infrastructure.",
            "difficulty": "Intermediate",
            "time": "4-6 months",
            "learning_path": [
                {"phase": "Go Fundamentals", "duration": "4 weeks", "topics": ["Syntax & types", "Goroutines & channels", "Error handling", "Testing"]},
                {"phase": "Backend Development", "duration": "6 weeks", "topics": ["HTTP servers", "REST APIs", "Database integration", "Middleware patterns"]},
                {"phase": "Cloud & DevOps", "duration": "6 weeks", "topics": ["Docker containers", "Kubernetes basics", "CI/CD pipelines", "Microservices"]},
                {"phase": "Production Systems", "duration": "4 weeks", "topics": ["gRPC services", "Distributed systems", "Monitoring & logging", "Deploy to cloud"]}
            ],
            "career_paths": ["Backend Engineer", "DevOps Engineer", "Site Reliability Engineer", "Cloud Architect", "Infrastructure Engineer"]
        },
        "6": {
            "lang": "Rust",
            "reason": "Rust delivers C++-level performance with memory safety guarantees. No garbage collector, no data races. Ideal for systems programming, embedded systems, WebAssembly, blockchain, and performance-critical applications. Steep learning curve but massive long-term payoff.",
            "difficulty": "Advanced",
            "time": "8-12 months",
            "learning_path": [
                {"phase": "Ownership & Borrowing", "duration": "6 weeks", "topics": ["Memory safety", "Lifetimes", "Move semantics", "Borrow checker"]},
                {"phase": "Systems Programming", "duration": "8 weeks", "topics": ["Concurrency", "Unsafe Rust", "FFI", "Performance optimization"]},
                {"phase": "Real Applications", "duration": "10 weeks", "topics": ["CLI tools", "Web servers", "WebAssembly", "Embedded systems"]},
                {"phase": "Advanced Topics", "duration": "8 weeks", "topics": ["Async/await", "Macros", "Blockchain dev", "Open source contribution"]}
            ],
            "career_paths": ["Systems Programmer", "Blockchain Developer", "Performance Engineer", "Embedded Systems Engineer", "WebAssembly Developer"]
        },
        "7": {
            "lang": "TypeScript",
            "reason": "TypeScript is JavaScript with superpowers - static typing prevents bugs and improves developer experience. Essential for large-scale applications, it's used by Microsoft, Google, and Airbnb. If you know JavaScript, TypeScript is a natural next step.",
            "difficulty": "Intermediate",
            "time": "2-3 months (assuming JS knowledge)",
            "learning_path": [
                {"phase": "TypeScript Basics", "duration": "3 weeks", "topics": ["Type system", "Interfaces", "Generics", "Utility types"]},
                {"phase": "Frontend with TS", "duration": "4 weeks", "topics": ["React + TypeScript", "Type-safe APIs", "Component typing", "Advanced patterns"]},
                {"phase": "Backend with TS", "duration": "4 weeks", "topics": ["Node.js + TypeScript", "Express typing", "ORM integration", "Testing"]},
                {"phase": "Production Ready", "duration": "3 weeks", "topics": ["Build tooling", "Strict mode", "Monorepos", "Deploy full-stack app"]}
            ],
            "career_paths": ["TypeScript Developer", "Full-Stack Engineer", "Frontend Architect", "Node.js Engineer"]
        },
        "8": {
            "lang": "SQL & Database Management",
            "reason": "Every application needs data storage. Master SQL for relational databases (PostgreSQL, MySQL) and understand NoSQL (MongoDB, Redis). Data is the foundation of modern software - database skills are universally valuable across all tech roles.",
            "difficulty": "Beginner-Intermediate",
            "time": "3-5 months",
            "learning_path": [
                {"phase": "SQL Fundamentals", "duration": "4 weeks", "topics": ["SELECT queries", "JOINs", "Aggregations", "Subqueries"]},
                {"phase": "Database Design", "duration": "4 weeks", "topics": ["Normalization", "Indexes", "Constraints", "Transactions"]},
                {"phase": "Advanced SQL", "duration": "4 weeks", "topics": ["Window functions", "CTEs", "Performance tuning", "Stored procedures"]},
                {"phase": "NoSQL & Modern", "duration": "4 weeks", "topics": ["MongoDB", "Redis caching", "Graph databases", "Data modeling"]}
            ],
            "career_paths": ["Database Administrator", "Data Engineer", "Backend Developer", "Data Analyst", "Database Architect"]
        },
        "9": {
            "lang": "Java",
            "reason": "Java runs everywhere - from Android apps to enterprise backends. Used by banks, e-commerce giants, and Android. Strong typing, mature ecosystem, and massive job market make it a safe, lucrative choice. Spring Boot makes modern Java development enjoyable.",
            "difficulty": "Intermediate",
            "time": "5-7 months",
            "learning_path": [
                {"phase": "Core Java", "duration": "6 weeks", "topics": ["OOP principles", "Collections", "Exceptions", "Generics", "Lambda expressions"]},
                {"phase": "Spring Framework", "duration": "8 weeks", "topics": ["Spring Boot", "REST APIs", "JPA & Hibernate", "Security"]},
                {"phase": "Enterprise Patterns", "duration": "6 weeks", "topics": ["Microservices", "Messaging (Kafka)", "Caching", "Testing"]},
                {"phase": "Production Apps", "duration": "6 weeks", "topics": ["CI/CD", "Docker", "Cloud deployment", "Monitoring"]}
            ],
            "career_paths": ["Java Backend Developer", "Android Developer", "Enterprise Architect", "DevOps Engineer", "Java Team Lead"]
        },
        "10": {
            "lang": "Ruby (Ruby on Rails)",
            "reason": "Ruby on Rails revolutionized web development with 'convention over configuration'. Build full-stack apps incredibly fast. Perfect for startups, MVPs, and rapid prototyping. Companies like GitHub, Shopify, and Airbnb were built on Rails.",
            "difficulty": "Beginner",
            "time": "4-6 months",
            "learning_path": [
                {"phase": "Ruby Language", "duration": "3 weeks", "topics": ["Ruby syntax", "Blocks & iterators", "OOP in Ruby", "Gems"]},
                {"phase": "Rails Framework", "duration": "8 weeks", "topics": ["MVC pattern", "ActiveRecord", "Routing", "Views & Helpers"]},
                {"phase": "Advanced Rails", "duration": "6 weeks", "topics": ["Authentication", "APIs", "ActionCable (WebSockets)", "Background jobs"]},
                {"phase": "Deploy & Scale", "duration": "4 weeks", "topics": ["Heroku deployment", "Testing (RSpec)", "Performance", "Real startup app"]}
            ],
            "career_paths": ["Rails Developer", "Full-Stack Engineer", "Startup CTO", "Backend Developer"]
        },
        "11": {
            "lang": "PHP (Laravel)",
            "reason": "PHP powers 77% of websites (WordPress, Facebook started here). Modern PHP with Laravel is elegant, fast, and productive. Massive freelance market, easy deployment, and mature ecosystem. Great for web agencies and freelancers.",
            "difficulty": "Beginner",
            "time": "4-5 months",
            "learning_path": [
                {"phase": "PHP Basics", "duration": "3 weeks", "topics": ["Syntax", "OOP", "Error handling", "Composer"]},
                {"phase": "Laravel Framework", "duration": "6 weeks", "topics": ["Routing", "Eloquent ORM", "Blade templates", "Middleware"]},
                {"phase": "Advanced Laravel", "duration": "5 weeks", "topics": ["APIs", "Authentication", "Queues", "Testing"]},
                {"phase": "Professional Dev", "duration": "4 weeks", "topics": ["Payment integration", "Real-time features", "Deploy", "Client projects"]}
            ],
            "career_paths": ["PHP Developer", "Laravel Specialist", "WordPress Developer", "Freelance Developer", "Web Agency Developer"]
        },
        "12": {
            "lang": "Cybersecurity & Ethical Hacking",
            "reason": "Learn to think like an attacker to defend systems. Master penetration testing, network security, and vulnerability assessment. High demand, excellent pay, and you're always learning. Python, Bash, and networking knowledge required.",
            "difficulty": "Advanced",
            "time": "8-12 months",
            "learning_path": [
                {"phase": "Foundations", "duration": "6 weeks", "topics": ["Networking basics", "Linux/Bash", "Python scripting", "Security concepts"]},
                {"phase": "Offensive Security", "duration": "10 weeks", "topics": ["Penetration testing", "Web vulnerabilities", "Network attacks", "Exploitation"]},
                {"phase": "Defense & Response", "duration": "8 weeks", "topics": ["Security monitoring", "Incident response", "Forensics", "SIEM tools"]},
                {"phase": "Certifications", "duration": "8 weeks", "topics": ["CEH prep", "CompTIA Security+", "Real penetration tests", "Bug bounties"]}
            ],
            "career_paths": ["Penetration Tester", "Security Analyst", "Ethical Hacker", "Security Engineer", "Bug Bounty Hunter"]
        }
    }
    
    RESOURCES_MAP = {
        "JavaScript": [
            "MDN Web Docs - https://developer.mozilla.org",
            "freeCodeCamp - https://freecodecamp.org",
            "JavaScript.info - https://javascript.info",
            "React Official Docs - https://react.dev",
            "Node.js Docs - https://nodejs.org/docs"
        ],
        "Python": [
            "Python.org Tutorial - https://docs.python.org/3/tutorial/",
            "Real Python - https://realpython.com",
            "DataCamp - https://datacamp.com",
            "Kaggle Learn - https://kaggle.com/learn",
            "Fast.ai - https://fast.ai"
        ],
        "Swift/Kotlin": [
            "Apple Developer - https://developer.apple.com",
            "Android Developer - https://developer.android.com",
            "Ray Wenderlich - https://raywenderlich.com",
            "Hacking with Swift - https://hackingwithswift.com"
        ],
        "C#/C++": [
            "Unity Learn - https://learn.unity.com",
            "Unreal Docs - https://docs.unrealengine.com",
            "GameDev.tv - https://gamedev.tv",
            "Microsoft Learn - https://learn.microsoft.com"
        ],
        "Go (Golang)": [
            "Go Official Tour - https://go.dev/tour",
            "Go by Example - https://gobyexample.com",
            "Uber Go Style Guide - https://github.com/uber-go/guide",
            "Golang.org Docs - https://golang.org/doc"
        ],
        "Rust": [
            "The Rust Book - https://doc.rust-lang.org/book/",
            "Rust by Example - https://doc.rust-lang.org/rust-by-example/",
            "Rustlings - https://github.com/rust-lang/rustlings",
            "Let's Get Rusty - https://letsgetrusty.com"
        ],
        "TypeScript": [
            "TypeScript Handbook - https://typescriptlang.org/docs/handbook/",
            "TypeScript Deep Dive - https://basarat.gitbook.io/typescript/",
            "Total TypeScript - https://totaltypescript.com",
            "Execute Program - https://executeprogram.com"
        ],
        "SQL & Database Management": [
            "Mode SQL Tutorial - https://mode.com/sql-tutorial/",
            "PostgreSQL Tutorial - https://postgresqltutorial.com",
            "MongoDB University - https://university.mongodb.com",
            "SQLBolt - https://sqlbolt.com"
        ],
        "Java": [
            "Oracle Java Tutorials - https://docs.oracle.com/javase/tutorial/",
            "Spring Boot Docs - https://spring.io/guides",
            "Baeldung - https://baeldung.com",
            "Java Brains - https://javabrains.io"
        ],
        "Ruby (Ruby on Rails)": [
            "Ruby Docs - https://ruby-doc.org",
            "Rails Guides - https://guides.rubyonrails.org",
            "The Odin Project - https://theodinproject.com",
            "GoRails - https://gorails.com"
        ],
        "PHP (Laravel)": [
            "Laravel Docs - https://laravel.com/docs",
            "PHP The Right Way - https://phptherightway.com",
            "Laracasts - https://laracasts.com",
            "PHP.net Manual - https://php.net/manual"
        ],
        "Cybersecurity & Ethical Hacking": [
            "TryHackMe - https://tryhackme.com",
            "HackTheBox - https://hackthebox.com",
            "Cybrary - https://cybrary.it",
            "OWASP - https://owasp.org",
            "PortSwigger Web Academy - https://portswigger.net/web-security"
        ]
    }
    
    KEYWORDS = {
        "1": ["web", "website", "frontend", "backend", "browser", "html", "css", "javascript", "react", "node", "interface", "user interface", "full stack", "fullstack"],
        "2": ["data", "science", "analysis", "analytics", "machine learning", "ml", "ai", "artificial intelligence", "pandas", "model", "predict", "climate", "weather", "statistic", "visual", "dataset", "pattern", "numpy", "tensorflow"],
        "3": ["mobile", "app", "ios", "android", "phone", "smartphone", "iphone", "download", "swift", "kotlin"],
        "4": ["game", "gaming", "games", "3d", "graphics", "unity", "unreal", "character", "world", "interactive experience", "video game", "gameplay"],
        "5": ["go", "golang", "concurrent", "microservice", "cloud", "devops", "infrastructure", "scalable", "distributed", "kubernetes", "docker"],
        "6": ["rust", "performance", "system", "memory", "embedded", "webassembly", "wasm", "blockchain", "low level", "safe"],
        "7": ["typescript", "type safe", "typed", "javascript with types", "ts", "static typing", "type system"],
        "8": ["database", "sql", "mysql", "postgresql", "mongodb", "data storage", "query", "nosql", "redis", "data modeling"],
        "9": ["java", "enterprise", "spring", "android java", "jvm", "backend java", "corporate"],
        "10": ["ruby", "rails", "ruby on rails", "startup", "mvp", "rapid development", "convention"],
        "11": ["php", "laravel", "wordpress", "web development php", "freelance", "cms"],
        "12": ["security", "hacking", "penetration", "cybersecurity", "ethical hacking", "vulnerability", "infosec", "pentesting", "network security"]
    }
    
    @classmethod
    def process_chat(cls, message: str, session_id: str) -> Dict[str, Any]:
        """Process chat with AI if available, fallback to rules"""
        msg_lower = message.lower().strip()
        
        # Very short greetings
        if msg_lower in ["hello", "hi", "hey", "hello!", "hi!", "hey!"]:
            return {
                "status": "ok",
                "response": "👋 Hello! I'm TechGuide Bot. Ask me anything about programming languages, tech careers, or what to learn!",
                "type": "greeting"
            }
        
        # Try AI first if available
        if AI_AVAILABLE:
            try:
                from ai_helper import chat_with_ai
                
                # Get conversation context
                context = f"Session: {session_id}"
                
                ai_response = chat_with_ai(message, context)
                
                if ai_response.get("success"):
                    return {
                        "status": "ok",
                        "response": ai_response["response"],
                        "type": "ai_chat",
                        "ai_powered": True,
                        "model": "gemini-pro"
                    }
            except Exception as e:
                logger.warning(f"AI failed, using fallback: {e}")
        
        # Fallback to keyword-based classification
        return cls.classify_and_recommend(message, session_id)
        
    @classmethod
    def classify_and_recommend(cls, text: str, session_id: str) -> Dict[str, Any]:
        """Smarter classification with better keyword matching"""
        text_lower = text.lower()
        scores = {"1": 0, "2": 0, "3": 0, "4": 0}
        
        # Score each category with weighted keywords
        for choice, keywords in cls.KEYWORDS.items():
            for keyword in keywords:
                if keyword in text_lower:
                    # Exact word boundary matches get more weight
                    if f" {keyword} " in f" {text_lower} " or text_lower.startswith(keyword) or text_lower.endswith(keyword):
                        scores[choice] += 3
                    else:
                        scores[choice] += 1
        
        max_score = max(scores.values())
        best_choice = max(scores, key=scores.get) if max_score > 0 else ""
        
        # Need at least score of 2 to be confident
        if not best_choice or max_score < 2:
            return {
                "status": "clarification_needed",
                "response": "I'd love to help! Could you be more specific?\n\n1. 🌐 **Web Development** - Websites and web apps\n2. 📊 **Data Science** - Data analysis, ML, AI\n3. 📱 **Mobile Apps** - iOS/Android apps\n4. 🎮 **Game Development** - Video games\n\nWhich area interests you most?",
                "type": "clarification"
            }
        
        return cls.get_recommendation(best_choice, session_id)
    
    @classmethod
    def get_recommendation(cls, choice: str, session_id: str) -> Dict[str, Any]:
        """Get recommendation for choice"""
        if choice not in cls.INTEREST_MAP:
            return {
                "status": "error",
                "message": "Invalid choice. Please select 1-4."
            }
        
        choice_data = cls.INTEREST_MAP[choice]
        lang = choice_data["lang"]
        
        return {
            "status": "ok",
            "language": lang,
            "reason": choice_data["reason"],
            "resources": cls.RESOURCES_MAP.get(lang, []),
            "metadata": {
                "difficulty": choice_data["difficulty"],
                "estimated_time": choice_data["time"],
                "learning_path": choice_data["learning_path"],
                "career_paths": choice_data["career_paths"],
                "session_id": session_id
            },
            "type": "recommendation"
        }

# API ENDPOINTS

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "TechGuide Bot API - Advanced",
        "version": "3.0.0",
        "timestamp": datetime.now().isoformat(),
        "ai_enabled": AI_AVAILABLE
    }

@app.get("/health")
@app.head("/health")  # Add HEAD method support
async def health_check():
    """Health check endpoint - supports both GET and HEAD"""
    return {
        "status": "healthy",
        "service": "TechGuide Bot API",
        "version": "3.0.0",
        "ai_enabled": AI_AVAILABLE
    }

@app.post("/chat")
async def chat(request: ChatRequest):
    """Main chat endpoint"""
    try:
        session_id = request.session_id or str(uuid.uuid4())
        
        logger.info(f"Chat request - Session: {session_id}, Message: {request.message}")
        
        # Store user message
        sessions[session_id]["messages"].append({
            "role": "user",
            "content": request.message,
            "timestamp": datetime.now().isoformat()
        })
        
        # Process message
        result = EnhancedBackend.process_chat(request.message, session_id)
        
        # Store bot response
        sessions[session_id]["messages"].append({
            "role": "assistant",
            "content": result.get("response") or result.get("reason", ""),
            "timestamp": datetime.now().isoformat(),
            "data": result
        })
        
        result["session_id"] = session_id
        return result
        
    except Exception as e:
        logger.error(f"Error in chat: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/techguide")
async def get_recommendation(request: TechGuideRequest):
    """Get programming language recommendation"""
    try:
        session_id = request.session_id or str(uuid.uuid4())
        
        if request.choice:
            result = EnhancedBackend.get_recommendation(request.choice, session_id)
        elif request.message:
            result = EnhancedBackend.classify_and_recommend(request.message, session_id)
        else:
            return {"status": "error", "message": "Provide either choice or message"}
        
        # Store recommendation
        if result.get("status") == "ok" and result.get("language"):
            sessions[session_id]["recommendations"].append({
                "language": result["language"],
                "timestamp": datetime.now().isoformat()
            })
        
        return result
        
    except Exception as e:
        logger.error(f"Error in recommendation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history/{session_id}")
async def get_history(session_id: str):
    """Get conversation history"""
    if session_id not in sessions:
        return {
            "status": "ok",
            "session_id": session_id,
            "messages": [],
            "recommendations": []
        }
    
    return {
        "status": "ok",
        "session_id": session_id,
        **sessions[session_id]
    }

@app.get("/")
async def root():
    """API root"""
    return {
        "service": "TechGuide Bot API - Advanced",
        "version": "3.0.0",
        "status": "operational",
        "ai_enabled": AI_AVAILABLE
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)