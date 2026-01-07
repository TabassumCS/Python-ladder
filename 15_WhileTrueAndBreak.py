#Sometimes you want a loop to run until something specific happens, but you don't know when. This is where while True and break are useful!

"""
While True (Infinite Loop):
pythonwhile True:
    print("This runs forever!")
This loop never stops on its own - it needs something to stop it!

Break - Stopping the Loop:
pythonwhile True:
    answer = input("Type 'stop' to exit: ")
    if answer == "stop":
        break  # Exits the loop immediately
    print("Still running...")

print("Loop ended!")
How it works:

while True starts an infinite loop
When the condition is met (answer == "stop"), break exits the loop
Program continues after the loop
"""


"""
Write a program that:
1. Shows a menu with 3 options in a loop:
   - 1: Print "Python is fun"
   - 2: Print "I love coding"
   - 3: Exit
2. Uses `while True` to keep showing the menu
3. Uses `break` to exit when user chooses option 3"""


while True:
    print("\n--- Menu ---")
    print("1: Pyhton is fun")
    print("2: I love coding")
    print("3: Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Python is fun!")
    elif choice == "2":
        print("I love to code!")
    elif choice == "3":
        print("Exiting...")
        break  # Exit the loop
    else:
        print("Invalid option!")

