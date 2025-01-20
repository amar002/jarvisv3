import streamlit as st
from streamlit.components.v1 import html
from components.onboarding import interactive_onboarding
from components.dashboard import display_dashboard

# Define a top navigation bar using HTML and CSS
def render_top_nav():
    nav_html = """
    <style>
        .top-nav {
            background-color: #f8f9fa;
            overflow: hidden;
            border-bottom: 2px solid #ddd;
            display: flex;
            justify-content: space-evenly;
            padding: 10px 0;
        }
        .top-nav a {
            text-decoration: none;
            color: #333;
            font-weight: bold;
            padding: 14px 16px;
            transition: 0.3s;
            border-radius: 5px;
        }
        .top-nav a:hover {
            background-color: #ddd;
        }
        .top-nav .active {
            background-color: #007bff;
            color: white;
        }
    </style>
    <div class="top-nav">
        <a href="#" id="home" onclick="setActive('home')">Home</a>
        <a href="#" id="onboarding" onclick="setActive('onboarding')">Onboarding</a>
        <a href="#" id="dashboard" onclick="setActive('dashboard')">Dashboard</a>
    </div>
    <script>
        function setActive(page) {
            const links = document.querySelectorAll('.top-nav a');
            links.forEach(link => link.classList.remove('active'));
            document.getElementById(page).classList.add('active');
            fetch('/?page=' + page);
        }
    </script>
    """
    html(nav_html, height=70)

# Render the top navigation bar
render_top_nav()

# Determine the active page based on query parameters
page = st.experimental_get_query_params().get("page", ["home"])[0]

# Render the corresponding page
if page == "home":
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
    if st.button("Get Started"):
        st.experimental_set_query_params(page="onboarding")
elif page == "onboarding":
    interactive_onboarding()
elif page == "dashboard":
    display_dashboard()
