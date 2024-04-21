# ConsciousnessAgents
LLama3 Consciousness Agents - Agent 1: Handles inquiries about the philosophical aspects of consciousness. Agent 2: Deals with the neural correlates of consciousness. Agent 3: Focuses on quantum theories of consciousness.

# Modelfile

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


    
# Install 
    git clone https://github.com/BeeChains/ConsciousnessAgents.git
    pip install -r requirements.txt

# RUN
streamlit run app.py
