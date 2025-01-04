import streamlit as st
from utils.gemini_api import get_gpt_response

def question_flow():
    st.subheader("Let’s learn more about you to suggest personalized goals and habits.")

    if "user_responses" not in st.session_state:
        st.session_state.user_responses = {}

    questions = [
        "What is one habit you’re proud of and want to continue?",
        "Where do you see yourself a year from now? (Describe your ideal self)",
        "What’s one skill or strength you excel at?",
        "What is one habit you struggle to maintain?"
    ]

    for idx, question in enumerate(questions):
        st.session_state.user_responses[f"question_{idx+1}"] = st.text_input(question, key=f"question_{idx+1}")

    if st.button("Generate My Goals"):
        prompt = (
            "Based on the following user input, generate 3 personalized goals, explain why they are important, "
            "and provide a simple plan to achieve each:\n\n"
        )
        for idx, response in st.session_state.user_responses.items():
            prompt += f"{idx}: {response}\n"
        
        prompt += (
            "\nProvide output in this format:\n"
            "- Goal 1: [Goal]\n"
            "  Reason: [Why this goal is important]\n"
            "  Plan: [Simple plan to achieve the goal]\n"
            "- Goal 2: ...\n"
            "- Goal 3: ..."
        )
        st.session_state.generated_goals = get_gpt_response(prompt)
        st.subheader("Here are your personalized goals:")
        st.write(st.session_state.generated_goals)
