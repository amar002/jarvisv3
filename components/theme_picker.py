import streamlit as st
from utils.goal_generator import generate_improved_goals

def theme_picker_flow():
    st.subheader("Pick a theme to focus on:")
    themes = ["Health", "Finance", "Coding", "Sleep Habits", "Workout"]
    
    # Allow users to add multiple goals
    if "goals_data" not in st.session_state:
        st.session_state.goals_data = []

    with st.form(key="goal_form"):
        selected_theme = st.selectbox("Choose your theme:", themes, key="theme_selector")
        user_goal = st.text_area("Input your goal here:", key="goal_input")
        submit_button = st.form_submit_button("Add Goal")
        
        if submit_button and user_goal.strip():
            st.session_state.goals_data.append({"theme": selected_theme, "goal": user_goal, "improved_goal": None})
            st.success("Goal added successfully!")
    
    # Display the added goals
    st.subheader("Your Goals")
    for idx, goal_data in enumerate(st.session_state.goals_data):
        st.write(f"**Theme:** {goal_data['theme']}")
        st.write(f"**Goal:** {goal_data['goal']}")
        if goal_data["improved_goal"]:
            st.write(f"**Improved Goal:** {goal_data['improved_goal']}")
    
    # Generate improved goals
    if st.button("Generate Improved Goals"):
        for goal_data in st.session_state.goals_data:
            if not goal_data["improved_goal"]:
                goal_data["improved_goal"] = generate_improved_goals(goal_data["theme"], goal_data["goal"])
        st.experimental_rerun()
    
    # Review and finalize improved goals
    if any(goal["improved_goal"] for goal in st.session_state.goals_data):
        st.subheader("Review and Finalize Your Goals")
        for idx, goal_data in enumerate(st.session_state.goals_data):
            st.write(f"**Theme:** {goal_data['theme']}")
            st.text_area("Edit Improved Goal:", value=goal_data["improved_goal"], key=f"improved_goal_{idx}")
        
        if st.button("Accept the Goals"):
            # Add goals to habit list
            if "habits_data" not in st.session_state:
                st.session_state.habits_data = []
            for goal_data in st.session_state.goals_data:
                st.session_state.habits_data.append({"name": goal_data["improved_goal"], "status": "Pending"})
            st.success("Goals added to your habit list!")
            st.session_state.goals_data = []  # Clear goals
            st.experimental_rerun()

    # Retry flow
    if st.button("Retry"):
        st.session_state.goals_data = []  # Clear goals data
        st.experimental_rerun()
