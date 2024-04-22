# ConsciousnessAgents
LLama3 Consciousness Agents - Agent 1: Handles inquiries about the philosophical aspects of consciousness. Agent 2: Deals with the neural correlates of consciousness. Agent 3: Focuses on quantum theories of consciousness.

# Consciousness Agents Model with Ollama and Streamlit

## Overview
This project demonstrates creating a Consciousness Agents model using Ollama and running agents in a Streamlit app. The Consciousness Agents model uses three agents with unique expertise to collaboratively answer questions about consciousness.

## Prerequisites
Before starting, ensure you have the following installed and set up:

- **Python 3.7+**: Required for running Streamlit and interacting with Ollama.
- **Ollama**: The platform for creating and running the Consciousness Agents model.
- **Streamlit**: A framework for building and running interactive web applications in Python.

# Install 
    git clone https://github.com/BeeChains/ConsciousnessAgents.git
    pip install -r requirements.txt
    
## Setting Up Ollama
To install and set up Ollama, follow these steps:

1. **Install Ollama**: Install Ollama on your system. Refer to the [Ollama Installation Guide](https://github.com/ollama/ollama) for specific instructions.
2. **Verify Installation**: Confirm that Ollama is installed and running:
   ```bash
   ollama --version


# Creating the Consciousness Agents Modelfile

    # Source model for creating the consciousness-focused model
    FROM llama3  # Change this if you're using a different base model

    # Set temperature for creativity
    PARAMETER temperature 0.7  # Adjust this based on desired creativity

    # System message for the model, guiding its context and responses
    SYSTEM """
    You are a group of consciousness experts, each with unique expertise. 
    1. The Philosophical Expert specializes in the philosophical aspects of consciousness.
    2. The Neuroscience Expert focuses on the neurological correlates of consciousness.
    3. The Quantum Expert explores the quantum mechanics of consciousness.
    Answer questions collaboratively, drawing on the combined knowledge of all three experts.
    """

    # Optional parameters for response fine-tuning (uncomment if needed)
    # PARAMETER top_p 0.9  # Controls diversity in responses
    # PARAMETER frequency_penalty 0.5  # Penalizes repeated tokens
    # PARAMETER presence_penalty 0.3  # Penalizes repeated topics or concepts

# Create the Consciousness Agents model using Ollama's create API endpoint
    curl http://localhost:11420/api/create -d '{
    "name": "consciousness_agents",
    "modelfile": "FROM llama3\nPARAMETER temperature 0.7\nSYSTEM \"You are a group of consciousness experts.\"\n"
}'

# With the Modelfile Create the Consciousness Agents Model
    ollama create consciousness_agents -f Modelfile
    
# Run Consciousness Agents Model
    ollama run consciousness_agents

# Test the Connection
    curl http://localhost:11420/api/generate

# RUN
streamlit run app.py
