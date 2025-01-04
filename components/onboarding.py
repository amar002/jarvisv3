import streamlit as st

def interactive_onboarding():
    st.title("Welcome to HabitFlow!")
    st.subheader("Let’s learn more about you to suggest personalized goals and habits.")

    if "user_responses" not in st.session_state:
        st.session_state.user_responses = {}

    if "goals_generated" not in st.session_state or st.session_state.get("retry", False):
        # Additional questions for deeper insights
        st.session_state.user_responses['habit_proud'] = st.text_input("What is one habit you’re proud of and want to continue?")
        st.session_state.user_responses['future_self'] = st.text_area("Where do you see yourself a year from now? (Describe your ideal self)")
        st.session_state.user_responses['strength'] = st.text_input("What’s one skill or strength you excel at?")
        st.session_state.user_responses['habit_challenge'] = st.text_input("What is one habit you struggle to maintain?")
        st.session_state.user_responses['ideal_morning'] = st.text_area("Describe your ideal morning routine.")

        if st.button("Generate My Goals"):
            st.session_state.retry = False
            prompt = (
                f"Based on the following user input, generate 3 personalized goals, explain why they are important, "
                f"and provide a simple plan to achieve each:\n\n"
                f"1. Habit they are proud of: {st.session_state.user_responses['habit_proud']}\n"
                f"2. Ideal self in one year: {st.session_state.user_responses['future_self']}\n"
                f"3. Strength or skill: {st.session_state.user_responses['strength']}\n"
                f"4. Habit they struggle with: {st.session_state.user_responses['habit_challenge']}\n"
                f"5. Ideal morning routine: {st.session_state.user_responses['ideal_morning']}\n\n"
                f"Provide output in this format:\n"
                f"- Goal 1: [Goal]\n"
                f"  Reason: [Why this goal is important]\n"
                f"  Plan: [Simple plan to achieve the goal]\n"
                f"- Goal 2: ...\n"
                f"- Goal 3: ..."
            )
            st.session_state.generated_goals = get_gpt_response(prompt)

    if "generated_goals" in st.session_state and not st.session_state.get("retry", False):
        st.subheader("Here are your personalized goals:")
        st.write(st.session_state.generated_goals)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Accept the Goals"):
                st.session_state.edit_goals = True
        with col2:
            if st.button("Retry"):
                st.session_state.retry = True
                st.session_state.generated_goals = None
                st.experimental_rerun()

    if st.session_state.get("edit_goals", False):
        st.subheader("Edit and Save Your Goals")
        goals = st.session_state.generated_goals.split("- Goal")[1:]
        for i, goal in enumerate(goals, start=1):
            edited_goal = st.text_area(f"Goal {i}:", value=goal.strip())
            st.session_state.habits_data.append({"name": f"Goal {i}: {edited_goal}", "due": "Today", "status": "Pending"})

        if st.button("Save Goals"):
            st.success("Goals added to your habit list!")
            st.session_state.edit_goals = False
            st.experimental_rerun()
