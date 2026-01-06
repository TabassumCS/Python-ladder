"""You can use a for loop to go through each item in a list:
Basic loop through a list:
pythonfruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

This prints:
```
apple
banana
orange
How it works:

The loop takes each item from the list one at a time
Each item is stored in the variable fruit
The code inside runs for each item

With manual numbering:
pythonfruits = ["apple", "banana", "orange"]
count = 1

for fruit in fruits:
    print(f"{count}. {fruit}")
    count += 1
```

This prints:
```
1. apple
2. banana
3. orange
Better way - Using enumerate():
pythonfruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

Same result, but cleaner!

**What is enumerate()?**
- It gives you **two things**: the position number (index) and the item
- `start=1` means start counting from 1 (default is 0)"""


"""
Write a program that:
1. Creates an empty list
2. Asks the user how many items they want to add
3. Uses a **for loop** to ask for each item and add it to the list
4. Prints all items in a numbered list using **enumerate()**"""

shopping = []

number_of_items = int(input("Enter the number of items you want in the list"))

for i in range(number_of_items):
    item = input("Enter item: ")
    shopping.append(item)

print("Your Shopping List:")
for index, item in enumerate(shopping, start=1):
    print(f"{index}. {item}")
