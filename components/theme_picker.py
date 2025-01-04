import streamlit as st
from utils.goal_generator import generate_improved_goals

def theme_picker_flow():
    st.subheader("Pick a theme to focus on:")
    themes = ["Health", "Finance", "Coding", "Sleep Habits", "Workout"]
    
    # Initialize goals_data if not already done
    if "goals_data" not in st.session_state:
        st.session_state.goals_data = []

    # Form to add multiple goals
    with st.form(key="goal_form"):
        selected_theme = st.selectbox("Choose your theme:", themes, key="theme_selector")
        user_goal = st.text_area("Input your goal here:", key="goal_input")
        submit_button = st.form_submit_button("Add Goal")
        
        if submit_button and user_goal.strip():
            st.session_state.goals_data.append({"theme": selected_theme, "goal": user_goal, "improved_goal": None})
            st.success("Goal added successfully!")

    # Display added goals
    st.subheader("Your Goals")
    for idx, goal_data in enumerate(st.session_state.goals_data):
        col1, col2 = st.columns([8, 1])
        with col1:
            st.write(f"**Theme:** {goal_data['theme']} | **Goal:** {goal_data['goal']}")
        with col2:
            if st.button("❌", key=f"remove_{idx}"):
                st.session_state.goals_data.pop(idx)
                st.success("Goal removed successfully!")
                st.experimental_set_query_params(reload=True)  # Refresh after removing a goal

    # Button to improve all goals
    if st.session_state.goals_data:
        if st.button("Improve My Goals"):
            for goal_data in st.session_state.goals_data:
                if not goal_data["improved_goal"]:
                    goal_data["improved_goal"] = generate_improved_goals(goal_data["theme"], goal_data["goal"])
            st.experimental_set_query_params(reload=True)  # Refresh to show improved goals

    # Show improved goals
    if any(goal["improved_goal"] for goal in st.session_state.goals_data):
        st.subheader("Improved Goals")
        for idx, goal_data in enumerate(st.session_state.goals_data):
            st.text_area(f"Improved Goal for {goal_data['theme']}:",
                         value=goal_data["improved_goal"], key=f"edit_goal_{idx}")

        # Accept the goals
        if st.button("Accept the Goals"):
            if "habits_data" not in st.session_state:
                st.session_state.habits_data = []
            for goal_data in st.session_state.goals_data:
                st.session_state.habits_data.append({"name": goal_data["improved_goal"], "status": "Pending"})
            st.success("Goals added to your habit list!")
            st.session_state.goals_data = []  # Clear goals data after accepting
            st.experimental_set_query_params(reload=True)  # Refresh to reset flow
