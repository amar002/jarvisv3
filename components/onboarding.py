import streamlit as st
from utils.gemini_api import get_gpt_response  # Ensure this function is defined and imported

def interactive_onboarding():
    st.title("Welcome to HabitFlow!")
    st.subheader("Let’s learn more about you to suggest personalized goals and habits.")

    if "user_responses" not in st.session_state:
        st.session_state.user_responses = {}
    if "dynamic_questions" not in st.session_state:
        st.session_state.dynamic_questions = []

    # Generate dynamic questions using Gemini LLM
    if not st.session_state.dynamic_questions:
        prompt = (
            "Generate 4 personalized onboarding questions for a habit-building platform. "
            "The questions should help understand a user's goals, strengths, and challenges."
        )
        response = get_gpt_response(prompt)
        st.session_state.dynamic_questions = response.split("\n")  # Assuming LLM response contains line-separated questions

    # Ask dynamic questions
    for idx, question in enumerate(st.session_state.dynamic_questions):
        st.session_state.user_responses[f"question_{idx+1}"] = st.text_input(question.strip(), key=f"question_{idx+1}")

    if st.button("Generate My Goals"):
        st.session_state.retry = False
        prompt = (
            f"Based on the following user responses, generate 3 personalized goals, explain why they are important, "
            f"and provide a simple plan to achieve each:\n\n"
        )
        for idx, (key, response) in enumerate(st.session_state.user_responses.items(), 1):
            prompt += f"{idx}. {response}\n"
        
        prompt += (
            "\nProvide output in this format:\n"
            "- Goal 1: [Goal]\n"
            "  Reason: [Why this goal is important]\n"
            "  Plan: [Simple plan to achieve the goal]\n"
            "- Goal 2: ...\n"
            "- Goal 3: ..."
        )
        st.session_state.generated_goals = get_gpt_response(prompt)

    # Display generated goals
    if "generated_goals" in st.session_state and not st.session_state.get("retry", False):
        st.subheader("Here are your personalized goals:")
        st.write(st.session_state.generated_goals)

        # Accept or Retry options
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Accept the Goals"):
                st.session_state.edit_goals = True
        with col2:
            if st.button("Retry"):
                st.session_state.retry = True
                st.session_state.generated_goals = None
                st.experimental_rerun()

    # Edit and Save Goals
    if st.session_state.get("edit_goals", False):
        st.subheader("Edit and Save Your Goals")
        goals = st.session_state.generated_goals.split("- Goal")[1:]
        for i, goal in enumerate(goals, start=1):
            edited_goal = st.text_area(f"Goal {i}:", value=goal.strip())
            st.session_state.habits_data.append({"name": f"Goal {i}: {edited_goal}", "due": "Today", "status": "Pending"})

        if st.button("Save Goals"):
            st.success("Goals added to your habit list!")
            st.session_state.edit_goals = False
            st.experimental_rerun()
