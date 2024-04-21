class Agent:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def respond(self, question):
        # This is a simple response mechanism; adjust based on the agent's role
        return f"{self.name}: {self.description} - In response to your question, '{question}'"
