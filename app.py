import streamlit as st
import logging
from agent_logic import create_agents  # Function to initialize agents
from agent_controller import AgentController  # Controller to manage agents and interactions

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Streamlit App
st.title("Consciousness Research Assistant")

# Initialize agents and controller
agents = create_agents()  # Get a list of agents
controller = AgentController(agents)  # Create controller to manage agents and Ollama communication

# User question input
question = st.text_input("Ask a question about consciousness:")

# Button to trigger agent responses
if st.button("Ask") and question.strip():
    try:
        # Get responses from all agents using Ollama Llama3 model
        responses = controller.handle_question(question)  # Retrieve responses from agents

        # Display responses in Streamlit
        for agent_name, response in responses.items():
            st.write(f"{agent_name}: {response}")

        logger.info(f"User asked: '{question}' and received responses from agents.")

    except Exception as e:
        st.write("An error occurred while processing your request.")
        logger.error(f"Error: {str(e)}")
else:
    st.write("Please enter a valid question.")
