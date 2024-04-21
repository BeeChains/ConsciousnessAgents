import streamlit as st
import os
import logging
from agent_logic import create_agents  # Function to initialize multiple agents
from agent_controller import AgentController  # Central controller for managing agent responses

# Set up environment variables for API keys (ensure these are set correctly in your system)
os.environ["LLAMA3_API_KEY"] = "YOUR_LLAMA3_API_KEY"  # Replace with your API key

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Streamlit App
st.title("Consciousness Research Assistant")

# Initialize agents
agents = create_agents()  # Function to initialize and return a list of agents

# Create agent controller
controller = AgentController(agents)  # Controller to manage agent interactions

# User question input
question = st.text_input("Ask a question about consciousness:")

# Button to trigger agent responses
if st.button("Ask") and question.strip():
    try:
        # Get responses from all agents
        responses = controller.handle_question(question)  # Get responses from all agents

        # Display responses in Streamlit
        for agent_name, response in responses.items():
            st.write(f"{agent_name}: {response}")

        logger.info(f"User asked: '{question}' and received responses from agents.")

    except Exception as e:
        st.write("An error occurred while processing your request.")
        logger.error(f"Error: {str(e)}")
else:
    st.write("Please enter a valid question.")
