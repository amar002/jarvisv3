import streamlit as st
from components.onboarding import interactive_onboarding
from components.dashboard import display_dashboard

# Sidebar navigation menu
st.sidebar.title("HabitFlow Navigation")
menu = st.sidebar.radio(
    "Navigate to:",
    ["Home", "Onboarding", "Dashboard"]
)

# Home Page
if menu == "Home":
    st.title("Welcome to HabitFlow!")
    st.subheader("Your Personal Habit-Building Companion 🚀")
    
    st.markdown("### Why HabitFlow?")
    st.write("""
    HabitFlow helps you build and track habits in a personalized way. Whether you know your goals 
    or need help identifying them, HabitFlow guides you every step of the way.
    """)

    st.markdown("### How It Works:")
    st.write("""
    1. **Set Your Goals**: Use AI to define and refine your goals.\n
    2. **Build a Plan**: Break goals into actionable steps with clear milestones.\n
    3. **Track Progress**: Use the dashboard to monitor and update your progress.\n
    4. **Achieve More**: Stay motivated with progress tracking and completion rewards.
    """)

    # Call to Action
    if st.button("Get Started"):
        st.session_state.current_page = "Onboarding"
        

# Onboarding
elif menu == "Onboarding":
    interactive_onboarding()

# Dashboard
elif menu == "Dashboard":
    display_dashboard()
