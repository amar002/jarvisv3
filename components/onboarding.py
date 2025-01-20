import streamlit as st
from components.theme_picker import theme_picker_flow
from components.question_flow import question_flow
from utils.data_handler import save_habits


def interactive_onboarding():
    st.title("Welcome to HabitFlow!")
    st.subheader("Do you have clarity about your goals?")

    # User choice: Yes or No
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

    # Handle Goals After Generation
    if "goals_data" in st.session_state and st.session_state.goals_data:
        st.subheader("Review Your Goals")

        # Show a brief outline of goals
        for idx, goal_data in enumerate(st.session_state.goals_data):
            st.write(f"**Goal {idx+1}:** {goal_data['improved_goal'] or goal_data['goal']}")

        # Accept goals to finalize them
        if st.button("Accept My Goals"):
            # Save the finalized goals to habits_data for dashboard display
            if "habits_data" not in st.session_state:
                st.session_state.habits_data = []
            for goal_data in st.session_state.goals_data:
                st.session_state.habits_data.append(
                    {"name": goal_data["improved_goal"] or goal_data["goal"], "status": "Pending"}
                )

            # Save persistently and clear goals_data
            save_habits(st.session_state.habits_data)
            st.session_state.goals_data = []  # Clear goals data after saving

            # Navigate to dashboard
            st.success("Your goals have been saved! You can find them under 'My Goals' on the Dashboard.")
            st.session_state.current_page = "Dashboard"

    # Debugging logs (optional)
    #st.write("Session state:", st.session_state)
