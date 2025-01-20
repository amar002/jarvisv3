import streamlit as st
from components.onboarding import interactive_onboarding
from components.dashboard import display_dashboard

# Define a top navigation bar using HTML and CSS
def render_top_nav(current_page):
    nav_html = f"""
    <style>
        .top-nav {{
            background-color: #f8f9fa;
            overflow: hidden;
            border-bottom: 2px solid #ddd;
            display: flex;
            justify-content: space-evenly;
            padding: 10px 0;
        }}
        .top-nav a {{
            text-decoration: none;
            color: #333;
            font-weight: bold;
            padding: 14px 16px;
            transition: 0.3s;
            border-radius: 5px;
        }}
        .top-nav a:hover {{
            background-color: #ddd;
        }}
        .top-nav .active {{
            background-color: #007bff;
            color: white;
        }}
    </style>
    <div class="top-nav">
        <a href="/?page=Home" class="{'active' if current_page == 'Home' else ''}">Home</a>
        <a href="/?page=Onboarding" class="{'active' if current_page == 'Onboarding' else ''}">Onboarding</a>
        <a href="/?page=Dashboard" class="{'active' if current_page == 'Dashboard' else ''}">Dashboard</a>
    </div>
    """
    st.markdown(nav_html, unsafe_allow_html=True)

# Determine the current page based on query parameters
page = st.query_params.get("page", ["Home"])[0]

# Render the top navigation bar
render_top_nav(page)

# Render the corresponding page based on the selected menu item
if page == "Home":
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
        st.experimental_set_query_params(page="Onboarding")
        st.experimental_rerun()

elif page == "Onboarding":
    interactive_onboarding()

elif page == "Dashboard":
    display_dashboard()

else:
    st.error("Page not found! Please use the navigation bar to access other pages.")
