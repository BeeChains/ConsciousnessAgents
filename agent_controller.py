# Central controller to manage agent responses and combine them
class AgentController:
    def __init__(self, agents):
        self.agents = agents  # List of agents
    
    def handle_question(self, question):
        # Gather responses from all agents
        responses = {}
        
        for agent in self.agents:
            responses[agent.name] = agent.respond(question)  # Get each agent's response
        
        # You could add logic here to combine responses or provide additional analysis
        
        return responses  # Return a dictionary of agent responses
