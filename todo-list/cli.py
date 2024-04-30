# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()

        todos.append(todo + "\n")
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index +1}-{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number - 1] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Command not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            todo_removed = todos[number - 1]
            todos.pop(number)

            functions.write_todos(todos)
            print(f"TODO {todo_removed} was removed from the list.")
        except IndexError:
            print("Index not valid")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("command not valid")

print("Exited")
