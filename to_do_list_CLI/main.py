from modules.func import show_todos, add_todo, print_todos, edit_todo, complete_todo
import time
# from modules import func (func.print_todos() etc .... if there are many functions in file, this is preferred.)

now = time.strftime("%d %b, %Y %H:%M:%S")
print("It is", now)

while True:
    prompt_message = input("Type add, show, edit, complete or exit: ").strip()

    if prompt_message == 'add':
        entry = input("Enter a todo: ") + "\n"
        items = show_todos(entry)
        add_todo(items)
    elif prompt_message == 'show' or prompt_message == "display":
        print_todos()
    elif prompt_message == 'edit':
        todos = print_todos()
        number = int(input("Number of todo to edit: "))
        new_todo = input("Enter new todo: ")
        edit_todo(number, new_todo)
    elif prompt_message == 'complete':
        print_todos()
        number = int(input("Number of todo to complete: "))
        complete_todo(number)
    elif prompt_message == 'exit':
        break
    else:
        print("Invalid input! Try again")

print("Bye!")