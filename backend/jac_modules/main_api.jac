# JAC API entry point
"""
Main API entry point for TechGuide Bot
Exposes JAC walkers for external invocation
"""

# Import nodes and walkers
include:jac nodes;
include:jac walkers;

# Main graph initialization
with entry {
    # Initialize root node
    root;
}

# API endpoint handlers (can be called from Python)
walker get_recommendation {
    has choice: str;
    has session_id: str = "";
    
    can execute with `root entry {
        agent = TechGuideAgent(
            choice=self.choice,
            session_id=self.session_id
        );
        root spawn agent;
        report agent.result;
    }
}

walker classify_text {
    has text: str;
    
    can execute with `root entry {
        classifier = ClassifierWalker(input_text=self.text);
        root spawn classifier;
        report classifier.result;
    }
}

walker health_check {
    can execute with `root entry {
        health = HealthCheckWalker();
        root spawn health;
        report health.result;
    }
}