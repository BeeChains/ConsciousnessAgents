import requests  # Using requests to communicate with Ollama Llama3

# Central controller to manage agent responses and interact with Ollama
class AgentController:
    def __init__(self, agents):
        self.agents = agents  # List of agents
    
    def interact_with_ollama(self, prompt):
        # Interact with Ollama Llama3 to generate responses
        try:
            # Call Ollama with the given prompt
            response = requests.post(
                "http://localhost:11420/api/generate",  # Ollama API endpoint
                json={"prompt": prompt}  # Send the user's question as the prompt
            )

            # Return the response text
            if response.status_code == 200:
                return response.json().get("text", "No response received")
            else:
                raise Exception(f"Error from Ollama: {response.status_code}")

        except Exception as e:
            raise Exception(f"Failed to interact with Ollama: {str(e)}")

    def handle_question(self, question):
        # Collect responses from all agents using Ollama Llama3
        responses = {}
        
        for agent in self.agents:
            # Each agent sends a prompt to Ollama and retrieves the response
            prompt = f"{agent.name} about {agent.expertise}: {question}"
            responses[agent.name] = self.interact_with_ollama(prompt)
        
        return responses
