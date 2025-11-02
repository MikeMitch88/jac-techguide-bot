
"""
AI Helper Module for TechGuide Bot - WORKING VERSION
Uses models/gemini-2.0-flash (fast and free)
"""

import os
import logging
from typing import Dict, Any, Optional
import json

logger = logging.getLogger(__name__)

# Set API key
os.environ["GEMINI_API_KEY"] = "AIzaSyARKdB_4LqXAdtEBQ07PWd85ZN5IyzSrZY"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Try to import and configure
try:
    import google.generativeai as genai
    
    if GEMINI_API_KEY:
        genai.configure(api_key=GEMINI_API_KEY)
        # Use the correct model name with 'models/' prefix
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        AI_AVAILABLE = True
        logger.info("✅ Google Gemini AI ENABLED (gemini-2.0-flash)")
    else:
        AI_AVAILABLE = False
        logger.warning("⚠️ No API key found")
        
except Exception as e:
    AI_AVAILABLE = False
    logger.error(f"❌ AI initialization failed: {e}")

# ============================================================================
# AI HELPER CLASS
# ============================================================================

class AIHelper:
    """Direct Gemini integration with proper model name"""
    
    def __init__(self):
        self.enabled = AI_AVAILABLE
        
    def is_enabled(self) -> bool:
        return self.enabled
    
    def chat(self, message: str, context: Optional[str] = None) -> Dict[str, Any]:
        """
        Main chat function - handles any user question intelligently
        """
        if not self.enabled:
            return {
                "success": False,
                "response": "AI not available. Using fallback logic.",
                "ai_powered": False
            }
        
        try:
            # Build comprehensive prompt
            system_context = """You are TechGuide Bot, an expert programming language advisor and tech career mentor.

Your expertise covers ALL programming languages and tech domains:
- Languages: JavaScript, Python, Java, C++, Go, Rust, TypeScript, Ruby, PHP, Swift, Kotlin, C#, R, Scala, Elixir, Haskell, and more
- Domains: Web dev, mobile, data science, ML/AI, game dev, DevOps, cloud, cybersecurity, embedded systems, blockchain
- Tools: Git, Docker, Kubernetes, AWS, databases, frameworks, libraries

Your role:
1. Understand what the user wants to build/learn (ask clarifying questions if vague)
2. Recommend the BEST technology for their specific goal
3. Explain WHY with practical reasoning
4. Provide realistic timelines and learning paths
5. Give honest career and market insights
6. Be encouraging but realistic

Response style:
- Concise but comprehensive (3-5 paragraphs unless more detail requested)
- Use specific examples and real-world applications
- Structure: [Recommendation] → [Why] → [Learning Path] → [Career Prospects]
- If comparing, give honest pros/cons
- If user asks general questions, provide actionable answers"""

            if context:
                full_prompt = f"{system_context}\n\nContext: {context}\n\nUser: {message}\n\nResponse:"
            else:
                full_prompt = f"{system_context}\n\nUser: {message}\n\nResponse:"
            
            # Call Gemini
            response = model.generate_content(full_prompt)
            
            logger.info(f"✅ AI response generated for: {message[:50]}...")
            
            return {
                "success": True,
                "response": response.text,
                "ai_powered": True,
                "model": "gemini-2.0-flash"
            }
            
        except Exception as e:
            logger.error(f"❌ AI chat failed: {e}")
            return {
                "success": False,
                "response": f"I encountered an error: {str(e)}. Please try rephrasing.",
                "error": str(e)
            }
    
    def classify_interest(self, text: str) -> Dict[str, Any]:
        """
        Use AI to intelligently classify user interest into categories
        """
        if not self.enabled:
            return {"success": False}
        
        try:
            prompt = f"""Analyze this user's interest and classify it into the BEST matching category:

Categories:
1. JavaScript - Web development (React, Node.js, full-stack)
2. Python - Data science, ML, AI, automation, scripting, backend
3. Swift/Kotlin - Native mobile (iOS/Android apps)
4. C#/C++ - Game development (Unity, Unreal Engine)
5. Go - Cloud, microservices, DevOps, infrastructure, scalability
6. Rust - Systems programming, performance-critical, blockchain, WebAssembly
7. TypeScript - Type-safe web development, large-scale JavaScript projects
8. SQL/Databases - Database management, data engineering, analytics
9. Java - Enterprise backend, Android, large-scale systems
10. Ruby/Rails - Rapid web development, startups, MVPs
11. PHP/Laravel - Web development, WordPress, freelancing
12. Cybersecurity - Ethical hacking, penetration testing, security engineering

User's interest: "{text}"

Respond with ONLY valid JSON (no markdown):
{{
    "category": "1-12",
    "language": "exact language name from list",
    "confidence": 0.0 to 1.0,
    "reasoning": "brief explanation (1-2 sentences)",
    "alternative": "mention if another category could fit"
}}"""

            response = model.generate_content(prompt)
            response_text = response.text.strip()
            
            # Remove markdown if present
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            result = json.loads(response_text)
            result["success"] = True
            result["ai_powered"] = True
            
            logger.info(f"✅ AI classified: {result.get('language')} (conf: {result.get('confidence')})")
            
            return result
            
        except Exception as e:
            logger.error(f"❌ AI classification failed: {e}")
            return {"success": False, "error": str(e)}

# Global instance
ai_helper = AIHelper()

# Convenience functions
def chat_with_ai(message: str, context: Optional[str] = None) -> Dict[str, Any]:
    """Chat with AI - returns structured response"""
    return ai_helper.chat(message, context)

def classify_with_ai(text: str) -> Dict[str, Any]:
    """Classify user interest using AI"""
    return ai_helper.classify_interest(text)

# Test module
if __name__ == "__main__":
    print("🤖 Testing AI Helper (Gemini 2.0 Flash)\n")
    print(f"Enabled: {ai_helper.is_enabled()}\n")
    
    if ai_helper.is_enabled():
        # Test 1: Simple question
        print("=" * 60)
        print("Test 1: General question")
        print("=" * 60)
        result = chat_with_ai("What programming language should I learn first as a complete beginner?")
        if result.get("success"):
            print(f"✅ Response:\n{result.get('response', '')}\n")
        else:
            print(f"❌ Failed: {result.get('error')}\n")
        
        # Test 2: Classification
        print("=" * 60)
        print("Test 2: Interest classification")
        print("=" * 60)
        result = classify_with_ai("I want to build scalable REST APIs that handle millions of requests per second")
        if result.get("success"):
            print(f"✅ Classification Result:")
            print(f"   Language: {result.get('language')}")
            print(f"   Confidence: {result.get('confidence')}")
            print(f"   Reasoning: {result.get('reasoning')}")
            if result.get('alternative'):
                print(f"   Alternative: {result.get('alternative')}")
        else:
            print(f"❌ Failed: {result.get('error')}")
        
        # Test 3: Complex question
        print("\n" + "=" * 60)
        print("Test 3: Career question")
        print("=" * 60)
        result = chat_with_ai("I'm 30 years old and want to transition into tech. Which path gives me the best chance of getting hired within 6 months?")
        if result.get("success"):
            print(f"✅ Response:\n{result.get('response', '')[:300]}...\n")
        else:
            print(f"❌ Failed: {result.get('error')}\n")
    else:
        print("❌ AI is not enabled. Check API key and installation.")