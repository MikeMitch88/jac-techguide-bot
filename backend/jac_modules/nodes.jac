# All node definitions
"""
Node definitions for TechGuide Bot API
All conversation states and data structures
"""

# Session management node
node SessionNode {
    has session_id: str = "";
    has timestamp: str = "";
    has last_choice: str = "";
    has conversation_history: list = [];
    
    can log_interaction with entry {
        # Log interaction details
        if self.session_id {
            self.conversation_history.append({
                "choice": self.last_choice,
                "timestamp": self.timestamp
            });
        }
    }
}

# Welcome state node
node WelcomeNode {
    has message: str = "Welcome to TechGuide Bot API";
    has version: str = "2.0";
    
    can get_welcome_data with entry {
        # Returns structured welcome data
        return {
            "message": self.message,
            "version": self.version,
            "status": "ready"
        };
    }
}

# Interest collection node
node InterestNode {
    has options: dict = {
        "1": "Web Development",
        "2": "Data Science",
        "3": "Mobile Apps",
        "4": "Game Development"
    };
    has valid_choices: list = ["1", "2", "3", "4"];
    
    can validate_choice(choice: str) -> bool {
        return choice in self.valid_choices;
    }
    
    can get_interest_name(choice: str) -> str {
        return self.options.get(choice, "Unknown");
    }
}

# Recommendation node
node RecommendNode {
    has language: str = "";
    has reason: str = "";
    has difficulty: str = "Beginner";
    has estimated_time: str = "3-6 months";
    
    can get_recommendation_data with entry {
        return {
            "language": self.language,
            "reason": self.reason,
            "difficulty": self.difficulty,
            "estimated_time": self.estimated_time
        };
    }
}

# Resource node
node ResourceNode {
    has resources: list = [];
    has resource_types: dict = {
        "docs": [],
        "tutorials": [],
        "videos": []
    };
    
    can get_resources_data with entry {
        return {
            "resources": self.resources,
            "resource_types": self.resource_types
        };
    }
}

# Result aggregation node
node ResultNode {
    has status: str = "ok";
    has language: str = "";
    has reason: str = "";
    has resources: list = [];
    has metadata: dict = {};
    
    can compile_result with entry {
        return {
            "status": self.status,
            "language": self.language,
            "reason": self.reason,
            "resources": self.resources,
            "metadata": self.metadata
        };
    }
}

# Error handling node
node ErrorNode {
    has error_message: str = "";
    has error_code: str = "INVALID_INPUT";
    
    can get_error_data with entry {
        return {
            "status": "error",
            "message": self.error_message,
            "code": self.error_code
        };
    }
}