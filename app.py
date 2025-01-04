import streamlit as st
from components.onboarding import interactive_onboarding
from components.dashboard import display_dashboard
from components.suggestions import display_chat
from components.reminders import display_reminder_options
from utils.data_handler import load_habits, save_habits

# Initialize session state
if "habits_data" not in st.session_state:
    st.session_state.habits_data = load_habits()

st.title("HabitFlow")
st.subheader("Build small habits, achieve big goals.")

# Navigation menu
menu = st.radio(
    "Navigate:",
    ["Onboarding", "Dashboard", "Suggestions", "Reminders"],
    horizontal=True
)

if menu == "Onboarding":
    interactive_onboarding()
elif menu == "Dashboard":
    display_dashboard()
elif menu == "Suggestions":
    display_chat()
elif menu == "Reminders":
    display_reminder_options()

# Save data on app exit
save_habits(st.session_state.habits_data)
