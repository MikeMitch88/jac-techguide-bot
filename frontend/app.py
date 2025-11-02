"""
TechGuide Bot - Advanced ChatGPT-Style Frontend
Modern conversational interface with real-time AI recommendations
"""

import streamlit as st
import requests
import json
from datetime import datetime
import time
import os
from typing import Dict, Any, List

# ============================================================================
# CONFIGURATION
# ============================================================================

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

# Page configuration
st.set_page_config(
    page_title="TechGuide Bot - AI Language Advisor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/yourusername/techguide-bot',
        'Report a bug': 'https://github.com/yourusername/techguide-bot/issues',
        'About': '# TechGuide Bot\nYour AI-powered programming language advisor!'
    }
)

# ============================================================================
# CUSTOM STYLING
# ============================================================================

st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
    }
    
    /* Chat container */
    .chat-container {
        padding: 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
    }
    
    /* User message bubble */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 5px 20px;
        margin: 0.5rem 0;
        margin-left: auto;
        max-width: 80%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        animation: slideInRight 0.3s ease-out;
    }
    
    /* Bot message bubble */
    .bot-message {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a7b 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 20px 5px;
        margin: 0.5rem 0;
        max-width: 85%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        animation: slideInLeft 0.3s ease-out;
    }
    
    /* Recommendation card */
    .recommendation-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-left: 5px solid #667eea;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        animation: fadeIn 0.5s ease-out;
    }
    
    /* Language title */
    .language-title {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: glow 2s ease-in-out infinite;
    }
    
    /* Learning path timeline */
    .timeline-item {
        border-left: 3px solid #667eea;
        padding-left: 1.5rem;
        margin: 1rem 0;
        position: relative;
    }
    
    .timeline-item::before {
        content: "●";
        position: absolute;
        left: -8px;
        color: #667eea;
        font-size: 1.2rem;
    }
    
    /* Resource link styling */
    .resource-link {
        background: rgba(102, 126, 234, 0.1);
        padding: 0.8rem 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 3px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .resource-link:hover {
        background: rgba(102, 126, 234, 0.2);
        transform: translateX(5px);
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* Status badge */
    .status-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    .status-online {
        background: #4caf50;
        color: white;
    }
    
    .status-offline {
        background: #f44336;
        color: white;
    }
    
    /* Animations */
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes glow {
        0%, 100% { filter: brightness(1); }
        50% { filter: brightness(1.2); }
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    }
    
    .main-header h1 {
        color: white;
        font-size: 3rem;
        font-weight: 800;
        margin: 0;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
    }
    
    /* Input box styling */
    .stTextInput > div > div > input {
        background: #1a1a2e;
        color: white;
        border: 2px solid #667eea;
        border-radius: 25px;
        padding: 1rem 1.5rem;
        font-size: 1.1rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a0a 0%, #1a1a2e 100%);
    }
    
    /* Career path badges */
    .career-badge {
        display: inline-block;
        background: rgba(102, 126, 234, 0.2);
        color: #667eea;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.3rem;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add welcome message
    st.session_state.messages.append({
        "role": "assistant",
        "content": "👋 Hello! I'm **TechGuide Bot**, your AI-powered programming language advisor.\n\nI help you discover the perfect programming language for your goals. Just tell me what you want to build, and I'll guide you to the best choice with personalized recommendations!\n\n**What would you like to create today?**",
        "timestamp": datetime.now().isoformat()
    })

if "session_id" not in st.session_state:
    import uuid
    st.session_state.session_id = str(uuid.uuid4())

if "backend_status" not in st.session_state:
    st.session_state.backend_status = None

if "auto_refresh" not in st.session_state:
    st.session_state.auto_refresh = True

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def check_backend_health() -> Dict[str, Any]:
    """Check backend health status"""
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        if response.status_code == 200:
            return {"status": "online", "data": response.json()}
        else:
            return {"status": "error", "message": f"HTTP {response.status_code}"}
    except requests.exceptions.ConnectionError:
        return {"status": "offline", "message": "Cannot connect to backend"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def send_chat_message(message: str) -> Dict[str, Any]:
    """Send chat message to backend"""
    try:
        with st.spinner("🤔 Thinking..."):
            response = requests.post(
                f"{BACKEND_URL}/chat",
                json={
                    "message": message,
                    "session_id": st.session_state.session_id
                },
                timeout=15
            )
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "status": "error",
                "response": f"Backend error: {response.status_code}"
            }
    
    except requests.exceptions.ConnectionError:
        return {
            "status": "error",
            "response": "❌ **Connection Error**\n\nCannot reach the backend server. Please ensure it's running:\n```bash\nuvicorn server:app --reload\n```"
        }
    except Exception as e:
        return {
            "status": "error",
            "response": f"Error: {str(e)}"
        }

def get_conversation_history() -> Dict[str, Any]:
    """Get conversation history from backend"""
    try:
        response = requests.get(
            f"{BACKEND_URL}/history/{st.session_state.session_id}",
            timeout=5
        )
        if response.status_code == 200:
            return response.json()
        return {"messages": [], "recommendations": []}
    except:
        return {"messages": [], "recommendations": []}

def display_learning_path(learning_path: List[Dict]):
    """Display learning path timeline"""
    st.markdown("### 🗺️ Your Learning Journey")
    
    for phase in learning_path:
        st.markdown(f"""
        <div class="timeline-item">
            <h4>📘 {phase['phase']} <span style="color: #667eea;">({phase['duration']})</span></h4>
            <ul>
                {''.join([f'<li>{topic}</li>' for topic in phase['topics']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

def display_resources(resources: List[str]):
    """Display learning resources"""
    st.markdown("### 📚 Curated Learning Resources")
    
    for idx, resource in enumerate(resources, 1):
        # Parse resource name and URL if present
        if " - " in resource:
            name, url = resource.split(" - ", 1)
            st.markdown(f"""
            <div class="resource-link">
                {idx}. <strong>{name}</strong><br>
                <a href="{url}" target="_blank" style="color: #667eea; text-decoration: none;">
                    🔗 {url}
                </a>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="resource-link">
                {idx}. <strong>{resource}</strong>
            </div>
            """, unsafe_allow_html=True)

def display_career_paths(career_paths: List[str]):
    """Display career path badges"""
    st.markdown("### 💼 Career Opportunities")
    
    badges_html = "".join([
        f'<span class="career-badge">{path}</span>'
        for path in career_paths
    ])
    
    st.markdown(f'<div style="margin: 1rem 0;">{badges_html}</div>', unsafe_allow_html=True)

def display_recommendation(result: Dict[str, Any]):
    """Display recommendation in beautiful format"""
    
    if result.get("type") == "recommendation":
        language = result.get("language", "Unknown")
        reason = result.get("reason", "")
        resources = result.get("resources", [])
        metadata = result.get("metadata", {})
        
        # Main recommendation card
        st.markdown(f"""
        <div class="recommendation-card">
            <h1 class="language-title">🎯 {language}</h1>
        </div>
        """, unsafe_allow_html=True)
        
        # Metrics row
        if metadata:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>📊 Difficulty</h3>
                    <h2>{metadata.get('difficulty', 'N/A')}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>⏱️ Learning Time</h3>
                    <h2>{metadata.get('estimated_time', 'N/A')}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>🎓 Paths</h3>
                    <h2>{len(metadata.get('career_paths', []))}</h2>
                </div>
                """, unsafe_allow_html=True)
        
        # Reason
        st.markdown("### 💡 Why This Language?")
        st.markdown(f"<p style='font-size: 1.1rem; line-height: 1.8; color: #e0e0e0;'>{reason}</p>", unsafe_allow_html=True)
        
        # Learning path
        if metadata.get("learning_path"):
            display_learning_path(metadata["learning_path"])
        
        # Resources
        if resources:
            display_resources(resources)
        
        # Career paths
        if metadata.get("career_paths"):
            display_career_paths(metadata["career_paths"])
        
        # Classification info (if available)
        if "classification" in result:
            with st.expander("🔍 How I Understood Your Request"):
                classification = result["classification"]
                st.write(f"**Confidence:** {classification.get('confidence', 0):.0%}")
                st.write(f"**Detected Keywords:** {', '.join(classification.get('detected_keywords', []))}")

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.markdown("# 🤖 TechGuide Bot")
    st.markdown("### AI Language Advisor")
    
    st.markdown("---")
    
    # Backend status
    st.markdown("### 🔌 Backend Status")
    
    if st.button("🔄 Check Status", use_container_width=True):
        st.session_state.backend_status = check_backend_health()
    
    if st.session_state.backend_status:
        status = st.session_state.backend_status.get("status")
        
        if status == "online":
            st.markdown('<span class="status-badge status-online">🟢 Online</span>', unsafe_allow_html=True)
            data = st.session_state.backend_status.get("data", {})
            st.caption(f"Version: {data.get('version', 'N/A')}")
        else:
            st.markdown('<span class="status-badge status-offline">🔴 Offline</span>', unsafe_allow_html=True)
            st.caption("Start backend: `uvicorn server:app --reload`")
    
    st.markdown("---")
    
    # Session info
    st.markdown("### 📊 Session Info")
    st.caption(f"**ID:** {st.session_state.session_id[:8]}...")
    st.caption(f"**Messages:** {len(st.session_state.messages)}")
    
    # Quick actions
    st.markdown("---")
    st.markdown("### ⚡ Quick Actions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🌐 Web", use_container_width=True):
            response = send_chat_message("I want to build websites")
            st.session_state.messages.append({
                "role": "user",
                "content": "I want to build websites",
                "timestamp": datetime.now().isoformat()
            })
            st.session_state.messages.append({
                "role": "assistant",
                "content": response.get("response", ""),
                "data": response,
                "timestamp": datetime.now().isoformat()
            })
            st.rerun()
    
    with col2:
        if st.button("📊 Data", use_container_width=True):
            response = send_chat_message("I want to work with data")
            st.session_state.messages.append({
                "role": "user",
                "content": "I want to work with data",
                "timestamp": datetime.now().isoformat()
            })
            st.session_state.messages.append({
                "role": "assistant",
                "content": response.get("response", ""),
                "data": response,
                "timestamp": datetime.now().isoformat()
            })
            st.rerun()
    
    col3, col4 = st.columns(2)
    
    with col3:
        if st.button("📱 Mobile", use_container_width=True):
            response = send_chat_message("I want to create mobile apps")
            st.session_state.messages.append({
                "role": "user",
                "content": "I want to create mobile apps",
                "timestamp": datetime.now().isoformat()
            })
            st.session_state.messages.append({
                "role": "assistant",
                "content": response.get("response", ""),
                "data": response,
                "timestamp": datetime.now().isoformat()
            })
            st.rerun()
    
    with col4:
        if st.button("🎮 Games", use_container_width=True):
            response = send_chat_message("I want to make games")
            st.session_state.messages.append({
                "role": "user",
                "content": "I want to make games",
                "timestamp": datetime.now().isoformat()
            })
            st.session_state.messages.append({
                "role": "assistant",
                "content": response.get("response", ""),
                "data": response,
                "timestamp": datetime.now().isoformat()
            })
            st.rerun()
    
    st.markdown("---")
    
    # Chat history export
    if st.button("💾 Download Chat", use_container_width=True):
        history_json = json.dumps(st.session_state.messages, indent=2)
        st.download_button(
            label="📥 Download JSON",
            data=history_json,
            file_name=f"techguide_chat_{st.session_state.session_id[:8]}.json",
            mime="application/json",
            use_container_width=True
        )
    
    # New chat
    if st.button("🔄 New Chat", type="primary", use_container_width=True):
        import uuid
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = [{
            "role": "assistant",
            "content": "👋 Hello! I'm **TechGuide Bot**. What would you like to build today?",
            "timestamp": datetime.now().isoformat()
        }]
        st.rerun()
    
    st.markdown("---")
    
    # About
    with st.expander("ℹ️ About"):
        st.markdown("""
        **TechGuide Bot** is an AI-powered programming language advisor built with:
        
        - 🧠 **JAC** - Core reasoning engine
        - ⚡ **FastAPI** - Backend API
        - 🎨 **Streamlit** - Interactive UI
        
        **Features:**
        - Conversational AI interface
        - Smart language recommendations
        - Personalized learning paths
        - Career guidance
        - Curated resources
        """)

# ============================================================================
# MAIN CHAT INTERFACE
# ============================================================================

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 TechGuide Bot</h1>
    <p>Your AI-Powered Programming Language Advisor</p>
</div>
""", unsafe_allow_html=True)

# Chat messages container
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        
        if role == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(content)
        else:
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(content)
                
                # Display recommendation if available
                if "data" in message and message["data"].get("ai_powered"):
                    st.caption("🤖 AI-Powered Response (Gemini)")
                    

# Chat input
user_input = st.chat_input("💬 Tell me what you want to build...", key="chat_input")

if user_input:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "timestamp": datetime.now().isoformat()
    })
    
    # Get bot response
    response = send_chat_message(user_input)
    
    # Add bot response
    bot_message = {
        "role": "assistant",
        "content": response.get("response") or response.get("reason", "I couldn't process that. Please try again."),
        "timestamp": datetime.now().isoformat()
    }
    
    if response.get("status") == "ok":
        bot_message["data"] = response
    
    st.session_state.messages.append(bot_message)
    
    # Rerun to display new messages
    st.rerun()

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem 0;">
    <p style="font-size: 0.9rem;">
        Built with ❤️ using <strong>JAC</strong>, <strong>FastAPI</strong>, and <strong>Streamlit</strong>
    </p>
    <p style="font-size: 0.8rem;">
        <a href="http://localhost:8000/docs" target="_blank" style="color: #667eea; text-decoration: none;">📚 API Docs</a> | 
        <a href="http://localhost:8000/health" target="_blank" style="color: #667eea; text-decoration: none;">💚 Health Check</a> |
        <a href="https://github.com/yourusername/techguide-bot" target="_blank" style="color: #667eea; text-decoration: none;">⭐ GitHub</a>
    </p>
</div>
""", unsafe_allow_html=True)