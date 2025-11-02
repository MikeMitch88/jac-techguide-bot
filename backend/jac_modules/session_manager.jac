"""
Session management for TechGuide Bot
Handles conversation context and history
"""

import:py from datetime { datetime }
import:py from uuid { uuid4 }

# Session storage node
node SessionNode {
    has session_id: str = "";
    has created_at: str = "";
    has messages: list = [];
    has user_interests: list = [];
    has recommendations: list = [];
    
    can add_message(role: str, content: str) {
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": str(datetime.now())
        });
    }
    
    can add_recommendation(language: str, choice: str) {
        self.recommendations.append({
            "language": language,
            "choice": choice,
            "timestamp": str(datetime.now())
        });
    }
    
    can get_history with entry {
        return {
            "session_id": self.session_id,
            "messages": self.messages,
            "recommendations": self.recommendations,
            "created_at": self.created_at
        };
    }
}

# Walker for session management
walker SessionManager {
    has session_id: str = "";
    has action: str = "";  # "create", "get", "update"
    has data: dict = {};
    has result: dict = {};
    
    can start with `root entry {
        if self.action == "create" {
            new_session = SessionNode(
                session_id=str(uuid4()),
                created_at=str(datetime.now())
            );
            root ++> new_session;
            self.result = {"session_id": new_session.session_id};
        }
        visit [-->];
    }
    
    can handle_session with SessionNode entry {
        if self.action == "get" and here.session_id == self.session_id {
            self.result = here.get_history();
        }
        disengage;
    }
}