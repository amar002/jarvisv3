from utils.data_handler import load_habits

def display_dashboard():
    st.title("Habit Dashboard")
    habits = load_habits()
    
    if not habits:
        st.write("No habits to display. Start your journey by adding goals!")
    else:
        for i, habit in enumerate(habits):
            col1, col2, col3 = st.columns([6, 2, 2])
            with col1:
                st.write(f"📝 {habit['name']} - **{habit['status']}**")
            with col2:
                if st.button("Mark as Done", key=f"done_{i}"):
                    habit["status"] = "Completed"
                    st.success(f"Marked '{habit['name']}' as done!")
            with col3:
                if st.button("Remove", key=f"remove_{i}"):
                    habits.pop(i)
                    st.warning(f"Removed habit: {habit['name']}")
        save_habits(habits)
