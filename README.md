# ConsciousnessAgents
LLama3 Consciousness Agents - Agent 1: Handles inquiries about the philosophical aspects of consciousness. Agent 2: Deals with the neural correlates of consciousness. Agent 3: Focuses on quantum theories of consciousness.

# Modelfile

    # Define the model source (e.g., Llama, GPT, or another base model)
    FROM llama3

    # Set temperature to control creativity
    PARAMETER temperature 1  # Higher is more creative, lower is more coherent

    # Set the system message to establish the model's context
    SYSTEM """
    You are a consciousness expert. Answer questions about consciousness, including philosophical, neurological, and quantum aspects.
    """

    # Optional: Set other parameters like top_p, frequency_penalty, etc.

    
# Install 
    git clone https://github.com/BeeChains/ConsciousnessAgents.git
    pip install -r requirements.txt

# RUN
streamlit run app.py
