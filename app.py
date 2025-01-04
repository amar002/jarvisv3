import streamlit as st
from components.onboarding import interactive_onboarding
from components.theme_picker import theme_picker_flow
from components.question_flow import question_flow

# Sidebar menu for navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Menu Options:",
    ["Home", "Onboarding", "Theme Picker", "Question Flow"],
)

# Home Page
if menu == "Home":
    st.title("Welcome to HabitFlow!")
    st.subheader("Your Personal Habit-Building Companion 🚀")
    
    # Multiple headers to introduce sections
    st.markdown("### Why HabitFlow?")
    st.write("""
    HabitFlow helps you build and track habits in a personalized way. Whether you know what you want 
    or need help figuring out your goals, HabitFlow is here to guide you.
    """)

    st.markdown("### How It Works:")
    st.write("""
    1. **Set Your Focus**: Choose a theme like Health, Finance, or Productivity.\n
    2. **Generate Goals**: Get actionable goals using AI.\n
    3. **Track Progress**: Monitor your habits with an interactive dashboard.\n
    4. **Stay Motivated**: Receive personalized tips and reminders.
    """)

    # Highlight key features
    st.markdown("### Key Features:")
    st.write("""
    - AI-powered goal suggestions.
    - Personalized habit tracking.
    - Gamification with scores and badges.
    - Visual insights and reminders.
    """)

    # Add a call-to-action button
    if st.button("Get Started"):
        st.session_state.user_choice = None  # Reset user choice
        st.experimental_rerun()

# Other Pages
elif menu == "Onboarding":
    interactive_onboarding()
elif menu == "Theme Picker":
    theme_picker_flow()
elif menu == "Question Flow":
    question_flow()
