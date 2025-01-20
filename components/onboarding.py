import streamlit as st
from components.theme_picker import theme_picker_flow
from components.question_flow import question_flow
from utils.data_handler import save_habits, load_habits

def interactive_onboarding():
    st.title("Welcome to HabitFlow!")
    st.subheader("Do you have clarity about your goals?")

    # Two paths based on user selection
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, I know what to do, show me how"):
            st.session_state.user_choice = "yes"
    with col2:
        if st.button("No, Need help in figuring out what to do"):
            st.session_state.user_choice = "no"

    # Route to appropriate flow
    if st.session_state.get("user_choice") == "yes":
        theme_picker_flow()
    elif st.session_state.get("user_choice") == "no":
        question_flow()

    # Save data persistently after onboarding
    if "habits_data" in st.session_state:
        save_habits(st.session_state.habits_data)

    # Ensure query params reflect the current state
    if st.session_state.get("user_choice"):
        st.query_params["user_choice"] = st.session_state.user_choice

    # Debugging logs (optional)
    #st.write("Session state:", st.session_state)
    #st.write("Query params:", st.query_params)
