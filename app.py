import streamlit as st
import os
import requests
import streamlit.components.v1 as components
import logging
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from pydantic import BaseModel, model_validator

# Set up environment variables for API keys
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
os.environ["SERPER_API_KEY"] = "YOUR_SERPER_API_KEY"

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Pydantic Model for User with Validation
class User(BaseModel):
    username: str
    age: int

    @model_validator(mode='after')
    def check_age(cls, model):
        if model.age < 18:
            raise ValueError("User must be at least 18 years old.")
        return model


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
        # Placeholder Agent Logic (Define your specific agents here)
        agent = None  # This should be replaced with your defined agent logic
        if selected_aspect == "Philosophical Aspects":
            agent = Agent("Philosophical Explorer", "Explore philosophical aspects of consciousness.")
        elif selected_aspect == "Neural Correlates":
            agent = Agent("Neuroscience Investigator", "Study the neural correlates of consciousness.")
        elif selected_aspect == "Quantum Theories":
            agent = Agent("Quantum Consciousness Theorist", "Explore quantum mechanics and consciousness.")

        if agent:
            response = agent.respond(question)
            st.write(response)
            logger.info(f"User asked: '{question}' and received: '{response}'")
        else:
            st.write("No agent found for the selected aspect.")

    except Exception as e:
        st.write("An error occurred while processing your request.")
        logger.error(f"Error: {str(e)}")
else:
    st.write("Please enter a valid question.")
