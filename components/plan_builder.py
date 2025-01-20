import streamlit as st
from utils.gemini_api import get_gpt_response

def build_plan(goal):
    """
    Build a detailed plan for the given goal using the Gemini LLM.
    """
    prompt = f"""
    Break down the following goal into a detailed plan with daily, weekly, and monthly milestones. 
    Each milestone should include what to do and the expected outcome at the end of the milestone.

    Goal: {goal}

    Provide the output in this format:
    - Daily Milestones:
        1. [Task and Expected Outcome]
        2. ...
    - Weekly Milestones:
        1. [Task and Expected Outcome]
        2. ...
    - Monthly Milestones:
        1. [Task and Expected Outcome]
        2. ...
    """
    response = get_gpt_response(prompt)
    return response

def plan_builder(goal):
    """
    Streamlit interface for building and displaying the plan.
    """
    st.subheader("Plan Builder")
    st.write(f"**Goal:** {goal}")

    # Generate the plan
    with st.spinner("Building your plan..."):
        plan = build_plan(goal)
    
    # Display the plan
    st.subheader("Your Goal Plan")
    st.write(plan)

    # Accept or Retry options
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Accept Plan"):
            if "habits_data" not in st.session_state:
                st.session_state.habits_data = []
            st.session_state.habits_data.append({"name": goal, "plan": plan, "status": "Pending"})
            st.success("Plan added to your habit list!")
    with col2:
        if st.button("Retry"):
            st.experimental_rerun()
plan_builder.py
python
Copy
Edit
