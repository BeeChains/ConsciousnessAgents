from agent_logic import Agent

def get_agent(selected_aspect):
    # Define agents based on the selected aspect
    if selected_aspect == "Philosophical Aspects":
        return Agent("Philosophical Explorer", "Explore philosophical aspects of consciousness.")
    elif selected_aspect == "Neural Correlates":
        return Agent("Neuroscience Investigator", "Study the neural correlates of consciousness.")
    elif selected_aspect == "Quantum Theories":
        return Agent("Quantum Consciousness Theorist", "Explore quantum mechanics and consciousness.")
    else:
        return None  # No agent found if the aspect doesn't match any predefined cases
