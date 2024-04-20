from crewai import CrewAIOrchestrator
from langchain_community_llms import Ollama

# Initialize the LLaMA model with Ollama and CrewAI orchestrator
ollama = Ollama(model="llama3:8b")
crewai_orchestrator = CrewAIOrchestrator()

# Example function to distribute queries to the appropriate LLaMA agent
def process_query_with_crewai(question, aspect):
    agent_id = determine_agent_id(aspect)
    # Using CrewAI to orchestrate which agent to send the query to
    response = crewai_orchestrator.orchestrate(ollama, agent_id, question)
    return response

def determine_agent_id(aspect):
    # Logic to determine agent based on the aspect of consciousness
    return agent_id

import streamlit as st
from crewai_integration import process_query_with_crewai

st.title("Consciousness Research Assistant")

agent_options = {
    "Philosophical Aspects": 1,
    "Neural Correlates": 2,
    "Quantum Theories": 3,
}

question = st.text_input("What's your question about consciousness?")
selected_aspect = st.selectbox("Choose the aspect of consciousness your question relates to:", list(agent_options.keys()))

if st.button("Ask"):
    if question:
        response = process_query_with_crewai(question, selected_aspect)
        st.write(response)
    else:
        st.write("Please enter a question.")
