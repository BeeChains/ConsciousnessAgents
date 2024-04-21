import streamlit as st
import logging
from agent_controller import AgentController  # Controller to manage interactions with Ollama

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define Streamlit App
st.title("Consciousness Research Assistant")

# Instantiate the agent controller
controller = AgentController("consciousness")  # Name of the consciousness-focused model

# User question input
question = st.text_input("Ask a question about consciousness:")

# Button to trigger agent responses
if st.button("Ask") and question.strip():
    try:
        # Get the response from the consciousness-focused model via the controller
        response = controller.get_response(question)

        # Display the response in Streamlit
        st.write(f"Response: {response}")

        logger.info(f"User asked: '{question}' and received response: '{response}'.")

    except Exception as e:
        st.write("An error occurred while processing your request.")
        logger.error(f"Error: {str(e)}")
else:
    st.write("Please enter a valid question.")
