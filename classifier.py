# Python helper for text classification
"""
Advanced text classifier for TechGuide Bot
Uses simple NLP techniques for better classification
"""

from typing import Dict, Tuple
import re

class InterestClassifier:
    """
    Classifies user interest text into programming categories
    """
    
    def __init__(self):
        self.keywords = {
            "1": {  # Web Development
                "primary": ["web", "website", "frontend", "backend", "fullstack"],
                "secondary": ["html", "css", "javascript", "react", "vue", "angular", "node"],
                "context": ["browser", "http", "server", "client", "responsive"]
            },
            "2": {  # Data Science
                "primary": ["data", "analytics", "machine learning", "ai", "science"],
                "secondary": ["python", "pandas", "numpy", "tensorflow", "analysis"],
                "context": ["model", "prediction", "statistics", "visualization", "dataset"]
            },
            "3": {  # Mobile Apps
                "primary": ["mobile", "app", "ios", "android", "smartphone"],
                "secondary": ["swift", "kotlin", "flutter", "react native"],
                "context": ["phone", "tablet", "device", "touch", "notification"]
            },
            "4": {  # Game Development
                "primary": ["game", "gaming", "3d", "graphics"],
                "secondary": ["unity", "unreal", "engine", "animation"],
                "context": ["character", "level", "physics", "render", "gameplay"]
            }
        }
    
    def classify(self, text: str) -> Tuple[str, float, Dict]:
        """
        Classify text and return choice, confidence, and scores
        """
        text_lower = text.lower()
        scores = {"1": 0, "2": 0, "3": 0, "4": 0}
        
        # Score each category
        for choice, keywords in self.keywords.items():
            # Primary keywords (weight: 3)
            for keyword in keywords["primary"]:
                if keyword in text_lower:
                    scores[choice] += 3
            
            # Secondary keywords (weight: 2)
            for keyword in keywords["secondary"]:
                if keyword in text_lower:
                    scores[choice] += 2
            
            # Context keywords (weight: 1)
            for keyword in keywords["context"]:
                if keyword in text_lower:
                    scores[choice] += 1
        
        # Find best match
        max_score = max(scores.values())
        best_choice = max(scores, key=scores.get) if max_score > 0 else ""
        
        # Calculate confidence
        total_score = sum(scores.values())
        confidence = (max_score / total_score) if total_score > 0 else 0.0
        
        return best_choice, confidence, scores

# Standalone testing
if __name__ == "__main__":
    classifier = InterestClassifier()
    
    test_cases = [
        "I want to build websites",
        "I'm interested in machine learning and AI",
        "I want to create mobile apps for iOS",
        "I love making video games"
    ]
    
    for text in test_cases:
        choice, confidence, scores = classifier.classify(text)
        print(f"\nText: {text}")
        print(f"Choice: {choice}, Confidence: {confidence:.2f}")
        print(f"Scores: {scores}")