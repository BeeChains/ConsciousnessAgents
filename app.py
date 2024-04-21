import streamlit as st
import os
import logging
from pydantic import BaseModel, root_validator
from agent_logic import Agent  # Assuming this module defines the Agent class
from streamlit_agent_logic import get_agents  # Modified to return a list of agents

# Set environment variables for API keys
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
os.environ["SERPER_API_KEY"] = "YOUR_SERPER_API_KEY"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Streamlit App
st.title("Consciousness Research Assistant")

# Define agent interactions
agents = get_agents()  # Get a list of agents from the helper function

# Interaction history
interaction_history = []

# Define a function to interact with agents
def interact_with_agents(question):
    # Simulate a dialogue between agents based on user input
    interaction = {"User": question}
    
    for agent in agents:
        # Each agent responds to the question
        response = agent.respond(question)
        interaction[agent.name] = response  # Store the agent's response in the history
    
    interaction_history.append(interaction)  # Add interaction to history

# User question input
question = st.text_input("Enter your question about consciousness:")

# Respond to the question when the 'Ask' button is clicked
if st.button("Ask") and question.strip():
    try:
        interact_with_agents(question)  # Trigger interaction with agents
        
        # Display interaction history
        for i, interaction in enumerate(interaction_history):
            st.write(f"Interaction {i + 1}:")
            for key, value in interaction.items():
                st.write(f"{key}: {value}")

        logger.info(f"User asked: '{question}' and interacted with agents.")

    except Exception as e:
        st.write("An error occurred while processing your request.")
        logger.error(f"Error: {str(e)}")
else:
    st.write("Please enter a valid question.")
