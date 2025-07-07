import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("To-Do List")

new_task = st.text_input("Type a new task:").strip()
if st.button("Add Task"):
    if new_task != "":
        st.session_state.tasks.append((new_task, False))
        st.success("Task added!")
    else:
        st.warning("You must type something!")

st.subheader("Your Tasks:")
remaining_tasks = []
for i, (tasks_text, completed) in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([6, 1, 1])
    with col1:
        checkbox_value = st.checkbox(tasks_text, value=completed, key=f"checkbox_{i}")

    with col2:
        if st.button("Complete", key=f"complete_{i}"):
            st.success(f"✅ Completed: {tasks_text}")
            checkbox_value = True

    with col3:
        if st.button("Remove", key=f"remove_{i}"):
            st.success(f"! Removed: {tasks_text}")
            continue

    remaining_tasks.append((tasks_text, checkbox_value))

st.session_state.tasks = remaining_tasks