import streamlit as st
from components.theme_picker import theme_picker_flow
from components.question_flow import question_flow
from utils.data_handler import save_habits, load_habits

def interactive_onboarding():
    st.title("Welcome to HabitFlow!")
    st.subheader("Do you have clarity?")

    # Two paths based on user selection
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, I know what to do, show me how"):
            st.session_state.user_choice = "yes"
    with col2:
        if st.button("No, Need help in figuring out what to do"):
            st.session_state.user_choice = "no"

   if st.session_state.get("user_choice") == "yes":
    theme_picker_flow()
elif st.session_state.get("user_choice") == "no":
    question_flow()

# Navigation to reset or switch
st.query_params["reload"] = "true"  # Updated for deprecation warning
