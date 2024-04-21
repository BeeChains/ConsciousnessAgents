import os
import streamlit as st
import logging
from crewai import Agent, Task, Crew, Process
from langchain.llms import Ollama
from pydantic import BaseModel, model_validator
from crewai_tools import SerperDevTool


# Set up environment variables for API keys
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
os.environ["SERPER_API_KEY"] = "YOUR_SERPER_API_KEY"

# Initialize logging for monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Define a Pydantic model for User with a basic validation
class User(BaseModel):
    username: str
    age: int

    @model_validator(mode='after')
    def check_age(cls, model):
        if model.age < 18:
            raise ValueError("User must be at least 18 years old.")
        return model


# Define the specialized agents with roles and goals
class PhilosophicalAspectsAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Philosophical Explorer",
            goal="Explore philosophical dimensions of consciousness.",
            backstory="You are a researcher in philosophical studies, exploring various aspects of consciousness.",
            tools=[SerperDevTool()],  # Add the SerperDevTool for search capabilities
            verbose=True,
            allow_delegation=False
        )


class NeuralCorrelatesAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Neuroscience Investigator",
            goal="Identify neural correlates of consciousness.",
            backstory="You are a neuroscience expert focused on discovering brain regions associated with consciousness.",
            verbose=True,
            allow_delegation=False
        )


class QuantumTheoriesAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Quantum Consciousness Theorist",
            goal="Investigate quantum mechanics in relation to consciousness.",
            backstory="You specialize in quantum theories and their implications for consciousness.",
            verbose=True,
            allow_delegation=True
        )


# Initialize the agents with specific roles
agents = {
    "Philosophical Aspects": PhilosophicalAspectsAgent(),
    "Neural Correlates": NeuralCorrelatesAgent(),
    "Quantum Theories": QuantumTheoriesAgent()
}


# Set up Streamlit UI
st.title("Consciousness Research Assistant")

# User selects the aspect of consciousness
selected_aspect = st.selectbox(
    "Choose the aspect of consciousness your question relates to:",
    list(agents.keys())
)

# User inputs their question about consciousness
question = st.text_input("What's your question about consciousness?")

# Process and respond to the question when the 'Ask' button is clicked
if st.button('Ask') and question.strip():
    try:
        agent = agents[selected_aspect]
        response = agent.respond(question)
        st.write(response)
        logger.info(f"User asked: '{question}' and received: '{response}'")
    except Exception as e:
        st.write("An error occurred while processing your request. Please try again.")
        logger.error(f"Error: {str(e)}")
else:
    st.write("Please enter a valid question.")
