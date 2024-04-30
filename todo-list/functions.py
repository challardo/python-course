FILE_PATH = "todos.txt"


def get_todos(filepath=FILE_PATH):
    """
    Read the text file and return the list of todo items.
    """
    with open(filepath, "r") as file:
        return file.readlines()


def write_todos(todos_arg, filepath=FILE_PATH):
    """
    write the todo items list in the text file.
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
