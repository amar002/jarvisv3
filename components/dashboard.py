import streamlit as st
from utils.data_handler import load_habits
from utils.data_handler import save_habits


def display_dashboard():
    st.title("My Goals")

    # Load habits
    habits = load_habits()

    if not habits:
        st.write("No goals available. Start by creating goals in the onboarding flow!")
    else:
        for idx, habit in enumerate(habits):
            col1, col2, col3 = st.columns([7, 2, 1])
            with col1:
                st.write(f"**{habit['name']}** - Status: {habit['status']}")
            with col2:
                if st.button("Mark as Done", key=f"done_{idx}"):
                    habits[idx]["status"] = "Completed"
                    st.success(f"Marked '{habit['name']}' as done!")
            with col3:
                if st.button("Remove", key=f"remove_{idx}"):
                    habits.pop(idx)
                    st.warning(f"Removed '{habit['name']}'!")
        save_habits(habits)
