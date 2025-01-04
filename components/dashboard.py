import streamlit as st
from components.goal_completion import generate_appreciation_message

def display_dashboard():
    st.write("### Habit Dashboard")
    
    for i, habit in enumerate(st.session_state.habits_data):
        col1, col2, col3 = st.columns([4, 1, 1])

        with col1:
            st.write(f"📝 {habit['name']} - **{habit['status']}**")

        with col2:
            if st.button("Done", key=f"done_{i}"):
                habit["status"] = "Completed"
                message = generate_appreciation_message(habit["name"])
                st.success(message)
                st.experimental_rerun()

        with col3:
            if st.button("Remove", key=f"remove_{i}"):
                st.session_state.habits_data.pop(i)
                st.warning(f"Removed habit: {habit['name']}")
                st.experimental_rerun()
