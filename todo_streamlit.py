import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("To-Do List")

new_task = st.text_input("Type a new task:")
if st.button("Add Task"):
    if new_task != "":
        st.session_state.tasks.append(new_task)
        st.success("Task added!")
    else:
        st.warning("You must type something!")

st.subheader("Your Tasks:")
remaining_tasks = []
for i, task in enumerate(st.session_state.tasks):
    done = st.checkbox(task, key=i)
    if not done:
        remaining_tasks.append(task)
    else:
        st.success(f"Removed: {task}")

st.session_state.tasks = remaining_tasks