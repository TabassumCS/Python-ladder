#A list is like a container that holds multiple items in order.

"""Creating a list:
pythonnumbers = [5, 10, 15, 20]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]
Empty list:
pythonmy_list = []
Adding items to a list:
pythonshopping = []
shopping.append("milk")
shopping.append("bread")
print(shopping)  # ['milk', 'bread']
Accessing items by position (index):
pythonfruits = ["apple", "banana", "orange"]
print(fruits[0])  # apple (first item)
print(fruits[1])  # banana (second item)
print(fruits[2])  # orange (third item)
Important: Lists start counting at 0, not 1!
Length of a list:
pythonfruits = ["apple", "banana", "orange"]
print(len(fruits))  # 3
```"""

"""Write a program that:
1. Creates an empty list
2. Asks the user for 3 favorite movies (one at a time)
3. Adds each movie to the list using `append()`
4. Prints the complete list
5. Prints how many movies are in the list using `len()`"""

movies = []
movie1 =input("Enter movie 1: ")
movie2 =input("Enter movie 2: ")
movie3 =input("Enter movie 3: ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(f"{movies}\nYou have {len(movies)} favorite movies")
