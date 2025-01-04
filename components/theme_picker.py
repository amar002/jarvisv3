import streamlit as st
from utils.gemini_api import get_gpt_response

def theme_picker_flow():
    st.subheader("Pick a theme to focus on:")
    themes = ["Health", "Finance", "Coding", "Sleep Habits", "Workout"]
    selected_theme = st.selectbox("Choose your theme:", themes)

    st.text_area("Input your goals here:", key="user_goal_input")

    if st.button("Improve My Goals"):
        user_goal = st.session_state.get("user_goal_input", "")
        prompt = f"Improve and suggest actionable steps for this goal in the context of {selected_theme}: {user_goal}"
        improved_goal = get_gpt_response(prompt)
        st.subheader("Here are some suggestions to refine your goals:")
        st.write(improved_goal)
