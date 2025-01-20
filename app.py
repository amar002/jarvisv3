import streamlit as st
from components.onboarding import interactive_onboarding
from components.dashboard import display_dashboard

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Sidebar navigation menu
st.sidebar.title("HabitFlow Navigation")
menu = st.sidebar.radio(
    "Navigate to:",
    ["Home", "Onboarding", "Dashboard"],
    index=["Home", "Onboarding", "Dashboard"].index(st.session_state.current_page),
    key="menu_navigation",
)

# Update current page in session state
if menu != st.session_state.current_page:
    st.session_state.current_page = menu

# Render the selected page
if st.session_state.current_page == "Home":
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

elif st.session_state.current_page == "Onboarding":
    interactive_onboarding()

elif st.session_state.current_page == "Dashboard":
    display_dashboard()
