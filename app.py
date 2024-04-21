import streamlit as st
import os
import logging
from pydantic import BaseModel, root_validator  # Updated import for Pydantic validation
from agent_logic import Agent  # Importing Agent from agent_logic.py
from streamlit_agent_logic import get_agent  # Importing helper function

# Set environment variables for API keys (ensure these are set correctly in your system)
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
os.environ["SERPER_API_KEY"] = "YOUR_SERPER_API_KEY"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Streamlit App
st.title("Consciousness Research Assistant")

# Select an aspect of consciousness
aspect_choices = ["Philosophical Aspects", "Neural Correlates", "Quantum Theories"]
selected_aspect = st.selectbox("Choose an aspect of consciousness:", aspect_choices)

# Input a question
question = st.text_input("Enter your question about consciousness:")

# Respond to the question when the 'Ask' button is clicked
if st.button('Ask') and question.strip():
    try:
        # Get the appropriate agent based on the selected aspect
        agent = get_agent(selected_aspect)  # Using the helper function to get the agent

        if agent:
            response = agent.respond(question)  # Assuming Agent has a respond method
            st.write(response)  # Displaying the response in Streamlit
            logger.info(f"User asked: '{question}' and received: '{response}'")
        else:
            st.write("No agent found for the selected aspect.")  # Error handling for agent logic

    except Exception as e:
        st.write("An error occurred while processing your request.")
        logger.error(f"Error: {str(e)}")  # Detailed logging for easier debugging
else:
    st.write("Please enter a valid question.")  # User-friendly message if input is invalid
