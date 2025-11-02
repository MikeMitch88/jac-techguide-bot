"""
Configuration for TechGuide Bot Frontend
"""

import os

# Backend configuration
BACKEND_HOST = os.getenv("BACKEND_HOST", "localhost")
BACKEND_PORT = os.getenv("BACKEND_PORT", "8000")
BACKEND_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}"

# Frontend configuration
FRONTEND_PORT = os.getenv("FRONTEND_PORT", "8501")
FRONTEND_HOST = os.getenv("FRONTEND_HOST", "localhost")

# Feature flags
ENABLE_CHAT_HISTORY = os.getenv("ENABLE_CHAT_HISTORY", "true").lower() == "true"
ENABLE_CLASSIFICATION = os.getenv("ENABLE_CLASSIFICATION", "true").lower() == "true"

# UI Configuration
APP_TITLE = "TechGuide Bot"
APP_ICON = "🤖"
THEME_PRIMARY_COLOR = "#1E88E5"