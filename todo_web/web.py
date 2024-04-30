import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My todo app")
st.subheader("A simple todo app")
st.write("made with steamlit")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(
    label="enter a todo",
    placeholder="Add a new todo",
    on_change=add_todo,
    key="new_todo",
)

st.write(st.session_state)
