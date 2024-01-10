FILEPATH = "./data/todos.txt"


def print_todos():
    """ Read file and print todos """
    with open(FILEPATH, 'r') as f:
        items_local = f.readlines()
        for index, item in enumerate(items_local):
            print(f"{index + 1}-{item}", end='')
    return items_local


def add_todo(user_entry):
    show_todos(user_entry)
    with open(FILEPATH, 'w') as f:
        f.writelines(user_entry)


def show_todos(user_entry=None):
    with open(FILEPATH, 'r') as f:
        items_local = f.readlines()
        if user_entry:
            items_local.append(user_entry)
    return items_local


def edit_todo(num, todo):
    items_local = show_todos()
    items_local[num - 1] = todo + "\n"
    add_todo(items_local)
    print_todos()


def complete_todo(num):
    items_local = show_todos()
    try:
        removed_todo = items_local.pop(num - 1)
        add_todo(items_local)
        print(f"Todo {removed_todo.strip()} was successfully removed!")
    except IndexError:
        print("Record does not exists")


# FOR LOCAL TESTING func.py filename
if __name__ == "__main__":
    print(print_todos())
