import streamlit as st
from components.theme_picker import theme_picker_flow
from components.question_flow import question_flow
from components.plan_builder import plan_builder
from utils.data_handler import save_habits

def interactive_onboarding():
    st.title("Welcome to HabitFlow!")
    st.subheader("Do you have clarity about your goals?")

    # Display options for user choice
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, I know what to do, show me how"):
            st.session_state.user_choice = "yes"
    with col2:
        if st.button("No, Need help in figuring out what to do"):
            st.session_state.user_choice = "no"

    # Route based on user choice
    user_choice = st.session_state.get("user_choice")
    if user_choice == "yes":
        theme_picker_flow()
    elif user_choice == "no":
        question_flow()

    # After accepting goals, invoke the Plan Builder
    if "goals_data" in st.session_state and st.session_state.goals_data:
        st.subheader("Finalize Your Goals")
        for idx, goal_data in enumerate(st.session_state.goals_data):
            st.write(f"**Goal {idx+1}:** {goal_data['improved_goal']}")
        if st.button("Generate Plans for Goals"):
            for goal_data in st.session_state.goals_data:
                plan_builder(goal_data["improved_goal"])  # Generate and display plans for each goal
            st.session_state.goals_data = []  # Clear goals after generating plans

    # Save data persistently after onboarding
    if "habits_data" in st.session_state:
        save_habits(st.session_state.habits_data)

    # Debugging logs (optional)
    #st.write("Session state:", st.session_state)
