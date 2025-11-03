
"""
TechGuide Bot - Ultra-Modern AI Assistant UI
Professional ChatGPT-style interface with proper alignment
"""

import streamlit as st
import requests
from typing import Dict, Any
from datetime import datetime
import time
import os
import uuid

# ============================================================================
# CONFIGURATION
# ============================================================================

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# Page configuration
st.set_page_config(
    page_title="TechGuide AI - Your Programming Mentor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# ENHANCED MODERN STYLING WITH PROPER ALIGNMENT
# ============================================================================

st.markdown("""
<style>
    /* ==================== GLOBAL THEME ==================== */
    :root {
        --primary-violet: #8B5CF6;
        --primary-purple: #A855F7;
        --accent-teal: #14B8A6;
        --accent-cyan: #06B6D4;
        --dark-bg: #0F0F1E;
        --dark-card: #1A1A2E;
        --dark-elevated: #232342;
        --text-primary: #F8FAFC;
        --text-secondary: #94A3B8;
        --border-subtle: rgba(139, 92, 246, 0.1);
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Remove default padding */
    .main > div {
        padding-top: 2rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0F0F1E 0%, #1A1A2E 50%, #1E1633 100%);
        color: var(--text-primary);
    }
    
    #MainMenu, footer, header {visibility: hidden;}
    
    /* ==================== HEADER ==================== */
    .main-header {
        background: linear-gradient(135deg, var(--primary-violet) 0%, var(--primary-purple) 50%, var(--accent-teal) 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(139, 92, 246, 0.3);
        text-align: center;
    }
    
    .main-header h1 {
        color: white;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 2px 20px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        color: rgba(255,255,255,0.95);
        font-size: 1rem;
        margin: 0.5rem 0 0 0;
        font-weight: 500;
    }
    
    /* ==================== CHAT CONTAINER ==================== */
    .stChatMessage {
        background: transparent !important;
        padding: 0.75rem 0 !important;
        margin-bottom: 1.5rem !important;
    }
    
    /* Force proper alignment */
    [data-testid="stChatMessage"] {
        display: flex !important;
        flex-direction: row !important;
        align-items: flex-start !important;
    }
    
    /* User messages - RIGHT ALIGNED */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        justify-content: flex-end !important;
        flex-direction: row-reverse !important;
    }
    
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) [data-testid="stChatMessageContent"] {
        background: linear-gradient(135deg, var(--primary-violet), var(--primary-purple)) !important;
        color: white !important;
        padding: 1rem 1.25rem !important;
        border-radius: 18px 18px 4px 18px !important;
        max-width: 70% !important;
        margin-left: auto !important;
        margin-right: 0.75rem !important;
        box-shadow: 0 4px 16px rgba(139, 92, 246, 0.4) !important;
        font-size: 0.95rem !important;
        line-height: 1.6 !important;
    }
    
    /* Assistant messages - LEFT ALIGNED */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        justify-content: flex-start !important;
    }
    
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) [data-testid="stChatMessageContent"] {
        background: var(--dark-elevated) !important;
        color: var(--text-primary) !important;
        padding: 1.25rem 1.5rem !important;
        border-radius: 4px 18px 18px 18px !important;
        max-width: 80% !important;
        margin-left: 0.75rem !important;
        margin-right: auto !important;
        border: 1px solid var(--border-subtle) !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5) !important;
        font-size: 0.95rem !important;
        line-height: 1.7 !important;
    }
    
    /* Avatar styling */
    [data-testid="chatAvatarIcon-assistant"] {
        background: linear-gradient(135deg, var(--accent-teal), var(--accent-cyan)) !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 12px rgba(20, 184, 166, 0.5) !important;
        width: 40px !important;
        height: 40px !important;
    }
    
    [data-testid="chatAvatarIcon-user"] {
        background: linear-gradient(135deg, var(--primary-violet), var(--primary-purple)) !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.5) !important;
        width: 40px !important;
        height: 40px !important;
    }
    
    /* Fix markdown in chat messages */
    [data-testid="stChatMessageContent"] p {
        margin: 0 0 0.5rem 0 !important;
    }
    
    [data-testid="stChatMessageContent"] p:last-child {
        margin-bottom: 0 !important;
    }
    
    [data-testid="stChatMessageContent"] ul, 
    [data-testid="stChatMessageContent"] ol {
        margin: 0.5rem 0 !important;
        padding-left: 1.5rem !important;
    }
    
    [data-testid="stChatMessageContent"] li {
        margin: 0.25rem 0 !important;
    }
    
    [data-testid="stChatMessageContent"] strong {
        font-weight: 700 !important;
    }
    
    /* ==================== RECOMMENDATION CARD ==================== */
    .recommendation-card {
        background: linear-gradient(135deg, var(--dark-elevated), var(--dark-card));
        border: 1px solid var(--border-subtle);
        border-left: 4px solid var(--primary-violet);
        padding: 2rem;
        border-radius: 16px;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    }
    
    .language-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, var(--primary-violet), var(--accent-teal));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
    }
    
    /* ==================== METRIC CARDS ==================== */
    .metric-card {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.15), rgba(20, 184, 166, 0.15));
        border: 1px solid var(--border-subtle);
        padding: 1.5rem;
        border-radius: 14px;
        text-align: center;
        transition: all 0.3s;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 32px rgba(139, 92, 246, 0.3);
    }
    
    .metric-card h3 {
        font-size: 0.8rem;
        color: var(--text-secondary);
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
    }
    
    .metric-card h2 {
        font-size: 1.5rem;
        color: var(--text-primary);
        margin: 0;
        font-weight: 700;
    }
    
    /* ==================== TIMELINE ==================== */
    .timeline-item {
        position: relative;
        padding-left: 2.5rem;
        padding-bottom: 1.5rem;
        border-left: 2px solid var(--border-subtle);
        margin-left: 0.5rem;
    }
    
    .timeline-item:last-child {
        border-left: 2px solid transparent;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -7px;
        top: 0;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--primary-violet), var(--accent-teal));
        box-shadow: 0 0 0 4px var(--dark-bg), 0 0 16px rgba(139, 92, 246, 0.5);
    }
    
    .timeline-item h4 {
        color: var(--text-primary);
        font-size: 1.05rem;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .timeline-item .duration {
        color: var(--accent-teal);
        font-size: 0.85rem;
        font-weight: 600;
        margin-left: 0.5rem;
    }
    
    .timeline-item li {
        color: var(--text-secondary);
        padding: 0.3rem 0;
        font-size: 0.9rem;
        line-height: 1.6;
        list-style: none;
    }
    
    .timeline-item li::before {
        content: '→';
        color: var(--accent-teal);
        font-weight: bold;
        margin-right: 0.5rem;
    }
    
    /* ==================== RESOURCES ==================== */
    .resource-link {
        background: rgba(139, 92, 246, 0.08);
        padding: 1rem 1.25rem;
        border-radius: 12px;
        margin: 0.75rem 0;
        border-left: 3px solid var(--primary-violet);
        transition: all 0.3s;
    }
    
    .resource-link:hover {
        background: rgba(139, 92, 246, 0.15);
        transform: translateX(8px);
    }
    
    .resource-link a {
        color: var(--accent-teal) !important;
        text-decoration: none;
        font-weight: 500;
    }
    
    /* ==================== CAREER BADGES ==================== */
    .career-badge {
        display: inline-block;
        background: rgba(20, 184, 166, 0.15);
        color: var(--accent-teal);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.4rem 0.3rem;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid rgba(20, 184, 166, 0.3);
        transition: all 0.3s;
    }
    
    .career-badge:hover {
        background: rgba(20, 184, 166, 0.25);
        transform: translateY(-2px);
    }
    
    /* ==================== SIDEBAR ==================== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--dark-bg), var(--dark-card));
        border-right: 1px solid var(--border-subtle);
    }
    
    [data-testid="stSidebar"] .stButton > button {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.2), rgba(20, 184, 166, 0.2));
        color: var(--text-primary);
        border: 1px solid var(--border-subtle);
        border-radius: 24px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.3s;
        width: 100%;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background: linear-gradient(135deg, var(--primary-violet), var(--accent-teal));
        transform: translateX(4px);
        box-shadow: 0 4px 16px rgba(139, 92, 246, 0.4);
    }
    
    /* Status badges */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .status-online {
        background: rgba(34, 197, 94, 0.15);
        color: #22C55E;
        border: 1px solid rgba(34, 197, 94, 0.3);
    }
    
    .status-offline {
        background: rgba(239, 68, 68, 0.15);
        color: #EF4444;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }
    
    /* ==================== CHAT INPUT ==================== */
    .stChatInputContainer textarea {
        background: var(--dark-elevated) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: 16px !important;
        color: var(--text-primary) !important;
        font-size: 0.95rem !important;
        padding: 1rem !important;
    }
    
    .stChatInputContainer textarea:focus {
        border-color: var(--primary-violet) !important;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.3) !important;
    }
    
    /* ==================== SCROLLBAR ==================== */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--dark-bg);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, var(--primary-violet), var(--accent-teal));
        border-radius: 4px;
    }
    
    /* ==================== RESPONSIVE ==================== */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 1.75rem;
        }
        
        [data-testid="stChatMessageContent"] {
            max-width: 90% !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE
# ============================================================================

if "messages" not in st.session_state:
    st.session_state.messages = []
    welcome_msg = """Hello! I'm **TechGuide AI**, your intelligent programming mentor.

I help developers at all levels discover the perfect technology for their goals. I provide:

- Personalized language recommendations
- Structured learning roadmaps  
- Career insights and market trends
- Curated learning resources

**What would you like to build today?**"""
    
    st.session_state.messages.append({
        "role": "assistant",
        "content": welcome_msg,
        "timestamp": datetime.now().isoformat()
    })

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "backend_status" not in st.session_state:
    st.session_state.backend_status = None

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def check_backend_health() -> Dict[str, Any]:
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        if response.status_code == 200:
            return {"status": "online", "data": response.json()}
        return {"status": "error"}
    except:
        return {"status": "offline"}

def send_chat_message(message: str) -> Dict[str, Any]:
    try:
        response = requests.post(
            f"{BACKEND_URL}/chat",
            json={"message": message, "session_id": st.session_state.session_id},
            timeout=15
        )
        if response.status_code == 200:
            return response.json()
        return {"status": "error", "response": f"Backend error: {response.status_code}"}
    except requests.exceptions.ConnectionError:
        return use_fallback_logic(message)
    except Exception as e:
        return {"status": "error", "response": f"Error: {str(e)}"}

def use_fallback_logic(message: str) -> Dict[str, Any]:
    msg_lower = message.lower()
    
    if any(word in msg_lower for word in ["web", "website", "frontend"]):
        return {
            "status": "ok",
            "response": "I recommend **JavaScript** for web development.\n\nJavaScript powers modern web experiences with frameworks like React, Vue, and Angular for stunning UIs, plus Node.js for scalable backends. It's beginner-friendly with a massive ecosystem.",
            "type": "recommendation"
        }
    elif any(word in msg_lower for word in ["data", "science", "ml", "ai"]):
        return {
            "status": "ok",
            "response": "I recommend **Python** for data science and AI.\n\nPython dominates the AI/ML space with libraries like TensorFlow, PyTorch, Pandas, and NumPy. Its clean syntax makes it perfect for both beginners and professionals.",
            "type": "recommendation"
        }
    elif any(word in msg_lower for word in ["mobile", "app", "ios", "android"]):
        return {
            "status": "ok",
            "response": "I recommend **Swift/Kotlin** for native mobile development.\n\nSwift (iOS) and Kotlin (Android) are the official languages for their platforms. Build blazing-fast apps with access to all native features.",
            "type": "recommendation"
        }
    else:
        return {
            "status": "ok",
            "response": "Hello! I can help you choose the perfect programming language.\n\nTell me what you want to build:\n• Web applications\n• Data science projects\n• Mobile apps\n• Games",
            "type": "greeting"
        }

def display_learning_path(learning_path: list):
    st.markdown("### Learning Journey")
    for phase in learning_path:
        topics_html = "".join([f"<li>{topic}</li>" for topic in phase['topics']])
        st.markdown(f"""
        <div class="timeline-item">
            <h4>{phase['phase']}<span class="duration">({phase['duration']})</span></h4>
            <ul>{topics_html}</ul>
        </div>
        """, unsafe_allow_html=True)

def display_resources(resources: list):
    st.markdown("### Learning Resources")
    for idx, resource in enumerate(resources, 1):
        if " - " in resource:
            name, url = resource.split(" - ", 1)
            st.markdown(f"""
            <div class="resource-link">
                <strong>{idx}. {name}</strong><br>
                <a href="{url}" target="_blank">{url}</a>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="resource-link"><strong>{idx}. {resource}</strong></div>', unsafe_allow_html=True)

def display_career_paths(career_paths: list):
    st.markdown("### Career Opportunities")
    badges_html = "".join([f'<span class="career-badge">{path}</span>' for path in career_paths])
    st.markdown(f'<div>{badges_html}</div>', unsafe_allow_html=True)

def display_recommendation(result: Dict[str, Any]):
    if result.get("type") == "recommendation" and result.get("language"):
        language = result.get("language")
        reason = result.get("reason", "")
        resources = result.get("resources", [])
        metadata = result.get("metadata", {})
        
        st.markdown(f'<div class="recommendation-card"><h1 class="language-title">{language}</h1></div>', unsafe_allow_html=True)
        
        if metadata:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f'<div class="metric-card"><h3>Difficulty</h3><h2>{metadata.get("difficulty", "N/A")}</h2></div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="metric-card"><h3>Timeline</h3><h2>{metadata.get("estimated_time", "N/A")}</h2></div>', unsafe_allow_html=True)
            with col3:
                st.markdown(f'<div class="metric-card"><h3>Careers</h3><h2>{len(metadata.get("career_paths", []))}</h2></div>', unsafe_allow_html=True)
        
        st.markdown("### Why This Language?")
        st.markdown(f"<p style='font-size: 1.05rem; line-height: 1.8; color: var(--text-secondary);'>{reason}</p>", unsafe_allow_html=True)
        
        if metadata.get("learning_path"):
            display_learning_path(metadata["learning_path"])
        if resources:
            display_resources(resources)
        if metadata.get("career_paths"):
            display_career_paths(metadata["career_paths"])

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.markdown("# TechGuide AI")
    st.markdown("### Programming Mentor")
    st.markdown("---")
    
    st.markdown("### Connection")
    if st.button("Check Status", use_container_width=True):
        st.session_state.backend_status = check_backend_health()
    
    if st.session_state.backend_status:
        if st.session_state.backend_status.get("status") == "online":
            st.markdown('<span class="status-badge status-online">Connected</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="status-badge status-offline">Offline Mode</span>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Quick Start")
    
    if st.button("Web Dev", use_container_width=True):
        response = send_chat_message("I want to build websites")
        st.session_state.messages.append({"role": "user", "content": "I want to build websites", "timestamp": datetime.now().isoformat()})
        st.session_state.messages.append({"role": "assistant", "content": response.get("response", ""), "data": response, "timestamp": datetime.now().isoformat()})
        st.rerun()
    
    if st.button("Data Science", use_container_width=True):
        response = send_chat_message("I want to work with data")
        st.session_state.messages.append({"role": "user", "content": "I want to work with data", "timestamp": datetime.now().isoformat()})
        st.session_state.messages.append({"role": "assistant", "content": response.get("response", ""), "data": response, "timestamp": datetime.now().isoformat()})
        st.rerun()
    
    if st.button("Mobile Apps", use_container_width=True):
        response = send_chat_message("I want to create mobile apps")
        st.session_state.messages.append({"role": "user", "content": "I want to create mobile apps", "timestamp": datetime.now().isoformat()})
        st.session_state.messages.append({"role": "assistant", "content": response.get("response", ""), "data": response, "timestamp": datetime.now().isoformat()})
        st.rerun()
    
    if st.button("Game Dev", use_container_width=True):
        response = send_chat_message("I want to make games")
        st.session_state.messages.append({"role": "user", "content": "I want to make games", "timestamp": datetime.now().isoformat()})
        st.session_state.messages.append({"role": "assistant", "content": response.get("response", ""), "data": response, "timestamp": datetime.now().isoformat()})
        st.rerun()
    
    st.markdown("---")
    st.markdown("### Session")
    st.caption(f"**Messages:** {len(st.session_state.messages)}")
    st.caption(f"**ID:** {st.session_state.session_id[:8]}...")
    
    if st.button("New Chat", type="primary", use_container_width=True):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm TechGuide AI. What would you like to build?", "timestamp": datetime.now().isoformat()}]
        st.rerun()

# ============================================================================
# MAIN CHAT
# ============================================================================

st.markdown('<div class="main-header"><h1>TechGuide AI</h1><p>Your Intelligent Programming Language Advisor</p></div>', unsafe_allow_html=True)

# Display messages
for message in st.session_state.messages:
    role = message["role"]
    with st.chat_message(role):
        st.markdown(message["content"])
        if "data" in message and message["data"].get("type") == "recommendation":
            display_recommendation(message["data"])

# Chat input
user_input = st.chat_input("Tell me what you want to build...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input, "timestamp": datetime.now().isoformat()})
    
    with st.chat_message("assistant"):
        with st.spinner(""):
            time.sleep(0.3)
            response = send_chat_message(user_input)
    
    bot_message = {
        "role": "assistant",
        "content": response.get("response") or response.get("reason", "I couldn't process that."),
        "timestamp": datetime.now().isoformat()
    }
    
    if response.get("status") == "ok":
        bot_message["data"] = response
    
    st.session_state.messages.append(bot_message)
    st.rerun()

st.markdown("---")
st.markdown('<div style="text-align: center; color: var(--text-secondary); padding: 1.5rem 0;">Built with JAC • FastAPI • Streamlit • Gemini AI</div>', unsafe_allow_html=True)
