import streamlit as st
import requests
import logging
from agent_controller import AgentController  # Controller to manage interactions with Ollama

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define Streamlit app
st.title("Consciousness Research Assistant")

# Initialize agent controller with the Consciousness Agents model
controller = AgentController("consciousness_agents")

# User question input
question = st.text_input("Ask a question about consciousness:")

# Respond to user question
if st.button("Ask") and question.strip():
    try:
        # Get response from the Consciousness Agents model
        response = controller.get_response(question)
        st.write(f"Response: {response}")

    except Exception as e:
        st.write("An error occurred while processing your request.")
else:
    st.write("Please enter a valid question.")
