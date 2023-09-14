# Define an empty list to store the to-do items
todo_list = []

# Function to add a new item to the to-do list
def add_item():
    item = input("Enter a new task: ")
    todo_list.append(item)
    print(f"'{item}' has been added to the to-do list.")

# Function to display the current to-do list
def display_list():
    print("\nTo-Do List:")
    for index, item in enumerate(todo_list, start=1):
        print(f"{index}. {item}")

# Function to remove an item from the to-do list
def remove_item():
    display_list()
    if len(todo_list) == 0:
        print("The to-do list is empty.")
    else:
        try:
            choice = int(input("Enter the number of the task to remove: "))
            if 1 <= choice <= len(todo_list):
                removed_item = todo_list.pop(choice - 1)
                print(f"'{removed_item}' has been removed from the to-do list.")
            else:
                print("Invalid choice. Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. View the to-do list")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        display_list()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")