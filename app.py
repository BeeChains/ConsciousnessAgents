import streamlit as st
import logging
from streamlit_agent_logic import get_agents  # Importing the list of agents

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Streamlit app
st.title("Consciousness Research Assistant")

# Define agent expertise
agents = get_agents()  # This returns a list of agents, each with a specific role/expertise

# Track the interaction history
interaction_history = []

# Function to interact with agents and gather responses based on their expertise
def interact_with_agents(question):
    # Create a new interaction for this question
    interaction = {"User": question}
    
    for agent in agents:
        # Each agent provides a response based on their expertise
        response = agent.respond(question)
        interaction[agent.name] = response  # Store each agent's response

    interaction_history.append(interaction)  # Add the new interaction to the history

# User question input
question = st.text_input("Enter your question about consciousness:")

# Button to trigger agent interactions
if st.button("Ask") and question.strip():
    try:
        interact_with_agents(question)  # Interact with all agents

        # Display the interaction history
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
