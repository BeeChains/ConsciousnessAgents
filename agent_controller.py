import requests  # To interact with Ollama's Llama3 model

# Controller to manage agent interactions with Ollama
class AgentController:
    def __init__(self, model_name):
        self.model_name = model_name  # Name of the consciousness-focused model
    
    def get_response(self, prompt):
        # Send a request to Ollama's Llama3 model to generate a response
        try:
            response = requests.post(
                f"http://localhost:11434/api/generate",  # Endpoint for Ollama server
                json={"model": self.model_name, "prompt": prompt}
            )
            
            if response.status_code == 200:
                return response.json().get("text", "No response received")
            else:
                raise Exception(f"Error from Ollama: {response.status_code}")
        
        except Exception as e:
            raise Exception(f"Failed to interact with Ollama: {str(e)}")
