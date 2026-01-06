"""Functions (Reusable Code)
A function is a block of code that you can use over and over again without rewriting it."""

"""Creating a simple function:
pythondef greet():
    print("Hello!")
    print("Welcome!")

greet()  # Call the function
greet()  # Call it again
This prints "Hello! Welcome!" twice.
How it works:

def means "define a function"
greet() is the function name
The indented code is what the function does
greet() at the end calls (runs) the function


Functions with parameters (inputs):
def greet(name):
    print(f"Hello, {name}!")

greet("Tabassum")  # Hello, Tabassum!
greet("Sam")       # Hello, Sam!
The function takes name as input and uses it inside.

Functions that return values:
def add(a, b):
    result = a + b
    return result

answer = add(5, 3)
print(answer)  # 8

Important: return gives the value back so you can use it later!

Without return:
def add(a, b):
    result = a + b
    print(result)  # Just shows it

answer = add(5, 3)  # answer is None

With return:

def add(a, b):
    result = a + b
    return result  # Gives it back

answer = add(5, 3)  # answer is 8"""

"""Write a program that:
1. Creates a function called `celsius_to_fahrenheit` that takes `celsius` as a parameter
2. The function calculates fahrenheit using: `(celsius * 9/5) + 32`
3. The function **returns** the result (don't use print inside the function!)
4. Ask the user for a temperature in Celsius
5. Call the function and print the result"""

def celsius_to_fahrenheit(celsius):
    result = (celsius* (9/5)+32)
    return result

celsius = float(input("Enter then temperature in celsius:"))
fahrenheit=celsius_to_fahrenheit(celsius)
print(f"{celsius}C is {fahrenheit}F")
