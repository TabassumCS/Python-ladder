"""
Adding items:
pythonfruits = ["apple", "banana"]

# Add to the end
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'orange']

# Add at a specific position
fruits.insert(1, "mango")
print(fruits)  # ['apple', 'mango', 'banana', 'orange']
The insert() takes two parameters: insert(index, item)

Index 0 = first position
Index 1 = second position, etc.


Removing items:
pythonfruits = ["apple", "banana", "orange", "mango"]

# Remove by value (removes first occurrence)
fruits.remove("banana")
print(fruits)  # ['apple', 'orange', 'mango']

# Remove by index (position)
fruits.pop(0)  # Removes first item (index 0)
print(fruits)  # ['orange', 'mango']

# Remove last item
fruits.pop()  # No index = removes last
print(fruits)  # ['orange']
Key differences:

remove("banana") - removes by item name
pop(0) - removes by position (index)
pop() - removes last item


Checking if item exists:
pythonfruits = ["apple", "banana", "orange"]

if "banana" in fruits:
    print("Yes, banana is in the list")

if "mango" not in fruits:
    print("No mango found")"""


"""
Write a program that:
1. Creates an empty todo list
2. Shows a menu with options:
   - 1: Add a task
   - 2: Remove a task
   - 3: View all tasks
   - 4: Exit
3. Uses a **while loop** to keep showing the menu until user chooses to exit
4. Uses **if/elif** to handle each option
"""

todo = []
while True:

    print("\n--- To Do List ---")
    print("1: Add a task")
    print("2: Remove a task (by name)")
    print("3: View all tasks (with numbers using enumerate)")
    print("4: Exit")

    choice  = input("Choose: ")

    if choice == "1":
        task = input("add task:")
        todo.append(task)
        print("Task added!")
        

    elif choice == "2":
        if len(todo) == 0:
            print("No tasks to remove!")
        else:
            print("\nYour tasks:")
            for index, task in enumerate(todo, start=1):
                print(f"{index}. {task}")
            task = input("Enter the task name to remove")
            if task in todo:
                todo.remove(task)
                print("Task removed!")
            else:
                print("Task not found")
    elif choice == "3":
        print("\nYour Tasks:")
        for index, task in enumerate(todo, start=1):
            print(f"{index}. {task}")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")




