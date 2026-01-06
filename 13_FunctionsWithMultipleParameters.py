"""Functions with Multiple Parameters
Functions can take more than one input:
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8
Multiple parameters example:
def introduce(name, age, city):
    print(f"My name is {name}, I am {age} years old, and I live in {city}")

introduce("Tabassum", 24, "Manchester")
Functions can return calculations:
def rectangle_area(length, width):
    area = length * width
    return area

result = rectangle_area(5, 3)
print(f"Area: {result}")  # Area: 15
"""

"""
Write a program that:
1. Creates 4 functions: `add()`, `subtract()`, `multiply()`, `divide()`
2. Each function takes 2 parameters (a, b) and returns the result
3. Ask the user for two numbers
4. Call all 4 functions and print the results
"""

def add(a, b):
    result = a+b
    return result

def subtract(a, b):
    result = a-b
    return result

def multiply(a, b):
    result = a*b
    return result

def divide(a, b):
    result = a/b
    return result

a= int(input("Enter a number"))
b= int(input("Enter another number"))


print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {subtract(a, b)}")
print(f"{a} * {b} = {multiply(a, b)}")
print(f"{a} / {b} = {divide(a, b)}")