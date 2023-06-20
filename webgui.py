import streamlit as st
import functions
todos = functions.get_todos();
def add_todo():
    get_todo = st.session_state["new_todo"] + '\n'
    todos.append(get_todo)
    functions.write_todos(todos)
    # print(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("Add your todos")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.balloons()
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter your todo",
              on_change=add_todo, key="new_todo")
st.button("Add")
# newly added reset button
if st.button("Reset"):
    todos.clear()
    functions.write_todos(todos)
    st.experimental_rerun()

# st.session_state
