import streamlit as st
from utils.gemini_api import get_gpt_response

def interactive_onboarding():
    st.title("Welcome to HabitFlow!")
    st.subheader("Let’s learn more about you to suggest personalized goals and habits.")
    
    user_responses = {}
    user_responses['habit_proud'] = st.text_input("What is one habit you’re proud of and want to continue?")
    user_responses['future_self'] = st.text_area("Where do you see yourself a year from now? (Describe your ideal self)")
    user_responses['strength'] = st.text_input("What’s one skill or strength you excel at?")
    
    if st.button("Generate My Goals"):
        prompt = (
            f"Based on the following user input, generate 3 personalized goals, explain why they are important, "
            f"and provide a simple plan to achieve each:\n\n"
            f"1. Habit they are proud of: {user_responses['habit_proud']}\n"
            f"2. Ideal self in one year: {user_responses['future_self']}\n"
            f"3. Strength or skill: {user_responses['strength']}\n\n"
            f"Provide output in this format:\n"
            f"- Goal 1: [Goal]\n"
            f"  Reason: [Why this goal is important]\n"
            f"  Plan: [Simple plan to achieve the goal]\n"
        )
        goals = get_gpt_response(prompt)
        st.session_state.generated_goals = goals
        st.write(goals)
