"""
Enhanced Walker definitions with AI reasoning
"""

import:py from datetime { datetime }

# Smart recommendation walker with reasoning
walker SmartRecommendWalker {
    has message: str = "";
    has choice: str = "";
    has session_id: str = "";
    has context: list = [];
    has result: dict = {};
    
    # Enhanced knowledge base with learning paths
    has interest_map: dict = {
        "1": {
            "lang": "JavaScript",
            "reason": "JavaScript is the backbone of modern web development. With frameworks like React, Vue, and Angular for frontends, and Node.js for backends, you can build full-stack applications. The language is beginner-friendly, has a massive community, and countless job opportunities.",
            "difficulty": "Beginner",
            "time": "3-4 months",
            "learning_path": [
                {"phase": "Basics", "duration": "4 weeks", "topics": ["Variables, Functions, DOM manipulation", "ES6+ features", "Async/Promises"]},
                {"phase": "Frameworks", "duration": "6 weeks", "topics": ["React fundamentals", "State management", "API integration"]},
                {"phase": "Projects", "duration": "4 weeks", "topics": ["Build a portfolio site", "Create a full-stack app", "Deploy to production"]}
            ],
            "career_paths": ["Frontend Developer", "Full-Stack Developer", "Node.js Backend Developer"]
        },
        "2": {
            "lang": "Python",
            "reason": "Python is the Swiss Army knife of programming. Renowned for its clean syntax and readability, it dominates data science, machine learning, and AI. With libraries like Pandas, NumPy, TensorFlow, and Scikit-learn, you can analyze data, build ML models, and create intelligent systems. Python is also great for web development (Django, Flask) and automation.",
            "difficulty": "Beginner",
            "time": "4-6 months",
            "learning_path": [
                {"phase": "Basics", "duration": "3 weeks", "topics": ["Syntax, Data types", "Functions, Classes", "File handling"]},
                {"phase": "Data Science", "duration": "8 weeks", "topics": ["Pandas, NumPy", "Data visualization (Matplotlib, Seaborn)", "Machine Learning basics"]},
                {"phase": "Projects", "duration": "5 weeks", "topics": ["Kaggle competitions", "Build a predictive model", "Data analysis portfolio"]}
            ],
            "career_paths": ["Data Scientist", "ML Engineer", "Python Developer", "AI Researcher"]
        },
        "3": {
            "lang": "Swift/Kotlin",
            "reason": "Native mobile development is where performance meets user experience. Swift (for iOS) and Kotlin (for Android) are the official languages for their respective platforms. You'll learn to build smooth, responsive apps that leverage device hardware, integrate with native APIs, and deliver the best possible mobile experience.",
            "difficulty": "Intermediate",
            "time": "6-9 months",
            "learning_path": [
                {"phase": "Basics", "duration": "6 weeks", "topics": ["Language fundamentals", "UI design patterns", "Mobile architecture"]},
                {"phase": "Platform APIs", "duration": "8 weeks", "topics": ["Native components", "Networking", "Data persistence"]},
                {"phase": "Projects", "duration": "8 weeks", "topics": ["Build 2-3 apps", "App Store deployment", "User feedback iteration"]}
            ],
            "career_paths": ["iOS Developer", "Android Developer", "Mobile Architect"]
        },
        "4": {
            "lang": "C#/C++",
            "reason": "Game development requires languages that balance high performance with developer productivity. C# with Unity offers an approachable entry into game dev with extensive documentation and a huge asset store. C++ with Unreal Engine provides cutting-edge graphics and performance for AAA titles. Both have strong communities and career opportunities.",
            "difficulty": "Intermediate",
            "time": "6-12 months",
            "learning_path": [
                {"phase": "Basics", "duration": "8 weeks", "topics": ["Language fundamentals", "OOP concepts", "Game math basics"]},
                {"phase": "Engine Mastery", "duration": "12 weeks", "topics": ["Unity/Unreal basics", "Physics systems", "Animation"]},
                {"phase": "Projects", "duration": "12 weeks", "topics": ["Complete 2D game", "3D prototype", "Polish and publish"]}
            ],
            "career_paths": ["Game Developer", "Engine Programmer", "Technical Artist"]
        }
    };
    
    # Keyword mapping for intelligent classification
    has keyword_map: dict = {
        "1": ["web", "website", "frontend", "backend", "html", "css", "javascript", "react", "vue", "angular", "node", "fullstack", "browser", "http"],
        "2": ["data", "science", "analysis", "analytics", "machine learning", "ml", "ai", "artificial intelligence", "pandas", "numpy", "tensorflow", "model", "prediction", "statistics"],
        "3": ["mobile", "app", "ios", "android", "phone", "smartphone", "tablet", "swift", "kotlin", "flutter", "react native"],
        "4": ["game", "gaming", "games", "3d", "graphics", "unity", "unreal", "engine", "character", "level", "animation"]
    };
    
    has resources_map: dict = {
        "JavaScript": {
            "resources": [
                "MDN Web Docs - https://developer.mozilla.org",
                "freeCodeCamp - https://freecodecamp.org",
                "JavaScript.info - https://javascript.info",
                "React Official Docs - https://react.dev",
                "Node.js Documentation - https://nodejs.org"
            ]
        },
        "Python": {
            "resources": [
                "Python.org Official Tutorial - https://docs.python.org/3/tutorial/",
                "DataCamp - https://datacamp.com",
                "Kaggle Learn - https://kaggle.com/learn",
                "Fast.ai - https://fast.ai",
                "Coursera Python Specialization"
            ]
        },
        "Swift/Kotlin": {
            "resources": [
                "Apple Developer Docs - https://developer.apple.com",
                "Android Developer Guides - https://developer.android.com",
                "Ray Wenderlich - https://raywenderlich.com",
                "Udacity Mobile Development",
                "Hacking with Swift - https://hackingwithswift.com"
            ]
        },
        "C#/C++": {
            "resources": [
                "Unity Learn - https://learn.unity.com",
                "Unreal Engine Docs - https://docs.unrealengine.com",
                "GameDev.tv - https://gamedev.tv",
                "Brackeys YouTube Channel",
                "Game Programming Patterns - https://gameprogrammingpatterns.com"
            ]
        }
    };
    
    can start with `root entry {
        # Process the request
        if self.choice {
            self.process_choice();
        } elif self.message {
            self.classify_and_recommend();
        } else {
            self.result = {
                "status": "error",
                "message": "Please provide either a choice (1-4) or describe your interest"
            };
        }
        disengage;
    }
    
    can process_choice {
        if self.choice not in ["1", "2", "3", "4"] {
            self.result = {
                "status": "error",
                "message": "Invalid choice. Please select 1-4 or describe your interest in words."
            };
            return;
        }
        
        choice_data = self.interest_map[self.choice];
        lang = choice_data["lang"];
        
        self.result = {
            "status": "ok",
            "language": lang,
            "reason": choice_data["reason"],
            "resources": self.resources_map[lang]["resources"],
            "metadata": {
                "difficulty": choice_data["difficulty"],
                "estimated_time": choice_data["time"],
                "learning_path": choice_data["learning_path"],
                "career_paths": choice_data["career_paths"],
                "session_id": self.session_id
            }
        };
    }
    
    can classify_and_recommend {
        text_lower = self.message.lower();
        scores = {"1": 0, "2": 0, "3": 0, "4": 0};
        
        # Score each category
        for choice in self.keyword_map {
            for keyword in self.keyword_map[choice] {
                if keyword in text_lower {
                    scores[choice] = scores[choice] + 1;
                }
            }
        }
        
        # Find best match
        max_score = 0;
        best_choice = "";
        for choice in scores {
            if scores[choice] > max_score {
                max_score = scores[choice];
                best_choice = choice;
            }
        }
        
        if max_score == 0 {
            # No clear match - ask for clarification
            self.result = {
                "status": "clarification_needed",
                "message": "I'd love to help! Could you be more specific? Are you interested in:\n1. Building websites and web applications\n2. Data analysis and machine learning\n3. Mobile apps for iOS/Android\n4. Video games and interactive experiences",
                "suggestions": [
                    "Web Development",
                    "Data Science",
                    "Mobile Apps",
                    "Game Development"
                ]
            };
        } else {
            # Process the classified choice
            self.choice = best_choice;
            self.process_choice();
            self.result["classification"] = {
                "confidence": float(max_score) / 10.0,
                "scores": scores,
                "detected_keywords": self.get_detected_keywords(text_lower, best_choice)
            };
        }
    }
    
    can get_detected_keywords(text: str, choice: str) -> list {
        detected = [];
        for keyword in self.keyword_map[choice] {
            if keyword in text {
                detected.append(keyword);
            }
        }
        return detected;
    }
}

# Chat walker for conversational interface
walker ChatWalker {
    has message: str = "";
    has session_id: str = "";
    has conversation_history: list = [];
    has result: dict = {};
    
    can start with `root entry {
        # Handle different message types
        msg_lower = self.message.lower();
        
        # Greeting detection
        if any(greeting in msg_lower for greeting in ["hello", "hi", "hey", "greetings"]) {
            self.result = {
                "status": "ok",
                "response": "👋 Hello! I'm TechGuide Bot, your AI-powered programming language advisor. I help you discover the perfect language for your goals.\n\nWhat would you like to build? Feel free to describe your interests, and I'll recommend the best language for you!",
                "type": "greeting"
            };
        }
        # Help request
        elif any(word in msg_lower for word in ["help", "what can you do", "how do you work"]) {
            self.result = {
                "status": "ok",
                "response": "I can help you:\n\n🎯 Find the right programming language based on your interests\n📚 Get curated learning resources\n🗺️ See a complete learning path\n💼 Discover career opportunities\n\nJust tell me what you want to build, or choose from:\n1. Web Development\n2. Data Science\n3. Mobile Apps\n4. Game Development",
                "type": "help"
            };
        }
        # Recommendation request
        else {
            # Delegate to SmartRecommendWalker
            recommender = SmartRecommendWalker(
                message=self.message,
                session_id=self.session_id,
                context=self.conversation_history
            );
            root spawn recommender;
            self.result = recommender.result;
            self.result["type"] = "recommendation";
        }
        
        disengage;
    }
}

# History walker
walker HistoryWalker {
    has session_id: str = "";
    has result: dict = {};
    
    can start with `root entry {
        # Would connect to session storage
        self.result = {
            "status": "ok",
            "session_id": self.session_id,
            "history": [],
            "message": "History feature coming soon!"
        };
        disengage;
    }
}